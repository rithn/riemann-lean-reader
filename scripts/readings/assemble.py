"""Assemble data/file-lines/<cluster>.yaml (tracker #10) from the reviewed English readings of the 1,461 core Lean files.

usage (from repo/): uv run -q --with pyyaml python -I scripts/readings/assemble.py [<readings dir>]
default <readings dir>: ../research/lean-reader/readings (read only; nothing there is written)

Spec: research/plans/core-lean-readings-process.md, sections 2 and 4. Per module, the canonical draft is the attempt
that writer-batch/<module>/result.json points to (its draft.yaml, after the sample and full reviews' repairs). The model
wrote line, reading and key_decls (name + gloss); everything else is computed here:
  depth, lines   files.tsv (depth from notes/tree/import_closure.tsv, lines from the source), both re-checked
  blueprint      research/lean-reader/xref/blueprint_matches.tsv, matched rows of this module ('merten:<label>', 'naskrecki:<label>')
  status, check  the review records: every module was reviewed once (three samples of 150, then the remaining 1,011).
                 fixed   = the review flagged findings and the draft was repaired (it has edits in check-log.tsv)
                 checked = the review flagged nothing
                 pending = anything else (reported; the site leaves pending entries out)
Fails (exit 1) unless: 1,461 modules, each in the cluster files.tsv gives and the site's mod_cl gives (same unit_of logic
as scripts/site/build_site.py), and §4's deterministic checks pass: every key_decls name is a declaration of that module
in decls.tsv.gz, line <= 140 and reading <= 700 characters, line on one line, at most 5 key_decls, no first person and
no banned words (the writer batch's own BANNED pattern, plus "this file" and "this module", which the writer rules forbid).
Display fixes in data/file-lines-overrides.yaml are applied first (each must match its 'old' text exactly).
"""
import os, re, sys, csv, gzip, json, collections
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.dirname(REPO)
RD = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, 'research', 'lean-reader', 'readings')
XREF = os.path.join(ROOT, 'research', 'lean-reader', 'xref')
LEAN = os.path.join(ROOT, 'src', 'lean', 'src')
OUT = os.path.join(REPO, 'data', 'file-lines')
COMMIT = '40e56bab'
EXPECTED = 1461
LIMITS = {'line': 140, 'reading': 700}
# the writer batch's rule (research/lean-reader/readings/scripts/run_writer_smoke.py): first person and hedges/filler
BANNED = re.compile(r"\b(?:I|(?i:we|our|us|seems|likely|appears|crucial|elegant|powerful|plays a key role|this file|this module))\b")
OVERRIDES_F = os.path.join(REPO, 'data', 'file-lines-overrides.yaml')   # display fixes on top of the drafts (see that file)
SAMPLES = [('sample-01', 'draft-sample-review.md'), ('sample-02', 'draft-sample-review-02.md'), ('sample-03', 'draft-sample-review-03.md')]

errors = []
def err(msg):
    errors.append(msg)

# ---------- the file list and the site's cluster membership
files = list(csv.DictReader(open(os.path.join(RD, 'files.tsv'), encoding='utf-8'), delimiter='\t'))
CORE = list(yaml.safe_load(open(os.path.join(REPO, 'data', 'core-names.yaml'), encoding='utf-8')))
D = os.path.join(ROOT, 'notes', 'cluster3')
M = json.load(open(os.path.join(D, 'map.json')))
unit_cl = {f: c['id'] for c in M['clusters'] for f in c['files']}
parent = {}
for ln in open(os.path.join(D, 'merged.tsv'), encoding='utf-8'):
    a, b = (ln.rstrip('\n').split('\t') + [''])[:2]
    parent[a] = None if b == '-' else b
def unit_of(m, depth=0):   # as in build_site.py
    if m in unit_cl:
        return m
    p = parent.get(m)
    return unit_of(p, depth + 1) if p and depth < 20 else None
mod_cl = {}
for m in list(unit_cl) + list(parent):
    u = unit_of(m)
    if u:
        mod_cl[m] = unit_cl[u]
members = collections.Counter(k for k in mod_cl.values() if k in CORE)
fdepth = {}
for ln in open(os.path.join(ROOT, 'notes', 'tree', 'import_closure.tsv'), encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if p[0] != 'module':
        fdepth[p[0]] = int(p[1]) if p[1] not in ('', '-', 'None') else None

if len(files) != EXPECTED or len({r['module'] for r in files}) != EXPECTED:
    err(f'files.tsv: {len(files)} rows, {len({r["module"] for r in files})} modules, expected {EXPECTED}')
for r in files:
    m, k = r['module'], r['cluster']
    if k not in CORE:
        err(f'{m}: cluster {k} is not a core cluster')
    if mod_cl.get(m) != k:
        err(f'{m}: files.tsv says {k}, the site (mod_cl) says {mod_cl.get(m)}')
    if fdepth.get(m) != int(r['depth']):
        err(f'{m}: depth {r["depth"]} in files.tsv, {fdepth.get(m)} in import_closure.tsv')
    src = os.path.join(LEAN, *m.split('.')) + '.lean'
    if not os.path.isfile(src):
        err(f'{m}: no source at {src}')
    else:
        n = open(src, encoding='utf-8', errors='replace').read().count('\n')
        if abs(n - int(r['lines'])) > 1:
            err(f'{m}: {r["lines"]} lines in files.tsv, {n} in the source')
per_cl = collections.Counter(r['cluster'] for r in files)
for k in CORE:
    if per_cl[k] != members[k]:
        err(f'{k}: {per_cl[k]} files in files.tsv, {members[k]} on the site')

# ---------- the review records: which review saw each module, and what it found
review = {}   # module -> (review, outcome)
for name, f in SAMPLES:
    t = open(os.path.join(RD, f), encoding='utf-8').read()
    for _, m, out in re.findall(r'^\|[^|\n]*\|\s*(k\d{4})\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|', t, re.M):
        assert m not in review, f'{m} in two reviews'
        review[m] = (name, {'No issues flagged': 'clean'}.get(out, out.lower()))
for r in csv.DictReader(open(os.path.join(RD, 'check-batch', 'review-register.tsv'), encoding='utf-8'), delimiter='\t'):
    assert r['module'] not in review, f'{r["module"]} in two reviews'
    review[r['module']] = ('full-review', r['outcome'])
edits = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(RD, 'check-log.tsv'), encoding='utf-8'), delimiter='\t'):
    edits[r['module']].append(r)

# ---------- declarations (decls.tsv.gz) and blueprint matches
want = {r['module'] for r in files}
DECLS = collections.defaultdict(set)
with gzip.open(os.path.join(XREF, 'decls.tsv.gz'), 'rt', encoding='utf-8') as fh:
    for r in csv.DictReader(fh, delimiter='\t'):
        if r['module'] in want:
            DECLS[r['module']].add(r['name'])
BP = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(XREF, 'blueprint_matches.tsv'), encoding='utf-8'), delimiter='\t'):
    if r['status'] == 'matched' and r['module'] in want:
        x = f'{r["source"]}:{r["label"]}'
        if x not in BP[r['module']]:
            BP[r['module']].append(x)

# ---------- assemble
OVR = collections.defaultdict(list)
for o in (yaml.safe_load(open(OVERRIDES_F, encoding='utf-8')) if os.path.exists(OVERRIDES_F) else []) or []:
    assert o['field'] in ('line', 'reading') and o['module'] in want, f'overrides: bad entry {o}'
    OVR[o['module']].append(o)
OVR_USED = []
def one_line(s):
    return ' '.join(str(s).split())
out = collections.defaultdict(list)
status_n = collections.Counter()
pending = []
warn = []
for r in files:
    m, k = r['module'], r['cluster']
    res = json.load(open(os.path.join(RD, 'writer-batch', m, 'result.json'), encoding='utf-8'))
    if res.get('status') != 'valid':
        err(f'{m}: result.json status {res.get("status")!r}')
        continue
    dr = yaml.safe_load(open(os.path.join(RD, 'writer-batch', m, res['attempt'], 'draft.yaml'), encoding='utf-8'))
    if not isinstance(dr, dict) or set(dr) - {'module'} != {'line', 'reading', 'key_decls'}:
        err(f'{m}: draft fields {sorted(dr) if isinstance(dr, dict) else type(dr)}')
        continue
    line, reading = one_line(dr['line']), one_line(dr['reading'])
    for o in OVR.get(m, []):
        cur = line if o['field'] == 'line' else reading
        if o['old'] not in cur:
            err(f'{m}: override for {o["field"]} no longer matches: {o["old"]!r}')
            continue
        cur = cur.replace(o['old'], o['new'])
        if o['field'] == 'line':
            line = cur
        else:
            reading = cur
        OVR_USED.append(m)
    kd = [{'name': str(x['name']), 'gloss': one_line(x['gloss'])} for x in dr['key_decls'] or []]
    # §4 deterministic checks
    for f, v in (('line', line), ('reading', reading)):
        if not v:
            err(f'{m}: empty {f}')
        if len(v) > LIMITS[f]:
            err(f'{m}: {f} has {len(v)} characters (limit {LIMITS[f]})')
        b = BANNED.search(v)
        if b:
            err(f'{m}: {f} contains {b.group()!r}')
    if '\n' in str(dr['line']).strip():
        err(f'{m}: line spans several lines')
    if len(kd) > 5:
        err(f'{m}: {len(kd)} key_decls (limit 5)')
    seen = set()
    for x in kd:
        if x['name'] not in DECLS[m]:
            err(f'{m}: key_decls name {x["name"]} is not a declaration of this module in decls.tsv.gz')
        if x['name'] in seen:
            err(f'{m}: key_decls name {x["name"]} twice')
        seen.add(x['name'])
        if not x['gloss']:
            err(f'{m}: empty gloss for {x["name"]}')
        b = BANNED.search(x['gloss'])
        if b:
            err(f'{m}: gloss of {x["name"]} contains {b.group()!r}')
    # status from the review records
    rv = review.get(m)
    ed = edits.get(m, [])
    before = os.path.exists(os.path.join(RD, 'writer-batch', m, res['attempt'], 'draft-before-sample-review.yaml'))
    if rv and rv[1] == 'clean' and not ed:
        status, check = 'checked', {'verdict': 'supported', 'notes': ''}
    elif rv and rv[1] != 'clean' and ed and before:
        fields = list(dict.fromkeys(e['field'].split('.')[0] for e in ed))
        status = 'fixed'
        check = {'verdict': 'imprecise', 'notes': f'Review {rv[0]} ({rv[1]} findings): {len(ed)} field '
                 f'{"edit" if len(ed) == 1 else "edits"} ({", ".join(fields)}). Before and after text: check-log.tsv.'}
    else:
        status = 'pending'
        why = ('not in any review' if not rv else
               f'review {rv[0]} flagged {rv[1]} findings but the draft has no logged repair' if rv[1] != 'clean' else
               f'review {rv[0]} flagged nothing but the draft has logged edits')
        check = {'verdict': 'unclassified', 'notes': why}
        pending.append((m, k, why))
    if m in OVR_USED:
        check['notes'] = (check['notes'] + ' ' if check['notes'] else '') + 'Display fix: data/file-lines-overrides.yaml.'
    status_n[status] += 1
    out[k].append({'module': m, 'depth': int(r['depth']), 'lines': int(r['lines']), 'line': line, 'reading': reading,
                   'key_decls': kd, 'blueprint': BP.get(m, []), 'status': status, 'check': check})

missing = want - {e['module'] for es in out.values() for e in es}
if missing:
    err(f'{len(missing)} modules not assembled: {sorted(missing)[:5]}')
total = sum(map(len, out.values()))
if total != EXPECTED:
    err(f'{total} entries assembled, expected {EXPECTED}')
if errors:
    print(f'FAILED: {len(errors)} problems; nothing written')
    for e in errors[:60]:
        print('  ' + e)
    sys.exit(1)

os.makedirs(OUT, exist_ok=True)
class _D(yaml.SafeDumper):
    pass
def _str(d, s):   # long text folded (>), the rest plain
    return d.represent_scalar('tag:yaml.org,2002:str', s, style='>' if len(s) > 100 else None)
_D.add_representer(str, _str)
for k in CORE:
    es = sorted(out[k], key=lambda e: (e['depth'], e['module']))
    doc = {'cluster': k, 'source_commit': COMMIT, 'files': es}
    with open(os.path.join(OUT, k + '.yaml'), 'w', encoding='utf-8') as fh:
        fh.write(f'# Generated by scripts/readings/assemble.py from the reviewed readings (research/lean-reader/readings);\n'
                 f'# display fixes go in data/file-lines-overrides.yaml; do not edit this output by hand. Spec: research/plans/core-lean-readings-process.md, section 2.\n')
        yaml.dump(doc, fh, Dumper=_D, allow_unicode=True, sort_keys=False, width=110)
    back = yaml.safe_load(open(os.path.join(OUT, k + '.yaml'), encoding='utf-8'))
    assert [(e['module'], e['line'], e['reading'], e['key_decls']) for e in back['files']] == \
           [(e['module'], e['line'], e['reading'], e['key_decls']) for e in es], f'{k}: YAML round trip changed the text'
lens = {f: [len(e[f]) for es in out.values() for e in es] for f in ('line', 'reading')}
gl = [len(x['gloss']) for es in out.values() for e in es for x in e['key_decls']]
print(f'file-lines: {total} files in {len(CORE)} clusters -> {OUT}')
print('  per cluster: ' + ', '.join(f'{k} {len(out[k])}' for k in CORE))
print('  status: ' + ', '.join(f'{s} {n}' for s, n in status_n.most_common()))
print(f'  key_decls: {len(gl)} (files with none: {sum(1 for es in out.values() for e in es if not e["key_decls"])}); '
      f'blueprint links: {sum(len(e["blueprint"]) for es in out.values() for e in es)} on '
      f'{sum(1 for es in out.values() for e in es if e["blueprint"])} files')
print(f'  longest: line {max(lens["line"])}, reading {max(lens["reading"])}, gloss {max(gl)} characters')
print(f'  deterministic checks (section 4): passed; display fixes applied: {len(OVR_USED)}')
for m, k, why in pending:
    print(f'  PENDING {k} {m}: {why}')
for w in warn:
    print('  note: ' + w)
