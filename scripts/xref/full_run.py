"""P4. The full cross-reference run: resolve.py's rules over every file of the archive, saved per cluster.

usage: uv run --no-project python -I full_run.py <lean/src> <xref data dir> <site modules.json> [workers=8]

Needs decls.tsv.gz and files.jsonl.gz from index_decls.py. Same lookup as resolve.py (79b): candidates are the
declarations of the file and its transitive imports; one candidate = "resolved from source", several = ambiguous,
none = unresolved. Only unique matches are used downstream. Writes into <xref dir>/full/:
  <cluster>.tsv.gz    one row per resolved or ambiguous occurrence in the cluster's files:
                      module, line, token, category, target, target_module, user (the declaration it sits in)
  spans.tsv.gz        every declaration: name, module, kind, start, end (last non-blank line), stmt_end (the line
                      holding the first top-level `:=`, `where` or `|`; = end if none), flags
  used_by.tsv.gz      per declaration with at least one unique use: name, module, decls (distinct declarations that
                      use it, itself excluded), occurrences, files
  summary.json        totals by category (as in report.md), per cluster, runtime
Files in no cluster (160) are run too and saved under the cluster id '-' (unmapped.tsv.gz).
"""
import os, sys, gzip, json, time, bisect, collections
from multiprocessing import get_context

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leansrc
import resolve

IX = SRC = None
OPEN_BR, CLOSE_BR = set('([{⦃⟨'), set(')]}⦄⟩')


def stmt_end(c):
    """Line offset (0-based, within the command) of the first top-level `:=`, `where` or `|`."""
    t = c.text
    depth = 0
    line = 0
    i, n = 0, len(t)
    while i < n:
        ch = t[i]
        if ch == '\n':
            line += 1
        elif ch in OPEN_BR:
            depth += 1
        elif ch in CLOSE_BR:
            depth = max(0, depth - 1)
        elif depth == 0:
            if ch == ':' and t.startswith(':=', i):
                return line
            if ch == '|' and (i == 0 or t[i - 1] in ' \n') and c.kind in ('inductive',):
                return line
            if ch == 'w' and t.startswith('where', i) and (i == 0 or not leansrc.IDCHAR.match(t[i - 1])) \
                    and (i + 5 >= n or not leansrc.IDCHAR.match(t[i + 5])):
                return line
        i += 1
    return None


def one(mod):
    rows = []
    cnt, nclo = resolve.process(SRC, IX, mod, rows)
    text = open(os.path.join(SRC, *mod.split('.')) + '.lean', encoding='utf-8', errors='replace').read()
    p = leansrc.parse(text)
    spans = []
    for c in p['cmds']:
        if not c.full:
            continue
        lines = c.text.split('\n')
        k = len(lines)
        while k > 1 and not lines[k - 1].strip():
            k -= 1
        end = c.line + k - 1
        se = stmt_end(c)
        fl = ('p' if 'private' in c.mods else '') + ('P' if 'protected' in c.mods else '')
        spans.append((c.full, c.kind, c.line, end, c.line + se if se is not None else end, fl))
    starts = sorted((s[2], s[0]) for s in spans)
    keys = [s[0] for s in starts]
    out = []
    for (m, line, tok, cat, tgt, tm, nc) in rows:
        if not (cat.startswith('resolved') or cat == 'ambiguous'):
            continue
        j = bisect.bisect_right(keys, line) - 1
        user = starts[j][1] if j >= 0 else ''
        out.append((line, tok, cat, tgt, tm, user))
    return mod, dict(cnt), out, spans


def main():
    global IX, SRC
    SRC, d, mj = sys.argv[1], sys.argv[2], sys.argv[3]
    workers = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    out_dir = os.path.join(d, 'full')
    os.makedirs(out_dir, exist_ok=True)
    t0 = time.time()
    IX = resolve.Index(d)
    print(f'index loaded in {time.time() - t0:.0f}s', flush=True)
    m = json.load(open(mj))
    mod_cl = {(f"{m['folders'][a]}.{b}" if m['folders'][a] else b): 'k%04d' % k for a, b, k in m['rows']}
    mods = sorted(IX.mods[i] for i in IX.imports)
    if os.environ.get('P4_LIMIT'):   # test runs only
        mods = mods[:int(os.environ['P4_LIMIT'])]
    by_cl = collections.defaultdict(list)
    total, per_cl = collections.Counter(), collections.defaultdict(collections.Counter)
    use_decls = collections.defaultdict(set)
    use_occ, use_files = collections.Counter(), collections.defaultdict(set)
    t1 = time.time()
    with gzip.open(os.path.join(out_dir, 'spans.tsv.gz'), 'wt', encoding='utf-8') as fs, \
            get_context('fork').Pool(workers) as pool:
        fs.write('name\tmodule\tkind\tstart\tend\tstmt_end\tflags\n')
        for i, (mod, cnt, rows, spans) in enumerate(pool.imap_unordered(one, mods, chunksize=100)):
            k = mod_cl.get(mod, '-')
            total.update(cnt)
            per_cl[k].update(cnt)
            by_cl[k].append((mod, rows))
            for s in spans:
                fs.write(f'{s[0]}\t{mod}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\n')
            for line, tok, cat, tgt, tm, user in rows:
                if cat.startswith('resolved'):
                    key = (tgt, tm)
                    use_occ[key] += 1
                    use_files[key].add(mod)
                    if user and not (user == tgt and tm == mod):
                        use_decls[key].add((mod, user))
            if (i + 1) % 20000 == 0:
                print(f'  {i + 1:,} files, {time.time() - t1:.0f}s', flush=True)
    t_res = time.time() - t1
    nrows = 0
    for k, lst in by_cl.items():
        name = 'unmapped' if k == '-' else k
        with gzip.open(os.path.join(out_dir, name + '.tsv.gz'), 'wt', encoding='utf-8') as fh:
            fh.write('module\tline\ttoken\tcategory\ttarget\ttarget_module\tuser\n')
            for mod, rows in sorted(lst):
                for r in rows:
                    fh.write(mod + '\t' + '\t'.join(map(str, r)) + '\n')
                    nrows += 1
    with gzip.open(os.path.join(out_dir, 'used_by.tsv.gz'), 'wt', encoding='utf-8') as fh:
        fh.write('name\tmodule\tdecls\toccurrences\tfiles\n')
        for key in sorted(use_occ):
            fh.write(f'{key[0]}\t{key[1]}\t{len(use_decls[key])}\t{use_occ[key]}\t{len(use_files[key])}\n')
    json.dump({'n_files': len(mods), 'seconds_resolve': round(t_res, 1), 'workers': workers, 'rows_saved': nrows,
               'targets_used': len(use_occ), 'totals': dict(total), 'per_cluster': {k: dict(v) for k, v in per_cl.items()}},
              open(os.path.join(out_dir, 'summary.json'), 'w'), indent=0)
    print(f'{len(mods):,} files in {t_res:.0f}s; {nrows:,} rows saved; {len(use_occ):,} declarations used')
    for k, v in sorted(total.items()):
        print(f'  {k:40s} {v:>11,}')


if __name__ == '__main__':
    main()
