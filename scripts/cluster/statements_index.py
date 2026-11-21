"""Index every named claim (any `def ... : Prop`) in the project.

usage: uv run -q python -I scripts/cluster/statements_index.py <out.json>

Reads the Lean files as text only. Tracks `namespace X` / `end X` to build full names.
Writes {full name: claim text (whitespace squeezed, capped at 1500 chars)}.
"""
import os, re, sys, json
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'src', 'lean', 'src'))
HEAD = re.compile(r"^(?:(?:private|protected|noncomputable|@\[[^\]]*\])\s+)*(?:def|abbrev)\s+([^\s:({\[]+)")
TOP = re.compile(r"^(?:theorem|lemma|def|abbrev|instance|structure|class|inductive|namespace|end|section|open|variable|@\[|private|protected|noncomputable|set_option|#|example|/--|--)")


def scan(path):
    out, ns = {}, []
    try:
        lines = open(os.path.join(SRC, path), encoding='utf-8', errors='replace').read().split('\n')
    except OSError:
        return out
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('namespace '):
            ns.append(l.split()[1]); i += 1; continue
        if l.startswith('end ') and ns and l.split()[1] == ns[-1]:
            ns.pop(); i += 1; continue
        m = HEAD.match(l)
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip() and not TOP.match(lines[j]):
                j += 1
            text = ' '.join(' '.join(lines[i:j]).split())
            if ': Prop' in text or ':Prop' in text:
                name = m.group(1).lstrip('_root_.') if m.group(1).startswith('_root_.') else '.'.join(ns + [m.group(1)])
                out[name] = text[:1500] + (' …' if len(text) > 1500 else '')
            i = j; continue
        i += 1
    return out


if __name__ == '__main__':
    paths = []
    for root, _, fs in os.walk(SRC):
        paths += [os.path.relpath(os.path.join(root, f), SRC) for f in fs if f.endswith('.lean')]
    res = {}
    with Pool(10) as p:
        for d in p.imap_unordered(scan, paths, chunksize=500):
            res.update(d)
    json.dump(res, open(sys.argv[1], 'w'))
    print(len(paths), 'files,', len(res), 'named claims')
