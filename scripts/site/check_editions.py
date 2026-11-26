"""Check the generated two-edition site before promoting a preview.

Run with the same Python as the generator: python -I scripts/site/check_editions.py ../site
"""
import argparse
import csv
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


def sitemap_paths(xml):
    return {urlsplit(node.text).path for node in ElementTree.fromstring(xml).findall('.//{*}loc')}


def redirects(text):
    return {tuple(line.split()) for line in text.splitlines() if line.strip() and not line.startswith('#')}


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        url = attrs.get('href') if tag in ('a', 'link') else attrs.get('src') if tag in ('img', 'script') else None
        if url:
            self.links.append(url)


def check_generated_links(site, page_paths, modules):
    virtual = {record['href'] for record in modules.values()}
    for page in page_paths:
        parser = PageLinks()
        parser.feed((site / page.strip('/') / 'index.html').read_text(encoding='utf-8'))
        for url in parser.links:
            parsed = urlsplit(url)
            if parsed.netloc not in ('', 'riemannhypothesissolved.com') or not parsed.path.startswith('/'):
                continue
            path = unquote(parsed.path)
            if path.startswith(('/file/', '/concept/')) or path in virtual:
                continue
            target = site / path.lstrip('/')
            assert target.is_file() or (target / 'index.html').is_file(), (page, url)


def check_original_baseline(site, revision, paths, new_paths, rules):
    def original(path):
        return subprocess.check_output(['git', '-C', str(site), 'show', f'{revision}:{path}'])

    old_paths = sitemap_paths(original('sitemap.xml'))
    assert paths == old_paths | new_paths, (
        f'Sitemap removed {sorted(old_paths - paths)} and added {sorted(paths - old_paths - new_paths)} '
        f'beyond the expected new pages. Expected new pages missing: {sorted(new_paths - paths)}'
    )
    old_rules = redirects(original('_redirects').decode())
    assert old_rules - rules == {('/list/', '/', '200')}, 'Unexpected removal of a legacy redirect'
    assert rules - old_rules == {('/sernau/file/*', '/sernau/reader/', '200')}, 'Unexpected new rewrites'
    # Updated share-card images change ogv independently of the original map or taxonomy.
    old_overview = json.loads(original('data/overview.json'))
    new_overview = json.loads((site / 'data/overview.json').read_bytes())
    old_overview.pop('ogv')
    new_overview.pop('ogv')
    assert old_overview == new_overview, 'Original map overview changed'
    for name in ('api/clusters.json', 'api/themes.json', 'api/references.json', 'api/file-lines/index.json'):
        assert (site / name).read_bytes() == original(name), f'Original map output changed: {name}'
    subprocess.run(['git', '-C', str(site), 'diff', '--exit-code', '--quiet', revision, '--',
                    'data/c', 'data/lean', 'api/file-lines', 'src', ':(exclude)src/sernau'], check=True)


def check(site, baseline=None):
    def read_json(url):
        return json.loads((site / url.lstrip('/')).read_text(encoding='utf-8'))

    registry = read_json('/api/editions.json')
    assert registry['default'] == 'alpoge'
    editions = {record['id']: record for record in registry['editions']}
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
    assert len(modules) == edition['totals']['modules']
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
    assert len(graph['edges']) == edition['totals']['groupEdges']
    assert sum(len(module['imports']) for module in covered.values()) == edition['totals']['moduleEdges']
    for edge in graph['edges']:
        assert edge['evidence'], edge
        for reference in edge['evidence']:
            assert covered[reference['from']]['group'] == edge['from']
            assert covered[reference['to']]['group'] == edge['to']
            assert reference in covered[reference['from']]['imports']
            assert reference in covered[reference['to']]['importers']

    content_paths = {'/sernau/', '/sernau/route/', '/shorter-riemann-hypothesis-proof/'}
    for url in content_paths:
        assert url in paths
        assert (site / url.strip('/') / 'index.md').is_file()
    assert '/sernau/reader/' not in paths and '/sernau/list/' not in paths
    assert sum(x.startswith('/cluster/') and '/lean/' not in x for x in paths) == 2647
    assert sum(x.startswith('/theme/') for x in paths) == 63
    assert sum(x.startswith('/cluster/') and '/lean/' in x for x in paths) == 27

    original = (site / 'src/Main.lean').read_text().splitlines()
    readable = (site / modules['Main']['raw'].lstrip('/')).read_text().splitlines()
    assert 'rhOfAll' in original[3] and 'New.zeta_zeros_on_line New.grh' in readable[4]
    rules = redirects((site / '_redirects').read_text(encoding='utf-8'))
    assert ('/sernau/file/*', '/sernau/reader/', '200') in rules
    assert ('/file/*', '/', '200') in rules
    assert len(rules) <= 100
    assert (site / 'sernau/reader/index.html').is_file()
    assert (site / 'list/index.html').is_file()
    check_generated_links(site, [
        '/shorter-riemann-hypothesis-proof/', '/sernau/', '/sernau/list/', '/sernau/route/',
        '/sernau/reader/', *(group['href'] for group in graph['groups']),
    ], modules)
    openapi = read_json('/api/openapi.json')
    api_index = read_json('/api/index.json')
    for endpoint in ('/api/editions.json', editions['sernau']['api'], info['groups'], info['modules'], info['theorems']):
        assert endpoint in openapi['paths'] and endpoint in api_index['endpoints'], endpoint
    if baseline:
        new_paths = content_paths | {group['href'] for group in graph['groups']}
        check_original_baseline(site, baseline, paths, new_paths, rules)
    print(f"Checked {len(modules)} readable files, {len(graph['groups'])} groups and both editions’ routes and entry sources.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--baseline-revision', help='Site Git revision to compare against')
    args = parser.parse_args()
    check(args.site, args.baseline_revision)
