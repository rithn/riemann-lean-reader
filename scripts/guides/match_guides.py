"""Deterministic page-level links from outside guides to the map's clusters (guides-design.md section 5 step 2).

usage: uv run --no-project --with pymupdf python -I match_guides.py <sources dir> <xref dir> <site modules.json>
                                                                    <lean src tree> <out dir> [<summary.json>] [--decls=<file>]

<sources dir>   research/guides/sources (pinned copies; read as data, nothing in it is run)
<xref dir>      research/lean-reader/xref (decls.tsv.gz, blueprint_matches.tsv)
<out dir>       repo/data/guide-refs: writes <guide id>.tsv with columns cluster, page, page_url, basis, evidence

A page is a PDF page (pymupdf, 1-based, page_url = PDF url + #page=N), one saved web page (page_url = its URL),
a repository file (page_url = GitHub blob URL at the pinned commit) or one blueprint statement / atlas entry.

Per page the script finds, in this order of strength (one row per cluster per page, strongest basis kept):
  exact-name       a project declaration's full name (decls.tsv.gz, commit 40e56bab). Dotted names are taken
                   as written, or their longest dotted prefix that is a declaration (`A.b.le` -> `A.b`).
                   Names without a dot count only if they have an underscore or an inner capital and >= 6
                   characters; a private one only if the same page names its file (last module part).
                   Names declared in modules of more than one cluster are skipped.
  exact-path       a path to a file of the archive (`lean/src/A/B.lean` or `A/B.lean` from a top folder),
                   also inside GitHub URLs; for Jaswal after expanding the folder abbreviations of his p. 7.
  exact-module     a module name `A.B.C` that is a file of the archive
  unique-filename  a bare `C.lean`, or a partial path (`.../B/C.lean`), that ends exactly one file's path
  blueprint-label  a statement of Merten's blueprint or an entry of Naskręcki's atlas whose Lean name was
                   matched by repo/scripts/xref/blueprints.py (blueprint_matches.tsv)
Text is read three ways and the hits pooled: as extracted; with line breaks joined next to `.`, `/`, `_` and
after a hyphen; and with every line break between two non-space characters removed. Ligatures, soft hyphens,
zero-width spaces and `’` (as Lean's prime) are normalised. Mathlib names are not in decls.tsv and never match.
Module -> cluster as the site does it: site/data/modules.json rows (folder index, leaf, cluster number).

Manual rows: a row whose basis starts with `manual-` (e.g. `manual-certifies-main`) is written by hand into
<out dir>/<guide id>.tsv and kept on every rerun: the script reads them back before rewriting the file and appends
them after its own rows (a script row for the same cluster and page is dropped in favour of the manual one).
The build treats them like any other row.

url_names (tamnd only): a web page whose address names a declaration (`code/decl/?n=<full name>`) is matched on
that name too; the saved HTML of those pages is an empty shell filled in by the site's script, so the address is
the only text that names the declaration.
"""
import os, sys, re, csv, json, gzip, html, collections, glob, urllib.parse

_args = [a for a in sys.argv[1:] if not a.startswith('--decls=')]
src_dir, xref, modules_json, tree, out_dir = _args[:5]
summary_path = _args[5] if len(_args) > 5 else None
# --decls=<file>: also write every cited declaration and file, unshortened (the evidence column keeps only 4 per
# row, then '+N more'): guide, cluster, page, kind (d = declaration, f = file), name or module, declaring module
DECLS_OUT = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--decls=')), None)
DECL_ROWS = set()
import pymupdf

# ---------------- reference data ----------------
mj = json.load(open(modules_json))
mod_cl = {(f"{mj['folders'][a]}.{b}" if mj['folders'][a] else b): 'k%04d' % k for a, b, k in mj['rows']}

files = []                       # archive paths relative to lean/src, e.g. Development/X/Y.lean
for root, _, fs in os.walk(tree):
    for f in fs:
        if f.endswith('.lean'):
            files.append(os.path.relpath(os.path.join(root, f), tree))
file_set = set(files)
modules = {f[:-5].replace('/', '.') for f in files}
by_base = collections.defaultdict(list)
for f in files:
    by_base[os.path.basename(f)].append(f)
TOP = sorted({f.split('/')[0] for f in files})

decl_mods = collections.defaultdict(set)
private = set()
with gzip.open(os.path.join(xref, 'decls.tsv.gz'), 'rt', encoding='utf-8') as fh:
    next(fh)
    for ln in fh:
        n, mod, line, k, fl = ln.rstrip('\n').split('\t')
        decl_mods[n].add(mod)
        if 'p' in fl:
            private.add((n, mod))

# ---------------- guides ----------------
# Jaswal v2, p. 7: "DA Development/AutomorphicArithmetic, AVT ..., A path beginning .../ omits its leading folders"
JASWAL_ABBR = {
    'DA': 'Development/AutomorphicArithmetic', 'AVT': 'Development/AbelianVarietyTheory',
    'CB': 'DA/CharacterBoxes', 'WB': 'Development/WeilBound', 'PC': 'DA/PrimitiveCosets',
    'FSR': 'Formalism/SharpRestriction', 'LT': 'DA/DedekindLFunctions/LandauTheorems',
    'FLG': 'Formalism/LocalToGlobal', 'TPS': 'DA/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries',
    'TGC': 'FSR/RamificationFrobenius/TotientGaloisClasses', 'AV': 'DA/AutomorphicVarieties',
    'GTI': 'FSR/GlobalTheoremInputs.lean', 'SWB': 'Formalism/SizeWindowBrackets',
    'LRC': 'Formalism/LocalRingCardinality'}


def expand_abbr(abbr):
    full = {}
    for k in abbr:
        v = abbr[k]
        for _ in range(4):
            v = re.sub(r'^([A-Z]+)(?=/|$)', lambda m: abbr.get(m.group(1), m.group(1)), v)
        full[k] = v
    return full


JASWAL = expand_abbr(JASWAL_ABBR)
for k, v in JASWAL.items():
    assert os.path.exists(os.path.join(tree, v)), (k, v)

manifest = {}
with open(os.path.join(src_dir, 'manifest.tsv')) as fh:
    for r in csv.DictReader(fh, delimiter='\t'):
        manifest.setdefault(r['id'], []).append(r)


def commit_of(gid):
    return next(r['version'] for r in manifest[gid] if r['file'].endswith('repo'))


def web_pages(d):
    if not os.path.exists(os.path.join(d, 'pages.tsv')):
        return []
    with open(os.path.join(d, 'pages.tsv')) as fh:
        return [(os.path.join(d, r['file']), r['final_url']) for r in csv.DictReader(fh, delimiter='\t')]


GUIDES = {
    'rubinstein-zeta-guide': {'pdf': [('rubinstein-zeta-guide/zeta-paper_v2.pdf',
                              'https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf')],
                              'web': ['rubinstein-zeta-guide']},
    'sutherland-grh-verification': {'web': ['sutherland-grh-verification']},
    'lean-community-statement': {'web': ['lean-community-statement']},
    'jaswal-zenodo-guide': {'pdf': [('jaswal-zenodo-guide/v2.pdf', 'https://zenodo.org/records/24432579/files/'
                            'jaswal-rh-dirichlet-after-alpoge.pdf')], 'web': ['jaswal-zenodo-guide'],
                            'abbr': JASWAL},
    'adriazola-reconstruction': {'pdf': [('adriazola-reconstruction/repo/manuscript/main.pdf', 'GH:manuscript/main.pdf')],
                                 'repo': ('adriazola-reconstruction/repo', 'jimjamzola/RH-Alpoge-Reconstruction', '*.md')},
    # older version (67 pages, 21 Nov, the one the 23 Nov mapping read), kept apart: written to <summary dir>
    'adriazola-reconstruction@route-notes': {'pdf': [('adriazola-reconstruction/repo/RH_Route_Notes.pdf', 'GH:RH_Route_Notes.pdf')],
                                             'repo_of': 'adriazola-reconstruction', 'side': True},
    'naskrecki-riemann-rev': {'web': ['naskrecki-riemann-rev/site'],
                              'pdf': [(f'naskrecki-riemann-rev/site/pdfs/{p.replace("/", "_")}',
                                       f'https://nasqret.github.io/riemann-rev/{p}')
                                      for p in ('guide/proof-guide.pdf', 'blueprint/atlas-blueprint.pdf',
                                                'digests/layer-descent.pdf', 'digests/local-nilpotence.pdf',
                                                'digests/tower-bound.pdf')],
                              'labels': ('naskrecki', lambda lab: ('atlas#' + lab, 'https://nasqret.github.io/riemann-rev/atlas/'))},
    'merten-riemann-blueprint': {'labels': ('merten', lambda lab: ('object/' + lab, 'https://riemann.fuxi.merten.dev/#/object/' + lab))},
    'rubinstein-grh-lean-verification': {'web': ['rubinstein-grh-lean-verification']},
    'baez-azimuth-masullo': {'web': ['baez-azimuth-masullo']},
    'aaronson-shtetl-optimized': {'web': ['aaronson-shtetl-optimized']},
    'tamnd-riemann-handbook': {'web': ['tamnd-riemann-handbook', 'tamnd-riemann-handbook/more'], 'url_names': True},
}

# ---------------- text ----------------
LIG = {'ﬀ': 'ff', 'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬃ': 'ffi', 'ﬄ': 'ffl', 'ﬅ': 'st', 'ﬆ': 'st',
       '­': '', '​': '', '‌': '', '‍': '', '⁠': '', '﻿': '', '’': "'",
       '‑': '-', '‐': '-', '∕': '/', '…': '...', ' ': ' '}
LIG_RE = re.compile('|'.join(map(re.escape, LIG)))


def html_text(raw):
    t = re.sub(r'(?is)<!--.*?-->', ' ', raw)
    t = re.sub(r'(?is)<style\b.*?</style>', ' ', t)
    attrs = re.findall(r'''(?i)\b(?:href|src|title|data-[\w-]+)\s*=\s*["']([^"']*)["']''', t)
    t = re.sub(r'(?i)<wbr\s*/?>', '', t)
    t = re.sub(r'(?i)<(br|/p|/div|/li|/tr|/h\d|/pre|/td|/th)\b[^>]*>', '\n', t)
    t = re.sub(r'(?s)<[^>]+>', ' ', t)
    return html.unescape(t + '\n' + '\n'.join(attrs))


def variants(t):
    t = LIG_RE.sub(lambda m: LIG[m.group(0)], t)
    v1 = re.sub(r'(?<=[./_])[ \t]*\n[ \t]*|[ \t]*\n[ \t]*(?=[./_])', '', t)
    v1 = re.sub(r'(?<=\w)-[ \t]*\n[ \t]*(?=\w)', '', v1)
    v2 = re.sub(r'(?<=\S)[ \t]*\n[ \t]*(?=\S)', '', v1)
    return [('', t), (' (line-joined)', v1), (' (lines joined)', v2)]


IDENT = r"[^\W\d][\w'!?]*"
NAME_RE = re.compile(rf"(?<![\w'./]){IDENT}(?:\.{IDENT})*")
PATH_RE = re.compile(r"(?:(?:\.\.\.|…)\s?/)?(?:[\w'.\-]+/)*[\w'\-]+\.lean\b")
CAMEL = re.compile(r'[a-z0-9][A-Z]|_')

RANK = {'exact-name': 0, 'exact-path': 1, 'exact-module': 2, 'unique-filename': 3, 'blueprint-label': 4}


def cluster_of_module(m):
    return mod_cl.get(m)


def find_hits(text, abbr=None):
    """-> list of (cluster, basis, evidence)"""
    hits, skipped = [], collections.Counter()
    seen = set()
    for tag, t in variants(text):
        if abbr:
            # folder abbreviations only before '/', file abbreviations (ending .lean) anywhere as a word
            t = re.sub(r'(?<![\w/.])(' + '|'.join(sorted(abbr, key=len, reverse=True)) + r')(?=/|\b)',
                       lambda m: abbr[m.group(1)] if abbr[m.group(1)].endswith('.lean') or
                       t[m.end():m.end() + 1] == '/' else m.group(1), t)
        # paths
        for m in PATH_RE.finditer(t):
            p = m.group(0)
            key = ('p', p)
            if key in seen:
                continue
            seen.add(key)
            q = p.split('lean/src/', 1)[1] if 'lean/src/' in p else p
            partial = bool(re.match(r'(?:\.\.\.|…)', q))
            q = re.sub(r'^(?:\.\.\.|…)\s?/', '', q)
            if not partial and q in file_set and ('/' in q or 'lean/src/' in p):
                c = cluster_of_module(q[:-5].replace('/', '.'))
                if c:
                    hits.append((c, 'exact-path', p + tag, ('f', q[:-5].replace('/', '.'))))
                else:
                    skipped['path without cluster'] += 1
                continue
            cands = [f for f in by_base.get(os.path.basename(q), []) if f == q or f.endswith('/' + q)]
            if len(cands) == 1:
                c = cluster_of_module(cands[0][:-5].replace('/', '.'))
                if c:
                    hits.append((c, 'unique-filename', f'{p} -> {cands[0]}{tag}', ('f', cands[0][:-5].replace('/', '.'))))
            elif len(cands) > 1:
                skipped['file name not unique'] += 1
            else:
                skipped['path not in archive'] += 1
        # names and modules
        for m in NAME_RE.finditer(t):
            tok = m.group(0)
            key = ('n', tok)
            if key in seen:
                continue
            seen.add(key)
            if tok.endswith('.lean'):
                continue
            parts = tok.split('.')
            if len(parts) > 1 and tok in modules:
                c = cluster_of_module(tok)
                if c:
                    hits.append((c, 'exact-module', tok + tag, ('f', tok)))
                continue
            for k in range(len(parts), 0, -1):
                n = '.'.join(parts[:k])
                if n in decl_mods:
                    if k == 1 and not (len(n) >= 6 and CAMEL.search(n)):
                        break
                    mods = decl_mods[n]
                    if k == 1 and all((n, x) in private for x in mods):
                        # a private name is only usable inside its file: count it only if the page also
                        # names that file (its last module component as a word)
                        mods = {x for x in mods if re.search(r'(?<![\w])' + re.escape(x.rsplit('.', 1)[-1])
                                                             + r'(?![\w])', t)}
                        if not mods:
                            skipped['private short name, file not named on page'] += 1
                            break
                    cls = {cluster_of_module(x) for x in mods} - {None}
                    if len(cls) == 1:
                        hits.append((cls.pop(), 'exact-name', n + tag, ('d', n, sorted(mods)[0] if len(mods) == 1 else '')))
                    elif len(cls) > 1:
                        skipped['name in several clusters'] += 1
                    break
                if k > 1 and '.'.join(parts[:k]) in modules:
                    break
    return hits, skipped


def merge_rows(page_hits):
    """page_hits: {(page, url): [(cluster, basis, evidence)]} -> rows"""
    rows = []
    for (page, url), hs in page_hits.items():
        per = collections.defaultdict(list)
        for c, b, e, *_ in hs:
            per[c].append((RANK[b], b, e))
        for c, lst in per.items():
            lst.sort()
            best = lst[0][1]
            ev = []
            for _, b, e in lst:
                if e not in ev:
                    ev.append(e)
            evs = '; '.join(ev[:4]) + (f'; +{len(ev) - 4} more' if len(ev) > 4 else '')
            rows.append((c, page, url, best, evs))
    return rows


# blueprint labels
bm = collections.defaultdict(list)
with open(os.path.join(xref, 'blueprint_matches.tsv')) as fh:
    for r in csv.DictReader(fh, delimiter='\t'):
        if r['status'] == 'matched' and r['cluster']:
            bm[r['source']].append(r)

os.makedirs(out_dir, exist_ok=True)
summary = {}
for gid, g in GUIDES.items():
    page_hits = collections.OrderedDict()
    scanned = collections.Counter()
    skipped = collections.Counter()
    abbr = g.get('abbr')

    def add(page, url, text):
        h, s = find_hits(text, abbr)
        skipped.update(s)
        page_hits[(page, url)] = h

    for rel, url in g.get('pdf', []):
        if url.startswith('GH:'):
            rg = g.get('repo_of', gid)
            url = f"https://github.com/{GUIDES[rg]['repo'][1]}/blob/{commit_of(rg)}/{url[3:]}"
        doc = pymupdf.open(os.path.join(src_dir, rel))
        tag = '' if len(g.get('pdf', [])) == 1 else os.path.basename(url) + ' '
        for i, pg in enumerate(doc):
            add(f'{tag}p. {i + 1}', f'{url}#page={i + 1}', pg.get_text())
            scanned['pdf pages'] += 1
    for d in g.get('web', []):
        for path, url in web_pages(os.path.join(src_dir, d)):
            txt = html_text(open(path, encoding='utf-8', errors='replace').read())
            if g.get('url_names'):
                q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
                txt += '\n' + '\n'.join(q.get('n', []))
            add(url, url, txt)
            scanned['web pages'] += 1
    if 'repo' in g:
        rd, slug, pat = g['repo']
        base = os.path.join(src_dir, rd)
        for path in sorted(glob.glob(os.path.join(base, '**', pat), recursive=True)):
            rel = os.path.relpath(path, base)
            url = f'https://github.com/{slug}/blob/{commit_of(gid)}/{rel}'
            add(rel, url, open(path, encoding='utf-8', errors='replace').read())
            scanned['repo files'] += 1
    if 'labels' in g:
        srcname, fn = g['labels']
        for r in bm[srcname]:
            page, url = fn(r['label'])
            page_hits.setdefault((page, url), []).append((r['cluster'], 'blueprint-label',
                                                          f"{r['label']}: {r['lean_name']}", ('d', r['lean_name'], r['module'])))
        scanned['blueprint statements'] = len({r['label'] for r in bm[srcname]})

    rows = merge_rows(page_hits)
    if DECLS_OUT and not g.get('side'):
        for (page, url), hs in page_hits.items():
            for h in hs:
                if len(h) > 3:
                    ref = h[3]
                    DECL_ROWS.add((gid, h[0], page, ref[0], ref[1], ref[2] if ref[0] == 'd' else ref[1]))
    rows.sort(key=lambda r: (r[0], r[1]))
    od = os.path.dirname(summary_path) if g.get('side') else out_dir
    outf = os.path.join(od, f"{gid.replace('@', '--')}.tsv")
    manual = []
    if os.path.exists(outf):   # hand-written rows (basis manual-*) survive the rerun
        with open(outf, encoding='utf-8') as fh:
            for r in csv.DictReader(fh, delimiter='\t', quoting=csv.QUOTE_NONE):
                if (r.get('basis') or '').startswith('manual-'):
                    manual.append((r['cluster'], r['page'], r['page_url'], r['basis'], r['evidence']))
    mkeys = {(r[0], r[1]) for r in manual}
    rows = [r for r in rows if (r[0], r[1]) not in mkeys] + manual
    with open(outf, 'w', encoding='utf-8') as fh:
        fh.write('cluster\tpage\tpage_url\tbasis\tevidence\n')
        for r in rows:
            fh.write('\t'.join(x.replace('\t', ' ').replace('\n', ' ') for x in r) + '\n')
    summary[gid] = {'scanned': dict(scanned), 'pages_with_hits': len({r[1] for r in rows}),
                    'clusters': sorted({r[0] for r in rows}), 'rows': len(rows),
                    'by_basis': dict(collections.Counter(r[3] for r in rows)),
                    'clusters_by_basis': {b: len({r[0] for r in rows if r[3] == b}) for b in RANK},
                    'skipped': dict(skipped)}
    print(gid, summary[gid]['scanned'], 'pages with hits', summary[gid]['pages_with_hits'],
          'clusters', len(summary[gid]['clusters']), summary[gid]['by_basis'], dict(skipped), file=sys.stderr)
if summary_path:
    json.dump(summary, open(summary_path, 'w'), indent=1)
if DECLS_OUT:
    with open(DECLS_OUT, 'w', encoding='utf-8') as fh:
        fh.write('guide\tcluster\tpage\tkind\tname\tmodule\n')
        for r in sorted(DECL_ROWS):
            fh.write('\t'.join(r) + '\n')
    print(f'{DECLS_OUT}: {len(DECL_ROWS)} rows', file=sys.stderr)
