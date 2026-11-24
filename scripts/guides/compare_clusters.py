"""Compare guide-refs clusters with the 23 Nov `clusters` lists in guides.yaml (read only).

usage: uv run --no-project --with pyyaml python -I compare_clusters.py <guides.yaml> <summary.json>
Prints one JSON object per guide: clusters now, 23 Nov, new, missing.
"""
import sys, json, yaml

g = {x['id']: x for x in yaml.safe_load(open(sys.argv[1]))['guides']}
s = json.load(open(sys.argv[2]))
out = {}
for gid, v in s.items():
    now = set(v['clusters'])
    base = gid.split('@')[0]
    old = set(g.get(base, {}).get('clusters') or [])
    out[gid] = {'now': len(now), 'nov23': len(old), 'new': sorted(now - old), 'missing': sorted(old - now)}
print(json.dumps(out, indent=1))
