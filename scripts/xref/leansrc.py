"""Source-only reader for the Lean files of the proof (no Lean run). Shared by the xref scripts.

parse(text) splits a file into top-level commands and tracks, for each command, the namespace stack,
the `open`s in force, and the `variable` names in force. Declarations get their full Lean name.

Simplifications (see research/lean-reader/xref/report.md for what they cost):
- A command starts at a column-0 line; indented lines and lines starting with `|`, `where`, `deriving`,
  `termination_by`, closing brackets etc. continue it. The corpus is machine-formatted, so this holds.
- No comments exist in the corpus; we still blank `--` and `/- -/` comments and string literals.
- Auxiliary `where` definitions, unnamed instances, `macro`/`notation` output and `export` are not indexed.
"""
import re

# Lean 4 identifier characters (Lean's isLetterLike + isSubScriptAlnum, ASCII letters, _ ' ! ?)
_START = (r"A-Za-z_α-κμ-ωΑ-ΟΡΣ-Ωϊ-ϻ"
          r"ἀ-῾℀-⅏\U0001d49c-\U0001d59f")
_REST = _START + r"0-9'!?₀-₉ₐ-ₜᵢ-ᵪⱼ"
ATOM = rf"[{_START}][{_REST}]*|«[^»]*»"
IDENT = re.compile(rf"(?:{ATOM})(?:\.(?:{ATOM}))*")
ATOM_RE = re.compile(ATOM)
IDCHAR = re.compile(rf"[{_REST}.]")

CONT = ('|', 'where', 'deriving', 'termination_by', 'decreasing_by', ')', ']', '}', '⟩', ':=', 'with', '·')
MODS = {'private', 'protected', 'noncomputable', 'partial', 'unsafe', 'nonrec', 'scoped', 'local'}
DECL_KINDS = {'theorem', 'lemma', 'def', 'abbrev', 'instance', 'structure', 'class', 'inductive',
              'opaque', 'axiom', 'example', 'alias', 'irreducible_def'}

_STR = re.compile(r'"(?:\\.|[^"\\])*"')
_LINECOM = re.compile(r'--[^\n]*')


def _strip_block_comments(t):
    if '/-' not in t:
        return t
    out, i, depth, n = [], 0, 0, len(t)
    start = 0
    while i < n:
        if t.startswith('/-', i):
            if depth == 0:
                out.append(t[start:i])
            depth += 1; i += 2; continue
        if depth and t.startswith('-/', i):
            depth -= 1; i += 2
            if depth == 0:
                start = i
            continue
        if depth and t[i] == '\n':
            out.append('\n')
        i += 1
    if depth == 0:
        out.append(t[start:])
    return ''.join(out)


def clean(text):
    """Blank strings and comments, keeping line numbers."""
    text = _strip_block_comments(text)
    if '"' in text:
        text = _STR.sub('""', text)
    if '--' in text:
        text = _LINECOM.sub('', text)
    return text


def skip_brackets(s, i, op='[', cl=']'):
    """s[i] == op; return index after the matching close bracket."""
    d = 0
    while i < len(s):
        if s[i] == op:
            d += 1
        elif s[i] == cl:
            d -= 1
            if d == 0:
                return i + 1
        i += 1
    return i


def strip_attrs(s):
    """Remove leading `@[...]` attribute blocks and `set_option x y in` prefixes from a command head."""
    while True:
        s = s.lstrip()
        if s.startswith('@['):
            s = s[skip_brackets(s, 1):]
        elif s.startswith('set_option '):
            m = re.match(r'set_option\s+\S+\s+\S+\s+in\b', s)
            if not m:
                return s
            s = s[m.end():]
        else:
            return s


def split_commands(lines):
    """Yield (start_line_1based, [lines]) for each top-level command."""
    cur, start = None, 0
    for i, ln in enumerate(lines, 1):
        if ln and ln[0] not in ' \t' and not ln.startswith(CONT):
            # a lone attribute line glues to the next column-0 line
            if cur is not None and (not strip_attrs(' '.join(cur)).strip()
                                    or _SETOPT_IN.match(cur[-1])):
                cur.append(ln); continue
            if cur is not None:
                yield start, cur
            cur, start = [ln], i
        elif cur is not None:
            cur.append(ln)
    if cur is not None:
        yield start, cur


_SETOPT_IN = re.compile(r'(@\[.*\]\s*)?set_option\s+\S+\s+\S+\s+in\s*$')
_OPEN_ITEM = re.compile(r'\(([^)]*)\)|(\S+)')


def parse_open(rest):
    """`open ...` body -> (list of (namespace, mode, names), applies_to_next_only)."""
    rest = rest.strip()
    in_next = False
    m = re.search(r'\s+in(\s|$)', rest)
    if m:
        in_next, rest = True, rest[:m.start()]
    if rest.startswith('scoped '):
        return [], in_next          # `open scoped` brings in notation/instances only, no names
    toks = rest.split()
    if 'hiding' in toks:
        k = toks.index('hiding')
        return [(ns, 'all', ()) for ns in toks[:k - 1]] + [(toks[k - 1], 'hiding', tuple(toks[k + 1:]))], in_next
    if 'renaming' in toks:
        k = toks.index('renaming')
        pairs = re.findall(r'(\S+)\s*→\s*([^\s,]+)', ' '.join(toks[k + 1:]))
        return [(toks[k - 1], 'renaming', tuple(pairs))], in_next
    out = []
    for m in _OPEN_ITEM.finditer(rest):
        if m.group(1) is not None:
            if out:
                ns = out.pop()[0]
                out.append((ns, 'only', tuple(m.group(1).split())))
        else:
            out.append((m.group(2), 'all', ()))
    return out, in_next


_BINDER_GROUP = re.compile(rf"[(\{{⦃\[]\s*((?:(?:{ATOM})\s+)*(?:{ATOM}))\s*:(?![=:])")


def variable_names(text):
    return {n for g in _BINDER_GROUP.findall(text) for n in g.split()}


_FIELD = re.compile(rf"^(\s+)((?:(?:{ATOM})\s+)*(?:{ATOM}))\s*(?::(?![=:])|\(|\{{|\[|:=)")
_CTOR = re.compile(rf"\|\s*({ATOM})")
_MKCTOR = re.compile(rf"^\s+({ATOM})\s*::")


def decl_head(text):
    """Return (kind, name_or_None, mods, rest_after_name) for a declaration command, else None."""
    s = strip_attrs(text)
    mods = set()
    while True:
        w = s.split(None, 1)
        if not w:
            return None
        if w[0] in MODS:
            mods.add(w[0]); s = w[1] if len(w) > 1 else ''
            continue
        break
    kind = w[0]
    if kind == 'class' and len(w) > 1 and w[1].startswith('inductive'):
        kind, s = 'inductive', w[1][len('inductive'):]
    elif kind not in DECL_KINDS:
        return None
    else:
        s = w[1] if len(w) > 1 else ''
    if kind == 'example':
        return kind, None, mods, s
    s = s.lstrip()
    if kind == 'instance' and s.startswith('('):        # instance (priority := n) name : ...
        s = s[skip_brackets(s, 0, '(', ')'):].lstrip()
    m = IDENT.match(s)
    if not m:
        return kind, None, mods, s
    name = m.group(0)
    after = s[m.end():]
    if after.startswith('.{'):
        after = after[skip_brackets(after, 1, '{', '}'):]
    return kind, name, mods, after


class Cmd:
    __slots__ = ('line', 'text', 'kind', 'name', 'full', 'mods', 'ns', 'opens', 'vars', 'members', 'nlines')

    def __init__(self, line, text, nlines):
        self.line, self.text, self.nlines = line, text, nlines
        self.kind = self.name = self.full = None
        self.mods, self.members = set(), []


def parse(text):
    """Parse a file. Returns dict with imports, cmds (list of Cmd), namespaces, sections, opens (raw)."""
    lines = clean(text).split('\n')
    stack = []                  # (kind, components, saved_opens, saved_vars)
    ns = []                     # current namespace components
    opens = []                  # active opens: list of (ns_text, mode, names, ns_context_tuple)
    vars_ = set()
    pending_in = None           # opens from `open X in` for the next command only
    imports, cmds, namespaces, sections, raw_opens, variables = [], [], [], 0, [], []
    for start, cl in split_commands(lines):
        head = cl[0]
        w = head.split()
        k = w[0]
        if k == 'import' or k == 'public' and w[1:2] == ['import']:
            imports += w[1:] if k == 'import' else w[2:]
            continue
        if k == 'namespace' and len(w) > 1:
            stack.append(('ns', w[1].split('.'), list(opens), set(vars_)))
            ns = ns + w[1].split('.')
            namespaces.append('.'.join(ns))
            continue
        if k == 'section' or (k == 'noncomputable' and w[1:2] == ['section']) or k == 'mutual':
            stack.append(('sec', [], list(opens), set(vars_)))
            sections += k != 'mutual'
            continue
        if k == 'end':
            if stack:
                kind, comps, opens, vars_ = stack.pop()
                if kind == 'ns':
                    ns = ns[:len(ns) - len(comps)]
            continue
        if k == 'open':
            rest = re.split(r'\s+in\s+', head, maxsplit=1)
            one_line = len(rest) == 2 and rest[1].strip()      # `open X in theorem ...` on one line
            items, in_next = parse_open((rest[0] + ' in' if one_line else ' '.join(cl))[len('open'):])
            items = [(a, b, c, tuple(ns)) for a, b, c in items]
            raw_opens += [(start, a) for a, *_ in items]
            if in_next:
                pending_in = items
                if one_line:
                    cl = [rest[1]] + cl[1:]
                    head = cl[0]; w = head.split(); k = w[0]
                else:
                    continue
            else:
                opens = opens + items
                continue
        if k in ('set_option', 'universe', 'attribute', 'omit', 'include', 'variable') and k != 'variable' \
                and not (k == 'set_option' and ' in' in head):
            c = Cmd(start, '\n'.join(cl), len(cl)); c.kind = k
            c.ns, c.opens, c.vars = tuple(ns), opens + (pending_in or []), vars_
            cmds.append(c); pending_in = None
            continue
        if k == 'variable':
            t = '\n'.join(cl)
            names = variable_names(t)
            variables += sorted(names)
            c = Cmd(start, t, len(cl)); c.kind = 'variable'
            c.ns, c.opens, c.vars = tuple(ns), opens + (pending_in or []), set(vars_)
            cmds.append(c); pending_in = None
            vars_ = vars_ | names
            continue
        t = '\n'.join(cl)
        c = Cmd(start, t, len(cl))
        c.ns, c.opens, c.vars = tuple(ns), opens + (pending_in or []), vars_
        pending_in = None
        h = decl_head(t)
        if h:
            kind, name, mods, after = h
            c.kind, c.name, c.mods = kind, name, mods
            if name:
                if name.startswith('_root_.'):
                    c.full = name[7:]
                else:
                    c.full = '.'.join(ns + [name])
                if kind in ('structure', 'class', 'inductive'):
                    c.members = members(kind, cl)
        else:
            c.kind = 'other:' + k
        cmds.append(c)
    return {'imports': imports, 'cmds': cmds, 'namespaces': namespaces, 'sections': sections,
            'opens': raw_opens, 'variables': variables}


def members(kind, cl):
    """Fields / constructors of a structure, class or inductive (names relative to the type)."""
    out = []
    if kind == 'inductive':
        for i, ln in enumerate(cl):
            for m in _CTOR.finditer(ln):
                out.append((m.group(1), i, 'ctor'))
        return out
    body = '\n'.join(cl)
    ctor = 'mk'
    wi = None
    for i, ln in enumerate(cl):
        if re.search(r'\bwhere\s*$', ln) or re.match(r'\s*where\b', ln):
            wi = i; break
    if wi is None:
        return [('mk', 0, 'ctor-auto')]
    indent = None
    for i in range(wi + 1, len(cl)):
        ln = cl[i]
        m = _MKCTOR.match(ln)
        if m:
            ctor = m.group(1); continue
        m = _FIELD.match(ln)
        if m:
            ind = len(m.group(1))
            if indent is None:
                indent = ind
            if ind == indent:
                for n in m.group(2).split():
                    out.append((n, i, 'field'))
    out.append((ctor, 0, 'ctor' if ctor != 'mk' or 'mk ::' in body else 'ctor-auto'))
    return out
