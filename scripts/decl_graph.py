"""Approximate declaration-level dependency graph, read as text only (no Lean run).

usage: python -I decl_graph.py <lean/src> <root_decl> <outdir>

Pass 1 indexes every project declaration (full name -> file, line span), tracking
`namespace`/`section`/`end`. Pass 2 walks breadth-first from <root_decl>: it takes each
declaration's text, pulls out identifier tokens and resolves them the way Lean mostly does
(current namespace and its parents, `open`ed namespaces, the root). Dotted tokens that
don't resolve (usually `x.foo` field notation) fall back to a unique suffix match.

This is an approximation. It misses references Lean makes implicitly: instances,
coercions, tactics such as simp lemmas found automatically, and macro-generated
declarations. It can also add a few false edges. Treat the counts as "about".
Writes nodes.tsv (name, file, line, depth, kind, n_children) and edges.tsv.
"""
import os, re, sys, collections, pickle

src, root, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(outdir, exist_ok=True)

DECL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|scoped|partial|unsafe|nonrec)\s+)*"
                  r"(theorem|lemma|def|abbrev|structure|class|instance|inductive)\s+([^\s:({\[⦃]+)")
FIELD = re.compile(r"^\s+([^\W\d][\w'!?₀-₉]*)\s*:")
CTOR = re.compile(r"^\s*\|\s*([^\W\d][\w'!?₀-₉]*)")
TOK = re.compile(r"[^\W\d][\w'!?₀-₉ₐ-ₜ.]*")
CONT = ('|', 'where', 'termination_by', 'decreasing_by', ')', ']', '}', '⟩')

# ---------- pass 1: index ----------
cache = os.path.join(outdir, 'index.pkl')
if os.path.exists(cache):
    index, opens_of = pickle.load(open(cache, 'rb'))
else:
    index = {}      # full name -> (file, start, end, kind)
    opens_of = {}   # file -> list of opened namespaces
    for dp, _, fs in os.walk(src):
        for f in fs:
            if not f.endswith('.lean'):
                continue
            rel = os.path.relpath(os.path.join(dp, f), src)
            lines = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read().split('\n')
            stack, opens, cur = [], [], None   # stack of (kind, name)

            def close(cur, end):
                if cur:
                    n, s, k = cur
                    index[n] = (rel, s, end, k)

            for i, ln in enumerate(lines, 1):
                if not ln or ln[0] in ' \t' or ln.startswith(CONT):
                    if cur and cur[2] in ('structure', 'class', 'inductive'):
                        m = FIELD.match(ln) or CTOR.match(ln)
                        if m:
                            index.setdefault(cur[0] + '.' + m.group(1), (rel, i, i, 'field'))
                    continue
                close(cur, i - 1); cur = None
                w = ln.split()
                if w[0] == 'namespace' and len(w) > 1:
                    stack.append(('ns', w[1]))
                elif w[0] in ('section', 'noncomputable') and 'section' in w[:2]:
                    stack.append(('sec', ''))
                elif w[0] == 'end':
                    if stack:
                        stack.pop()
                elif w[0] == 'open':
                    opens += [x for x in w[1:] if x not in ('scoped', 'in', 'Classical') and not x.startswith('(')]
                else:
                    m = DECL.match(ln)
                    if m and m.group(2):
                        kind, name = m.group(1), m.group(2)
                        if name.startswith('_root_.'):
                            full = name[7:]
                        else:
                            ns = '.'.join(x for k, x in stack if k == 'ns')
                            full = f"{ns}.{name}" if ns else name
                        cur = (full, i, kind)
            close(cur, len(lines))
            opens_of[rel] = sorted(set(opens))
    pickle.dump((index, opens_of), open(cache, 'wb'))
print(f"indexed {len(index):,} project declarations")

by_last = collections.defaultdict(list)
for n in index:
    by_last[n.rsplit('.', 1)[-1]].append(n)

# ---------- pass 2: walk ----------
filecache = {}


def text(name):
    f, s, e, _ = index[name]
    if f not in filecache:
        if len(filecache) > 2000:
            filecache.clear()
        filecache[f] = open(os.path.join(src, f), encoding='utf-8', errors='replace').read().split('\n')
    return '\n'.join(filecache[f][s - 1:e])


def resolve(tok, ctx, opens):
    parts = ctx.split('.')
    for k in range(len(parts) - 1, -1, -1):           # ctx namespaces, innermost first, then root
        cand = '.'.join(parts[:k] + [tok]) if k else tok
        if cand in index:
            return [cand]
    hits = [f"{o}.{tok}" for o in opens if f"{o}.{tok}" in index]
    if hits:
        return hits
    if '.' in tok:                                     # field notation: x.foo -> *.foo if unique
        c = by_last.get(tok.rsplit('.', 1)[-1], [])
        if len(c) == 1:
            return c
    return []


depth, edges, unres = {root: 0}, [], collections.Counter()
q = collections.deque([root])
while q:
    n = q.popleft()
    body = text(n)
    body = body.split(':=', 1)[0] + ' ' + body.split(':=', 1)[-1] if ':=' in body else body
    toks = set(t.rstrip('.') for t in TOK.findall(body))
    toks.discard(n)
    kids = set()
    for t in toks:
        r = resolve(t, n, opens_of[index[n][0]])
        if not r and t[0].isupper():
            unres[t.split('.')[0]] += 1
        kids.update(x for x in r if x != n)
    for c in sorted(kids):
        edges.append((n, c))
        if c not in depth:
            depth[c] = depth[n] + 1
            q.append(c)

nkids = collections.Counter(a for a, _ in edges)
with open(os.path.join(outdir, 'nodes.tsv'), 'w') as fh:
    fh.write('name\tfile\tline\tdepth\tkind\tn_children\n')
    for n in sorted(depth, key=lambda x: (depth[x], x)):
        f, s, _, k = index[n]
        fh.write(f"{n}\t{f}\t{s}\t{depth[n]}\t{k}\t{nkids[n]}\n")
with open(os.path.join(outdir, 'edges.tsv'), 'w') as fh:
    fh.write('from\tto\n')
    fh.writelines(f"{a}\t{b}\n" for a, b in edges)

files = {index[n][0] for n in depth}
print(f"reached {len(depth):,} declarations in {len(files):,} files; {len(edges):,} edges; "
      f"max depth {max(depth.values())}")
print('by top folder:', collections.Counter(index[n][0].split('/')[0] for n in depth).most_common())
print('depth histogram:', sorted(collections.Counter(depth.values()).items()))
