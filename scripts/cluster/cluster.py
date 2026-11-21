"""Cluster the project's files by content, imports, or both, and score each method.

usage: uv run -q --with scikit-learn --with scipy --with igraph --with leidenalg --with gensim \
         --with faiss-cpu python -I scripts/cluster/cluster.py <dir made by features.py> [methods]

methods (comma list, default all): folder, tfidf, imports, mix, smooth, node2vec
Writes <dir>/clusters-<method>.npy (cluster id per module) and prints a score table.

Scores use the files already mapped by the LLM mapping loop (labels.json: the
concept/leaf nodes each file needs). They are noisy and cover only ~2% of files, so
read them as a comparison between methods, not as accuracy.
  knn@10   mean Jaccard of concept sets between a labelled file and its 10 nearest
           labelled files in the method's vector space (vector methods only)
  pairJ    mean Jaccard between labelled files in the same cluster
  lift     pairJ / Jaccard of random labelled pairs
  cover    share of labelled files whose cluster holds another labelled file
"""
import os, sys, json, time
import numpy as np, scipy.sparse as sp
from sklearn.preprocessing import normalize

D = sys.argv[1]
WANT = (sys.argv[2] if len(sys.argv) > 2 else 'folder,tfidf,imports,mix,smooth,node2vec').split(',')
rng = np.random.default_rng(0)
mods = open(os.path.join(D, 'mods.txt')).read().split()
N = len(mods)
idx = {m: i for i, m in enumerate(mods)}
adj = sp.load_npz(os.path.join(D, 'adj.npz'))
A = ((adj + adj.T) > 0).astype(np.float32)
A.setdiag(0); A.eliminate_zeros(); A = A.tocsr()
X0 = np.load(os.path.join(D, 'svd.npy'))
labels = {idx[m]: set(c) for m, c in json.load(open(os.path.join(D, 'labels.json'))).items()}
L = np.array(sorted(labels))
print(f'{N} files, {A.nnz // 2} undirected import edges, {len(L)} labelled', flush=True)


def jac(a, b):
    return len(a & b) / len(a | b)


ri = rng.integers(0, len(L), (20000, 2))
BASE = np.mean([jac(labels[L[i]], labels[L[j]]) for i, j in ri if i != j])


def knn(Z, k=15):
    import faiss
    faiss.omp_set_num_threads(10)
    Z = np.ascontiguousarray(normalize(Z).astype(np.float32))
    ix = faiss.IndexFlatIP(Z.shape[1]); ix.add(Z)
    S, I = ix.search(Z, k + 1)
    r = np.repeat(np.arange(N), k); c = I[:, 1:].ravel(); w = np.clip(S[:, 1:].ravel(), 0, None)
    K = sp.csr_matrix((w, (r, c)), shape=(N, N))
    return K.maximum(K.T).tocsr()


def knn_score(Z, k=10):
    import faiss
    Zl = np.ascontiguousarray(normalize(Z[L]).astype(np.float32))
    ix = faiss.IndexFlatIP(Zl.shape[1]); ix.add(Zl)
    _, I = ix.search(Zl, k + 1)
    return np.mean([np.mean([jac(labels[L[i]], labels[L[j]]) for j in row[1:]]) for i, row in enumerate(I)])


CAP = 50


def _part(W, res):
    import igraph as ig, leidenalg as la
    W = sp.triu(W, 1).tocoo()
    g = ig.Graph(n=W.shape[0], edges=np.column_stack([W.row, W.col]), directed=False)
    p = la.find_partition(g, la.RBConfigurationVertexPartition, weights=W.data,
                          resolution_parameter=res, seed=0, n_iterations=2)
    return np.array(p.membership)


def leiden(W):
    """Leiden at resolution 1, then re-run Leiden inside every cluster bigger than CAP
    (doubling the resolution when it will not split) until all are <= CAP.
    Returns (leaf cluster ids, top-level cluster ids)."""
    W = W.tocsr()
    top = _part(W, 1.0)
    cl = top.copy(); nxt = cl.max() + 1
    todo = [np.flatnonzero(cl == c) for c in np.unique(cl)]
    while todo:
        mem = todo.pop()
        if len(mem) <= CAP:
            continue
        sub = W[mem][:, mem]
        res, m = 1.0, None
        while res <= 1024:
            m = _part(sub, res)
            if m.max() > 0:
                break
            res *= 2
        if m.max() == 0:   # no edges to cut on: chop in order
            m = np.arange(len(mem)) // CAP
        for c in np.unique(m):
            part = mem[m == c]
            cl[part] = nxt; nxt += 1
            todo.append(part)
    _, cl = np.unique(cl, return_inverse=True)
    return cl, top


def scale(W):
    return W / W.sum()


def sym_norm(W, self_loops=False):
    if self_loops:
        W = W + sp.identity(N, dtype=np.float32, format='csr')
    d = np.asarray(W.sum(1)).ravel(); d[d == 0] = 1
    Dm = sp.diags(1 / np.sqrt(d))
    return (Dm @ W @ Dm).tocsr()


def node2vec(dim=64, walks=5, length=40):
    """uniform random walks (DeepWalk = node2vec with p=q=1) + word2vec."""
    from gensim.models import Word2Vec
    ip, ind = A.indptr, A.indices
    deg = np.diff(ip)
    names = [str(i) for i in range(N)]
    sents = []
    for _ in range(walks):
        cur = np.arange(N); path = [cur]
        for _ in range(length - 1):
            step = ip[cur] + (rng.random(N) * np.maximum(deg[cur], 1)).astype(np.int64)
            cur = np.where(deg[cur] > 0, ind[np.minimum(step, len(ind) - 1)], cur)
            path.append(cur)
        P = np.stack(path, 1)
        sents += [[names[x] for x in row] for row in P]
    m = Word2Vec(sents, vector_size=dim, window=5, min_count=0, sg=1, negative=5,
                 workers=10, epochs=1, seed=0)
    return np.stack([m.wv[names[i]] for i in range(N)])


def report(name, cls, Z=None):
    cl, top = cls if isinstance(cls, tuple) else (cls, None)
    if top is not None:
        np.save(os.path.join(D, f'top-{name}.npy'), top)
    k = f'{knn_score(Z):.3f}' if Z is not None else '  -  '
    pairs = []
    lc = cl[L]
    for c in np.unique(lc):
        mem = L[lc == c]
        if len(mem) < 2:
            continue
        for _ in range(min(200, len(mem) * (len(mem) - 1) // 2)):
            i, j = rng.choice(mem, 2, replace=False)
            pairs.append(jac(labels[i], labels[j]))
    cnt = np.bincount(lc)
    cover = np.mean(cnt[lc] > 1)
    sizes = np.bincount(cl)
    sizes = sizes[sizes > 0]
    pj = np.mean(pairs) if pairs else 0
    print(f'{name:<14} knn@10 {k}  pairJ {pj:.3f}  lift {pj / BASE:4.1f}  cover {cover:.2f}  '
          f'clusters {len(sizes):6d}  median {int(np.median(sizes)):4d}  max {sizes.max():6d}  '
          f'>50: {(sizes > 50).sum()}  top-level {len(np.unique(top)) if top is not None else "-"}', flush=True)
    np.save(os.path.join(D, f'clusters-{name}.npy'), cl)


print(f'random labelled pair Jaccard {BASE:.3f}', flush=True)
t = time.time()
if 'folder' in WANT:
    f = {}
    report('folder', np.array([f.setdefault(m.rsplit('.', 1)[0], len(f)) for m in mods]))
K = None
if 'tfidf' in WANT or 'mix' in WANT:
    K = knn(X0)
if 'tfidf' in WANT:
    report('tfidf', leiden(K), X0)
if 'imports' in WANT:
    report('imports', leiden(A))
if 'mix' in WANT:
    An = scale(sym_norm(A)); Kn = scale(K)
    for a in (0.3, 0.5, 0.7):
        report(f'mix{a}', leiden(a * An + (1 - a) * Kn))
if 'smooth' in WANT:
    S = sym_norm(A, self_loops=True)
    Z = X0
    for hops in (1, 2, 3):
        Z = S @ Z
        if hops >= 2:
            Zn = normalize(Z)
            report(f'smooth{hops}', leiden(knn(Zn)), Zn)
if 'node2vec' in WANT:
    E = node2vec()
    np.save(os.path.join(D, 'node2vec.npy'), E)
    report('n2v-only', leiden(knn(E)), E)
    Z = np.hstack([normalize(X0), normalize(E)])
    report('n2v+tfidf', leiden(knn(Z)), Z)
print(f'{time.time() - t:.0f}s', flush=True)
