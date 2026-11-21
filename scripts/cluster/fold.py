"""Fold single-importer files into their importer, then rebuild clustering inputs on the units.

usage: uv run -q --with numpy --with scipy --with scikit-learn python -I scripts/cluster/fold.py <in dir> <out dir> [cap]

A file imported by exactly one project file becomes part of its importer's unit (repeated,
bottom-up, up to `cap` files per unit, default 50). Every path into such a file passes
through its importer, so merging cannot create loops.
Note: Lean imports are transitive, so "imported only by A" means B reaches the rest of the
project through A, not that only A uses B's results.
Writes in <out dir> the same files features.py makes (mods = unit heads), with tfidf =
sum of the members' rows, plus merged.tsv with a third column: wrapper | helper.
"""
import os, sys, json, shutil
import numpy as np, scipy.sparse as sp
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize

I, O = sys.argv[1], sys.argv[2]; CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 50
os.makedirs(O, exist_ok=True)
mods = open(os.path.join(I, 'mods.txt')).read().split(); N = len(mods)
A = sp.load_npz(os.path.join(I, 'adj.npz')).tocsr()          # a imports b
ib = A.T.tocsr(); indeg = np.diff(ib.indptr)
# height = longest import chain below a file (process leaves first)
from scipy.sparse.csgraph import connected_components
_, scc = connected_components(A, directed=True, connection='strong')
h = np.zeros(N, int); order = []
outdeg = np.diff(A.indptr).copy(); q = list(np.flatnonzero(outdeg == 0))
while q:
    x = q.pop(); order.append(x)
    for y in ib.indices[ib.indptr[x]:ib.indptr[x + 1]]:
        h[y] = max(h[y], h[x] + 1); outdeg[y] -= 1
        if outdeg[y] == 0: q.append(y)
placed = np.zeros(N, bool); placed[order] = True
print(f'{N} files; {(~placed).sum()} in small import loops (left unfolded)')

par = np.arange(N); size = np.ones(N, int)
def find(x):
    while par[x] != x:
        par[x] = par[par[x]]; x = par[x]
    return x
for x in sorted(np.flatnonzero((indeg == 1) & placed), key=lambda x: h[x]):
    p = ib.indices[ib.indptr[x]]
    rx, rp = find(x), find(p)
    if rx != rp and size[rx] + size[rp] <= CAP:
        par[rx] = rp; size[rp] += size[rx]
root = np.array([find(x) for x in range(N)])
heads = np.unique(root); uid = {r: i for i, r in enumerate(heads)}; U = len(heads)
u = np.array([uid[r] for r in root])
s = np.bincount(u)
print(f'{U} units; size median {int(np.median(s))}, p99 {int(np.percentile(s, 99))}, max {s.max()}')

P = sp.csr_matrix((np.ones(N), (u, np.arange(N))), shape=(U, N))
Ac = (P @ A @ P.T).tocsr(); Ac.setdiag(0); Ac.eliminate_zeros(); Ac.data[:] = 1
sp.save_npz(os.path.join(O, 'adj.npz'), Ac.astype(np.float32))
X = sp.load_npz(os.path.join(I, 'tfidf.npz'))
Xu = normalize((P @ X).tocsr().astype(np.float32))
sp.save_npz(os.path.join(O, 'tfidf.npz'), Xu)
np.save(os.path.join(O, 'svd.npy'), normalize(TruncatedSVD(128, random_state=0).fit_transform(Xu)).astype(np.float32))
shutil.copy(os.path.join(I, 'vocab.json'), O); shutil.copy(os.path.join(I, 'skip.txt'), O)
hm = [mods[r] for r in heads]
open(os.path.join(O, 'mods.txt'), 'w').write('\n'.join(hm) + '\n')
lab = json.load(open(os.path.join(I, 'labels.json'))); new = {}
idx = {m: i for i, m in enumerate(mods)}
for m, cs in lab.items():
    hd = hm[u[idx[m]]]; new[hd] = sorted(set(new.get(hd, [])) | set(cs))
json.dump(new, open(os.path.join(O, 'labels.json'), 'w'))
L = []
for l in open(os.path.join(I, 'merged.tsv')):
    a, b = l.rstrip('\n').split('\t')[:2]
    L.append(f"{a}\t{hm[u[idx[b]]] if b != '-' else '-'}\twrapper\n")
for x in range(N):
    if root[x] != x:
        L.append(f'{mods[x]}\t{hm[u[x]]}\thelper\n')
open(os.path.join(O, 'merged.tsv'), 'w').write(''.join(L))
print(f'{Ac.nnz} unit import edges; {len(new)} labelled units')
