"""Original-edition declaration, xref and reading artifacts."""

import collections
import csv
import glob
import gzip
import json
import os
import re
import time


# name links, compressed: per file the list of targets its names resolve to, plus overrides. The app links a token to
# the one target in that list whose full name is the token or ends with '.' + token (else it drops the token's last
# dotted part, as Lean reads a projection, and tries again); lvMatch() in app.js, keep in step. A token for which that
# rule gives another answer, or none, or whose target has a short name that could be a local (not _lv_safe), or that
# resolves differently on different lines, is written out: overrides {token: t index | {line: t index}}.
def _lv_safe(short):
    return len(short) >= 8 or (len(short) >= 4 and bool(re.search(r'[_0-9]|.[A-Z]', short)))
def _lv_index(cand, full):   # every dotted suffix of each candidate's full name -> candidates
    ix = collections.defaultdict(list)
    for c in cand:
        p = full[c].split('.')
        for i in range(len(p)):
            ix['.'.join(p[i:])].append(c)
    return ix
def _lv_match(tok, ix):
    s = tok
    while True:
        hits = ix.get(s, ())
        if len(hits) == 1:
            return hits[0]
        if hits or '.' not in s:
            return None
        s = s.rsplit('.', 1)[0]
def _lv_links(links, full):   # targets >= 0 are in this node (full names known); < 0 elsewhere: always written out
    cand = sorted({t for v in links.values() for t in ([v] if isinstance(v, int) else v.values()) if t >= 0})
    ix = _lv_index(cand, full)
    over = {}
    for tok, v in links.items():
        if isinstance(v, int) and v >= 0 and _lv_safe(full[v].rsplit('.', 1)[-1]) and _lv_match(tok, ix) == v:
            continue
        over[tok] = v
    return [cand, over] if over else [cand]


def build_reader_artifacts(*, OUT, LV_OUT, XREF_D, REPO, CL, overview_clusters,
                           mod_cl, members, unit_cl, module_kind, parent, fdist, importers,
                           FL, FL_PART, FL_PARTS, fl_ppath, G_MAP, _glabel):
    """Emit the original main and lazy xref shards plus the hover projection."""
    if not os.path.isfile(os.path.join(XREF_D, 'full', 'decl_stats.tsv.gz')):
        print(f'Lean viewer data: no P4 output in {XREF_D}/full, skipped')
        return None
    os.makedirs(os.path.join(LV_OUT, 'x'), exist_ok=True)
    for f in glob.glob(os.path.join(LV_OUT, '*.json')) + glob.glob(os.path.join(LV_OUT, '*.json.gz')) + glob.glob(os.path.join(LV_OUT, 'x', '*.json.gz')):
        os.remove(f)
    if os.path.exists(os.path.join(OUT, 'data', 'lean-hover.json')):
        os.remove(os.path.join(OUT, 'data', 'lean-hover.json'))
    _t0 = time.monotonic()
    LVK = {'theorem': 't', 'lemma': 'l', 'def': 'd', 'abbrev': 'a', 'instance': 'i', 'structure': 's', 'class': 'c',
           'inductive': 'n', 'alias': 'A', 'opaque': 'o', 'axiom': 'x', 'irreducible_def': 'd'}
    DSTAT = {}          # (name, module) -> [kind, start, end, stmt_end, flags, used, chain]
    MDECL = collections.defaultdict(list)
    with gzip.open(os.path.join(XREF_D, 'full', 'decl_stats.tsv.gz'), 'rt', encoding='utf-8') as fh:
        next(fh)
        for ln in fh:
            n, m, k, a, b, se, fl, u, ch = ln.rstrip('\n').split('\t')
            if m in mod_cl:
                r = (LVK.get(k, k[:1]), int(a), int(b), int(se), fl, int(u), int(ch))
                DSTAT[(n, m)] = r
                MDECL[m].append(n)
    # English titles from the blueprints (real sources only): Merten's statement title, else Naskręcki's atlas title
    _bt = {}
    _mer = {s['label']: s.get('title') for s in json.load(open(os.path.join(XREF_D, 'merten.json')))['statements']}
    _nas = {s['label']: s.get('title') for s in json.load(open(os.path.join(XREF_D, 'naskrecki.json')))['declarations']}
    # which title, when both name a declaration: a Merten statement about this declaration alone, else the atlas entry
    # (one declaration each), else a Merten statement that covers several declarations
    _rows = [r for r in csv.DictReader(open(os.path.join(XREF_D, 'blueprint_matches.tsv')), delimiter='\t') if r['status'] == 'matched']
    _nper = collections.Counter(r['label'] for r in _rows if r['source'] == 'merten')
    _rank = {}
    for r in _rows:
        t = (_mer if r['source'] == 'merten' else _nas).get(r['label'])
        key = (r['lean_name'], r['module'])
        rk = 2 if r['source'] == 'naskrecki' else 1 if _nper[r['label']] == 1 else 3
        if t and rk < _rank.get(key, 9):
            _rank[key] = rk
            _bt[key] = [t, 'b' if r['source'] == 'merten' else 'a', r['label']]
    # guide citations, unshortened (guide-decls.tsv.gz): per declaration the guides on the map that name it, per file
    # the citations (guide, page, declaration)
    _goi = {g['id']: g for g in G_MAP}
    DGUIDES = collections.defaultdict(set)
    FCITES = collections.defaultdict(list)
    def _gpage(g, k, raw):
        note, l = _glabel(g, raw)
        if note:
            return l, next((u for x, u in g['notes'].get(k, []) if x == l), None)
        url = next((u for x, u in g['refs'].get(k, []) if x == l), None)
        return ('p. ' + l if l.isdigit() else l), url
    with gzip.open(os.path.join(REPO, 'data', 'guide-decls.tsv.gz'), 'rt', encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            g = _goi.get(r['guide'])
            if not g or r['cluster'] not in CL:
                continue
            m = r['module']
            if r['kind'] == 'd':
                if (r['name'], m) not in DSTAT:
                    continue
                DGUIDES[(r['name'], m)].add(g['oi'])
            elif m not in mod_cl:
                continue
            l, u = _gpage(g, r['cluster'], r['page'])
            e = [g['oi'], l, u, r['name'].rsplit('.', 1)[-1] if r['kind'] == 'd' else '']
            if e not in FCITES[m]:
                FCITES[m].append(e)
    _ord = {g['oi']: i for i, g in enumerate(G_MAP)}
    def _pk(e):
        mm = re.match(r'p\. (\d+)', e[1])
        return (e[0], 0 if mm else 1, int(mm.group(1)) if mm else 0, e[1], e[3])
    LEAN_HOVER = {}
    _hsz = []
    for k in CL:
        # explorer order: unit heads by steps from Main (then name), each followed by its helpers along the fold tree
        mems = members[k]
        kids = collections.defaultdict(list)
        heads = []
        for m in mems:
            p = parent.get(m)
            if m in unit_cl or p not in mod_cl or mod_cl.get(p) != k:
                heads.append(m)
            else:
                kids[p].append(m)
        heads.sort(key=lambda m: (fdist.get(m) is None, fdist.get(m) or 0, m.rsplit('.', 1)[-1].lower(), m))
        order, par = [], {}
        def walk(m, pi):
            par[m] = pi
            i = len(order); order.append(m)
            for c in sorted(kids.get(m, []), key=lambda x: (x.rsplit('.', 1)[-1].lower(), x)):
                walk(c, i)
        for h in heads:
            walk(h, -1)
        OWN = {m: i for i, m in enumerate(order)}
        NS, NSI = [], {}       # namespaces of this cluster's declarations (main file)
        XNS, XNSI = [], {}     # namespaces of declarations elsewhere (lazy file)
        XM, XMI = [], {}       # modules elsewhere (lazy file)
        def tab(lst, idx, v):
            if v not in idx:
                idx[v] = len(lst); lst.append(v)
            return idx[v]
        def split(name, lst, idx):
            a, _, b = name.rpartition('.')
            return (tab(lst, idx, a) if a else -1), b
        try:
            REFS = json.load(gzip.open(os.path.join(XREF_D, 'full', 'refs', k + '.json.gz'), 'rt', encoding='utf-8'))
        except FileNotFoundError:
            REFS = {}
        # this cluster's declarations (the link targets inside the node point at them by [file, declaration] index)
        DIDX, DS = {}, []
        allD = []
        for fi_, m in enumerate(order):
            ds = []
            for n in sorted(MDECL.get(m, []), key=lambda n: DSTAT[(n, m)][1]):
                st = DSTAT[(n, m)]
                a, b = split(n, NS, NSI)
                g = len(DGUIDES.get((n, m), ()))
                row = [a, b, st[0], st[1], st[2], st[5], g, _bt.get((n, m), 0), st[6]]
                while len(row) > 6 and not row[-1]:   # trailing zeros (no title, not on the chain) are left out
                    row.pop()
                DIDX[(n, m)] = [fi_, len(ds)]
                ds.append(row)
                allD.append((n, m, st, g, (n, m) in _bt, fi_))
            DS.append(ds)
        T, TI, TF = [], {}, []   # link targets inside the node: [file, declaration]; full names for the matching rule
        E, EI = [], {}           # link targets in other nodes (lazy file); a link to one is written as -(index + 1)
        def ti(tgt, tm):
            key = (tgt, tm)
            if key in DIDX:
                if key not in TI:
                    TI[key] = len(T); T.append(DIDX[key]); TF.append(tgt)
                return TI[key]
            st = DSTAT.get(key)
            if not st:
                return None
            if key not in EI:
                a, b = split(tgt, XNS, XNSI)
                EI[key] = len(E); E.append([tab(XM, XMI, tm), a, b, st[0], st[1], st[2]])
            return -EI[key] - 1
        F, BY = [], []
        for fi_, m in enumerate(order):
            links = {}
            for tok, v in REFS.get(m, {}).items():
                if isinstance(v, list):
                    t = ti(*v)
                    if t is not None:
                        links[tok] = t
                else:
                    per = {l: ti(*x) for l, x in v.items()}
                    per = {l: t for l, t in per.items() if t is not None}
                    if per:
                        links[tok] = per
            links = _lv_links(links, TF)
            by = sorted(importers.get(m, []), key=lambda x: (fdist.get(x) is None, fdist.get(x) or 0, x))
            kd = 'u' if m in unit_cl else ('w' if module_kind.get(m) == 'wrapper' else 'h')
            F.append([par[m], kd, fdist.get(m), len(by), DS[fi_], links, sorted(FCITES.get(m, []), key=_pk)])
            BY.append([OWN[x] if x in OWN else -tab(XM, XMI, x) - 1 for x in by[:5]])
        def mods(ms):   # [folders, [[folder index, last part]]]
            fd, fdi = [], {}
            return fd, [[tab(fd, fdi, mm.rpartition('.')[0]), mm.rpartition('.')[2]] for mm in ms]
        d1, x1 = mods(order)
        d2, x2 = mods(XM)
        main = {'d': d1, 'x': x1, 'ns': NS, 'f': F, 't': T}
        if FL.get(k):   # #10 readings (core clusters only): r.p the /lean/ page parts; r.f [file index, line, reading, part, [[declaration index, gloss]]]
            rf = []
            for e in FL[k]:
                fi_ = OWN[e['module']]
                gl = [[DIDX[(x['name'], e['module'])][1], x['gloss']] for x in e['key_decls'] or [] if (x['name'], e['module']) in DIDX]
                rf.append([fi_, e['line'] if e['status'] != 'cut' else '', (e.get('reading') or '') if e['status'] != 'cut' else '',
                           FL_PART[(k, e['module'])], gl if e['status'] != 'cut' else []])
            main['r'] = {'p': [fl_ppath(k, i) for i in range(len(FL_PARTS[k]))], 'f': rf}
        lazy = {'d': d2, 'x': x2, 'ns': XNS, 'e': E, 'by': BY}
        for path, obj in ((os.path.join(LV_OUT, k + '.json.gz'), main), (os.path.join(LV_OUT, 'x', k + '.json.gz'), lazy)):
            raw = json.dumps(obj, separators=(',', ':'), ensure_ascii=False).encode()
            open(path, 'wb').write(gzip.compress(raw, 9, mtime=0))
            _hsz.append((k, path.endswith(os.path.join('x', k + '.json.gz')), len(raw), os.path.getsize(path)))
        # the top 3 ("main") declarations (decision 5, simplified 24 Nov): (a) cited by guides or blueprints, more
        # guides first; then (b) on the chain to Main, the file closer to Main first. Ties: theorems and lemmas before
        # definitions, then source order (explorer order, then line). Nothing in (a) or (b): no "main:" list.
        THM = ('t', 'l')
        ca = [x for x in allD if x[3] or x[4]]
        cb = [x for x in allD if not (x[3] or x[4]) and x[2][6]]
        ca.sort(key=lambda x: (-x[3], x[2][0] not in THM, x[5], x[2][1]))
        cb.sort(key=lambda x: (fdist.get(x[1]) if fdist.get(x[1]) is not None else 999, x[2][0] not in THM, x[5], x[2][1]))
        LEAN_HOVER[k] = [len(allD)] + [x[0].rsplit('.', 1)[-1] for x in (ca + cb)[:3]]
    for lazy in (False, True):
        r = sorted(x[2] for x in _hsz if x[1] == lazy); z = sorted(x[3] for x in _hsz if x[1] == lazy)
        print(f'Lean viewer data ({"lazy x/" if lazy else "main"}): {len(z)} files, {sum(z) / 1e6:.1f} MB gzipped '
              f'({sum(r) / 1e6:.1f} MB raw), median {z[len(z) // 2] / 1e3:.0f} kB, max {z[-1] / 1e3:.0f} kB gzipped '
              f'({r[-1] / 1e3:.0f} kB raw)')
    print(f'Lean viewer data built in {time.monotonic() - _t0:.0f}s')
    json.dump({'k': [LEAN_HOVER.get(k, [0]) for k in overview_clusters]},
              open(os.path.join(OUT, 'data', 'lean-hover.json'), 'w'), separators=(',', ':'), ensure_ascii=False)
    return LEAN_HOVER
