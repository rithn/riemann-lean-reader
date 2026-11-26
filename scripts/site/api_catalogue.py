"""The static API catalogue and schemas derived from published payloads."""

from dataclasses import dataclass
import json

from proof_editions import DEFAULT, LABELS, ROUTES


@dataclass(frozen=True)
class Endpoint:
    file: str
    operation: str
    summary: str
    descriptions: bool = False
    keyed_records: str | None = None

    @property
    def url(self):
        return '/api/' + self.file

    @property
    def schema(self):
        return self.operation.removeprefix('get')


CORE_ENDPOINTS = (
    Endpoint('index.json', 'getIndex', 'API index: the endpoints, tag meanings and licence'),
    Endpoint('status.json', 'getStatus', 'Dated status of the proof, with primary sources'),
    Endpoint('clusters.json', 'getClusters', 'Every cluster', descriptions=True),
    Endpoint('themes.json', 'getThemes', 'Every theme', descriptions=True),
    Endpoint('references.json', 'getReferences', 'Checked references, and works cited by guides (not checked)',
             descriptions=True),
)
READINGS_INDEX = Endpoint('file-lines/index.json', 'getFileLinesIndex',
                          'Core clusters with English readings of their Lean files')
EDITION_ENDPOINTS = (
    Endpoint('editions.json', 'getEditions', 'Proof editions and source revisions. '
             f'Home defaults to {LABELS[DEFAULT]}. Use {ROUTES["sernau"]["map"]} or {ROUTES["alpoge"]["map"]} for explicit maps.'),
    Endpoint('sernau/index.json', 'getSernauIndex', 'Readable edition data and provenance'),
    Endpoint('sernau/groups.json', 'getSernauGroups', 'Readable source groups and their dependencies'),
    Endpoint('sernau/modules.json', 'getSernauModules', 'Readable Lean modules and source links', keyed_records='modules'),
    Endpoint('sernau/theorems.json', 'getSernauTheorems', 'Five headline theorem declarations in the readable edition'),
)


def register_edition_endpoints(index):
    index['endpoints'].update({endpoint.url: endpoint.summary for endpoint in EDITION_ENDPOINTS})


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


def endpoint_schema(endpoint, payload):
    descriptions = payload['fields'] if endpoint.descriptions else None
    if not endpoint.keyed_records:
        return oa_schema([payload], desc=descriptions)
    field = endpoint.keyed_records
    parent = {key: value for key, value in payload.items() if key != field}
    schema = oa_schema([parent], desc=descriptions)
    schema['properties'][field] = {'type': 'object', 'additionalProperties': oa_schema(list(payload[field].values()))}
    schema['required'].append(field)
    return schema


def operation(operation_id, summary, description, schema, parameters=None):
    get = {'operationId': operation_id, 'summary': summary, 'description': description}
    if parameters:
        get['parameters'] = parameters
    get['responses'] = {'200': {'description': 'OK', 'content': {'application/json': {
        'schema': {'$ref': f'#/components/schemas/{schema}'}}}}}
    return {'get': get}


def openapi_document(api_dir, index, status, *, date, site, license_url, reading_clusters, reading_fields):
    endpoints = (*CORE_ENDPOINTS, *((READINGS_INDEX,) if reading_clusters else ()), *EDITION_ENDPOINTS)
    paths, schemas = {}, {}
    for endpoint in endpoints:
        description = index['description'] if endpoint.file == 'index.json' else index['endpoints'][endpoint.url]
        paths[endpoint.url] = operation(endpoint.operation, endpoint.summary, description, endpoint.schema)
        payload = json.loads((api_dir / endpoint.file).read_text(encoding='utf-8'))
        schemas[endpoint.schema] = endpoint_schema(endpoint, payload)
    if reading_clusters:
        readings_path = '/api/file-lines/{cluster}.json'
        parameters = [{'name': 'cluster', 'in': 'path', 'required': True, 'description': 'core cluster id',
                       'schema': {'type': 'string', 'enum': list(reading_clusters)}}]
        paths[readings_path] = operation('getFileLines', "A core cluster's Lean files in plain English",
                                        index['endpoints'][readings_path], 'FileLines', parameters)
        readings = [json.loads((api_dir / 'file-lines' / f'{cluster}.json').read_text(encoding='utf-8'))
                    for cluster in reading_clusters]
        schemas['FileLines'] = oa_schema(readings, desc=reading_fields)
    return {
        'openapi': '3.1.0',
        'info': {'title': index['name'], 'version': date,
                 'summary': 'Static JSON about the map of the Lean proof of the Riemann hypothesis.',
                 'description': ('Read-only static files, no key, no rate limit beyond normal caching (max-age 3600, CORS open). '
                                 + status['note'] + ' Era, level and new_in_proof are ' + index['tags']['note'] + '.'),
                 'license': {'name': 'CC BY 4.0', 'url': license_url}},
        'servers': [{'url': site}],
        'externalDocs': {'description': 'API index', 'url': site + '/api/index.json'},
        'paths': paths,
        'components': {'schemas': schemas},
    }
