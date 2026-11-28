#!/usr/bin/env python3
"""Split the mini-clusters that span more than one chapter of Naskręcki's handout along his notes.

Input (made by analyze.py and the Naskręcki mapping): declarations.tsv, edges.tsv,
naskrecki/concordance_matches.tsv, naskrecki/note_chapters.json.
Seeds: a cone declaration matched to a declaration of a note's own unit ("in_unit") gets that note.
Inside each mixed cluster the other declarations take a note from their neighbours inside the cluster
(statement uses count 2, proof uses 1), round by round. Declarations no seed reaches, and (variant
"shared") declarations whose neighbours disagree, form one leftover part of the cluster.
Parts of one old cluster that end up on a common cycle of the part graph are merged back until the
part graph has no cycles. Run:  python3 data/scripts/refine_naskrecki.py
"""
import collections, csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get('SERNAU_SPLIT_DATA', os.path.dirname(HERE))
NK = os.path.join(DATA, 'naskrecki')
sys.setrecursionlimit(100000)

DEFK = {'def', 'structure', 'class', 'inductive', 'opaque', 'axiom'}
decl = {r['name']: r for r in csv.DictReader(open(os.path.join(DATA, 'declarations.tsv')), delimiter='\t')}
cone = {n for n, r in decl.items() if r['in_cone'] == '1'}
cluster = {n: decl[n]['cluster'] for n in cone}
isdef = lambda n: decl[n]['kind'] in DEFK
succ = collections.defaultdict(set); T = collections.defaultdict(set)
for r in csv.DictReader(open(os.path.join(DATA, 'edges.tsv')), delimiter='\t'):
    u, v = r['source'], r['target']
    if u in cone and v in cone and u != v:
        succ[u].add(v)
        if r['kind'] == 'statement':
            T[u].add(v)

nc = json.load(open(os.path.join(NK, 'note_chapters.json')))
chapter = nc['chapter']
seed_votes = collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(os.path.join(NK, 'concordance_matches.tsv')), delimiter='\t'):
    if r['in_unit'] == 'True' and r['match'] in cone:
        seed_votes[r['match']][r['note']] += 1
seed = {n: c.most_common(1)[0][0] for n, c in seed_votes.items()}


def scc(nodes, nbr):
    idx, low, on, st, out, i = {}, {}, set(), [], [], [0]
    for s in nodes:
        if s in idx:
            continue
        work = [(s, iter(nbr.get(s, ())))]
        idx[s] = low[s] = i[0]; i[0] += 1; st.append(s); on.add(s)
        while work:
            v, it = work[-1]
            for w in it:
                if w not in idx:
                    idx[w] = low[w] = i[0]; i[0] += 1; st.append(w); on.add(w)
                    work.append((w, iter(nbr.get(w, ())))); break
                elif w in on:
                    low[v] = min(low[v], idx[w])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == idx[v]:
                    comp = []
                    while True:
                        w = st.pop(); on.discard(w); comp.append(w)
                        if w == v:
                            break
                    out.append(comp)
    return out

# declarations on a common cycle must stay together
dcomp = {}
for comp in scc(sorted(cone), succ):
    for n in comp:
        dcomp[n] = comp[0]

members = collections.defaultdict(list)
for n in cone:
    members[cluster[n]].append(n)
chap_of = collections.defaultdict(collections.Counter)
for n, note in seed.items():
    chap_of[cluster[n]][chapter[note]] += 1
MIXED = sorted(c for c, v in chap_of.items() if len(v) > 1)


def split(variant):
    P = dict(cluster)
    for c in MIXED:
        mem = set(members[c])
        lab = {n: seed[n] for n in mem if n in seed}
        # a block of mutually dependent declarations takes one note
        blocks = collections.defaultdict(list)
        for n in mem:
            blocks[dcomp[n]].append(n)
        for b, ns in blocks.items():
            vs = collections.Counter(lab[n] for n in ns if n in lab)
            if vs:
                for n in ns:
                    lab[n] = vs.most_common(1)[0][0]
        nb = collections.defaultdict(collections.Counter)
        for u in mem:
            for v in succ[u] & mem:
                w = 2 if v in T[u] else 1
                nb[u][v] += w; nb[v][u] += w
        undecided = set()
        while True:
            new = {}
            for n in mem:
                if n in lab or n in undecided:
                    continue
                votes = collections.Counter()
                for m, w in nb[n].items():
                    if m in lab and lab[m] != '·shared':
                        votes[lab[m]] += w
                if not votes:
                    continue
                top, k = votes.most_common(1)[0]
                if variant == 'shared' and k < 0.6 * sum(votes.values()):
                    new[n] = '·shared'
                else:
                    new[n] = top
            if not new:
                break
            for b in {dcomp[n] for n in new}:  # keep blocks whole
                vs = collections.Counter(new[n] for n in blocks[b] if n in new)
                for n in blocks[b]:
                    if n not in lab:
                        lab[n] = vs.most_common(1)[0][0]
        for n in mem:
            P[n] = f'{c}#{lab.get(n, "·rest")}'
    return unmerge_cycles(P)


def unmerge_cycles(P):
    # merge parts of one old cluster that share a cycle, until the part graph is acyclic
    merges = 0
    while True:
        ps = collections.defaultdict(set)
        for u in cone:
            for v in succ[u]:
                if P[u] != P[v]:
                    ps[P[u]].add(P[v])
        cyc = [comp for comp in scc(sorted(set(P.values())), ps) if len(comp) > 1]
        if not cyc:
            break
        ren = {}
        for comp in cyc:
            by = collections.defaultdict(list)
            for p in comp:
                by[p.split('#')[0]].append(p)
            for orig, plist in by.items():
                if len(plist) > 1:
                    tgt = '+'.join(sorted({p.split('#', 1)[1] for p in plist if '#' in p}))
                    for p in plist:
                        ren[p] = f'{orig}#{tgt}'
        if not ren:
            raise SystemExit('cycle across old clusters: should not happen')
        merges += 1
        P = {n: ren.get(p, p) for n, p in P.items()}
    return P, merges


MIN_PART = 0


def split_upset(coarse, down=False):
    """Label each declaration by the set of notes whose seeds reach it (inside its old cluster).
    A use u -> v implies up(u) is a subset of up(v), so parts ordered by inclusion have no cycles.
    Paths between members of one old cluster never leave it (the old cluster DAG is acyclic).
    coarse=True keeps one part per single note and puts every larger set into one 'shared' part
    (still acyclic: no use goes from a larger set to a single note). Declarations no seed reaches
    form a 'top' part, which only other top declarations can use."""
    P = dict(cluster)
    for c in MIXED:
        mem = set(members[c])
        pred = collections.defaultdict(set)
        for u in mem:
            for v in succ[u] & mem:
                pred[v].add(u)
        up = collections.defaultdict(set)
        # forward search from each note's seeds along uses
        notes = collections.defaultdict(list)
        for n in mem:
            if n in seed:
                notes[seed[n]].append(n)
        for note, ss in notes.items():
            st, seen = list(ss), set()
            while st:
                x = st.pop()
                if x in seen:
                    continue
                seen.add(x); up[x].add(note)
                st.extend(succ[x] & mem)
        dn = collections.defaultdict(set)
        if down:  # notes whose seeds a declaration reaches; only needed for the top part
            for note, ss in notes.items():
                st, seen = list(ss), set()
                while st:
                    x = st.pop()
                    if x in seen:
                        continue
                    seen.add(x); dn[x].add(note)
                    st.extend(pred[x])
        for n in mem:
            S = up.get(n)
            if not S:
                lab = next(iter(dn[n])) if len(dn.get(n, ())) == 1 else '·top'
            elif len(S) == 1:
                lab = next(iter(S))
            else:
                lab = '·shared' if coarse else '+'.join(sorted(S))
            P[n] = f'{c}#{lab}'
        if MIN_PART and coarse and not down:  # small single-note parts join the shared part (stays acyclic)
            sz = collections.Counter(P[n] for n in mem)
            for n in mem:
                lab = P[n].split('#', 1)[1]
                if not lab.startswith('·') and sz[P[n]] < MIN_PART:
                    P[n] = f'{c}#·shared'
    return unmerge_cycles(P) if down else (P, 0)


def evaluate(P):
    cross_edges = 0; used = set(); stmt_defs = set(); pe = set()
    for u in cone:
        for v in succ[u]:
            if P[u] != P[v]:
                cross_edges += 1; used.add(v); pe.add((P[u], P[v]))
                if v in T[u] and isdef(v):
                    stmt_defs.add(v)
    sizes = collections.Counter(P.values())
    mixed = 0
    pc = collections.defaultdict(set)
    for n, note in seed.items():
        pc[P[n]].add(chapter[note])
    mixed = sum(1 for s in pc.values() if len(s) > 1)
    pn = collections.defaultdict(set)
    for n, note in seed.items():
        pn[P[n]].add(note)
    ps = collections.defaultdict(set)
    for a, b in pe:
        ps[a].add(b)
    cyc = sum(len(c) for c in scc(sorted(sizes), ps) if len(c) > 1)
    return {'parts_in_cycles': cyc, 'parts': len(sizes), 'part_edges': len(pe), 'cross_decl_edges': cross_edges,
            'distinct_cross_defs': sum(1 for v in used if isdef(v)),
            'distinct_cross_defs_in_statements': len(stmt_defs),
            'distinct_cross_theorems': sum(1 for v in used if decl[v]['kind'] == 'theorem'),
            'parts_spanning_chapters': mixed,
            'parts_spanning_notes': sum(1 for s in pn.values() if len(s) > 1),
            'size_median': sorted(sizes.values())[len(sizes) // 2], 'size_max': max(sizes.values())}


res = {'before': evaluate(cluster)}
out = {}
for variant in ('majority', 'shared', 'upset_coarse', 'upset_fine', 'upset_down', 'upset_coarse_min5'):
    MIN_PART = 5 if variant == 'upset_coarse_min5' else 0
    P, merges = split(variant) if variant in ('majority', 'shared') else split_upset(variant != 'upset_fine', variant == 'upset_down')
    res[variant] = evaluate(P); res[variant]['cycle_merge_rounds'] = merges
    out[variant] = P
    per = []
    for c in MIXED:
        parts = collections.Counter(P[n] for n in members[c])
        per.append({'cluster': c, 'size': len(members[c]), 'chapters': dict(chap_of[c]),
                    'parts': {p.split('#', 1)[1] if '#' in p else p: k for p, k in parts.most_common()}})
    res[variant + '_per_cluster'] = per
json.dump(res, open(os.path.join(NK, 'refine_summary.json'), 'w'), indent=1, ensure_ascii=False)
for variant, P in out.items():
    with open(os.path.join(DATA, f'parts_N_naskrecki_{variant}.tsv'), 'w') as f:
        f.write('declaration\tpart\n')
        for n in sorted(P):
            f.write(f'{n}\t{P[n]}\n')
print(json.dumps({k: v for k, v in res.items() if not k.endswith('per_cluster')}, indent=1))
print('mixed clusters:', len(MIXED))
