#!/usr/bin/env python3
"""Tracker N3, tier 1: works cited on guide pages that cover a cluster, for the site (automatic, not checked).

usage (from repo/): uv run -q --with pyyaml python -I scripts/refs/guide_cited_refs.py [--n3 DIR] [--quiet]
build_site.py runs it at the start of every build when research/references/n3/ is there, so a new batch of Codex
judgments needs only a rebuild. Without research/ the build reads the two files below as committed.

Reads (research/references/n3/, read only; see SPEC.md there):
  candidates.tsv, candidates-priority.tsv   one row per (guide page, cluster, citation); tier 1 = a blueprint \\cite or
                                            a page that covers at most 4 clusters
  refs.tsv                                  the works, resolved with Crossref and arXiv where possible
  out/accepted-judgments.jsonl              Codex's judgments that passed the checker (one per candidate)
  merge.py                                  turns the 'supports' judgments into spine-format references
Writes (only when the content changes, so a rebuild with the same inputs leaves both files alone):
  data/guide-cited-refs.tsv   one row per (cluster, work): the tier-1 candidates that no judgment overrides.
      cluster   cluster id
      ref_id    id of the work in refs.tsv
      n_guides  distinct guides that cite the work on a page covering the cluster (the site orders by it)
      citation  plain-text citation: Crossref or arXiv metadata when resolve_status is matched, else the guide's
                bibliography entry, cleaned (an ambiguous match never lends its DOI)
      url       https://doi.org/<doi> or https://arxiv.org/abs/<id> (matched only, or printed in the entry), or empty
      cited_on  the citing pages, 'guide|page|page_url' joined with ';' (page as in candidates.tsv)
  data/references-n3.yaml     merge.py's output (spine format), its n3: true entries re-cited by the rule above; the site
                              shows those entries as checked references, with their precision
Left out: entries from 2026 with no published record (other guides, GitHub issues, the joint statement, forum
threads): they are notes on this proof, not literature for a cluster.
Judgments override the automatic rows: any 'supports' for a (cluster, work) moves it to the checked references (via
merge.py) and drops the row; otherwise any 'context-only' or 'unrelated' drops the row; 'unsure' or no judgment keeps it.
"""
import argparse, csv, html, json, os, re, subprocess, sys, tempfile, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.dirname(REPO)
OUT_DIR = os.environ.get('_RH_SITE_STAGE_STATE', os.path.join(REPO, 'data'))
OUT_TSV = os.path.join(OUT_DIR, 'guide-cited-refs.tsv')
OUT_YAML = os.path.join(OUT_DIR, 'references-n3.yaml')
COLS = ['cluster', 'ref_id', 'n_guides', 'citation', 'url', 'cited_on']


def read_tsv(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE))


# ---------- citation text
_ACC = {'´': '\u0301', 'ˇ': '\u030c', '`': '\u0300', '¨': '\u0308', '˝': '\u030b'}
def tidy(s):
    """Plain text from a bibliography or Crossref string: entities, tags, TeX, PDF accent splits, hyphen breaks."""
    s = s.replace('\\n', ' ')
    for _ in range(2):
        s = html.unescape(s)
    s = re.sub(r'(?<=\w)<(?:i|b|em|scp)>', ' ', s)                       # 'abelian<i>L</i>' -> 'abelian L'
    s = re.sub(r'</?(?:i|b|em|sup|sub|scp|mml:[a-z]+)[^>]*>', '', s)
    s = re.sub(r'\\+', '\\\\', s)                                        # TSV-doubled backslashes
    s = re.sub(r'\{\\(?:germ|frak|mathfrak)\s*(\w)\}', r'\1', s)
    s = re.sub(r'\\(?:mathrm|mathbf|mathbb|mathfrak|mathcal|operatorname|rm|bf|it|emph|textit|textrm|text)\s*\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:rm|bf|it|germ|frak)\s+', '', s)
    s = re.sub(r'\\([a-zA-Z]+)', lambda m: {'mu': 'μ', 'lambda': 'λ', 'zeta': 'ζ', 'ell': 'ℓ', 'chi': 'χ', 'pi': 'π',
                                           'Gamma': 'Γ', 'theta': 'θ', 'infty': '∞', 'times': '×', 'le': '≤',
                                           'leq': '≤', 'ge': '≥', 'geq': '≥', 'sigma': 'σ'}.get(m.group(1), ''), s)
    s = s.replace('$', '').replace('{', '').replace('}', '').replace('\\', '')
    s = re.sub(r'([´ˇ`¨˝])\s?([A-Za-z])', lambda m: m.group(2) + _ACC[m.group(1)], s)   # 'Slijepˇcevi´c' -> 'Slijepčević'
    s = re.sub(r'([aeAE])¸', lambda m: m.group(1) + '\u0328', s)                         # 'Naskre¸cki' -> 'Naskręcki'
    s = re.sub(r'([A-Za-z])¸', lambda m: m.group(1) + '\u0327', s)
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'(?<=[a-z]{3})([A-Z])(?=-[a-z])', r' \1', s)   # a tag dropped upstream: 'abelianL-functions'
    s = re.sub(r'(\w)- ([a-z])', r'\1\2', s)      # line-break hyphen: 'Mathe- matics'
    s = re.sub(r'(\w)- ([A-Z])', r'\1-\2', s)     # 'Heath- Brown'
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'\s+([,.;:])', r'\1', s)


def names(authors):
    out = []
    for a in [x.strip() for x in authors.split(';') if x.strip()]:
        fam, sep, given = a.partition(',')
        out.append(f'{given.strip()} {fam.strip()}'.strip() if sep else a)
    if len(out) > 4:
        return ', '.join(out[:3]) + ' et al.'
    return ', '.join(out[:-1]) + ' and ' + out[-1] if len(out) > 1 else (out[0] if out else '')


def venue(v, year):
    """Crossref venue 'Journal; Publisher 45, 375-401' -> 'Journal 45 (1995), 375–401'; a book: its series or publisher."""
    v = tidy(v)
    cont, sep, rest = v.partition('; ')
    if not sep:
        cont, rest = '', v
    m = re.match(r'^(.*?)(?:\s+(\d[\w.]*))?(?:,\s*([\dA-Za-z]+-[\dA-Za-z]+|\d+))?$', rest)
    pub, vol, pages = (m.group(1), m.group(2), m.group(3)) if m else (rest, None, None)
    if re.fullmatch(r'arXiv:\S+', v):
        return v, False
    head = cont or pub
    if vol and cont:
        head += f' {vol}'
    head += f' ({year})' if year else ''
    if pages:
        head += ', ' + pages.replace('-', '–')
    return head, True


# extraction damage in a Crossref title (math lost its markup): a word glued to '=' ('forl=p'), a Greek letter split
# from its subscript ('μ p'), a hyphen word missing its first letter ('reducible -adic', 'p -adic'), a capital glued
# to the word before it ('abelianL-functions'). Such a title is not shown: the guide's own entry is used instead,
# with the matched record's link kept.
_DAMAGE = re.compile(r'[A-Za-z]{3,}=|[\u03b1-\u03c9\u0391-\u03a9] [a-z]\b|(?:^|\s)-[a-z]|\b[A-Za-z] -[a-z]|[a-z]{3}[A-Z]-[a-z]')
DAMAGED = []   # ref_ids whose Crossref title was replaced by the guide's entry (printed by --damaged)
def damaged(r):
    return bool(_DAMAGE.search(tidy(r['title']))) or bool(re.search(r'[a-z]{3}[A-Z]-[a-z]', r['title']))


def citation(r):
    """(text, url). Matched: authors, title, venue, year from the record, DOI or arXiv link. Else the guide's entry."""
    if r['resolve_status'] == 'matched' and damaged(r):
        DAMAGED.append(r['ref_id']) if r['ref_id'] not in DAMAGED else None
        txt, _ = citation({**r, 'resolve_status': 'raw'})
        return txt, f'https://doi.org/{r["doi"]}' if r['doi'] else f'https://arxiv.org/abs/{r["arxiv"]}' if r['arxiv'] else ''
    if r['resolve_status'] == 'matched' and r['authors'].strip() and r['title'].strip():
        au, ti = names(tidy(r['authors'])), tidy(r['title']).rstrip('.:; ')
        ve, has_year = venue(r['venue'], r['year']) if r['venue'].strip() else (f'({r["year"]})' if r['year'] else '', True)
        txt = ', '.join(x for x in (au, ti, ve) if x)
        if not has_year and r['year']:
            txt += f' ({r["year"]})'
        url = f'https://doi.org/{r["doi"]}' if r['doi'] else f'https://arxiv.org/abs/{r["arxiv"]}' if r['arxiv'] else ''
        return txt, url
    raw = tidy(r['raw_entry'])
    raw = re.sub(r'^\[[^\]]{1,20}\]\s*', '', raw)            # a label printed before the entry
    raw = re.sub(r'^\d{1,3}\.\s+', '', raw)
    # a link only when the entry itself prints the DOI or arXiv id (never the DOI of an ambiguous record)
    m = re.search(r'\b(?:doi(?:\.org)?[:/]\s*)(10\.\d{4,9}/\S+?)[.,;)]?(?:\s|$)', raw, re.I)
    a = re.search(r'arXiv:\s*(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})', raw)
    url = f'https://doi.org/{m.group(1)}' if m else f'https://arxiv.org/abs/{a.group(1)}' if a else ''
    return raw, url


# ---------- rows
def build(n3, quiet=False):
    C = {r['cand_id']: r for r in read_tsv(os.path.join(n3, 'candidates.tsv'))}
    tier = {r['cand_id']: r['tier'] for r in read_tsv(os.path.join(n3, 'candidates-priority.tsv'))}
    R = {r['ref_id']: r for r in read_tsv(os.path.join(n3, 'refs.tsv'))}
    jf = os.path.join(n3, 'out', 'accepted-judgments.jsonl')
    J = {}
    if os.path.exists(jf):
        for line in open(jf, encoding='utf-8'):
            line = line.strip()
            if line:
                try:
                    j = json.loads(line)
                except ValueError:
                    continue
                if j.get('cand_id') in C:
                    J[j['cand_id']] = j          # last line wins, as in merge.py
    verdicts = collections.defaultdict(set)      # (cluster, ref_id) -> verdicts of its judged candidates (any tier)
    for cid, j in J.items():
        verdicts[(C[cid]['cluster'], C[cid]['ref_id'])].add(j.get('verdict'))
    groups = collections.OrderedDict()
    st = collections.Counter()
    for cid, c in C.items():
        if tier.get(cid) == '1' and c['ref_id'] in R:
            r = R[c['ref_id']]
            if r['year'] >= '2026' and r['resolve_status'] != 'matched':   # notes on the 2026 proof itself (other guides,
                st['left out (2026 notes on the proof, not literature)'] += 1   # issues, statements, forum threads)
                continue
            groups.setdefault((c['cluster'], c['ref_id']), []).append(c)
    rows = []
    for (k, rid), cs in groups.items():
        v = verdicts.get((k, rid), set())
        if 'supports' in v:
            st['moved to checked (supports)'] += 1; continue
        if v & {'context-only', 'unrelated'}:
            st['dropped (context-only or unrelated)'] += 1; continue
        txt, url = citation(R[rid])
        seen, cited = set(), []
        for c in cs:
            key = (c['guide'], c['page'])
            if key in seen:
                continue
            seen.add(key)
            for x in (c['page'], c['page_url']):
                assert '|' not in x and ';' not in x and '\t' not in x, (cid, x)
            cited.append(f'{c["guide"]}|{c["page"]}|{c["page_url"]}')
        rows.append({'cluster': k, 'ref_id': rid, 'n_guides': str(len({c['guide'] for c in cs})),
                     'citation': txt.replace('\t', ' '), 'url': url, 'cited_on': ';'.join(cited)})
        st['kept'] += 1
    rows.sort(key=lambda r: (r['cluster'], -int(r['n_guides']), -r['cited_on'].count(';'), r['citation'].lower()))
    body = '\t'.join(COLS) + '\n' + ''.join('\t'.join(r[c] for c in COLS) + '\n' for r in rows)
    changed = write_if_changed(OUT_TSV, body)
    # merge.py: the supports judgments in spine format (to a temporary file, copied when more than its date changed)
    with tempfile.TemporaryDirectory() as td:
        tmp = os.path.join(td, 'references-n3.yaml')
        args = [sys.executable, '-I', os.path.join(n3, 'merge.py'), '--out', tmp]
        if os.path.exists(jf):
            args.insert(3, jf)
        else:
            open(os.path.join(td, 'none.jsonl'), 'w').close(); args.insert(3, os.path.join(td, 'none.jsonl'))
        p = subprocess.run(args, capture_output=True, text=True)
        if p.returncode:
            sys.exit(f'guide_cited_refs: merge.py failed:\n{p.stderr}')
        new = open(tmp, encoding='utf-8').read()
    new = recite(new, C, R)
    old = open(OUT_YAML, encoding='utf-8').read() if os.path.exists(OUT_YAML) else None
    undated = lambda s: re.sub(r'(?m)^  written: .*$', '', s or '')
    ychanged = old is None or undated(old) != undated(new)
    if ychanged:
        open(OUT_YAML, 'w', encoding='utf-8').write(new)
    if not quiet:
        print(f'guide-cited refs (N3 tier 1): {len(rows)} rows, {len({r["cluster"] for r in rows})} clusters; '
              f'judgments read {len(J)}; ' + ', '.join(f'{n} {k}' for k, n in st.items() if k != 'kept')
              + f'; {"written" if changed else "unchanged"} data/guide-cited-refs.tsv, '
              f'{"written" if ychanged else "unchanged"} data/references-n3.yaml')
    return rows


def recite(text, C, R):
    """The n3: true entries of merge.py's output get the same citation text and link rule as the automatic rows
    (Crossref metadata only when matched; an ambiguous record lends no DOI). Spine entries are left as they are."""
    import yaml
    y = yaml.safe_load(text)
    for c in y.get('clusters') or []:
        for r in c.get('references') or []:
            if not r.get('n3'):
                continue
            rid = next((C[x]['ref_id'] for x in r.get('cand_ids') or [] if x in C), None)
            if rid not in R:
                continue
            txt, url = citation(R[rid])
            r['citation'], r['url'] = txt, url
            if R[rid]['resolve_status'] == 'matched' and R[rid]['doi']:
                r['doi'] = R[rid]['doi']
            else:
                r.pop('doi', None)
    return yaml.safe_dump(y, sort_keys=False, allow_unicode=True, width=200, default_flow_style=False)


def write_if_changed(path, body):
    if os.path.exists(path) and open(path, encoding='utf-8').read() == body:
        return False
    open(path, 'w', encoding='utf-8').write(body)
    return True


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--n3', default=os.path.join(ROOT, 'research', 'references', 'n3'))
    ap.add_argument('--quiet', action='store_true')
    ap.add_argument('--damaged', action='store_true', help='list the matched titles replaced by the guide entry')
    a = ap.parse_args()
    build(a.n3, a.quiet)
    if a.damaged:
        R = {r['ref_id']: r for r in read_tsv(os.path.join(a.n3, 'refs.tsv'))}
        for rid in sorted(DAMAGED):
            print(f'{rid}\t{tidy(R[rid]["title"])}\t->\t{citation(R[rid])[0]}')
