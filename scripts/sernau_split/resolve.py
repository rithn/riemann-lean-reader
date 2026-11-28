#!/usr/bin/env python3
"""Approximate declaration graph of Sernau's readable edition from the source text (no Lean build).

For every declaration it records the project declarations named in its statement (before the
top-level `:=`, `where` or `|`) and in its proof or body. Names are resolved as Lean would, as far
as text allows: current namespaces, the namespaces of the declaration's own name, `open` lines in
scope, `export`, private names of the same file, and dot notation `x.foo` when the type of `x` is a
binder of the declaration or a `variable` in scope. Each edge records the method that resolved it.

Writes data/raw/decls.jsonl in the format analyze.py reads.
Run:  uv run --no-project python data/scripts/resolve.py
"""
import collections, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get('SERNAU_SPLIT_DATA', os.path.dirname(HERE))
SRC = os.environ.get('SERNAU_SPLIT_SOURCE')
OUT = os.path.join(DATA, 'raw', 'decls.jsonl')

MODS = ('private', 'protected', 'noncomputable', 'scoped', 'local', 'partial', 'unsafe', 'nonrec')
DECL_KW = {'theorem': 'thm', 'lemma': 'thm', 'def': 'def', 'abbrev': 'def', 'instance': 'def',
           'structure': 'induct', 'class': 'induct', 'inductive': 'induct', 'opaque': 'opaque',
           'axiom': 'axiom'}


def is_letterlike(ch):
    o = ord(ch)
    return ((0x3b1 <= o <= 0x3c9 and o != 0x3bb) or (0x391 <= o <= 0x3a9 and o not in (0x3a0, 0x3a3))
            or 0x3ca <= o <= 0x3fb or 0x1f00 <= o <= 0x1ffe or 0x2100 <= o <= 0x214f
            or 0x1d49c <= o <= 0x1d59f)


def is_sub(ch):
    o = ord(ch)
    return 0x2080 <= o <= 0x208c or 0x2090 <= o <= 0x209c or 0x1d62 <= o <= 0x1d6a or o in (0x2071, 0x207f)


def id_start(ch):
    return ch.isalpha() and ord(ch) < 0x370 or ch == '_' or is_letterlike(ch) or (ch.isalpha() and ord(ch) > 0x3ff and not is_letterlike(ch) and ch not in 'λΠΣ')


def id_rest(ch):
    return id_start(ch) or ch.isdigit() or ch in "_'!?" or is_sub(ch)


def strip_comments(s):
    """Blank out comments and string literals, keeping offsets."""
    out = list(s)
    i, n = 0, len(s)
    while i < n:
        if s.startswith('--', i):
            j = s.find('\n', i)
            j = n if j < 0 else j
            for k in range(i, j): out[k] = ' '
            i = j
        elif s.startswith('/-', i):
            depth, j = 1, i + 2
            while j < n and depth:
                if s.startswith('/-', j): depth += 1; j += 2
                elif s.startswith('-/', j): depth -= 1; j += 2
                else: j += 1
            for k in range(i, j):
                if out[k] != '\n': out[k] = ' '
            i = j
        elif s[i] == '"':
            j = i + 1
            while j < n and s[j] != '"':
                j += 2 if s[j] == '\\' else 1
            for k in range(i, min(j + 1, n)):
                if out[k] != '\n': out[k] = ' '
            i = j + 1
        elif s[i] == "'" and i + 2 < n and s[i + 2] == "'" and (i == 0 or not id_rest(s[i - 1])):
            out[i + 1] = ' '; i += 3  # char literal
        else:
            i += 1
    return ''.join(out)


def idents(s):
    """Yield (start offset, dotted identifier, preceded_by_dot)."""
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if ch == '«':
            j = s.find('»', i)
            if j < 0: break
            i = j + 1; continue
        if id_start(ch) and (i == 0 or not id_rest(s[i - 1])):
            j = i
            while True:
                while j < n and id_rest(s[j]): j += 1
                if j + 1 < n and s[j] == '.' and (id_start(s[j + 1])):
                    j += 1; continue
                break
            pre_dot = i > 0 and s[i - 1] == '.' and not (i > 1 and s[i - 2] == '.')
            yield i, s[i:j], pre_dot
            i = j
        else:
            i += 1


OPEN, CLOSE = '([{⦃⟨', ')]}⦄⟩'

# Lean keywords and tactic names: a bare token of this form is syntax, not a declaration
SYNTAX = set('''exact intro intros apply refine simp simp_all simpa rw rwa rfl use show calc have obtain by fun
at with using only constructor ext congr cases induction rcases rintro trans symm linarith positivity ring
ring_nf field norm_num omega decide exists left right specialize aesop grind gcongr grw nlinarith push_cast
norm_cast exfalso contradiction assumption subst unfold change convert filter_upwards field_simp set let from
then else if match do return where in open for this case next all_goals any_goals first try repeat refine'
exacts choose lift classical haveI letI infer_instance inferInstance apply_fun nth_rw erw dsimp simp_rw
fin_cases interval_cases split_ifs by_cases by_contra push_neg tauto continuity measurability fun_prop
bound module abel group noncomm_ring zify qify lia polyrith mono suffices generalize wlog clear revert
mod_cast exact_mod_cast assumption_mod_cast native_decide sorry'''.split())


def split_statement(code):
    """Offset of the end of the statement in comment-stripped code of one declaration."""
    depth, i, n = 0, 0, len(code)
    while i < n:
        c = code[i]
        if c in OPEN: depth += 1
        elif c in CLOSE: depth = max(0, depth - 1)
        elif depth == 0:
            if code.startswith(':=', i): return i
            if c == '\n':
                m = re.match(r'[ \t]*(\|\s|where\b)', code[i + 1:])
                if m: return i
            if code.startswith(' where', i) and (i + 6 >= n or not id_rest(code[i + 6])): return i
        i += 1
    return n


BINDER = re.compile(r'[\(\{\[⦃]\s*([^:()\[\]{}⦃⦄]+?)\s*:\s*([^\s()\[\]{},]+)')


def binder_types(text):
    """Map local names to the head identifier of their type, from binders in `text`."""
    out = {}
    for m in BINDER.finditer(text):
        head = m.group(2)
        if not head or not id_start(head[0]): continue
        for v in m.group(1).split():
            if v and id_start(v[0]):
                out[v] = head
    return out


LOCAL_INTRO = re.compile(r'(?<![\w.])(?:∀|∃!|∃|fun|λ|∑|∏|⋃|⋂|have|obtain|let|set|intro|rintro|intros|with|'
                         r'generalize|by_cases)\s+([^\n:=↦,∈|]*)')


def local_names(code):
    out = set(binder_types(code))
    for m in LOCAL_INTRO.finditer(code):
        for _, i, _ in idents(m.group(1)):
            if '.' not in i:
                out.add(i)
    return out


def looks_local(x, locals_):
    """A first component that is a local variable rather than a namespace."""
    if x in locals_:
        return True
    return len(x) <= 2 or not x[0].isupper()


def binder_groups(text):
    """Binder groups of a `variable` command: (bracket, names, type text)."""
    out, i, n = [], 0, len(text)
    pairs = {'(': ')', '{': '}', '[': ']', '⦃': '⦄'}
    while i < n:
        c = text[i]
        if c in pairs:
            depth, j = 0, i
            while j < n:
                if text[j] in OPEN: depth += 1
                elif text[j] in CLOSE:
                    depth -= 1
                    if depth == 0: break
                j += 1
            inner = text[i + 1:j]
            k = inner.find(':')
            if k >= 0 and not inner.startswith(':'):
                nm, ty = inner[:k], inner[k + 1:]
            else:
                nm, ty = '', inner
            names_ = [x for x in nm.split() if x and id_start(x[0])]
            out.append((c, names_, ty))
            i = j + 1
        else:
            i += 1
    return out


def allvarnames(groups):
    return {x for _, ns, _ in groups for x in ns}


def module_of(path):
    rel = os.path.relpath(path, SRC)[:-5]
    return rel.replace(os.sep, '.')


def files():
    out = []
    for top in ('Lib', 'New'):
        for dp, _, fs in os.walk(os.path.join(SRC, top)):
            for f in fs:
                if f.endswith('.lean'):
                    out.append(os.path.join(dp, f))
    out += [os.path.join(SRC, 'Main.lean'), os.path.join(SRC, 'Statements.lean')]
    return sorted(out)


HEAD = re.compile(r'^(?:@\[[^\n]*?\]\s*)*((?:(?:%s)\s+)*)(theorem|lemma|def|abbrev|instance|structure|class\s+inductive|class\s+abbrev|class|inductive|opaque|axiom)\b' % '|'.join(MODS))


def parse_file(path):
    """Commands of one file with their scope (namespaces, opens, variables)."""
    raw = open(path, encoding='utf-8').read()
    code = strip_comments(raw)
    lines = code.split('\n')
    rawlines = raw.split('\n')
    # command starts: column-0 lines that are not blank and not continuation punctuation
    starts = []
    for i, l in enumerate(lines):
        if l and not l[0].isspace() and l[0] not in ')]}|⟩,.':
            starts.append(i)
    # docstrings / attributes that precede a declaration belong to it
    cmds = []
    for k, s in enumerate(starts):
        e = (starts[k + 1] if k + 1 < len(starts) else len(lines))
        while e - 1 > s and not lines[e - 1].strip():
            e -= 1  # drop trailing blank lines and the next declaration's doc comment
        cmds.append([s, e])
    # attach raw doc comment start (raw line with '/--' at col 0 above, blanked in code)
    return raw, rawlines, code, lines, cmds


def main():
    decls = {}          # full name -> record
    order = []
    per_file = []
    for path in files():
        mod = module_of(path)
        raw, rawlines, code, lines, cmds = parse_file(path)
        ns_stack = []   # list of (kind, name parts)
        opens = [[]]    # stack of open lists per scope
        variables = [[]]
        pending_open_in = []
        for s, e in cmds:
            text = '\n'.join(lines[s:e])
            first = lines[s]
            t = first.strip()
            # scoping commands
            m = re.match(r'namespace\s+(\S+)', t)
            if m:
                ns_stack.append(('ns', m.group(1).split('.'))); opens.append([]); variables.append([]); continue
            m = re.match(r'(noncomputable\s+)?section\b\s*(\S*)', t)
            if m:
                ns_stack.append(('sec', [])); opens.append([]); variables.append([]); continue
            m = re.match(r'end\b\s*(\S*)', t)
            if m and not HEAD.match(t):
                if ns_stack:
                    ns_stack.pop(); opens.pop(); variables.pop()
                continue
            m = re.match(r'open\s+(?:scoped\s+)?(.*?)(\s+in)?\s*$', text.replace('\n', ' '))
            if t.startswith('open ') or t.startswith('open\t'):
                body = text.replace('\n', ' ')
                inm = re.search(r'\bin\b', body)
                names = re.sub(r'\bscoped\b', ' ', body[4:])
                names = re.sub(r'\(.*?\)', ' ', names)
                if inm:
                    # `open X in` applies to the rest of this command only
                    head, rest = body.split(' in', 1)
                    nn = [x for x in re.sub(r'\bscoped\b', ' ', head[4:]).split() if x != 'hiding']
                    pending_open_in = nn
                    if not HEAD.match(rest.strip()):
                        continue
                    t = rest.strip()
                else:
                    opens[-1].extend(x for x in names.split() if x not in ('hiding', 'renaming', '→'))
                    continue
            if t.startswith('export '):
                opens[-1].extend(x for x in re.sub(r'\(.*?\)', ' ', t[7:]).split())
                continue
            if t.startswith('variable'):
                variables[-1].append(text[8:]); continue
            mh = HEAD.match(text.lstrip()) if not text.startswith('open') else HEAD.match(t)
            if not mh:
                pending_open_in = []
                continue
            mods, kw = mh.group(1).split(), mh.group(2)
            kw = 'class' if kw.startswith('class') else kw
            after = text[text.find(mh.group(0)) + len(mh.group(0)):] if mh.group(0) in text else ''
            mname = re.match(r'\s*([^\s:({\[⦃⟨]+)', after)
            cur_ns = [p for kind, parts in ns_stack for p in parts]
            if kw == 'instance':
                mi = re.match(r'\s*(?:\(priority\s*:=\s*[^)]*\)\s*)?([^\s:({\[⦃⟨]+)\s', after)
                if mi and mi.group(1) not in ('where',) and id_start(mi.group(1)[0]) and not after.lstrip().startswith(('(', '[', '{', ':')):
                    nm = mi.group(1)
                else:
                    nm = f'inst@L{s + 1}'
            else:
                if not mname: continue
                nm = mname.group(1)
            if nm.startswith('_root_.'):
                full = nm[len('_root_.'):]
            else:
                full = '.'.join(cur_ns + [nm]) if cur_ns else nm
            # doc comment start in raw text: look upward for '/--' at column 0 right above
            ds = s
            j = s - 1
            while j >= 0 and rawlines[j].strip() and (rawlines[j].lstrip().startswith(('/--', '@[')) or j >= 0 and lines[j].strip() == ''):
                if rawlines[j].startswith('/--') or rawlines[j].startswith('@['):
                    ds = j
                j -= 1
                if j < s - 60: break
            # statement / body split
            body = text
            cut = split_statement(body)
            rec = {
                'n': full, 'm': mod, 'k': DECL_KW[kw], 'kw': kw,
                'priv': 'private' in mods, 'struct': kw in ('structure', 'class'), 'cls': kw == 'class',
                'inst': kw == 'instance', 'proj': False,
                'r': [ds + 1, 0, e, 0, s + 1],
                'stmt_code': body[:cut], 'body_code': body[cut:],
                'ns': cur_ns, 'self_ns': full.split('.')[:-1],
                'opens': [o for lst in opens for o in lst] + pending_open_in,
                'vars': [v for lst in variables for v in lst],
                'file': path,
            }
            pending_open_in = []
            if full in decls:
                full = f'{full}@{mod}:{s + 1}'; rec['n'] = full
            decls[full] = rec; order.append(full)
            # structure fields and constructors
            if kw in ('structure', 'class'):
                mw = re.search(r'\bwhere\b', body)
                ctor = 'mk'
                if mw:
                    fields_txt = body[mw.end():]
                    mc = re.match(r'\s*(\S+)\s*::', fields_txt)
                    if mc: ctor = mc.group(1); fields_txt = fields_txt[mc.end():]
                    for fl in re.finditer(r'^  \(?([^\s:(){}\[\].]+(?:\s+[^\s:(){}\[\].]+)*)\s*:', fields_txt, re.M):
                        for fn in fl.group(1).split():
                            if id_start(fn[0]):
                                fr = full + '.' + fn
                                if fr not in decls:
                                    decls[fr] = dict(rec, n=fr, k='def', struct=False, cls=False, inst=False,
                                                     proj=True, stmt_code='', body_code='', field_of=full)
                                    order.append(fr)
                cn = full + '.' + ctor
                decls.setdefault(cn, dict(rec, n=cn, k='ctor', struct=False, cls=False, inst=False,
                                          stmt_code='', body_code='', field_of=full)); order.append(cn)
            if kw == 'inductive':
                for mc in re.finditer(r'^\s*\|\s*([^\s:({\[]+)', body, re.M):
                    cn = full + '.' + mc.group(1)
                    decls.setdefault(cn, dict(rec, n=cn, k='ctor', struct=False, cls=False, inst=False,
                                              stmt_code='', body_code='', field_of=full)); order.append(cn)

    names = set(decls)
    by_last = collections.defaultdict(set)
    for n in names:
        parts = n.split('.')
        for k in range(1, min(4, len(parts)) + 1):
            by_last['.'.join(parts[-k:])].add(n)

    # visibility: a declaration sees earlier declarations of its file and its transitive imports
    imports = {}
    for path in files():
        mod = module_of(path)
        imports[mod] = [l.split()[1] for l in open(path, encoding='utf-8') if l.startswith('import ')]
    closure = {}
    def clos(m):
        if m in closure: return closure[m]
        closure[m] = set()
        out = set()
        for i in imports.get(m, []):
            if i in imports:
                out.add(i); out |= clos(i)
        closure[m] = out
        return out
    for m in imports: clos(m)
    def visible(c, rec):
        d = decls[c]
        if d['m'] == rec['m']:
            return d['r'][4] <= rec['r'][4]
        return d['m'] in closure.get(rec['m'], ())

    # most common binder type of each local name, over the whole project
    tcount = collections.defaultdict(collections.Counter)
    for rec in decls.values():
        for vtxt in rec.get('vars', []):
            for k2, v2 in binder_types(vtxt).items(): tcount[k2][v2] += 1
        for k2, v2 in binder_types(rec.get('stmt_code', '')).items(): tcount[k2][v2] += 1
    common_type = {}
    for k2, c in tcount.items():
        (ty, nty), = c.most_common(1)
        if nty >= 5 and nty >= 0.6 * sum(c.values()):
            common_type[k2] = ty
    names_first = {n.split('.')[0] for n in names}

    namespaces = set()
    for n in names:
        parts = n.split('.')
        for k in range(1, len(parts)):
            namespaces.add('.'.join(parts[:k]))
    scope_cache = {}

    def scope(rec):
        """Namespace prefixes to try, innermost first: own name's namespaces, current namespaces,
        then each `open` resolved against the current namespaces and the earlier opens."""
        key = (tuple(rec['ns']), tuple(rec['self_ns']), tuple(rec['opens']))
        if key in scope_cache:
            return scope_cache[key]
        prefixes = []
        sn, ns = rec['self_ns'], rec['ns']
        for k in range(len(sn), 0, -1):
            prefixes.append('.'.join(sn[:k]))
        for k in range(len(ns), -1, -1):
            prefixes.append('.'.join(ns[:k]))
        opened = []
        for o in rec['opens']:
            for base in prefixes + opened:
                full = (base + '.' + o) if base else o
                if full in namespaces and full not in opened:
                    opened.append(full)
        out = []
        for x in prefixes + opened:
            if x not in out:
                out.append(x)
        scope_cache[key] = out
        return out

    def candidates(ident, rec):
        """Full names an identifier could denote, in Lean's order of preference."""
        return [(p + '.' + ident) if p else ident for p in scope(rec)]

    def resolve(ident, rec, local_types, locals_=frozenset()):
        """Return (full name, method) or None."""
        for c in candidates(ident, rec):
            if c in names and visible(c, rec):
                return c, 'name'
        parts = ident.split('.')
        # dot notation: x.foo.bar with x a typed local
        if len(parts) >= 2 and parts[0] in local_types:
            th = local_types[parts[0]]
            r = resolve(th, rec, {})
            tail = '.'.join(parts[1:])
            if r is None and th:
                # type from Mathlib: the project may extend its namespace (`Set.conjClosure`)
                r2 = resolve(th.split('.')[-1] + '.' + tail, rec, {}) or resolve(th.split('.')[-1] + '.' + parts[1], rec, {})
                if r2 and r2[1] == 'name':
                    return r2[0], 'dot-typed'
            if r:
                cand = r[0] + '.' + tail
                if cand in names and visible(cand, rec):
                    return cand, 'dot-typed'
                # first field only
                cand = r[0] + '.' + parts[1]
                if cand in names and visible(cand, rec):
                    return cand, 'dot-typed'
        # untyped local (pattern, `fun`, `obtain`): the type this name most often has in a binder
        if len(parts) >= 2 and parts[0] not in local_types and parts[0] in common_type:
            r = resolve(common_type[parts[0]], rec, {})
            if r:
                for cand in (r[0] + '.' + '.'.join(parts[1:]), r[0] + '.' + parts[1]):
                    if cand in names and visible(cand, rec):
                        return cand, 'dot-common-type'
        # last resort: `x.foo` with `x` a local of unknown type, and `foo` naming exactly one
        # visible project declaration; only for distinctive field names
        if (len(parts) >= 2 and parts[0] not in names_first and looks_local(parts[0], local_types)
                and ('_' in parts[-1] or len(parts[-1]) >= 10)):
            tail = '.'.join(parts[1:])
            cs = {c for c in by_last.get(tail, ()) if c.endswith('.' + tail) and visible(c, rec)}
            if len(cs) == 1:
                return next(iter(cs)), 'dot-unique'
        return None

    def uses(code, rec, local_types, locals_=frozenset()):
        found = {}
        for off, ident, pre_dot in idents(code):
            if pre_dot:
                # `.foo` or `(x).foo`: resolve only if unique among project names with that last part
                last = ident.split('.')[-1]
                if not ('_' in last or len(last) >= 10):
                    continue
                cs = by_last.get(ident, set())
                cs = {c for c in cs if c.split('.')[-1] == last and visible(c, rec)}
                if len(cs) == 1:
                    c = next(iter(cs))
                    if c != rec['n']: found.setdefault(c, 'dot-unique')
                continue
            if '.' not in ident and (ident in locals_ or ident in SYNTAX):
                continue  # a bound variable or syntax, not a global name
            if len(ident) == 1 and code[off + 1:off + 2] == '[':
                continue  # notation such as Mathlib's `Ω[B⁄R]`
            lt = dict(local_types); lt.update({x: None for x in locals_ if x not in lt})
            r = resolve(ident, rec, {k: v for k, v in local_types.items()}, locals_)
            if r is None:
                # strip trailing components (e.g. `foo.mp`, `foo.le`) and try again
                ps = ident.split('.')
                for k in range(len(ps) - 1, 0, -1):
                    r = resolve('.'.join(ps[:k]), rec, local_types, locals_)
                    if r and r[1] == 'dot-unique':
                        r = None; break
                    if r: r = (r[0], r[1] + '+suffix'); break
            if r and r[0] != rec['n']:
                found.setdefault(r[0], r[1])
            # chained dot notation `D.foo.bar`: `bar` is about the type of `D.foo`; link later parts
            # that name exactly one visible project declaration (distinctive names only)
            ps = ident.split('.')
            if len(ps) >= 2 and (looks_local(ps[0], set(local_types) | set(locals_)) or (r and r[1].startswith('dot'))):
                covered = r[0].split('.')[-1] if r else None
                for j in range(1, len(ps)):
                    c = ps[j]
                    if c == covered or not ('_' in c or len(c) >= 10):
                        continue
                    cs = {x for x in by_last.get(c, ()) if x.split('.')[-1] == c and visible(x, rec)}
                    if len(cs) == 1:
                        x = next(iter(cs))
                        if x != rec['n']:
                            found.setdefault(x, 'dot-chain')
        return found

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    stats = collections.Counter()
    with open(OUT, 'w', encoding='utf-8') as f:
        for n in order:
            rec = decls[n]
            if rec.get('field_of'):
                t = {rec['field_of']: 'field'}
                v = {}
            else:
                lt = {}
                for vtxt in rec['vars']:
                    lt.update(binder_types(vtxt))
                lt.update(binder_types(rec['stmt_code']))
                # binders in the body (fun x : T, have h : T) are not tracked
                loc_s = local_names(rec['stmt_code'])
                for vtxt in rec['vars']:
                    loc_s |= set(binder_types(vtxt))
                t = uses(rec['stmt_code'], rec, lt, loc_s)
                # `variable` binders: Lean 4 includes a binder when the statement (for a definition,
                # also the body) mentions it, then binders mentioned by included ones, and instance
                # binders all of whose variables are included
                ment = {i.split('.')[0] for _, i, _ in idents(rec['stmt_code'])}
                if rec['k'] != 'thm':
                    ment |= {i.split('.')[0] for _, i, _ in idents(rec['body_code'])}
                groups = [g for vtxt in rec['vars'] for g in binder_groups(vtxt)]
                inc = [False] * len(groups)
                incnames = set()
                changed = True
                while changed:
                    changed = False
                    for gi, (br, gnames, gtype) in enumerate(groups):
                        if inc[gi]:
                            continue
                        toks = {i.split('.')[0] for _, i, _ in idents(gtype)}
                        if br == '[':
                            vars_in = toks & allvarnames(groups)
                            ok = bool(vars_in) and vars_in <= incnames
                        else:
                            ok = bool(set(gnames) & (ment | {x for gj, g in enumerate(groups) if inc[gj]
                                                             for _, x, _ in idents(g[2])}))
                        if ok:
                            inc[gi] = True; incnames |= set(gnames); changed = True
                for gi, (br, gnames, gtype) in enumerate(groups):
                    if inc[gi]:
                        for k2 in uses(gtype, rec, lt, loc_s):
                            t.setdefault(k2, 'variable')
                v = uses(rec['body_code'], rec, lt, loc_s | local_names(rec['body_code']))
                v = {k2: m for k2, m in v.items() if k2 not in t}
            for m in list(t.values()) + list(v.values()):
                stats[m] += 1
            stmt_txt = ' '.join(rec['stmt_code'].split())
            out = {'n': n, 'priv': rec['priv'], 'm': rec['m'], 'k': rec['k'], 'struct': rec['struct'],
                   'cls': rec['cls'], 'inst': rec['inst'], 'proj': rec['proj'], 'r': rec['r'],
                   't': sorted(t), 'v': sorted(v), 'tm': 0, 'pp': stmt_txt[:4000],
                   'tmeth': t, 'vmeth': v}
            f.write(json.dumps(out, ensure_ascii=False) + '\n')
    print(len(order), 'declarations;', dict(stats))


if __name__ == '__main__':
    main()
