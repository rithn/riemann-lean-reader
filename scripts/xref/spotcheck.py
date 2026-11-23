"""79d. Draw 50 resolved occurrences from occurrences.tsv.gz and check them independently.

usage: uv run --no-project python -I spotcheck.py <lean/src> <xref data dir> [seed=7]
25 are drawn among occurrences whose target is a blueprint Lean name (checked against the blueprint's own
module: Merten's lean-facts.json module or Naskręcki's stated module), 25 among the other resolved ones.
Each pick has a distinct (target) name. For every pick the script greps the target module's file for a
declaration of the last name component and rebuilds the namespace from the `namespace`/`end` lines above it
(a separate, simpler reading than leansrc.py), then prints the usage line for a manual read.
Writes spotcheck.tsv; the `manual` column is filled by hand after reading the usage lines.
"""
import os, sys, re, gzip, csv, json, random

src, d = sys.argv[1], sys.argv[2]
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 7
bp = {}
for r in csv.DictReader(open(os.path.join(d, 'blueprint_matches.tsv')), delimiter='\t'):
    if r['status'] == 'matched':
        bp[r['lean_name']] = (r['source'], r['their_module'])
rows = [l.rstrip('\n').split('\t') for l in gzip.open(os.path.join(d, 'occurrences.tsv.gz'), 'rt', encoding='utf-8')][1:]
res = [r for r in rows if r[3].startswith('resolved')]
rnd = random.Random(seed)
rnd.shuffle(res)
pick, seen = [], set()
for want_bp, k in ((True, 25), (False, 25)):
    n = 0
    for r in res:
        if (r[4] in bp) != want_bp or r[4] in seen:
            continue
        seen.add(r[4]); pick.append(r); n += 1
        if n == k:
            break


def grep_decl(mod, full):
    """Independent check: find `<kw> <name>` in the file and rebuild the namespace from namespace/end lines."""
    lines = open(os.path.join(src, *mod.split('.')) + '.lean', encoding='utf-8').read().split('\n')
    last = full.rsplit('.', 1)[-1]
    stack = []
    for i, ln in enumerate(lines, 1):
        w = ln.split()
        if not w:
            continue
        if w[0] == 'namespace':
            stack.append(w[1])
        elif w[0] in ('section', 'noncomputable') and 'section' in w[:2]:
            stack.append('')
        elif w[0] == 'end' and stack:
            stack.pop()
        m = re.search(r'\b(?:theorem|lemma|def|abbrev|structure|class|inductive|instance|alias)\s+(\S+)', ln)
        names = []
        if m:
            names.append(m.group(1))
        f = re.match(r'\s+(\S+)\s*:', ln) or re.match(r'\s*\|\s*(\S+)', ln)
        if f:
            names.append('*.' + f.group(1))
        for nm in names:
            nm = nm.split('.{')[0]
            if nm == last or nm.endswith('.' + last):
                ns = '.'.join(x for x in stack if x)
                if nm.startswith('*.'):
                    return i, 'member ' + ln.strip()[:80], full.endswith('.' + last)
                cand = nm[7:] if nm.startswith('_root_.') else (ns + '.' + nm if ns else nm)
                if cand == full:
                    return i, ln.strip()[:100], True
    if full.endswith('.mk'):
        return 0, 'implicit mk constructor', True
    return 0, 'not found by grep', False


out = []
for r in pick:
    mod, line, tok, cat, tgt, tmod = r[:6]
    gl, gtext, gok = grep_decl(tmod, tgt)
    use = open(os.path.join(src, *mod.split('.')) + '.lean', encoding='utf-8').read().split('\n')[int(line) - 1].strip()
    b = bp.get(tgt)
    bpok = '' if not b else ('yes' if b[1] == tmod else 'no')
    out.append({'group': 'blueprint' if b else 'other', 'module': mod, 'line': line, 'token': tok, 'category': cat,
                'target': tgt, 'target_module': tmod, 'grep_line': gl, 'grep_ok': 'yes' if gok else 'no',
                'blueprint_module_ok': bpok, 'usage': use[:200], 'grep_text': gtext, 'manual': ''})
with open(os.path.join(d, 'spotcheck.tsv'), 'w') as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter='\t')
    w.writeheader(); w.writerows(out)
for i, o in enumerate(out, 1):
    print(f"{i:2d} [{o['group']}] {o['token']} -> {o['target']} ({o['category']}) grep={o['grep_ok']} bp={o['blueprint_module_ok']}")
    print(f"     use: {o['usage'][:170]}")
    print(f"     decl: {o['grep_text'][:120]}")
print('grep ok', sum(o['grep_ok'] == 'yes' for o in out), '/', len(out),
      '; blueprint module ok', sum(o['blueprint_module_ok'] == 'yes' for o in out), '/',
      sum(1 for o in out if o['blueprint_module_ok']))
