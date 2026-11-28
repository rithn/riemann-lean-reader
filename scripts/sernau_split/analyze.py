#!/usr/bin/env python3
"""Build the declaration graph, the proof cone, the mini-cluster DAG and the split metrics.

Input : data/raw/decls.jsonl (from Extract.lean) and the pinned source tree.
Output: data/*.tsv, data/*.json (see report.md, section "Files").

Run:  uv run --no-project python data/scripts/analyze.py
"""
import collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get('SERNAU_SPLIT_DATA', os.path.dirname(HERE))
SRC = os.environ.get('SERNAU_SPLIT_SOURCE')
COMMIT = '72fead102f663d5c7a407964a13dc0cf9d977207'
GH = f'https://github.com/lsernau/grh-lean/blob/{COMMIT}/grh/src/'
RAW = os.environ.get('RAW', os.path.join(DATA, 'raw', 'decls.jsonl'))
OUTDIR = os.environ.get('OUT', DATA)
ROOTS = ['riemannHypothesis', 'riemannZeta_eq_zero_re', 'LFunction_ne_zero_of_half_lt_re',
         'LFunction_eq_zero_re', 'LFunction_eq_zero_re_of_isPrimitive']
DEFKINDS = {'def', 'opaque', 'induct', 'axiom', 'quot'}


def modpath(m):
    return m.replace('.', '/') + '.lean'


def srcfile(m):
    # the pinned copy keeps grh/src's contents at the top level
    return os.path.join(SRC, modpath(m))


_lines = {}


def lines_of(m):
    if m not in _lines:
        try:
            _lines[m] = open(srcfile(m), encoding='utf-8').read().split('\n')
        except FileNotFoundError:
            _lines[m] = []
    return _lines[m]


OPEN, CLOSE = '([{⦃⟨', ')]}⦄⟩'


def split_decl(m, r):
    """Return (docstring, statement text) of the declaration at range r (1-based lines)."""
    L = lines_of(m)
    text = '\n'.join(L[r[0] - 1:r[2]])
    doc = ''
    mdoc = re.match(r'\s*/--(.*?)-/\s*', text, re.S)
    if mdoc:
        doc = ' '.join(mdoc.group(1).split())
        text = text[mdoc.end():]
    # statement: up to the first top-level ':=' or ' where' or a top-level '|' line
    depth, i, n = 0, 0, len(text)
    cut = n
    while i < n:
        c = text[i]
        if c in OPEN:
            depth += 1
        elif c in CLOSE:
            depth = max(0, depth - 1)
        elif depth == 0:
            if text.startswith(':=', i):
                cut = i
                break
            if text.startswith('\n', i):
                rest = text[i + 1:]
                if re.match(r'\s*\|\s', rest) or re.match(r'\s*where\b', rest):
                    cut = i
                    break
            if text.startswith(' where', i) and (i + 6 == n or not text[i + 6].isalnum()):
                cut = i
                break
        i += 1
    stmt = text[:cut].rstrip()
    stmt = '\n'.join(stmt.split('\n')[:40])
    return doc, stmt


def load():
    D = {}
    for line in open(RAW, encoding='utf-8'):
        d = json.loads(line)
        D[d['n']] = d
    return D


def resolve_owners(D):
    """Map every constant to a user-facing owner or mark it transparent (None)."""
    owner = {}
    for n, d in D.items():
        r = d['r']
        parent = n.rsplit('.', 1)[0] if '.' in n else None
        pd = D.get(parent) if parent else None
        if d['k'] in ('ctor', 'rec') and pd and pd['k'] == 'induct':
            owner[n] = parent
        elif d.get('proj') and pd and pd['k'] == 'induct':
            owner[n] = parent
        elif r is None:
            owner[n] = None  # generated: inline its dependencies
        elif pd and pd['r'] is not None and pd['r'][:3] == r[:3] and pd['k'] == 'induct':
            owner[n] = parent
        else:
            owner[n] = n
    # chase owners to fixpoint
    def top(n):
        seen = set()
        while owner.get(n) not in (None, n) and n not in seen:
            seen.add(n)
            n = owner[n]
        return n
    for n in list(owner):
        if owner[n] is not None:
            owner[n] = top(n)
    return owner


def resolved_edges(D, owner):
    memo = {}

    def expand(x, stack=()):
        """Owners reached from constant x (x itself if user-facing)."""
        o = owner.get(x)
        if o is not None:
            return {o}
        if x in memo:
            return memo[x]
        if x in stack:
            return set()
        d = D.get(x)
        out = set()
        if d:
            for y in d['t'] + d['v']:
                out |= expand(y, stack + (x,))
        memo[x] = out
        return out

    T = collections.defaultdict(set)
    V = collections.defaultdict(set)
    for n, d in D.items():
        o = owner.get(n)
        if o is None:
            continue
        for y in d['t']:
            for z in expand(y):
                if z != o:
                    T[o].add(z)
        for y in d['v']:
            for z in expand(y):
                if z != o:
                    V[o].add(z)
    nodes = sorted({o for o in owner.values() if o is not None})
    return nodes, T, V


def scc(nodes, succ):
    index, low, onst, st, comp = {}, {}, set(), [], {}
    counter = [0]
    sys.setrecursionlimit(1000000)
    out = []
    for s in nodes:
        if s in index:
            continue
        work = [(s, iter(sorted(succ.get(s, ()))))]
        index[s] = low[s] = counter[0]; counter[0] += 1; st.append(s); onst.add(s)
        while work:
            v, it = work[-1]
            adv = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter[0]; counter[0] += 1; st.append(w); onst.add(w)
                    work.append((w, iter(sorted(succ.get(w, ())))))
                    adv = True
                    break
                elif w in onst:
                    low[v] = min(low[v], index[w])
            if adv:
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                c = []
                while True:
                    w = st.pop(); onst.discard(w); c.append(w)
                    if w == v:
                        break
                out.append(c)
                for w in c:
                    comp[w] = len(out) - 1
    return out, comp


def topo(nodes, succ):
    """Users before used (roots first)."""
    indeg = collections.Counter()
    for u in nodes:
        for v in succ.get(u, ()):
            indeg[v] += 1
    q = collections.deque(sorted(u for u in nodes if indeg[u] == 0))
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in sorted(succ.get(u, ())):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    assert len(order) == len(nodes), 'graph not acyclic'
    return order


class Clusters:
    """Union of declarations into clusters with exact reachability bitsets on the cluster DAG."""

    def __init__(self, nodes, succ, cid):
        self.cid = dict(cid)  # node -> cluster id
        self.members = collections.defaultdict(set)
        for n, c in self.cid.items():
            self.members[c].add(n)
        self.csucc = collections.defaultdict(set)
        self.cpred = collections.defaultdict(set)
        for u in nodes:
            for v in succ.get(u, ()):
                a, b = self.cid[u], self.cid[v]
                if a != b:
                    self.csucc[a].add(b); self.cpred[b].add(a)
        ids = sorted(self.members)
        self.bit = {c: i for i, c in enumerate(ids)}
        order = topo(ids, self.csucc)
        self.desc = {}
        for c in reversed(order):
            m = 0
            for s in self.csucc[c]:
                m |= self.desc[s] | (1 << self.bit[s])
            self.desc[c] = m

    def reaches(self, a, b):
        return bool(self.desc[a] >> self.bit[b] & 1)

    def can_merge(self, a, b):
        """Merging a and b keeps the cluster graph acyclic."""
        if a == b:
            return False
        for x, y in ((a, b), (b, a)):
            for s in self.csucc[x]:
                if s != y and self.reaches(s, y):
                    return False
        return True

    def merge(self, a, b):
        """Merge b into a (caller checked can_merge)."""
        for n in self.members[b]:
            self.cid[n] = a
        self.members[a] |= self.members.pop(b)
        for s in self.csucc.pop(b, set()):
            self.cpred[s].discard(b)
            if s != a:
                self.csucc[a].add(s); self.cpred[s].add(a)
        for p in self.cpred.pop(b, set()):
            self.csucc[p].discard(b)
            if p != a:
                self.csucc[p].add(a); self.cpred[a].add(p)
        self.csucc[a].discard(a); self.cpred[a].discard(a)
        ba, bb = 1 << self.bit[a], 1 << self.bit[b]
        newdesc = (self.desc[a] | self.desc.pop(b)) & ~ba & ~bb
        self.desc[a] = newdesc
        for c, m in self.desc.items():
            if c != a and (m & ba or m & bb):
                self.desc[c] = (m | newdesc | ba) & ~bb


def main():
    D = load()
    owner = resolve_owners(D)
    nodes, T, V = resolved_edges(D, owner)
    succ = {u: T[u] | V[u] for u in nodes}
    info = {n: D[n] for n in nodes}

    # proof cone
    roots = [r for r in ROOTS if r in succ]
    if os.environ.get('TEST_ALL_ROOTS'):
        used = set().union(*succ.values())
        roots = [u for u in nodes if u not in used]
    cone, stack = set(), list(roots)
    missing = [r for r in ROOTS if r not in succ]
    while stack:
        u = stack.pop()
        if u in cone:
            continue
        cone.add(u)
        stack.extend(succ[u])
    cone_named = set(cone)
    # instances are found by instance search, never by name: add an instance once every project
    # declaration in its statement is in the cone, then everything it uses (repeat to a fixpoint)
    via_instance = set()
    if not os.environ.get('NO_INSTANCES'):
        changed = True
        while changed:
            changed = False
            for u in nodes:
                if u in cone or not info[u]['inst']:
                    continue
                if T[u] <= cone:
                    stack = [u]
                    while stack:
                        x = stack.pop()
                        if x in cone:
                            continue
                        cone.add(x); via_instance.add(x); changed = True
                        stack.extend(succ[x])
    # condense any cycles (mutual blocks, owner folding)
    comps, comp = scc(sorted(cone), {u: succ[u] & cone for u in cone})
    big = [c for c in comps if len(c) > 1]
    rep = {}
    for c in comps:
        h = sorted(c)[0]
        for n in c:
            rep[n] = h
    G = collections.defaultdict(set)
    for u in cone:
        for v in succ[u] & cone:
            if rep[u] != rep[v]:
                G[rep[u]].add(rep[v])
    gnodes = sorted(set(rep.values()))
    order = topo(gnodes, G)
    preds = collections.defaultdict(set)
    for u in gnodes:
        for v in G[u]:
            preds[v].add(u)

    # Stage 1: Sernau's files as a guide. Split each file into the pieces that are joined by
    # dependencies inside the file. A file's declarations come before their users in the file,
    # and files import each other without cycles, so this partition is already acyclic.
    par = {n: n for n in gnodes}
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for u in gnodes:
        for v in G[u]:
            if info[u]['m'] == info[v]['m']:
                par[find(u)] = find(v)
    cid = {u: find(u) for u in gnodes}
    stage1 = len(set(cid.values()))

    # Stage 2: greedy modularity agglomeration (Clauset-Newman-Moore) on the undirected weighted
    # graph, merging only clusters whose union keeps the cluster graph acyclic.
    GAMMA = float(os.environ.get('GAMMA', '5'))
    W_STMT = float(os.environ.get('W_STMT', '2'))
    C = Clusters(gnodes, G, cid)
    W = collections.defaultdict(lambda: collections.defaultdict(float))
    deg = collections.defaultdict(float)
    mtot = 0.0
    for u in gnodes:
        for v in G[u]:
            w = W_STMT if v in T.get(u, ()) or any(v == rep.get(x) for x in T.get(u, ())) else 1.0
            a_, b_ = C.cid[u], C.cid[v]
            deg[a_] += w; deg[b_] += w; mtot += w
            if a_ != b_:
                W[a_][b_] += w; W[b_][a_] += w
    import heapq
    def gain(x, y):
        return W[x][y] / mtot - GAMMA * deg[x] * deg[y] / (2 * mtot * mtot)
    ver = collections.Counter()
    heap = []
    for x in list(W):
        for y, w in W[x].items():
            if x < y:
                heap.append((-gain(x, y), x, y, 0, 0))
    heapq.heapify(heap)
    merges = rejected = 0
    while heap:
        g, x, y, vx, vy = heapq.heappop(heap)
        if x not in C.members or y not in C.members or ver[x] != vx or ver[y] != vy:
            continue
        if -g <= 0:
            break
        if not C.can_merge(x, y):
            rejected += 1
            continue
        C.merge(x, y)
        merges += 1
        for z, w in W.pop(y).items():
            del W[z][y]
            if z != x:
                W[x][z] += w; W[z][x] += w
        W[x].pop(x, None)
        deg[x] += deg.pop(y)
        ver[x] += 1
        for z in W[x]:
            a_, b_ = (x, z) if x < z else (z, x)
            heapq.heappush(heap, (-gain(a_, b_), a_, b_, ver[a_], ver[b_]))
    stage2 = len(C.members)
    rounds = merges


    # expand SCC representatives back
    final = {}
    for n in cone:
        final[n] = C.cid[rep[n]]
    clusters = collections.defaultdict(set)
    for n, c in final.items():
        clusters[c].add(n)
    # name each cluster after its head: the member from which most of the cluster is reachable
    # (ties: more users outside the cluster, then the later line in the file)
    rename = {}
    for c, mem in clusters.items():
        best = None
        for u in mem:
            seen, st = set(), [u]
            while st:
                x = st.pop()
                for y in succ[x]:
                    if y in mem and y not in seen:
                        seen.add(y); st.append(y)
            ext = sum(1 for p in cone if final.get(p) != c and u in succ[p]) if len(mem) < 400 else 0
            key = (len(seen), ext, info[u]['r'][0] if info[u]['r'] else 0)
            if best is None or key > best[0]:
                best = (key, u)
        rename[c] = best[1]
    final = {n: rename[c] for n, c in final.items()}
    clusters = {rename[c]: mem for c, mem in clusters.items()}

    # ---- per-declaration table
    os.makedirs(OUTDIR, exist_ok=True)
    def link(n):
        d = info[n]
        line = d['r'][4] if d['r'] and len(d['r']) > 4 else (d['r'][0] if d['r'] else 1)
        return f"{GH}{modpath(d['m'])}#L{line}"
    def isdef(n):
        d = info[n]
        if d['inst']:
            return False
        return d['k'] in DEFKINDS or d['struct'] or d['cls']
    def isinst(n):
        return info[n]['inst']
    def kindlabel(n):
        d = info[n]
        if d['cls']: return 'class'
        if d['struct']: return 'structure'
        if d['inst']: return 'instance'
        return {'thm': 'theorem', 'def': 'def', 'opaque': 'opaque', 'induct': 'inductive',
                'axiom': 'axiom'}.get(d['k'], d['k'])
    projdefs = set(n for n in nodes if isdef(n))

    with open(os.path.join(OUTDIR, 'declarations.tsv'), 'w') as f:
        f.write('name\tkind\tmodule\tline\tin_cone\tcluster\tn_type_uses\tn_proof_uses\tn_type_project_defs\tpp_len\tlink\n')
        for n in nodes:
            d = info[n]
            tdefs = len([x for x in T[n] if x in projdefs])
            f.write('\t'.join(map(str, [n, kindlabel(n), d['m'], d['r'][0] if d['r'] else '',
                    int(n in cone), final.get(n, ''), len(T[n]), len(V[n] - T[n]), tdefs,
                    len(d['pp']), link(n)])) + '\n')
    with open(os.path.join(OUTDIR, 'edges.tsv'), 'w') as f:
        f.write('source\ttarget\tkind\n')
        for u in nodes:
            for v in sorted(T[u]):
                f.write(f'{u}\t{v}\tstatement\n')
            for v in sorted(V[u] - T[u]):
                f.write(f'{u}\t{v}\tproof\n')

    # ---- partitions to compare
    def folder(n):
        m = info[n]['m'].split('.')
        return '.'.join(m[:2])
    def file_(n):
        return info[n]['m']
    parts = {
        'A_folders': {n: folder(n) for n in cone},
        'F_files': {n: file_(n) for n in cone},
        'M_miniclusters': final,
        'S1_file_pieces': {n: cid[rep[n]] for n in cone},
    }

    def evaluate(P):
        cross = collections.defaultdict(set)  # (pa, pb) -> set of used decls in pb
        for u in cone:
            for v in succ[u] & cone:
                if P[u] != P[v]:
                    cross[(P[u], P[v])].add(v)
        used = set().union(*cross.values()) if cross else set()
        udefs = {v for v in used if isdef(v)}
        uinst = {v for v in used if isinst(v)}
        uthms = used - udefs - uinst
        # definitions that cross in a statement (the reader of the statement must know them)
        stmt_defs = {v for u in cone for v in T[u] & cone if P[u] != P[v] and isdef(v)}
        # acyclicity of the part graph
        ps = sorted(set(P.values()))
        psucc = collections.defaultdict(set)
        for (a, b) in cross:
            psucc[a].add(b)
        comps_, _ = scc(ps, psucc)
        cyc = [c for c in comps_ if len(c) > 1]
        sizes = collections.Counter(P.values())
        # per part: how many of its decls are used from outside (entries), and defs it imports
        entries = collections.defaultdict(set); imp_defs = collections.defaultdict(set)
        imp_thms = collections.defaultdict(set)
        for (a, b), vs in cross.items():
            entries[b] |= vs
            for v in vs:
                if isdef(v): imp_defs[a].add(v)
                elif not isinst(v): imp_thms[a].add(v)
        med = lambda xs: sorted(xs)[len(xs) // 2] if xs else 0
        return {
            'parts': len(ps), 'part_edges': len(cross),
            'cross_decl_edges': sum(1 for u in cone for v in succ[u] & cone if P[u] != P[v]),
            'distinct_cross_defs': len(udefs), 'distinct_cross_defs_in_statements': len(stmt_defs),
            'distinct_cross_instances': len(uinst), 'distinct_cross_theorems': len(uthms),
            'parts_in_cycles': sum(len(c) for c in cyc), 'largest_cycle': max((len(c) for c in cyc), default=0),
            'size_max': max(sizes.values()), 'size_median': med(list(sizes.values())),
            'singleton_parts': sum(1 for s in sizes.values() if s == 1),
            'median_entries_per_part': med([len(entries[p]) for p in ps]),
            'median_imported_defs_per_part': med([len(imp_defs[p]) for p in ps]),
            'max_imported_defs_per_part': max((len(imp_defs[p]) for p in ps), default=0),
        }, cross
    results = {}
    crosses = {}
    for k, P in parts.items():
        results[k], crosses[k] = evaluate(P)
        with open(os.path.join(OUTDIR, f'parts_{k}.tsv'), 'w') as f:
            f.write('declaration\tpart\n')
            for n in sorted(P):
                f.write(f'{n}\t{P[n]}\n')

    # ---- mini-cluster table
    contents = {}
    for line in open(os.path.join(SRC, 'CONTENTS.md'), encoding='utf-8'):
        m = re.match(r'- `([^`]+)` \((\d+)\): (.*)', line.strip())
        if m:
            contents[m.group(1).replace('/', '.')] = m.group(3)
    index_rows = collections.defaultdict(list)
    for line in open(os.path.join(SRC, 'INDEX.md'), encoding='utf-8'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) >= 2 and cells[1].startswith('`') and '/' in cells[1]:
            index_rows[cells[1].strip('`').replace('/', '.')].append(cells[0])

    P = final
    cross = crosses['M_miniclusters']
    cl_out = []
    succ_c = collections.defaultdict(set); pred_c = collections.defaultdict(set)
    for (a, b) in cross:
        succ_c[a].add(b); pred_c[b].add(a)
    corder = topo(sorted(clusters), succ_c)
    depth = {}
    for c in reversed(corder):
        depth[c] = 1 + max((depth[s] for s in succ_c[c]), default=-1)
    for c in corder:
        mem = clusters[c]
        entries = sorted({v for (a, b), vs in cross.items() if b == c for v in vs})
        imports = sorted({v for (a, b), vs in cross.items() if a == c for v in vs})
        files = collections.Counter(info[n]['m'] for n in mem)
        loc = sum((info[n]['r'][2] - info[n]['r'][0] + 1) for n in mem if info[n]['r'])
        hd = info[c]
        doc, stmt = split_decl(hd['m'], hd['r']) if hd['r'] else ('', '')
        cl_out.append({
            'id': c, 'head': c, 'head_kind': kindlabel(c), 'head_doc': doc, 'head_statement': stmt,
            'head_link': link(c), 'file': hd['m'], 'file_title': contents.get(hd['m'], ''),
            'index_results': index_rows.get(hd['m'], []),
            'folder': folder(c), 'size': len(mem), 'lines': loc,
            'kinds': dict(collections.Counter(kindlabel(n) for n in mem)),
            'files': dict(files), 'depth': depth[c],
            'entries': entries, 'n_entries': len(entries),
            'imports_defs': [v for v in imports if isdef(v)],
            'imports_theorems': [v for v in imports if not isdef(v) and not isinst(v)],
            'imports_instances': [v for v in imports if isinst(v)],
            'uses_clusters': sorted(succ_c[c]), 'used_by_clusters': sorted(pred_c[c]),
            'is_root': c in [rep.get(r) for r in ROOTS],
        })
    # shared vocabulary: project definitions imported by at least 5% of the clusters
    imp_count = collections.Counter(v for c in cl_out for v in c['imports_defs'])
    vthr = max(2, int(0.05 * len(cl_out)))
    vocab = sorted((v for v, k in imp_count.items() if k >= vthr), key=lambda v: -imp_count[v])
    vset = set(vocab)
    for c in cl_out:
        c['imports_defs_beyond_vocab'] = [v for v in c['imports_defs'] if v not in vset]
    with open(os.path.join(OUTDIR, 'vocabulary.tsv'), 'w') as f:
        f.write('definition\tkind\tclusters_importing\tdefined_in_cluster\tlink\n')
        for v in vocab:
            f.write(f"{v}\t{kindlabel(v)}\t{imp_count[v]}\t{final[v]}\t{link(v)}\n")
    med = lambda xs: sorted(xs)[len(xs) // 2] if xs else 0
    vocab_stats = {'threshold_clusters': vthr, 'size': len(vocab),
                   'median_imported_defs': med([len(c['imports_defs']) for c in cl_out]),
                   'median_imported_defs_beyond_vocab': med([len(c['imports_defs_beyond_vocab']) for c in cl_out]),
                   'p90_imported_defs_beyond_vocab': sorted(len(c['imports_defs_beyond_vocab']) for c in cl_out)[int(.9 * len(cl_out))],
                   'top': [(v, imp_count[v]) for v in vocab[:40]]}
    json.dump(cl_out, open(os.path.join(OUTDIR, 'miniclusters.json'), 'w'), ensure_ascii=False, indent=0)

    # cross-cluster declaration list with statements
    with open(os.path.join(OUTDIR, 'cross_minicluster.tsv'), 'w') as f:
        f.write('user_cluster\tused_cluster\tdeclaration\tkind\tleak\tedge_kinds\tproject_defs_in_statement\tstatement_chars\tlink\n')
        for (a, b), vs in sorted(cross.items()):
            for v in sorted(vs):
                ks = set()
                for u in clusters[a]:
                    if v in T[u]: ks.add('statement')
                    elif v in V[u]: ks.add('proof')
                f.write('\t'.join(map(str, [a, b, v, kindlabel(v), int(isdef(v)), ','.join(sorted(ks)),
                        len([x for x in T[v] if x in projdefs]), len(info[v]['pp']), link(v)])) + '\n')

    entry_stmts = {}
    for c in cl_out:
        for v in c['entries']:
            if v not in entry_stmts:
                d = info[v]
                doc, stmt = split_decl(d['m'], d['r']) if d['r'] else ('', '')
                entry_stmts[v] = {'kind': kindlabel(v), 'doc': doc, 'statement': stmt, 'link': link(v),
                                  'module': d['m'], 'pp': d['pp'][:1500],
                                  'project_defs_in_statement': sorted(x for x in T[v] if x in projdefs)}
    json.dump(entry_stmts, open(os.path.join(OUTDIR, 'interface_declarations.json'), 'w'), ensure_ascii=False, indent=0)

    summary = {
        'constants_in_export': len(D),
        'user_facing_declarations': len(nodes),
        'generated_constants_inlined': sum(1 for n in D if owner.get(n) is None),
        'folded_into_inductive': sum(1 for n, o in owner.items() if o not in (None, n)),
        'cone': len(cone), 'outside_cone': len(nodes) - len(cone),
        'cone_by_name_only': len(cone_named), 'added_via_instances': len(via_instance),
        'added_via_instances_by_kind': dict(collections.Counter(kindlabel(n) for n in via_instance)),
        'outside_cone_by_kind': dict(collections.Counter(kindlabel(n) for n in nodes if n not in cone)),
        'cone_by_kind': dict(collections.Counter(kindlabel(n) for n in cone)),
        'missing_roots': missing, 'cycles_condensed': [sorted(c) for c in big],
        'edges_statement': sum(len(T[u] & cone) for u in cone),
        'edges_proof_only': sum(len((V[u] - T[u]) & cone) for u in cone),
        'stage1_clusters': stage1, 'gamma': GAMMA, 'w_stmt': W_STMT, 'merges': merges, 'rejected_for_cycles': rejected, 'stage2_clusters': stage2, 
        'splits': results,
        'cluster_depth': max(depth.values()),
        'vocabulary': vocab_stats,
    }
    json.dump(summary, open(os.path.join(OUTDIR, 'summary.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(summary, indent=1, ensure_ascii=False)[:6000])


if __name__ == '__main__':
    main()
