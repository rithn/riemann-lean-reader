"""79b/79c. Resolve identifiers in Lean files against declarations in the file and its transitive imports.

usage: uv run --no-project python -I resolve.py <lean/src> <xref data dir> [n_sample=500] [seed=79] [--all]

Needs decls.tsv.gz and files.jsonl.gz from index_decls.py. Sample: Main plus every module within 4 imports
of Main (the import chain at the top of the proof), then random other modules (fixed seed) up to n_sample.
Writes sample.txt, occurrences.tsv.gz (one row per identifier occurrence) and summary.json.

Name lookup follows Lean 4's resolveGlobalName, restricted to project declarations visible from the file:
 1. current namespace (and the declaration's own name prefix), innermost level first, parents next;
 2. if nothing: the name from the root, private names of this file, and every `open`ed namespace
    (`open X (a)`, `hiding`, `renaming` honoured; atomic names skip `protected` declarations);
 3. if nothing and the name is dotted: drop the last component (Lean reads it as a projection) and retry.
One candidate (name, module) = resolved, several = ambiguous, none = unresolved. Mathlib and Lean core are
not indexed (not local), so their names land in "unresolved".
"""
import os, sys, re, gzip, json, time, random, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leansrc
from leansrc import IDENT, ATOM, ATOM_RE

KEYWORDS = set("""
theorem lemma def abbrev instance structure class inductive example where extends deriving with fun λ let have
show from at by do then else if match return for in mut unless this Type Sort Prop forall exists suffices
calc only using generalizing at_top open namespace section end variable universe noncomputable private
protected partial unsafe local scoped attribute set_option omit include termination_by decreasing_by
macro syntax notation infix infixl infixr prefix postfix elab mutual nonrec haveI letI show_term
_ sorry
exact apply refine refine' intro intros rintro rcases obtain cases cases' induction induction' simp simp_all
simpa dsimp rw rwa erw rewrite nth_rw nth_rewrite simp_rw unfold unfold_let delta constructor use exists left
right norm_num ring ring_nf linarith nlinarith positivity omega decide aesop tauto field_simp push_cast
exact_mod_cast norm_cast assumption_mod_cast gcongr congr ext funext split_ifs split by_cases by_contra
by_contra! contradiction exfalso specialize change convert convert_to trivial assumption subst subst_vars
filter_upwards set generalize choose classical exacts first try repeat repeat' all_goals any_goals iterate case
next rename_i clear revert symm trans infer_instance linear_combination conv conv_lhs conv_rhs abel
fin_cases interval_cases push_neg zify qify lift peel wlog apply_fun mono bound beta_reduce group noncomm_ring
module norm_num1 rfl' exact? apply? simp? decide! native_decide refine_lift injection injections
contrapose contrapose! nontriviality inhabit rcases' obtain' subsingleton aesop_cat continuity measurability
fun_prop polyrith compute_degree monicity field_simp' slim_check plausible ac_rfl cc itauto abel_nf
simp_intro unfold_projs whnf exact_rfl apply_rules solve_by_elim library_search show_term existsi
refine_struct match_target swap rotate pick_goal on_goal focus done skip stop fail admit sorry
norm_num? positivity? gcongr? rel field_simp? ring1 ring_nf? linarith! nlinarith! cancel_denoms
lia tfae_have tfae_finish dsimp? simp_arith simpa? omega_nat bv_omega bv_decide calc? let'
""".split())
# Mathlib notation tokens that the lexer would read as identifiers
NOTATION = set('ℕ ℤ ℚ ℝ ℂ ℍ 𝓞 𝔸 ℙ 𝓝 𝓤 𝔼 ∂ ℵ ℶ ℤ_ ℚ_'.split())

# a letter glued to these is part of a notation such as →L[ℂ], →ₗ[R], ≃ₐ[K], ⊗[R], →+*
NOTATION_PREV = set('→≃↪↠⊗⧸⁅⁆‖|⟪⟫∘≫⋙')
QUANT = re.compile(r"(?:\bfun\b|λ|∀ᶠ|∃ᶠ|∀|∃!|∃|∑'|∏'|∑ᶠ|∏ᶠ|∑|∏|⨆|⨅|⋃|⋂|∫⁻|∫|∮|Σ'|Σ|Π)")
QUANT_END = re.compile(r",|=>|↦")
QUANT_STOP = re.compile(r":|∈|∉|<|≤|>|≥|≠|⊆|\bin\b|∣|=")
TAC_ALL = re.compile(r"(?<![\w.'])(?:intro|intros|rintro|introv|rename_i|ext|funext|choose|cases'|induction'|"
                     r"obtain|rcases|rcases'|peel|lift)\b(.*)$")
TAC_WITH = re.compile(r"(?<![\w.'])with\b(.*)$")
TAC_FIRST = re.compile(rf"(?<![\w.'])(?:have|haveI|let|letI|set|by_cases|by_contra!?|suffices|generalize|obtain|show|"
                       rf"replace|wlog|case|next)\s+({ATOM})")
ARM = re.compile(r"^\s*(?:·\s*)?\|(.*?)(?:=>|$)")
ASSIGN = re.compile(rf"({ATOM})\s*:=(?!=)")
SETB = re.compile(rf"\{{\s*({ATOM})\s*(?:\||∈|:(?![=:]))")
TYPEU = re.compile(rf"\b(?:Type|Sort)\*?\s+({ATOM})")
UNIV = re.compile(r"\.\{([^}]*)\}")


INST_GROUP = re.compile(r'\[[^\[\]]*\]')
TYPED = re.compile(r':[^()\[\]{}⦃⦄⟨⟩,]*')


def cut_colon(seg):
    """Part of a binder segment before its first depth-0 type ascription."""
    depth = 0
    for i, ch in enumerate(seg):
        if ch in '([{⦃⟨':
            depth += 1
        elif ch in ')]}⦄⟩':
            depth -= 1
        elif ch == ':' and depth == 0:
            return seg[:i]
    return seg


def pattern_part(seg):
    """Drop instance groups and type ascriptions, leaving the bound names."""
    seg = INST_GROUP.sub(' ', seg)
    return TYPED.sub(' ', seg)


def locals_of(text):
    """Heuristic set of locally bound names in one command."""
    loc = set(leansrc.variable_names(text))
    for m in QUANT.finditer(text):
        seg = text[m.end():m.end() + 400]
        e = QUANT_END.search(seg)
        seg = seg[:e.start()] if e else seg[:80]
        loc.update(leansrc.variable_names(seg))
        depth, cut = 0, len(seg)
        for i, ch in enumerate(seg):
            if ch in '([{⦃⟨':
                depth += 1
            elif ch in ')]}⦄⟩':
                depth -= 1
            elif depth == 0 and QUANT_STOP.match(seg, i):
                cut = i; break
        loc.update(ATOM_RE.findall(pattern_part(seg[:cut])))
    for ln in text.split('\n'):
        for rx in (TAC_ALL, TAC_WITH):
            for m in rx.finditer(ln):
                seg = re.split(r'\b(?:using|at)\b|:=|=>', m.group(1))[0]
                loc.update(ATOM_RE.findall(pattern_part(cut_colon(seg))))
        for m in TAC_FIRST.finditer(ln):
            loc.add(m.group(1))
        m = ARM.match(ln)
        if m:
            loc.update(ATOM_RE.findall(m.group(1)))
    loc.update(ASSIGN.findall(text))
    loc.update(SETB.findall(text))
    loc.update(TYPEU.findall(text))
    for g in UNIV.findall(text):
        loc.update(x.strip() for x in g.split(','))
    loc.discard('_'); loc.discard('rfl')
    return loc


ATTR = re.compile(r'@\[')


def blank_attrs(text):
    """Blank attribute lists `@[...]`, `attribute [...]` and `set_option x y in` (names there are not refs)."""
    out = list(text)
    for m in ATTR.finditer(text):
        e = leansrc.skip_brackets(text, m.start() + 1)
        for i in range(m.start(), e):
            if out[i] != '\n':
                out[i] = ' '
    t = ''.join(out)
    if t.lstrip().startswith('attribute'):
        i = t.find('[')
        if i >= 0:
            e = leansrc.skip_brackets(t, i)
            t = t[:i] + ' ' * (e - i) + t[e:]
    t = re.sub(r'set_option\s+\S+\s+\S+(\s+in)?', lambda m: ' ' * len(m.group(0)), t)
    return t


class Index:
    def __init__(self, d):
        self.mods, self.mid = [], {}
        self.decl = collections.defaultdict(list)       # name -> [(mod id, flags)]
        self.kind = {}
        with gzip.open(os.path.join(d, 'decls.tsv.gz'), 'rt', encoding='utf-8') as fh:
            next(fh)
            for ln in fh:
                n, m, line, k, fl = ln.rstrip('\n').split('\t')
                i = self.mid.get(m)
                if i is None:
                    i = self.mid[m] = len(self.mods); self.mods.append(m)
                self.decl[n].append((i, fl, int(line)))
                self.kind[n] = k
        self.imports = {}
        self.ns = set()
        with gzip.open(os.path.join(d, 'files.jsonl.gz'), 'rt', encoding='utf-8') as fh:
            for ln in fh:
                r = json.loads(ln)
                m = r['module']
                if m not in self.mid:
                    self.mid[m] = len(self.mods); self.mods.append(m)
                self.imports[self.mid[m]] = r['imports']
                self.ns.update(r['namespaces'])
        for i, imps in self.imports.items():
            self.imports[i] = [self.mid[x] for x in imps if x in self.mid]
        for n in self.decl:
            p = n.split('.')
            for k in range(1, len(p)):
                self.ns.add('.'.join(p[:k]))
        self.last = collections.defaultdict(list)
        for n in self.decl:
            self.last[n.rsplit('.', 1)[-1]].append(n)

    def closure(self, m):
        seen = {m}
        st = [m]
        while st:
            x = st.pop()
            for y in self.imports.get(x, ()):
                if y not in seen:
                    seen.add(y); st.append(y)
        return seen


class Resolver:
    def __init__(self, ix, mod):
        self.ix, self.me = ix, ix.mid[mod]
        self.clo = ix.closure(self.me)
        self.open_cache = {}
        self.stats = collections.Counter()

    def visible(self, name, atomic_via_scope=False):
        out = []
        for m, fl, _ in self.ix.decl.get(name, ()):
            if self.clo is not None and m not in self.clo:
                continue
            if 'p' in fl and m != self.me:
                continue
            if atomic_via_scope and 'P' in fl:
                continue
            out.append((name, m))
        return out

    def opens(self, raw):
        key = tuple(raw)
        r = self.open_cache.get(key)
        if r is not None:
            return r
        res = []
        for X, mode, names, ctx in raw:
            if X.startswith('_root_.'):
                cands = [X[7:]]
            else:
                cands = ['.'.join(ctx[:k] + (X,)) for k in range(len(ctx), 0, -1)] + [X]
                cands += [o + '.' + X for o, _, _ in res]
            for c in dict.fromkeys(cands):
                if c in self.ix.ns:
                    res.append((c, mode, names))
        self.open_cache[key] = res
        return res

    def resolve(self, tok, ns, opens):
        """-> (candidates, how) ; how in ns/root/open/proj/none"""
        idt, proj = tok, 0
        while True:
            atomic = '.' not in idt
            if idt.startswith('_root_.'):
                r = self.visible(idt[7:])
                return (r, 'root') if r else ([], 'none')
            levels = 0
            first = None
            for k in range(len(ns), 0, -1):
                r = self.visible('.'.join(ns[:k]) + '.' + idt, atomic)
                if r:
                    levels += 1
                    if first is None:
                        first = r
            if first:
                if levels > 1:
                    self.stats['ns_multi_level'] += 1
                return first, 'proj' if proj else 'ns'
            r = self.visible(idt)
            for o, mode, names in opens:
                if mode == 'all':
                    r += self.visible(o + '.' + idt, atomic)
                elif mode == 'hiding':
                    if idt.split('.')[0] not in names:
                        r += self.visible(o + '.' + idt, atomic)
                elif mode == 'only':
                    if idt in names:
                        r += self.visible(o + '.' + idt)
                elif mode == 'renaming':
                    for old, new in names:
                        if idt == new:
                            r += self.visible(o + '.' + old)
            if r:
                r = list(dict.fromkeys(r))
                return r, 'proj' if proj else ('open' if any(x[0] != idt for x in r) else 'root')
            if atomic:
                return [], 'none'
            idt = idt.rsplit('.', 1)[0]
            proj += 1


SKIP_KINDS = {'set_option', 'universe', 'omit', 'include'}


def process(src, ix, mod, out_rows):
    text = open(os.path.join(src, *mod.split('.')) + '.lean', encoding='utf-8', errors='replace').read()
    p = leansrc.parse(text)
    R = Resolver(ix, mod)
    univ = set()
    cnt = collections.Counter()
    for c in p['cmds']:
        if c.kind == 'universe':
            univ.update(c.text.split()[1:])
            continue
        if c.kind in SKIP_KINDS:
            continue
        if c.kind.startswith('other:'):
            cnt['blind:macro_or_notation_cmd'] += 1
            continue
        body = blank_attrs(c.text)
        loc = locals_of(body) | c.vars | univ
        ns = c.ns
        if c.full and c.name and not c.name.startswith('_root_.') and '.' in c.name:
            ns = ns + tuple(c.name.split('.')[:-1])
        elif c.name and c.name.startswith('_root_.') and c.name.count('.') > 1:
            ns = tuple(c.name[7:].split('.')[:-1])
        opens = R.opens(c.opens)
        if c.members:
            loc.update(n for n, _, _ in c.members)
        skipped_name = False
        lines_start = [0]
        for i, ch in enumerate(body):
            if ch == '\n':
                lines_start.append(i + 1)
        import bisect
        for m in IDENT.finditer(body):
            tok = m.group(0)
            s = m.start()
            if not skipped_name and c.name and tok == c.name:
                skipped_name = True
                continue
            prev = body[s - 1] if s else ' '
            first = tok.split('.')[0]
            if prev == '.':
                cat = 'blind:dot'
            elif prev == '?' or prev in NOTATION_PREV:
                cat = 'excl:keyword'
            elif first in KEYWORDS or first in NOTATION or tok.startswith('«'):
                cat = 'excl:keyword' if '.' not in tok or first not in ('this',) else 'excl:local_dot'
            elif first in loc:
                cat = 'excl:local' if '.' not in tok else 'excl:local_dot'
            else:
                cat = None
            line = c.line + bisect.bisect_right(lines_start, s) - 1
            if cat:
                cnt[cat] += 1
                out_rows.append((mod, line, tok, cat, '', '', 0))
                continue
            cands, how = R.resolve(tok, ns, opens)
            if len(cands) == 1:
                cat = 'resolved'
                tgt, tm = cands[0][0], ix.mods[cands[0][1]]
            elif cands:
                cat = 'ambiguous'
                tgt, tm = ' '.join(sorted({x[0] for x in cands})), ' '.join(sorted({ix.mods[x[1]] for x in cands}))
            else:
                # would the same rules find a project declaration if every file were visible?
                clo, R.clo = R.clo, None
                g, _ = R.resolve(tok, ns, opens)
                R.clo = clo
                cat = 'unresolved:outside_imports' if g else 'unresolved:no_project_decl'
                tgt = ' '.join(sorted({x[0] for x in g})[:3]); tm = ''
            if cat == 'resolved':
                cat2 = 'resolved:' + ('same_file' if cands[0][1] == R.me else 'import') + (':proj' if how == 'proj' else '')
            else:
                cat2 = cat
            cnt[cat2] += 1
            out_rows.append((mod, line, tok, cat2, tgt, tm, len(cands)))
    cnt['stat:ns_multi_level'] = R.stats['ns_multi_level']
    return cnt, len(R.clo)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    src, d = args[0], args[1]
    n = int(args[2]) if len(args) > 2 else 500
    seed = int(args[3]) if len(args) > 3 else 79
    t0 = time.time()
    ix = Index(d)
    t_index = time.time() - t0
    print(f"index loaded: {len(ix.decl):,} names, {len(ix.mods):,} modules in {t_index:.0f}s")
    depth = {}
    root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
    for ln in open(os.path.join(root, 'notes', 'tree', 'import_closure.tsv')):
        if ln.startswith('module\t'):
            continue
        a, b, _ = ln.split('\t', 2)
        depth[a] = int(b)
    chain = sorted((m for m, k in depth.items() if k <= 4), key=lambda m: (depth[m], m))
    rest = sorted(m for m in ix.imports if ix.mods[m] not in set(chain))
    rnd = random.Random(seed)
    sample = chain + sorted(ix.mods[m] for m in rnd.sample(rest, n - len(chain)))
    open(os.path.join(d, 'sample.txt'), 'w').write(
        f"# {len(chain)} modules within 4 imports of Main (depth from notes/tree/import_closure.tsv), "
        f"then {n - len(chain)} random modules, random.Random({seed}).sample\n" + '\n'.join(sample) + '\n')
    total = collections.Counter()
    per_file = []
    t1 = time.time()
    with gzip.open(os.path.join(d, 'occurrences.tsv.gz'), 'wt', encoding='utf-8') as fh:
        fh.write('module\tline\ttoken\tcategory\ttarget\ttarget_module\tn_candidates\n')
        for mod in sample:
            rows = []
            ts = time.time()
            c, nclo = process(src, ix, mod, rows)
            per_file.append({'module': mod, 'closure': nclo, 'seconds': round(time.time() - ts, 3), **c})
            total.update(c)
            fh.writelines('\t'.join(map(str, r)) + '\n' for r in rows)
    t_res = time.time() - t1
    json.dump({'n_files': len(sample), 'chain_files': len(chain), 'seed': seed, 'totals': dict(total),
               'seconds_index_load': round(t_index, 1), 'seconds_resolve': round(t_res, 1),
               'per_file': per_file}, open(os.path.join(d, 'summary.json'), 'w'), indent=1)
    print(f"resolved {len(sample)} files in {t_res:.0f}s")
    for k, v in sorted(total.items()):
        print(f"  {k:40s} {v:>9,}")


if __name__ == '__main__':
    main()
