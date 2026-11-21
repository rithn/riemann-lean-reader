"""File-level import closure from a root module, read as text only (no Lean run).

usage: python -I import_closure.py <lean/src> <RootModule> <out.tsv>
Writes one row per project module that the root reaches: module, depth (shortest import
path from the root), and its direct project imports. Also prints which Mathlib top-level
areas get imported, and from how many files each.
"""
import os, sys, collections

src, root, out = sys.argv[1], sys.argv[2], sys.argv[3]


def path_of(mod):
    return os.path.join(src, *mod.split('.')) + '.lean'


def imports_of(mod):
    res = []
    with open(path_of(mod), encoding='utf-8', errors='replace') as fh:
        for ln in fh:
            s = ln.strip()
            if s.startswith('import '):
                res += s[7:].split()
            elif s and not s.startswith(('--', 'module', 'prelude', 'public import')):
                break  # imports must come first in Lean 4
    return res


depth, edges = {root: 0}, {}
mathlib = collections.Counter()
q = collections.deque([root])
while q:
    m = q.popleft()
    proj = []
    for i in imports_of(m):
        if os.path.exists(path_of(i)):
            proj.append(i)
            if i not in depth:
                depth[i] = depth[m] + 1
                q.append(i)
        else:
            mathlib['.'.join(i.split('.')[:2])] += 1
    edges[m] = proj

with open(out, 'w') as fh:
    fh.write('module\tdepth\timports\n')
    for m in sorted(depth, key=lambda x: (depth[x], x)):
        fh.write(f"{m}\t{depth[m]}\t{' '.join(edges[m])}\n")

total = sum(1 for dp, _, fs in os.walk(src) for f in fs if f.endswith('.lean'))
print(f"{len(depth)} of {total} project files reachable from {root}; max depth {max(depth.values())}")
print('by top folder:', collections.Counter(m.split('.')[0] for m in depth).most_common())
print('non-project imports (top 25):', mathlib.most_common(25))
