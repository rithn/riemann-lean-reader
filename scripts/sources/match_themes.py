"""Word cloud per cited name (titles + abstracts of its papers), matched to the TF-IDF clusters.

usage: uv run -q --with numpy --with scipy python -I scripts/sources/match_themes.py <papers.json> <cluster dir>
For each name: its top words (that also occur in the Lean vocabulary), and the clusters and
themes whose files score highest against those words (cosine of TF-IDF). Writes name_matches.json.
"""
import json, re, sys, os, collections, numpy as np, scipy.sparse as sp
P, D = sys.argv[1], sys.argv[2]
papers = json.load(open(P)); voc = json.load(open(os.path.join(D, 'vocab.json'))); vi = {w: i for i, w in enumerate(voc)}
X = sp.load_npz(os.path.join(D, 'tfidf.npz')).tocsr(); idf_proxy = np.asarray((X > 0).sum(0)).ravel()
mp = json.load(open(os.path.join(D, 'map.json'))); mods = open(os.path.join(D, 'mods.txt')).read().split()
row = {m: i for i, m in enumerate(mods)}
cl_ids = [c['id'] for c in mp['clusters']]; cl_rows = [[row[m] for m in c['files']] for c in mp['clusters']]
C = sp.vstack([sp.csr_matrix(X[r].mean(0)) for r in cl_rows]).tocsr()
C = sp.diags(1 / np.maximum(np.sqrt(C.multiply(C).sum(1).A.ravel()), 1e-9)) @ C
theme = {c['id']: c['theme'] for c in mp['clusters']}; tw = {t['id']: ' '.join(t['words'][:4]) for t in mp['themes']}
title = {}
STOP = set('the of and for in on a an to with by is are we this that as from be its their which these our it can at or under over into some new prove show also two one paper result results theorem give given'.split())
out = {}
for name, v in papers.items():
    text = ' '.join(p['title'] + ' ' + p['abstract'] for p in v['papers']).lower()
    ws = [w for w in re.findall(r"[a-z][a-z\-]+", text) if w not in STOP and len(w) > 3]
    ws = [p for w in ws for p in w.split('-') if len(p) > 3]
    cnt = collections.Counter(w for w in ws if w in vi)
    q = np.zeros(len(voc), np.float32)
    for w, n in cnt.items():
        q[vi[w]] = np.log1p(n) * np.log(X.shape[0] / max(idf_proxy[vi[w]], 1))
    q /= max(np.linalg.norm(q), 1e-9)
    s = C @ q
    best = np.argsort(-s)[:8]
    ths = collections.Counter()
    for b in best: ths[theme[cl_ids[b]]] += 1
    out[name] = {'words': [w for w, _ in cnt.most_common(15)], 'clusters': [(cl_ids[b], round(float(s[b]), 3)) for b in best],
                 'themes': ths.most_common(3)}
    print(f"\n{name}  [{v['step']}]\n  words: {' '.join(out[name]['words'][:12])}\n  best clusters: "
          + ', '.join(f'{k}({x})' for k, x in out[name]['clusters'][:4])
          + '\n  themes: ' + '; '.join(f'{t} [{tw[t]}] x{n}' for t, n in ths.most_common(2)))
json.dump(out, open(os.path.join(os.path.dirname(P), 'name_matches.json'), 'w'), indent=1)
