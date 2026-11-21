"""Find the key papers behind each name cited in the note, via the OpenAlex API (no key).

usage: uv run -q python -I scripts/sources/find_papers.py <out_dir>

One search per name (OpenAlex's free budget is ~100 requests/day per IP), most-cited
first, 5 results each. Queries put each name in the context the note uses it in.
Writes <out_dir>/papers.json: {name: {step, query, papers: [...]}}, with title, year,
authors, citations, doi, abstract (rebuilt from OpenAlex's word index) and reference ids.
Only mathematical terms are sent; nothing about the user or this project.
"""
import json, os, sys, time, urllib.parse, urllib.request

NAMES = {  # name: (what the note uses it for, search query)
    'Stepanov': ('core analogy: auxiliary polynomial with multiplicity (RH for curves)', 'Stepanov method auxiliary polynomial curves finite fields Riemann hypothesis'),
    'Bombieri': ('standard exposition of Stepanov', 'Bombieri counting points on curves over finite fields Stepanov'),
    'Weil (curves)': ('RH over function fields', 'Weil Riemann hypothesis curves over finite fields'),
    'Deligne': ('Weil conjectures', 'Deligne Weil conjectures proof'),
    'Guinand-Weil': ('explicit formula; "had the sign"', 'Weil explicit formula positivity criterion Riemann hypothesis'),
    'Katz': ('exponential sums, square-root cancellation', 'Katz exponential sums monodromy'),
    'Gabber': ('hypersurface in Katz argument', 'Gabber Katz exponential sums hypersurface'),
    'Theta lifts (Howe)': ('chain of theta lifts mimicking multiplicity', 'theta correspondence Howe duality'),
    'Rallis': ('seesaw, Rallis inner product', 'Rallis inner product formula theta lifting'),
    'Kudla (seesaw)': ('seesaw dual pairs', 'Kudla seesaw dual reductive pairs'),
    'Gan-Gross-Prasad': ('GGP / Bessel periods', 'Gan Gross Prasad conjecture Bessel periods'),
    'Ichino-Ikeda': ('period formulas for GGP', 'Ichino Ikeda periods automorphic forms'),
    'Siegel (mass)': ('Siegel mass formula', 'Siegel mass formula quadratic forms'),
    'Siegel-Weil': ('theta integrals = Eisenstein series', 'Siegel-Weil formula'),
    'Chowla-Selberg': ('divisibility of lift norms', 'Chowla Selberg formula CM periods'),
    'Weyl': ('equidistribution / Weyl law in divisibility step', 'Weyl equidistribution exponential sums'),
    'Iwasawa': ('Iwasawa tower (pigeonhole analogy)', 'Iwasawa theory cyclotomic towers'),
    'Bost': ('Bost slope inequality', 'Bost slope inequality Arakelov'),
    'Vandiver': ('weakening of Vandiver conjecture', 'Vandiver conjecture class groups cyclotomic'),
    'Lichtenbaum': ('K-groups of Z', 'Lichtenbaum conjecture K-theory special values'),
    'Behrend': ('choice of Iwasawa tower', 'Behrend sets without arithmetic progressions'),
    'Kazhdan-Patterson': ('theta on n-fold covers of GL_n', 'Kazhdan Patterson metaplectic forms'),
    'Heath-Brown-Patterson': ('Gauss sums via theta on covers of GL2', 'Heath-Brown Patterson cubic Gauss sums distribution'),
    'Jacquet (RTF)': ('relative trace formula', 'Jacquet relative trace formula'),
    'Poincare series': ('norm of projected Poincare series', 'Poincare series Kloosterman sums spectral'),
    'Turan': ('power-sum method, "Turan over n"', 'Turan power sum method zeros zeta function'),
    'Mehta': ('Mehta-like integral', 'Mehta integral Selberg integral'),
    'Bertini': ('Bertini, definite sign from middle cohomology', 'Bertini theorem hypersurfaces finite fields'),
    'Borger': ('F1 via Lambda-rings', 'Borger Lambda-rings field with one element'),
    'Balaban': ('Balaban induction (renormalisation group)', 'Balaban renormalization group lattice gauge'),
    'Dirichlet / GRH': ('the target: GRH for Dirichlet L-functions', 'generalized Riemann hypothesis Dirichlet L-functions zeros'),
    'von Mangoldt': ('the von Mangoldt sum of length X', 'von Mangoldt function explicit formula prime number theorem'),
    'Hecke characters': ('Hecke characters, CM', 'Hecke characters Grossencharacters L-functions'),
}

out = sys.argv[1]; os.makedirs(out, exist_ok=True)
path = os.path.join(out, 'papers.json')
res = json.load(open(path)) if os.path.exists(path) else {}
F = 'id,doi,display_name,publication_year,cited_by_count,authorships,abstract_inverted_index,referenced_works'
for name, (step, q) in NAMES.items():
    if name in res:
        continue
    url = 'https://api.openalex.org/works?' + urllib.parse.urlencode(
        {'search': q, 'sort': 'relevance_score:desc', 'per-page': 5, 'select': F})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'lean-reader-research'}), timeout=60))
    except Exception as e:
        print(name, 'FAILED', e); break
    ps = []
    for w in d.get('results', []):
        inv = w.get('abstract_inverted_index') or {}
        pos = sorted((p, t) for t, ps_ in inv.items() for p in ps_)
        ps.append({'id': w['id'].rsplit('/', 1)[-1], 'title': w['display_name'], 'year': w['publication_year'],
                   'cites': w['cited_by_count'], 'doi': w.get('doi'),
                   'authors': [a['author']['display_name'] for a in w.get('authorships', [])][:4],
                   'abstract': ' '.join(t for _, t in pos),
                   'refs': [r.rsplit('/', 1)[-1] for r in w.get('referenced_works') or []]})
    res[name] = {'step': step, 'query': q, 'papers': ps}
    json.dump(res, open(path, 'w'), indent=1)
    print(f"{name}: {len(ps)} papers; top: {ps[0]['title'][:70] if ps else '-'} ({ps[0]['year'] if ps else ''})", flush=True)
    time.sleep(0.3)
