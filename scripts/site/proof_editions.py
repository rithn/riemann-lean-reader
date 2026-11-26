"""Route and provenance records used by the HTML and machine-facing views."""

import json
from pathlib import Path


PIN = Path(__file__).resolve().parents[2] / 'data/sernau/edition.json'
DEFAULT = 'sernau'
COMPARISON = '/shorter-riemann-hypothesis-proof/'
SERNAU_PASS_UTC = '2026-11-26T02:47:54Z'
SERNAU_READABLE_RESULT = 'Paranoid Comparator passed on machine B. Machine A stopped at its memory threshold.'
SERNAU_COMPACT_RESULT = 'Paranoid Comparator passed on machines A and B.'


def read_pin():
    return json.loads(PIN.read_text(encoding='utf-8'))


_pin = read_pin()
ORIGINAL = _pin['original']
ROUTES = {
    'sernau': {'map': _pin['url'], 'list': _pin['url'] + 'list/', 'route': _pin['url'] + 'route/',
               'reader': _pin['url'] + 'reader/'},
    'alpoge': {'map': '/alpoge/', 'list': '/list/', 'route': '/route/', 'reader': '/alpoge/reader/'},
}
NAMES = {'sernau': 'Sernau', 'alpoge': 'Alpöge'}
LABELS = {'sernau': _pin['label'], 'alpoge': 'Alpöge original'}
VERIFICATION_URL = _pin['verificationUrl']
VIRTUAL_ENTRIES = (
    (ROUTES['sernau']['map'] + 'file/*', ROUTES['sernau']['reader']),
    ('/file/*', ROUTES['alpoge']['reader']),
    ('/concept/*', ROUTES['alpoge']['reader']),
    (ROUTES['alpoge']['list'].rstrip('/'), ROUTES['alpoge']['list']),
)


def edition_api(edition):
    return {'default': DEFAULT, 'editions': [
        {'id': 'alpoge', 'label': LABELS['alpoge'], 'map': ROUTES['alpoge']['map'],
         'revision': ORIGINAL['revision'], 'source': ORIGINAL['repository'],
         'api': '/api/clusters.json', 'unit': 'Explorer cluster'},
        {'id': 'sernau', 'label': LABELS['sernau'], 'map': ROUTES['sernau']['map'],
         'revision': edition['revision'], 'source': edition['repository'],
         'api': edition['apiUrl'], 'unit': 'source group'},
        {'id': 'sernau-compact', 'label': 'Sernau compact', 'revision': edition['revision'],
         'source': f"{edition['repository']}/tree/{edition['revision']}/{Path(edition['compact']['sourceRoot']).parent.as_posix()}",
         'comparison': COMPARISON},
    ]}


def verification_api(edition):
    return {'revision': edition['revision'], 'as_of_utc': edition['verificationAsOf'],
            'source': edition['verificationUrl'], 'readable': SERNAU_READABLE_RESULT,
            'compact': SERNAU_COMPACT_RESULT}
