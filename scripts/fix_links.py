"""Drop `needs` links between file nodes that the Lean imports don't support.

usage: uv run -q --with pyyaml python -I scripts/fix_links.py <import_closure.tsv> [--apply]

A link "A needs B" between two file nodes is kept only if B's file is A's own file
or is imported by A's file, directly or through other project files. Links to
concept/leaf nodes are never touched. Wrong-way links (B imports A) are what create
cycles; links to files A never imports are guesses. Without --apply, only reports.
With --apply, rewrites tree/nodes/part-*.yaml (keeping each file's header lines).
merge in batch.py applies the same rule to new rounds.
"""
import glob, os, sys, yaml
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
import treelib

imp = {}
for ln in list(open(sys.argv[1]))[1:]:
    m, _, i = ln.rstrip('\n').split('\t')
    imp[m] = i.split()


def mod(path):
    return path[:-5].replace('/', '.') if path.endswith('.lean') else None


def importer(imp):
    cache = {}
    def reach(a):
        if a not in cache:
            seen, q = set(), [a]
            while q:
                x = q.pop()
                for k in imp.get(x, ()):
                    if k not in seen:
                        seen.add(k); q.append(k)
            cache[a] = seen
        return cache[a]
    return reach


def node_mods(n):
    return {mod(str(r).split(':')[0]) for r in n.get('lean') or []} - {None}


def check(nodes, reach):
    """yield (node, kept needs, dropped needs)."""
    byid = {n['id']: n for n in nodes}
    for n in nodes:
        if n.get('kind') in ('concept', 'leaf') or not n.get('needs'):
            continue
        src = node_mods(n)
        if not src:
            continue
        keep, drop = [], []
        for x in n['needs']:
            t = byid.get(x)
            tm = node_mods(t) if t and t.get('kind') not in ('concept', 'leaf') else set()
            if not tm or tm & src or any(tm & reach(s) for s in src):
                keep.append(x)
            else:
                drop.append(x)
        yield n, keep, drop


if __name__ == '__main__':
    reach = importer(imp)
    _, nodes = treelib.load(REPO)
    res = [(n, k, d) for n, k, d in check(nodes, reach) if d]
    wrongway = sum(1 for n, _, d in res for x in d
                   for t in [next(m for m in nodes if m['id'] == x)]
                   if any(node_mods(n) & reach(s) for s in node_mods(t)))
    print(f"{sum(len(d) for _, _, d in res)} links to drop on {len(res)} nodes "
          f"({wrongway} point the wrong way, the rest are to files never imported)")
    for n, _, d in res[:8]:
        print(' ', n['id'], '-x->', d)
    if '--apply' in sys.argv:
        fix = {n['id']: k for n, k, _ in res}
        for p in sorted(glob.glob(os.path.join(REPO, 'tree', 'nodes', 'part-*.yaml'))):
            text = open(p).read()
            head = ''.join(l + '\n' for l in text.split('\n')[:2] if l.startswith('#'))
            doc = yaml.safe_load(text) or {}
            ns = doc.get('nodes') or []
            changed = False
            for n in ns:
                if n['id'] in fix:
                    changed = True
                    if fix[n['id']]: n['needs'] = fix[n['id']]
                    else: n.pop('needs', None)
            if changed:
                open(p, 'w').write(head + yaml.safe_dump({'nodes': ns}, allow_unicode=True, sort_keys=False, width=100))
        print('applied')
