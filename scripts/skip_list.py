"""List project files to skip when building the tree, so nobody reads them twice.

usage: python -I skip_list.py <lean/src> <out skip.tsv>

Reads files as text only. Reasons:
  empty             : only `import Mathlib` (or other libraries); a stand-in for it
  import-hub        : only imports, at least one a project file; bundles other files
  config-only       : imports plus build settings (`run_cmd`, `set_option`, `open`,
                      `namespace`/`section`/`end`), no definitions or theorems,
                      e.g. BuildAid/D1-D5
  statement-wrapper : XStatement.lean whose only theorem restates one from its partner
                      X.lean, with a proof that just cites it (`first | exact @N | ...`).
                      Merge it with the partner. Strict: any other content keeps the
                      file, except `attribute [...]` lines that also appear in X.lean.
                      A 100-file random sample checked this pattern (all 100 restate
                      the partner's theorem); nothing was compiled.
Anything else is kept. Columns: file, reason, lines, partner (for wrappers), note.
note = "chain" when the partner's own proof is just a citation too, so the real
proof is one more step away.
"""
import os, re, sys
from collections import Counter

src, out = sys.argv[1], sys.argv[2]
CONFIG = ('run_cmd ', 'set_option ', 'open ', 'namespace ', 'section', 'end', 'noncomputable section')
DECL = re.compile(r'^(?:set_option \S+ \S+ in )?(?:@\[[^\]]*\] )?(?:protected |private )?(theorem|lemma) (\S+)')
CITE = re.compile(r'(?:exact|apply|refine)\s+@?([^\s()|;<>]+)')
FILLER = re.compile(r'\b(?:by|first|intros?|assumption)\b|<;>|[|();]|\s')
OTHER_DECL = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:noncomputable |private |protected )*'
                        r'(def|abbrev|structure|class|instance|inductive|axiom|opaque|example|theorem|lemma)\b')


def citation_only(proof):
    """The single name a proof cites, if it does nothing else; else None."""
    p = proof.strip()
    if re.fullmatch(r'@?[^\s()|;<>:=]+', p):          # term-mode `:= N`
        return p.lstrip('@')
    names = {n.rsplit('.', 1)[-1] for n in CITE.findall(p)}
    if len(names) != 1 or FILLER.sub('', CITE.sub('', p)):
        return None
    return CITE.findall(p)[0]


def wrapper(p, body, rest):
    """(partner path, note) if p is a statement-wrapper, else None."""
    if not p.endswith('Statement.lean'):
        return None
    xp = p[:-len('Statement.lean')] + '.lean'
    if not os.path.exists(xp):
        return None
    xtext = open(xp, encoding='utf-8', errors='replace').read()
    xlines = {l.strip() for l in xtext.split('\n')}
    starts = [i for i, l in enumerate(rest) if OTHER_DECL.match(l) or DECL.match(l)]
    if len(starts) != 1 or not DECL.match(rest[starts[0]]):
        return None
    for l in rest[:starts[0]]:
        if not (l.startswith(CONFIG) or (l.startswith('attribute ') and l in xlines)):
            return None
    tail = rest[starts[0]:]
    while tail and tail[-1].startswith(('end', 'namespace ')):
        tail = tail[:-1]
    text = ' '.join(tail)
    if ':=' not in text:
        return None
    name = citation_only(text.rsplit(':=', 1)[1])
    if not name:
        return None
    last = re.escape(name.rsplit('.', 1)[-1])
    m = re.search(r'^(?:@\[[^\]]*\]\s*)?(?:protected |private )?(?:theorem|lemma) (\S*[.]|)' + last
                  + r"(?![\w'!?])(.*?)(?=^\S)", xtext + '\n#', re.M | re.S)
    if not m:
        return None
    xproof = m.group(0).rsplit(':=', 1)[-1] if ':=' in m.group(0) else ''
    note = 'chain' if citation_only(' '.join(xproof.split())) else ''
    return os.path.relpath(xp, src), note


rows = []
for dp, _, fs in os.walk(src):
    for f in fs:
        if not f.endswith('.lean'):
            continue
        p = os.path.join(dp, f)
        lines = [l.strip() for l in open(p, encoding='utf-8', errors='replace')]
        body = [l for l in lines if l]
        rest = [l for l in body if not l.startswith('import ')]
        if len(rest) > 40:          # this much non-import text has real content
            continue
        partner = note = ''
        if not rest:
            mods = [m for l in body for m in l.split()[1:]]
            proj = [m for m in mods if os.path.exists(os.path.join(src, *m.split('.')) + '.lean')]
            reason = 'import-hub' if proj else 'empty'
        elif all(l.startswith(CONFIG) for l in rest):
            reason = 'config-only'
        else:
            w = wrapper(p, body, rest)
            if not w:
                continue
            reason, (partner, note) = 'statement-wrapper', w
        rows.append((os.path.relpath(p, src), reason, len(lines), partner, note))

rows.sort()
with open(out, 'w') as fh:
    fh.write('file\treason\tlines\tpartner\tnote\n')
    fh.writelines('\t'.join(map(str, r)) + '\n' for r in rows)
print(len(rows), 'files to skip:', dict(Counter(r[1] for r in rows)),
      '; wrapper chains:', sum(1 for r in rows if r[4] == 'chain'))
