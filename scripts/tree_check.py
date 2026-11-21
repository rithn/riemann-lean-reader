"""Check tree.yaml and draw it as a Mermaid diagram.

usage: uv run --with pyyaml python -I scripts/tree_check.py tree.yaml [lean/src] > TREE_GRAPH.md

Loads tree.yaml plus tree/concepts.yaml and tree/nodes/part-*.yaml next to it (treelib).

Checks: unique ids, every `needs` id exists, no cycles, leaves have no `needs`,
every node is reachable from a root or an `orphan: true` node. If lean/src is given, also checks that every
`lean:` file exists and its line number is in range.
"""
import os, sys, yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import treelib

roots, all_nodes = treelib.load(os.path.dirname(os.path.abspath(sys.argv[1])))
doc = {'roots': roots, 'nodes': all_nodes}
src = sys.argv[2] if len(sys.argv) > 2 else None
nodes = {n['id']: n for n in doc['nodes']}
errs = []
if len(nodes) != len(doc['nodes']):
    errs.append('duplicate ids')
for n in nodes.values():
    for c in n.get('needs', []):
        if c not in nodes:
            errs.append(f"{n['id']}: unknown need {c}")
    if n['kind'] == 'leaf' and n.get('needs'):
        errs.append(f"{n['id']}: leaf with needs")
    for ref in n.get('lean', []) if src else []:
        f, _, ln = ref.partition(':')
        p = os.path.join(src, f)
        if not os.path.exists(p):
            errs.append(f"{n['id']}: missing file {f}")
        elif ln and int(ln) > sum(1 for _ in open(p, encoding='utf-8', errors='replace')):
            errs.append(f"{n['id']}: line out of range {ref}")

state, seen = {}, set()


def dfs(i, path):
    if state.get(i) == 1:
        errs.append('cycle: ' + ' -> '.join(path + [i])); return
    if state.get(i) == 2:
        return
    state[i] = 1; seen.add(i)
    for c in nodes[i].get('needs', []):
        if c in nodes:
            dfs(c, path + [i])
    state[i] = 2


for r in doc['roots'] + [i for i, n in nodes.items() if n.get('orphan')]:
    dfs(r, [])
errs += [f"{i}: not reachable from a root" for i in nodes if i not in seen]
if errs:
    sys.exit('\n'.join(errs))

STYLE = {'explained': 'fill:#c8f7c5', 'textbook': 'fill:#cfe2ff', 'research': 'fill:#ffe5b4',
         'new': 'fill:#f8c8dc', 'unmapped': 'fill:#eeeeee,stroke-dasharray:4'}
out = ['# Prerequisite tree (diagram)', '',
       'Generated from [tree.yaml](tree.yaml) by `scripts/tree_check.py`. Do not edit by hand.', '',
       'Arrows point from a result to what it needs. Green: explained · blue: textbook · '
       'orange: research · pink: new in this proof · grey dashed: not mapped yet.', '',
       '```mermaid', 'graph TD']
for n in nodes.values():
    label = n['title'].replace('"', "'") + (' ?' if n.get('guess') else '')
    shape = f'(["{label}"])' if n['kind'] == 'leaf' else f'[["{label}"]]' if n['kind'] == 'theorem' else f'["{label}"]'
    out.append(f"  {n['id'].replace('-', '_')}{shape}")
for n in nodes.values():
    for c in n.get('needs', []):
        out.append(f"  {n['id'].replace('-', '_')} --> {c.replace('-', '_')}")
for s, css in STYLE.items():
    ids = [n['id'].replace('-', '_') for n in nodes.values() if n['status'] == s]
    if ids:
        out += [f"  classDef {s} {css}", f"  class {','.join(ids)} {s}"]
out.append('```')
print('\n'.join(out))
counts = {}
for n in nodes.values():
    counts[n['status']] = counts.get(n['status'], 0) + 1
print(f"ok: {len(nodes)} nodes, {counts}", file=sys.stderr)
