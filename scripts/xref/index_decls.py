"""79a. Per-file extraction of namespaces, opens, sections, variables and declared names (source only).

usage: uv run --no-project python -I index_decls.py <lean/src> <outdir>
Writes <outdir>/decls.tsv.gz   name, module, line, kind, flags (p = private, P = protected)
       <outdir>/files.jsonl.gz one line per module: imports, namespaces, opens, sections, variables, n_decls
Fields and constructors of structures/classes/inductives are rows with kind field / ctor / ctor-auto
(ctor-auto = the implicit `mk`). Unnamed instances, `where` auxiliaries and macro output are not rows.
"""
import os, sys, gzip, json, time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leansrc


def one(args):
    src, rel = args
    mod = rel[:-5].replace(os.sep, '.')
    text = open(os.path.join(src, rel), encoding='utf-8', errors='replace').read()
    p = leansrc.parse(text)
    rows = []
    for c in p['cmds']:
        if not c.full:
            continue
        fl = ('p' if 'private' in c.mods else '') + ('P' if 'protected' in c.mods else '')
        rows.append((c.full, mod, c.line, c.kind, fl))
        for n, off, k in c.members:
            rows.append((c.full + '.' + n, mod, c.line + off, k, ''))
    meta = {'module': mod, 'imports': p['imports'], 'namespaces': sorted(set(p['namespaces'])),
            'opens': sorted({o for _, o in p['opens']}), 'sections': p['sections'],
            'variables': p['variables'], 'n_decls': sum(1 for r in rows if r[3] not in ('field', 'ctor', 'ctor-auto'))}
    return rows, meta


def main():
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    t0 = time.time()
    rels = sorted(os.path.relpath(os.path.join(dp, f), src) for dp, _, fs in os.walk(src)
                  for f in fs if f.endswith('.lean'))
    nd = 0
    kinds = {}
    with gzip.open(os.path.join(out, 'decls.tsv.gz'), 'wt', encoding='utf-8') as fd, \
            gzip.open(os.path.join(out, 'files.jsonl.gz'), 'wt', encoding='utf-8') as fm, Pool() as pool:
        fd.write('name\tmodule\tline\tkind\tflags\n')
        for rows, meta in pool.imap(one, [(src, r) for r in rels], chunksize=200):
            for r in rows:
                fd.write('\t'.join(map(str, r)) + '\n')
                kinds[r[3]] = kinds.get(r[3], 0) + 1
            nd += len(rows)
            fm.write(json.dumps(meta, ensure_ascii=False) + '\n')
    print(f"{len(rels):,} files, {nd:,} rows in {time.time() - t0:.0f}s")
    print('by kind:', sorted(kinds.items(), key=lambda x: -x[1]))


if __name__ == '__main__':
    main()
