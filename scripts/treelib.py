"""Load the whole tree: tree.yaml (core) + tree/concepts.yaml + tree/nodes/part-*.yaml.

tree.yaml holds roots, the readable top of the proof, layer 2, leaves and the
hand-mapped nodes. Background concepts found while mapping chunks live in
tree/concepts.yaml. File nodes from chunk mapping live in shards
tree/nodes/part-NNN.yaml, each capped at SHARD_MAX nodes; a new shard starts when
the last one is full.
"""
import glob, os, yaml

SHARD_MAX = 500


def paths(repo):
    return ([os.path.join(repo, 'tree.yaml'), os.path.join(repo, 'tree', 'concepts.yaml')]
            + sorted(glob.glob(os.path.join(repo, 'tree', 'nodes', 'part-*.yaml'))))


def load(repo):
    """(roots, list of all nodes) across every file."""
    core = yaml.safe_load(open(os.path.join(repo, 'tree.yaml')))
    nodes = list(core['nodes'])
    for p in paths(repo)[1:]:
        if os.path.exists(p):
            nodes += (yaml.safe_load(open(p)) or {}).get('nodes') or []
    return core['roots'], nodes


def append_nodes(repo, nodes, header=''):
    """Append nodes to the last shard, starting a new one past SHARD_MAX."""
    d = os.path.join(repo, 'tree', 'nodes'); os.makedirs(d, exist_ok=True)
    shards = sorted(glob.glob(os.path.join(d, 'part-*.yaml')))
    while nodes:
        if shards:
            cur = shards[-1]
            have = len((yaml.safe_load(open(cur)) or {}).get('nodes') or [])
        if not shards or have >= SHARD_MAX:
            cur = os.path.join(d, f'part-{len(shards) + 1:03d}.yaml'); have = 0
            open(cur, 'w').write('# File nodes from chunk mapping. Schema: see tree.yaml header.\n'
                                 '# Read from the Lean text only; nothing compiled.\nnodes:\n')
            shards.append(cur)
        take, nodes = nodes[:SHARD_MAX - have], nodes[SHARD_MAX - have:]
        text = yaml.safe_dump(take, allow_unicode=True, sort_keys=False, width=100)
        with open(cur, 'a') as fh:
            if header:
                fh.write('\n' + '\n'.join('# ' + l for l in header.split('\n')) + '\n')
            fh.write(text)


def append_concepts(repo, nodes):
    p = os.path.join(repo, 'tree', 'concepts.yaml')
    if not os.path.exists(p):
        open(p, 'w').write('# Background concepts found while mapping chunks. Schema: see tree.yaml header.\nnodes:\n')
    if nodes:
        open(p, 'a').write(yaml.safe_dump(nodes, allow_unicode=True, sort_keys=False, width=100))
