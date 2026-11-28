#!/usr/bin/env python3
"""Rank readable-edition candidates for compact-edition declarations that Naskręcki's concordances cite
but that name matching missed. Writes naskrecki/match_candidates.jsonl and prints the score distribution.

Score = name-token similarity + statement-token similarity + file prior (readable modules where already
matched declarations of the same compact file landed)."""
import collections, csv, glob, json, math, os, re

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.dirname(HERE)
NK = os.path.join(DATA, 'naskrecki')
rows = list(csv.DictReader(open(os.path.join(NK, 'concordance_matches.tsv')), delimiter='\t'))
conc = {}
for f in glob.glob(os.path.join(NK, 'src/writeup/notes/*/concordance.json')):
    for k, v in json.load(open(f))['declarations'].items():
        conc[v['name']] = v
raw = {}
for line in open(os.path.join(DATA, 'raw', 'decls.jsonl'), encoding='utf-8'):
    d = json.loads(line)
    if not d['n'].startswith(('inst@', 'New.inst@')) and '@' not in d['n']:
        raw[d['n']] = d

SPLIT = re.compile(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+|[^\x00-\x7f]')
STOP = {'of', 'the', 'eq', 'iff', 'le', 'lt', 'ne', 'mk', 'apply', 'def', 'new', 'lemma', 'theorem', 'def', 'instance',
        'type', 'fun', 'by', 'and', 'or', 'not', 'in', 'to', 'at', 'is', 'a'}


def name_tokens(n):
    parts = n.split('.')[-2:]  # last two components; earlier namespaces were often renamed
    return {t.lower() for p in parts for t in SPLIT.findall(p)} - STOP


def stmt_tokens(s):
    s = re.sub(r'--.*', ' ', s or '')
    ids = re.findall(r"[A-Za-z_][\w'.₀-₉]*|[^\sA-Za-z0-9_(){}\[\],:]", s)
    out = set()
    for i in ids:
        for p in i.split('.'):
            if len(p) > 1 and p.lower() not in STOP:
                out.add(p)
    return out


def jacc(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


# file prior from matched pairs
prior = collections.defaultdict(collections.Counter)
for r in rows:
    if r['match'] and r['match'] in raw:
        prior[r['file']][raw[r['match']]['m']] += 1
# candidate index by name token
inv = collections.defaultdict(set)
ntok = {n: name_tokens(n) for n in raw}
for n, ts in ntok.items():
    for t in ts:
        inv[t].add(n)
df = {t: len(v) for t, v in inv.items()}
N = len(raw)
stok = {}


def st(n):
    if n not in stok:
        stok[n] = stmt_tokens(raw[n]['pp'][:2500])
    return stok[n]


def idf_sim(a, b):
    if not a or not b:
        return 0.0
    w = lambda t: math.log(N / (1 + df.get(t, 0)))
    inter = sum(w(t) for t in a & b); union = sum(w(t) for t in a | b)
    return inter / union if union else 0.0


todo = {}
for r in rows:
    if not r['match'] and r['name'] not in todo:
        todo[r['name']] = r
out = []
for name, r in todo.items():
    c = conc[name]
    nt = name_tokens(name)
    cs = stmt_tokens(c.get('statement', ''))
    pr = prior.get(r['file'], collections.Counter()); ptot = sum(pr.values()) or 1
    cands = set()
    for t in nt:
        if df.get(t, 0) < 400:
            cands |= inv[t]
    for m in pr:  # all declarations in the prior modules
        cands |= {n for n in raw if raw[n]['m'] == m} if len(pr) <= 6 else set()
    scored = []
    for n in cands:
        if raw[n]['k'] not in ('thm', 'def', 'opaque', 'induct', 'axiom') and not raw[n]['struct']:
            continue
        s_name = idf_sim(nt, ntok[n]); s_stmt = jacc(cs, st(n)); s_file = pr.get(raw[n]['m'], 0) / ptot
        scored.append((0.45 * s_name + 0.4 * s_stmt + 0.15 * s_file, round(s_name, 2), round(s_stmt, 2), round(s_file, 2), n))
    scored.sort(reverse=True)
    top = scored[:5]
    margin = top[0][0] - (top[1][0] if len(top) > 1 else 0) if top else 0
    out.append({'compact': name, 'note': r['note'], 'kind': c['kind'], 'compact_file': c['file'], 'compact_lines': c['lines'],
                'compact_statement': c.get('statement', '')[:1200], 'margin': round(margin, 3),
                'candidates': [{'readable': n, 'score': round(s, 3), 'name': a, 'stmt': b, 'file': f, 'module': raw[n]['m'],
                                'line': raw[n]['r'][4] if len(raw[n]['r']) > 4 else raw[n]['r'][0],
                                'statement': raw[n]['pp'][:700]} for s, a, b, f, n in top]})
with open(os.path.join(NK, 'match_candidates.jsonl'), 'w') as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + '\n')
top = [o['candidates'][0]['score'] if o['candidates'] else 0 for o in out]
auto = [o for o in out if o['candidates'] and o['candidates'][0]['score'] >= 0.55 and o['margin'] >= 0.15]
print(len(out), 'unmatched;', 'no candidates', sum(1 for o in out if not o['candidates']),
      '; auto (score>=.55, margin>=.15):', len(auto), '; ambiguous:', len(out) - len(auto))
