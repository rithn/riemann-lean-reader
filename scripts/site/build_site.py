"""Write data/*.json for the static explorer site (github.com/rithn/rh-lean-explorer).

usage: uv run -q --with pyyaml --with networkx --with scipy python -I scripts/site/build_site.py <cluster dir> <out dir>
e.g.   ... build_site.py ../notes/cluster3 ../site

Reads only our own derived data (map.json, merged.tsv, import list, naming answers, tree YAML).
No Lean source text is copied: files appear by module name and path only.
"""
import os, re, sys, json, glob, shutil, datetime, collections
import yaml, networkx as nx

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.dirname(REPO)
D, OUT = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(OUT, 'data', 'c'), exist_ok=True)
for f in glob.glob(os.path.join(OUT, 'data', 'c', '*.json')):
    os.remove(f)
# front-end files (index.html, app.js, style.css) live in the explorer repo itself; only data/ is written

M = json.load(open(os.path.join(D, 'map.json')))
CL = {c['id']: c for c in M['clusters']}
TH = {t['id']: t for t in M['themes']}

# ---------- fields and tags: copies of research/content/fields.yaml and research/content/tags/cluster-tags.json, kept in
# data/ so the build does not depend on research/. A theme belongs to one of 9 fields; a cluster's field is its theme's.
# A cluster's era is the decade of the newest concept it needs, its level the highest level among those concepts.
FY = yaml.safe_load(open(os.path.join(REPO, 'data', 'fields.yaml')))
FIELDS = FY['fields']
FIDX = {f['id']: i for i, f in enumerate(FIELDS)}
TFIELD = {t: FY['themes'][t]['field'] for t in TH}
assert set(TFIELD.values()) <= set(FIDX), 'fields.yaml: a theme names an unknown field'
# short chip labels and the lightness each hue needs on the navy background (contrast 7.5:1 or more against #0b1230;
# indigo and violet need the most). The app reads both from overview.json 'fields'.
FIELD_SHORT = {'nt': 'Number theory', 'aut': 'Automorphic', 'theta': 'Theta & Siegel–Weil', 'lat': 'Lattices',
               'ht': 'Heights', 'av': 'Abelian varieties', 'padic': 'p-adic Hodge', 'ag': 'Algebraic geometry',
               'an': 'Harmonic analysis'}
FIELD_L = {'nt': 56, 'aut': 72, 'theta': 72, 'lat': 58, 'ht': 64, 'av': 76, 'padic': 58, 'ag': 82, 'an': 58}
def fcol(f):   # a field's colour, as the app draws it (col() in app.js with the field's lightness)
    return f'hsla({f["hue"]},80%,{FIELD_L[f["id"]]}%,1)'
CTAGS = json.load(open(os.path.join(REPO, 'data', 'cluster-tags.json')))
assert set(CTAGS) == set(CL), 'cluster-tags.json does not cover the clusters exactly'
ERAS = [('pre1900', 'before 1900'), ('1900-1949', '1900–1949'), ('1950s', '1950s'), ('1960s', '1960s'), ('1970s', '1970s'),
        ('1980s', '1980s'), ('1990s', '1990s'), ('2000s', '2000s'), ('2010s', '2010s'), ('2020s', '2020s')]
ERA_OF = {'before 1900': 0, '1900-1949': 1, **{e: i for i, (e, _) in enumerate(ERAS) if i > 1}}
LEVELS = [('school', 'School'), ('ug', 'Undergraduate'), ('grad', 'Graduate'), ('phd', 'PhD'), ('research', 'Research')]
LEVEL_OF = {n: i for i, (_, n) in enumerate(LEVELS)}
assert all(x['era'] in ERA_OF and x['level'] in LEVEL_OF for x in CTAGS.values()), 'cluster-tags.json: unknown era or level'
def ctag_line(k):   # 'Abelian varieties · 1960s · PhD level' (static cluster pages; the app writes its own)
    x = CTAGS[k]
    return ' · '.join([FIELDS[FIDX[TFIELD[CL[k]['theme']]]]['name'], ERAS[ERA_OF[x['era']]][1], f'{x["level"]} level']
                      + (['new in this proof'] if x['new_in_proof'] else []))

# ---------- names: newest run wins (sampled-fixed > full-data > first sampled)
NAMES = {}
for sub in ('naming-s10/out', 'naming/out-pilot', 'naming/out', 'naming-s10b/out'):
    for f in sorted(glob.glob(os.path.join(D, sub, 'bundle-*.yaml'))):
        try:
            for c in yaml.safe_load(open(f))['clusters']:
                if c.get('id') in CL and c.get('title'):
                    NAMES[c['id']] = c
        except Exception:
            pass

# ---------- aliases: the namers wrote topic tags and book titles freely, so merge spellings of the same thing
import unicodedata
def _fold(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
TAG_ALIAS = {
    'adeles-and-ideles': 'adeles', 'adeles-ideles': 'adeles', 'ideles-adeles': 'adeles',
    'adeles-and-restricted-products': 'adeles', 'adeles-local-global': 'adeles',
    'automorphic-forms-adelic': 'automorphic-forms', 'automorphic-forms-adeles': 'automorphic-forms',
    'howe-duality': 'theta-correspondence', 'theta-correspondence-howe-duality': 'theta-correspondence',
    'theta-correspondence-weil-representation': 'theta-correspondence',
    'weil-representation-theta-functions': 'weil-representation',
    'theta-functions-and-theta-lifts': 'theta-functions', 'theta-functions-theta-lifts': 'theta-functions',
    'local-langlands-correspondence': 'local-langlands', 'discrete-series-representations': 'discrete-series',
    'smooth-representations-padic-groups': 'smooth-representations-p-adic-groups',
    'abelian-varieties-basics': 'abelian-varieties', 'moduli-spaces-basics': 'moduli-spaces',
    'trace-formula-basics': 'trace-formula', 'formal-group-laws': 'formal-groups',
    'heights-arakelov': 'arakelov-heights', 'heights-and-arakelov-theory': 'arakelov-heights',
    'heights-diophantine-geometry': 'heights-diophantine', 'whittaker-functions': 'whittaker-models',
    'jacquet-module-parabolic-induction': 'parabolic-induction-jacquet-modules',
    'coherent-sheaves-cohomology': 'coherent-sheaf-cohomology', 'doubling-method-rallis': 'doubling-method',
    'hermitian-line-bundles-arakelov': 'hermitian-line-bundles', 'hermitian-line-bundles-arithmetic': 'hermitian-line-bundles',
    'multiprojective-space-segre': 'multi-projective-space', 'weil-pairing-torsion': 'weil-pairing',
    'fock-model-oscillator': 'fock-space-oscillator-representation', 'genus-mass-formula': 'hermitian-lattices-genus-mass',
}
_STOP = {'and', 'of', 'the', 'on', 'over', 'in', 'basics'}
def _tagkey(t):
    t = _fold(t).strip().replace('concept-', '').replace('padic', 'p-adic').replace('blow-ups', 'blowups')
    t = TAG_ALIAS.get(t, t)
    return t, ' '.join(sorted(w.rstrip('s') if len(w) > 3 else w for w in t.split('-') if w not in _STOP))
_tagc, _tagform = collections.Counter(), {}
for n in NAMES.values():
    for t in n.get('new_concepts') or []:
        t, key = _tagkey(t); _tagc[(key, t)] += 1
for (key, t), c in sorted(_tagc.items(), key=lambda z: -z[1]):
    _tagform.setdefault(key, t)                     # most used spelling wins
def _booktitle(s):
    s = re.sub(r'\([^)]*\)', '', s)
    parts = [p for p in re.split(r'[,;:]', s) if p.strip()]
    authors = re.split(r'\band\b|[-,]', _fold(parts[0]))[0].split() if parts else ['']
    sur = authors[-1] if authors else ''
    title = re.sub(r'[^a-z0-9]+', ' ', _fold(parts[-1])).strip() if len(parts) > 1 else ''
    return (sur, title)
_bookc = collections.Counter(n['source']['title'].strip() for n in NAMES.values()
                             if isinstance(n.get('source'), dict) and n['source'].get('title'))
_bookform = {}
for b, c in sorted(_bookc.items(), key=lambda z: (-z[1], -len(z[0]))):
    _bookform.setdefault(_booktitle(b), b)
for n in NAMES.values():
    if n.get('new_concepts'):
        seen = []
        for t in n['new_concepts']:
            f = _tagform[_tagkey(t)[1]]
            if f not in seen and f not in (n.get('concepts') or []) and 'concept-' + f not in (n.get('concepts') or []):
                seen.append(f)
        n['new_concepts'] = seen
    s = n.get('source')
    if isinstance(s, dict) and s.get('title'):
        s['title'] = _bookform[_booktitle(s['title'].strip())]
print(f'aliases: {len(_tagc)} tag spellings -> {len(set(_tagform.values()))}; '
      f'{len(_bookc)} book spellings -> {len(set(_bookform.values()))}')
# the namers saw only statements, so many descriptions end by hedging about proofs; the joint statement by the Lean and
# Mathlib communities has since certified the proof (21 Nov 2026), so drop those sentences (or the hedging clause)
PROOFW = re.compile(r"(?i)\b(proofs?|proved|prove|correct(ness)?|checked|confirm|judge[ds]?)\b")
HEDGE = re.compile(r"(?i)\bI (cannot|can't|can not|could not|only|see)\b|only statements|statements only|statements? (are|is|were) (seen|visible)|visible statements|not visible|unseen|unknown|not assessed|nothing (here )?is (shown|checked)|no proofs? (is |are )?(visible|confirmed|judged)|not proofs|only see the claims")
STMT_ONLY = re.compile(r"(?i)^(I (only )?see (only )?statements( only)?|only statements (are|were) (visible|seen)|statements only are visible)[^.]*\.$")
CLAUSE = re.compile(r"(?i)^(.{12,}?)(?:\s*[,;]\s*(?:though|but|and|so)?\s*|\s+and\s+)(?=I\b|uses only statements|only statements|no proofs?|the actual proofs|proofs? |whose proofs)")
VIS = re.compile(r"(?i)only statements (are |were )?(visible|shown|seen)|uses only statements visible|only statements are shown|because only statements")
def is_hedge(s):
    return bool(VIS.search(s) or STMT_ONLY.match(s) or (HEDGE.search(s) and PROOFW.search(s)) or re.match(r"(?i)^only statements", s))
def dehedge(text):
    out = []
    for s in re.split(r'(?<=[.!?])\s+', (text or '').strip()):
        if not s: continue
        if is_hedge(s):
            m = CLAUSE.match(s)
            if m and not is_hedge(m.group(1)) and not HEDGE.search(m.group(1)):
                out.append(m.group(1).rstrip(' ,;') + '.')
            continue
        out.append(s)
    return ' '.join(out)
# the namers also left notes about their own confidence ("so confidence is low", "; low confidence from folders only.");
# they are internal and were showing up in search snippets, so drop them from every blurb and description
CONF_TAIL = re.compile(r'(?i)\s*[;,:—–-]\s*(?:with\s+)?(?:low|medium|high|moderate)[- ]confidence\b[^.]*\.?\s*$')
def deconf(text):
    if not text:
        return text
    text = CONF_TAIL.sub('.', text.strip())
    return ' '.join(x for x in re.split(r'(?<=[.!?])\s+', text) if not re.search(r'(?i)confidence', x)).strip()
for c in NAMES.values():
    if c.get('plain'):
        c['plain'] = deconf(dehedge(c['plain']))
HINTS = json.load(open(os.path.join(D, 'hints.json'))) if os.path.exists(os.path.join(D, 'hints.json')) else {}

# ---------- tree (core proof outline + concepts + mapped file nodes)
core = yaml.safe_load(open(os.path.join(REPO, 'tree.yaml')))
concepts = yaml.safe_load(open(os.path.join(REPO, 'tree', 'concepts.yaml')))['nodes']
filenodes = [n for f in sorted(glob.glob(os.path.join(REPO, 'tree', 'nodes', '*.yaml')))
             for n in yaml.safe_load(open(f))['nodes']]
CONC = {n['id']: n for n in core['nodes'] + concepts}

# ---------- module -> unit -> cluster
unit_cl = {f: c['id'] for c in M['clusters'] for f in c['files']}
parent, kind = {}, {}
for line in open(os.path.join(D, 'merged.tsv')):
    a, b, k = (line.rstrip('\n').split('\t') + ['', ''])[:3]
    parent[a], kind[a] = (None if b == '-' else b), (k or 'merged')
def unit_of(m, depth=0):
    if m in unit_cl:
        return m
    p = parent.get(m)
    return unit_of(p, depth + 1) if p and depth < 20 else None
mod_cl = {}
for m in list(unit_cl) + list(parent):
    u = unit_of(m)
    if u:
        mod_cl[m] = unit_cl[u]

imports, importers = {}, collections.defaultdict(list)
for line in open(os.path.join(ROOT, 'notes', 'tree', 'import_closure.tsv')):
    if line.startswith('module\t'):
        continue
    p = line.rstrip('\n').split('\t')
    imports[p[0]] = [x for x in (p[2].split() if len(p) > 2 else [])]
    for x in imports[p[0]]:
        importers[x].append(p[0])

TOTAL_FILES = len(imports)   # every .lean file in the archive (175,187); mod_cl holds the mapped ones (175,027)
# lines of Lean in the whole archive (all 175,187 files), from the file index: 17,374,215
TOTAL_LINES = sum(int(l.split('\t')[1]) for l in list(open(os.path.join(ROOT, 'notes', 'file_index.tsv')))[1:])
LINES_TXT = f'about {TOTAL_LINES / 1e6:.1f} million lines'
UNMAPPED_TXT = (f'The other {TOTAL_FILES - len(mod_cl):,} files are in the archive but not on the map, because none has a statement '
                '(a theorem or definition) of its own: 96 are import-only files that just list other files, 5 are build helpers '
                '(<code>BuildAid.D1</code>–<code>D5</code>), and 59 had no statements our extraction could read.')
LICENSE = 'https://creativecommons.org/licenses/by/4.0/'
LICENSE_TXT = ("The site's own data (cluster and theme names, descriptions, the map layout and the JSON files) is licensed under "
               f'<a href="{LICENSE}">CC BY 4.0</a>; the Lean source keeps its own licence.')

# ---------- proof status: the ONE canonical wording (plan item 36). Every status line comes from here: page footers and
# meta descriptions (short form), About, /api/status.json, llms.txt and llms-full.txt (long form), and the app, which reads
# overview.json 'status' (home lede, about(), source card). Facts and quotes: research/content/fact-sheet.md, VERIFIED lines
# only. When a sentence changes, move STATUS_AS_OF and add a changelog entry. Write HTML; plain() and mdtext() derive the rest.
import html as _html
STATUS_AS_OF = '2026-11-22'
AS_OF_TXT = datetime.date.fromisoformat(STATUS_AS_OF).strftime('%-d %b %Y')
STMT = 'https://leanprover-community.github.io/blog/posts/riemann-hypothesis/'
NOTE, DREW = 'https://alpo.ge/remark.pdf', 'https://math.mit.edu/~drew/grh/'
MATHLIB_RH = 'https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis'
LEAN_REPO = 'https://github.com/leanprover-community/riemann-hypothesis'
LEAN_SHA = '40e56bab026552e089d7afcfeff08d2defb9c005'   # unchanged mirror of the 175,187-file archive; app.js GH_SHA must match
def plain(h):
    return _html.unescape(re.sub(r'<[^>]+>', '', h))
def mdtext(h):   # links and code only, which is all the status HTML uses
    h = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', h)
    return _html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'</?code>', '`', h)))
# short form: footers, meta, the app's home lede
ST_CERT = (f'On 21 Nov 2026 a <a href="{STMT}">joint statement</a> by the Lean and Mathlib communities, endorsed by the '
           'Lean FRO and the Mathlib Initiative, certified the Lean statement and proof.')
ST_MORE = f'More independent checks: <a href="{DREW}">math.mit.edu/~drew/grh</a>.'
ST_SHORT = f'{ST_CERT} {ST_MORE}'
ST_META = plain(ST_CERT)
ST_CHIP = 'certified 21 Nov'   # header chip label; its tooltip is ST_META
# long form: About, /api/status.json, llms.txt, llms-full.txt
ST_RELEASE = (f'On 20 Nov 2026 Levent Alpöge released a proof of the Riemann hypothesis, and of the generalized Riemann hypothesis '
              f'(GRH) for Dirichlet L-functions, as a Lean library of {TOTAL_FILES:,} Lean files, {LINES_TXT}, with a note at '
              f'<a href="{NOTE}">alpo.ge</a>.')
ST_QUOTE = 'In its words: “We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct.”'
ST_CHECKS = [   # the joint statement's four criteria, in its order, worded as on /status/ (data/pages/status.md)
    f'The formal statement is the Riemann hypothesis as Mathlib states it: <a href="{MATHLIB_RH}"><code>RiemannHypothesis</code></a>.',
    'The library compiles without errors, and dozens of people reproduced the same proof export.',
    'Two independent tools confirmed that the theorem proved is exactly Mathlib\'s statement.',
    'Several independent proof checkers accepted the exported proof.']
ST_VERIFIED = (f'All {TOTAL_FILES:,} modules compile with zero errors. Every module has been replayed through Lean\'s kernel, and the '
               'exported proof has been accepted by nanoda, con-leche and con-ron. lean4lean accepts every module. A sandboxed rebuild '
               'on a separate machine produced an export identical to the published one.')
ST_ONGOING = (f'Andrew Sutherland\'s verification page at MIT keeps the full, live list of independent checks: '
              f'<a href="{DREW}">math.mit.edu/~drew/grh</a>.')
ST_SCOPE = ('The proof covers Mathlib\'s <code>RiemannHypothesis</code> and GRH for Dirichlet L-functions, all moduli and characters. '
            'The theorems are stated without hypotheses.')
ST_ARCHIVE = (f'The source viewer shows the original archive as released: commit <code>{LEAN_SHA[:8]}</code> of the '
              f'<a href="{LEAN_REPO}">community mirror</a>, an unchanged copy of the {TOTAL_FILES:,}-file archive. The community '
              'repository has since removed 10,724 files in cleanup pull requests, leaving 164,464 .lean files including a new Challenge.lean.')
ST_ARCHIVE_SHORT = 'This is the original archive as released; the community repository has since removed 10,724 files in cleanup pull requests.'
RUBINSTEIN = 'https://mrubinst.github.io/grh-lean-verification/'
ST_SOURCES = [('Joint statement by the Lean and Mathlib communities (21 Nov 2026)', STMT),
              ("Levent Alpöge's note (20 Nov 2026)", NOTE),
              ("Andrew Sutherland's verification page, MIT", DREW),
              ("Michael Rubinstein's check, Waterloo", RUBINSTEIN),
              ("Mathlib's RiemannHypothesis", MATHLIB_RH),
              (f'The Lean source as released (community mirror, commit {LEAN_SHA[:8]})', f'{LEAN_REPO}/tree/{LEAN_SHA}')]
ST_LONG = (f'<p class="lede">{ST_RELEASE} {ST_CERT} {ST_QUOTE}</p><p class="meta">Status as of {AS_OF_TXT}. '
           '<a href="/status/">Full status page</a>.</p>'
           f'<h2>How the Lean proof was checked</h2><p>{ST_VERIFIED}</p><p>The joint statement certifies four criteria:</p><ol>'
           + ''.join(f'<li>{x}</li>' for x in ST_CHECKS) + f'</ol><p>{ST_ONGOING}</p>'
           f'<h2>What was proved</h2><p>{ST_SCOPE}</p>'
           '<h2>Primary sources</h2><ul>' + ''.join(f'<li><a href="{u}">{_html.escape(t)}</a></li>' for t, u in ST_SOURCES) + '</ul>')
STATUS_BLOCK = {'as_of': STATUS_AS_OF, 'short': ST_SHORT, 'cert': ST_CERT, 'meta': ST_META, 'chip': ST_CHIP, 'long': ST_LONG,
                'archive': ST_ARCHIVE, 'archive_short': ST_ARCHIVE_SHORT, 'source_sha': LEAN_SHA, 'page': '/status/'}

def lean_path(m):
    return m.replace('.', '/') + '.lean'

# mapped file nodes -> module
NODE_OF = collections.defaultdict(list)
for n in filenodes + core['nodes']:
    for ref in n.get('lean') or []:
        m = ref.split(':')[0]
        if m.endswith('.lean'):
            NODE_OF[m[:-5].replace('/', '.')].append(n)

# ---------- cluster graph, distance from the main theorem
uses = {k: list(c.get('uses') or []) for k, c in CL.items()}
used_by = collections.defaultdict(list)
for k, us in uses.items():
    for u in us:
        used_by[u].append(k)
main = mod_cl.get('Main')
dist, par = {main: 0}, {main: None}   # par: the BFS parent, the same tree the app draws (PARENT in app.js)
q = collections.deque([main])
while q:
    k = q.popleft()
    for u in uses[k]:
        if u not in dist:
            dist[u] = dist[k] + 1; par[u] = k; q.append(u)
def uproute(k):   # [k, …, main]: the route read upward, from the cluster to the main theorem
    r = []
    while k is not None and k in par:
        r.append(k); k = par[k]
    return r
nroutes = {main: 1}   # shortest routes from the main theorem's cluster (BFS order: parents are counted first)
for k in sorted(dist, key=dist.get):
    for u in uses[k]:
        if dist.get(u) == dist[k] + 1:
            nroutes[u] = nroutes.get(u, 0) + nroutes[k]
def reach(k, nbr):
    seen, q = {k}, [k]
    while q:
        for x in nbr[q.pop()]:
            if x not in seen:
                seen.add(x); q.append(x)
    return len(seen) - 1
builds = {main: reach(main, uses)}                    # for the main theorem: everything it rests on
# feeds[k]: clusters whose files import a file of k, directly or through other files. Counted on the file graph, which
# has no loops; on the cluster graph (which has loops) almost every cluster reaches almost every other one.
_cbit = {k: 1 << i for i, k in enumerate(CL)}
_imp_by = collections.defaultdict(list)
for m, xs in imports.items():
    for x in xs:
        if x in imports:
            _imp_by[x].append(m)
_left = {m: len(_imp_by[m]) for m in imports}
_todo = collections.deque(m for m, n in _left.items() if n == 0)
_up = {}                                              # file -> bitset of clusters that depend on it
while _todo:
    m = _todo.popleft()
    b = 0
    for i in _imp_by[m]:
        b |= _up[i] | _cbit.get(mod_cl.get(i), 0)
    _up[m] = b
    for x in imports[m]:
        if x in _left:
            _left[x] -= 1
            if _left[x] == 0:
                _todo.append(x)
assert len(_up) == len(imports), 'file graph has a loop'
_feedbits = collections.defaultdict(int)
for m, k in mod_cl.items():
    _feedbits[k] |= _up.get(m, 0)
feeds = {k: bin(_feedbits[k] & ~_cbit[k]).count('1') for k in CL}
del _up
# file level: import steps from the module Main (the file graph has no loops)
fdist = {'Main': 0}
_q = collections.deque(['Main'])
while _q:
    m = _q.popleft()
    for x in imports.get(m, []):
        if x in imports and x not in fdist:
            fdist[x] = fdist[m] + 1; _q.append(x)
_chain = {}
for m in sorted(imports, key=lambda m: -fdist.get(m, 0)):   # longest import chain, in files (memoised DFS)
    st = [m]
    while st:
        x = st[-1]
        if x in _chain:
            st.pop(); continue
        todo = [y for y in imports.get(x, []) if y in imports and y not in _chain]
        if todo:
            st += todo
        else:
            _chain[x] = 1 + max((_chain[y] for y in imports.get(x, []) if y in imports), default=0); st.pop()
import statistics
FSTATS = {'median': int(statistics.median(fdist.values())), 'max': max(fdist.values()), 'chain': max(_chain.values()),
          'reached': len(fdist)}
print('file routes:', FSTATS)
core_cl = collections.defaultdict(list)
for n in core['nodes']:
    for ref in n.get('lean') or []:
        m = ref.split(':')[0][:-5].replace('/', '.')
        if m in mod_cl:
            core_cl[mod_cl[m]].append(n['id'])

# ---------- labels
def split_camel(s):
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', s)
def folder_label(folders):
    if not folders:
        return 'Unnamed group'
    parts = folders[0][0].split('.')
    return ': '.join(split_camel(p) for p in parts[-2:])
# folders that show up in many themes (flat dump folders like Proofs.DivisorProofs) make poor names
_fcount = collections.Counter(f[0] for t in TH.values() for f in t['folders'][:3])
GENERIC = {'statement', 'proof', 'proofs', 'groundtheory', 'ground', 'development', 'formalism', 'theory', 'of',
           'maxsynthpendingdepth', 'pending', 'depth', 'synth', 'statements', 'aux', 'lemma', 'def'}
def theme_name(t):
    fs = [f[0] for f in t['folders'] if _fcount[f[0]] < 4] or [t['folders'][0][0]]
    leafs = []
    for f in fs[:2]:
        leaf = split_camel(f.split('.')[-1])
        if leaf not in leafs:
            leafs.append(leaf)
    name = ' & '.join(leafs[:2])
    titles = [NAMES[k]['title'] for k in t['clusters'] if k in NAMES]
    return name, len(titles)

# ---------- layout: themes, then clusters inside each theme
TG = nx.Graph()
TG.add_nodes_from(TH)
w = collections.Counter()
for k, us in uses.items():
    for u in us:
        a, b = CL[k]['theme'], CL[u]['theme']
        if a != b:
            w[tuple(sorted((a, b)))] += 1
for (a, b), x in w.items():
    TG.add_edge(a, b, weight=x)
size = {t: sum(len(CL[k]['files']) for k in TH[t]['clusters']) for t in TH}
pos_t = nx.spring_layout(TG, weight='weight', seed=7, k=1.6 / len(TH) ** 0.5, iterations=300)
R = {t: 0.6 * (len(TH[t]['clusters']) ** 0.5) for t in TH}
# spread themes so circles of radius R do not overlap much (simple repulsion passes)
P = {t: [pos_t[t][0] * 40, pos_t[t][1] * 40] for t in TH}
for _ in range(400):
    moved = False
    ts = list(TH)
    for i, a in enumerate(ts):
        for b in ts[i + 1:]:
            dx, dy = P[b][0] - P[a][0], P[b][1] - P[a][1]
            d = (dx * dx + dy * dy) ** 0.5 or 1e-3
            need = R[a] + R[b] + 1.2
            if d < need:
                s = (need - d) / 2 / d
                P[a][0] -= dx * s; P[a][1] -= dy * s; P[b][0] += dx * s; P[b][1] += dy * s; moved = True
    if not moved:
        break
pos_c = {}
for t, th in TH.items():
    G = nx.Graph(); G.add_nodes_from(th['clusters'])
    for k in th['clusters']:
        for u in uses[k]:
            if CL[u]['theme'] == t:
                G.add_edge(k, u)
    lp = nx.spring_layout(G, seed=3, iterations=100) if len(G) > 1 else {th['clusters'][0]: (0, 0)}
    for k, (x, y) in lp.items():
        pos_c[k] = (P[t][0] + x * R[t], P[t][1] + y * R[t])

r2 = lambda v: round(v, 2)
def slug(s, n=60):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:n].rsplit('-', 1)[0] if len(s) > n else s
TNAME = {t: theme_name(th)[0] for t, th in TH.items()}
TN_FILE = os.path.join(D, 'theme-naming', 'theme_names.yaml')
TNAMED = {x['id']: x for x in yaml.safe_load(open(TN_FILE))['themes']} if os.path.exists(TN_FILE) else {}
for x in TNAMED.values():
    if x.get('blurb'):
        x['blurb'] = deconf(x['blurb'])
_dup = collections.Counter(TNAME.values())
for t in TH:
    if t in TNAMED:
        TNAME[t] = TNAMED[t]['name']
    elif _dup[TNAME[t]] > 1:
        TNAME[t] += ' (' + ', '.join(w for w in TH[t]['words'] if w not in GENERIC)[:2 * 14].rsplit(',', 1)[0] + ')'
named = len(NAMES)
# static page paths; every cluster gets one (named clusters by title, any unnamed one by folder label)
TSLUG = {t: slug(TNAME[t]) for t in TH}
CSLUG = {k: slug(NAMES[k]['title'] if k in NAMES else folder_label(CL[k]['folders'])) for k in CL}
TPATH = {t: f'/theme/{t}-{TSLUG[t]}/' for t in TH}
CPATH = {k: f'/cluster/{k}-{CSLUG[k]}/' for k in CL}
# every slug a theme has ever had (scripts/site/theme_slugs_history.json: id -> [slug, ...], oldest first); a renamed
# theme keeps its old slugs here, and _redirects 301s each old /theme/<id>-<old>/ straight to the current path
TSLUG_F = os.path.join(HERE, 'theme_slugs_history.json')
TSLUG_HIST = json.load(open(TSLUG_F)) if os.path.exists(TSLUG_F) else {}
for t in TH:
    if TSLUG[t] not in TSLUG_HIST.setdefault(t, []):
        TSLUG_HIST[t].append(TSLUG[t])
json.dump(dict(sorted(TSLUG_HIST.items())), open(TSLUG_F, 'w'), indent=1)
TOLD = {f'/theme/{t}-{s}/': TPATH[t] for t, ss in TSLUG_HIST.items() if t in TPATH for s in ss if s != TSLUG[t]}
assert not set(TOLD) & set(TPATH.values()), 'an old theme path is also a current one'
# overview.json is what the map needs for first paint. Field notes: 's' is the URL slug (page = /cluster/<id>-<s>/,
# /theme/<id>-<s>/); 'uses' are cluster numbers (k0677 -> 677; the app turns them back into ids); search words
# ('w') and folder labels ('fl', kept here only for unnamed clusters) live in words.json, loaded after first paint. Dropped as unused by the app: conf, coh, lines, core.
overview = {
    'updated': datetime.date.today().isoformat(),
    'counts': {'clusters': len(CL), 'themes': len(TH), 'named': named,
               'files': len(mod_cl), 'total': TOTAL_FILES, 'units': len(unit_cl), 'lines': TOTAL_LINES},
    'main': main, 'builds': builds[main], 'status': STATUS_BLOCK, 'fstats': FSTATS,
    'themes': [{'id': t, 'name': TNAME[t], 'blurb': TNAMED.get(t, {}).get('blurb'), 'conf': TNAMED.get(t, {}).get('confidence'),
                'fl': theme_name(th)[0], 'n': len(th['clusters']), 's': TSLUG[t],
                'units': size[t], 'words': th['words'][:8], 'x': r2(P[t][0]), 'y': r2(P[t][1]), 'r': r2(R[t])}
               for t, th in TH.items()],
    'tedges': [[a, b, x] for (a, b), x in w.items()],
    'clusters': [],
    # fields: the map's default colours and a filter (themes carry 'f', the field's index). 'l' is the lightness the hue
    # needs on the navy background. Era and level per cluster are one digit each, in the order of 'clusters' (an index
    # into 'eras' / 'levels'); 'new' lists the clusters (as numbers) that rest on the proof's own constructions.
    'fields': [{'id': f['id'], 'name': f['name'], 'short': FIELD_SHORT[f['id']], 'hue': f['hue'], 'l': FIELD_L[f['id']],
                'description': f['description']} for f in FIELDS],
    'eras': [{'id': i, 'name': n} for i, n in ERAS],
    'levels': [{'id': i, 'name': n} for i, n in LEVELS],
    'tags': {'era': ''.join(str(ERA_OF[CTAGS[k]['era']]) for k in CL), 'level': ''.join(str(LEVEL_OF[CTAGS[k]['level']]) for k in CL),
             'new': [int(k[1:]) for k in CL if CTAGS[k]['new_in_proof']]},
}
for o in overview['themes']:
    o['f'] = FIDX[TFIELD[o['id']]]
for k, c in CL.items():
    n = NAMES.get(k, {})
    overview['clusters'].append({
        'id': k, 't': c['theme'], 'title': n.get('title'), 's': CSLUG[k],
        **({} if n.get('title') else {'fl': folder_label(c['folders'])}),
        'n': len(c['files']), 'uses': [int(u[1:]) for u in uses[k]], 'd': dist.get(k), 'fi': feeds[k],
        **({'r': min(nroutes[k], 100)} if nroutes.get(k, 1) > 1 else {}),
        'x': r2(pos_c[k][0]), 'y': r2(pos_c[k][1]),
    })
WORDS = {'w': {k: c['words'][:6] for k, c in CL.items()}, 'fl': {k: folder_label(c['folders']) for k in CL}}

# ---------- per-cluster detail
members = collections.defaultdict(list)
for m, k in mod_cl.items():
    members[k].append(m)
fcount = collections.Counter(mod_cl.values())
for o in overview['clusters']:
    o['files'] = fcount[o['id']]
for o in overview['themes']:   # 'files' = Lean files (sums to the mapped total); 'units' = units after folding (sums to 63,892)
    o['files'] = sum(fcount[k] for k in TH[o['id']]['clusters'])
for k, c in CL.items():
    n = NAMES.get(k, {})
    files = []
    for m in sorted(members[k], key=lambda m: (m not in unit_cl, m)):
        imp = imports.get(m, [])
        ext = sorted({mod_cl[x] for x in imp if x in mod_cl and mod_cl[x] != k})
        files.append({
            'm': m, 'k': 'unit' if m in unit_cl else kind.get(m, 'merged'), 'dm': fdist.get(m),
            'imp': imp, 'by': len(importers.get(m, [])), 'ext': ext,
            'node': [{'id': x['id'], 'title': x['title'], 'plain': dehedge(x.get('plain', '')), 'status': x.get('status'),
                      'guess': bool(x.get('guess'))} for x in NODE_OF.get(m, [])][:2] or None,
        })
    conc = []
    for cid in (n.get('concepts') or []) + [x for x in c.get('concepts') or [] if x not in (n.get('concepts') or [])]:
        x = CONC.get(cid)
        conc.append({'id': cid, 'title': x['title'] if x else cid.replace('concept-', '').replace('-', ' '),
                     'known': bool(x)})
    detail = {
        'id': k, 'theme': c['theme'], 'title': n.get('title'), 'plain': n.get('plain'),
        'fl': folder_label(c['folders']), 'folders': c['folders'], 'words': c['words'],
        'coherent': n.get('coherent'), 'confidence': n.get('confidence'),
        'concepts': conc, 'new_concepts': n.get('new_concepts') or [],
        'source': n.get('source') if isinstance(n.get('source'), dict) else None,
        'hints': HINTS.get(k, []), 'uses': uses[k], 'used_by': sorted(used_by[k]),
        'dist': dist.get(k), 'core': core_cl.get(k, []), 'lines': c['lines'], 'files': files,
    }
    json.dump(detail, open(os.path.join(OUT, 'data', 'c', k + '.json'), 'w'), separators=(',', ':'))

# ---------- search index: folders + leaf names
folders, fidx, rows = [], {}, []
for m, k in mod_cl.items():
    a, _, b = m.rpartition('.')
    if a not in fidx:
        fidx[a] = len(folders); folders.append(a)
    rows.append([fidx[a], b, int(k[1:])])
json.dump({'folders': folders, 'rows': rows}, open(os.path.join(OUT, 'data', 'modules.json'), 'w'), separators=(',', ':'))

# ---------- learning tree (core outline + concepts), with cluster links
def tnode(x):
    cls = sorted({mod_cl[r.split(':')[0][:-5].replace('/', '.')] for r in x.get('lean') or []
                  if r.split(':')[0][:-5].replace('/', '.') in mod_cl})
    return {'id': x['id'], 'title': x['title'], 'kind': x['kind'], 'status': x.get('status'),
            'plain': x.get('plain', ''), 'needs': x.get('needs') or [], 'learn': x.get('learn') or [],
            'lean': x.get('lean') or [], 'clusters': cls, 'guess': bool(x.get('guess'))}
used_concepts = collections.defaultdict(list)
for k, c in CL.items():
    for cid in dict.fromkeys((NAMES.get(k, {}).get('concepts') or []) + (c.get('concepts') or [])):
        used_concepts[cid].append(k)
json.dump({'roots': core['roots'], 'nodes': [tnode(x) for x in core['nodes'] + concepts],
           'concept_clusters': used_concepts},
          open(os.path.join(OUT, 'data', 'tree.json'), 'w'), separators=(',', ':'))
json.dump(overview, open(os.path.join(OUT, 'data', 'overview.json'), 'w'), separators=(',', ':'))
json.dump(WORDS, open(os.path.join(OUT, 'data', 'words.json'), 'w'), separators=(',', ':'))
print(f'{len(CL)} clusters ({named} named), {len(TH)} themes, {len(mod_cl)} files -> {OUT}')


# ---------- static pages for search engines, sharing and machines
# index.html is the template: <!--head-->…<!--/head--> and <!--prerender-->…<!--/prerender--> are replaced, and the
# asset URLs get content hashes (?v=…) so _headers can cache /data/*, /app.js and /style.css as immutable.
# Every page also gets a Markdown copy next to it (<path>index.md, linked with rel=alternate type=text/markdown).
# Rebuild after editing app.js or style.css: the hashes in the HTML are what bust the long cache.
import html, hashlib, secrets, email.utils
from html.parser import HTMLParser
SITE = 'https://riemannhypothesissolved.com'
TPL = open(os.path.join(OUT, 'index.html')).read()
H = html.escape
today = datetime.date.today().isoformat()
GH = 'https://github.com/rithn/riemann-lean-reader'
X_SITE, X_FEEDBACK = 'https://x.com/RiemannMap', 'https://x.com/SomTheBuilder'
FILES_TXT = f'{TOTAL_FILES:,} Lean files ({len(mod_cl):,} mapped)'
SITE_NAME = 'RH Lean Explorer'

# ---------- content versions
def hfiles(paths):
    h = hashlib.sha256()
    for f in paths:
        h.update(os.path.relpath(f, OUT).encode()); h.update(open(f, 'rb').read())
    return h.hexdigest()[:10]
DATA_V = hfiles(sorted(glob.glob(os.path.join(OUT, 'data', '*.json')) + glob.glob(os.path.join(OUT, 'data', 'c', '*.json'))))
APP_V, CSS_V = hfiles([os.path.join(OUT, 'app.js')]), hfiles([os.path.join(OUT, 'style.css')])
TPL = re.sub(r'<link rel="stylesheet" href="/style\.css[^"]*">', f'<link rel="stylesheet" href="/style.css?v={CSS_V}">', TPL, count=1)
TPL = re.sub(r'<script src="/app\.js[^"]*"[^>]*></script>', f'<script src="/app.js?v={APP_V}" data-v="{DATA_V}"></script>', TPL, count=1)
TPL = re.sub(r'Charting [\d,]+ Lean files…', f'Charting {TOTAL_FILES:,} Lean files…', TPL)
TPL = re.sub(r'<a class="status-chip ok" href="/(?:about|status)/" title="[^"]*">\s*<i></i><span>Lean proof · <b>[^<]*</b></span>',
             f'<a class="status-chip ok" href="/status/" title="{H(ST_META)} How it was checked.">\n    <i></i><span>Lean proof · <b>{ST_CHIP}</b></span>', TPL, count=1)
assert ST_META in html.unescape(TPL), 'status chip not found in the index.html template'
assert f"GH_SHA = '{LEAN_SHA}'" in open(os.path.join(OUT, 'app.js')).read(), 'app.js GH_SHA differs from LEAN_SHA'
assert f'data-v="{DATA_V}"' in TPL and f'style.css?v={CSS_V}' in TPL

# ---------- lastmod: a page's date changes only when its title, description or body changes
# (state kept in scripts/site/lastmod.json: path -> [content hash, date]); '{{UPDATED}}' in a page becomes that date
STATE_F = os.path.join(HERE, 'lastmod.json')
STATE = json.load(open(STATE_F)) if os.path.exists(STATE_F) else {}
NEW_STATE = {}
def lastmod(key, *parts):
    h = hashlib.sha256('\x00'.join(parts).encode()).hexdigest()[:12]
    old = STATE.get(key)
    NEW_STATE[key] = [h, old[1] if old and old[0] == h else today]
    return NEW_STATE[key][1]
DATA_DATE = lastmod('data:', DATA_V)

# ---------- hreflang. Translated pages (/ja/, /tr/) do not exist yet, so this is a no-op today. To add one, register
# the group on every member path, e.g. g = {'en': '/about/', 'ja': '/ja/about/', 'tr': '/tr/about/'};
# ALTERNATES.update({p: g for p in g.values()}). head() then emits <link rel="alternate" hreflang="…"> for each
# language plus hreflang="x-default" (the 'en' page). The sitemap could carry the same links later (xhtml:link).
ALTERNATES = {}
def alt_links(path):
    a = ALTERNATES.get(path)
    if not a:
        return ''
    return (''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{p}">\n' for l, p in sorted(a.items()))
            + f'<link rel="alternate" hreflang="x-default" href="{SITE}{a.get("en", path)}">\n')

# ---------- JSON-LD
def ld(obj):  # JSON-LD block; '</' escaped so text cannot close the script tag
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', **obj}, ensure_ascii=False).replace('</', '<\\/') + '</script>\n'
ORG_ID, SITE_ID = SITE + '/#org', SITE + '/#website'
ORG = {'@type': 'Organization', '@id': ORG_ID, 'name': SITE_NAME, 'url': SITE + '/', 'logo': SITE + '/logo.png', 'sameAs': [X_SITE]}
RH_THING = {'@type': 'Thing', 'name': 'Riemann hypothesis', 'sameAs': 'https://en.wikipedia.org/wiki/Riemann_hypothesis'}
def crumbs_ld(*items):  # (name, path) pairs, home first
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + p} for i, (n, p) in enumerate(items)]}
def article_ld(path, headline, desc, published):
    return {'@type': 'Article', '@id': SITE + path + '#article', 'headline': headline, 'description': desc,
            'url': SITE + path, 'mainEntityOfPage': SITE + path, 'inLanguage': 'en',
            'datePublished': published + 'T00:00:00Z', 'dateModified': '{{UPDATED}}T00:00:00Z', 'author': {'@id': ORG_ID},
            'publisher': {'@id': ORG_ID}, 'about': RH_THING, 'isPartOf': {'@id': SITE_ID}, 'image': SITE + '/og.png?v=2'}
def faq_ld(pairs):
    """FAQPage for (question, answer) pairs; answers may hold simple HTML (links, lists).
    Only use it on a page that visibly shows exactly these questions and answers (Google's rule). Used by /faq/."""
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in pairs]}

# ---------- Markdown copies: a small HTML -> Markdown converter for the markup these pages use
class _MD(HTMLParser):
    BLOCK = {'p', 'div', 'h1', 'h2', 'h3', 'li', 'ul', 'ol', 'details', 'summary', 'footer', 'nav'}
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.lines, s.buf, s.depth, s.bullet, s.prefix, s.links, s.skip = [], '', 0, False, '', [], 0
    def flush(s):
        t = ' '.join(s.buf.split()); s.buf = ''
        if not t:
            return
        ind = '  ' * max(0, s.depth - 1)
        if s.bullet:
            s.lines.append(ind + '- ' + t); s.bullet = False
        elif s.depth:
            s.lines.append(ind + '  ' + t)
        else:
            s.lines += [s.prefix + t, '']
        s.prefix = ''
    def handle_starttag(s, tag, a):
        a = dict(a)
        if tag in ('script', 'style', 'svg'):
            s.skip += 1
        if tag in s.BLOCK:
            s.flush()
        if tag in ('ul', 'ol'):
            s.depth += 1
        elif tag == 'li':
            s.bullet = True
        elif tag in ('h1', 'h2', 'h3'):
            s.prefix = '#' * int(tag[1]) + ' '
            if s.lines and s.lines[-1] != '':
                s.lines.append('')
        elif tag == 'a':
            href = a.get('href') or ''
            s.links.append([SITE + href if href.startswith('/') else href, False]); s.buf += '['
        elif tag in ('b', 'strong'):
            s.buf += '**'
        elif tag in ('em', 'i'):
            s.buf += '*'
        elif tag == 'code':
            s.buf += '`'
        elif tag == 'small':   # a link's subtitle goes after the link: [Title](url) — subtitle
            if s.links and not s.links[-1][1]:
                s.buf = s.buf.rstrip() + f']({s.links[-1][0]})'; s.links[-1][1] = True
            s.buf += ' — '
        elif tag == 'br':
            s.flush()
    def handle_endtag(s, tag):
        if tag in ('script', 'style', 'svg'):
            s.skip -= 1
        if tag == 'a' and s.links:
            u, done = s.links.pop()
            if not done:
                s.buf = s.buf.rstrip() + f']({u})'
        elif tag in ('b', 'strong'):
            s.buf = s.buf.rstrip() + '** '
        elif tag in ('em', 'i'):
            s.buf += '*'
        elif tag == 'code':
            s.buf += '`'
        if tag in s.BLOCK:
            s.flush()
        if tag in ('ul', 'ol'):
            s.depth -= 1
            if not s.depth:
                s.lines.append('')
    def handle_data(s, d):
        if not s.skip:
            s.buf += d
def to_md(body):
    body = re.sub(r'</span>(?=<span class="?chip)', '</span>, ', body)
    body = body.replace('<span class="sep">/</span>', ' / ')
    p = _MD(); p.feed(body); p.flush()
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(p.lines)).strip() + '\n'
def mdpath(path):
    return path + 'index.md' if path.endswith('/') else path + '.md'

# ---------- page writer
URLS = []  # (path, priority, lastmod) for the sitemap
ARTICLES = {'/about/', '/learn/', '/route/'}   # pages with Article JSON-LD get og:type article (content pages add theirs below)
def head(path, title, desc, lds, md=True):
    t, d, u = H(title), H(desc), H(SITE + path)
    return ((ld({'@graph': lds}) if lds else '') + f'\n<link rel="canonical" href="{u}">\n' + alt_links(path)
            + (f'<link rel="alternate" type="text/markdown" href="{H(mdpath(path))}">\n' if md else '')
            + f'<link rel="alternate" type="application/rss+xml" title="{SITE_NAME} changelog" href="/changelog/feed.xml">\n'
            f'<meta property="og:type" content="{"article" if path in ARTICLES else "website"}">\n'
            f'<meta property="og:site_name" content="{SITE_NAME}">\n<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n<meta property="og:url" content="{u}">\n'
            f'<meta property="og:image" content="{SITE}/og.png?v=2">\n<meta property="og:image:width" content="1200">\n'
            f'<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:site" content="@RiemannMap">\n'
            f'<meta name="twitter:title" content="{t}">\n<meta name="twitter:description" content="{d}">\n'
            f'<meta name="twitter:image" content="{SITE}/og.png?v=2">\n')
def page(path, title, desc, route, body, lds=(), priority=.5, md=None):
    is404 = path.endswith('.html')
    date = lastmod(path, title, desc, body)
    t = TPL
    t = re.sub(r'<title>.*?</title>', f'<title>{H(title)}</title>', t, count=1)
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H(desc)}">', t, count=1)
    t = between(t, '<!--head-->', '<!--/head-->', head(path, title, desc, list(lds), md=not is404))
    t = re.sub(r'<body data-route="[^"]*">', f'<body data-route="{H(route)}">', t, count=1)
    t = between(t, '<!--prerender-->', '<!--/prerender-->', body).replace('{{UPDATED}}', date)
    if is404:  # 404.html: noindex, no canonical
        t = t.replace(f'<link rel="canonical" href="{H(SITE + path)}">\n', '<meta name="robots" content="noindex">\n')
        open(os.path.join(OUT, path.strip('/')), 'w').write(t)
        return
    URLS.append((path, priority, date))
    md = ((md if md is not None else to_md(body.replace('{{UPDATED}}', date))) + f'\n---\n\n{title}. Web page: {SITE}{path} · updated {date} · '
          f'site map for machines: {SITE}/llms.txt\n')
    d = os.path.join(OUT, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.md'), 'w').write(md)
    if path == '/':
        return t
    open(os.path.join(d, 'index.html'), 'w').write(t)
def between(t, a, b, new):
    i, j = t.index(a) + len(a), t.index(b)
    return t[:i] + new + t[j:]
def clip(s, n=155):
    s = ' '.join(str(s or '').split())
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'
def fit(name, n=60):
    """Title for a map page: the name plus as much of the primary query ('Lean proof of the Riemann hypothesis')
    as fits in about 60 characters (keep in step with pageTitle() in app.js)."""
    for t in (f'{name} in the Lean proof of the Riemann hypothesis', f'{name} · Riemann hypothesis Lean proof',
              f'{name} · RH Lean proof'):
        if len(t) <= n:
            return t
    return name

# ---------- shared bits
for sub in ('theme', 'cluster', 'changelog', 'api', 'route'):
    shutil.rmtree(os.path.join(OUT, sub), ignore_errors=True)
def ctitle(k):
    return NAMES[k]['title'] if k in NAMES else folder_label(CL[k]['folders'])
def oneline(k, n=170):   # a cluster's description cut to its first sentence
    t = (NAMES.get(k) or {}).get('plain') or ''
    m = re.match(r'^(.{30,}?[.!?])\s+(?=[A-Z"(])', t)
    return clip(m.group(1) if m else t, n)
def clink(k, end='', sub=None):
    sub = TNAME[CL[k]['theme']] if sub is None else sub
    return (f'<li><a href="{CPATH[k]}"><span class="t">{H(ctitle(k))}' + (f'<small>{H(sub)}</small>' if sub else '') + '</span>'
            + (f'<span class="end">{H(end)}</span>' if end else '') + '</a></li>')
def pct(n):
    p = 100 * n / len(CL)
    return f'{p:.0f}%' if p >= 1 else ('under 1%' if n else '0%')
def feeds_txt(k):
    if k == main:
        return f'The whole proof feeds into it: it builds on all {builds[main]:,} other clusters.'
    n = feeds[k]
    return f'Feeds into {n:,} cluster{"" if n == 1 else "s"} · {pct(n)} of the map.'
def neighbours(title, ids, on_route):
    """'Builds on' / 'Needed by' as plain HTML: themes with counts, key neighbours, then the full list."""
    if not ids:
        return f'<h2>{title} 0 clusters</h2><p class="meta">None outside this cluster.</p>'
    tc = collections.Counter(CL[x]['theme'] for x in ids)
    key = sorted(ids, key=lambda x: (x not in on_route, -fcount[x], x))[:3]
    return (f'<h2>{title} {len(ids):,} cluster{"" if len(ids) == 1 else "s"}</h2>'
            f'<p class="meta">By theme: ' + ', '.join(f'<a href="{TPATH[t]}">{H(TNAME[t])}</a> ({n})' for t, n in tc.most_common()) + '</p>'
            f'<p class="meta">Key: ' + ', '.join(f'<a href="{CPATH[x]}">{H(ctitle(x))}</a>' + (' (on the route to the main theorem)' if x in on_route else '') for x in key) + '</p>'
            f'<ul class="rows">{"".join(clink(x) for x in sorted(ids, key=lambda x: (dist.get(x, 99), -fcount[x])))}</ul>')
MAIN = CPATH[main]
# route glyph: the import route to the main theorem, as inline SVG (keep in step with routeGlyph() in app.js).
# 1-3 steps: one dot per step, then the gold star; 4 or more: two dots, an ellipsis, the count in a ring, the star.
def route_glyph(d, color):
    import math
    parts = ['star'] if d == 0 else (['dot'] * d if d <= 3 else ['dot', 'dot', 'gap', 'num']) + ['star']
    wd, G, cy, x, out = {'dot': 7, 'gap': 10, 'num': 15, 'star': 14}, 5, 8, 1, []
    for i, p in enumerate(parts):
        if i:
            out.append(f'<line x1="{x:g}" y1="{cy}" x2="{x + G:g}" y2="{cy}" stroke="{color}" stroke-opacity=".55" stroke-width="1.4"/>'); x += G
        cx = x + wd[p] / 2
        if p == 'dot':
            out.append(f'<circle cx="{cx:g}" cy="{cy}" r="3.2" fill="{color}"/>')
        elif p == 'gap':
            out += [f'<circle cx="{cx + o:g}" cy="{cy}" r="1.1" fill="{color}"/>' for o in (-3.2, 0, 3.2)]
        elif p == 'num':
            out.append(f'<circle cx="{cx:g}" cy="{cy}" r="6.8" fill="none" stroke="{color}" stroke-width="1.3"/><text x="{cx:g}" y="{cy + 3.2:g}" '
                       f'text-anchor="middle" fill="{color}" font-family="Inter, system-ui, sans-serif" font-size="{7.5 if d > 9 else 9}" font-weight="600">{d}</text>')
        else:
            pts = ' '.join(f'{cx + q * math.cos(a):.1f},{cy + q * math.sin(a):.1f}' for j in range(10)
                           for a, q in [(-math.pi / 2 + j * math.pi / 5, 6.8 if j % 2 == 0 else 6.8 * .45)])
            out.append(f'<polygon points="{pts}" fill="#f5c46b"/>')
        x += wd[p]
    return (f'<span class="rg"><svg viewBox="0 0 {x + 1:g} 16" width="{x + 1:g}" height="16" aria-hidden="true" focusable="false">'
            + ''.join(out) + '</svg></span>')
def steps_txt(d):
    return 'The main theorem' if d == 0 else f'{d} import step{"" if d == 1 else "s"} to the main theorem'
STATUS = (f'<p class="meta">Proof status as of {AS_OF_TXT}: {ST_SHORT[0].lower()}{ST_SHORT[1:]} Names and descriptions on this map '
          'are written by Claude from samples of the code and may be wrong.</p>')
# feedback lives in one place: the site footer in the index.html template (@SomTheBuilder on X)
ABOUT_T = 'Has the Riemann hypothesis been solved? How it was checked'
CONTENT_PAGES = []   # (path, title, h1) of the Markdown content pages, filled in below; footer, home, llms.txt use it
ROUTE_T = 'How the Lean proof of the Riemann hypothesis is structured: the route to the main theorem'
ROUTE_NAV = 'How the proof is structured: the route to the main theorem'
LEARN_T = 'The Riemann hypothesis proof, step by step: learning path'
HOME_T = 'Lean proof of the Riemann hypothesis: an interactive map'
def explore(*extra, main_link=True):
    """'Where next' list on map pages: links the map to the explainers and back."""
    items = list(extra) + [(MAIN if main_link else None, "Start at the main theorem's cluster"), ('/route/', ROUTE_NAV), ('/about/', ABOUT_T),
                           ('/learn/', 'Learning path: the proof step by step, down to school maths')]
    return '<h2>Explore</h2><ul class="rows">' + ''.join(f'<li><a href="{p}">{H(t)}</a></li>' for p, t in items if p) + '</ul>'
TT = {x['id']: tnode(x) for x in core['nodes'] + concepts}
LEARN_OF = collections.defaultdict(list)  # cluster -> learning-path entries that point at it
for x in TT.values():
    for k in x['clusters']:
        LEARN_OF[k].append(x)

# ---------- theme pages
REL = collections.defaultdict(list)   # theme -> [(import links, other theme)] from the theme edges (tedges)
for (a, b), x in w.items():
    REL[a].append((x, b)); REL[b].append((x, a))
for t, th in TH.items():
    tn = TNAMED.get(t, {})
    cs = sorted(th['clusters'], key=lambda k: (dist.get(k, 99), -fcount[k]))
    desc = clip(f"{tn.get('blurb') or ''} {len(cs)} clusters of Lean files in the Lean proof of the Riemann hypothesis.")
    rel = sorted(REL[t], key=lambda z: (-z[0], z[1]))[:6]
    body = (f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>Theme</div>'
            f'<div class="eyebrow">Theme · Lean proof of the Riemann hypothesis</div>'
            f'<h1>{H(TNAME[t])}</h1>' + f'<p class="meta tags">Field: {H(FIELDS[FIDX[TFIELD[t]]]["name"])}</p>'
            + (f'<p class="lede">{H(tn["blurb"])}</p>' if tn.get('blurb') else '') + STATUS +
            f'<h2>Clusters</h2><ul class="rows">{"".join(clink(k, sub=oneline(k)) for k in cs)}</ul>'
            + (f'<h2>Related themes</h2><ul class="rows">' + ''.join(
                f'<li><a href="{TPATH[o]}"><span class="t">{H(TNAME[o])}<small>{x} import links between their clusters</small></span></a></li>'
                for x, o in rel) + '</ul>' if rel else '')
            + explore())
    page(TPATH[t], fit(TNAME[t]), desc, f'theme/{t}', body, [crumbs_ld(('Map', '/'), (TNAME[t], TPATH[t]))], .6)

# ---------- cluster pages
for k, p in CPATH.items():
    n, c = NAMES.get(k, {}), CL[k]
    title = n.get('title') or folder_label(c['folders'])
    src = n.get('source') if isinstance(n.get('source'), dict) else None
    refs = ''.join([f'<div class="ref">{H(src.get("title", ""))}{" · " + H(src["where"]) if src.get("where") else ""}'
                    f'<small>Background reading suggested by the AI namer · unchecked</small></div>'] if src else []) + \
           ''.join(f'<div class="ref note">{H(re.sub(r"\s*\(word match [\d.]+\):", " —", h))}<small>Cited in the author\'s note · '
                   f'matched by word overlap · unchecked</small></div>' for h in HINTS.get(k, []))
    conc = [CONC[x]['title'] if x in CONC else x.replace('concept-', '').replace('-', ' ') for x in n.get('concepts') or []]
    route = ''
    if k in dist and dist[k] > 0:   # the glyph is decorative here; the hidden text carries the meaning
        route = (f'<p class="meta"><a class="rglink" href="{MAIN}" title="{steps_txt(dist[k])}">'
                 f'{route_glyph(dist[k], fcol(FIELDS[FIDX[TFIELD[c["theme"]]]]))}<span class="sr">{steps_txt(dist[k])}.</span></a></p>')
    elif k == main:
        route = f'<p class="meta">{route_glyph(0, "#f5c46b")} This cluster holds the main theorem.</p>'
    th = c['theme']
    lp = LEARN_OF.get(k, [])
    up = uproute(k)
    why = ''
    if k != main and len(up) > 1:   # the route read upward: this cluster, each cluster that imports the last, the main theorem
        nr = nroutes.get(k, 1)
        why = ('<h2>Why it\'s in the proof</h2><ol class="rows steps">'
               + ''.join(f'<li><span class="t">This cluster: {H(ctitle(x))}</span></li>' if i == 0 else
                         f'<li><a href="{CPATH[x]}"><span class="t">★ Main theorem: {H(ctitle(x))}</span></a></li>' if x == main else
                         clink(x) for i, x in enumerate(up))
               + f'</ol><p class="meta">Each step is an import.' + (f' This is 1 of {"99+" if nr > 99 else nr} shortest routes.' if nr > 1 else '') + '</p>')
    on_route = set(up)
    body = (f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span><a href="{TPATH[th]}">{H(TNAME[th])}</a>'
            f'<span class="sep">/</span>{k}</div><div class="eyebrow">Cluster {k} · Lean proof of the Riemann hypothesis</div><h1>{H(title)}</h1>'
            f'<p class="meta tags">{H(ctag_line(k))}</p><p>{H(n.get("plain") or "")}</p>{route}<p class="meta">{H(feeds_txt(k))}</p>{STATUS}{why}'
            + (f'<h2>Prerequisite concepts</h2><div class="chips">{"".join(f"<span class=chip>{H(x)}</span>" for x in conc)}</div>' if conc else '')
            + (f'<h2>In the learning path</h2><ul class="rows">' + ''.join(
                f'<li><a href="/learn/#{H(x["id"])}"><span class="t">{H(x["title"])}<small>{H(x["kind"])}</small></span></a></li>' for x in lp)
               + '</ul>' if lp else '')
            + (f'<h2>References</h2>{refs}' if refs else '')
            + neighbours('Builds on', uses[k], on_route) + neighbours('Needed by', sorted(used_by[k]), on_route)
            + f'<p class="meta">{len(members[k])} Lean files, main folder {H(c["folders"][0][0] if c["folders"] else "")}.</p>'
            + explore((TPATH[th], f'Theme: {TNAME[th]}'), main_link=k != main))
    page(p, fit(title), clip(n.get('plain') or f'Cluster {k} of the Lean proof of the Riemann hypothesis.'), f'cluster/{k}', body,
         [crumbs_ld(('Map', '/'), (TNAME[th], TPATH[th]), (title, p))])

# ---------- about: the status of the claim, the page most searchers want (keep in step with about() in app.js)
STATUS_FACTS = [
    {'date': '2026-11-20', 'event': plain(ST_RELEASE), 'source': NOTE},
    {'date': '2026-11-21', 'event': plain(ST_CERT), 'source': STMT},
]
about = ('<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>About</div><div class="eyebrow">About · status of the proof</div>'
         '<h1>Has the Riemann hypothesis been solved?</h1>' + ST_LONG +
         '<h2>What this site is</h2><p>A reading guide: a map of the Lean files, grouped by their words and imports into '
         f'{len(CL):,} clusters in {len(TH)} themes. Cluster names and descriptions were written by Claude from a sample of about one '
         f'tenth of each cluster\'s files. They can be wrong. All {len(CL):,} clusters are named.</p><p>{UNMAPPED_TXT}</p><p>{ST_ARCHIVE}</p><p>{LICENSE_TXT}</p>'
         f'<h2>Where to start</h2><ul class="rows"><li><a href="{MAIN}">The main theorem\'s cluster</a></li>'
         '<li><a href="/learn/">Learning path: from the theorem down to school maths</a></li><li><a href="/">The full map</a></li>'
         '<li><a href="/changelog/">Changelog: what changed on this site, and when</a></li></ul>'
         '<h2>What the lines mean</h2><p>A line from cluster A to cluster B means some file in A imports a file in B. That is a formal '
         'dependency, not a claim about which ideas you need first. The golden route is the shortest chain of imports from the main '
         'theorem\'s cluster.</p>'
         f'<p class="meta">Data and scripts: <a href="{GH}">{GH.replace("https://", "")}</a> · data for machines: '
         '<a href="/api/">/api/</a> · updated {{UPDATED}}</p>')
ABOUT_D = f'A Lean proof of the Riemann hypothesis was released on 20 Nov 2026. {ST_META} What was checked, by whom, and what it covers.'
page('/about/', ABOUT_T, ABOUT_D, 'about', about,
     [article_ld('/about/', 'Has the Riemann hypothesis been solved? How the Lean proof was checked', ABOUT_D, '2026-11-21'),
      crumbs_ld(('Map', '/'), ('About', '/about/')), ORG], .9)

# ---------- learning path: the hand-built outline as nested lists (keep the H1 in step with learn() in app.js)
def tli(i, seen):
    n = TT.get(i)
    if not n or i in seen:
        return ''
    seen.add(i)
    on_map = ''.join(f' <a href="{CPATH[k]}">{H(NAMES[k]["title"] if k in NAMES else folder_label(CL[k]["folders"]))}</a>' for k in n['clusters'])
    kids = ''.join(tli(k, seen) for k in n['needs'])
    return (f'<li id="{H(i)}"><b>{H(n["title"])}</b> <small>{H(n["kind"])}</small><p>{H(n["plain"])}</p>'
            + (f'<p class="meta">On the map:{on_map}</p>' if on_map else '') + (f'<ul>{kids}</ul>' if kids else '') + '</li>')
seen = set()
LEARN_D = ('The Lean proof of the Riemann hypothesis, step by step: from the headline theorems through the main steps of '
           'the proof down to the background maths, with links to the code on the map.')
learn = ('<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>Learning path</div><div class="eyebrow">Learning path</div>'
         '<h1>The Riemann hypothesis proof, step by step</h1><p class="lede">From the Riemann hypothesis down to school maths: '
         'the outline runs from the two headline theorems through the main steps of the proof, then to background concepts and '
         'school or first-year university material. It follows the proof as we read it from the Lean code.</p>'
         f'<ul class="tree">{"".join(tli(r, seen) for r in core["roots"])}</ul>'
         f'<p class="meta">See also: <a href="/about/">how the proof was checked</a> · <a href="{MAIN}">the main theorem on the map</a></p>')
page('/learn/', LEARN_T, LEARN_D, 'learn', learn,
     [article_ld('/learn/', 'The Riemann hypothesis proof, step by step: a learning path', LEARN_D, '2026-11-21'),
      crumbs_ld(('Map', '/'), ('Learning path', '/learn/')), ORG], .8)

# ---------- /route/: how the proof is structured, from the main theorem down (keep numbers in step with the data)
DEPTHS = collections.Counter(dist.values())
def _plural(n, w):
    return f'{n:,} {w}{"" if n == 1 else "s"}'
DEPTH_KS = {d: sorted((k for k in CL if dist.get(k) == d), key=lambda k: -fcount[k]) for d in (1, 2)}
# the app draws this page as rings (routeView() in app.js); this static copy is its text equivalent: depth counts as a
# list, the first two steps as nested links (depth-2 clusters under the depth-1 cluster that imports them, as in par)
route_body = ('<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>Route</div><div class="eyebrow">Route · Lean proof of the Riemann hypothesis</div>'
              f'<h1>{H(ROUTE_T)}</h1>'
              f'<p class="lede">The Lean proof of the Riemann hypothesis is a library of {FILES_TXT}, grouped on this map into '
              f'{len(CL):,} clusters. A cluster\'s depth is the number of import steps from the main theorem\'s cluster to it.</p>'
              f'{STATUS}'
              '<h2>Clusters by depth</h2><p>Rings around the main theorem, from the centre out:</p><ul>'
              + ''.join(f'<li><a href="/list/?depth={d}">{"Depth 0 (the main theorem)" if d == 0 else "Depth " + str(d)}</a>: {_plural(DEPTHS[d], "cluster")}</li>' for d in sorted(DEPTHS))
              + (f'<li>Not reached from the main theorem: {_plural(len(CL) - len(dist), "cluster")}</li>' if len(dist) < len(CL) else '') + '</ul>'
              '<h2>The first two steps</h2><ul class="rows">'
              f'<li><a href="{CPATH[main]}"><span class="t">★ Main theorem: {H(ctitle(main))}</span></a><ul>'
              + ''.join(f'<li><a href="{CPATH[k]}">{H(ctitle(k))}</a> <small>depth 1</small>'
                        + (('<ul>' + ''.join(f'<li><a href="{CPATH[j]}">{H(ctitle(j))}</a> <small>depth 2</small></li>' for j in DEPTH_KS[2] if par.get(j) == k) + '</ul>')
                           if any(par.get(j) == k for j in DEPTH_KS[2]) else '') + '</li>' for k in DEPTH_KS[1])
              + '</ul></li></ul>'
              '<h2>File by file</h2><ul>'
              f'<li>{FSTATS["reached"]:,} Lean files, all reached from <code>Main</code> by imports</li>'
              f'<li>Median {FSTATS["median"]} imports from <code>Main</code>; farthest {FSTATS["max"]}</li>'
              f'<li>Longest import chain: {FSTATS["chain"]} files</li></ul>'
              '<p class="meta">Distances are shortest import chains; the cluster graph has loops, the file graph does not.</p>'
              f'<p><a href="/">Open the map</a> · <a href="{MAIN}">start at the main theorem</a> · <a href="/list/">every cluster as a list, by distance</a></p>')
ROUTE_D = clip(f'How the Lean proof of the Riemann hypothesis is structured: from the main theorem through {len(CL):,} clusters of '
               f'{TOTAL_FILES:,} Lean files, by import steps. The deepest cluster is {max(DEPTHS)} steps down; the longest import chain is {FSTATS["chain"]} files.')
page('/route/', ROUTE_T, ROUTE_D, 'route', route_body,
     [article_ld('/route/', ROUTE_T, ROUTE_D, '2026-11-22'), crumbs_ld(('Map', '/'), ('Route', '/route/')), ORG], .8)

# ---------- content pages: Markdown drafts in data/pages/*.md (copied from research/content/pages/, the approved text)
# Front matter gives title, description, h1 and path. Published as written, except: front matter, HTML comments and
# build notes for visuals not made yet (blockquotes starting "**Visual") are dropped, and the H1 comes from front matter.
# A page with sections '## … {#simple}', '{#student}' and '{#expert}' gets level tabs (all three in the DOM; app.js
# shows one, picked by the hash) and per-level Markdown copies at <path>simple.md, student.md and expert.md.
try:
    from markdown_it import MarkdownIt
except ImportError:
    sys.exit('build_site.py needs markdown-it-py: add --with markdown-it-py to the uv run command')
PAGES_DIR = os.path.join(REPO, 'data', 'pages')
MDIT = MarkdownIt('commonmark', {'html': False}).enable('table')
READ_LEVELS = [('simple', 'Simple'), ('student', 'Student'), ('expert', 'Expert')]
CONTENT = [   # draft, breadcrumb name, eyebrow, sitemap priority, first published
    ('status.md', 'Status', 'Status of the proof', .9),
    ('what-is-rh.md', 'What is the Riemann hypothesis?', 'Explainer · three levels', .9),
    ('how-we-know.md', 'How we know', 'How the proof was checked', .8),
    ('faq.md', 'FAQ', 'Frequently asked questions', .8),
    ('why-it-matters.md', 'Why it matters', 'Why it matters', .7),
    ('press.md', 'Press', 'Press, statements and reactions', .7)]
CONTENT_PUBLISHED = '2026-11-22'
def read_draft(f):
    t = open(os.path.join(PAGES_DIR, f), encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    fm, t = yaml.safe_load(m.group(1)), t[m.end():]
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'(?m)^> \*\*Visual [^\n]*\n(?:>[^\n]*\n)*\n?', '', t)
    t = re.sub(r'\A\s*# [^\n]*\n', '', t)
    return fm, re.sub(r'\n{3,}', '\n\n', t).strip() + '\n'
def md_html(t):
    h = MDIT.render(t)
    h = re.sub(r'<h([2-6])>(.*?)\s*\{#([\w-]+)\}</h\1>', r'<h\1 id="\3">\2</h\1>', h)
    h = h.replace('<table>', '<div class="tablewrap"><table>').replace('</table>', '</table></div>')
    return h.replace('<blockquote>', '<blockquote class="callout">').strip()
def md_abs(t):   # Markdown copies are read off-site: make site links absolute
    return re.sub(r'\]\((/[^)\s]*)\)', lambda m: f']({SITE}{m.group(1)})', t)
def h2_sections(t):   # [intro, '## …', '## …', …], split at H2 lines outside code fences
    out, cur, fence = [], [], False
    for line in t.split('\n'):
        if line.startswith('```'):
            fence = not fence
        if not fence and line.startswith('## '):
            out.append('\n'.join(cur)); cur = []
        cur.append(line)
    return out + ['\n'.join(cur)]
def level_split(t):
    """(before, {level: section}, after) if the page has all three level sections, one after the other; else None."""
    secs = h2_sections(t)
    idx = {}
    for i, x in enumerate(secs):
        m = re.match(r'## .*?\{#(\w+)\}\s*$', x.split('\n', 1)[0])
        if m:
            idx[m.group(1)] = i
    ids = [idx.get(l) for l, _ in READ_LEVELS]
    if None in ids:
        return None
    assert ids == list(range(ids[0], ids[0] + len(READ_LEVELS))), 'level sections must follow one another: simple, student, expert'
    return ('\n'.join(secs[:ids[0]]), {l: secs[i] for (l, _), i in zip(READ_LEVELS, ids)}, '\n'.join(secs[ids[-1] + 1:]))
def levels_html(before, lv, after):
    tabs = ''.join(f'<a href="#{l}" role="tab" data-level="{l}" aria-controls="{l}">{n}</a>' for l, n in READ_LEVELS)
    secs = ''.join(f'<section class="level" id="{l}" role="tabpanel" aria-label="{n} level">'
                   + md_html(re.sub(r'^(## .*?)\s*\{#\w+\}', r'\1', lv[l])) + '</section>' for l, n in READ_LEVELS)
    return (md_html(before) + '<div class="levels"><div class="ltabs" role="tablist" aria-label="Level">' + tabs + '</div>'
            + secs + '</div>' + md_html(after))
def keep_going(t):   # the closing links: a '## Keep going' / '## More' section, or a final 'More: …' line
    for x in h2_sections(t)[1:]:
        if re.match(r'## (Keep going|More)\b', x, re.I):
            return x.strip()
    m = re.search(r'(?m)^More: .*$', t)
    return m.group(0) if m else ''
def faq_pairs(t):   # H3 question, then its first paragraph (the visible answer, rendered the same way)
    return [(q, MDIT.renderInline(a.strip()))
            for q, a in re.findall(r'(?m)^### (.+)\n\n((?:(?!Source:)[^\n]+\n)+)', t)]
KNOWN_PATHS = set(CPATH.values()) | set(TPATH.values()) | {'/', '/about/', '/learn/', '/route/', '/list/', '/changelog/'}
DRAFTS = [(f, *read_draft(f), crumb, eb, pr) for f, crumb, eb, pr in CONTENT]
KNOWN_PATHS |= {fm['path'] for _, fm, *_ in DRAFTS}
for f, fm, t, crumb, eb, pr in DRAFTS:
    bad = [u for u in re.findall(r'\]\((/[^)#\s]*)', t) if u not in KNOWN_PATHS]
    assert not bad, f'{f}: links to pages that do not exist: {bad}'
    path, h1 = fm['path'], fm['h1']
    CONTENT_PAGES.append((path, fm['title'], h1))
    ARTICLES.add(path)
    lv = level_split(t)
    html_body = levels_html(*lv) if lv else md_html(t)
    html_body = re.sub(r'^<p><em>', '<p class="meta asof"><em>', html_body, count=1)
    body = (f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>{H(crumb)}</div><div class="eyebrow">{H(eb)}</div>'
            f'<h1>{H(h1)}</h1>{html_body}')
    lds = [article_ld(path, h1, fm['description'], CONTENT_PUBLISHED), crumbs_ld(('Map', '/'), (crumb, path)), ORG]
    if fm.get('structured_data') == 'FAQPage':
        pairs = faq_pairs(t)
        assert len(pairs) >= 10, f'{f}: FAQPage with only {len(pairs)} questions'
        lds.insert(1, faq_ld(pairs))
    page(path, fm['title'], fm['description'], 'page', body, lds, pr, md=md_abs(f'# {h1}\n\n{t}'))
    if lv:   # one Markdown file per level: title, a one-line intro, the level's section, the closing links
        before, secs, after = lv
        intro = next((x.strip() for x in before.split('\n\n') if x.strip() and not re.fullmatch(r'\*[^*].*\*', x.strip())), '')
        more = keep_going(after)
        for l, n in READ_LEVELS:
            others = ' · '.join(f'[{m}]({SITE}{path}{k}.md)' for k, m in READ_LEVELS)
            lmd = (f'# {h1} ({n})\n\n{intro}\n\n*{n} level of three ({others}). Full page with every level: {SITE}{path}*\n\n'
                   + re.sub(r'^(## .*?)\s*\{#\w+\}', r'\1', secs[l].strip()) + '\n\n' + (more + '\n' if more else ''))
            open(os.path.join(OUT, path.strip('/'), f'{l}.md'), 'w').write(
                md_abs(lmd) + f'\n---\n\n{h1} ({n}). Web page: {SITE}{path}#{l} · site map for machines: {SITE}/llms.txt\n')
LEVEL_PAGES = [p for f, fm, t, *_ in DRAFTS if level_split(t) for p in [fm['path']]]

# ---------- changelog (scripts/site/changelog.yaml) and its RSS feed
CHANGES = sorted(yaml.safe_load(open(os.path.join(HERE, 'changelog.yaml'))), key=lambda e: str(e['date']), reverse=True)
for e in CHANGES:
    e['anchor'] = f'd-{e["date"]}-{slug(e["title"], 40)}'
assert len({e['anchor'] for e in CHANGES}) == len(CHANGES), 'changelog: two entries with the same date and title' 
def rfc822(d):
    return email.utils.format_datetime(datetime.datetime.combine(datetime.date.fromisoformat(str(d)), datetime.time(12), datetime.timezone.utc))
def change_html(e):
    return f'<ul>{"".join(f"<li>{H(x)}</li>" for x in e["items"])}</ul>'
clog = ('<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>Changelog</div><div class="eyebrow">Changelog</div>'
        '<h1>What changed on this site</h1><p class="lede">Dated changes to the map, its pages and the proof status it reports. '
        'Follow along with the <a href="/changelog/feed.xml">RSS feed</a> or <a href="' + X_SITE + '">@RiemannMap on X</a>.</p>'
        + ''.join(f'<h2 id="{e["anchor"]}">{H(e["title"])} <small>{datetime.date.fromisoformat(str(e["date"])).strftime("%-d %b %Y")}</small></h2>'
                  + change_html(e) for e in CHANGES))
page('/changelog/', 'Changelog · RH Lean Explorer', 'Dated changes to the map of the Lean proof of the Riemann hypothesis: '
     'new pages, data and status updates.', 'page', clog, [crumbs_ld(('Map', '/'), ('Changelog', '/changelog/'))], .4)
open(os.path.join(OUT, 'changelog', 'feed.xml'), 'w').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>\n'
    f'<title>{SITE_NAME} changelog</title><link>{SITE}/changelog/</link>\n'
    '<description>Dated changes to the map of the Lean proof of the Riemann hypothesis.</description><language>en</language>\n'
    f'<atom:link href="{SITE}/changelog/feed.xml" rel="self" type="application/rss+xml"/>\n'
    f'<lastBuildDate>{rfc822(CHANGES[0]["date"])}</lastBuildDate>\n'
    + ''.join(f'<item><title>{H(e["title"])}</title><link>{SITE}/changelog/#{e["anchor"]}</link>'
              f'<guid isPermaLink="false">rh-lean-explorer-changelog-{e["anchor"]}</guid><pubDate>{rfc822(e["date"])}</pubDate>'
              f'<description>{H(change_html(e))}</description></item>\n' for e in CHANGES)
    + '</channel></rss>\n')

# ---------- home: crawlable intro plus links to every theme
HOME_DESC = (f'The Lean proof of the Riemann hypothesis, visualized: an interactive map of its {FILES_TXT}. '
             f'{ST_META}')
home = ('<div class="eyebrow">Interactive map · Lean 4</div><h1 class="hero">The <em>Lean</em> proof of the Riemann hypothesis, mapped</h1>'
        f'<p class="lede">An interactive map of the {FILES_TXT} in Levent Alpöge\'s proof of the Riemann hypothesis, '
        f'released on 20 Nov 2026, grouped into {len(CL):,} clusters in {len(TH)} themes.</p>{STATUS}'
        f'<ul class="rows"><li><a href="/status/">Has the Riemann hypothesis been solved? Status of the proof</a></li>'
        '<li><a href="/what-is-the-riemann-hypothesis/">What is the Riemann hypothesis? Simple, student and expert</a></li>'
        '<li><a href="/how-we-know/">How we know the proof is correct</a></li><li><a href="/faq/">Frequently asked questions</a></li>'
        f'<li><a href="{MAIN}">Start at the main theorem</a></li><li><a href="/learn/">Learning path: the proof step by step</a></li>'
        '<li><a href="/changelog/">Changelog</a></li></ul>'
        f'<h2>Themes</h2><ul class="rows">{"".join(f"<li><a href=\"{TPATH[t]}\">{H(TNAME[t])}</a></li>" for t in TH)}</ul>')
DATASET = {
    '@type': 'Dataset', '@id': SITE + '/#dataset', 'name': 'Map of the Lean proof of the Riemann hypothesis',
    'description': (f"Clusters and themes of the {FILES_TXT} in Levent Alpöge's Lean proof of the Riemann hypothesis: "
                    f'{len(CL):,} clusters in {len(TH)} themes, the import links between clusters, each cluster\'s distance in '
                    'import steps from the main theorem, and cluster names and descriptions written by Claude from samples '
                    'of the code (they may be wrong). No Lean source text is included.'),
    'url': SITE + '/', 'sameAs': GH, 'isAccessibleForFree': True, 'license': LICENSE, 'inLanguage': 'en', 'dateModified': DATA_DATE,
    'creator': {'@id': ORG_ID}, 'publisher': {'@id': ORG_ID}, 'about': RH_THING, 'isBasedOn': NOTE,
    'keywords': ['Riemann hypothesis', 'Lean 4', 'formal proof', 'Mathlib', 'proof map', 'import graph'],
    'distribution': [{'@type': 'DataDownload', 'encodingFormat': 'application/json', 'contentUrl': SITE + u, 'name': nm}
                     for u, nm in (('/api/clusters.json', 'Clusters: id, title, theme, page, files, distance from the main theorem, field, era, maths level'),
                                   ('/api/themes.json', 'Themes: id, name, blurb, page, clusters, files'),
                                   ('/api/status.json', 'Dated status of the proof, with primary sources'))],
}
# 404 (written before index.html, from the template); with a 404.html, Cloudflare Pages returns real 404s
page('/404.html', 'Page not found · RH Lean Explorer', HOME_DESC, '404',
     '<div class="eyebrow">404</div><h1>Page not found</h1><p class="lede">That page is not on the map. '
     '<a href="/">Open the full map</a> or <a href="/about/">read how the proof was checked</a>.</p>')
open(os.path.join(OUT, 'index.html'), 'w').write(page('/', HOME_T, HOME_DESC, '', home, [
    {'@type': 'WebSite', '@id': SITE_ID, 'name': SITE_NAME, 'url': SITE + '/', 'description': HOME_DESC, 'inLanguage': 'en',
     'about': RH_THING, 'publisher': {'@id': ORG_ID}, 'sameAs': [X_SITE]}, ORG, DATASET], 1.0))

# ---------- /api/: small JSON files for machines (short cache; /data/ is the app's own versioned format)
os.makedirs(os.path.join(OUT, 'api'), exist_ok=True)
def jdump(name, obj):
    json.dump(obj, open(os.path.join(OUT, 'api', name), 'w'), ensure_ascii=False, separators=(',', ':'))
API_STATUS = {
    'updated': NEW_STATE['/status/'][1], 'question': 'Has the Riemann hypothesis been solved?',
    'as_of': STATUS_AS_OF, 'status': plain(ST_SHORT), 'timeline': STATUS_FACTS,
    'certification': {'text': plain(ST_CERT), 'quote': plain(ST_QUOTE), 'source': STMT},
    'verified': plain(ST_VERIFIED), 'verified_sources': [DREW, RUBINSTEIN],
    'checks': [plain(x) for x in ST_CHECKS], 'checks_source': STMT,
    'ongoing_checks': {'text': plain(ST_ONGOING), 'url': DREW},
    'scope': plain(ST_SCOPE),
    'source_archive': {'text': plain(ST_ARCHIVE), 'repo': LEAN_REPO, 'commit': LEAN_SHA, 'files': TOTAL_FILES},
    'sources': [{'name': t, 'url': u} for t, u in ST_SOURCES], 'details': DREW, 'page': SITE + '/status/',
    'counts': {'lean_files': TOTAL_FILES, 'mapped_files': len(mod_cl), 'clusters': len(CL), 'themes': len(TH)},
    'note': 'Cluster and theme names and descriptions on this site are written by Claude from samples of the code and may be wrong.',
    'license': {'url': LICENSE, 'name': 'CC BY 4.0', 'applies_to': "this site's own data (cluster and theme names, descriptions, map layout, JSON); the Lean source keeps its own licence"},
}
jdump('status.json', API_STATUS)
API_FIELDS = [{'id': f['id'], 'name': f['name'], 'hue': f['hue'], 'description': f['description']} for f in FIELDS]
jdump('clusters.json', {'updated': DATA_DATE, 'site': SITE, 'fields': {'path': 'page on the site (prefix with site)', 'dist': 'import steps from the main theorem (null: not reachable)',
      'files': 'Lean files in the cluster', 'field': "id of the cluster's field of mathematics (that of its theme; see math_fields)",
      'era': 'decade of the newest concept the cluster needs: ' + ', '.join(n for n, _ in ERA_OF.items()),
      'era_year': 'year of that newest concept', 'level': 'highest maths level among its concepts: ' + ', '.join(n for _, n in LEVELS),
      'new_in_proof': "true if it rests on the proof's own named constructions rather than published mathematics"},
      'tags_note': 'field, era and level are editorial tags derived from the theme and cluster descriptions and their concept tags; they may be wrong',
      'math_fields': API_FIELDS, 'main': main, 'clusters': [
    {'id': k, 'title': NAMES[k]['title'] if k in NAMES else None, 'theme': CL[k]['theme'], 'path': CPATH[k],
     'files': fcount[k], 'dist': dist.get(k), 'field': TFIELD[CL[k]['theme']], 'era': CTAGS[k]['era'], 'era_year': CTAGS[k]['era_year'],
     'level': CTAGS[k]['level'], 'new_in_proof': CTAGS[k]['new_in_proof']} for k in CL]})
jdump('themes.json', {'updated': DATA_DATE, 'fields': {'files': 'Lean files in the theme (all themes sum to the mapped total)',
      'units': 'units after folding wrappers and single-use helpers into the file they belong to', 'clusters': 'clusters in the theme',
      'field': 'id of the field of mathematics the theme belongs to (see math_fields in /api/clusters.json)'}, 'themes': [
    {'id': t, 'name': TNAME[t], 'blurb': TNAMED.get(t, {}).get('blurb'), 'path': TPATH[t], 'url': SITE + TPATH[t],
     'clusters': len(TH[t]['clusters']), 'files': sum(fcount[k] for k in TH[t]['clusters']), 'units': size[t], 'field': TFIELD[t]} for t in TH]})
API_INDEX = {'name': SITE_NAME + ' API', 'description': 'Static JSON about the map of the Lean proof of the Riemann hypothesis.',
             'endpoints': {'/api/status.json': 'dated proof status with primary sources',
                           '/api/clusters.json': f'all {len(CL):,} clusters: id, title, theme, page, files, dist, field, era, era_year, level, new_in_proof; plus math_fields, the {len(FIELDS)} fields (id, name, hue, description)',
                           '/api/themes.json': f'all {len(TH)} themes: id, name, blurb, page, clusters, files, field'},
             'tags': {'field': f'one of {len(FIELDS)} fields of mathematics per theme; a cluster takes its theme\'s field',
                      'era': 'decade of the newest concept a cluster needs: ' + ', '.join(ERA_OF),
                      'level': 'highest maths level among a cluster\'s concepts: ' + ', '.join(n for _, n in LEVELS),
                      'new_in_proof': 'the cluster rests on the proof\'s own named constructions',
                      'note': 'editorial tags derived from descriptions and concept tags; they may be wrong',
                      'map_filters': 'the map takes the same filters in its URL, e.g. /?field=av,aut&d=0-4&era=1960s&level=phd&new=1; /list/ too'},
             'markdown': 'every HTML page has a Markdown copy at <page>index.md, e.g. /status/index.md; pages with levels also have '
                         '<page>simple.md, student.md and expert.md, e.g. /what-is-the-riemann-hypothesis/student.md',
             'feeds': {'/changelog/feed.xml': 'RSS 2.0 changelog', '/sitemap.xml': 'all pages'}, 'source': GH,
             'license': API_STATUS['license']}
jdump('index.json', API_INDEX)
open(os.path.join(OUT, 'api', 'index.html'), 'w').write(
    '<!doctype html><meta charset="utf-8"><title>API · RH Lean Explorer</title><meta name="robots" content="noindex">'
    '<link rel="canonical" href="' + SITE + '/api/index.json"><pre>' + H(json.dumps(API_INDEX, indent=2, ensure_ascii=False)) + '</pre>')

# ---------- llms.txt and llms-full.txt
llms = (f'# {SITE_NAME}\n\n> {HOME_DESC}\n\n'
        f'An interactive map of the Lean proof of the Riemann hypothesis: {FILES_TXT} in {len(CL):,} clusters and {len(TH)} themes. '
        'Names and descriptions are written by Claude from samples of the code and may be wrong. Every page has a Markdown copy at <page>index.md.\n\n'
        f'## Status (as of {STATUS_AS_OF})\n\n'
        + ''.join(f'- {e["date"]}: {e["event"]} Source: {e["source"]}\n' for e in STATUS_FACTS)
        + f'- {plain(ST_QUOTE)}\n- Verified: {mdtext(ST_VERIFIED)}\n- The joint statement certifies four criteria:\n'
        + ''.join(f'  {i}. {mdtext(x)}\n' for i, x in enumerate(ST_CHECKS, 1))
        + f'- {mdtext(ST_ONGOING)}\n- What was proved: {mdtext(ST_SCOPE)}\n'
        + f'- Source shown on the map: {mdtext(ST_ARCHIVE)}\n'
        + '- Primary sources: ' + '; '.join(f'[{t}]({u})' for t, u in ST_SOURCES) + '\n\n'
        f'## Start here\n\n'
        + ''.join(f'- [{h1}]({SITE}{p}index.md)\n' for p, _, h1 in CONTENT_PAGES)
        + ''.join(f'- Levels for {SITE}{p}: for a plain explanation with no maths background fetch {SITE}{p}simple.md; '
                  f'for high-school or undergraduate level {SITE}{p}student.md; for researchers {SITE}{p}expert.md. '
                  f'{SITE}{p}index.md has all three.\n' for p in LEVEL_PAGES)
        + f'- [About this site and how the proof was checked]({SITE}/about/index.md)\n'
        f'- [Learning path: the proof step by step]({SITE}/learn/index.md)\n'
        f'- [How the proof is structured: the route to the main theorem]({SITE}/route/index.md)\n\n'
        f'## The map, by theme\n\n'
        + ''.join(f'- [{TNAME[t]}]({SITE}{TPATH[t]}index.md)\n' for t in sorted(TH, key=lambda t: TNAME[t]))
        + f'\n## Data\n\n- [API index]({SITE}/api/index.json): the JSON endpoints\n'
        f'- [Clusters]({SITE}/api/clusters.json): every cluster with its page and distance from the main theorem\n'
        f'- Licence: CC BY 4.0 ({LICENSE}) for the site\'s own data (names, descriptions, map layout, JSON); the Lean source keeps its own licence.\n\n'
        f'## Updates\n\n- [Changelog]({SITE}/changelog/index.md) · [RSS]({SITE}/changelog/feed.xml)\n'
        f'- Full text of the key pages: {SITE}/llms-full.txt\n')
open(os.path.join(OUT, 'llms.txt'), 'w').write(llms)
# llms-full.txt: the content pages, About, Learn, /route/, and every cluster within two steps of the main theorem, in full
full = [llms, '\n---\n']
for pth in [p for p, _, _ in CONTENT_PAGES] + ['/about/', '/learn/', '/route/'] + [CPATH[k] for k in sorted((k for k in CL if dist.get(k, 99) <= 2), key=lambda k: (dist[k], -fcount[k]))]:
    full += [open(os.path.join(OUT, pth.strip('/'), 'index.md')).read(), '\n---\n']
open(os.path.join(OUT, 'llms-full.txt'), 'w').write('\n'.join(full))

# ---------- sitemap (clean URLs, lastmod from the content state), robots, IndexNow key
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{d}</lastmod><priority>{p}</priority></url>\n'
              for u, p, d in sorted(URLS, key=lambda z: (-z[1], z[0]))) + '</urlset>\n')
# _redirects (Cloudflare Pages, read top-down): the app-view rewrites, then 301s from old theme paths (renamed themes,
# from TSLUG_HIST) to the current ones, with and without the trailing slash, and for the Markdown copies
REDIR = ('# Generated by scripts/site/build_site.py; edit there, not here.\n'
         '# Cloudflare Pages rewrites (200 = serve the home page (index.html) at the same URL; target must be "/" because Pages 308s /index.html to /; the app reads the path).\n'
         '# Clusters, themes, /about/, /learn/ and /changelog/ are real static pages; only these app views have none.\n'
         '# Any other unknown path still gets the real 404 (404.html).\n'
         '/file/*     /   200\n/concept/*  /   200\n/list       /   200\n/list/      /   200\n')
if TOLD:
    REDIR += '\n# Renamed themes: old address -> current address (permanent)\n' + ''.join(
        f'{o} {n} 301\n{o.rstrip("/")} {n} 301\n{o}index.md {n}index.md 301\n' for o, n in sorted(TOLD.items()))
open(os.path.join(OUT, '_redirects'), 'w').write(REDIR)
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nContent-Signal: search=yes, ai-input=yes, ai-train=yes\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
KEY_F = os.path.join(HERE, 'indexnow.key')   # IndexNow key (public by design: it is served at /<key>.txt)
if not os.path.exists(KEY_F):
    open(KEY_F, 'w').write(secrets.token_hex(16) + '\n')
KEY = open(KEY_F).read().strip()
for f in glob.glob(os.path.join(OUT, '*.txt')):
    if re.fullmatch(r'[0-9a-f]{32}\.txt', os.path.basename(f)) and os.path.basename(f) != KEY + '.txt':
        os.remove(f)
open(os.path.join(OUT, KEY + '.txt'), 'w').write(KEY)
json.dump(dict(sorted(NEW_STATE.items())), open(STATE_F, 'w'), indent=0, separators=(',', ':'))
changed = sorted(u for u, _, d in URLS if d == today)
print(f'{len(TPATH)} theme pages, {len(CPATH)} cluster pages, sitemap with {len(URLS)} urls ({len(changed)} changed today); '
      f'data v={DATA_V} app v={APP_V} css v={CSS_V}')
