"""Write data/*.json for the static explorer site (github.com/rithn/rh-lean-explorer).

usage: uv run -q --with pyyaml --with networkx --with scipy --with markdown-it-py --with pillow python -I scripts/site/build_site.py <cluster dir> <out dir>
e.g.   ... build_site.py ../notes/cluster3 ../site
(from a worktree, e.g. repo-core: ... build_site.py ../notes/cluster3 ../site-core)

Reads only our own derived data (map.json, merged.tsv, import list, naming answers, tree YAML).
No Lean source text is copied: files appear by module name and path only.
"""
import os, re, sys, json, glob, shutil, datetime, collections
import yaml, networkx as nx

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.dirname(REPO)
D, OUT = sys.argv[1], sys.argv[2]
# 80a: --src-bundles[=DIR] also writes one Lean source bundle per cluster (default DIR: <out>/src/c). Off by default:
# the full set is ~1 GB (the whole archive once more), see the note at SRC_BUNDLE below
SRC_BUNDLES = next((a.split('=', 1)[1] if '=' in a else os.path.join(OUT, 'src', 'c') for a in sys.argv[3:] if a.startswith('--src-bundles')), None)
# N3 tier 1 (works cited on guide pages that cover a cluster) and the Codex judgments that override them: rebuilt from
# research/references/n3/ on every build where it exists (RH_N3 points elsewhere), so a new batch of judgments needs only
# a rebuild; the script rewrites data/guide-cited-refs.tsv and data/references-n3.yaml only when their content changes.
# Without research/ the committed copies are read. Run before data/c/ is cleared: merge.py reads cluster titles there.
N3_D = os.environ.get('RH_N3') or os.path.join(ROOT, 'research', 'references', 'n3')
if os.path.exists(os.path.join(N3_D, 'candidates.tsv')):
    import subprocess
    subprocess.run([sys.executable, '-I', os.path.join(REPO, 'scripts', 'refs', 'guide_cited_refs.py'), '--n3', N3_D], check=True)
os.makedirs(os.path.join(OUT, 'data', 'c'), exist_ok=True)
for f in glob.glob(os.path.join(OUT, 'data', 'c', '*.json')):
    os.remove(f)
# front-end files (index.html, app.js, style.css) live in the explorer repo itself; only data/ is written

M = json.load(open(os.path.join(D, 'map.json')))
CL = {c['id']: c for c in M['clusters']}
TH = {t['id']: t for t in M['themes']}

# ---------- content dates (lastmod). State in scripts/site/lastmod.json: key -> [content hash, date the content last
# changed]. A key is a page path ('/status/'), or 'data:' for the app data. The date moves only when the hash moves, so
# rebuilding unchanged content keeps every date; a key seen for the first time gets today. The hash leaves out noise:
# asset versions (?v=…, data-v="…") and anything the caller strips (the Share bar). scripts/site/indexnow.py reads the
# same hashes to submit only the pages that changed since its last submission.
import hashlib
today = datetime.date.today().isoformat()
STATE_F = os.path.join(HERE, 'lastmod.json')
STATE = json.load(open(STATE_F)) if os.path.exists(STATE_F) else {}
NEW_STATE = {}
NOISE_RE = re.compile(r'\?v=[0-9a-f]+|\s?data-v="[^"]*"|(?<=/app)\.[0-9a-f]{10}(?=\.js)|(?<=/style)\.[0-9a-f]{10}(?=\.css)')
def chash(*parts):
    return hashlib.sha256('\x00'.join(NOISE_RE.sub('', x) for x in parts).encode()).hexdigest()[:12]
def lastmod(key, *parts):
    h = chash(*parts)
    old = STATE.get(key)
    NEW_STATE[key] = [h, old[1] if old and old[0] == h else today]
    return NEW_STATE[key][1]

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
# the namers saw only statements, so many descriptions end by hedging about proofs; the joint statement by the Lean FRO
# and the Mathlib Initiative has since certified the proof (21 Nov 2026), so drop those sentences (or the hedging clause)
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
# ---------- checked names (data/core-names.yaml): the 16 core clusters' titles and descriptions, checked against their
# full Lean source. They win over every AI run above (and skip dehedge/deconf: they are used exactly as written). Each
# also carries its evidence (module: declaration — what it says), shown on the cluster's page and in the app's panel.
CHECKED = yaml.safe_load(open(os.path.join(REPO, 'data', 'core-names.yaml')))
assert set(CHECKED) <= set(CL), 'core-names.yaml names an unknown cluster'
for k, x in CHECKED.items():
    assert x.get('title') and x.get('plain') and len(x.get('evidence') or []) >= 2, f'core-names.yaml: {k} needs title, plain, evidence'
    NAMES[k] = {**NAMES.get(k, {}), 'title': x['title'], 'plain': ' '.join(x['plain'].split()), 'checked': True}
def evidence(k, n=3):   # [(module, declaration, what it says)] for a checked cluster, first n
    out = []
    for e in CHECKED[k]['evidence'][:n]:
        e = ' '.join(e.split())
        m = re.match(r'^(\S+): (.+?) — (.+)$', e)
        out.append(m.groups() if m else ('', '', e))
    return out
HINTS = json.load(open(os.path.join(D, 'hints.json'))) if os.path.exists(os.path.join(D, 'hints.json')) else {}
# ---------- 35b: checked references for the spine (data/references-spine.yaml, a copy of research/references/
# spine-2026-11-23.yaml). On those clusters they replace the AI namer's book suggestion ('source'), which elsewhere is
# shown as "Automatic match, unchecked". exact and section come first; topic is shown as Background. A cluster with no
# checked reference keeps its automatic one unless the yaml's verdict on it is 'wrong'. Notes the checker marked as
# unread suggestions ("My suggestion; not read", "... Not read.") are not shown; 'evidence' goes to /api/ only.
SPINE_Y = yaml.safe_load(open(os.path.join(REPO, 'data', 'references-spine.yaml'), encoding='utf-8'))
SPINE_DATE = str(SPINE_Y['meta']['written'])
PREC_ORDER = {'exact': 0, 'section': 1, 'topic': 2}
PREC_TIP = {'exact': 'Exact: the theorem or lemma number was read in the cited text and the result matches the Lean statement',
            'section': 'Section: the right chapter or section, not a specific theorem',
            'topic': 'Topic: a general reference, cited without a checked chapter or theorem number'}
AUTO_LABEL = 'Automatic match, unchecked'
_UNREAD = re.compile(r'(?i)\bnot read\b')
def _spine_ref(r):
    assert r['precision'] in PREC_ORDER, r
    url = r.get('url') or (f'https://doi.org/{r["doi"]}' if r.get('doi') else None)
    note = ' '.join(str(r.get('note') or '').split())
    return {'citation': ' '.join(r['citation'].split()), 'locator': ' '.join(str(r.get('locator') or '').split()) or None,
            'url': url, 'doi': r.get('doi'), 'precision': r['precision'],
            'match': ' '.join(str(r.get('match') or '').split()) or None,
            'note': None if not note or _UNREAD.search(note) else note}
SPINE = {}
for x in SPINE_Y['clusters']:
    k = x['id']
    assert k in CL, f'references-spine.yaml names an unknown cluster {k}'
    refs = sorted((_spine_ref(r) for r in x.get('references') or []), key=lambda r: PREC_ORDER[r['precision']])
    SPINE[k] = {'verdict': x['current_book_verdict'], 'refs': refs,
                'evidence': [[str(e) for e in r.get('evidence') or []] for r in sorted(x.get('references') or [], key=lambda r: PREC_ORDER[r['precision']])]}
    s = NAMES.get(k, {}).get('source')
    cur = f'{s["title"]}, {s["where"]}' if isinstance(s, dict) and s.get('where') else (s or {}).get('title') if isinstance(s, dict) else None
    if (cur or None) != (x.get('current_book_reference') or None):
        print(f'NOTE references-spine.yaml {k}: the reference it judged ({x.get("current_book_reference")!r}) is not today\'s ({cur!r})')
# N3: references from guide citations that Codex judged 'supports' (data/references-n3.yaml, written by
# scripts/refs/guide_cited_refs.py from merge.py's output; only its n3: true entries are read, the spine ones above are
# the same). Shown exactly as the spine's checked references, after them, on spine and other clusters alike. CHECKED_REFS:
# cluster -> {'refs', 'evidence', 'date'}, the spine's and N3's together, by precision. A non-spine cluster keeps its
# automatic book reference: N3 did not assess it.
N3_F = os.path.join(REPO, 'data', 'references-n3.yaml')
N3_Y = yaml.safe_load(open(N3_F, encoding='utf-8')) if os.path.exists(N3_F) else {'meta': {}, 'clusters': []}
N3_DATE = str(N3_Y['meta'].get('written') or SPINE_DATE)
CHECKED_REFS = {k: {'refs': list(v['refs']), 'evidence': list(v['evidence']), 'date': SPINE_DATE} for k, v in SPINE.items()}
N3_N = collections.Counter()
N3_FULL_NOTE = {}
def n3_note(full, n):   # pages and app: the first supports judgment's note (merge.py puts the best one first, notes
    # joined by ' | '), at most 2 sentences, then how many guide citations were judged; the full text stays in the API
    first = (full or '').split(' | ')[0].strip()
    ss = re.split(r'(?<=[.!?])\s+(?=[A-Z(])', first) if first else []
    short = ' '.join(ss[:2])
    if short and _UNREAD.search(short):
        short = ''
    return ' '.join(x for x in (short, f'({n} guide {"citation" if n == 1 else "citations"} checked)') if x)
for x in N3_Y.get('clusters') or []:
    rs = [r for r in x.get('references') or [] if r.get('n3')]
    if not rs or x['id'] not in CL:
        assert not rs, f'references-n3.yaml names an unknown cluster {x["id"]}'
        continue
    e = CHECKED_REFS.setdefault(x['id'], {'refs': [], 'evidence': [], 'date': N3_DATE})
    e['date'] = max(e['date'], N3_DATE)
    for r in rs:
        d = {**_spine_ref(r), 'basis': 'guide-citation-judged'}
        full = ' '.join(str(r.get('note') or '').split()) or None
        d['note'] = n3_note(full, len(r.get('cand_ids') or []) or 1)
        e['refs'].append(d)
        e['evidence'].append([str(z) for z in r.get('evidence') or []])
        N3_FULL_NOTE[id(d)] = full   # the API keeps every judgment's note
        N3_N[x['id'] in SPINE] += 1
for e in CHECKED_REFS.values():
    o = sorted(range(len(e['refs'])), key=lambda i: PREC_ORDER[e['refs'][i]['precision']])
    e['refs'], e['evidence'] = [e['refs'][i] for i in o], [e['evidence'][i] for i in o]
print(f'references (N3, judged supports): {sum(N3_N.values())} checked references from guide citations, '
      f'{N3_N[True]} on spine clusters, {N3_N[False]} elsewhere')
def shown_source(k):   # the automatic (AI namer) book reference still shown for cluster k, or None
    s = NAMES.get(k, {}).get('source')
    if not isinstance(s, dict) or not s.get('title'):
        return None
    if k in SPINE and (SPINE[k]['refs'] or SPINE[k]['verdict'] == 'wrong'):
        return None
    return s
for k in ('k0704', 'k0674', 'k0694', 'k0469'):   # the four the checker found wrong: their automatic reference must go
    assert k in SPINE and SPINE[k]['verdict'] == 'wrong' and shown_source(k) is None, k
print(f'references: {len(SPINE)} spine clusters, {sum(len(v["refs"]) for v in SPINE.values())} checked references')

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
# the files in the archive but not on the map, recounted from the source (22 Nov 2026; /proof-in-numbers/ has the same
# breakdown): import-only files that just list other files, build helpers (BuildAid.D1–D5), and files with no theorem or definition
UNMAPPED = {'import_only': 150, 'build_helpers': 5, 'no_theorem_or_definition': 5}
assert sum(UNMAPPED.values()) == TOTAL_FILES - len(mod_cl), 'unmapped-file breakdown no longer adds up: recount it'
LICENSE = 'https://creativecommons.org/licenses/by/4.0/'

# ---------- proof status: the ONE canonical wording (plan item 36). Every status line comes from here: page footers and
# meta descriptions (short form), /api/status.json, llms.txt and llms-full.txt (long form), and the app, which reads
# overview.json 'status' (home lede, source card). /status/ itself is data/pages/status.md. Facts and quotes: research/content/fact-sheet.md, VERIFIED lines
# only. When a sentence changes, move STATUS_AS_OF and add a changelog entry. Write HTML; plain() and mdtext() derive the rest.
import html as _html
STATUS_AS_OF = '2026-11-24'
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
ST_CERT = (f'On 21 Nov 2026 a <a href="{STMT}">joint statement</a> by the Lean FRO and the Mathlib Initiative '
           'certified the Lean statement and proof.')   # byline as changed on the blog on 23 Nov 2026
ST_MORE = f'More independent checks: <a href="{DREW}">math.mit.edu/~drew/grh</a>.'
ST_SHORT = f'{ST_CERT} {ST_MORE}'
ST_META = plain(ST_CERT)
ST_META_SHORT = 'Certified by the Lean FRO and the Mathlib Initiative on 21 Nov 2026.'   # the home meta description (160-character cap)
ST_CHIP = 'certified 21 Nov'   # header chip label; its tooltip is ST_META
ST_CHIP_SHORT = 'Certified'      # the chip's label on narrow screens
# long form: /api/status.json, llms.txt, llms-full.txt
ST_RELEASE = (f'On 20 Nov 2026 Levent Alpöge released a proof of the Riemann hypothesis, and of the generalized Riemann hypothesis '
              f'(GRH) for Dirichlet L-functions, as a Lean library of {TOTAL_FILES:,} Lean files, {LINES_TXT}, with a note at '
              f'<a href="{NOTE}">alpo.ge</a>.')
ST_QUOTE = 'In its words: “We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct.”'
ST_CHECKS = [   # the joint statement's four criteria, in its order, worded as on /status/ (data/pages/status.md)
    f'The formal statement is the Riemann hypothesis as Mathlib states it: <a href="{MATHLIB_RH}"><code>RiemannHypothesis</code></a>.',
    'The library compiles without errors, and dozens of people reproduced the same proof export.',
    'Two independent tools confirmed that the theorem proved, <code>riemannHypothesis</code>, is exactly Mathlib\'s statement of the Riemann hypothesis.',
    'Several independent proof checkers accepted the exported proof.']
ST_VERIFIED = (f'All {TOTAL_FILES:,} modules compile with zero errors. Every module has been replayed through Lean\'s kernel, and the '
               'exported proof has been accepted by nanoda, con-leche and con-ron, and by Lean\'s own kernel in its default and paranoid '
               'modes. lean4lean accepts every module. A sandboxed rebuild on a separate machine produced an export identical to the '
               'published one.')
ST_ONGOING = (f'Andrew Sutherland\'s verification page at MIT keeps the full, live list of independent checks: '
              f'<a href="{DREW}">math.mit.edu/~drew/grh</a>.')
ST_SCOPE = ('The proof covers Mathlib\'s <code>RiemannHypothesis</code> and GRH for Dirichlet L-functions, all moduli and characters. '
            'The theorems are stated without hypotheses.')
ST_ARCHIVE = (f'The source viewer shows the original archive as released: commit <code>{LEAN_SHA[:8]}</code> of the '
              f'<a href="{LEAN_REPO}">community mirror</a>, an unchanged copy of the {TOTAL_FILES:,}-file archive. The community '
              'repository removes unused files; at commit 6866a9c6 (24 Nov 2026, 13:39 UTC) it had 60,156 .lean files.')
ST_ARCHIVE_SHORT = 'This is the original archive as released (175,187 files); the community repository removes unused files and had 60,156 at commit 6866a9c6 (24 Nov 2026).'
RUBINSTEIN = 'https://mrubinst.github.io/grh-lean-verification/'
ST_SOURCES = [('Joint statement by the Lean FRO and the Mathlib Initiative (21 Nov 2026)', STMT),
              ("Levent Alpöge's note (20 Nov 2026)", NOTE),
              ("Andrew Sutherland's verification page, MIT", DREW),
              ("Michael Rubinstein's check, Waterloo", RUBINSTEIN),
              ("Mathlib's RiemannHypothesis", MATHLIB_RH),
              (f'The Lean source as released (community mirror, commit {LEAN_SHA[:8]})', f'{LEAN_REPO}/tree/{LEAN_SHA}')]
STATUS_BLOCK = {'as_of': STATUS_AS_OF, 'short': ST_SHORT, 'cert': ST_CERT, 'meta': ST_META, 'chip': ST_CHIP,
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
# the same for clusters (scripts/site/cluster_slugs_history.json): a renamed cluster's old /cluster/<id>-<old>/ 301s
# to its current path
CSLUG_F = os.path.join(HERE, 'cluster_slugs_history.json')
CSLUG_HIST = json.load(open(CSLUG_F)) if os.path.exists(CSLUG_F) else {}
for k in CL:
    if CSLUG[k] not in CSLUG_HIST.setdefault(k, []):
        CSLUG_HIST[k].append(CSLUG[k])
open(CSLUG_F, 'w').write('{\n' + ',\n'.join(f'{json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}' for k, v in sorted(CSLUG_HIST.items())) + '\n}\n')
COLD = {f'/cluster/{k}-{s}/': CPATH[k] for k, ss in CSLUG_HIST.items() if k in CPATH for s in ss if s != CSLUG[k]}
assert not set(COLD) & set(CPATH.values()), 'an old cluster path is also a current one'
# overview.json is what the map needs for first paint. Field notes: 's' is the URL slug (page = /cluster/<id>-<s>/,
# /theme/<id>-<s>/); 'uses' are cluster numbers (k0677 -> 677; the app turns them back into ids); 'ck': 1 marks a cluster whose
# name was checked against its code (data/core-names.yaml); search words
# ('w') and folder labels ('fl', kept here only for unnamed clusters) live in words.json, loaded after first paint. Dropped as unused by the app: conf, coh, lines, core.
overview = {
    'updated': STATE.get('data:', [None, today])[1],   # the date the data last changed (checked at DATA_V below), not the build date
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
        **({'ck': 1} if n.get('checked') else {}),
        'n': len(c['files']), 'uses': [int(u[1:]) for u in uses[k]], 'd': dist.get(k), 'fi': feeds[k],
        **({'r': min(nroutes[k], 100)} if nroutes.get(k, 1) > 1 else {}),
        'x': r2(pos_c[k][0]), 'y': r2(pos_c[k][1]),
    })
WORDS = {'w': {k: c['words'][:6] for k, c in CL.items()}, 'fl': {k: folder_label(c['folders']) for k in CL}}

# ---------- guides (design: research/plans/guides-design.md, sections 1-4 and 6). data/guides.yaml lists the outside
# guides; data/guide-refs/<id>.tsv (cluster, page, page_url, basis, evidence; one row per cluster per page) says which
# clusters each one cites and on which pages. A guide is shown for a cluster only if it has a row there (hand-written rows
# have a basis starting 'manual-' and are kept by scripts/guides/match_guides.py on rerun); the 'clusters' list in
# guides.yaml is used only for a guide with no TSV at all. Only guides with page: true appear on the map (node boxes,
# hovers, ?guide=); a page: false guide is a line on /guides/ with its node count. A page that is a Markdown file of
# the guide's repository (Adriazola's audit/*.md) is an "audit note": listed apart from the PDF pages, by its file name
# without .md, underscores as spaces. Both schemas are read: the new one (author: {name, home, photo, photo_source},
# posted_at: {url, date}, status checked | explains, slug, page, order, licence, host_copy, versions) and the first one
# (author as a string or {value, unconfirmed}, url, date, status verified | explains-only). Photos: author.photo names a
# file in research/guides/photos-src/ (only its file name is used); the build writes 48 and 96 px WebP copies to
# site/guides/photos/<slug>-48.webp and -96.webp; no photo: an initials badge. For tests only, RH_GUIDES_YAML,
# RH_GUIDE_REFS and RH_GUIDE_PHOTOS point the build at fixtures (research/guides/fixtures/).
GUIDES_Y = os.environ.get('RH_GUIDES_YAML') or os.path.join(REPO, 'data', 'guides.yaml')
GREFS_D = os.environ.get('RH_GUIDE_REFS') or os.path.join(REPO, 'data', 'guide-refs')
GPHOTO_SRC = os.environ.get('RH_GUIDE_PHOTOS') or os.path.join(ROOT, 'research', 'guides', 'photos-src')
GPHOTO_OUT = os.path.join(OUT, 'guides', 'photos')
GUIDES = yaml.safe_load(open(GUIDES_Y, encoding='utf-8'))['guides']
GUIDES = [g for g in GUIDES if g.get('listed', True) is not False]   # listed: false (with dropped_note): kept in guides.yaml, skipped everywhere (hub, pages, sitemap, refs, photos)
G_STATUS_OF = {'verified': 'checked', 'checked': 'checked', 'explains-only': 'explains', 'explains': 'explains'}
G_ROLE = {'academic': 0, 'university': 0, 'named': 1, 'person': 1, 'organisation': 2, 'organization': 2, 'org': 2, 'unnamed': 3}
def gfield(g, k):   # (value, confirmed)
    v = g.get(k)
    return (v.get('value'), not v.get('unconfirmed')) if isinstance(v, dict) and 'value' in v else (v, True)
def _gdate(v):
    try:
        return datetime.date.fromisoformat(str(v)[:10])
    except (TypeError, ValueError):
        return None
def _host(u):
    h = re.sub(r'^https?://', '', u or '').split('/')[0]
    return h[4:] if h.startswith('www.') else h
def _initials(name):
    ws = [w for w in re.split(r'[\s\-]+', re.sub(r'\(.*?\)', '', name or '')) if w[:1].isalpha()]
    return ((ws[0][0] + (ws[-1][0] if len(ws) > 1 else '')) if ws else '?').upper()
def _gsrc(u, fb=None):   # an ai_statement 'url' ('https://… (page 2)', or only 'PDF page 6') -> (address, location note)
    m = re.search(r'https?://[^\s)]+', str(u or ''))
    rest = re.sub(r'https?://[^\s)]+', '', str(u or '')).strip()
    rest = rest[1:-1].strip() if rest.startswith('(') and rest.endswith(')') else rest
    return (m.group(0) if m else fb), rest or None
def _gai(g):   # ai_statement -> {'src': 'author' | 'repo', 'quote', 'url', 'loc', 'also': [(quote, url, loc)]}; None: no label
    s = g.get('ai_statement')
    if not isinstance(s, dict) or not s.get('quote'):
        return None
    url, loc = _gsrc(s.get('url'))
    assert url, f'guides.yaml {g.get("id")}: ai_statement needs a url'
    also = [(' '.join(str(x['quote']).split()), *_gsrc(x.get('url'), url)) for x in (s.get('also') or []) if isinstance(x, dict) and x.get('quote')]
    return {'src': 'repo' if s.get('source') == 'repository-history' else 'author', 'quote': ' '.join(str(s['quote']).split()),
            'url': url, 'loc': loc, 'also': also}
def gnorm(g, i):
    gid = g.get('id')
    a = g.get('author')
    if isinstance(a, dict) and 'name' in a:
        name, aok, home, photo, psrc = a.get('name'), not a.get('unconfirmed'), a.get('home'), a.get('photo'), a.get('photo_source')
    else:
        (name, aok), home, photo, psrc = gfield(g, 'author'), None, None, None
    title, tok = gfield(g, 'guide_title') if g.get('guide_title') else gfield(g, 'title')   # guide_title: the guide's own title, where the page's differs
    pa = g.get('posted_at') if isinstance(g.get('posted_at'), dict) else {}
    url, uok = gfield(pa, 'url') if pa.get('url') else gfield(g, 'url')
    date, dok = gfield(pa, 'date') if pa.get('date') else gfield(g, 'date')
    assert title and url and uok, f'guides.yaml {gid}: needs a title and a confirmed url'
    st = G_STATUS_OF.get(g.get('status'))
    assert st, f'guides.yaml {gid}: status must be one of {sorted(G_STATUS_OF)}'
    slug_ = g.get('slug') or None
    assert not slug_ or re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug_), f'guides.yaml {gid}: slug {slug_!r} must be lower-case words and hyphens'
    vers = [v for v in (g.get('versions') or []) if isinstance(v, dict)]
    ph2, ph2src = (a.get('photo_also'), a.get('photo_source_also')) if isinstance(a, dict) else (None, None)   # a second logo (joint statement)
    return {'photo_also': ph2, 'photo_source_also': ph2src, 'home_also': a.get('home_also') if isinstance(a, dict) else None,'id': gid, 'i': i, 'slug': slug_, 'page': bool(g.get('page')) and bool(slug_),
            'name': name if name and aok else None, 'home': home, 'photo': photo, 'photo_source': psrc,
            'title': title + ('' if tok else ' (title not confirmed)'), 'url': url, 'date': _gdate(date) if dok else None,
            'type': gfield(g, 'type')[0] if gfield(g, 'type')[1] else None, 'format': g.get('format'),
            'licence': g.get('licence') or g.get('license'), 'host_copy': bool(g.get('host_copy')), 'versions': vers,
            'status': st, 'quote': g.get('status_quote'), 'order': g.get('order'),
            # cite_as: the short name in "cited on Jaswal, p. 12" (N3); default the last word of the author's name
            'cite_as': str(g.get('cite_as') or (name.split()[-1] if name and aok else title.split(':')[0][:30])),
            'role': (a.get('order_group') if isinstance(a, dict) else None) or g.get('role'),
            'photo_crop': a.get('photo_crop') if isinstance(a, dict) else None,
            'companion_reading': g.get('companion_reading'),
            'mapping_note': g.get('mapping_note'),
            'ai': _gai(g),
            'clusters': [k for k in (g.get('clusters') or []) if k in CL]}
GD = [gnorm(g, i) for i, g in enumerate(GUIDES)]
assert len({g['id'] for g in GD}) == len(GD), 'guides.yaml: two guides with the same id'
assert len({g['slug'] for g in GD if g['slug']}) == len([g for g in GD if g['slug']]), 'guides.yaml: two guides with the same slug'
# hub order: 'order' where given; else role (academic, named, organisation, unnamed), newest first within each
def _gkey(g):
    role = g['role'] - 1 if isinstance(g['role'], int) else G_ROLE.get(str(g['role'] or '').lower(), 1 if g['name'] else 3)   # order_group 1-3
    return (g['order'] if isinstance(g['order'], (int, float)) else 10**6, role, -(g['date'] or datetime.date.min).toordinal(), g['id'])
GD.sort(key=_gkey)
for i, g in enumerate(GD):
    g['i'] = i
# guide-refs: cluster -> pages, per guide. A page is a PDF page number or one web page of a guide site
def _pkey(p):
    return (0, int(p), '') if str(p).isdigit() else (1, 0, str(p))
def _glabel(g, p):   # a guide-refs 'page' -> (is an audit note, the label shown)
    if p.lower().endswith('.md') and ' ' not in p and g.get('format') == 'pdf':   # an audit note (a PDF guide's repository Markdown file): file name without .md, underscores as spaces
        return True, p.rstrip('/').rsplit('/', 1)[-1][:-3].replace('_', ' ').strip()
    m = re.fullmatch(r'(?:p\.?\s*)?(\d+)', p)
    if m:                            # a PDF page: 'p. 44' or '44'
        p = m.group(1)
    elif re.match(r'https?://', p):  # a web guide's page given as its address: its last path segment, or the address
        seg = [x for x in re.sub(r'[?#].*$', '', p).split('/')[3:] if x]
        p = re.sub(r'^https?://(www\.)?', '', p).rstrip('/') if p.rstrip('/') == g['url'].rstrip('/') or not seg else seg[-1].removesuffix('.html')
        if len(p) > 40 and '/' in p:   # a long address: its host only
            p = p.split('/', 1)[0]
    elif '/' in p and ' ' not in p:  # a path in a repository or site: its last part
        p = p.rstrip('/').rsplit('/', 1)[-1]
    return False, p
G_REFS_SEEN = []
for g in GD:
    f = os.path.join(GREFS_D, g['id'] + '.tsv')
    g['refs'] = collections.OrderedDict()
    g['manual'] = []   # hand-written rows: (cluster, evidence)
    g['basis'] = collections.defaultdict(set)   # cluster -> the bases of its rows (shown as 'Found by')
    g['notes'] = collections.defaultdict(list)   # cluster -> [(label, url)]: the guide's repository Markdown files (audit notes)
    g['from_refs'] = os.path.exists(f)
    if not g['from_refs']:
        for k in g['clusters']:
            g['refs'][k] = []
        continue
    G_REFS_SEEN.append(g['id'])
    lines = [l.rstrip('\n').split('\t') for l in open(f, encoding='utf-8') if l.strip()]
    has_hdr = bool(lines) and lines[0][0].strip().lower() == 'cluster'
    hdr = [h.strip().lower() for h in lines[0]] if has_hdr else ['cluster', 'page', 'page_url', 'basis', 'evidence']
    bad = 0
    for row in lines[1:] if has_hdr else lines:
        r = dict(zip(hdr, row))
        k, p, u = r.get('cluster', '').strip(), r.get('page', '').strip(), r.get('page_url', '').strip()
        if k not in CL:
            bad += 1; continue
        pages = g['refs'].setdefault(k, [])
        g['basis'][k].add(r.get('basis', '').strip())
        if r.get('basis', '').strip().startswith('manual-'):
            g['manual'].append((k, r.get('evidence', '').strip()))
        note, p = _glabel(g, p)
        if note:   # an audit note
            if p and not any(x[0] == p for x in g['notes'][k]):
                g['notes'][k].append((p, u if re.match(r'https?://', u) else None))
            continue
        if p and not any(x[0] == p for x in pages):
            pages.append((p, u if re.match(r'https?://', u) else None))
    for k in g['refs']:
        g['refs'][k].sort(key=lambda x: _pkey(x[0]))
        g['notes'][k].sort(key=lambda x: x[0].lower())
    if bad:
        print(f'guide-refs/{g["id"]}.tsv: {bad} rows name no cluster on the map, left out')
def page_groups(pages):   # [(label, url)]: runs of consecutive PDF pages as one range ('p. 30–31', linked to its first page)
    out, run = [], []
    def flush():
        if run:
            a, b = run[0], run[-1]
            out.append((f'p. {a[0]}' if a is b else f'p. {a[0]}–{b[0]}', a[1]))
            run.clear()
    for p, u in pages:
        if str(p).isdigit():
            if run and int(p) == int(run[-1][0]) + 1:
                run.append((p, u)); continue
            flush(); run.append((p, u))
        else:
            flush(); out.append((p if len(p) <= 40 else p[:39] + '…', u))
    flush()
    return out
# host copies (design section 2): host_copy: true and a pinned file, the last version with 'local' (a path under the
# project root; else research/guides/sources/<id>/<version>.pdf), whose md5 matches where one is given. Served as
# /guides/<slug>/files/<slug>-v<N>.pdf (or <slug>-<date>.pdf for a version with a longer label). Page links that point
# at the same file in a GitHub blob viewer (which ignores #page=N) are sent to our copy instead.
def vlabel(v):   # 'v2' or 2 -> '2'; a longer label ('manuscript/main.pdf (225 pages)') as it is
    return re.sub(r'^[vV](?=\d)', '', str(v.get('version')).strip())
def _glocal(g, v):
    for f in ([v['local']] if v.get('local') else []) + [os.path.join('research', 'guides', 'sources', g['id'], f'{v.get("version")}.pdf')]:
        if os.path.isfile(os.path.join(ROOT, f)):
            if v.get('md5') and hashlib.md5(open(os.path.join(ROOT, f), 'rb').read()).hexdigest() != v['md5']:
                print(f'guides: {f} does not match the md5 of {g["id"]} version {v.get("version")}: not served'); continue
            return f
for g in GD:
    g['copy_plan'] = None
    if not (g['host_copy'] and g['page']):
        continue
    v = next(({**v, 'local': f} for v in reversed(g['versions']) for f in [_glocal(g, v)] if f), None)
    if not v:
        print(f'guides: {g["id"]} has host_copy: true but no local pinned file: link to the original only'); continue
    l = vlabel(v)
    tag = f'v{l}' if re.fullmatch(r'[\d.]+', l) else (str(_gdate(v.get('date')) or '') or re.sub(r'[^a-z0-9.]+', '-', l.lower()).strip('-'))
    g['copy_plan'] = (f'{g["slug"]}-{tag}{os.path.splitext(v["local"])[1]}', v)
    cp = f'/guides/{g["slug"]}/files/{g["copy_plan"][0]}'
    blob = lambda u: re.sub(r'/blob/[0-9a-f]{7,40}/', '/blob/*/', re.sub(r'#.*$', '', u or ''))
    vu = v.get('file_url') or v.get('url')   # file_url: the PDF the page links point at, where 'url' is a tree or release page
    if vu and ('/blob/' in vu or vu.lower().endswith('.pdf')):
        g['fix_url'] = (lambda cp, vu: lambda u: cp + u[u.index('#'):] if u and '#page=' in u and blob(u) == blob(vu) else u)(cp, vu)
        for k, ps in g['refs'].items():
            g['refs'][k] = [(p, g['fix_url'](u)) for p, u in ps]
G_PMAX = 8   # pages listed per guide in a cluster's list; the rest are on the guide's own page ('m': how many more)
G_MAP = [g for g in GD if g['page']]   # the guides on the map (overview 'guides', in hub order); 'oi': index there
for i, g in enumerate(G_MAP):
    g['oi'] = i
for g in GD:   # a guide whose PDF pages sit next to audit notes calls them 'Manuscript p. N'
    g['pdf_word'] = 'Manuscript' if any(g['notes'].values()) else ''
CGUIDES = collections.defaultdict(list)   # cluster -> [{'i': index in overview 'guides', 'p': [[label, url], …], 'm': more, 'n': [[note, url], …]}]
for g in G_MAP:
    for k, pages in g['refs'].items():
        pg = page_groups(pages)
        CGUIDES[k].append({'i': g['oi'], 'p': [[l, u] for l, u in pg[:G_PMAX]], **({'m': len(pg) - G_PMAX} if len(pg) > G_PMAX else {}),
                           **({'n': [[l, u] for l, u in g['notes'][k]]} if g['notes'].get(k) else {})})
# N3 tier 1: works cited on a guide page that covers the cluster, automatic and not checked (data/guide-cited-refs.tsv,
# written by scripts/refs/guide_cited_refs.py; see its header). Shown after the checked and automatic references as
# "Cited by expert guides (automatic, not checked)", GC_CAP works first (most citing guides first), the rest behind
# "Show all". GCITE: cluster -> [{'citation', 'url', 'guides': n, 'on': [(guide, label, url)]}]. The app reads the same
# lists from data/guide-cites.json, fetched only when the section is opened; each cluster file carries only the count
# ('gc'). A citing page of a guide that is not listed is left out (and the work, if no page is left).
GC_T = 'Cited by expert guides (automatic, not checked)'
GC_LABEL = 'Cited on a guide page that covers this node (automatic, not checked)'
GC_NOTE = ('A guide page can cover several clusters, so a work listed here may concern another part of that page. '
           'Checked references, where there are any, are listed above.')
GC_CAP, GC_PMAX = 8, 4   # works shown before "Show all"; citing pages shown per work before "and N more"
GC_F = os.path.join(REPO, 'data', 'guide-cited-refs.tsv')
G_BY_ID = {g['id']: g for g in GD}
G_BY_SLUG = {g['slug']: g for g in GD if g['slug']}
GCITE = collections.defaultdict(list)
_gc_skip = collections.Counter()
if os.path.exists(GC_F):
    with open(GC_F, encoding='utf-8', newline='') as f:
        import csv as _csv
        for r in _csv.DictReader(f, delimiter='\t', quoting=_csv.QUOTE_NONE):
            if r['cluster'] not in CL:
                _gc_skip['cluster not on the map'] += 1; continue
            on, seen = [], set()
            for x in r['cited_on'].split(';'):
                gid, pg, pu = (x.split('|') + ['', ''])[:3]
                g = G_BY_ID.get(gid)
                if not g:
                    _gc_skip['guide not listed'] += 1; continue
                note, lab = _glabel(g, pg)
                lab = f'p. {lab}' if lab.isdigit() else lab
                u = g.get('fix_url', lambda u: u)(pu) if re.match(r'https?://', pu) else None
                if (gid, lab) not in seen:
                    seen.add((gid, lab)); on.append((gid, lab, u))
            if not on:
                continue
            GCITE[r['cluster']].append({'citation': ' '.join(r['citation'].split()), 'url': r['url'] or None,
                                        'guides': len({x[0] for x in on}), 'on': on})
for k in GCITE:
    GCITE[k].sort(key=lambda w: (-w['guides'], -len(w['on']), w['citation'].lower()))
GC_GUIDES = sorted({x[0] for ws in GCITE.values() for w in ws for x in w['on']}, key=lambda i: G_BY_ID[i]['i'])
# the app's copy: g [[short name, the guide's page here or its original]], c {cluster: [[citation, url, [[g index, page label, url], …]], …]}
json.dump({'label': GC_LABEL, 'g': [[G_BY_ID[i]['cite_as'], f'/guides/{G_BY_ID[i]["slug"]}/' if G_BY_ID[i]['page'] else G_BY_ID[i]['url']] for i in GC_GUIDES],
           'c': {k: [[w['citation'], w['url'], [[GC_GUIDES.index(gi), l, u] for gi, l, u in w['on']]] for w in ws] for k, ws in sorted(GCITE.items())}},
          open(os.path.join(OUT, 'data', 'guide-cites.json'), 'w'), separators=(',', ':'), ensure_ascii=False)
print(f'guide-cited references (N3 tier 1, automatic): {sum(map(len, GCITE.values()))} works on {len(GCITE)} clusters, '
      f'{sum(1 for k in GCITE if k not in SPINE)} outside the spine' + (f'; left out: {dict(_gc_skip)}' if _gc_skip else ''))
# photos: 48 px (hover, lists) and 96 px (pages) WebP copies, square, centre crop; stale copies are removed
os.makedirs(GPHOTO_OUT, exist_ok=True)
_gph_keep = set()
def _gphoto(g, photo, base, sfx=''):   # writes the copies; sets g['ph48'+sfx], g['ph96'+sfx]
    src = os.path.join(GPHOTO_SRC, os.path.basename(str(photo)))
    if not os.path.exists(src):
        print(f'guides: photo {photo} for {g["id"]} not found in {GPHOTO_SRC}: initials instead')
        return
    if src.lower().endswith('.svg'):   # a logo: served as it is (small, sharp at any size), both sizes the same file
        svg = open(src, 'rb').read()
        if re.search(rb'(?i)<script|\bon[a-z]+\s*=|javascript:|<foreignObject', svg) or len(svg) > 200_000:
            print(f'guides: {src} has scripts or is over 200 kB: initials instead'); return
        fn = f'{base}.svg'
        dst = os.path.join(GPHOTO_OUT, fn)
        if not os.path.exists(dst) or open(dst, 'rb').read() != svg:
            open(dst, 'wb').write(svg)
        _gph_keep.add(fn)
        g['ph48' + sfx] = g['ph96' + sfx] = f'/guides/photos/{fn}'
        return
    from PIL import Image as _Img, ImageOps as _IOps
    im = _IOps.exif_transpose(_Img.open(src))
    im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
    if g.get('photo_crop'):   # author.photo_crop: [left, top, size] in the original, for a photo where the face is small
        x0, y0, s = (int(v) for v in g['photo_crop'])
        im = im.crop((x0, y0, x0 + s, y0 + s))
    s = min(im.size)
    im = im.crop(((im.width - s) // 2, max(0, (im.height - s) // 3), (im.width - s) // 2 + s, max(0, (im.height - s) // 3) + s))
    im = _Img.frombytes(im.mode, im.size, im.tobytes())   # pixels only: no EXIF, GPS, XMP or comments travel to the copies
    for px in (48, 96):
        fn = f'{base}-{px}.webp'
        b = __import__('io').BytesIO()
        im.resize((px, px), _Img.LANCZOS).save(b, 'WEBP', quality=78, method=6, exif=b'', xmp=b'')
        assert not re.search(rb'EXIF|XMP ', b.getvalue()), f'{fn}: metadata in the copy'
        dst = os.path.join(GPHOTO_OUT, fn)
        if not os.path.exists(dst) or open(dst, 'rb').read() != b.getvalue():
            open(dst, 'wb').write(b.getvalue())
        _gph_keep.add(fn)
        g[f'ph{px}{sfx}'] = f'/guides/photos/{fn}'
for g in GD:
    g['ph48'] = g['ph96'] = g['ph48b'] = g['ph96b'] = None
    g['initials'] = _initials(g['name'] or g['title'])
    if g['photo']:
        _gphoto(g, g['photo'], g['slug'] or g['id'])
    if g['photo_also'] and g['ph48']:   # an organisation's second logo, shown beside the first
        _gphoto(g, g['photo_also'], (g['slug'] or g['id']) + '-2', 'b')
for f in os.listdir(GPHOTO_OUT):
    if f not in _gph_keep:
        os.remove(os.path.join(GPHOTO_OUT, f))
# the app's copy: overview 'guides' (hub order): id, s slug (the ?guide= value), pg 1 if it has a page, a author (null: none named), t title, u original,
# ph 48 px photo, in initials, k cluster numbers; each cluster file lists its guides and their pages ('guides')
overview['guides'] = [{'id': g['id'], 's': g['slug'] or g['id'], **({'pg': 1} if g['page'] else {}), 'a': g['name'], 't': g['title'], 'u': g['url'],
                       'ph': g['ph48'], **({'ph2': g['ph48b']} if g['ph48b'] else {}), 'in': g['initials'],
                       **({'pw': g['pdf_word']} if g['pdf_word'] else {}), **({'ai': g['ai']['src'][0]} if g['ai'] else {}),
                       'k': [int(k[1:]) for k in g['refs']]} for g in G_MAP]
print(f'guides: {len(GD)} ({sum(g["page"] for g in GD)} with a page), refs read for {len(G_REFS_SEEN)}, '
      f'{len(CGUIDES)} clusters cite a guide, {sum(1 for g in GD if g["ph48"])} photos or logos, '
      f'{sum(1 for g in GD if g["ai"])} AI-labelled, {sum(1 for g in GD if not g["refs"])} with 0 nodes')

# ---------- #10: English readings of the core Lean files (spec: research/plans/core-lean-readings-process.md, section 5).
# data/file-lines/<cluster>.yaml, written by scripts/readings/assemble.py from the reviewed drafts: per file the
# module, depth, lines, a one-sentence line, a reading, up to 5 key declarations (name + gloss), blueprint labels, status
# (checked | fixed | cut | pending) and the check. Pending entries are left out everywhere. Shown on one indexable page
# per core cluster, CPATH[k] + 'lean/' (split into part-2/, part-3/… when one page would pass FL_MAX), with the key
# declarations' statements cut from the local source at build time (up to `:=`, as the viewer's lxStatement does); in
# the Lean viewer above the code and as the CodeLens title where no blueprint or atlas title exists (data/lean/<id>
# .json.gz 'r', core clusters only); on the cluster pages and /core/ as a link; and in /api/file-lines/.
FL_DIR = os.path.join(REPO, 'data', 'file-lines')
FL_MAX = 400_000          # bytes of HTML per page (section 5.2); the build fails if a page is over it
FL_FRAME = 40_000         # bytes per page besides the file sections and the contents list: template, head, intro, links
FL_LABEL = 'Checked against the code'
FL_HOW = ('Written by AI from the Lean source at commit 40e56bab; each sentence checked against the code by a second pass.')
FL_BANNED = re.compile(r"\b(?:I|(?i:we|our|us|seems|likely|appears|crucial|elegant|powerful|plays a key role|this file|this module))\b")   # assemble.py's
FL = {}                   # k -> shown entries (not pending), in page order: depth, then module
FL_PEND = collections.Counter()
_fl_src = os.path.join(ROOT, 'src', 'lean', 'src')
_fl_decls_f = os.path.join(os.environ.get('RH_XREF') or os.path.join(ROOT, 'research', 'lean-reader', 'xref'), 'decls.tsv.gz')
def _fl_load():   # a function, so that its names do not leak into the build's globals
    for _f in sorted(glob.glob(os.path.join(FL_DIR, '*.yaml'))):
        _y = yaml.safe_load(open(_f, encoding='utf-8'))
        k = _y['cluster']
        assert os.path.basename(_f) == k + '.yaml' and k in CHECKED, f'{_f}: not a core cluster'
        assert str(_y['source_commit']) == LEAN_SHA[:8], f'{_f}: source_commit {_y["source_commit"]} is not {LEAN_SHA[:8]}'
        es = []
        for e in _y['files']:
            m = e['module']
            assert mod_cl.get(m) == k, f'{_f}: {m} is not a file of {k} on the map (mod_cl: {mod_cl.get(m)})'
            assert e['status'] in ('checked', 'fixed', 'cut', 'pending'), f'{_f}: {m}: status {e["status"]}'
            assert e['depth'] == fdist.get(m), f'{_f}: {m}: depth {e["depth"]}, the map says {fdist.get(m)}'
            if e['status'] == 'pending':
                FL_PEND[k] += 1
                continue
            for fld in ('line', 'reading'):
                b = FL_BANNED.search(e.get(fld) or '')
                assert not b, f'{_f}: {m}: {fld} has {b.group()!r} (first person or a banned word)'
            assert len(e['line']) <= 140 and len(e.get('reading') or '') <= 700, f'{_f}: {m}: line or reading over its limit'
            assert len(e['key_decls'] or []) <= 5, f'{_f}: {m}: more than 5 key_decls'
            for x in e['key_decls'] or []:
                b = FL_BANNED.search(x['gloss'])
                assert not b, f'{_f}: {m}: gloss of {x["name"]} has {b.group()!r}'
            es.append(e)
        assert len({e['module'] for e in es}) == len(es), f'{_f}: a module listed twice'
        FL[k] = sorted(es, key=lambda e: (e['depth'], e['module']))
_fl_load()
if FL:
    if os.path.exists(_fl_decls_f):   # section 5.7: every key_decls name is a declaration of its module
        import gzip as _gz, csv as _csv
        _want = {e['module'] for es in FL.values() for e in es}
        _dn = collections.defaultdict(set)
        with _gz.open(_fl_decls_f, 'rt', encoding='utf-8') as _fh:
            for _r in _csv.DictReader(_fh, delimiter='\t'):
                if _r['module'] in _want:
                    _dn[_r['module']].add(_r['name'])
        _bad = [(e['module'], x['name']) for es in FL.values() for e in es for x in e['key_decls'] or [] if x['name'] not in _dn[e['module']]]
        assert not _bad, f'file-lines: key_decls not in decls.tsv.gz: {_bad[:5]}'
        del _dn
    else:
        print(f'WARNING file-lines: no {_fl_decls_f}, key_decls names not checked against the declaration index')
    print(f'file-lines: {sum(map(len, FL.values()))} files with readings in {len(FL)} core clusters'
          + (f', {sum(FL_PEND.values())} pending left out ({", ".join(f"{k} {n}" for k, n in sorted(FL_PEND.items()))})' if FL_PEND else ''))
# statements of the key declarations, cut from the local source: the command that declares the name (scripts/xref/
# leansrc.py), up to its first top-level `:=`, `where` or `|` (an inductive's constructors); a def or abbrev under 8
# lines whole, and a structure, class or inductive under 16 lines whole (their fields are their content). A name that
# is no command of its own (a structure field) shows its line from decls.tsv. Same rule as lxStmtEnd / lxStatement in app.js.
sys.path.insert(0, os.path.join(REPO, 'scripts', 'xref'))
import leansrc as _leansrc
def _fl_stmt_end(lines, a, b, kind):
    depth = 0
    for n in range(a, min(b, len(lines)) + 1):
        L = lines[n - 1]
        for i, ch in enumerate(L):
            if ch in '([{⦃⟨':
                depth += 1
            elif ch in ')]}⦄⟩':
                depth = max(0, depth - 1)
            elif not depth:
                if ch == ':' and L[i + 1:i + 2] == '=':
                    return n, i
                if ch == '|' and kind == 'inductive' and (not i or L[i - 1] == ' '):
                    return n, i
                if ch == 'w' and L.startswith('where', i) and not re.match(r"[\w'.]", L[i - 1] if i else ' ') and not re.match(r"[\w']", L[i + 5:i + 6] or ' '):
                    return n, i
    return None
FL_STMT_MAX = 40   # lines of one statement shown on the page; longer ones end with a note and the link to the file
def fl_statements(m, names):
    """{name: (first line number, [lines])} for the names declared in module m."""
    text = open(os.path.join(_fl_src, *m.split('.')) + '.lean', encoding='utf-8', errors='replace').read()
    lines = text.split('\n')
    cmds = {c.full: c for c in _leansrc.parse(text)['cmds'] if getattr(c, 'full', None)}
    out = {}
    for nm in names:
        c = cmds.get(nm)
        if not c:
            continue
        cl = c.text.split('\n')
        k = len(cl)
        while k > 1 and not cl[k - 1].strip():
            k -= 1
        a, b = c.line, c.line + k - 1
        se = _fl_stmt_end(lines, a, b, c.kind)
        whole = (c.kind in ('def', 'abbrev') and b - a < 8) or (c.kind in ('structure', 'class', 'inductive') and b - a < 16)
        if not se or whole:
            st = lines[a - 1:b]
        else:
            st = lines[a - 1:se[0]]
            st[-1] = st[-1][:se[1]].rstrip() + (' := …' if lines[se[0] - 1].startswith(':=', se[1]) else '')
        out[nm] = (a, st)
    return out
FL_DLINE = {}   # (module, name) -> line, for names that are not commands (fields): from decls.tsv
if FL and os.path.exists(_fl_decls_f):
    _want = {(e['module'], x['name']) for es in FL.values() for e in es for x in e['key_decls'] or []}
    with _gz.open(_fl_decls_f, 'rt', encoding='utf-8') as _fh:
        for _r in _csv.DictReader(_fh, delimiter='\t'):
            if (_r['module'], _r['name']) in _want:
                FL_DLINE[(_r['module'], _r['name'])] = int(_r['line'])
# blueprint labels -> (source name, title, url): Merten's statements (their file in the blueprint repository) and
# Naskręcki's atlas entries (the atlas page)
FL_BP = {}
_xd = os.path.dirname(_fl_decls_f)
if os.path.exists(os.path.join(_xd, 'merten.json')):
    for s in json.load(open(os.path.join(_xd, 'merten.json')))['statements']:
        FL_BP['merten:' + s['label']] = ("Merten's blueprint", s.get('title') or s['label'], s.get('url'))
    for s in json.load(open(os.path.join(_xd, 'naskrecki.json')))['declarations']:
        FL_BP['naskrecki:' + s['label']] = ("Naskręcki's atlas", s.get('title') or s['label'], s.get('atlas') or s.get('url'))
_E = _html.escape
def fl_anchor(m):   # the file's id on its /lean/ page: the module name itself
    return m
def fl_short(name):
    return name.rsplit('.', 1)[-1]
def fl_pre(a, st):
    return ('<pre class="lst"><code>' + ''.join(f'<span class="l"><span class="n">{a + i}</span>{_E(L) or ' '}</span>' for i, L in enumerate(st[:FL_STMT_MAX]))
            + (f'<span class="l more">… {len(st) - FL_STMT_MAX} more lines of the statement in the full file</span>' if len(st) > FL_STMT_MAX else '')
            + '</code></pre>')
def fl_section(k, e):
    """(HTML, Markdown) of one file's entry on its cluster's /lean/ page."""
    m = e['module']
    st = fl_statements(m, [x['name'] for x in e['key_decls'] or []])
    fh = f'/file/{m}'
    meta = [f'{"★ Main" if e["depth"] == 0 else str(e["depth"]) + " import " + ("step" if e["depth"] == 1 else "steps") + " from Main"}',
            f'{e["lines"]:,} lines']
    lbl = f' · <span class="ck">{FL_LABEL}</span>' if e['status'] in ('checked', 'fixed') else ''
    h = [f'<section class="lf" id="{_E(fl_anchor(m))}"><h3><a href="{_E(fh)}"><code>{_E(m)}</code></a></h3>',
         f'<p class="meta">{" · ".join(meta)}{lbl}</p>']
    md = [f'### {m}', '', f'{" · ".join(meta)}' + (f' · {FL_LABEL}' if lbl else '') + f' · [Open in the Lean viewer]({SITE_URL}{fh})', '']
    if e['status'] != 'cut':
        h.append(f'<p class="lfl">{_E(e["line"])}</p>')
        md += [f'**{e["line"]}**', '']
        if e.get('reading'):
            h.append(f'<p>{_E(e["reading"])}</p>')
            md += [e['reading'], '']
    kd = e['key_decls'] or []
    if kd:
        h.append(f'<h4>Key declarations</h4>')
        md += ['Key declarations:', '']
        for x in kd:
            nm, s = x['name'], fl_short(x['name'])
            h.append(f'<div class="lkd"><p><a href="{_E(fh)}#{_E(s)}"><code>{_E(nm)}</code></a>'
                     + (f': {_E(x["gloss"])}' if e['status'] != 'cut' else '') + '</p>')
            md.append(f'- `{nm}`' + (f': {x["gloss"]}' if e['status'] != 'cut' else ''))
            if nm in st:
                a, lines = st[nm]
            elif (m, nm) in FL_DLINE:
                a = FL_DLINE[(m, nm)]
                lines = [open(os.path.join(_fl_src, *m.split('.')) + '.lean', encoding='utf-8', errors='replace').read().split('\n')[a - 1]]
            else:
                a, lines = None, []
            if lines:
                h.append(fl_pre(a, lines))
                md += ['', '  ```lean'] + [f'  {L}' for L in lines[:FL_STMT_MAX]] + (['  …'] if len(lines) > FL_STMT_MAX else []) + ['  ```']
            h.append('</div>')
        md.append('')
    bps = [FL_BP.get(b) for b in e.get('blueprint') or []]
    bps = [b for b in bps if b]
    if bps:
        h.append('<p class="meta lbp">Blueprint: ' + ' · '.join(
            (f'<a href="{_E(u)}">{_E(t)}</a>' if u else _E(t)) + f' <span class="src">({_E(src)})</span>' for src, t, u in bps) + '</p>')
        md += ['Blueprint: ' + ' · '.join((f'[{t}]({u})' if u else t) + f' ({src})' for src, t, u in bps), '']
    h.append(f'<p class="lfa"><a href="{_E(fh)}">Show the full file ›</a><a class="top" href="#contents">Contents ↑</a></p></section>')
    return ''.join(h), '\n'.join(md)
SITE_URL = 'https://riemannhypothesissolved.com'
# per cluster: the sections, split into parts of about equal size, each under the budget; FL_PART[(k, module)] = part index (0: lean/)
FL_SEC, FL_PARTS, FL_PART = {}, {}, {}
def fl_ppath(k, i):
    return CPATH[k] + 'lean/' + (f'part-{i + 1}/' if i else '')
def _fl_split():   # a function, so that its names do not leak into the build's globals
    for k, es in FL.items():
        secs = [(e, *fl_section(k, e)) for e in es]
        # every part repeats the full contents list (about 2 module names and the line per file)
        budget = FL_MAX - FL_FRAME - sum(len((2 * e['module'] + e['line']).encode()) + 160 for e in es)
        tot = sum(len(x[1].encode()) for x in secs)
        target = min(budget, tot / -(-tot // budget) * 1.02)   # ceil(tot / budget) parts of about equal size
        parts, cur, size = [], [], 0
        for s in secs:
            n = len(s[1].encode())
            if cur and size + n > target:
                parts.append(cur); cur, size = [], 0
            cur.append(s); size += n
        if cur:
            parts.append(cur)
        FL_SEC[k], FL_PARTS[k] = secs, parts
        for i, p in enumerate(parts):
            for s in p:
                FL_PART[(k, s[0]['module'])] = i
_fl_split()

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
        'source': shown_source(k),   # automatic (AI namer) book reference, unchecked; None where checked ones replace it
        **({'refs': CHECKED_REFS[k]['refs'], 'refs_checked': CHECKED_REFS[k]['date']} if k in CHECKED_REFS else {}),
        **({'gc': len(GCITE[k])} if k in GCITE else {}),   # N3: works cited by guides (data/guide-cites.json has them)
        'hints': HINTS.get(k, []), 'uses': uses[k], 'used_by': sorted(used_by[k]),
        'dist': dist.get(k), 'core': core_cl.get(k, []), 'lines': c['lines'], 'files': files,
        **({'checked': True, 'evidence': [{'m': m, 'decl': dc, 'says': w} for m, dc, w in evidence(k)]} if k in CHECKED else {}),
        **({'guides': CGUIDES[k]} if k in CGUIDES else {}),   # [{'i': index in overview 'guides', 'p': [[page label, url], …]}]
        **({'rl': len(FL[k])} if FL.get(k) else {}),   # #10: files with an English reading, on CPATH[k] + 'lean/'
    }
    json.dump(detail, open(os.path.join(OUT, 'data', 'c', k + '.json'), 'w'), separators=(',', ':'))

# ---------- Lean viewer data (design: research/plans/lean-structure-design.md, "Viewer layout DECIDED"). One file per
# cluster, data/lean/<id>.json, fetched when the viewer opens; data/lean-hover.json (declaration count and the top 3
# per cluster, for the map hover) is fetched after first paint. Built from the P4 cross-reference run
# (repo/scripts/xref/full_run.py, then derive.py; output in research/lean-reader/xref/full/, or $RH_XREF/full/), the
# blueprint matches (blueprint_matches.tsv, merten.json, naskrecki.json in the same xref folder) and the guides' full
# citation lists (data/guide-decls.tsv.gz, written by scripts/guides/match_guides.py --decls=). No P4 output: the viewer
# data is skipped and the app shows the source without declarations. Only unique matches are used ("resolved from source").
# data/lean/<id>.json.gz (stored gzipped; the app fetches the bytes and unzips them with DecompressionStream, so it does
# not depend on how the host labels .gz files):
#   d  folders; x this cluster's files as [folder index, last part], in explorer order (units closest to Main first,
#      each followed by its helpers, depth-first along the fold tree)
#   ns namespaces of this cluster's declarations (a name is ns[i] + '.' + short name)
#   f  per file: [parent file index (-1: a unit head), kind (u unit, h helper, w wrapper), steps from Main (null:
#      none), importers (count), declarations, name links, cited by]
#      declaration: [ns index (-1: none), short name, kind, start line, end line, used, guides, title, chain] (the
#        last two left out when 0). used: distinct declarations in the proof that name it (P4); guides: distinct
#        guides on the map that cite it; title: [English title, 'b' Merten's blueprint | 'a' Naskręcki's atlas,
#        label] or 0; chain: 1 if reached from Main's declarations through resolved uses. The statement's end (`:=`)
#        is found by the app in the source.
#      name links: [targets in this node, overrides]; overrides {token: target | {line: target}}. A target >= 0 is
#        t[target]; a target < 0 is a declaration in another node, e[-target - 1] in the lazy file
#      cited by: [[guide index in overview 'guides', page label, url, short declaration name or '']]
#   t  link targets in this node: [file index, declaration index]
# data/lean/x/<id>.json.gz, fetched only when a name in another node is hovered or clicked, or the "Imports and used
# by" panel opens:
#   d, x  modules elsewhere (as above); ns their namespaces
#   e  [x index, ns index, short name, kind, start line, end line] per link target in another node
#   by per file, up to 5 importers: >= 0 a file of this node, < 0 x[-i - 1]
XREF_D = os.path.join(os.environ.get('RH_XREF') or os.path.join(ROOT, 'research', 'lean-reader', 'xref'))
LV_OUT = os.path.join(OUT, 'data', 'lean')
os.makedirs(os.path.join(LV_OUT, 'x'), exist_ok=True)
for f in glob.glob(os.path.join(LV_OUT, '*.json')) + glob.glob(os.path.join(LV_OUT, '*.json.gz')) + glob.glob(os.path.join(LV_OUT, 'x', '*.json.gz')):
    os.remove(f)
LEAN_HOVER = None
if os.path.exists(os.path.join(OUT, 'data', 'lean-hover.json')):
    os.remove(os.path.join(OUT, 'data', 'lean-hover.json'))
# name links, compressed: per file the list of targets its names resolve to, plus overrides. The app links a token to
# the one target in that list whose full name is the token or ends with '.' + token (else it drops the token's last
# dotted part, as Lean reads a projection, and tries again); lvMatch() in app.js, keep in step. A token for which that
# rule gives another answer, or none, or whose target has a short name that could be a local (not _lv_safe), or that
# resolves differently on different lines, is written out: overrides {token: t index | {line: t index}}.
def _lv_safe(short):
    return len(short) >= 8 or (len(short) >= 4 and bool(re.search(r'[_0-9]|.[A-Z]', short)))
def _lv_index(cand, full):   # every dotted suffix of each candidate's full name -> candidates
    ix = collections.defaultdict(list)
    for c in cand:
        p = full[c].split('.')
        for i in range(len(p)):
            ix['.'.join(p[i:])].append(c)
    return ix
def _lv_match(tok, ix):
    s = tok
    while True:
        hits = ix.get(s, ())
        if len(hits) == 1:
            return hits[0]
        if hits or '.' not in s:
            return None
        s = s.rsplit('.', 1)[0]
def _lv_links(links, full):   # targets >= 0 are in this node (full names known); < 0 elsewhere: always written out
    cand = sorted({t for v in links.values() for t in ([v] if isinstance(v, int) else v.values()) if t >= 0})
    ix = _lv_index(cand, full)
    over = {}
    for tok, v in links.items():
        if isinstance(v, int) and v >= 0 and _lv_safe(full[v].rsplit('.', 1)[-1]) and _lv_match(tok, ix) == v:
            continue
        over[tok] = v
    return [cand, over] if over else [cand]
def _lean_viewer():   # a function, so that none of its names leak into the build's globals (par, order, …)
    LEAN_HOVER = None
    import gzip, csv
    _t0 = __import__('time').time()
    LVK = {'theorem': 't', 'lemma': 'l', 'def': 'd', 'abbrev': 'a', 'instance': 'i', 'structure': 's', 'class': 'c',
           'inductive': 'n', 'alias': 'A', 'opaque': 'o', 'axiom': 'x', 'irreducible_def': 'd'}
    DSTAT = {}          # (name, module) -> [kind, start, end, stmt_end, flags, used, chain]
    MDECL = collections.defaultdict(list)
    with gzip.open(os.path.join(XREF_D, 'full', 'decl_stats.tsv.gz'), 'rt', encoding='utf-8') as fh:
        next(fh)
        for ln in fh:
            n, m, k, a, b, se, fl, u, ch = ln.rstrip('\n').split('\t')
            if m in mod_cl:
                r = (LVK.get(k, k[:1]), int(a), int(b), int(se), fl, int(u), int(ch))
                DSTAT[(n, m)] = r
                MDECL[m].append(n)
    # English titles from the blueprints (real sources only): Merten's statement title, else Naskręcki's atlas title
    _bt = {}
    _mer = {s['label']: s.get('title') for s in json.load(open(os.path.join(XREF_D, 'merten.json')))['statements']}
    _nas = {s['label']: s.get('title') for s in json.load(open(os.path.join(XREF_D, 'naskrecki.json')))['declarations']}
    # which title, when both name a declaration: a Merten statement about this declaration alone, else the atlas entry
    # (one declaration each), else a Merten statement that covers several declarations
    _rows = [r for r in csv.DictReader(open(os.path.join(XREF_D, 'blueprint_matches.tsv')), delimiter='\t') if r['status'] == 'matched']
    _nper = collections.Counter(r['label'] for r in _rows if r['source'] == 'merten')
    _rank = {}
    for r in _rows:
        t = (_mer if r['source'] == 'merten' else _nas).get(r['label'])
        key = (r['lean_name'], r['module'])
        rk = 2 if r['source'] == 'naskrecki' else 1 if _nper[r['label']] == 1 else 3
        if t and rk < _rank.get(key, 9):
            _rank[key] = rk
            _bt[key] = [t, 'b' if r['source'] == 'merten' else 'a', r['label']]
    # guide citations, unshortened (guide-decls.tsv.gz): per declaration the guides on the map that name it, per file
    # the citations (guide, page, declaration)
    _goi = {g['id']: g for g in G_MAP}
    DGUIDES = collections.defaultdict(set)
    FCITES = collections.defaultdict(list)
    def _gpage(g, k, raw):
        note, l = _glabel(g, raw)
        if note:
            return l, next((u for x, u in g['notes'].get(k, []) if x == l), None)
        url = next((u for x, u in g['refs'].get(k, []) if x == l), None)
        return ('p. ' + l if l.isdigit() else l), url
    with gzip.open(os.path.join(REPO, 'data', 'guide-decls.tsv.gz'), 'rt', encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            g = _goi.get(r['guide'])
            if not g or r['cluster'] not in CL:
                continue
            m = r['module']
            if r['kind'] == 'd':
                if (r['name'], m) not in DSTAT:
                    continue
                DGUIDES[(r['name'], m)].add(g['oi'])
            elif m not in mod_cl:
                continue
            l, u = _gpage(g, r['cluster'], r['page'])
            e = [g['oi'], l, u, r['name'].rsplit('.', 1)[-1] if r['kind'] == 'd' else '']
            if e not in FCITES[m]:
                FCITES[m].append(e)
    _ord = {g['oi']: i for i, g in enumerate(G_MAP)}
    def _pk(e):
        mm = re.match(r'p\. (\d+)', e[1])
        return (e[0], 0 if mm else 1, int(mm.group(1)) if mm else 0, e[1], e[3])
    LEAN_HOVER = {}
    _hsz = []
    for k in CL:
        # explorer order: unit heads by steps from Main (then name), each followed by its helpers along the fold tree
        mems = members[k]
        kids = collections.defaultdict(list)
        heads = []
        for m in mems:
            p = parent.get(m)
            if m in unit_cl or p not in mod_cl or mod_cl.get(p) != k:
                heads.append(m)
            else:
                kids[p].append(m)
        heads.sort(key=lambda m: (fdist.get(m) is None, fdist.get(m) or 0, m.rsplit('.', 1)[-1].lower(), m))
        order, par = [], {}
        def walk(m, pi):
            par[m] = pi
            i = len(order); order.append(m)
            for c in sorted(kids.get(m, []), key=lambda x: (x.rsplit('.', 1)[-1].lower(), x)):
                walk(c, i)
        for h in heads:
            walk(h, -1)
        OWN = {m: i for i, m in enumerate(order)}
        NS, NSI = [], {}       # namespaces of this cluster's declarations (main file)
        XNS, XNSI = [], {}     # namespaces of declarations elsewhere (lazy file)
        XM, XMI = [], {}       # modules elsewhere (lazy file)
        def tab(lst, idx, v):
            if v not in idx:
                idx[v] = len(lst); lst.append(v)
            return idx[v]
        def split(name, lst, idx):
            a, _, b = name.rpartition('.')
            return (tab(lst, idx, a) if a else -1), b
        try:
            REFS = json.load(gzip.open(os.path.join(XREF_D, 'full', 'refs', k + '.json.gz'), 'rt', encoding='utf-8'))
        except FileNotFoundError:
            REFS = {}
        # this cluster's declarations (the link targets inside the node point at them by [file, declaration] index)
        DIDX, DS = {}, []
        allD = []
        for fi_, m in enumerate(order):
            ds = []
            for n in sorted(MDECL.get(m, []), key=lambda n: DSTAT[(n, m)][1]):
                st = DSTAT[(n, m)]
                a, b = split(n, NS, NSI)
                g = len(DGUIDES.get((n, m), ()))
                row = [a, b, st[0], st[1], st[2], st[5], g, _bt.get((n, m), 0), st[6]]
                while len(row) > 6 and not row[-1]:   # trailing zeros (no title, not on the chain) are left out
                    row.pop()
                DIDX[(n, m)] = [fi_, len(ds)]
                ds.append(row)
                allD.append((n, m, st, g, (n, m) in _bt, fi_))
            DS.append(ds)
        T, TI, TF = [], {}, []   # link targets inside the node: [file, declaration]; full names for the matching rule
        E, EI = [], {}           # link targets in other nodes (lazy file); a link to one is written as -(index + 1)
        def ti(tgt, tm):
            key = (tgt, tm)
            if key in DIDX:
                if key not in TI:
                    TI[key] = len(T); T.append(DIDX[key]); TF.append(tgt)
                return TI[key]
            st = DSTAT.get(key)
            if not st:
                return None
            if key not in EI:
                a, b = split(tgt, XNS, XNSI)
                EI[key] = len(E); E.append([tab(XM, XMI, tm), a, b, st[0], st[1], st[2]])
            return -EI[key] - 1
        F, BY = [], []
        for fi_, m in enumerate(order):
            links = {}
            for tok, v in REFS.get(m, {}).items():
                if isinstance(v, list):
                    t = ti(*v)
                    if t is not None:
                        links[tok] = t
                else:
                    per = {l: ti(*x) for l, x in v.items()}
                    per = {l: t for l, t in per.items() if t is not None}
                    if per:
                        links[tok] = per
            links = _lv_links(links, TF)
            by = sorted(importers.get(m, []), key=lambda x: (fdist.get(x) is None, fdist.get(x) or 0, x))
            kd = 'u' if m in unit_cl else ('w' if kind.get(m) == 'wrapper' else 'h')
            F.append([par[m], kd, fdist.get(m), len(by), DS[fi_], links, sorted(FCITES.get(m, []), key=_pk)])
            BY.append([OWN[x] if x in OWN else -tab(XM, XMI, x) - 1 for x in by[:5]])
        def mods(ms):   # [folders, [[folder index, last part]]]
            fd, fdi = [], {}
            return fd, [[tab(fd, fdi, mm.rpartition('.')[0]), mm.rpartition('.')[2]] for mm in ms]
        d1, x1 = mods(order)
        d2, x2 = mods(XM)
        main = {'d': d1, 'x': x1, 'ns': NS, 'f': F, 't': T}
        if FL.get(k):   # #10 readings (core clusters only): r.p the /lean/ page parts; r.f [file index, line, reading, part, [[declaration index, gloss]]]
            rf = []
            for e in FL[k]:
                fi_ = OWN[e['module']]
                gl = [[DIDX[(x['name'], e['module'])][1], x['gloss']] for x in e['key_decls'] or [] if (x['name'], e['module']) in DIDX]
                rf.append([fi_, e['line'] if e['status'] != 'cut' else '', (e.get('reading') or '') if e['status'] != 'cut' else '',
                           FL_PART[(k, e['module'])], gl if e['status'] != 'cut' else []])
            main['r'] = {'p': [fl_ppath(k, i) for i in range(len(FL_PARTS[k]))], 'f': rf}
        lazy = {'d': d2, 'x': x2, 'ns': XNS, 'e': E, 'by': BY}
        for path, obj in ((os.path.join(LV_OUT, k + '.json.gz'), main), (os.path.join(LV_OUT, 'x', k + '.json.gz'), lazy)):
            raw = json.dumps(obj, separators=(',', ':'), ensure_ascii=False).encode()
            open(path, 'wb').write(gzip.compress(raw, 9, mtime=0))
            _hsz.append((k, path.endswith(os.path.join('x', k + '.json.gz')), len(raw), os.path.getsize(path)))
        # the top 3 ("main") declarations (decision 5, simplified 24 Nov): (a) cited by guides or blueprints, more
        # guides first; then (b) on the chain to Main, the file closer to Main first. Ties: theorems and lemmas before
        # definitions, then source order (explorer order, then line). Nothing in (a) or (b): no "main:" list.
        THM = ('t', 'l')
        ca = [x for x in allD if x[3] or x[4]]
        cb = [x for x in allD if not (x[3] or x[4]) and x[2][6]]
        ca.sort(key=lambda x: (-x[3], x[2][0] not in THM, x[5], x[2][1]))
        cb.sort(key=lambda x: (fdist.get(x[1]) if fdist.get(x[1]) is not None else 999, x[2][0] not in THM, x[5], x[2][1]))
        LEAN_HOVER[k] = [len(allD)] + [x[0].rsplit('.', 1)[-1] for x in (ca + cb)[:3]]
    for lazy in (False, True):
        r = sorted(x[2] for x in _hsz if x[1] == lazy); z = sorted(x[3] for x in _hsz if x[1] == lazy)
        print(f'Lean viewer data ({"lazy x/" if lazy else "main"}): {len(z)} files, {sum(z) / 1e6:.1f} MB gzipped '
              f'({sum(r) / 1e6:.1f} MB raw), median {z[len(z) // 2] / 1e3:.0f} kB, max {z[-1] / 1e3:.0f} kB gzipped '
              f'({r[-1] / 1e3:.0f} kB raw)')
    print(f'Lean viewer data built in {__import__("time").time() - _t0:.0f}s')
    json.dump({'k': [LEAN_HOVER.get(c['id'], [0]) for c in overview['clusters']]},
              open(os.path.join(OUT, 'data', 'lean-hover.json'), 'w'), separators=(',', ':'), ensure_ascii=False)
    del DSTAT, MDECL
    return LEAN_HOVER
if not os.path.exists(os.path.join(XREF_D, 'full', 'decl_stats.tsv.gz')):
    print(f'Lean viewer data: no P4 output in {XREF_D}/full, skipped')
else:
    LEAN_HOVER = _lean_viewer()

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
# ---------- share cards: a 1200x630 PNG per cluster (/og/c/<id>.png) and theme (/og/t/<id>.png), the og:image and
# twitter:image of its static page. og_cards.py draws them (Pillow: add --with pillow to the uv run command) in a few
# processes, and only those whose key changed: the key hashes the card's fields, og_cards.py, the fonts and logo.png.
# OG_V, a hash of all keys, versions the image URLs (/og/* is cached for a year); the app reads it as overview 'ogv'.
import hashlib, subprocess, tempfile
try:
    import PIL
except ImportError:
    sys.exit('build_site.py needs Pillow for the share cards: add --with pillow to the uv run command')
OG_PY = os.path.join(HERE, 'og_cards.py')
_ogh = hashlib.sha256()
for f in [OG_PY, os.path.join(OUT, 'logo.png')] + sorted(glob.glob(os.path.join(HERE, 'fonts', '*.ttf'))):
    _ogh.update(open(f, 'rb').read())
OG_RENDER_V = _ogh.hexdigest()
def _fieldof(t):
    f = FIELDS[FIDX[TFIELD[t]]]
    return f['name'], f['hue'], FIELD_L[f['id']]
def _steps_from(d):
    return 'Holds the main theorem' if d == 0 else f'{d} import step{"" if d == 1 else "s"} from the main theorem'
OG_JOBS = []
for k, c in CL.items():
    fname, hue, li = _fieldof(c['theme'])
    d = dist.get(k)
    OG_JOBS.append({'path': f'og/c/{k}.png', 'tag': f'Cluster {k}', 'eyebrow': f'{fname} · {TNAME[c["theme"]]}',
                    'title': NAMES[k]['title'] if k in NAMES else folder_label(c['folders']), 'hue': hue, 'l': li, 'd': d,
                    'route': _steps_from(d) if d is not None else 'Not on an import route from the main theorem'})
for t, th in TH.items():
    fname, hue, li = _fieldof(t)
    ds = [dist[k] for k in th['clusters'] if k in dist]
    d = min(ds) if ds else None
    OG_JOBS.append({'path': f'og/t/{t}.png', 'tag': 'Theme', 'eyebrow': f'{fname} · {len(th["clusters"])} clusters · '
                    f'{sum(fcount[k] for k in th["clusters"]):,} Lean files', 'title': TNAME[t], 'hue': hue, 'l': li, 'd': d,
                    'route': ('Holds the main theorem' if d == 0 else f'Closest cluster: {_steps_from(d)}') if d is not None else ''})
for j in OG_JOBS:
    j['key'] = hashlib.sha256((OG_RENDER_V + json.dumps(j, sort_keys=True, ensure_ascii=False)).encode()).hexdigest()[:20]
OG_V = hashlib.sha256(''.join(j['key'] for j in OG_JOBS).encode()).hexdigest()[:10]
overview['ogv'] = OG_V
with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as _f:
    json.dump({'out': os.path.abspath(OUT), 'jobs': OG_JOBS}, _f)
subprocess.run([sys.executable, '-I', OG_PY, _f.name], check=True)
os.remove(_f.name)
_ogkeep = {os.path.join(OUT, j['path']) for j in OG_JOBS}
for f in glob.glob(os.path.join(OUT, 'og', '*', '*.png')):   # cards of clusters or themes that no longer exist
    if f not in _ogkeep:
        os.remove(f)
def og_url(path):
    return f'{SITE}/{path}?v={OG_V}'

json.dump(WORDS, open(os.path.join(OUT, 'data', 'words.json'), 'w'), separators=(',', ':'))
# G3: each /data/ file is fetched with its own content hash (?v=<hash of that file>), so a build that changes 41 cluster
# files gives 41 new URLs, not ~2,650 (one global ?v= made every /data/ URL new after any change, and Google's renderer
# fetched them all again). overview 'dv': 'f' the shared files' hashes, 'c' the cluster files' hashes, DV_N hex digits
# each, concatenated in the order of overview 'clusters'. overview.json itself is versioned by data-v (OV_V below).
DV_N = 7
def _fh(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:DV_N]
overview['dv'] = {'f': {n: _fh(os.path.join(OUT, 'data', n + '.json')) for n in ('tree', 'words', 'modules', 'guide-cites')
                        + (('lean-hover',) if LEAN_HOVER else ())},
                  'c': ''.join(_fh(os.path.join(OUT, 'data', 'c', c['id'] + '.json')) for c in overview['clusters']),
                  # the Lean viewer files (data/lean/<id>.json), the same way; absent when the P4 data was missing
                  **({'l': ''.join(_fh(os.path.join(LV_OUT, c['id'] + '.json.gz')) for c in overview['clusters']),
                      'lx': ''.join(_fh(os.path.join(LV_OUT, 'x', c['id'] + '.json.gz')) for c in overview['clusters'])} if LEAN_HOVER else {})}
def write_overview():
    json.dump(overview, open(os.path.join(OUT, 'data', 'overview.json'), 'w'), separators=(',', ':'))
write_overview()
print(f'{len(CL)} clusters ({named} named), {len(TH)} themes, {len(mod_cl)} files -> {OUT}')


# ---------- static pages for search engines, sharing and machines
# index.html is the template: <!--head-->…<!--/head--> and <!--prerender-->…<!--/prerender--> are replaced, and the
# asset URLs get content hashes (app.<hash>.js, style.<hash>.css; /data/*?v=…) so _headers can cache them as immutable.
# Every page also gets a Markdown copy next to it (<path>index.md, linked with rel=alternate type=text/markdown).
# Rebuild after editing app.js or style.css: the hashes in the HTML are what bust the long cache.
import html, hashlib, secrets, email.utils
from html.parser import HTMLParser
SITE = 'https://riemannhypothesissolved.com'
TPL = open(os.path.join(OUT, 'index.html')).read()
H = html.escape
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
DATA_FILES = sorted(glob.glob(os.path.join(OUT, 'data', '*.json')) + glob.glob(os.path.join(OUT, 'data', 'c', '*.json'))
                    + glob.glob(os.path.join(OUT, 'data', 'lean', '*.json.gz')) + glob.glob(os.path.join(OUT, 'data', 'lean', 'x', '*.json.gz')))
DATA_V = hfiles(DATA_FILES)
if STATE.get('data:', [None])[0] != chash(DATA_V):   # the data changed (overview 'updated' was the old date): date it today
    overview['updated'] = today
    write_overview()
    DATA_V = hfiles(DATA_FILES)
DATA_DATE = lastmod('data:', DATA_V)   # = overview['updated']
assert DATA_DATE == overview['updated']
OV_V = hfiles([os.path.join(OUT, 'data', 'overview.json')])   # data-v: the version of overview.json alone (G3)
# app.js and style.css (hand-written, in the site repo) are copied to app.<hash>.js and style.<hash>.css, and the pages
# load those: a new file name per change, so no cache (browser or Cloudflare edge) can serve an old copy under a new
# version (a ?v= query once came back stale for ~15 min). _headers caches the hashed names for a year; the plain names
# stay (short cache) for HTML cached before the switch. Older hashed copies are kept ASSET_KEEP_DAYS after their last
# build, so HTML cached from a previous deploy still finds its files.
APP_V, CSS_V = hfiles([os.path.join(OUT, 'app.js')]), hfiles([os.path.join(OUT, 'style.css')])
APP_F, CSS_F = f'app.{APP_V}.js', f'style.{CSS_V}.css'
ASSET_KEEP_DAYS = 30
for src, dst, pat in (('app.js', APP_F, r'app\.[0-9a-f]{10}\.js'), ('style.css', CSS_F, r'style\.[0-9a-f]{10}\.css')):
    shutil.copyfile(os.path.join(OUT, src), os.path.join(OUT, dst))   # also refreshes its mtime: kept while in use
    for f in os.listdir(OUT):
        if re.fullmatch(pat, f) and f != dst and os.path.getmtime(os.path.join(OUT, f)) < datetime.datetime.now().timestamp() - ASSET_KEEP_DAYS * 86400:
            os.remove(os.path.join(OUT, f))
TPL = re.sub(r'<link rel="stylesheet" href="/style(?:\.[0-9a-f]{10})?\.css[^"]*">', f'<link rel="stylesheet" href="/{CSS_F}">', TPL, count=1)
TPL = re.sub(r'<script src="/app(?:\.[0-9a-f]{10})?\.js[^"]*"[^>]*></script>', f'<script src="/{APP_F}" data-v="{OV_V}"></script>', TPL, count=1)
TPL = re.sub(r'Charting [\d,]+ Lean files…', f'Charting {TOTAL_FILES:,} Lean files…', TPL)
TPL = re.sub(r'<a class="status-chip ok" href="/(?:about|status)/" title="[^"]*"(?: aria-label="[^"]*")?>\s*<i></i><span>Lean proof · <b>[^<]*</b></span>(?:<small class="cshort">[^<]*</small>)?',
             f'<a class="status-chip ok" href="/status/" title="{H(ST_META)} How it was checked." aria-label="Lean proof {ST_CHIP}: status of the proof">'
             f'\n    <i></i><span>Lean proof · <b>{ST_CHIP}</b></span><small class="cshort">{ST_CHIP_SHORT}</small>', TPL, count=1)
assert ST_META in html.unescape(TPL), 'status chip not found in the index.html template'
assert f"GH_SHA = '{LEAN_SHA}'" in open(os.path.join(OUT, 'app.js')).read(), 'app.js GH_SHA differs from LEAN_SHA'
# 80b: the source viewer (/file/) serves the files of the proof's last step from this site, /src/<module>.lean, copied
# byte for byte from the local tree (src/lean/src, the archive at LEAN_SHA); every other file still comes from the pinned
# GitHub mirror, which is also the fallback. The set: Main and the spine it imports down to MainConclusion (where
# everyCharacter is proved), plus every file those five import directly, as /core/ "How the last step works" describes.
SRC_SPINE = ['Main', 'Supplements.Kernels.MainTheoremsAll', 'Supplements.Kernels.MainTheoremsCritical',
             'Supplements.Kernels.MainTheorems', 'Development.AutomorphicArithmetic.CharacterBoxes.MainConclusion']
assert all(b in imports[a] for a, b in zip(SRC_SPINE, SRC_SPINE[1:])), 'SRC_SPINE: each file must import the next'
LOCAL_SRC = sorted(set(SRC_SPINE) | {x for m in SRC_SPINE for x in imports[m]})
LEAN_SRC = os.path.join(ROOT, 'src', 'lean', 'src')
os.makedirs(os.path.join(OUT, 'src'), exist_ok=True)
for f in glob.glob(os.path.join(OUT, 'src', '*.lean')):   # only the top-level copies: src/c/ (80a bundles) is left alone
    if os.path.basename(f)[:-5] not in LOCAL_SRC:
        os.remove(f)
for m in LOCAL_SRC:
    shutil.copyfile(os.path.join(LEAN_SRC, *m.split('.')) + '.lean', os.path.join(OUT, 'src', m + '.lean'))
_ls = re.search(r'const LOCAL_SRC = new Set\((\[[^\]]*\])\)', open(os.path.join(OUT, 'app.js')).read())
_app = open(os.path.join(OUT, 'app.js')).read()   # 35b: the app's precision tooltips are the generator's
assert all(f"{p}: '{t}'" in _app for p, t in PREC_TIP.items()), 'app.js PREC_TIP must match the generator'
assert _ls and sorted(json.loads(_ls.group(1).replace("'", '"'))) == LOCAL_SRC, f'app.js LOCAL_SRC must list exactly: {LOCAL_SRC}'
assert f'data-v="{OV_V}"' in TPL and f'href="/{CSS_F}"' in TPL and f'src="/{APP_F}"' in TPL

# ---------- lastmod (state and lastmod() are at the top): a page's date changes only when its title, description or body
# changes; '{{UPDATED}}' in a page becomes that date

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
ARTICLES = {'/learn/', '/route/'}   # pages with Article JSON-LD get og:type article (content pages add theirs below)
def HA(s):   # title and description text in the head: escape only what HTML needs (an apostrophe stays one character)
    return html.escape(s, quote=False).replace('"', '&quot;')
CLARITY_TAG = """<script>
if (location.hostname === "riemannhypothesissolved.com") {
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "zj8viomivf");
}
</script>
"""

def head(path, title, desc, lds, md=True, img=None):
    t, d, u = HA(title), HA(desc), H(SITE + path)
    img, alt = img or (f'{SITE}/og.png?v=2', None)
    return (CLARITY_TAG + (ld({'@graph': lds}) if lds else '') + f'\n<link rel="canonical" href="{u}">\n' + alt_links(path)
            + (f'<link rel="alternate" type="text/markdown" href="{H(mdpath(path))}">\n' if md else '')
            + f'<link rel="alternate" type="application/rss+xml" title="{SITE_NAME} changelog" href="/changelog/feed.xml">\n'
            f'<meta property="og:type" content="{"article" if path in ARTICLES else "website"}">\n'
            f'<meta property="og:site_name" content="{SITE_NAME}">\n<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n<meta property="og:url" content="{u}">\n'
            f'<meta property="og:image" content="{H(img)}">\n<meta property="og:image:width" content="1200">\n'
            + (f'<meta property="og:image:alt" content="{H(alt)}">\n' if alt else '') +
            f'<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:site" content="@RiemannMap">\n'
            f'<meta name="twitter:title" content="{t}">\n<meta name="twitter:description" content="{d}">\n'
            f'<meta name="twitter:image" content="{H(img)}">\n')
SHARE_RE = re.compile(r'<p class="sharebar">.*?</p>| <span class="report">.*?</span>')   # QA23a: the report link is left out too
def share_btn(path, title):   # a Share button (app.js copies the link or opens the phone's share sheet); not part of lastmod
    return (f'<p class="sharebar"><button type="button" class="share" data-share="{H(SITE + path)}" data-title="{H(title)}">'
            '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 15V3m0 0-4 4m4-4 4 4M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7"/></svg>'
            '<span>Share</span></button></p>')
def NAV_KEY(path):   # top bar (owner, 24 Nov): Status · Guides · Timeline · Learn; the section a page belongs to, or ''
    m = re.match(r'/(status|guides|timeline|learn|concept)/', path)
    return ('learn' if m.group(1) == 'concept' else m.group(1)) if m else ''
def page(path, title, desc, route, body, lds=(), priority=.5, md=None, img=None, fm=False):
    """img: (og:image URL, alt text) for this page; default the site card /og.png. fm: title and description come from a
    content page's front matter (data/pages/*.md): over the caps only warns, as that text is reviewed separately."""
    is404 = path.endswith('.html')
    for what, v, cap in (('description', desc, DESC_MAX), ('title', title, TITLE_MAX)):   # 85b, 85d
        if max(len(v), len(HA(v)) if what == 'description' else 0) > cap:
            msg = f'{path}: {what} is {len(v)} characters, over {cap}: {v}'
            assert fm, msg
            print('WARNING (content page, shorten it in research/content/pages):', msg)
    date = lastmod(path, title, desc, SHARE_RE.sub('', body))
    t = TPL
    t = re.sub(r'<title>.*?</title>', lambda _: f'<title>{html.escape(title, quote=False)}</title>', t, count=1)
    t = re.sub(r'<meta name="description" content="[^"]*">', lambda _: f'<meta name="description" content="{HA(desc)}">', t, count=1)
    t = between(t, '<!--head-->', '<!--/head-->', head(path, title, desc, list(lds), md=not is404, img=img))
    t = re.sub(r'<body data-route="[^"]*">', f'<body data-route="{H(route)}">', t, count=1)
    nk = NAV_KEY(path)
    if nk:   # the top bar's item for this section (app.js navKey: keep in step)
        t = t.replace(f'<a href="/{nk}/" data-nav="{nk}">', f'<a href="/{nk}/" data-nav="{nk}" class="on" aria-current="page">', 1)
    t = between(t, '<!--prerender-->', '<!--/prerender-->', body).replace('{{UPDATED}}', date)
    if is404:  # 404.html: noindex, no canonical
        t = t.replace(f'<link rel="canonical" href="{H(SITE + path)}">\n', '<meta name="robots" content="noindex">\n')
        open(os.path.join(OUT, path.strip('/')), 'w').write(t)
        return
    URLS.append((path, priority, date))
    md = ((md if md is not None else to_md(SHARE_RE.sub('', body).replace('{{UPDATED}}', date))) + f'\n---\n\n{title}. Web page: {SITE}{path} · updated {date} · '
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
# 85b: meta descriptions of generated pages are at most 160 characters and end cleanly (meta_desc); the build fails if a
# generated page's description is longer, and warns for the content pages (their text is data/pages/*.md, reviewed apart)
DESC_MAX, TITLE_MAX = 160, 70
_ABBR = re.compile(r'(?:\b(?:e\.g|i\.e|vs|cf|al|resp|etc|approx|Thm|Prop|Lem|Def|Sec|Ch|No|St|Dr|Mr|Ms|Prof|Jr|Sr|ca|fig|Fig)|\b[A-Z])\.$')
_TAILW = re.compile(r'(?i)\s+(?:and|or|but|nor|of|the|a|an|to|in|into|onto|for|with|without|within|by|from|on|at|as|its|their|his|her|that|which|whose|who|is|are|was|were|be|been|via|over|under|than|then|so|if|when|where|while|each|every|all|any|some|no|not|this|these|those|such|like|about|between|among|called|named|known|how|what|several|more|less|most|very|also|both|either|neither|whether|after|before|until|up|down|per)$')
_CLAUSE = re.compile(r'\s*[,;:]\s|\s+[—–]\s+|\s+\(|\s+(?=(?:and|but|while|whereas|which|where|because|so that|through|using|via|with)\s)')
def _balanced(t):
    return t.count('(') == t.count(')') and t.count('[') == t.count(']') and t.count('“') == t.count('”') and t.count('"') % 2 == 0 and t.count('$') % 2 == 0
def _detail(t):   # drop dangling small words and punctuation from the end of a cut
    while True:
        t2 = _TAILW.sub('', t).rstrip(' ,;:—–(“"')
        if t2 == t:
            return t
        t = t2
def meta_desc(s, n=160):
    """A meta description of at most n characters (85b). The text as is if it fits; else, in this order: the longest run
    of whole sentences that fits, if at least 100 characters; the longest cut at a clause break (comma, semicolon, colon,
    dash, an opening bracket, or before 'and', 'which', 'where'…) that fits, with '…', if at least 100; whole sentences of
    at least 60, then of 40, or a clause cut of that length; else a cut at a word. A cut never ends on a dangling 'and', 'of', 'the'…"""
    s = ' '.join(str(s or '').split())
    w = lambda t: len(HA(t))   # length as written in the attribute, where a quote mark is &quot;, so either count is <= n
    if w(s) <= n:
        return s
    sent = ''
    for m in re.finditer(r'[.!?]["”)]?(?=\s+[A-Z0-9"“(`]|$)', s):
        pre = s[:m.end()]
        if w(pre) > n:
            break
        if not (pre[m.start()] == '.' and _ABBR.search(s[:m.start() + 1])) and _balanced(pre):
            sent = pre
    cut = ''
    for m in _CLAUSE.finditer(s):
        if w(s[:m.start()]) + 1 > n:
            break
        pre = _detail(s[:m.start()])
        if _balanced(pre) and len(pre) > len(cut):
            cut = pre
    for floor in (100, 60, 40):
        if len(sent) >= floor:
            return sent
        if len(cut) >= floor:
            return cut + '…'
    t = s[:n]
    while w(t) + 1 > n:
        t = t[:-1]
    return _detail(t.rsplit(' ', 1)[0]) + '…'
# P2: hand-written meta descriptions for the clusters whose automatic cut (meta_desc) ends mid-phrase, i.e. was cut at a
# word, not at a clause break. data/meta-desc-fixes.tsv: cluster, old (the automatic cut it replaces), new (whole
# sentences, words taken from the cluster's own name and description). A fix applies only while its 'old' still matches
# what meta_desc gives, so a changed description fails the build instead of keeping a stale fix.
MDFIX_F = os.path.join(REPO, 'data', 'meta-desc-fixes.tsv')
MDFIX = {}
if os.path.exists(MDFIX_F):
    for _ln in open(MDFIX_F, encoding='utf-8').read().splitlines()[1:]:
        if _ln.strip():
            _k, _old, _new = _ln.split('\t')
            MDFIX[_k] = (_old, _new)
def cluster_desc(k, text):
    d = meta_desc(text)
    if k in MDFIX:
        old, new = MDFIX[k]
        assert d == old, f'meta-desc-fixes.tsv: {k} no longer matches its automatic description; update or drop the fix:\n  {d}'
        assert max(len(new), len(HA(new))) <= DESC_MAX and new.endswith('.'), f'meta-desc-fixes.tsv: {k}: new text over {DESC_MAX} or not a sentence'
        return new
    return d
_TBREAK = re.compile(_CLAUSE.pattern + r'|\s+(?=(?:for|of|over|in|on|from|at|to|into|by|under|between|after|as|off|without|within)\s)')
def cut_title(s, n=TITLE_MAX):
    """85d: a name longer than n characters, cut for the <title> only (the H1 and the address keep the whole name): at
    the last phrase break that fits (a clause break, or before 'for', 'of', 'over'… so no noun phrase is split) if that
    keeps 30 characters or more, else at a word; never on a dangling 'and', 'of'…; then '…'. app.js has the same
    function (cutTitle); keep them in step."""
    if len(s) <= n:
        return s
    cut = ''
    for m in _TBREAK.finditer(s):
        if m.start() + 1 > n:
            break
        pre = _detail(s[:m.start()])
        if _balanced(pre) and len(pre) > len(cut):
            cut = pre
    return (cut if len(cut) >= 30 else _detail(s[:n].rsplit(' ', 1)[0])) + '…'
def fit(name, n=60):
    """Title for a map page: the name plus as much of the primary query ('Lean proof of the Riemann hypothesis')
    as fits in about 60 characters; a name too long for any suffix stands alone, cut to 70 characters if longer
    (cut_title) rather than cut to make room for a suffix (keep in step with fit() in app.js)."""
    for t in (f'{name} in the Lean proof of the Riemann hypothesis', f'{name} · Riemann hypothesis Lean proof',
              f'{name} · RH Lean proof'):
        if len(t) <= n:
            return t
    return cut_title(name)

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
        return (f'The whole proof feeds into it: through chains of imports it builds on all {builds[main]:,} other clusters '
                '(Builds on, below, counts only its direct imports).')
    n = feeds[k]
    return f'Feeds into {n:,} cluster{"" if n == 1 else "s"} · {pct(n)} of the map.'
def neighbours(title, ids, on_route):
    """'Builds on' / 'Needed by' as plain HTML: themes with counts, key neighbours, then the full list."""
    note = ('<p class="meta">Direct imports: clusters with a file that a file here imports.</p>' if title == 'Builds on' else
            '<p class="meta">Direct importers: clusters with a file that imports a file here.</p>')
    if not ids:
        return f'<h2>{title} 0 clusters</h2>{note}<p class="meta">None outside this cluster.</p>'
    tc = collections.Counter(CL[x]['theme'] for x in ids)
    key = sorted(ids, key=lambda x: (x not in on_route, -fcount[x], x))[:3]
    return (f'<h2>{title} {len(ids):,} cluster{"" if len(ids) == 1 else "s"}</h2>{note}'
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
# checked clusters (data/core-names.yaml) say so instead, with a badge that links to the evidence on the same page
STATUS_CK = STATUS.replace('Names and descriptions on this map are written', "This cluster's name and description were checked "
                           'against its full Lean code; the other names and descriptions on this map are written')
assert STATUS_CK != STATUS
CK_BADGE = ('<div class="badges"><a class="badge checked" href="#checked">Checked against the code</a>'
            f'<a class="badgelink" href="/core/">See all {len(CHECKED)} core clusters ›</a></div>')
def checked_html(k):
    return ('<h2 id="checked">Checked against the code</h2><p>This name and description were checked against every Lean file in '
            f'the cluster (source commit <code>{LEAN_SHA[:8]}</code>) and corrected where the earlier, AI-drafted ones were wrong. '
            'Some of the declarations the check rests on:</p><ul class="evidence">'
            + ''.join(f'<li><code>{H(dc)}</code>' + (f' in <code>{H(m)}</code>' if m else '') + f': {H(w)}</li>' for m, dc, w in evidence(k))
            + '</ul>')
# feedback lives in one place: the site footer in the index.html template (@SomTheBuilder on X)
# QA23a: a cluster page also gets the app's quiet "Report a wrong name" link (same X post, prefilled with the id and URL;
# keep in step with reportHref() in app.js). Like the Share bar it is not part of lastmod, nor of the Markdown copy.
from urllib.parse import quote as _quote
def report_html(k):
    u = 'https://x.com/intent/post?text=' + _quote(f'@SomTheBuilder Wrong name or description for cluster {k} on the RH Lean map: '
                                                  f'{SITE}{CPATH[k]}', safe="-_.!~*'()")
    return (f'<span class="report"><a href="{H(u)}" target="_blank" rel="noopener" aria-label="Report a wrong name or '
            f'description for cluster {k} on X (opens in a new tab)">Report a wrong name ›</a></span>')
def with_report(status, k):   # at the end of the status line, which says names and descriptions may be wrong
    assert status.endswith('may be wrong.</p>')
    return status[:-4] + ' ' + report_html(k) + '</p>'
STATUS_NAV = 'Has the Riemann hypothesis been solved? Status of the proof'
CORE_NAV = f'The core of the proof: {len(CHECKED)} clusters, names checked against the code'
NUMBERS_NAV = 'The proof in numbers: files, lines, clusters and checks'
CONTENT_PAGES = []   # (path, title, h1) of the Markdown content pages, filled in below; footer, home, llms.txt use it
ROUTE_T = 'How the Lean proof of the Riemann hypothesis is structured: the route to the main theorem'
ROUTE_TITLE = 'The route: how the Lean proof of the Riemann hypothesis is structured'   # <title>, 70-character cap; the H1 keeps ROUTE_T (keep in step with pageTitle() in app.js)
assert len(ROUTE_TITLE) <= 70
ROUTE_NAV = 'How the proof is structured: the route to the main theorem'
LEARN_T = 'The Riemann hypothesis proof, step by step: learning path'
HOME_T = 'Lean proof of the Riemann hypothesis: an interactive map'
def explore(*extra, main_link=True):
    """'Where next' list on map pages: links the map to the explainers and back."""
    items = list(extra) + [(MAIN if main_link else None, "Start at the main theorem's cluster"), ('/route/', ROUTE_NAV), ('/core/', CORE_NAV),
                           ('/proof-in-numbers/', NUMBERS_NAV), ('/status/', STATUS_NAV), ('/learn/', 'Learning path: the proof step by step, down to school maths')]
    return '<h2>Explore</h2><ul class="rows">' + ''.join(f'<li><a href="{p}">{H(t)}</a></li>' for p, t in items if p) + '</ul>'
TT = {x['id']: tnode(x) for x in core['nodes'] + concepts}
LEARN_OF = collections.defaultdict(list)  # cluster -> learning-path entries that point at it
for x in TT.values():
    for k in x['clusters']:
        LEARN_OF[k].append(x)
# the ids the static /learn/ page draws (tli() below walks the same tree from the two roots); other learning-path entries
# have no anchor there, so cluster pages link their app page /concept/<id> instead (link sweep 23 Nov: 9 dead anchors)
ON_LEARN, _todo = set(), list(core['roots'])
while _todo:
    _i = _todo.pop()
    if _i in TT and _i not in ON_LEARN:
        ON_LEARN.add(_i); _todo += TT[_i]['needs']
def learn_href(i):
    return f'/learn/#{i}' if i in ON_LEARN else f'/concept/{i}'

# ---------- theme pages
REL = collections.defaultdict(list)   # theme -> [(import links, other theme)] from the theme edges (tedges)
for (a, b), x in w.items():
    REL[a].append((x, b)); REL[b].append((x, a))
for t, th in TH.items():
    tn = TNAMED.get(t, {})
    cs = sorted(th['clusters'], key=lambda k: (dist.get(k, 99), -fcount[k]))
    desc = meta_desc(f"{tn.get('blurb') or ''} {len(cs)} clusters of Lean files in the Lean proof of the Riemann hypothesis.")
    rel = sorted(REL[t], key=lambda z: (-z[0], z[1]))[:6]
    body = (f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>Theme</div>'
            f'<div class="eyebrow">Theme · Lean proof of the Riemann hypothesis</div>'
            f'<h1>{H(TNAME[t])}</h1>' + f'<p class="meta tags">Field: {H(FIELDS[FIDX[TFIELD[t]]]["name"])}</p>' + share_btn(TPATH[t], TNAME[t])
            + (f'<p class="lede">{H(tn["blurb"])}</p>' if tn.get('blurb') else '') + STATUS +
            f'<h2>Clusters</h2><ul class="rows">{"".join(clink(k, sub=oneline(k)) for k in cs)}</ul>'
            + (f'<h2>Related themes</h2><ul class="rows">' + ''.join(
                f'<li><a href="{TPATH[o]}"><span class="t">{H(TNAME[o])}<small>{x} import links between their clusters</small></span></a></li>'
                for x, o in rel) + '</ul>' if rel else '')
            + explore())
    page(TPATH[t], fit(TNAME[t]), desc, f'theme/{t}', body, [crumbs_ld(('Map', '/'), (TNAME[t], TPATH[t]))], .6,
         img=(og_url(f'og/t/{t}.png'), f'{TNAME[t]}: a theme of the Lean proof of the Riemann hypothesis'))

# ---------- cluster pages
def spine_ref_html(r):   # one checked reference: citation (linked), locator, precision pill, match and note
    cit = f'<a href="{H(r["url"])}">{H(r["citation"])}</a>' if r['url'] else H(r['citation'])
    extra = ' '.join(x for x in ((f'Match: {r["match"]}.' if r['match'] else ''), r['note'] or '') if x)
    return (f'<div class="ref chk">{cit}' + (f' · <span class="loc">{H(r["locator"])}</span>' if r['locator'] else '')
            + f' <span class="prec {r["precision"]}" title="{H(PREC_TIP[r["precision"]])}"><span class="sr">(precision: </span>'
            f'{r["precision"]}<span class="sr">)</span></span>' + (f'<small>{H(extra)}</small>' if extra else '') + '</div>')
def spine_refs_html(k):   # 35b: the checked references of a spine cluster, exact and section first, then Background
    if k not in CHECKED_REFS or not CHECKED_REFS[k]['refs']:   # the spine's and N3's judged guide citations
        return ''
    rs = CHECKED_REFS[k]['refs']
    main_rs, bg = [r for r in rs if r['precision'] != 'topic'], [r for r in rs if r['precision'] == 'topic']
    d = datetime.date.fromisoformat(CHECKED_REFS[k]['date'])
    return (f'<p class="meta refnote">References checked on {d.day} {d:%b %Y}. Exact: the theorem number was read in the '
            'text and matches the Lean statement. Section: the right chapter or section. Topic: general background.</p>'
            + ''.join(spine_ref_html(r) for r in main_rs)
            + (f'<h3 class="refbg">Background</h3>' + ''.join(spine_ref_html(r) for r in bg) if bg else ''))
# ---------- guides: shared HTML (the hub, the guide pages and the cluster pages' "Expert guides" list; app.js draws the
# same pieces in the panel). Data: GD, CGUIDES (above, before the cluster files)
G_STATUS_T = {'checked': 'Checked the proof', 'explains': 'Explains the proof'}
G_BOX_T = 'Expert guides to this part of the proof'   # the section title on cluster pages and in the panel (app.js: keep in step)
GPATH = {g['slug']: f'/guides/{g["slug"]}/' for g in GD if g['page']}
def gdate(d):
    return d.strftime('%-d %b %Y') if d else ''
def gav(g, px=48):   # the author's photo (alt: the name), or an initials badge; two organisations: both logos, side by side
    src = g['ph96'] if px > 24 else g['ph48']
    src2 = g['ph96b'] if px > 24 else g['ph48b']
    if src and src2:
        a1, a2 = (str(g['name'] or '').split(' and ', 1) + [''])[:2]
        q = max(16, px * 2 // 3)
        return (f'<span class="gav2" style="--lg:{q}px"><img class="gav logo" src="{src}" width="{q}" height="{q}" alt="{H(a1.strip())} logo" loading="lazy" decoding="async">'
                f'<img class="gav logo" src="{src2}" width="{q}" height="{q}" alt="{H(a2.strip())} logo" loading="lazy" decoding="async"></span>')
    if src:
        return f'<img class="gav" src="{src}" width="{px}" height="{px}" alt="{H(g["name"] or "")}" loading="lazy" decoding="async">'
    hue = int(hashlib.sha256(g['id'].encode()).hexdigest()[:4], 16) % 360
    return (f'<span class="gav ini" style="--gh:{hue};--gs:{px}px" role="img" aria-label="{H(g["name"] or "No author named")}">'
            f'{H(g["initials"])}</span>')
def gauthor(g, link=True):
    if not g['name']:
        return 'No author named on the page'
    return f'<a href="{H(g["home"])}">{H(g["name"])}</a>' if link and g['home'] else H(g['name'])
def gposted(g):
    return (f'Originally posted at <a href="{H(g["url"])}">{H(_host(g["url"]))}</a>' + (f' on {gdate(g["date"])}' if g['date'] else ''))
def gversion(g):
    v = g['versions'][-1] if g['versions'] else None
    if not v or v.get('version') is None:
        return ''
    l = vlabel(v)
    return f'Version {l}' if re.fullmatch(r'[\d.]+', l) else ''   # a label such as 'post' shows on the guide page only
def gstatus(g):
    return (f'<span class="gst {g["status"]}">{G_STATUS_T[g["status"]]}</span>'
            + (f' <q>{H(" ".join(str(g["quote"]).split()))}</q>' if g.get('quote') else ''))
# the AI label (owner decision, 24 Nov 2026): "AI-assisted (author's statement)" with the author's own words, or for the one
# guide labelled from its commit trailers "AI-assisted (repository history)", saying that it is not the author's statement
G_AI_T = {'author': "AI-assisted (author's statement)", 'repo': 'AI-assisted (repository history)'}
G_AI_REPO = 'This label comes from the repository history (the commit trailers), not from a statement by the author.'
G_ZERO = 'This guide does not name Lean declarations, so it is not linked to nodes on the map.'
def gai_tag(g, link=True):   # the short tag (hub entry, cluster pages): links to the statement on the guide page
    if not g['ai']:
        return ''
    t_ = 'AI-assisted' + (' (repository history)' if g['ai']['src'] == 'repo' else '')
    tip = H(G_AI_T[g['ai']['src']] + ': ' + g['ai']['quote'])
    return (f'<a class="gai" href="{GPATH[g["slug"]]}#ai" title="{tip}">{t_}</a>' if link and g['slug'] in GPATH
            else f'<span class="gai" title="{tip}">{t_}</span>')
def gai_src(url, loc):
    return f'<a href="{H(url)}">{H(_host(url))}</a>' + (f' ({H(loc)})' if loc else '')
def gai_html(g):   # the guide page's line: label, quote, link (and the author's further statements)
    a = g['ai']
    if not a:
        return ''
    if a['src'] == 'repo':
        return (f'<div class="gailine" id="ai"><p><span class="gai">{G_AI_T["repo"]}</span> <q>{H(a["quote"])}</q> (repository history). '
                f'<a href="{H(a["url"])}">Commit history</a>. {H(G_AI_REPO)}</p></div>')
    also = ''.join(f'<li><q>{H(q)}</q> {gai_src(u, l)}</li>' for q, u, l in a['also'])
    return (f'<div class="gailine" id="ai"><p><span class="gai">{G_AI_T["author"]}</span> <q>{H(a["quote"])}</q> {gai_src(a["url"], a["loc"])}</p>'
            + (f'<ul class="gaialso">{also}</ul>' if also else '') + '</div>')
def gai_md(g):
    a = g['ai']
    if not a:
        return ''
    if a['src'] == 'repo':
        return f'{G_AI_T["repo"]}: "{a["quote"]}" (repository history, {a["url"]}). {G_AI_REPO}'
    return (f'{G_AI_T["author"]}: "{a["quote"]}" ({a["url"]}' + (f', {a["loc"]}' if a['loc'] else '') + ')'
            + ''.join(f'; "{q}" ({u}' + (f', {l}' if l else '') + ')' for q, u, l in a['also']))
def gpages_html(pages):
    return ', '.join(f'<a href="{H(u)}">{H(l)}</a>' if u else H(l) for l, u in pages)
def gnotes_n(n):
    return f'{n} audit {"note" if n == 1 else "notes"}'
def grefs_html(g, pages, notes, more=''):   # 'Pages: p. 12, p. 30–31' or 'Manuscript p. 7 · 12 audit notes: a, b, …' (static: a compact list)
    bits = []
    if pages:
        bits.append((f'{g["pdf_word"]} ' if g['pdf_word'] else f'{"Page" if len(pages) == 1 else "Pages"}: ') + gpages_html(pages) + more)
    if notes:
        bits.append(f'{gnotes_n(len(notes))}: <span class="gnl">{gpages_html(notes)}</span>')
    return ' · '.join(bits)
def grefs_md(g, pages, notes):
    bits = []
    if pages:
        bits.append((f'{g["pdf_word"]} ' if g['pdf_word'] else '') + ', '.join(f'[{l}]({u})' if u else l for l, u in pages))
    if notes:
        bits.append(f'{gnotes_n(len(notes))}: ' + ', '.join(f'[{l}]({u})' if u else l for l, u in notes))
    return ' · '.join(bits)
def gbox_html(k):   # the cluster page's list: each guide (photo, author, title -> its page or the original), its pages
    if k not in CGUIDES:
        return ''
    li = []
    for x in CGUIDES[k]:
        g = G_MAP[x['i']]
        more = (f', <a href="{GPATH[g["slug"]]}#nodes">{x["m"]} more</a>' if x.get('m') and g['slug'] in GPATH else f' and {x["m"]} more' if x.get('m') else '')
        refs = grefs_html(g, x['p'], x.get('n', []), more)
        li.append(f'<li><a href="{H(GPATH.get(g["slug"], g["url"]))}">{gav(g, 24)}<span class="t">{gauthor(g, False)}<small>{H(g["title"])}</small></span></a>'
                  + (f'<p class="gpages">{gai_tag(g)}</p>' if g['ai'] else '') + (f'<p class="gpages">{refs}</p>' if refs else '') + '</li>')
    return f'<h2 id="guides">{G_BOX_T}</h2><ul class="rows glist">{"".join(li)}</ul><p class="meta"><a href="/guides/">All guides</a></p>'
def gcite_item(w):   # one guide-cited work: the citation (linked by DOI or arXiv), then "cited on Jaswal, p. 12, …"
    cit = f'<a href="{H(w["url"])}">{H(w["citation"])}</a>' if w['url'] else H(w['citation'])
    on = [f'<a href="{H(u)}">{H(G_BY_ID[gi]["cite_as"])}, {H(l)}</a>' if u else f'{H(G_BY_ID[gi]["cite_as"])}, {H(l)}'
          for gi, l, u in w['on'][:GC_PMAX]]
    more = len(w['on']) - GC_PMAX
    return f'<div class="ref gc">{cit}<small>cited on {", ".join(on)}{f" and {more} more" if more > 0 else ""}</small></div>'
def gcite_html(k):   # N3 tier 1: the subsection at the end of References
    ws = GCITE.get(k)
    if not ws:
        return ''
    rest = ws[GC_CAP:]
    return (f'<h3 class="refbg" id="guide-cited">{GC_T}</h3><p class="meta refnote">{H(GC_LABEL)}. {H(GC_NOTE)} '
            f'<a href="/guides/">About the guides</a></p>' + ''.join(gcite_item(w) for w in ws[:GC_CAP])
            + (f'<details class="gcmore"><summary>Show all {len(ws)}</summary>{"".join(gcite_item(w) for w in rest)}</details>' if rest else ''))
def fl_link_text(k):
    return f'Read its Lean files, in plain English ({len(FL[k])} {"file" if len(FL[k]) == 1 else "files"})'
def fl_link(k):   # #10: the cluster page's link to its /lean/ page
    return f'<p class="lflink"><a class="btn" href="{CPATH[k]}lean/">{H(fl_link_text(k))} <span class="arr">→</span></a></p>' if FL.get(k) else ''
for k, p in CPATH.items():
    n, c = NAMES.get(k, {}), CL[k]
    title = n.get('title') or folder_label(c['folders'])
    src = shown_source(k)
    refs = spine_refs_html(k) + ''.join([f'<div class="ref">{H(src.get("title", ""))}{" · " + H(src["where"]) if src.get("where") else ""}'
                    f'<small>{AUTO_LABEL} · suggested by the AI that named the cluster</small></div>'] if src else []) + \
           ''.join(f'<div class="ref note">{H(re.sub(r"\s*\(word match [\d.]+\):", " —", h))}<small>Cited in the author\'s note · '
                   f'matched by word overlap · unchecked</small></div>' for h in HINTS.get(k, [])) + gcite_html(k)
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
            f'<p class="meta tags">{H(ctag_line(k))}</p>' + (CK_BADGE if k in CHECKED else '') + share_btn(p, title)
            + f'<p>{H(n.get("plain") or "")}</p>' + fl_link(k) + f'{route}<p class="meta">{H(feeds_txt(k))}</p>'
            + with_report(STATUS_CK if k in CHECKED else STATUS, k) + (checked_html(k) if k in CHECKED else '') + why
            + (f'<h2>Prerequisite concepts</h2><div class="chips">{"".join(f"<span class=chip>{H(x)}</span>" for x in conc)}</div>' if conc else '')
            + (f'<h2>In the learning path</h2><ul class="rows">' + ''.join(
                f'<li><a href="{H(learn_href(x["id"]))}"><span class="t">{H(x["title"])}<small>{H(x["kind"])}</small></span></a></li>' for x in lp)
               + '</ul>' if lp else '')
            + gbox_html(k)
            + (f'<h2>References</h2>{refs}' if refs else '')
            + neighbours('Builds on', uses[k], on_route) + neighbours('Needed by', sorted(used_by[k]), on_route)
            + f'<p class="meta">{len(members[k])} Lean files, main folder {H(c["folders"][0][0] if c["folders"] else "")}.</p>'
            + explore((TPATH[th], f'Theme: {TNAME[th]}'), main_link=k != main))
    page(p, fit(title), cluster_desc(k, n.get('plain') or f'Cluster {k} of the Lean proof of the Riemann hypothesis.'), f'cluster/{k}', body,
         [crumbs_ld(('Map', '/'), (TNAME[th], TPATH[th]), (title, p))],
         img=(og_url(f'og/c/{k}.png'), f'{title}: cluster {k} of the Lean proof of the Riemann hypothesis'))

# ---------- #10: /cluster/<id>-<slug>/lean/ (and part-2/, …): the core cluster's Lean files in plain English
FL_PAGES = {}   # k -> [(path, title, html bytes)]
def fl_contents(k):
    """the contents list by depth, linking every file (in whichever part it is)"""
    by = collections.defaultdict(list)
    for e in FL[k]:
        by[e['depth']].append(e)
    out = ['<h2 id="contents">Contents</h2><p class="meta">By import steps from <code>Main.lean</code>, closest first.</p>']
    for d in sorted(by):
        dl = '★ Main' if d == 0 else f'{d} import {"step" if d == 1 else "steps"} from Main'
        out.append(f'<h3 class="ldep">{dl} '
                   f'<span class="n">{len(by[d])}</span></h3><ul class="lcon">')
        for e in by[d]:
            m = e['module']
            out.append(f'<li><a href="{fl_ppath(k, FL_PART[(k, m)])}#{H(fl_anchor(m))}"><code>{H(m)}</code></a>'
                       + (f'<small>{H(e["line"])}</small>' if e['status'] != 'cut' else '') + '</li>')
        out.append('</ul>')
    return ''.join(out)
def fl_contents_md(k):
    by = collections.defaultdict(list)
    for e in FL[k]:
        by[e['depth']].append(e)
    out = ['## Contents', '']
    for d in sorted(by):
        out += ['- Main:' if d == 0 else f'- {d} import {"step" if d == 1 else "steps"} from Main:']
        out += [f'  - [{e["module"]}]({SITE}{fl_ppath(k, FL_PART[(k, e["module"])])}#{e["module"]})' for e in by[d]]
    return '\n'.join(out) + '\n'
def _fl_pages():   # a function, so that its names do not leak into the build's globals
    for k, parts in FL_PARTS.items():
        n, c = NAMES.get(k, {}), CL[k]
        title, th, cp = ctitle(k), c['theme'], CPATH[k]
        np_ = len(parts)
        nf = len(FL[k])
        for i, secs in enumerate(parts):
            path = fl_ppath(k, i)
            sfx = ' · Lean files in plain English' + (f', part {i + 1}' if i else '')
            ptitle = cut_title(title, TITLE_MAX - len(sfx)) + sfx
            first, last = secs[0][0], secs[-1][0]
            rng = f'files {FL[k].index(first) + 1}–{FL[k].index(last) + 1} of {nf}'
            desc = meta_desc((f'Part {i + 1} of {np_}, {rng}. ' if np_ > 1 else '')
                             + f'The {nf} Lean files of cluster {k}, {title}, in plain English: what each proves, its key '
                             f'statements, each reading checked against the code.')
            pnav = ''
            if np_ > 1:
                pnav = ('<nav class="lparts" aria-label="Parts of this page">' + ' '.join(
                    (f'<span aria-current="page">Part {j + 1}</span>' if j == i else f'<a href="{fl_ppath(k, j)}">Part {j + 1}</a>')
                    for j in range(np_)) + f'<span class="meta">{rng}</span></nav>')
            crumbs = (f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span><a href="{TPATH[th]}">{H(TNAME[th])}</a>'
                      f'<span class="sep">/</span><a href="{cp}">{k}</a><span class="sep">/</span>Lean files' + (f' (part {i + 1})' if i else '') + '</div>')
            body = (crumbs + f'<div class="eyebrow">Cluster {k} · Lean files in plain English</div>'
                    f'<h1>{H(title)}: its Lean files in plain English</h1>' + share_btn(path, ptitle)
                    + f'<p class="lede lhow">{H(FL_HOW)}</p>'
                    + f'<p class="meta">{nf} Lean {"file" if nf == 1 else "files"}, by distance from <code>Main.lean</code>. Each file links to the '
                    f'Lean viewer; the statements below are cut from the source up to <code>:=</code>. '
                    f'<a href="{cp}">Back to the cluster page</a> · <a href="/core/">All {len(CHECKED)} core clusters</a></p>'
                    + pnav + fl_contents(k) + '<h2 id="files">The files</h2>' + ''.join(h for _, h, _ in secs) + pnav
                    + explore((cp, f'Cluster page: {title}'), ('/core/', CORE_NAV), main_link=False))
            md = (f'# {title}: its Lean files in plain English\n\n{FL_HOW}\n\n'
                  f'Cluster {k} ({SITE}{cp}) · {nf} Lean files, by distance from Main.lean' + (f' · part {i + 1} of {np_}, {rng}' if np_ > 1 else '')
                  + f' · data: {SITE}/api/file-lines/{k}.json\n\n'
                  + (''.join(f'- Part {j + 1}: {SITE}{fl_ppath(k, j)}index.md\n' for j in range(np_)) + '\n' if np_ > 1 else '')
                  + fl_contents_md(k) + '\n## The files\n\n' + '\n'.join(x for _, _, x in secs) + '\n')
            lds = [crumbs_ld(('Map', '/'), (TNAME[th], TPATH[th]), (title, cp), ('Lean files' + (f', part {i + 1}' if i else ''), path)),
                   {'@type': 'WebPage', '@id': SITE + path, 'url': SITE + path, 'name': ptitle, 'description': desc, 'inLanguage': 'en',
                    'isPartOf': {'@id': SITE_ID}, 'about': {'@type': 'SoftwareSourceCode', 'name': f'Lean files of cluster {k}',
                    'programmingLanguage': 'Lean 4', 'codeRepository': f'{LEAN_REPO}/tree/{LEAN_SHA}'}}]
            page(path, ptitle, desc, 'page', body, lds, .6, md=md,
                 img=(og_url(f'og/c/{k}.png'), f'{title}: cluster {k} of the Lean proof of the Riemann hypothesis'))
            sz = os.path.getsize(os.path.join(OUT, path.strip('/'), 'index.html'))
            assert sz <= FL_MAX, f'{path}: {sz:,} bytes of HTML, over the {FL_MAX:,} limit: raise FL_FRAME'
            FL_PAGES.setdefault(k, []).append((path, ptitle, sz))
_fl_pages()
if FL_PAGES:
    _szs = [z for v in FL_PAGES.values() for _, _, z in v]
    print(f'file-lines pages: {len(_szs)} pages for {len(FL_PAGES)} clusters ({sum(1 for v in FL_PAGES.values() if len(v) > 1)} split), '
          f'{sum(_szs) / 1e6:.2f} MB HTML, largest {max(_szs) / 1e3:.0f} kB')

# ---------- /api/status.json timeline (the About page is now data/pages/about.md; the status text is on /status/)
STATUS_FACTS = [
    {'date': '2026-11-20', 'event': plain(ST_RELEASE), 'source': NOTE},
    {'date': '2026-11-21', 'event': plain(ST_CERT), 'source': STMT},
]

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
LEARN_D = ('The Lean proof of the Riemann hypothesis, step by step: from the headline theorems through its main steps '
           'down to background maths, linked to the code.')
learn = ('<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>Learning path</div><div class="eyebrow">Learning path</div>'
         '<h1>The Riemann hypothesis proof, step by step</h1><p class="lede">From the Riemann hypothesis down to school maths: '
         'the outline runs from the two headline theorems through the main steps of the proof, then to background concepts and '
         'school or first-year university material. It follows the proof as we read it from the Lean code.</p>'
         f'<ul class="tree">{"".join(tli(r, seen) for r in core["roots"])}</ul>'
         f'<p class="meta">See also: <a href="/status/">how the proof was checked</a> · <a href="/core/">the core of the proof</a> · <a href="{MAIN}">the main theorem on the map</a></p>')
assert seen == ON_LEARN, 'learn_href() and the /learn/ page disagree on which entries the page draws'
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
ROUTE_D = meta_desc(f'How the Lean proof of the Riemann hypothesis is structured, by import steps from the main theorem: {len(CL):,} clusters '
               f'holding {len(mod_cl):,} of its {TOTAL_FILES:,} Lean files. The deepest cluster is {max(DEPTHS)} steps down; the longest import chain is {FSTATS["chain"]} files.')
page('/route/', ROUTE_TITLE, ROUTE_D, 'route', route_body,
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
    ('press.md', 'Press', 'Press, statements and reactions', .7),
    ('core.md', 'The core', 'The core of the proof · 16 clusters', .8),
    ('proof-in-numbers.md', 'In numbers', 'The proof in numbers', .7),
    ('timeline.md', 'Timeline', 'Timeline', .6),
    ('about.md', 'About', 'About this map', .6)]
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
# ---------- the zeros figure: '{{figure:zeros}}' on a line of its own in a draft becomes an inline SVG of the critical strip
# (no JS; one copy per level section, ids suffixed) in the HTML, and its text description in the Markdown copies.
# Heights: the first ten non-trivial zeros of zeta, rounded to 4 places (LMFDB, https://www.lmfdb.org/zeros/zeta/).
ZEROS = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738]
ZEROS_TXT = ', '.join(f'{t:.4f}' for t in ZEROS)
ZEROS_CAP = ('The critical strip, where 0 < Re(s) < 1, with the critical line Re(s) = ½ down its middle. The Riemann hypothesis says '
             'every non-trivial zero of ζ lies on that line. The first ten above the real axis are drawn at their true heights; '
             'their mirror images below the axis are not shown. The trivial zeros sit at −2, −4, −6, … and ζ has a pole, not a zero, at s = 1.')
ZEROS_DESC = (f'Diagram of the complex plane, real part Re(s) across and imaginary part Im(s) up. A shaded vertical strip runs from '
              f'Re(s) = 0 to Re(s) = 1, with a gold dashed line at Re(s) = ½. Ten gold dots sit on the gold line at heights {ZEROS_TXT}. '
              'Blue dots on the real axis mark the trivial zeros at −2, −4 and −6; a cross marks the pole at s = 1.')
def zeros_figure(sfx):
    U, V, X0, Y0, W_, H_ = 32, 8.3, 222, 476, 380, 520     # px per unit of Re(s) and of Im(s); origin; viewBox size
    x = lambda re: round(X0 + re * U, 1)
    y = lambda im: round(Y0 - im * V, 1)
    sans, gold, acc = 'font-family="Inter, system-ui, sans-serif"', '#f5c46b', '#8ea2ff'
    o = [f'<rect x="{x(0)}" y="22" width="{U}" height="{H_ - 36}" fill="{acc}" fill-opacity=".16"/>',
         f'<line x1="{x(.5)}" y1="22" x2="{x(.5)}" y2="{Y0 + 6}" stroke="{gold}" stroke-width="2" stroke-dasharray="6 4"/>',
         # axes, with arrowheads
         f'<path d="M10 {Y0}H{W_ - 14}M{W_ - 20} {Y0 - 5}l7 5-7 5" fill="none" stroke="#8b96c2" stroke-width="1.4"/>',
         f'<path d="M{x(0)} {H_ - 14}V14M{x(0) - 5} 20l5-7 5 7" fill="none" stroke="#8b96c2" stroke-width="1.4"/>',
         f'<text x="{W_ - 6}" y="{Y0 + 22}" text-anchor="end" fill="#c3cbef" font-size="13" {sans}>Re(s)</text>',
         f'<text x="{x(0) - 8}" y="22" text-anchor="end" fill="#c3cbef" font-size="13" {sans}>Im(s)</text>',
         # direct labels: the strip, the line, the hypothesis
         f'<text x="{x(0) - 10}" y="62" text-anchor="end" fill="#c3cbef" font-size="14" {sans}>critical strip</text>',
         f'<text x="{x(0) - 10}" y="80" text-anchor="end" fill="#8b96c2" font-size="13" {sans}>0 &lt; Re(s) &lt; 1</text>',
         f'<text x="{x(0) - 10}" y="112" text-anchor="end" fill="{gold}" font-size="14" {sans}>critical line</text>',
         f'<text x="{x(0) - 10}" y="130" text-anchor="end" fill="{gold}" fill-opacity=".85" font-size="13" {sans}>Re(s) = ½</text>',
         f'<path d="M{x(0) - 6} 118H{x(.5) - 4}" stroke="{gold}" stroke-opacity=".6" stroke-width="1"/>',
         '<g font-family="Fraunces, Georgia, serif" font-style="italic" font-size="17" fill="#e9edff">'
         + ''.join(f'<text x="14" y="{256 + i * 23}">{t}</text>' for i, t in enumerate(('The Riemann hypothesis:', 'every non-trivial zero', 'lies on the gold line.')))
         + '</g>',
         # ticks on the real axis
         f'<g fill="#8b96c2" font-size="13" text-anchor="middle" {sans}>'
         + ''.join(f'<text x="{x(v) + dx}" y="{Y0 + 22}">{t}</text>' for v, t, dx in ((-6, '−6', 0), (-4, '−4', 0), (-2, '−2', 0), (0, '0', -6), (.5, '½', 0), (1, '1', 5)))
         + '</g>',
         # trivial zeros and the pole
         f'<text x="{x(-4)}" y="{Y0 - 16}" text-anchor="middle" fill="#b4c1ff" font-size="13" {sans}>trivial zeros</text>',
         ''.join(f'<circle cx="{x(v)}" cy="{Y0}" r="5" fill="{acc}"><title>Trivial zero at s = −{-v}</title></circle>' for v in (-2, -4, -6)),
         f'<g fill="#8b96c2">' + ''.join(f'<circle cx="{x(-6.6) + i * 4}" cy="{Y0}" r="1.3"/>' for i in (-1, 0, 1)) + '</g>',
         f'<path d="M{x(1) - 5} {Y0 - 5}l10 10m0-10-10 10" stroke="#ff8a8a" stroke-width="2"><title>Pole at s = 1</title></path>',
         f'<text x="{x(1) + 9}" y="{Y0 - 9}" fill="#ff8a8a" font-size="13" {sans}>pole</text>',
         f'<text x="{x(1) + 16}" y="40" fill="#8b96c2" font-size="13" {sans}>height</text>']
    ly = []
    for t in ZEROS:                                   # labels at least 18 apart, pushed up where two zeros are close
        ly.append(min(y(t), ly[-1] - 18) if ly else y(t))
    for t, l in zip(ZEROS, ly):
        o.append(f'<g class="z" tabindex="0"><title>Zero at s = ½ + {t:.4f}i</title>'
                 f'<path d="M{x(.5) + 7} {y(t)}L{x(1) + 4} {l}H{x(1) + 12}" fill="none" stroke="#8b96c2" stroke-opacity=".55"/>'
                 f'<circle cx="{x(.5)}" cy="{y(t)}" r="5.5" fill="{gold}" stroke="#0b1230" stroke-width="1.5"/>'
                 f'<text x="{x(1) + 16}" y="{l}" dy=".35em" fill="#e9edff" font-size="14" font-variant-numeric="tabular-nums" {sans}>{t:.4f}</text></g>')
    return (f'<figure class="zfig" id="zeros-{sfx}"><svg viewBox="0 0 {W_} {H_}" role="img" aria-labelledby="zt-{sfx} zd-{sfx}">'
            f'<title id="zt-{sfx}">The critical strip and the first ten zeros of the Riemann zeta function</title>'
            f'<desc id="zd-{sfx}">{H(ZEROS_DESC)}</desc>' + ''.join(o) + f'</svg><figcaption>{H(ZEROS_CAP)}</figcaption></figure>')
def zeros_md(t):   # the figure in the Markdown copies: its caption and the list of zeros
    t = re.sub(r'(?m)^(##+ .*?)\s*\{#[\w-]+\}\s*$', r'\1', t)   # heading ids ({#tautology}, {#nov-24}) are for the HTML only
    return re.sub(r'(?m)^\{\{figure:zeros\}\}$', lambda m: (
        f'*Figure: the critical strip and the first ten zeros.* {ZEROS_CAP}\n\n'
        f'Heights of the first ten non-trivial zeros, each at ½ + it: {ZEROS_TXT} ([LMFDB](https://www.lmfdb.org/zeros/zeta/)).'), t)
def figures_html(h, sfx):
    return h.replace('<p>{{figure:zeros}}</p>', zeros_figure(sfx))
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
                   + figures_html(md_html(re.sub(r'^(## .*?)\s*\{#\w+\}', r'\1', lv[l])), l) + '</section>' for l, n in READ_LEVELS)
    return (figures_html(md_html(before), 'top') + '<div class="levels"><div class="ltabs" role="tablist" aria-label="Level">' + tabs + '</div>'
            + secs + '</div>' + figures_html(md_html(after), 'end'))
def keep_going(t):   # the closing links: a '## Keep going' / '## More' section, or a final 'More: …' line
    for x in h2_sections(t)[1:]:
        if re.match(r'## (Keep going|More)\b', x, re.I):
            return x.strip()
    m = re.search(r'(?m)^More: .*$', t)
    return m.group(0) if m else ''
def faq_pairs(t):   # H3 question, then its first paragraph (the visible answer, rendered the same way)
    return [(q, MDIT.renderInline(a.strip()))
            for q, a in re.findall(r'(?m)^### (.+?)(?:\s*\{#[\w-]+\})?\n\n((?:(?!Source:)[^\n]+\n)+)', t)]
KNOWN_PATHS = set(CPATH.values()) | set(TPATH.values()) | {'/', '/learn/', '/route/', '/list/', '/changelog/', '/api/'}
DRAFTS = [(f, *read_draft(f), crumb, eb, pr) for f, crumb, eb, pr in CONTENT]
OLD_PATHS = {**TOLD, **COLD}   # a draft linking to a renamed cluster or theme gets its current address
for i, (f, fm, t, *rest) in enumerate(DRAFTS):
    t2 = re.sub(r'\]\((/(?:cluster|theme)/[^)#\s]*)', lambda m: '](' + OLD_PATHS.get(m.group(1), m.group(1)), t)
    if t2 != t:
        print(f'{f}: links to renamed pages updated')
        DRAFTS[i] = (f, fm, t2, *rest)
KNOWN_PATHS |= {fm['path'] for _, fm, *_ in DRAFTS} | {'/guides/'} | set(GPATH.values())
# site links added under a page's own text (the drafts are published as written, so these are not part of them)
RELATED = {'/status/': [('/core/', CORE_NAV), ('/proof-in-numbers/', NUMBERS_NAV),
                        ('/timeline/', 'Timeline of the Riemann hypothesis, 1748 to the 2026 Lean proof')]}
for f, fm, t, crumb, eb, pr in DRAFTS:
    bad = [u for u in re.findall(r'\]\((/[^)#\s]*)', t) if u not in KNOWN_PATHS]
    assert not bad, f'{f}: links to pages that do not exist: {bad}'
    path, h1 = fm['path'], fm['h1']
    CONTENT_PAGES.append((path, fm['title'], h1))
    ARTICLES.add(path)
    lv = level_split(t)
    html_body = levels_html(*lv) if lv else figures_html(md_html(t), 'main')
    html_body = re.sub(r'^<p><em>', '<p class="meta asof"><em>', html_body, count=1)
    if path == '/core/' and FL:   # #10: after each core cluster's "Cluster page" link, a link to its /lean/ page (HTML and Markdown)
        for k in FL:
            a_ = f'<a href="{CPATH[k]}">Cluster page</a>'
            assert html_body.count(a_) == 1 and t.count(f'[Cluster page]({CPATH[k]})') == 1, f'core.md: no single "Cluster page" link for {k}'
            html_body = html_body.replace(a_, a_ + f' · <a href="{CPATH[k]}lean/">{H(fl_link_text(k))}</a>')
            t = t.replace(f'[Cluster page]({CPATH[k]})', f'[Cluster page]({CPATH[k]}) · [{fl_link_text(k)}]({CPATH[k]}lean/)')
    body = (f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>{H(crumb)}</div><div class="eyebrow">{H(eb)}</div>'
            f'<h1>{H(h1)}</h1>{html_body}')
    rel = RELATED.get(path, [])
    assert all(u in KNOWN_PATHS for u, _ in rel)
    if rel:
        body += '<h2>More on this site</h2><ul class="rows">' + ''.join(f'<li><a href="{u}">{H(x)}</a></li>' for u, x in rel) + '</ul>'
    lds = [article_ld(path, h1, fm['description'], CONTENT_PUBLISHED), crumbs_ld(('Map', '/'), (crumb, path)), ORG]
    if fm.get('structured_data') == 'FAQPage':
        pairs = faq_pairs(t)
        assert len(pairs) >= 10, f'{f}: FAQPage with only {len(pairs)} questions'
        lds.insert(1, faq_ld(pairs))
    page(path, fm['title'], fm['description'], 'page', body, lds, pr, fm=True, md=md_abs(zeros_md(f'# {h1}\n\n{t}' + (
        '\n## More on this site\n\n' + ''.join(f'- [{x}]({u})\n' for u, x in rel) if rel else ''))))
    if lv:   # one Markdown file per level: title, a one-line intro, the level's section, the closing links
        before, secs, after = lv
        intro = next((x.strip() for x in before.split('\n\n') if x.strip() and not re.fullmatch(r'\*[^*].*\*', x.strip())), '')
        more = keep_going(after)
        for l, n in READ_LEVELS:
            others = ' · '.join(f'[{m}]({SITE}{path}{k}.md)' for k, m in READ_LEVELS)
            lmd = (f'# {h1} ({n})\n\n{intro}\n\n*{n} level of three ({others}). Full page with every level: {SITE}{path}*\n\n'
                   + re.sub(r'^(## .*?)\s*\{#\w+\}', r'\1', secs[l].strip()) + '\n\n' + (more + '\n' if more else ''))
            open(os.path.join(OUT, path.strip('/'), f'{l}.md'), 'w').write(
                md_abs(zeros_md(lmd)) + f'\n---\n\n{h1} ({n}). Web page: {SITE}{path}#{l} · site map for machines: {SITE}/llms.txt\n')
LEVEL_PAGES = [p for f, fm, t, *_ in DRAFTS if level_split(t) for p in [fm['path']]]

# ---------- /guides/ (design section 1) and /guides/<slug>/ (section 2). The hub's intro is data/pages/guides.md (a copy
# of research/content/pages/guides.md) when it exists, else the stub below. The list is always generated from guides.yaml:
# one list, no groups, in hub order (GD), at the line '{{guides}}' of guides.md (stub: after the intro). The rest of
# guides.md is shown as written.
GUIDES_F = os.path.join(PAGES_DIR, 'guides.md')
GUIDES_STUB = ({'title': 'Guides to the Lean proof of the Riemann hypothesis',
                'description': 'Guides, explainers and verification pages about the Lean proof of the Riemann hypothesis, by other '
                               'people. Each says whether its author checked the proof.',
                'h1': 'Guides to the proof by other people', 'path': '/guides/'},
               'Guides, explainers and verification pages about the Lean proof of the Riemann hypothesis, written by other people. '
               'Each entry says whether its author ran checks of the Lean proof or explains it without checking it.\n')
def gnodes(g):
    return len(g['refs'])
def gmapq(g):
    return f'/?guide={g["slug"] or g["id"]}'
def gentry_html(g):
    meta = ' · '.join(x for x in (gposted(g), H(gversion(g)), f'Licence: {H(g["licence"])}' if g['licence'] else '') if x)
    n = gnodes(g)
    nn = f'{n} {"node" if n == 1 else "nodes"}'
    tail = [f'On the map: <a href="{H(gmapq(g))}">{nn}</a>' if g['page'] else f'On the map: {nn}'] if n else ['0 nodes on the map']   # page: false: the count only
    if g['page']:
        tail.append(f'<a href="{GPATH[g["slug"]]}">Guide page ›</a>')
    return (f'<li class="gentry">{gav(g, 48)}<div class="gbody"><p class="gauth">{gauthor(g)}</p>'
            f'<a class="gtitle" href="{H(g["url"])}">{H(g["title"])}</a><p class="gmeta">{meta}</p>'
            f'<p class="gstl">{gstatus(g)}</p>' + (f'<p class="gstl">{gai_tag(g)}</p>' if g['ai'] else '')
            + (f'<p class="gmeta">{" · ".join(tail)}</p>' if tail else '') + '</div></li>')
def gentry_md(g):
    n = gnodes(g)
    bits = [g['name'] or 'No author named on the page', f'originally posted at {_host(g["url"])}' + (f' on {gdate(g["date"])}' if g['date'] else ''),
            gversion(g), f'licence: {g["licence"]}' if g['licence'] else '', G_STATUS_T[g['status']] + (f': "{" ".join(str(g["quote"]).split())}"' if g.get('quote') else ''),
            gai_md(g), (f'on the map: {n} {"node" if n == 1 else "nodes"}' + (f' ({SITE}{gmapq(g)})' if g['page'] else '')) if n else '0 nodes on the map',
            f'guide page: {SITE}{GPATH[g["slug"]]}' if g['page'] else '']
    return f'- [{g["title"]}]({g["url"]}) · ' + ' · '.join(b for b in bits if b) + '\n'
G_HTML = '<ul class="glistall">' + ''.join(gentry_html(g) for g in GD) + '</ul>'
G_MD = ''.join(gentry_md(g) for g in GD)
if os.path.exists(GUIDES_F):
    gfm, gt = read_draft('guides.md')
else:
    gfm, gt = GUIDES_STUB
    print('guides.md not found in data/pages: /guides/ uses the stub intro')
gbad = [u for u in re.findall(r'\]\((/[^)#\s]*)', gt) if u not in KNOWN_PATHS]
assert not gbad, f'guides.md: links to pages that do not exist: {gbad}'
assert gfm['path'] == '/guides/', 'guides.md: path must be /guides/'
if not re.search(r'(?m)^\{\{guides\}\}$', gt):   # the stub: the list after the intro (guides.md has its own '{{guides}}' line)
    assert not os.path.exists(GUIDES_F), 'guides.md: needs a line {{guides}} where the generated list goes'
    gt = gt.rstrip() + '\n\n{{guides}}\n'
gpath, gh1 = gfm['path'], gfm['h1']
CONTENT_PAGES.append((gpath, gfm['title'], gh1))
ARTICLES.add(gpath)
ghtml = re.sub(r'^<p><em>', '<p class="meta asof"><em>', md_html(gt).replace('<p>{{guides}}</p>', G_HTML), count=1)
assert G_HTML in ghtml
page(gpath, gfm['title'], gfm['description'], 'page',
     f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>Guides</div><div class="eyebrow">Guides and explainers</div>'
     f'<h1>{H(gh1)}</h1>{ghtml}',
     [article_ld(gpath, gh1, gfm['description'], str(gfm.get('published', '2026-11-23'))), crumbs_ld(('Map', '/'), ('Guides', gpath)), ORG], .6, fm=True,
     md=md_abs(f'# {gh1}\n\n' + re.sub(r'(?m)^\{\{guides\}\}\n?', lambda m: G_MD, gt).rstrip() + '\n'))

# /guides/<slug>/: one page per guide with page: true. "Read our copy" and "Download" only for host_copy: true with a pinned
# local file (the last version with 'local', a path under the project root), copied to site/guides/<slug>/files/
# 'Found by' on a guide page: how the rows of a node were found (guide-refs 'basis'). agent: a short name the page writes
# (no namespace or folders), proposed by an agent pass, resolved to one declaration or file by a script, sample-checked
G_BASIS_T = {'exact-name': 'full name', 'exact-path': 'file path', 'exact-module': 'module name', 'unique-filename': 'file name',
             'blueprint-label': 'blueprint label', 'agent': 'short name in text'}
def gbasis(g, k):
    bs = g['basis'].get(k, set())
    out = [t for b, t in G_BASIS_T.items() if b in bs] + (['by hand'] if any(b.startswith('manual-') for b in bs) else [])
    return ', '.join(dict.fromkeys(out)) or '–'
def dist_txt(k):
    d = dist.get(k)
    return 'not reached' if d is None else '0 (main theorem)' if d == 0 else str(d)
G_DIR = os.path.join(OUT, 'guides')
for d in os.listdir(G_DIR):   # pages of guides that no longer have one (only folders this build writes: index.html inside)
    p = os.path.join(G_DIR, d)
    if os.path.isdir(p) and d != 'photos' and f'/guides/{d}/' not in GPATH.values() and os.path.exists(os.path.join(p, 'index.html')):
        for r, ds, fs in os.walk(p, topdown=False):
            for f in fs:
                os.remove(os.path.join(r, f))
            os.rmdir(r)
for g in GD:
    if not g['page']:
        continue
    path, s = GPATH[g['slug']], g['slug']
    fdir = os.path.join(G_DIR, s, 'files')
    copy = None
    if g.get('copy_plan'):
        fn, v = g['copy_plan']
        os.makedirs(fdir, exist_ok=True)
        src, dst = os.path.join(ROOT, v['local']), os.path.join(fdir, fn)
        if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(src) or open(dst, 'rb').read() != open(src, 'rb').read():
            shutil.copyfile(src, dst)
        assert os.path.getsize(dst) < 25 * 2**20, f'{dst}: over the Cloudflare Pages limit of 25 MiB per file'
        copy = (f'{path}files/{fn}', v)
    if os.path.isdir(fdir):
        for f in os.listdir(fdir):
            if not copy or f != os.path.basename(copy[0]):
                os.remove(os.path.join(fdir, f))
    name = g['name'] or 'No author named'
    vers = [vlabel(v) + (f' ({gdate(_gdate(v.get("date")))})' if _gdate(v.get('date')) else '') for v in g['versions'] if v.get('version') is not None]
    meta = [gposted(g) + '.']
    if vers:
        meta.append(f'{"Version" if len(vers) == 1 else "Versions"} read: {H(", ".join(vers))}.')
    if g['licence']:
        meta.append(f'Licence: {H(g["licence"])}.')
    acts = [f'<a class="btn" href="{H(g["url"])}">Read the original</a>']
    if copy:
        acts += [f'<a class="btn" href="{copy[0]}">Read our copy</a>', f'<a class="btn" href="{copy[0]}" download>Download</a>']
    rows = sorted(g['refs'].items(), key=lambda kv: (dist.get(kv[0], 99), ctitle(kv[0])))
    nrow = len(rows)
    if nrow:   # a guide that cites no node has no map view
        acts.append(f'<a class="btn primary" href="{H(gmapq(g))}">On the map</a>')
    tbl = ('<div class="tablewrap"><table class="gnodes"><thead><tr><th>Node</th><th>Distance from Main</th><th>Pages</th><th>Found by</th></tr></thead><tbody>'
           + ''.join(f'<tr><td><a href="{CPATH[k]}">{H(ctitle(k))}</a></td><td>{dist_txt(k)}</td><td>{grefs_html(g, page_groups(ps), g["notes"].get(k, [])) or "–"}</td><td>{H(gbasis(g, k))}</td></tr>' for k, ps in rows)
           + '</tbody></table></div>') if rows else '<p class="meta">0 nodes on the map.</p>'
    if g['from_refs']:
        how = ('Each node is a cluster of the map holding a Lean declaration or file that the guide names on that page, found by '
               'exact match of full names and file paths.')
    else:
        how = 'Each node is a cluster holding a Lean file or declaration the guide names. Pages are not mapped yet.'
    if g['from_refs'] and any('agent' in bs for bs in g['basis'].values()):
        how += (' A checked agent pass then added short-name matches: names that the page writes without their namespace or '
                'folders, each resolved by a script to one declaration or file of the archive ("short name in text"). '
                'A second run checked a sample of 20 of them per guide; the ones that failed were removed.')
    if not nrow:
        how = 'The guide names no Lean declaration or file of the archive, so no node of the map is linked to it.'
    if g['manual']:
        nm = len({k for k, _ in g['manual']})
        ev = '; '.join(dict.fromkeys(e for _, e in g['manual']))
        auto = any(k not in {k2 for k2, _ in g['manual']} for k in g['refs'])
        how = ((how + ' ') if auto else 'The guide names no Lean declaration or file of the archive. ') + \
              f'{"One node is" if nm == 1 else f"{nm} nodes are"} listed by hand, from the guide\'s own words: {ev}' + ('' if ev.rstrip('"\'”').endswith('.') else '.')
    if any(g['notes'].values()):
        how += ' Audit notes are Markdown files in the guide\'s repository that name Lean files or declarations; they are listed by file name.'
    if g['mapping_note']:
        how += ' ' + g['mapping_note']
    if copy:
        l = vlabel(copy[1])
        d_ = gdate(_gdate(copy[1].get('date')))
        how += (f' Our copy is version {l}.' if re.fullmatch(r'[\d.]+', l) else
                f' Our copy is {l}' + (f', {d_}' if d_ else '') + '.' if os.path.basename(copy[1]['local']) in l else
                f' Our copy is {os.path.basename(copy[1]["local"])} from {l}' + (f', {d_}' if d_ else '') + '.')
    companion_html = companion_md = ''
    if companion := g['companion_reading']:
        title, url, description = companion['title'], companion['url'], companion['description']
        assert url.startswith('https://'), f'guide {s}: invalid companion URL'
        companion_html = f'<p><strong>Companion reading.</strong> <a href="{H(url)}">{H(title)}</a>. {H(description)}</p>'
        companion_md = f'**Companion reading.** [{title}]({url}). {description}\n\n'
    psrcs = [x for x in (g['photo_source'], g['photo_source_also'] if g['ph96b'] else None) if x]
    photo_credit = (f'<p class="meta gcredit">{"Logos" if len(psrcs) > 1 else "Photo"}: '
                    + ', '.join(f'<a href="{H(x)}">{H(_host(x))}</a>' for x in psrcs) + '</p>' if g['ph96'] and psrcs else '')
    body = (f'<div class="crumbs"><a href="/">Map</a><span class="sep">/</span><a href="/guides/">Guides</a><span class="sep">/</span>{H(name)}</div>'
            f'<div class="eyebrow">Guide · Lean proof of the Riemann hypothesis</div>'
            f'<div class="ghead">{gav(g, 96)}<div><p class="gauth">{gauthor(g)}</p><h1>{H(g["title"])}</h1></div></div>'
            f'<p class="gmeta">{" ".join(meta)}</p><p class="gstl">{gstatus(g)}</p>{gai_html(g)}'
            f'<div class="cta gact">{"".join(acts)}</div>' + ('' if nrow else f'<p class="meta gzero">{G_ZERO}</p>') + share_btn(path, g['title'])
            + companion_html
            + f'<h2 id="nodes">Nodes in this guide <span class="n">{nrow}</span></h2>{tbl}'
            f'<h2 id="how">How we mapped it</h2><p>{H(how)}</p>'
            f'<p>Authors can correct this: post to <a href="{X_FEEDBACK}">@SomTheBuilder</a> on X.</p>{photo_credit}'
            + explore(('/guides/', 'All guides')))
    sfx = f' · {name}'
    title = g['title'] + sfx if len(g['title'] + sfx) <= TITLE_MAX else cut_title(g['title'], TITLE_MAX - len(sfx)) + sfx
    desc = meta_desc((f'{name}: a guide to the Lean proof of the Riemann hypothesis, on the map: the {nrow} '
                      f'{"cluster" if nrow == 1 else "clusters"} it cites, with the pages that cite each. ' if nrow else
                      f'{name}: a guide to the Lean proof of the Riemann hypothesis, with a link to the original. ') + g['title'] + '.')
    md = (f'# {g["title"]}\n\n{name}' + (f' ({g["home"]})' if g['home'] else '') + f'. Original: {g["url"]}'
          + (f' · posted {gdate(g["date"])}' if g['date'] else '') + (f' · versions read: {", ".join(vers)}' if vers else '')
          + (f' · licence: {g["licence"]}' if g['licence'] else '') + '\n\n'
          + G_STATUS_T[g['status']] + (f': "{" ".join(str(g["quote"]).split())}"' if g.get('quote') else '') + '\n\n'
          + (gai_md(g) + '\n\n' if g['ai'] else '')
          + (f'Our copy: {SITE}{copy[0]}\n\n' if copy else '') + (f'On the map: {SITE}{gmapq(g)}\n\n' if nrow else f'{G_ZERO}\n\n')
          + companion_md
          + f'## Nodes in this guide ({nrow})\n\n| Node | Distance from Main | Pages | Found by |\n|---|---|---|---|\n'
          + ''.join(f'| [{ctitle(k)}]({SITE}{CPATH[k]}) | {dist_txt(k)} | '
                    + (grefs_md(g, page_groups(ps), g['notes'].get(k, [])) or '–') + f' | {gbasis(g, k)} |\n' for k, ps in rows)
          + f'\n## How we mapped it\n\n{how}\n\nAuthors can correct this: post to @SomTheBuilder on X ({X_FEEDBACK}).\n'
          + (f'\n{"Logos" if len(psrcs) > 1 else "Photo"}: {", ".join(psrcs)}\n' if photo_credit else ''))
    about = {'@type': 'CreativeWork', 'name': g['title'], 'url': g['url'],
             **({'author': {'@type': 'Person', 'name': g['name'], **({'url': g['home']} if g['home'] else {})}} if g['name'] else {}),
             **({'datePublished': g['date'].isoformat()} if g['date'] else {}), **({'license': g['licence']} if g['licence'] else {})}
    page(path, title, desc, 'page', body,
         [{'@type': 'WebPage', '@id': SITE + path, 'url': SITE + path, 'name': title, 'about': about, 'isPartOf': {'@id': SITE_ID}},
          crumbs_ld(('Map', '/'), ('Guides', '/guides/'), (name, path)), ORG], .5, md=md)

# ---------- /list/: an app view (rewritten to the home page), so no HTML of its own; its Markdown copy lists every
# cluster by distance from the main theorem, so the API's "every page has a Markdown copy" holds for it too
os.makedirs(os.path.join(OUT, 'list'), exist_ok=True)
_lmd = [f'# Every cluster, as a list\n\nThe {len(CL):,} clusters of the map of the Lean proof of the Riemann hypothesis, by distance '
        f'(import steps) from the main theorem\'s cluster. Interactive list: {SITE}/list/ · data: {SITE}/api/clusters.json\n']
for d in sorted(DEPTHS) + ([None] if len(dist) < len(CL) else []):
    ks = sorted((k for k in CL if dist.get(k) == d), key=lambda k: (-fcount[k], k))
    _lmd.append(f'\n## {"Not reached from the main theorem" if d is None else "Depth 0 (the main theorem)" if d == 0 else f"Depth {d}"} '
                f'({_plural(len(ks), "cluster")})\n\n'
                + ''.join(f'- [{ctitle(k)}]({SITE}{CPATH[k]}) · {k} · {TNAME[CL[k]["theme"]]} · {fcount[k]:,} files\n' for k in ks))
open(os.path.join(OUT, 'list', 'index.md'), 'w').write(''.join(_lmd) + f'\n---\n\nEvery cluster, as a list. Web page: {SITE}/list/ · site map for machines: {SITE}/llms.txt\n')

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
# HOME_DESC: meta, og and twitter description, capped at 160 characters (Bing flags longer ones); HOME_LONG for llms.txt
HOME_DESC = f'The Lean proof of the Riemann hypothesis, mapped: {len(mod_cl):,} of its {TOTAL_FILES:,} Lean files. {ST_META_SHORT}'   # P1: the map holds the mapped files only
assert len(HOME_DESC) <= 160, f'home description is {len(HOME_DESC)} characters'
HOME_LONG = (f'The Lean proof of the Riemann hypothesis, visualized: an interactive map of its {FILES_TXT}. '
             f'{ST_META}')
home = ('<div class="eyebrow">Interactive map · Lean 4</div><h1 class="hero">The <em>Lean</em> proof of the Riemann hypothesis, mapped</h1>'
        f'<p class="lede">An interactive map of the {FILES_TXT} in Levent Alpöge\'s proof of the Riemann hypothesis, '
        f'released on 20 Nov 2026, grouped into {len(CL):,} clusters in {len(TH)} themes.</p>{STATUS}'
        f'<ul class="rows"><li><a href="/status/">Has the Riemann hypothesis been solved? Status of the proof</a></li>'
        '<li><a href="/what-is-the-riemann-hypothesis/">What is the Riemann hypothesis? Simple, student and expert</a></li>'
        '<li><a href="/how-we-know/">How we know the proof is correct</a></li><li><a href="/faq/">Frequently asked questions</a></li>'
        f'<li><a href="/core/">{H(CORE_NAV)}</a></li><li><a href="/proof-in-numbers/">{H(NUMBERS_NAV)}</a></li>'
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
     '<a href="/">Open the full map</a> or <a href="/status/">read how the proof was checked</a>.</p>')
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
    'counts': {'lean_files': TOTAL_FILES, 'mapped_files': len(mod_cl), 'unmapped_files': {'total': TOTAL_FILES - len(mod_cl), **UNMAPPED},
               'clusters': len(CL), 'themes': len(TH)},
    'note': f'Cluster and theme names and descriptions on this site are written by Claude from samples of the code and may be wrong, except the {len(CHECKED)} core clusters marked checked in /api/clusters.json, which were checked against their full Lean code.',
    'license': {'url': LICENSE, 'name': 'CC BY 4.0', 'applies_to': "everything this site made (page text, cluster and theme names and descriptions, the map layout, images and the JSON files); the Lean source keeps its own licence"},
}
jdump('status.json', API_STATUS)
API_FIELDS = [{'id': f['id'], 'name': f['name'], 'hue': f['hue'], 'description': f['description']} for f in FIELDS]
jdump('clusters.json', {'updated': DATA_DATE, 'site': SITE, 'fields': {'path': 'page on the site (prefix with site)', 'dist': 'import steps from the main theorem (null: not reachable)',
      'files': 'Lean files in the cluster', 'field': "id of the cluster's field of mathematics (that of its theme; see math_fields)",
      'era': 'decade of the newest concept the cluster needs: ' + ', '.join(n for n, _ in ERA_OF.items()),
      'era_year': 'year of that newest concept', 'level': 'highest maths level among its concepts: ' + ', '.join(n for _, n in LEVELS),
      'new_in_proof': "true if it rests on the proof's own named constructions rather than published mathematics",
      'checked': f'true for the {len(CHECKED)} core clusters whose title and description were checked against their full Lean code and corrected; false: written by Claude from a sample of the code, may be wrong'},
      'tags_note': 'field, era and level are editorial tags derived from the theme and cluster descriptions and their concept tags; they may be wrong',
      'math_fields': API_FIELDS, 'main': main, 'clusters': [
    {'id': k, 'title': NAMES[k]['title'] if k in NAMES else None, 'theme': CL[k]['theme'], 'path': CPATH[k],
     'files': fcount[k], 'dist': dist.get(k), 'field': TFIELD[CL[k]['theme']], 'era': CTAGS[k]['era'], 'era_year': CTAGS[k]['era_year'],
     'level': CTAGS[k]['level'], 'new_in_proof': CTAGS[k]['new_in_proof'], 'checked': k in CHECKED} for k in CL]})
jdump('themes.json', {'updated': DATA_DATE, 'fields': {'files': 'Lean files in the theme (all themes sum to the mapped total)',
      'units': 'units after folding wrappers and single-use helpers into the file they belong to', 'clusters': 'clusters in the theme',
      'field': 'id of the field of mathematics the theme belongs to (see math_fields in /api/clusters.json)'}, 'themes': [
    {'id': t, 'name': TNAME[t], 'blurb': TNAMED.get(t, {}).get('blurb'), 'path': TPATH[t], 'url': SITE + TPATH[t],
     'clusters': len(TH[t]['clusters']), 'files': sum(fcount[k] for k in TH[t]['clusters']), 'units': size[t], 'field': TFIELD[t]} for t in TH]})
# 35b: the checked references of the spine clusters, with precision and the checker's evidence (Lean file and line,
# what was read and where); notes marked as unread suggestions are left out, as on the pages
jdump('references.json', {'updated': max(SPINE_DATE, N3_DATE) if N3_N else SPINE_DATE, 'lean_commit': str(SPINE_Y['meta']['lean_commit']),
      'fields': {'precision': '; '.join(f'{p}: {" ".join(str(v).split())}' for p, v in SPINE_Y['meta']['precision_labels'].items()),
                 'citation': 'the work cited', 'locator': 'where in it (chapter, section, theorem)', 'url': 'link to the work (DOI where there is one)',
                 'match': 'how the cited result compares with the Lean statement, where checked',
                 'note': "the checker's caveat, if any", 'evidence': 'what the reference was checked against (Lean file and line, contents lists, the blueprint, the citing guide page)',
                 'checked': 'true: a checked reference (clusters, references); false: an automatic one (guide_citations)',
                 'basis': 'spine-check: checked for the spine (main path and core); guide-citation-judged: a guide citation judged to support the cluster, with its precision; '
                          f'guide-page-citation: "{GC_LABEL}", the work is cited on a page of an expert guide that also covers this cluster, and nobody has checked that it is about this cluster',
                 'automatic_reference': f'the book reference the site showed before the check (suggested by the AI that named the cluster); verdict: ok, partly, weak, unverified, wrong or none; shown on the page only where there is no checked reference and the verdict is not wrong',
                 'guide_citations': f'{GC_LABEL}: per cluster, the works cited on guide pages that cover it (tier 1 of tracker N3: blueprint citations and pages that cover at most 4 clusters), '
                                    'with the pages that cite them; works a judgment moved to the checked references, or judged context-only or unrelated, are left out',
                 'cited_on': 'the citing pages: guide id, guide (short name), page as the guide labels it, url of that page',
                 'guides': 'number of distinct guides that cite the work on a page covering the cluster',
                 'other_clusters': f'clusters not listed here show only an automatic reference, labelled "{AUTO_LABEL}"'},
      'clusters': [{'id': k, 'title': ctitle(k), 'path': CPATH[k], 'dist': dist.get(k), 'spine': k in SPINE,
                    'automatic_reference': {'text': next((x.get('current_book_reference') for x in SPINE_Y['clusters'] if x['id'] == k), None),
                                            'verdict': SPINE[k]['verdict'], 'shown': shown_source(k) is not None} if k in SPINE else
                                           {'text': None, 'verdict': 'not-assessed', 'shown': shown_source(k) is not None},
                    'references': [{**r, **({'note': N3_FULL_NOTE[id(r)]} if id(r) in N3_FULL_NOTE else {}), 'checked': True,
                                    'basis': r.get('basis') or 'spine-check', 'evidence': ev} for r, ev in zip(v['refs'], v['evidence'])]}
                   for k, v in sorted(CHECKED_REFS.items(), key=lambda kv: (kv[0] not in SPINE, kv[0]))],
      'guide_citations': [{'cluster': k, 'title': ctitle(k), 'path': CPATH[k], 'spine': k in SPINE, 'label': GC_LABEL,
                           'works': [{'citation': w['citation'], 'url': w['url'], 'checked': False, 'basis': 'guide-page-citation', 'guides': w['guides'],
                                      'cited_on': [{'guide': gi, 'guide_name': G_BY_ID[gi]['cite_as'], 'page': l, 'url': u} for gi, l, u in w['on']]}
                                     for w in ws]} for k, ws in sorted(GCITE.items())]})
# #10: /api/file-lines/<k>.json, the English readings of a core cluster's Lean files (data/file-lines/<k>.yaml as shown,
# pending entries left out), and /api/file-lines/index.json listing them
FL_FIELDS = {'module': 'Lean module; the file is src/<module with / for .>.lean at source_commit', 'depth': 'import steps from Main',
             'lines': 'lines of Lean in the file', 'line': 'one sentence on what the file does (written by AI, checked against the code)',
             'reading': '2 to 5 sentences on what the file establishes (written by AI, checked against the code)',
             'key_decls': 'up to 5 declarations of the file chosen by the writer: name (full Lean name) and gloss (one sentence on its statement)',
             'blueprint': "labels of Merten's blueprint (merten:) and Naskręcki's atlas (naskrecki:) entries matched to the file's declarations",
             'status': 'checked: a second pass compared every sentence with the source and found nothing to fix; fixed: it found imprecise or wrong statements and they were corrected; cut: the reading was removed (statements only)',
             'check': "the review's verdict and a note on what was changed", 'viewer': 'the file in the Lean viewer', 'page': 'the file on its cluster\'s Lean page'}
if FL:
    os.makedirs(os.path.join(OUT, 'api', 'file-lines'), exist_ok=True)
    for k in FL:
        jdump(os.path.join('file-lines', k + '.json'), {
            'cluster': k, 'title': ctitle(k), 'cluster_page': SITE + CPATH[k], 'pages': [SITE + p for p, _, _ in FL_PAGES[k]],
            'source_commit': LEAN_SHA[:8], 'source': f'{LEAN_REPO}/tree/{LEAN_SHA}', 'how': FL_HOW, 'fields': FL_FIELDS,
            'files': [{**{f: e.get(f) for f in ('module', 'depth', 'lines', 'line', 'reading', 'key_decls', 'blueprint', 'status', 'check')},
                       'viewer': f'{SITE}/file/{e["module"]}', 'page': f'{SITE}{fl_ppath(k, FL_PART[(k, e["module"])])}#{e["module"]}'} for e in FL[k]]})
    jdump(os.path.join('file-lines', 'index.json'), {'updated': DATA_DATE, 'how': FL_HOW, 'source_commit': LEAN_SHA[:8],
          'clusters': [{'id': k, 'title': ctitle(k), 'files': len(FL[k]), 'url': f'{SITE}/api/file-lines/{k}.json',
                        'pages': [SITE + p for p, _, _ in FL_PAGES[k]]} for k in FL]})
API_INDEX = {'name': SITE_NAME + ' API', 'description': 'Static JSON about the map of the Lean proof of the Riemann hypothesis.',
             'endpoints': {'/api/status.json': 'dated proof status with primary sources',
                           '/api/clusters.json': f'all {len(CL):,} clusters: id, title, theme, page, files, dist, field, era, era_year, level, new_in_proof, checked; plus math_fields, the {len(FIELDS)} fields (id, name, hue, description)',
                           '/api/themes.json': f'all {len(TH)} themes: id, name, blurb, page, clusters, files, field',
                           '/api/references.json': f'checked references for {len(CHECKED_REFS)} clusters (the {len(SPINE)} of the spine, the main path and the core, and guide citations judged to support a cluster): citation, locator, url, doi, precision (exact, section or topic), match, note, evidence, "checked": true; '
                                                   f'and guide_citations, {sum(map(len, GCITE.values()))} works on {len(GCITE)} clusters flagged "checked": false, "basis": "guide-page-citation" ({GC_LABEL.lower()})',
                           **({'/api/file-lines/index.json': f'the {len(FL)} core clusters with English readings of their Lean files: id, title, files, url, pages',
                               '/api/file-lines/{cluster}.json': f'one core cluster\'s {sum(map(len, FL.values())):,} Lean files in plain English, e.g. /api/file-lines/{main}.json: '
                                                                 'module, depth, lines, line, reading, key_decls (name, gloss), blueprint, status, check, viewer, page. ' + FL_HOW} if FL else {})},
             'tags': {'field': f'one of {len(FIELDS)} fields of mathematics per theme; a cluster takes its theme\'s field',
                      'era': 'decade of the newest concept a cluster needs: ' + ', '.join(ERA_OF),
                      'level': 'highest maths level among a cluster\'s concepts: ' + ', '.join(n for _, n in LEVELS),
                      'new_in_proof': 'the cluster rests on the proof\'s own named constructions',
                      'note': 'editorial tags derived from descriptions and concept tags; they may be wrong',
                      'map_filters': 'the map takes the same filters in its URL, e.g. /?field=av,aut&d=0-4&era=1960s&level=phd&new=1; /list/ too'},
             'markdown': 'every HTML page has a Markdown copy at <page>index.md, e.g. /status/index.md; pages with levels also have '
                         '<page>simple.md, student.md and expert.md, e.g. /what-is-the-riemann-hypothesis/student.md',
             'feeds': {'/changelog/feed.xml': 'RSS 2.0 changelog', '/sitemap.xml': 'all pages'}, 'source': GH,
             'openapi': '/api/openapi.json', 'license': API_STATUS['license']}
jdump('index.json', API_INDEX)

# /api/openapi.json: an OpenAPI 3.1 description of the files above, its schemas inferred from the JSON as written (every
# value at a position is merged: types, required keys, enums for the tag fields), so it cannot drift from the real files
def _jtype(v):
    return ('null' if v is None else 'boolean' if isinstance(v, bool) else 'integer' if isinstance(v, int) else 'number'
            if isinstance(v, float) else 'string' if isinstance(v, str) else 'array' if isinstance(v, list) else 'object')
OA_ENUMS = {'era', 'level', 'field'}   # string fields of a cluster or theme with a small fixed set of values: listed as enums
OA_NULL = {'dist', 'title', 'blurb', 'url', 'doi', 'locator', 'match', 'note', 'text'}    # item fields the code can set to null even when today's data has none
def oa_schema(vals, key=None, desc=None, item=False):
    """desc: the file's own 'fields' notes; they (and enums, nullables) apply to the fields of array items only."""
    ts = {_jtype(v) for v in vals}
    if {'integer', 'number'} <= ts: ts.discard('integer')
    if item and key in OA_NULL: ts.add('null')
    s = {'type': sorted(ts)[0] if len(ts) == 1 else sorted(ts)}
    if item and desc and key in desc: s['description'] = desc[key]
    objs = [v for v in vals if isinstance(v, dict)]
    if objs:
        keys = list(dict.fromkeys(k for o in objs for k in o))
        s['properties'] = {k: oa_schema([o[k] for o in objs if k in o], k, desc, item and key is None) for k in keys}
        req = [k for k in keys if all(k in o for o in objs)]
        if req: s['required'] = req
    arrs = [v for v in vals if isinstance(v, list)]
    if arrs:
        items = [x for a in arrs for x in a]
        s['items'] = oa_schema(items, None, desc, True) if items else {}
    strs = sorted({v for v in vals if isinstance(v, str)})
    if item and key in OA_ENUMS and strs and len(strs) <= 20: s['enum'] = strs + ([None] if 'null' in ts else [])
    return s
OA_FILES = [('index.json', 'getIndex', 'API index: the endpoints, tag meanings and licence', API_INDEX['description'], {}),
            ('status.json', 'getStatus', 'Dated status of the proof, with primary sources', API_INDEX['endpoints']['/api/status.json'], {}),
            ('clusters.json', 'getClusters', 'Every cluster', API_INDEX['endpoints']['/api/clusters.json'],
             json.load(open(os.path.join(OUT, 'api', 'clusters.json')))['fields']),
            ('themes.json', 'getThemes', 'Every theme', API_INDEX['endpoints']['/api/themes.json'],
             json.load(open(os.path.join(OUT, 'api', 'themes.json')))['fields']),
            ('references.json', 'getReferences', 'Checked references, and works cited by guides (not checked)', API_INDEX['endpoints']['/api/references.json'],
             json.load(open(os.path.join(OUT, 'api', 'references.json')))['fields'])]
if FL:
    OA_FILES.append(('file-lines/index.json', 'getFileLinesIndex', 'Core clusters with English readings of their Lean files',
                     API_INDEX['endpoints']['/api/file-lines/index.json'], {}))
OPENAPI = {
    'openapi': '3.1.0',
    'info': {'title': SITE_NAME + ' API', 'version': DATA_DATE,
             'summary': 'Static JSON about the map of the Lean proof of the Riemann hypothesis.',
             'description': ('Read-only static files, no key, no rate limit beyond normal caching (max-age 3600, CORS open). '
                             + API_STATUS['note'] + ' Era, level and new_in_proof are ' + API_INDEX['tags']['note'] + '.'),
             'license': {'name': 'CC BY 4.0', 'url': LICENSE}},
    'servers': [{'url': SITE}],
    'externalDocs': {'description': 'API index', 'url': SITE + '/api/index.json'},
    'paths': {f'/api/{f}': {'get': {'operationId': op, 'summary': summ, 'description': d,
                                    'responses': {'200': {'description': 'OK', 'content': {'application/json': {
                                        'schema': {'$ref': f'#/components/schemas/{op[3:]}'}}}}}}}
              for f, op, summ, d, _ in OA_FILES},
    'components': {'schemas': {op[3:]: oa_schema([json.load(open(os.path.join(OUT, 'api', f)))], None, desc)
                               for f, op, _, _, desc in OA_FILES}},
}
if FL:   # one templated path for the 16 files; the schema merges all of them
    OPENAPI['paths']['/api/file-lines/{cluster}.json'] = {'get': {
        'operationId': 'getFileLines', 'summary': "A core cluster's Lean files in plain English",
        'description': API_INDEX['endpoints']['/api/file-lines/{cluster}.json'],
        'parameters': [{'name': 'cluster', 'in': 'path', 'required': True, 'description': 'core cluster id',
                        'schema': {'type': 'string', 'enum': list(FL)}}],
        'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/FileLines'}}}}}}}
    OPENAPI['components']['schemas']['FileLines'] = oa_schema(
        [json.load(open(os.path.join(OUT, 'api', 'file-lines', k + '.json'))) for k in FL], None, FL_FIELDS)
jdump('openapi.json', OPENAPI)
# /api/ for people (QA16): the site's own template and CSS, the endpoints as a table and the index JSON wrapped (no sideways
# scroll). Still noindex with its canonical on /api/index.json and not in the sitemap, as before: machines read the JSON
def _apirow(u, d):   # a templated path ({cluster}) is not a link
    return (f'<tr><td><code>{H(u)}</code></td>' if '{' in u else f'<tr><td><a href="{H(u)}"><code>{H(u)}</code></a></td>') + f'<td>{H(d)}</td></tr>'
API_BODY = ('<div class="crumbs"><a href="/">Map</a><span class="sep">/</span>API</div><div class="eyebrow">API</div>'
    f'<h1>{H(API_INDEX["name"])}</h1><p class="lede">{H(API_INDEX["description"])} Plain files: no key, no rate limit, '
    f'licensed <a href="{LICENSE}">{H(API_STATUS["license"]["name"])}</a>.</p>'
    '<h2 id="endpoints">Endpoints</h2><div class="tablewrap"><table><thead><tr><th>File</th><th>What it holds</th></tr></thead><tbody>'
    + _apirow('/api/index.json', 'this index, as JSON')
    + ''.join(_apirow(u, d) for u, d in API_INDEX['endpoints'].items())
    + _apirow(API_INDEX['openapi'], 'the same endpoints as OpenAPI 3.1, with their schemas')
    + '</tbody></table></div>'
    '<h2 id="tags">Tags</h2><ul>' + ''.join(f'<li><code>{H(k)}</code>: {H(v)}</li>' for k, v in API_INDEX['tags'].items()) + '</ul>'
    '<h2 id="more">Markdown, feeds and source</h2><ul>'
    f'<li>Markdown: {H(API_INDEX["markdown"])}.</li>'
    + ''.join(f'<li><a href="{H(u)}"><code>{H(u)}</code></a>: {H(d)}</li>' for u, d in API_INDEX['feeds'].items())
    + f'<li>Source of this site: <a href="{H(API_INDEX["source"])}">{H(API_INDEX["source"].replace("https://", ""))}</a></li></ul>'
    f'<h2 id="license">Licence</h2><p><a href="{LICENSE}">{H(API_STATUS["license"]["name"])}</a>: {H(API_STATUS["license"]["applies_to"])}.</p>'
    '<h2 id="json">The index as JSON</h2><pre class="wrap"><code>' + H(json.dumps(API_INDEX, indent=2, ensure_ascii=False)) + '</code></pre>')
_t = TPL
_t = re.sub(r'<title>.*?</title>', f'<title>API · {SITE_NAME}</title>', _t, count=1)
_t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H(API_INDEX["description"])}">', _t, count=1)
_t = between(_t, '<!--head-->', '<!--/head-->', CLARITY_TAG + '\n<meta name="robots" content="noindex">\n'
             f'<link rel="canonical" href="{SITE}/api/index.json">\n<link rel="alternate" type="application/json" href="/api/index.json">\n')
_t = re.sub(r'<body data-route="[^"]*">', '<body data-route="page">', _t, count=1)
_t = between(_t, '<!--prerender-->', '<!--/prerender-->', API_BODY)
assert '{{UPDATED}}' not in _t
open(os.path.join(OUT, 'api', 'index.html'), 'w').write(_t)

# ---------- llms.txt and llms-full.txt
llms = (f'# {SITE_NAME}\n\n> {HOME_LONG}\n\n'
        f'An interactive map of the Lean proof of the Riemann hypothesis: {FILES_TXT} in {len(CL):,} clusters and {len(TH)} themes. '
        f'Names and descriptions are written by Claude from samples of the code and may be wrong, except the {len(CHECKED)} core clusters marked "Checked against the code". Every page has a Markdown copy at <page>index.md.\n\n'
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
        + f'- [Learning path: the proof step by step]({SITE}/learn/index.md)\n'
        f'- [How the proof is structured: the route to the main theorem]({SITE}/route/index.md)\n\n'
        + (f'## The core Lean files, in plain English\n\n{FL_HOW}\n\n'
           + ''.join(f'- [{ctitle(k)}: its {len(FL[k])} Lean files]({SITE}{FL_PAGES[k][0][0]}index.md)'
                     + (f' (parts: ' + ', '.join(f'{SITE}{p}index.md' for p, _, _ in FL_PAGES[k][1:]) + ')' if len(FL_PAGES[k]) > 1 else '') + '\n' for k in FL) + '\n' if FL else '')
        + f'## The map, by theme\n\n'
        + ''.join(f'- [{TNAME[t]}]({SITE}{TPATH[t]}index.md)\n' for t in sorted(TH, key=lambda t: TNAME[t]))
        + f'\n## Data\n\n- [API index]({SITE}/api/index.json): the JSON endpoints\n'
        f'- [OpenAPI description]({SITE}/api/openapi.json): the same endpoints as OpenAPI 3.1, with their schemas\n'
        f'- [Clusters]({SITE}/api/clusters.json): every cluster with its page and distance from the main theorem\n'
        f'- [Checked references]({SITE}/api/references.json): sources for the {len(SPINE)} spine clusters and {len(CHECKED_REFS) - len(SPINE)} others, each with its precision (exact, section or topic)\n'
        f'- Cited by expert guides, in the same file (guide_citations, "checked": false, "basis": "guide-page-citation"): {sum(map(len, GCITE.values()))} works on {len(GCITE)} clusters. '
        f'{GC_LABEL}: the work is cited on a guide page that also covers the cluster; it is not a checked source for the cluster\'s Lean results\n'
        + (f'- [Lean files in plain English]({SITE}/api/file-lines/index.json): the {sum(map(len, FL.values())):,} Lean files of the {len(FL)} core clusters, '
           f'one sentence and a short reading each, with key declarations; {FL_HOW} One file per cluster, e.g. {SITE}/api/file-lines/{main}.json\n' if FL else '')
        + f'- Licence: CC BY 4.0 ({LICENSE}) for everything this site made (page text, names and descriptions, map layout, images, JSON); the Lean source keeps its own licence.\n\n'
        f'## Updates\n\n- [Changelog]({SITE}/changelog/index.md) · [RSS]({SITE}/changelog/feed.xml)\n'
        f'- Full text of the key pages: {SITE}/llms-full.txt\n')
open(os.path.join(OUT, 'llms.txt'), 'w').write(llms)
# llms-full.txt: the content pages, About, Learn, /route/, and every cluster within two steps of the main theorem, in full
full = [llms, '\n---\n']
for pth in [p for p, _, _ in CONTENT_PAGES] + ['/learn/', '/route/'] + [CPATH[k] for k in sorted((k for k in CL if dist.get(k, 99) <= 2), key=lambda k: (dist[k], -fcount[k]))]:
    full += [open(os.path.join(OUT, pth.strip('/'), 'index.md')).read(), '\n---\n']
open(os.path.join(OUT, 'llms-full.txt'), 'w').write('\n'.join(full))

# ---------- sitemap (clean URLs, lastmod from the content state), robots, IndexNow key
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{d}</lastmod><priority>{p}</priority></url>\n'
              for u, p, d in sorted(URLS, key=lambda z: (-z[1], z[0]))) + '</urlset>\n')
# _redirects (Cloudflare Pages, read top-down): the app-view rewrites, then 301s from old theme and cluster paths (renamed
# themes and clusters, from TSLUG_HIST and CSLUG_HIST) to the current ones, with and without the trailing slash, and for the Markdown copies
REDIR = ('# Generated by scripts/site/build_site.py; edit there, not here.\n'
         '# Cloudflare Pages rewrites (200 = serve the home page (index.html) at the same URL; target must be "/" because Pages 308s /index.html to /; the app reads the path).\n'
         '# Clusters, themes, /about/, /learn/ and /changelog/ are real static pages; only these app views have none.\n'
         '# Any other unknown path still gets the real 404 (404.html).\n'
         '/file/*     /   200\n/concept/*  /   200\n/list       /   200\n/list/      /   200\n')
# Cloudflare Pages applies only the first 100 rules of _redirects and silently ignores the rest (found live on 24 Nov:
# rules 101-113 returned 404). So the rules are written by priority, and the build stops at REDIR_MAX: the rewrites,
# then the 301s people follow (guides' old pinned copies; renamed themes and clusters, with and without the trailing
# slash), then the Markdown copies' 301s while room is left (the build says how many are left out)
REDIR_MAX = 100
G_OLD_COPIES = {'/guides/adriazola/files/adriazola-2026-11-23.pdf': 'adriazola'}   # guides' earlier pinned copies (links already shared)
_gold = {o: f'/guides/{s}/files/{G_BY_SLUG[s]["copy_plan"][0]}' for o, s in G_OLD_COPIES.items()
         if s in G_BY_SLUG and G_BY_SLUG[s].get('copy_plan') and not o.endswith('/' + G_BY_SLUG[s]['copy_plan'][0])}
_rblocks = [('Guides: earlier pinned copies -> the copy served now (permanent)', [f'{o} {n} 301' for o, n in sorted(_gold.items())]),
            ('Renamed themes: old address -> current address (permanent)', [x for o, n in sorted(TOLD.items()) for x in (f'{o} {n} 301', f'{o.rstrip("/")} {n} 301')]),
            ('Renamed clusters: old address -> current address (permanent)', [x for o, n in sorted(COLD.items()) for x in (f'{o} {n} 301', f'{o.rstrip("/")} {n} 301')]),
            ('Markdown copies of renamed themes and clusters (permanent)', [f'{o}index.md {n}index.md 301' for o, n in sorted({**TOLD, **COLD}.items())])]
_rn = sum(1 for l in REDIR.splitlines() if l.strip() and not l.startswith('#'))
_rcut = 0
for _h, _ls in _rblocks:
    _keep = _ls[:max(0, REDIR_MAX - _rn)]
    _rcut += len(_ls) - len(_keep)
    assert _h.startswith('Markdown') or len(_keep) == len(_ls), f'_redirects: over {REDIR_MAX} rules before the Markdown 301s'
    if _keep:
        REDIR += f'\n# {_h}\n' + ''.join(l + '\n' for l in _keep)
        _rn += len(_keep)
assert _rn <= REDIR_MAX
print(f'_redirects: {_rn} rules (Cloudflare applies {REDIR_MAX})' + (f'; {_rcut} Markdown-copy 301s left out' if _rcut else ''))
open(os.path.join(OUT, '_redirects'), 'w').write(REDIR)
# G3: /data/ stays crawlable: app.js fetches it while a page renders, and Google's renderer obeys robots.txt (with it
# blocked, every rendered page showed "Could not load the map data" and /learn/ lost two thirds of its text). The app
# always adds ?v=<hash>; only the bare /data/…json URLs (found as strings in app.js, never fetched by the app) are
# blocked, with $ (end of URL) so the versioned ones still match nothing. /api/ (the public data API) stays open.
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nContent-Signal: search=yes, ai-input=yes, ai-train=yes\nAllow: /\n'
    '# the app\'s data files are fetched with ?v=<version>; the bare addresses are never used by the site\n'
    'Disallow: /data/*.json$\n'
    'Disallow: /data/*.json.gz$\n\n'
    f'Sitemap: {SITE}/sitemap.xml\n')
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

# ---------- 80a: one source download per cluster, /src/c/<id>.txt (only with --src-bundles; see the note below)
# Format: plain UTF-8 text, a 4-line header (comment lines), then the cluster's Lean files in module order, each copied
# unchanged from the local tree (the archive at LEAN_SHA) after a separator line "-- ==== <module> ====". Text rather
# than JSON: no escaping, served as text/plain with noindex by the /src/* rule in _headers, readable as it is (curl one
# URL), and it compresses as well as JSON (both ~4.8x). The separator is a Lean comment line that occurs in no source
# file (checked here); to split, cut before each line matching /^-- ==== (\S+) ====$/ and drop that line (every source
# ends with a newline, also checked). A bundle is rewritten only when its bytes change; bundles of clusters that no
# longer exist are removed. Cloudflare Pages limits: 25 MiB per file, 20,000 files per site on the free plan (checked
# below). Measured 23 Nov 2026: 2,647 bundles, 1,001 MiB in all (about 206 MiB gzipped), largest 2.34 MiB (k0952): every file
# fits, but the set is the whole archive again, 3x the rest of the site, in the site's git repo; so it is off by
# default until the owner decides (research/review-2026-11-23-code-3.md).
SRC_SEP = re.compile(r'^-- ==== (\S+) ====$', re.M)
PAGES_MAX_FILE, PAGES_MAX_FILES = 25 * 2**20, 20000
if SRC_BUNDLES:
    os.makedirs(SRC_BUNDLES, exist_ok=True)
    _nb, _tot, _big = 0, 0, (0, '')
    for k in CL:
        ms = sorted(members[k])
        parts = [f'-- RH Lean Explorer: the Lean source of cluster {k}, {ctitle(k)}\n'
                 f'-- {len(ms)} files, copied unchanged from the archive at commit {LEAN_SHA[:8]} ({LEAN_REPO}/tree/{LEAN_SHA}).\n'
                 f'-- Page: {SITE}{CPATH[k]}\n'
                 '-- Each file starts after its line "-- ==== <module> ====" (that line is not part of the file).\n']
        for m in ms:
            src = open(os.path.join(LEAN_SRC, *m.split('.')) + '.lean', encoding='utf-8').read()
            assert not SRC_SEP.search(src), f'{m}: a line looks like a bundle separator'
            assert src.endswith('\n') or not src, f'{m}: no final newline'
            parts.append(f'-- ==== {m} ====\n{src}')
        b, f = ''.join(parts).encode('utf-8'), os.path.join(SRC_BUNDLES, k + '.txt')
        assert len(b) < PAGES_MAX_FILE, f'{k}: source bundle is {len(b)} bytes, over the Cloudflare Pages limit of 25 MiB: split it'
        if not os.path.exists(f) or os.path.getsize(f) != len(b) or open(f, 'rb').read() != b:
            open(f, 'wb').write(b); _nb += 1
        _tot += len(b); _big = max(_big, (len(b), k))
    for f in glob.glob(os.path.join(SRC_BUNDLES, '*.txt')):
        if os.path.basename(f)[:-4] not in CL:
            os.remove(f)
    print(f'source bundles: {len(CL)} in {SRC_BUNDLES} ({_nb} written), {_tot / 2**20:.0f} MiB, largest {_big[1]} {_big[0] / 2**20:.2f} MiB')
_nfiles = sum(len(fs) for r, ds, fs in os.walk(OUT) if '.git' not in r.split(os.sep))
assert _nfiles < PAGES_MAX_FILES, f'{OUT} holds {_nfiles} files, over the Cloudflare Pages free-plan limit of {PAGES_MAX_FILES}'
print(f'{_nfiles} files in {OUT} (Cloudflare Pages free plan: {PAGES_MAX_FILES:,})')
