"""One round of the mapping loop, split into the two deterministic halves.

usage (run from anywhere):
  uv run -q --with pyyaml python -I scripts/batch.py prepare <work dir> [agents] [lines per agent, default 5000]
  uv run -q --with pyyaml python -I scripts/batch.py merge   <batch dir>

prepare: first merges any earlier batch in <work dir> that has no MERGED marker,
         then picks the next unfinished chunks, assigns each todo file to exactly
         one chunk with a fixed node id, and writes <work dir>/bNNNN/ with
         assign.json, one bundle-KK.md per agent (task, ids, restatement-name map,
         concept list, source with real line numbers) and an empty fragments/ dir.
         Prints JSON: {"batch", "dir", "agents": [{"bundle", "chunks"}], "files"} or
         {"done": true} when nothing is left.
merge:   reads <batch dir>/fragments/*.yaml, keeps nodes for assigned files (fixing
         ids by lean path), new concepts go to tree/concepts.yaml, drops links to
         unknown ids, marks unlinked nodes orphan, appends to tree/nodes shards,
         re-syncs progress, writes MERGED and appends a line to <work dir>/log.jsonl.
         Safe to run twice (MERGED marker) and after a half-finished round: files
         with no valid node stay todo and are picked again next round.

Bundles contain the project's Lean source, so <work dir> must be outside the repo.
"""
import collections, glob, json, os, re, subprocess, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..'))
SRC = os.path.abspath(os.path.join(REPO, '..', 'src', 'lean', 'src'))
sys.path.insert(0, HERE)
import treelib

DECL = re.compile(r'^(?:set_option \S+ \S+ in )?(?:@\[[^\]]*\] )?(?:protected |private )?(?:theorem|lemma) (\S+)', re.M)
kebab = lambda s: re.sub(r'(?<!^)(?=[A-Z])', '-', s).lower().replace('_', '-')


def sync():
    subprocess.run([sys.executable, '-I', os.path.join(HERE, 'progress.py'), 'sync'], check=True,
                   stdout=subprocess.DEVNULL)


def chunks():
    return [json.loads(l) for l in open(os.path.join(REPO, 'tree', 'chunks.jsonl'))]


def done_map():
    return {json.loads(l)['path']: json.loads(l)['nodes'][0] for l in open(os.path.join(REPO, 'tree', 'done.jsonl'))}


# ---------------------------------------------------------------- merge
def merge(bdir):
    if os.path.exists(os.path.join(bdir, 'MERGED')):
        return json.load(open(os.path.join(bdir, 'MERGED')))
    a = json.load(open(os.path.join(bdir, 'assign.json')))
    given = a['given']                      # path -> id
    gid = set(given.values())
    roots, tree = treelib.load(REPO)
    have = {n['id'] for n in tree}
    new_files, new_concepts, log = [], {}, collections.Counter()
    for f in sorted(glob.glob(os.path.join(bdir, 'fragments', '*.yaml'))):
        ch = os.path.basename(f)[:-5]
        try:
            ns = (yaml.safe_load(open(f)) or {}).get('nodes') or []
        except Exception:
            log['bad_fragment'] += 1; continue
        for n in ns:
            if not isinstance(n, dict) or 'id' not in n:
                log['bad_node'] += 1; continue
            n['chunk'] = ch
            if str(n['id']).startswith('concept-'):
                if n['id'] in have or n['id'] in new_concepts:
                    log['concept_dup'] += 1
                else:
                    n.update(kind='concept', status=n.get('status', 'textbook')); n.pop('orphan', None)
                    new_concepts[n['id']] = n
                continue
            p = str((n.get('lean') or [''])[0]).split(':')[0]
            if p in given and n['id'] != given[p]:
                n['id'] = given[p]; log['id_fixed'] += 1
            if n['id'] not in gid or n['id'] in have or any(m['id'] == n['id'] for m in new_files):
                log['dropped'] += 1; continue
            n.setdefault('kind', 'step'); n.setdefault('status', 'explained')
            refs = []
            for ref in n.get('lean') or []:          # keep only real files; clamp bad line numbers
                f_, _, ln = str(ref).partition(':')
                fp = os.path.join(SRC, f_)
                if not os.path.isfile(fp):
                    log['lean_ref_dropped'] += 1; continue
                if ln and (not ln.isdigit() or int(ln) > sum(1 for _ in open(fp, encoding='utf-8', errors='replace'))):
                    ref = f_; log['line_fixed'] += 1
                refs.append(ref)
            if not refs:
                refs = [p] if p in given else []
            if not refs:
                log['dropped'] += 1; continue
            n['lean'] = refs
            new_files.append(n)
    known = have | {n['id'] for n in new_files} | set(new_concepts)
    for n in new_files + list(new_concepts.values()):
        nd = [x for x in n.get('needs') or [] if x in known and x != n['id']]
        log['link_dropped'] += len(n.get('needs') or []) - len(nd)
        if nd: n['needs'] = nd
        else: n.pop('needs', None)
    # drop file->file links the Lean imports don't support (wrong-way links make cycles)
    imp_tsv = os.path.join(REPO, '..', 'notes', 'tree', 'import_closure.tsv')
    if os.path.exists(imp_tsv):
        sys.argv = [sys.argv[0], imp_tsv]
        import fix_links
        reach = fix_links.importer(fix_links.imp)
        mine = {id(n) for n in new_files}
        for n, keep, drop in fix_links.check(tree + new_files + list(new_concepts.values()), reach):
            if drop and id(n) in mine:
                log['link_unsupported'] += len(drop)
                if keep: n['needs'] = keep
                else: n.pop('needs', None)
    # anything not reachable from a root or an orphan becomes an orphan
    allnodes = {n['id']: n for n in tree + new_files + list(new_concepts.values())}
    seen, stack = set(), list(roots) + [i for i, n in allnodes.items() if n.get('orphan')]
    while stack:
        i = stack.pop()
        if i in seen or i not in allnodes: continue
        seen.add(i); stack += allnodes[i].get('needs') or []
    for n in new_files:
        if n['id'] not in seen:
            n['orphan'] = True; log['orphaned'] += 1
            seen.add(n['id']); stack = list(n.get('needs') or [])
            while stack:
                i = stack.pop()
                if i in seen or i not in allnodes: continue
                seen.add(i); stack += allnodes[i].get('needs') or []
    for c in new_concepts.values():          # concepts nobody reached: hang them on themselves
        if c['id'] not in seen: c['orphan'] = True
    treelib.append_concepts(REPO, list(new_concepts.values()))
    treelib.append_nodes(REPO, new_files, header=f"batch {a['batch']}: chunks {a['chunks'][0]}..{a['chunks'][-1]}")
    sync()
    words = sorted(len(str(n.get('plain', '')).split()) for n in new_files) or [0]
    res = {'batch': a['batch'], 'files_assigned': len(given), 'nodes_merged': len(new_files),
           'concepts_new': len(new_concepts), 'missing': len(gid - {n['id'] for n in new_files}),
           'words_median': words[len(words) // 2], **log}
    json.dump(res, open(os.path.join(bdir, 'MERGED'), 'w'))
    with open(os.path.join(os.path.dirname(bdir), 'log.jsonl'), 'a') as fh:
        fh.write(json.dumps(res) + '\n')
    return res


# ---------------------------------------------------------------- prepare
def src_lines(p):
    """lines that go into a bundle: non-blank, non-import."""
    return sum(1 for l in open(os.path.join(SRC, p), encoding='utf-8', errors='replace')
               if l.strip() and not l.startswith('import '))


def prepare(work, agents=6, lines=5000):
    """Pack whole chunks into `agents` bundles of about `lines` source lines each.
    A chunk is never split; a chunk bigger than `lines` gets a bundle to itself."""
    os.makedirs(work, exist_ok=True)
    for b in sorted(glob.glob(os.path.join(work, 'b[0-9]*'))):
        if os.path.exists(os.path.join(b, 'assign.json')) and not os.path.exists(os.path.join(b, 'MERGED')):
            merge(b)
    sync()
    allc = chunks()
    done = done_map()
    owner, groups, cur, size = {}, [], [], 0
    for r in (c for c in allc if c['status'] != 'done'):
        new = [f['path'] for f in r['files']
               if not f.get('skip') and f['path'] not in done and f['path'] not in owner]
        if not new:
            continue
        add = sum(src_lines(p) for p in new)
        if cur and size + add > lines:
            groups.append(cur); cur, size = [], 0
            if len(groups) == agents:
                break
        for p in new:
            owner[p] = r['id']
        cur.append(r); size += add
    if cur and len(groups) < agents:
        groups.append(cur)
    rows = [r for g in groups for r in g]
    if not rows:
        return {'done': True}
    _, tree = treelib.load(REPO)
    byid = {n['id']: n for n in tree}
    concepts = '\n'.join(f"{n['id']} | {n['title']}" for n in tree if n.get('kind') in ('concept', 'leaf'))
    stems = collections.Counter(f['path'].rsplit('/', 1)[-1] for c in allc for f in c['files'])
    ids = {}
    for p in owner:
        st = p.rsplit('/', 1)[-1]
        i = 'f-' + (kebab(p.split('/')[-2]) + '--' if stems[st] > 1 else '') + kebab(st[:-5])
        j, k = i, 2
        while j in byid or j in ids.values():
            j, k = f'{i}-{k}', k + 1
        ids[p] = j
    idof = lambda p: ids.get(p) or done.get(p)
    n = len(glob.glob(os.path.join(work, 'b[0-9]*'))) + 1
    bdir = os.path.join(work, f'b{n:04d}'); os.makedirs(os.path.join(bdir, 'fragments'))
    out_agents = []
    for k, g in enumerate(groups, 1):
        out = [f"# Bundle {k} of batch {n}: chunks {', '.join(r['id'] for r in g)}\n",
               "## Chunks and files you own (write one node each, with this id)\n"]
        refs, names, own = {}, set(), []
        for r in g:
            mine = []
            for f in r['files']:
                p = f['path']
                if f.get('skip') and f.get('partner'):
                    m = DECL.search(open(os.path.join(SRC, p), encoding='utf-8', errors='replace').read())
                    if m and idof(f['partner']):
                        names.add(f"{m.group(1).replace('_root_.', '')} -> {idof(f['partner'])}")
                elif owner.get(p) == r['id']:
                    mine.append(p); own.append(p)
                elif p in owner or p in done:
                    refs[p] = (idof(p), byid[done[p]]['title'] if p in done and done[p] in byid
                               else f"(written by another agent, chunk {owner.get(p)})")
            top = r['top']
            tp = next((f.get('partner') for f in r['files'] if f['path'] == top and f.get('skip')), None) or top
            out.append(f"### {r['id']}  (top file: {top}; orphan node: {idof(tp) or '?'})")
            out += [f"- {ids[p]}  <- {p}" for p in mine] or ['- (nothing new to write; all files already mapped)']
            out.append('')
        out.append("## Files already mapped elsewhere (link by id in needs; do not write)\n")
        out += [f"- {i}  <- {p}  :: {t}" for p, (i, t) in sorted(refs.items())] or ['(none)']
        out.append("\n## Restatement names -> node id (proofs cite these names; they mean the node on the right)\n")
        out += sorted(names) or ['(none)']
        out.append("\n## Existing concept and leaf nodes (id | title). Reuse these.\n" + concepts)
        out.append("\n## Source of the files you own (imports and blank lines removed; numbers are real line numbers)\n")
        for p in own:
            out.append(f"\n===== {ids[p]}  ({p}) =====")
            for i, l in enumerate(open(os.path.join(SRC, p), encoding='utf-8', errors='replace').read().split('\n'), 1):
                if l.strip() and not l.startswith('import '):
                    out.append(f"{i:4}| {l}")
        bp = os.path.join(bdir, f'bundle-{k:02d}.md')
        open(bp, 'w').write('\n'.join(out) + '\n')
        out_agents.append({'bundle': bp, 'chunks': [r['id'] for r in g]})
    a = {'batch': n, 'chunks': [r['id'] for r in rows], 'given': ids}
    json.dump(a, open(os.path.join(bdir, 'assign.json'), 'w'), ensure_ascii=False)
    return {'batch': n, 'dir': bdir, 'agents': out_agents, 'files': len(ids)}


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'prepare':
        print(json.dumps(prepare(os.path.abspath(sys.argv[2]), *map(int, sys.argv[3:5]))))
    elif cmd == 'merge':
        print(json.dumps(merge(os.path.abspath(sys.argv[2]))))
