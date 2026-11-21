"""Build the inputs for clustering: import graph, TF-IDF content vectors, labels.

usage: uv run -q --with scikit-learn --with scipy --with pyyaml python -I scripts/cluster/features.py <out_dir>

Reads the Lean files as text only (never runs them). Writes to out_dir:
  mods.txt     one module per line (row order of every matrix)
  adj.npz      directed import graph, adj[a, b] = 1 if a imports b (project files only)
  tfidf.npz    sparse TF-IDF of identifier words (import lines left out: they are the graph)
  svd.npy      TF-IDF reduced to 128 dims, rows L2-normalised
  labels.json  {module: [concept ids]} for files already mapped in the tree
  skip.txt     skip modules (left out); merged.tsv: each skip module -> real module it merges into, or -
"""
import os, re, sys, json, glob
from multiprocessing import Pool
import numpy as np, scipy.sparse as sp, yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
SRC = os.path.abspath(os.path.join(REPO, '..', 'src', 'lean', 'src'))
NOTES = os.path.abspath(os.path.join(REPO, '..', 'notes'))

KW = set('''theorem lemma def abbrev instance structure class where with fun by have show from let
in if then else match do calc at only this namespace section end open variable noncomputable private
protected set_option autoImplicit false true simp rw exact intro intros apply refine use obtain rcases
cases induction constructor ext rfl omega linarith ring norm_num positivity field_simp push_cast
gcongr aesop decide exists_prop congr unfold change specialize exfalso contradiction trivial assumption
type prop sort and or not iff the for all some none'''.split())
ID = re.compile(r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*")
CAMEL = re.compile(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+|[0-9]+")


def words(path):
    out = []
    try:
        text = open(os.path.join(SRC, path), encoding='utf-8', errors='replace').read()
    except OSError:
        return ''
    for line in text.split('\n'):
        if line.startswith('import '):
            continue
        for ident in ID.findall(line):
            for part in ident.split('.'):
                p = part.strip("'_")
                if len(p) < 3 or p.lower() in KW:
                    continue
                out.append(p.lower())
                subs = [s.lower() for s in CAMEL.findall(p) if len(s) >= 3]
                if len(subs) > 1:
                    out += [s for s in subs if s not in KW]
    return ' '.join(out)


def main(out):
    os.makedirs(out, exist_ok=True)
    rows = [l.rstrip('\n').split('\t') for l in list(open(os.path.join(NOTES, 'tree', 'import_closure.tsv')))[1:]]
    mods = [r[0] for r in rows]
    idx = {m: i for i, m in enumerate(mods)}
    # skip files: wrappers merge into their partner; hubs, config-only and empty files drop out
    skip = {}
    for l in list(open(os.path.join(REPO, 'tree', 'skip.tsv')))[1:]:
        p = l.rstrip('\n').split('\t')
        skip[p[0][:-5].replace('/', '.')] = p[3][:-5].replace('/', '.') if p[1] == 'statement-wrapper' and p[3] else None
    def rep(m, depth=0):
        while m in skip and depth < 20:
            m = skip[m]; depth += 1
            if m is None:
                return None
        return m if m in idx and m not in skip else None
    full = mods
    mods = [m for m in full if m not in skip]
    ridx = {m: i for i, m in enumerate(mods)}
    R = {m: rep(m) for m in full}
    a, b = [], []
    for r in rows:
        x = R[r[0]]
        if x is None:
            continue
        for t in r[2].split():
            y = R.get(t)
            if y is not None and y != x:
                a.append(ridx[x]); b.append(ridx[y])
    adj = sp.csr_matrix((np.ones(len(a), np.float32), (a, b)), shape=(len(mods),) * 2)
    adj.data[:] = 1
    sp.save_npz(os.path.join(out, 'adj.npz'), adj)
    open(os.path.join(out, 'mods.txt'), 'w').write('\n'.join(mods) + '\n')
    open(os.path.join(out, 'merged.tsv'), 'w').write(''.join(f'{m}\t{R[m] or "-"}\n' for m in skip))
    print(len(full), 'modules,', len(mods), 'real,', adj.nnz, 'import edges after merging wrappers', flush=True)
    idx = ridx

    paths = [m.replace('.', '/') + '.lean' for m in mods]
    with Pool(10) as pool:
        docs = pool.map(words, paths, chunksize=500)
    print('tokenised', sum(len(d) for d in docs) // 1_000_000, 'M chars', flush=True)
    vec = TfidfVectorizer(token_pattern=r'\S+', lowercase=False, min_df=5, max_df=0.3,
                          sublinear_tf=True, dtype=np.float32)
    X = vec.fit_transform(docs)
    del docs
    sp.save_npz(os.path.join(out, 'tfidf.npz'), X)
    json.dump(vec.get_feature_names_out().tolist(), open(os.path.join(out, 'vocab.json'), 'w'))
    print('tfidf', X.shape, X.nnz, flush=True)
    Z = TruncatedSVD(128, random_state=0).fit_transform(X)
    np.save(os.path.join(out, 'svd.npy'), normalize(Z).astype(np.float32))
    print('svd done', flush=True)

    sys.path.insert(0, os.path.join(REPO, 'scripts'))
    import treelib
    _, nodes = treelib.load(REPO)
    concepts = {n['id'] for n in nodes if n['kind'] in ('concept', 'leaf')}
    labels = {}
    if True:
        for n in nodes:
            cs = sorted(c for c in n.get('needs') or [] if c in concepts or c.startswith('concept-'))
            for ref in n.get('lean') or []:
                m = R.get(ref.split(':')[0][:-5].replace('/', '.'))
                if m in idx and cs:
                    labels[m] = sorted(set(labels.get(m, [])) | set(cs))
    json.dump(labels, open(os.path.join(out, 'labels.json'), 'w'))
    open(os.path.join(out, 'skip.txt'), 'w').write('\n'.join(skip) + '\n')
    print(len(labels), 'labelled files', flush=True)


if __name__ == '__main__':
    main(sys.argv[1])
