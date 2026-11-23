"""84a/84b/84c. Read two public blueprints into structured data and match their Lean names to our files.

usage: uv run --no-project python -I blueprints.py <merten repo dir> <merten sha> <naskrecki repo dir> <naskrecki sha>
                                                   <xref data dir> <site modules.json> <site clusters.json>
The repo dirs are unpacked GitHub tarballs (read as data, nothing in them is run).
  Merten: chrisflav/riemann-blueprint, one Markdown file per statement with TOML front matter (`lean = [...]`).
  Naskręcki: nasqret/riemann-rev, data/model.json nodes (the atlas: declaration, module, lines).
Writes merten.json, naskrecki.json and blueprint_matches.tsv (one row per (source, statement, lean name)).
Match rule: the Lean name is looked up as a full name in decls.tsv.gz (our index, commit 40e56bab).
  matched = exactly one declaring module; ambiguous = several; not_found = none. If the full name is not
  declared, we also try it as a field/constructor row and record that in `how`.
"""
import os, sys, re, json, gzip, glob, tomllib, collections

mdir, msha, ndir, nsha, d, modules_json, clusters_json = sys.argv[1:8]

# ---------- 84a: Merten ----------
FM = re.compile(r'^\+\+\+\n(.*?)\n\+\+\+\n?(.*)$', re.S)
merten = []
for p in sorted(glob.glob(os.path.join(mdir, 'blueprint', '**', '*.md'), recursive=True)):
    if p.endswith('.proof.md'):
        continue
    m = FM.match(open(p, encoding='utf-8').read())
    if not m:
        continue
    fm = tomllib.loads(m.group(1))
    if fm.get('kind') in (None, 'section', 'chapter', 'reference', 'matter', 'proof'):   # statements only
        continue
    rel = os.path.relpath(p, mdir)
    label = fm.get('id') or (os.path.basename(os.path.dirname(p)) if p.endswith('_section.md')
                             else os.path.basename(p)[:-3])
    merten.append({'label': label, 'kind': fm.get('kind'), 'title': fm.get('title'),
                   'text': m.group(2).strip(), 'lean': fm.get('lean', []), 'uses': fm.get('uses', []),
                   'provenance': fm.get('provenance'), 'source': fm.get('source'),
                   'url': f'https://github.com/chrisflav/riemann-blueprint/blob/{msha}/{rel}'})
json.dump({'source': 'https://github.com/chrisflav/riemann-blueprint', 'commit': msha,
           'site': 'https://riemann.fuxi.merten.dev', 'lean_mirror_commit': '8c90877c (per its README)',
           'license_note': 'see the repository', 'statements': merten},
          open(os.path.join(d, 'merten.json'), 'w'), ensure_ascii=False, indent=1)
facts = json.load(open(os.path.join(mdir, 'lean-facts.json')))['decls']

# ---------- 84b: Naskręcki atlas ----------
model = json.load(open(os.path.join(ndir, 'data', 'model.json')))
nask = []
for n in model['nodes']:
    nask.append({'label': n['id'], 'title': n.get('title'), 'component': n.get('component'),
                 'kind': n.get('kind'), 'text': n.get('contract'), 'idea': n.get('idea'),
                 'lean': [n['declaration']] if n.get('declaration') else [], 'module': n.get('module'),
                 'lines': n.get('lines'), 'lean_head': n.get('lean_head'), 'tier': n.get('tier'),
                 'url': f'https://github.com/nasqret/riemann-rev/blob/{nsha}/data/model.json',
                 'lean_url': n.get('url'), 'atlas': 'https://nasqret.github.io/riemann-rev/atlas/'})
json.dump({'source': 'https://github.com/nasqret/riemann-rev', 'commit': nsha,
           'lean_mirror_commit': '40e56bab', 'license': '0BSD', 'declarations': nask},
          open(os.path.join(d, 'naskrecki.json'), 'w'), ensure_ascii=False, indent=1)

# ---------- 84c: match ----------
decl = collections.defaultdict(list)
with gzip.open(os.path.join(d, 'decls.tsv.gz'), 'rt', encoding='utf-8') as fh:
    next(fh)
    for ln in fh:
        n, mod, line, k, fl = ln.rstrip('\n').split('\t')
        decl[n].append((mod, int(line), k))
mj = json.load(open(modules_json))
mod_cl = {f"{mj['folders'][a]}.{b}" if mj['folders'][a] else b: 'k%04d' % k for a, b, k in mj['rows']}
cl_title = {c['id']: c['title'] for c in json.load(open(clusters_json))['clusters']}


decl_by_last = collections.defaultdict(list)
for n in decl:
    decl_by_last[n.rsplit('.', 1)[-1]].append(n)


rows, counts = [], collections.Counter()
for src, items in (('merten', merten), ('naskrecki', nask)):
    for it in items:
        for name in it['lean']:
            hits = decl.get(name, [])
            how = 'full name'
            if not hits and src == 'naskrecki' and it.get('module'):
                # the atlas gives the name as written in the file; look for a declaration in that module
                # whose full name ends with it
                cand = [(n, h) for n, hs in ((n, decl[n]) for n in decl_by_last.get(name.rsplit('.', 1)[-1], ()))
                        for h in hs if h[0] == it['module'] and (n == name or n.endswith('.' + name))]
                if cand:
                    hits = [h for _, h in cand]; how = f'suffix in stated module ({cand[0][0]})'
            mods = sorted({h[0] for h in hits})
            status = 'matched' if len(mods) == 1 else 'ambiguous' if mods else 'not_found'
            counts[(src, status)] += 1
            mod = mods[0] if len(mods) == 1 else ' '.join(mods)
            line = hits[0][1] if len(mods) == 1 else ''
            cl = mod_cl.get(mod, '') if len(mods) == 1 else ''
            theirs = it.get('module') if src == 'naskrecki' else (facts.get(name) or {}).get('module')
            agree = '' if not theirs or status != 'matched' else ('yes' if theirs == mod else 'no')
            rows.append((src, it['label'], name, status, how, mod, line, cl, cl_title.get(cl, ''),
                         theirs or '', agree))
        if not it['lean']:
            counts[(src, 'no_lean_name')] += 1

with open(os.path.join(d, 'blueprint_matches.tsv'), 'w') as fh:
    fh.write('source\tlabel\tlean_name\tstatus\thow\tmodule\tline\tcluster\tcluster_title\ttheir_module\tsame_module\n')
    fh.writelines('\t'.join(map(str, r)) + '\n' for r in rows)
print(f"merten: {len(merten)} statements, {sum(len(x['lean']) for x in merten)} lean names; "
      f"naskrecki: {len(nask)} nodes, {sum(len(x['lean']) for x in nask)} lean names")
for k, v in sorted(counts.items()):
    print(f"  {k[0]:10s} {k[1]:14s} {v}")
agree = collections.Counter((r[0], r[10]) for r in rows if r[10])
print('module agrees with the blueprint\'s own module:', dict(agree))
for src in ('merten', 'naskrecki'):
    stm = [it for it in (merten if src == 'merten' else nask) if it['lean']]
    ok = sum(1 for it in stm if any(r[0] == src and r[1] == it['label'] and r[3] == 'matched' for r in rows))
    cls = {r[7] for r in rows if r[0] == src and r[7]}
    print(f"  {src}: statements with >=1 matched name {ok}/{len(stm)}; distinct clusters {len(cls)}")
