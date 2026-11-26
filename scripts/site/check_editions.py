"""Check the generated two-edition site before promoting a preview.

Run with the same Python as the generator: python -I scripts/site/check_editions.py ../site
"""
import argparse
import csv
from fnmatch import fnmatchcase
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


VIRTUAL_REWRITES = {
    ('/file/*', '/alpoge/reader/', '200'),
    ('/concept/*', '/alpoge/reader/', '200'),
    ('/list', '/list/', '200'),
    ('/sernau/file/*', '/sernau/reader/', '200'),
}


def sitemap_paths(xml):
    return {urlsplit(node.text).path for node in ElementTree.fromstring(xml).findall('.//{*}loc')}


def redirects(text):
    return {tuple(line.split()) for line in text.splitlines() if line.strip() and not line.startswith('#')}


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.editions = {}
        self.scripts = []
        self.body = {}
        self.canonical = None
        self.robots = ''
        self.description = ''

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'body':
            self.body = attrs
        if tag == 'a' and 'data-edition-link' in attrs:
            edition = attrs['data-edition']
            assert edition not in self.editions, f'Duplicate initial link for {edition}'
            self.editions[edition] = (attrs['href'], attrs.get('aria-current'))
        if tag == 'script' and 'src' in attrs:
            self.scripts.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = urlsplit(attrs['href']).path
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.robots = attrs['content']
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = attrs['content']
        url = attrs.get('href') if tag in ('a', 'link') else attrs.get('src') if tag in ('img', 'script') else None
        if url:
            self.links.append(url)


def load_page(site, page):
    parser = PageLinks()
    parser.feed((site / page.strip('/') / 'index.html').read_text(encoding='utf-8'))
    return parser


def check_generated_links(site, page_paths, modules):
    virtual = {record['href'] for record in modules.values()}
    for page in page_paths:
        parser = load_page(site, page)
        for url in parser.links:
            parsed = urlsplit(url)
            if parsed.netloc not in ('', 'riemannhypothesissolved.com') or not parsed.path.startswith('/'):
                continue
            path = unquote(parsed.path)
            if path.startswith(('/file/', '/concept/')) or path in virtual:
                continue
            target = site / path.lstrip('/')
            assert target.is_file() or (target / 'index.html').is_file(), (page, url)


def check_shells(site):
    surfaces = {
        '/': ('sernau', 'map'),
        '/sernau/': ('sernau', 'map'),
        '/alpoge/': ('alpoge', 'map'),
        '/sernau/list/': ('sernau', 'list'),
        '/list/': ('alpoge', 'list'),
        '/sernau/route/': ('sernau', 'route'),
        '/route/': ('alpoge', 'route'),
        '/sernau/reader/': ('sernau', 'reader'),
        '/alpoge/reader/': ('alpoge', 'reader'),
    }
    descriptions = set()
    for page, (edition, view) in surfaces.items():
        html = load_page(site, page)
        assert html.body['data-edition'] == edition and html.body['data-view'] == view, page
        assert any(script.startswith('/explorer-shell.') for script in html.scripts), page
        destinations = {
            'list': ('/sernau/list/', '/list/'),
            'route': ('/sernau/route/', '/route/'),
        }.get(view, ('/sernau/', '/alpoge/'))
        assert html.editions == {
            key: (href, 'page' if key == edition else None)
            for key, href in zip(('sernau', 'alpoge'), destinations)
        }, (page, html.editions)
        if view in ('map', 'route'):
            assert html.canonical == page and 'noindex' not in html.robots, page
        if view == 'map':
            assert html.description and html.description not in descriptions, page
            descriptions.add(html.description)
        if view in ('list', 'reader'):
            assert 'noindex' in html.robots, page

    home = load_page(site, '/')
    assert {'/sernau/', '/alpoge/', '/sernau/list/', '/list/', '/sernau/route/', '/route/',
            '/sernau/file/Main#riemannHypothesis', '/file/Main#riemannHypothesis'} <= set(home.links)
    comparison = load_page(site, '/shorter-riemann-hypothesis-proof/')
    assert not comparison.editions
    assert {'/sernau/', '/alpoge/'} <= set(comparison.links)
    headers = (site / '_headers').read_text(encoding='utf-8')
    immutable = [line.splitlines()[0] for line in headers.split('\n/') if 'max-age=31536000, immutable' in line]
    for page in ('/', '/alpoge/'):
        for asset in load_page(site, page).scripts:
            if asset.startswith('/explorer-'):
                assert any(fnmatchcase(asset.lstrip('/'), pattern) for pattern in immutable), asset


def check_original_baseline(site, revision, paths, rules):
    def original(path):
        return subprocess.check_output(['git', '-C', str(site), 'show', f'{revision}:{path}'])

    old_paths = sitemap_paths(original('sitemap.xml'))
    new_paths = {'/alpoge/'}
    assert paths == old_paths | new_paths, (
        f'Sitemap removed {sorted(old_paths - paths)} and added {sorted(paths - old_paths - new_paths)} '
        f'beyond the expected new pages. Expected new pages missing: {sorted(new_paths - paths)}'
    )
    old_rules = redirects(original('_redirects').decode())
    assert {rule for rule in old_rules if rule[2] == '301'} == {rule for rule in rules if rule[2] == '301'}, (
        'Published redirect targets changed'
    )
    # Updated share-card images change ogv independently of the original map or taxonomy.
    old_overview = json.loads(original('data/overview.json'))
    new_overview = json.loads((site / 'data/overview.json').read_bytes())
    old_overview.pop('ogv', None)
    new_overview.pop('ogv', None)
    assert old_overview == new_overview, 'Original map overview changed'
    for name in ('api/clusters.json', 'api/themes.json', 'api/references.json', 'api/file-lines/index.json'):
        assert (site / name).read_bytes() == original(name), f'Original map output changed: {name}'
    assets = subprocess.check_output(['git', '-C', str(site), 'ls-tree', '--name-only', revision], text=True)
    for name in assets.splitlines():
        if name.count('.') == 2 and name.startswith(('app.', 'style.', 'sernau.')):
            assert (site / name).read_bytes() == original(name), f'Cached release asset changed: {name}'
    subprocess.run(['git', '-C', str(site), 'diff', '--exit-code', '--quiet', revision, '--',
                    'data/c', 'data/lean', 'api/file-lines', 'src', ':(exclude)src/sernau'], check=True)


def check(site, baseline=None):
    def read_json(url):
        return json.loads((site / url.lstrip('/')).read_text(encoding='utf-8'))

    registry = read_json('/api/editions.json')
    assert registry['default'] == 'sernau'
    editions = {record['id']: record for record in registry['editions']}
    assert {name: record['map'] for name, record in editions.items() if 'map' in record} == {
        'alpoge': '/alpoge/', 'sernau': '/sernau/',
    }
    assert editions['alpoge']['revision'] != editions['sernau']['revision']

    info = read_json(editions['sernau']['api'])
    edition = info['edition']
    modules = read_json(info['modules'])['modules']
    graph = read_json(info['groups'])
    paths = sitemap_paths((site / 'sitemap.xml').read_text(encoding='utf-8'))
    with (Path(__file__).resolve().parents[2] / 'data/sernau/modules.tsv').open(encoding='utf-8') as stream:
        inputs = {row['module']: row for row in csv.DictReader(stream, delimiter='\t')}

    assert read_json(edition['manifestUrl']) == edition
    assert read_json(edition['modulesUrl'])['modules'] == modules
    assert read_json(edition['overviewUrl'])['edges'] == graph['edges']
    assert set(inputs) == set(modules)
    assert len(modules) == edition['totals']['modules'] == 803
    assert len(graph['groups']) == edition['totals']['groups'] == 29
    for name, expected in modules.items():
        raw = (site / expected['raw'].lstrip('/')).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected['sha256'] == inputs[name]['sha256'], name
        assert expected['raw'].startswith('/src/sernau/' + edition['revision'] + '/'), name
        assert expected['href'] not in paths, name

    covered = {}
    for group in graph['groups']:
        path = group['href']
        assert path in paths and (site / path.strip('/') / 'index.md').is_file(), path
        detail = read_json(group['dataUrl'])
        assert detail['edition']['revision'] == edition['revision'], path
        assert set(detail['modules']) == set(group['modules']), path
        assert not covered.keys() & detail['modules'].keys()
        covered.update(detail['modules'])
    assert covered.keys() == modules.keys()
    assert len(graph['edges']) == edition['totals']['groupEdges'] == 189
    assert sum(len(module['imports']) for module in covered.values()) == edition['totals']['moduleEdges']
    file_graph = read_json(edition['fileGraphUrl'])
    assert file_graph['edition'] == {key: edition[key] for key in ('id', 'revision', 'buildId')}
    group_ids = {group['id'] for group in graph['groups']}
    assert file_graph['groupLabels'].keys() == file_graph['groupCenters'].keys() == group_ids
    assert len({tuple(center) for center in file_graph['groupCenters'].values()}) == len(group_ids)
    names = [name for name, _, _ in file_graph['files']]
    assert len(names) == len(modules) and set(names) == modules.keys()
    assert all([label, depth] == [modules[name]['label'], modules[name]['depth']]
               for name, label, depth in file_graph['files'])
    imports = [(names[source], names[target], line) for source, target, line in file_graph['imports']]
    assert len(imports) == len(set(imports)) == 1733
    assert set(imports) == {(edge['from'], edge['to'], edge['line'])
                            for module in covered.values() for edge in module['imports']}
    for edge in graph['edges']:
        assert edge['evidence'], edge
        for reference in edge['evidence']:
            assert covered[reference['from']]['group'] == edge['from']
            assert covered[reference['to']]['group'] == edge['to']
            assert reference in covered[reference['from']]['imports']
            assert reference in covered[reference['to']]['importers']

    content_paths = {'/', '/alpoge/', '/sernau/', '/sernau/route/', '/shorter-riemann-hypothesis-proof/'}
    for url in content_paths:
        assert url in paths
        assert (site / url.strip('/') / 'index.md').is_file()
    assert not paths & {'/alpoge/reader/', '/sernau/reader/', '/list/', '/sernau/list/'}
    assert sum(x.startswith('/cluster/') and '/lean/' not in x for x in paths) == 2647
    assert sum(x.startswith('/theme/') for x in paths) == 63
    assert sum(x.startswith('/cluster/') and '/lean/' in x for x in paths) == 27

    original = (site / 'src/Main.lean').read_text().splitlines()
    readable = (site / modules['Main']['raw'].lstrip('/')).read_text().splitlines()
    assert 'rhOfAll' in original[3] and 'New.zeta_zeros_on_line New.grh' in readable[4]
    theorems = read_json(info['theorems'])['theorems']
    with (Path(__file__).resolve().parents[2] / 'data/sernau/theorems.json').open(encoding='utf-8') as stream:
        statements = json.load(stream)
    assert len(theorems) == len(statements) == 5
    for record, theorem in zip(statements, theorems):
        name = record['name']
        assert theorem['name'] == name
        for key, registry_key, prefix, source in (
            ('original', 'alpoge', '/file/Main#', original), ('sernau', 'sernau', '/sernau/file/Main#', readable),
        ):
            target = theorem['editions'][key]
            assert target['href'] == prefix + name and target['revision'] == editions[registry_key]['revision'], name
            assert f'theorem {name} ' in source[target['line'] - 1], name
            assert f"/blob/{target['revision']}/" in target['github'] and target['github'].endswith(f"#L{target['line']}"), name
    rh = next(theorem for theorem in theorems if theorem['name'] == 'riemannHypothesis')
    grh = next(reference for reference in rh['references'] if reference['name'] == 'New.grh')
    assert grh['href'] == '/sernau/file/New.Reduction.OneSidedBound#New.grh' and grh['line'] == 239
    grh_source = (site / modules[grh['module']]['raw'].lstrip('/')).read_text().splitlines()
    assert 'theorem grh ' in grh_source[238]
    rules = redirects((site / '_redirects').read_text(encoding='utf-8'))
    assert {rule for rule in rules if rule[2] == '200'} == VIRTUAL_REWRITES
    for _, target, _ in VIRTUAL_REWRITES:
        assert (site / target.strip('/') / 'index.html').is_file(), target
    assert len(rules) <= 100
    check_shells(site)
    check_generated_links(site, [
        '/', '/alpoge/', '/shorter-riemann-hypothesis-proof/', '/sernau/', '/sernau/list/', '/sernau/route/',
        '/sernau/reader/', *(group['href'] for group in graph['groups']),
    ], modules)
    openapi = read_json('/api/openapi.json')
    api_index = read_json('/api/index.json')
    for endpoint in ('/api/editions.json', editions['sernau']['api'], info['groups'], info['modules'], info['theorems']):
        assert endpoint in openapi['paths'] and endpoint in api_index['endpoints'], endpoint
    if baseline:
        check_original_baseline(site, baseline, paths, rules)
    print(f"Checked {len(modules)} readable files, {len(graph['groups'])} groups and both editions’ routes and entry sources.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--baseline-revision', help='Site Git revision to compare against')
    args = parser.parse_args()
    check(args.site, args.baseline_revision)
