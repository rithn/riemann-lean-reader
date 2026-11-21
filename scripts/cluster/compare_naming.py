"""Compare two namings of the same clusters (e.g. full data vs a 10% sample).

usage: uv run -q --with pyyaml python -I scripts/cluster/compare_naming.py <out dir A> <out dir B> [n examples]
Prints agreement on concepts (Jaccard), title words, source book, coherent and confidence
flags, and some side-by-side titles.
"""
import glob, os, random, re, sys, statistics, yaml

def load(d):
    r = {}
    for f in glob.glob(os.path.join(d, '*.yaml')):
        for c in yaml.safe_load(open(f))['clusters']:
            r[c['id']] = c
    return r

A, B = load(sys.argv[1]), load(sys.argv[2]); n = int(sys.argv[3]) if len(sys.argv) > 3 else 8
ids = sorted(set(A) & set(B))
W = lambda t: {w for w in re.findall(r'[a-z]{4,}', str(t).lower())}
J = lambda a, b: len(a & b) / len(a | b) if a | b else 1.0
book = lambda c: (str((c.get('source') or {}).get('title', '')).split(',')[0].lower() if isinstance(c.get('source'), dict) else '')
cj = [J(set(A[i].get('concepts') or []), set(B[i].get('concepts') or [])) for i in ids]
tj = [J(W(A[i]['title']), W(B[i]['title'])) for i in ids]
pj = [J(W(A[i]['plain']), W(B[i]['plain'])) for i in ids]
print(f'{len(ids)} clusters in both')
print(f'concepts Jaccard median {statistics.median(cj):.2f}, share with >=1 shared concept '
      f'{sum(1 for i in ids if set(A[i].get("concepts") or []) & set(B[i].get("concepts") or [])) / len(ids):.2f}')
print(f'title word Jaccard median {statistics.median(tj):.2f}; plain-text word Jaccard median {statistics.median(pj):.2f}')
print(f'same source author {sum(1 for i in ids if book(A[i]) and book(A[i]) == book(B[i])) / len(ids):.2f}')
for f in ('coherent', 'confidence'):
    print(f'{f} agrees {sum(1 for i in ids if str(A[i].get(f)) == str(B[i].get(f))) / len(ids):.2f}; '
          f'A low/mixed {sum(1 for i in ids if str(A[i].get(f)) in ("low", "mixed"))}, B {sum(1 for i in ids if str(B[i].get(f)) in ("low", "mixed"))}')
random.seed(0)
for i in random.sample(ids, min(n, len(ids))):
    print(f'\n{i}\n  A: {A[i]["title"]}\n  B: {B[i]["title"]}')
