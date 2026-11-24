"""Merge the checked agent rows (short names written in a guide's text) into the live guide data (guides-design.md
section 5, steps 3 and 4).

usage: uv run --no-project python -I merge_agent_rows.py <accepted.jsonl> <spotcheck-result.json> <guide-refs dir>
                                                         <guide-decls.tsv.gz> [--max-fail=2]

<accepted.jsonl>         the agent proposals that passed confirm.py and the spot-check, one JSON object per line
                         (guide, page, page_url, cluster, kind decl|module, name, modules, quoted_text), i.e.
                         research/guides/n4/out/accepted-after-spotcheck.jsonl
<spotcheck-result.json>  the spot-check counts per guide (research/guides/n4/out/spotcheck-result.json). A guide is
                         merged only if at most --max-fail of its sampled rows failed; the others are left as they are.
<guide-refs dir>         repo/data/guide-refs: <guide id>.tsv (cluster, page, page_url, basis, evidence) is rewritten
<guide-decls.tsv.gz>     repo/data/guide-decls.tsv.gz (guide, cluster, page, kind d|f, name, module) is rewritten

Per merged guide: the old `agent` rows are dropped, then one `agent` row is added per (cluster, page) that has no
script row (exact-name, exact-path, ...) or hand-written row (`manual-*`) yet; those rows always win. Evidence is
`"<quote>" -> <full name>` per proposal, shortened like the script's rows (the first 4 items, then `; +N more`).
In guide-decls the rows of the old agent (cluster, page) pairs are dropped and the agent declarations and files of
the new ones are added, so the Lean viewer's "Cited by" lists them. Running it twice gives the same files.
scripts/guides/match_guides.py keeps only `manual-*` rows on rerun: run this script again after it.
"""
import sys, os, re, csv, json, gzip, collections

args = [a for a in sys.argv[1:] if not a.startswith('--')]
opts = dict(a[2:].split('=', 1) for a in sys.argv[1:] if a.startswith('--') and '=' in a)
if len(args) != 4:
    sys.exit(__doc__)
acc_f, res_f, refs_d, decls_f = args
max_fail = int(opts.get('max-fail', 2))

res = json.load(open(res_f, encoding='utf-8'))['guides']
ship = sorted(g for g, r in res.items() if r['failed'] <= max_fail)
held = sorted(g for g, r in res.items() if r['failed'] > max_fail)
acc = collections.defaultdict(list)
for ln in open(acc_f, encoding='utf-8'):
    if ln.strip():
        r = json.loads(ln)
        acc[r['guide']].append(r)

HDR = ['cluster', 'page', 'page_url', 'basis', 'evidence']


def shorten(ev):
    ev = list(dict.fromkeys(ev))
    return '; '.join(ev[:4]) + (f'; +{len(ev) - 4} more' if len(ev) > 4 else '')


def one_line(s):
    return re.sub(r'\s+', ' ', s.replace('\t', ' ')).strip()


with gzip.open(decls_f, 'rt', encoding='utf-8') as fh:
    drows = list(csv.DictReader(fh, delimiter='\t', quoting=csv.QUOTE_NONE))
dhdr = ['guide', 'cluster', 'page', 'kind', 'name', 'module']
drop_keys, add_decls, report = set(), set(), {}
for g in ship:
    f = os.path.join(refs_d, g + '.tsv')
    with open(f, encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh, delimiter='\t', quoting=csv.QUOTE_NONE))
    old_agent = {(r['cluster'], r['page']) for r in rows if r['basis'] == 'agent'}
    drop_keys |= {(g, c, p) for c, p in old_agent}
    keep = [r for r in rows if r['basis'] != 'agent']
    taken = {(r['cluster'], r['page']) for r in keep}
    new = collections.OrderedDict()
    for a in acc.get(g, []):
        key = (a['cluster'], a['page'])
        if key in taken:
            continue
        e = new.setdefault(key, {'url': a['page_url'], 'ev': []})
        assert e['url'] == a['page_url'], (g, key, e['url'], a['page_url'])
        e['ev'].append(f'"{one_line(a["quoted_text"])}" -> {a["name"]}')
        for m in a['modules']:
            add_decls.add((g, a['cluster'], a['page'], 'd' if a['kind'] == 'decl' else 'f', a['name'],
                           m if a['kind'] == 'decl' else a['name']))
    agent = [{'cluster': c, 'page': p, 'page_url': e['url'], 'basis': 'agent', 'evidence': shorten(e['ev'])}
             for (c, p), e in new.items()]
    script = [r for r in keep if not r['basis'].startswith('manual-')] + agent
    script.sort(key=lambda r: (r['cluster'], r['page']))
    out = script + [r for r in keep if r['basis'].startswith('manual-')]
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write('\t'.join(HDR) + '\n')
        for r in out:
            fh.write('\t'.join(one_line(r[h]) for h in HDR) + '\n')
    report[g] = {'rows_before': len(rows), 'rows_after': len(out), 'agent_rows': len(agent),
                 'clusters_before': len({r['cluster'] for r in rows}), 'clusters_after': len({r['cluster'] for r in out})}

drows = [r for r in drows if (r['guide'], r['cluster'], r['page']) not in drop_keys]
have = {tuple(r[h] for h in dhdr) for r in drows}
allr = sorted(have | add_decls)
with gzip.GzipFile(decls_f, 'wb', mtime=0) as gz:
    gz.write(('\t'.join(dhdr) + '\n' + ''.join('\t'.join(r) + '\n' for r in allr)).encode('utf-8'))
print(json.dumps({'merged': report, 'held (too many spot-check failures)': held,
                  'guide-decls rows': len(allr), 'agent decl rows': len(add_decls)}, indent=1))
