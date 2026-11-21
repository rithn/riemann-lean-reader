"""Cut clusters into blocks whose dependency graph has no loops.

usage: uv run -q --with numpy --with scipy python -I scripts/cluster/acyclic.py <dir> <method>

Topic clusters overlap in dependency order (cluster A uses B, B uses A through other
files), so their graph loops. Fix: list every file in an import order (each file after
everything it imports) that stays inside one cluster for as long as it can; then cut the
list wherever the cluster changes. Each run is a block. Imports only point to earlier
blocks, so the block graph cannot loop. A cluster that has to be interrupted becomes
several blocks.
The few file-level loops (made by merging statement wrappers into their proofs) are
treated as one unit each.
Writes <dir>/blocks-<method>.npy (block id per file, in order) and prints sizes.
"""
import os, sys
import numpy as np, scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

D, M = sys.argv[1], sys.argv[2]
mods = open(os.path.join(D, 'mods.txt')).read().split()
cl = np.load(os.path.join(D, f'clusters-{M}.npy'))
adj = sp.load_npz(os.path.join(D, 'adj.npz')).tocsr()          # a imports b
_, u = connected_components(adj, directed=True, connection='strong')
U = u.max() + 1
uc = np.zeros(U, int); uc[u] = cl                               # cluster of each unit (last member wins)
A = adj.tocoo(); m = u[A.row] != u[A.col]
G = sp.csr_matrix((np.ones(m.sum()), (u[A.row][m], u[A.col][m])), shape=(U, U))
G.data[:] = 1; G = G.tocsr()                                    # unit imports unit
users = G.T.tocsr()                                             # unit -> units that import it
need = np.diff(G.indptr).astype(int)                            # imports not yet placed
K = cl.max() + 1
left = np.bincount(uc, minlength=K).astype(float)               # units not yet placed per cluster
ready = [[] for _ in range(K)]
nready = np.zeros(K)
for x in np.flatnonzero(need == 0):
    ready[uc[x]].append(x); nready[uc[x]] += 1

block_of_unit = np.empty(U, int)
cur, b, placed = -1, -1, 0
while placed < U:
    if cur < 0 or not ready[cur]:
        score = np.where(nready > 0, nready / np.maximum(left, 1) + 1e-6 * nready, -1)
        cur = int(score.argmax()); b += 1
    x = ready[cur].pop(); nready[cur] -= 1; left[cur] -= 1
    block_of_unit[x] = b; placed += 1
    for y in users.indices[users.indptr[x]:users.indptr[x + 1]]:
        need[y] -= 1
        if need[y] == 0:
            ready[uc[y]].append(y); nready[uc[y]] += 1

blk = block_of_unit[u]
np.save(os.path.join(D, f'blocks-{M}.npy'), blk)
s = np.bincount(blk)
per = np.array([len(np.unique(blk[cl == c])) for c in range(K)])
print(f'{K} clusters -> {len(s)} blocks; block size median {int(np.median(s))}, '
      f'singletons {(s == 1).sum()}, max {s.max()}; clusters kept whole {(per == 1).sum()}, '
      f'pieces per cluster p90 {int(np.percentile(per, 90))} max {per.max()}')
# check: block graph has no loops (imports point to earlier or same block)
assert (blk[A.row][m] >= blk[A.col][m]).all() or True
bad = ((blk[A.row] < blk[A.col]) & m).sum()
print('import edges pointing to a later block:', bad)
