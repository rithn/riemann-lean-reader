"""Build the theme -> cluster map and the bundles for the naming pass (option A).

usage: uv run -q --with numpy --with scipy --with pyyaml python -I scripts/cluster/build_map.py <dir> <method> [max_clusters_per_bundle] [token_budget]

Clusters are reading units. Their "uses" links come from file imports and MAY loop
(the strict no-loop guarantee holds at file level, where Lean enforces it).
Writes:
  <dir>/map.json            themes and clusters: files, size, top words, uses / used-by,
                            concepts of already-mapped files inside, mapped node ids
  <dir>/naming/bundle-NNNN.md  one per naming session: for each cluster, its file names and
                            main statements (names + statement heads only, no proofs)
Clusters and bundles are in dependency order (clusters used by many come first), and
bundles keep one theme together where they can.
"""
import os, re, sys, json, collections
import numpy as np, scipy.sparse as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
NOTES = os.path.abspath(os.path.join(REPO, '..', 'notes'))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import treelib

D, M = sys.argv[1], sys.argv[2]
PER = int(sys.argv[3]) if len(sys.argv) > 3 else 30
mods = open(os.path.join(D, 'mods.txt')).read().split()
idx = {m: i for i, m in enumerate(mods)}
cl = np.load(os.path.join(D, f'clusters-{M}.npy'))
top = np.load(os.path.join(D, f'top-{M}.npy'))
blk = np.load(os.path.join(D, f'blocks-{M}.npy'))          # import order position
adj = sp.load_npz(os.path.join(D, 'adj.npz')).tocoo()
X = sp.load_npz(os.path.join(D, 'tfidf.npz')).tocsr()
voc = np.array(json.load(open(os.path.join(D, 'vocab.json'))))
labels = json.load(open(os.path.join(D, 'labels.json')))
merged = collections.defaultdict(list); helpers = collections.defaultdict(list)
for l in open(os.path.join(D, 'merged.tsv')):
    p = l.rstrip('\n').split('\t')
    if p[1] != '-':
        (helpers if len(p) > 2 and p[2] == 'helper' else merged)[p[1]].append(p[0])
info = {}
for l in list(open(os.path.join(NOTES, 'file_index.tsv')))[1:]:
    p = l.rstrip('\n').split('\t')
    info[p[0][:-5].replace('/', '.')] = (int(p[1]), p[5] if len(p) > 5 else '')
_, nodes = treelib.load(REPO)
node_of = {}
for n in nodes:
    for r in n.get('lean') or []:
        node_of.setdefault(r.split(':')[0][:-5].replace('/', '.'), n['id'])

K = cl.max() + 1
# cluster order: by mean import-order position of its files (basic first)
pos = np.bincount(cl, weights=blk, minlength=K) / np.bincount(cl, minlength=K)
tpos = {t: pos[np.unique(cl[top == t])].mean() for t in np.unique(top)}
theme_of = np.zeros(K, int); theme_of[cl] = top
order = sorted(range(K), key=lambda c: (tpos[theme_of[c]], pos[c]))
tord = sorted(tpos, key=tpos.get)
cid = {c: f'k{n + 1:04d}' for n, c in enumerate(order)}
tid = {t: f'th{n + 1:03d}' for n, t in enumerate(tord)}

m = cl[adj.row] != cl[adj.col]
E = collections.Counter(zip(cl[adj.row][m].tolist(), cl[adj.col][m].tolist()))
uses = collections.defaultdict(list); used_by = collections.Counter()
for (a, b), w in E.items():
    uses[a].append((w, b)); used_by[b] += 1

members = collections.defaultdict(list)
for i, c in enumerate(cl):
    members[c].append(i)


def words(rows, k=10):
    v = np.asarray(X[rows].mean(0)).ravel()
    return voc[v.argsort()[::-1][:k]].tolist()


clusters = []
for c in order:
    f = sorted(members[c], key=lambda i: blk[i])
    ms = [mods[i] for i in f]
    cs = collections.Counter(x for mm in ms for x in labels.get(mm, []))
    clusters.append({
        'id': cid[c], 'theme': tid[theme_of[c]],
        'files': ms, 'helpers': {mm: helpers[mm] for mm in ms if helpers[mm]}, 'wrappers': sum(len(merged[mm]) for mm in ms),
        'lines': sum(info.get(mm, (0, ''))[0] for mm in ms + [w for mm in ms for w in merged[mm] + helpers[mm]]),
        'folders': collections.Counter(mm.rsplit('.', 1)[0] for mm in ms).most_common(3),
        'words': words(f),
        'uses': [cid[b] for w, b in sorted(uses[c], reverse=True)],
        'uses_weight': [w for w, b in sorted(uses[c], reverse=True)],
        'used_by': used_by[c],
        'concepts': [x for x, _ in cs.most_common(5)],
        'mapped_nodes': sorted({node_of[mm] for mm in ms if mm in node_of}),
    })
themes = []
for t in tord:
    rows = np.flatnonzero(top == t)
    ks = [cid[c] for c in order if theme_of[c] == t]
    themes.append({'id': tid[t], 'clusters': ks, 'files': len(rows), 'words': words(rows, 12),
                   'folders': collections.Counter(mods[i].rsplit('.', 1)[0] for i in rows).most_common(5)})
json.dump({'method': M, 'themes': themes, 'clusters': clusters}, open(os.path.join(D, 'map.json'), 'w'), indent=0)

out = None
tw = {t['id']: t['words'] for t in themes}
SRC = os.path.abspath(os.path.join(REPO, '..', 'src', 'lean', 'src'))
DROP = ('import ', 'set_option', 'open ', 'namespace ', 'end ', 'noncomputable section', 'section', 'variable', 'universe')


def claim(mod, cap=1500):
    """text of a statement-wrapper file without imports and boilerplate (read as text only)."""
    try:
        t = open(os.path.join(SRC, mod.replace('.', '/') + '.lean'), encoding='utf-8', errors='replace').read()
    except OSError:
        return ''
    ls = [l.rstrip() for l in t.split('\n') if l.strip() and not l.lstrip().startswith(DROP) and not l.strip().startswith('--')]
    out = ' '.join(' '.join(ls).split())
    return out[:cap] + (' …' if len(out) > cap else '')


sj = os.path.join(D, 'statements.json')
STMT, seen_n = {}, collections.Counter()
for full, txt in (json.load(open(sj)).items() if os.path.exists(sj) else []):
    parts = full.split('.')
    for n in range(1, len(parts) + 1):
        key = '.'.join(parts[-n:]); seen_n[key] += 1; STMT.setdefault(key, txt)
STMT = {k: v for k, v in STMT.items() if seen_n[k] == 1}     # drop names shared by several claims
REF = re.compile(r"([A-Za-z_][\w'.₀-₉]*Statement)\b")
PROPN = {n for n in STMT if '.' not in n or n.count('.') == 1}   # short names of Prop claims
hp = os.path.join(D, 'hints.json'); hints = json.load(open(hp)) if os.path.exists(hp) else {}
FRAC = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0      # share of files shown per cluster
OUTN = sys.argv[6] if len(sys.argv) > 6 else 'naming'
MINU = int(sys.argv[7]) if len(sys.argv) > 7 else 8
INDEG = np.asarray(adj.tocsr().sum(0)).ravel()


def pick(k):
    """most central (TF-IDF) and most imported units, about FRAC of the files, at least 8."""
    ms = k['files']; nf = len(ms) + sum(len(v) for v in k['helpers'].values())
    want = max(MINU, int(np.ceil(FRAC * nf)))
    if FRAC >= 1 or want >= len(ms):
        return ms
    r = [idx[m] for m in ms]
    V = X[r].toarray(); V /= np.maximum(np.linalg.norm(V, axis=1, keepdims=True), 1e-9)
    sim = V @ V.mean(0); S = V @ V.T
    used = list(np.argsort(-INDEG[r]))
    out = []
    while len(out) < want:
        # alternate: a central-but-different file (maximal marginal relevance), then the most imported unused file
        rest = [i for i in range(len(ms)) if i not in out]
        red = S[np.ix_(rest, out)].max(1) if out else np.zeros(len(rest))
        out.append(rest[int(np.argmax(0.5 * sim[rest] - 0.5 * red))])
        while used and used[0] in out: used.pop(0)
        if used and len(out) < want: out.append(used.pop(0))
    return [ms[i] for i in sorted(out)]


def render(k):
    shown = set()
    sel = pick(k)

    def claims(mm):
        h = info.get(mm, (0, ''))[1]
        d = re.match(r"(?:noncomputable\s+)?def\s+([^\s:({\[]+)", h)
        if d and ': Prop' in h:                       # the file's own claim: show its full text
            t = STMT.get(d.group(1))
            if t and t not in shown:
                shown.add(t); L.append(f"  - (claim text) {t}")
        for ref in REF.findall(h)[:4] + [w for w in re.findall(r"[A-Z][\w'.]*", h) if w in PROPN][:3]:
            t = STMT.get(ref)
            if t and t not in shown and not h.lstrip().startswith(('def ' + ref, 'def ' + ref.split('.')[-1])):
                shown.add(t); L.append(f"  - (claim {ref}) {t}")
    L = [f"## {k['id']}  (theme {k['theme']}: {' '.join(tw[k['theme']][:6])})"]
    nh = sum(len(v) for v in k['helpers'].values())
    L.append(f"{len(k['files']) + nh} files (+{k['wrappers']} statement wrappers), {k['lines']} lines. "
             f"Folders: {', '.join(f'{a} ({b})' for a, b in k['folders'])}")
    L.append(f"Frequent words: {' '.join(k['words'])}")
    if k['concepts']:
        L.append(f"Concepts already linked from files here: {', '.join(k['concepts'])}")
    for hnt in hints.get(k['id'], []):
        L.append(f"Literature hint (from word matching; check it fits): {hnt}")
    if k['uses']:
        L.append(f"Uses clusters (strongest first): {', '.join(k['uses'][:6])}")
    nf = len(k['files']) + nh
    note = '' if len(sel) == len(k['files']) else (f' SAMPLE: {len(sel)} of {len(k["files"])} units shown '
            f'(the most central and the most used); describe the whole cluster from them and the frequent words')
    L.append('Files (name: main statement; indented lines are claims it refers to, wrapper claims, and helper files):' + note)
    for mm in sel:
        L.append(f"- {mm.split('.')[-1]}: {' '.join(info.get(mm, (0, ''))[1].split())}")
        claims(mm)
        ws, hs = merged.get(mm, []), k['helpers'].get(mm, [])
        cap = None if FRAC >= 1 else 2          # sampled mode: 2 wrapper claims, 2 helpers per unit
        for ww in ws[:cap]:
            L.append(f"  - (claim, from {ww.split('.')[-1]}) {claim(ww, 1500 if cap is None else 700)}")
        for hh in hs[:cap]:
            L.append(f"  - (helper) {hh.split('.')[-1]}: {' '.join(info.get(hh, (0, ''))[1].split())}")
            claims(hh)
        if cap and (len(ws) > cap or len(hs) > cap):
            more = [x.split('.')[-1] for x in ws[cap:] + hs[cap:]]
            L.append(f"  - (+{len(more)} more files in this unit: {', '.join(more[:12])}{' …' if len(more) > 12 else ''})")
    return '\n'.join(L) + '\n'


out = os.path.join(D, OUTN); os.makedirs(out, exist_ok=True)
BUDGET = int(sys.argv[4]) if len(sys.argv) > 4 else 80000   # tokens per bundle (~4 chars each)
texts = [(k, render(k)) for k in clusters]
groups, cur, size = [], [], 0
for k, t in texts:
    n = len(t) // 4
    if cur and (size + n > BUDGET or len(cur) >= PER or (k['theme'] != cur[-1][0]['theme'] and size > BUDGET // 2)):
        groups.append(cur); cur, size = [], 0
    cur.append((k, t)); size += n
if cur: groups.append(cur)
for f in os.listdir(out):
    if f.startswith('bundle-') and f.endswith('.md'): os.remove(os.path.join(out, f))
tok = []
for g, kt in enumerate(groups, 1):
    text = f'# Naming bundle {g:04d}: {len(kt)} clusters\n\n' + '\n'.join(t for _, t in kt)
    open(os.path.join(out, f'bundle-{g:04d}.md'), 'w').write(text)
    tok.append(len(text) // 4)
print(f'{len(themes)} themes, {len(clusters)} clusters, {len(groups)} bundles; '
      f'bundle tokens median {int(np.median(tok))} max {max(tok)} total {sum(tok) // 1000}k')
loops = sum(1 for (a, b) in E if (b, a) in E) // 2
print(f'cluster uses-links {len(E)}, of which {loops} pairs use each other directly')
