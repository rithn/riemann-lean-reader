"""Find bite-sized chunks of the project: files whose import subtree has 10-15 files.

usage: python -I subtrees.py <lean/src> <import_closure.tsv> <skip.tsv> <out.jsonl> [lo hi]

The subtree of a file = the file plus every project file it imports, directly or
indirectly (Mathlib not counted). Files with no maths (skip reasons empty, import-hub,
config-only) are walked through but not counted. Statement-wrappers are counted as
files but marked `skip` with their partner, so a chunk's `nodes` = files - wrappers. A chunk is "maximal": no file importing it also has a
subtree within the size limit, so chunks don't nest.
Output: one JSON object per line: id, top, folder, depth (from Main), n_files, n_nodes,
lines, status ("todo"), files: [{path, lines, skip?, partner?, note?}].
"""
import os, sys, json, collections

src, closure_tsv, skip_tsv, out = sys.argv[1:5]
lo, hi = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (10, 15)

imp, depth = {}, {}
for ln in list(open(closure_tsv))[1:]:
    m, d, i = ln.rstrip('\n').split('\t')
    imp[m], depth[m] = i.split(), int(d)
skip, wrap = set(), {}
for l in list(open(skip_tsv))[1:]:
    f, reason, _, partner, note = (l.rstrip('\n').split('\t') + ['', ''])[:5]
    if reason == 'statement-wrapper':
        wrap[f] = (partner, note)
    else:
        skip.add(f[:-5].replace('/', '.'))
rev = collections.defaultdict(list)
for m, ks in imp.items():
    for k in ks:
        rev[k].append(m)


def subtree(m, cap):
    """Counted members of m's subtree, or None once it exceeds cap."""
    seen, q, members = {m}, [m], []
    while q:
        x = q.pop()
        if x not in skip:
            members.append(x)
            if len(members) > cap:
                return None
        for k in imp.get(x, ()):
            if k not in seen:
                seen.add(k); q.append(k)
    return members


small = {}
for m in imp:
    s = subtree(m, hi)
    if s is not None and m not in skip:
        small[m] = s

lines = {}
def nlines(m):
    if m not in lines:
        lines[m] = sum(1 for _ in open(os.path.join(src, *m.split('.')) + '.lean', encoding='utf-8', errors='replace'))
    return lines[m]

chunks = [m for m, s in small.items() if len(s) >= lo and not any(p in small for p in rev[m])]
rows = sorted(((m, len(small[m]), sum(nlines(x) for x in small[m])) for m in chunks), key=lambda r: r[2])
def path(m):
    return '/'.join(m.split('.')) + '.lean'

with open(out, 'w') as fh:
    for k, (m, n, L) in enumerate(rows, 1):
        files = []
        for x in sorted(small[m]):
            e = {'path': path(x), 'lines': nlines(x)}
            if path(x) in wrap:
                e['skip'] = 'statement-wrapper'
                e['partner'] = wrap[path(x)][0]
                if wrap[path(x)][1]:
                    e['note'] = wrap[path(x)][1]
            files.append(e)
        nw = sum(1 for e in files if 'skip' in e)
        fh.write(json.dumps({'id': f"c{k:04d}", 'top': path(m), 'folder': '/'.join(m.split('.')[:2]),
                             'depth': depth[m], 'n_files': n, 'n_nodes': n - nw, 'lines': L,
                             'status': 'todo', 'files': files}, ensure_ascii=False) + '\n')

print(f"{len(small):,} files have a subtree of at most {hi} files; "
      f"{len(chunks):,} maximal chunks of {lo}-{hi} files covering "
      f"{len(set().union(*[set(small[m]) for m in chunks])):,} files")
print('chunks by folder:', collections.Counter('.'.join(m.split('.')[:2]) for m in chunks).most_common(8))
print('smallest by lines:', [(m.split('.')[-1], n, L) for m, n, L in rows[:5]])
