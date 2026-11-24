"""P4, step 2: per-declaration facts and per-file name links for the Lean viewer, from full_run.py's output.

usage: uv run --no-project python -I derive.py <xref data dir>

Reads <xref>/full/: spans.tsv.gz, <cluster>.tsv.gz (and unmapped.tsv.gz). Only unique matches ("resolved from
source") are used; ambiguous rows are dropped. Writes into <xref>/full/:
  decl_stats.tsv.gz  name, module, kind, start, end, stmt_end, flags, used, chain
                     used  = distinct declarations elsewhere in the proof whose text names it (itself excluded)
                     chain = 1 if it is reached from the declarations of Main by following those uses
                             (source-only: misses dot notation, instances and macros, so it under-counts)
  refs/<cluster>.json.gz  {module: {token: [target, target module]}}; a token that resolves to different targets
                     on different lines in one file maps to {line: [target, target module], ...} instead
  derive.json        counts
"""
import os, sys, gzip, json, glob, collections, time


def main():
    d = os.path.join(sys.argv[1], 'full')
    t0 = time.time()
    spans = {}
    with gzip.open(os.path.join(d, 'spans.tsv.gz'), 'rt', encoding='utf-8') as fh:
        next(fh)
        for ln in fh:
            r = ln.rstrip('\n').split('\t')
            spans[(r[0], r[1])] = r
    users = collections.defaultdict(set)     # target -> {user}
    edges = collections.defaultdict(set)     # user -> {target}
    os.makedirs(os.path.join(d, 'refs'), exist_ok=True)
    n_rows = n_amb = 0
    for f in sorted(glob.glob(os.path.join(d, '*.tsv.gz'))):
        base = os.path.basename(f)[:-7]
        if base in ('spans', 'used_by', 'decl_stats'):
            continue
        refs = collections.defaultdict(dict)
        with gzip.open(f, 'rt', encoding='utf-8') as fh:
            next(fh)
            for ln in fh:
                mod, line, tok, cat, tgt, tm, user = ln.rstrip('\n').split('\t')
                if not cat.startswith('resolved'):
                    n_amb += 1
                    continue
                n_rows += 1
                t = (tgt, tm)
                u = (user, mod)
                if user and u != t:
                    users[t].add(u)
                    edges[u].add(t)
                cur = refs[mod].get(tok)
                if cur is None:
                    refs[mod][tok] = [tgt, tm, {line: 1}]
                elif isinstance(cur, list) and cur[0] == tgt and cur[1] == tm:
                    cur[2][line] = 1
                else:
                    if isinstance(cur, list):      # split into per-line targets
                        cur = {l: [cur[0], cur[1]] for l in cur[2]}
                        refs[mod][tok] = cur
                    cur[line] = [tgt, tm]
        if base == 'unmapped':
            continue
        out = {m: {k: (v[:2] if isinstance(v, list) else v) for k, v in toks.items()} for m, toks in refs.items()}
        with gzip.open(os.path.join(d, 'refs', base + '.json.gz'), 'wt', encoding='utf-8') as fo:
            json.dump(out, fo, separators=(',', ':'), ensure_ascii=False)
    # the chain to Main: everything reached from Main's declarations through uses
    seen = {k for k in spans if k[1] == 'Main'}
    st = list(seen)
    while st:
        x = st.pop()
        for y in edges.get(x, ()):
            if y not in seen:
                seen.add(y); st.append(y)
    with gzip.open(os.path.join(d, 'decl_stats.tsv.gz'), 'wt', encoding='utf-8') as fh:
        fh.write('name\tmodule\tkind\tstart\tend\tstmt_end\tflags\tused\tchain\n')
        for k, r in spans.items():
            fh.write('\t'.join(r) + f'\t{len(users.get(k, ()))}\t{int(k in seen)}\n')
    info = {'unique_rows': n_rows, 'ambiguous_rows_dropped': n_amb, 'declarations': len(spans),
            'declarations_used': sum(1 for k in spans if users.get(k)), 'on_chain_to_main': len(seen),
            'seconds': round(time.time() - t0, 1)}
    json.dump(info, open(os.path.join(d, 'derive.json'), 'w'), indent=1)
    print(info)


if __name__ == '__main__':
    main()
