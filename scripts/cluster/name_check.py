"""Check naming answers against their bundles.

usage: uv run -q --with pyyaml python -I scripts/cluster/name_check.py <cluster dir> [bundle-NNNN ...]
With no bundle names, checks every answer. Prints one line per bundle; an answer that
fails to parse or misses clusters is renamed *.bad so the loop asks again.
"""
import os, re, sys, json, statistics, yaml

D = sys.argv[1]; N = os.path.join(D, os.environ.get('NAMING', 'naming')); OUT = os.path.join(N, 'out')
names = sys.argv[2:] or sorted(f[:-5] for f in os.listdir(OUT) if f.endswith('.yaml'))
concepts = set(re.findall(r'^- ([\w-]+):', open(os.path.join(N, 'concepts.md')).read(), re.M))
for k in names:
    want = re.findall(r'^## (k\d{4})', open(os.path.join(N, k + '.md')).read(), re.M)
    p = os.path.join(OUT, k + '.yaml')
    try:
        got = yaml.safe_load(open(p))['clusters']
        ids = [c['id'] for c in got]
    except Exception as e:
        print(f'{k}: BAD ({type(e).__name__})')
        if os.path.exists(p): os.replace(p, p + '.bad')
        continue
    miss = set(want) - set(ids)
    w = [len(str(c.get('plain', '')).split()) for c in got]
    unk = sorted({x for c in got for x in c.get('concepts') or [] if x not in concepts})
    stat = lambda f: sum(1 for c in got if str(c.get(f)).lower() == 'low' or str(c.get(f)).lower() == 'mixed')
    print(f'{k}: {len(ids)}/{len(want)} clusters, words median {statistics.median(w) if w else 0}, '
          f'mixed {stat("coherent")}, low-confidence {stat("confidence")}, '
          f'sources {sum(1 for c in got if c.get("source"))}, unknown concept ids {len(unk)}'
          + (f', MISSING {len(miss)}' if miss else ''))
    if len(miss) > len(want) // 5:
        os.replace(p, p + '.bad')
