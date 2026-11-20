"""Mechanical one-line index of every .lean file: declarations + main statement head. Reads files as text only."""
import os, re, sys, csv

root, out = sys.argv[1], sys.argv[2]
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|scoped)\s+)*'
                  r'(theorem|lemma|def|abbrev|structure|class|instance|inductive)\s+([^\s:({\[]+)?(.*)$')

rows = []
for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith('.lean'):
            continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, root)
        try:
            lines = open(p, encoding='utf-8', errors='replace').read().splitlines()
        except OSError:
            continue
        decls = []
        for i, ln in enumerate(lines):
            m = DECL.match(ln)
            if m:
                kind, name, rest = m.group(1), m.group(2) or '(anon)', m.group(3)
                sig = rest
                j = i + 1
                while ':=' not in sig and j < len(lines) and j < i + 6:
                    sig += ' ' + lines[j].strip(); j += 1
                sig = re.sub(r'\s+', ' ', sig.split(':=')[0]).strip()
                decls.append((kind, name, sig, i + 1))
        if decls:
            # "main" = last theorem/lemma (files usually end with the result), else last decl
            thms = [d for d in decls if d[0] in ('theorem', 'lemma')]
            k, n, s, l = (thms or decls)[-1]
            desc = f"{k} {n} {s}"[:240]
        else:
            k = n = desc = ''; l = 0
        kinds = {}
        for d in decls:
            kinds[d[0]] = kinds.get(d[0], 0) + 1
        rows.append((rel, len(lines), len(decls), ' '.join(f"{v}{c[0:3]}" for c, v in sorted(kinds.items())),
                     f"{rel}:{l}" if l else '', desc))

rows.sort()
with open(out, 'w', newline='') as fh:
    w = csv.writer(fh, delimiter='\t')
    w.writerow(['file', 'lines', 'n_decls', 'kinds', 'main_at', 'main_statement_head'])
    w.writerows(rows)
print(len(rows), 'files indexed;', sum(1 for r in rows if not r[5]), 'with no declarations')
