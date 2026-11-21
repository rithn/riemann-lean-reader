"""Track which files are already mapped, so no file is explained twice.

usage: uv run --with pyyaml python -I scripts/progress.py <command> [chunk id]
  sync        rebuild tree/done.jsonl from tree.yaml, and set each chunk's status
  show c0001  list a chunk's files as done / skip / todo
  next [n]    the next n chunks (smallest first) that still have todo files

Source of truth is the tree (tree.yaml + tree/concepts.yaml + tree/nodes/*.yaml): a file counts as done when some node's `lean:` list
names it. done.jsonl (one line per file: path, nodes) is generated; don't edit it.
A wrapper file counts as done when its partner is. Chunk status: todo (nothing
done), partial, or done (every non-skip file done).
"""
import json, os, sys, yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import treelib

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TREE, CHUNKS, DONE = (os.path.join(HERE, p) for p in ('tree.yaml', 'tree/chunks.jsonl', 'tree/done.jsonl'))


def load_done():
    done = {}
    for n in treelib.load(HERE)[1]:
        for ref in n.get('lean', []):
            done.setdefault(ref.split(':')[0], []).append(n['id'])
    return done


def state(f, done):
    if f['path'] in done:
        return 'done'
    if f.get('skip'):
        return 'skip(done)' if f.get('partner') in done else 'skip'
    return 'todo'


def chunks():
    return [json.loads(l) for l in open(CHUNKS)]


def status(c, done):
    real = [f for f in c['files'] if not f.get('skip')]
    k = sum(1 for f in real if f['path'] in done)
    return 'done' if k == len(real) else 'partial' if k else 'todo'


cmd = sys.argv[1] if len(sys.argv) > 1 else 'next'
done = load_done()
if cmd == 'sync':
    with open(DONE, 'w') as fh:
        for p in sorted(done):
            fh.write(json.dumps({'path': p, 'nodes': done[p]}, ensure_ascii=False) + '\n')
    cs = chunks()
    for c in cs:
        c['status'] = status(c, done)
    with open(CHUNKS, 'w') as fh:
        fh.writelines(json.dumps(c, ensure_ascii=False) + '\n' for c in cs)
    from collections import Counter
    print(f"{len(done)} files done; chunks: {dict(Counter(c['status'] for c in cs))}")
elif cmd == 'show':
    c = next(c for c in chunks() if c['id'] == sys.argv[2])
    print(f"{c['id']}  {c['n_nodes']} nodes, {c['lines']} lines, status {status(c, done)}\n  top: {c['top']}")
    for f in c['files']:
        s = state(f, done)
        extra = f" -> {', '.join(done[f['path']])}" if s == 'done' else f"  (partner {f['partner']})" if f.get('partner') else ''
        print(f"  {s:10} {f['lines']:5}  {f['path']}{extra}")
elif cmd == 'next':
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    for c in [c for c in chunks() if status(c, done) != 'done'][:n]:
        todo = sum(1 for f in c['files'] if state(f, done) == 'todo')
        print(f"{c['id']}  {todo} todo of {c['n_nodes']} nodes, {c['lines']} lines  {c['top'].rsplit('/', 1)[-1]}")
