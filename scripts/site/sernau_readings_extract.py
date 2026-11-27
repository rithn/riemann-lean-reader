"""Refresh mechanical Sernau readings from the pinned local source.

Selection: prefer a declaration named in the module introduction or matching the
file basename; then prefer theorem/lemma over definitions, with later source
lines breaking ties. Only declarations with a literal ` :=` header are eligible.
Pilot and explorer-draft records are never rewritten. No network is used.
"""
from collections import Counter
import csv
import json
from pathlib import Path
import re
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sernau_data as sd

ROOT = sd.REPO
INPUT = sd.INPUTS
SOURCE = ROOT.parent / 'site-sharing' / 'src' / 'sernau' / '72fead102f663d5c7a407964a13dc0cf9d977207'
WORD = re.compile(r"[^\W_]+(?:[.'’-][^\W_]+)*", re.UNICODE)


def comment(source, first_decl):
    lines = source.splitlines(keepends=True)
    match = re.search(r'(?m)^/-!', ''.join(lines[:first_decl - 1]))
    if not match:
        return None
    start = match.end()
    depth, pos = 1, start
    while depth and pos < len(source) - 1:
        token = source[pos:pos + 2]
        if token == '/-':
            depth += 1
            pos += 2
        elif token == '-/':
            depth -= 1
            if not depth:
                break
            pos += 2
        else:
            pos += 1
    if depth:
        raise ValueError('Unclosed module comment')
    begin = source.count('\n', 0, start) + 2
    end = source.count('\n', 0, pos)
    return begin, end, lines


def extract(row, module, modules, source, revision):
    lines = source.splitlines(keepends=True)
    eligible = []
    for d in module['declarations']:
        header, sep, _ = ''.join(lines[d['line'] - 1:d['endLine']]).partition(' :=')
        if sep:
            eligible.append((d, header))
    if not eligible:
        raise ValueError('No supported declaration signature: ' + row['module'])
    found = comment(source, module['declarations'][0]['line'])
    intro = ''.join(found[2][found[0]-1:found[1]]) if found else ''
    basename = row['module'].split('.')[-1].lower()
    def rank(item):
        d = item[0]
        leaf = d['name'].split('.')[-1]
        return (leaf in intro, leaf.lower() == basename, d['kind'] in ('theorem', 'lemma'), d['line'])
    d, signature = max(eligible, key=rank)
    route = []
    reverse = list(reversed(module['route']))
    for current, importer in zip(reverse, reverse[1:]):
        edge = next(e for e in modules[importer]['imports'] if e['to'] == current)
        route.append(dict(module=current, importer=importer, line=edge['line']))
    route.append(dict(module='Main'))
    record = dict(group=row['group'], revision=revision, origin='upstream', review='pending',
                  mechanical=True, declarations=[dict(module=row['module'], name=d['name'], line=d['line'], signature=signature)],
                  routeToMain=route, outsideReadings=[])
    if not found:
        record.update(needs_draft=True, reason='Missing opening module comment')
        return record
    begin, end, _ = found
    start = sum(len(line) for line in lines[:begin - 1])
    limit = sum(len(line) for line in lines[:end])
    while start < limit:
        line_end = source.find('\n', start, limit)
        line_end = limit if line_end < 0 else line_end + 1
        if source[start:line_end].strip() and not source[start:line_end].lstrip().startswith('#'):
            break
        start = line_end
    body = source[start:limit]
    # Sentence punctuation must be followed by whitespace or the end of the comment.
    ends = [m.end() for m in re.finditer(r"[.!?][\u201d\"')\]]*(?=\s|$)", body)]
    candidates = [i for i in ends if 40 <= len(WORD.findall(body[:i])) <= 180]
    paragraph = re.search(r'\n[ \t]*\n', body)
    paragraph_end = len(body[:paragraph.start()].rstrip()) if paragraph else len(body.rstrip())
    if paragraph_end in candidates:
        stop = paragraph_end
    else:
        stop = candidates[0] if candidates else None
    def span(a, b):
        return dict(path=row['path'], line=source.count('\n', 0, a) + 1,
                    endLine=source.count('\n', 0, b - 1) + 1,
                    startOffset=a, endOffset=b, text=source[a:b])
    if stop is not None:
        record['excerpt'] = span(start, start + stop)
        if start + stop < limit:
            record['remainder'] = span(start + stop, limit)
        if re.search(r'\b(?:TODO|FIXME)\b', record['excerpt']['text'], re.I):
            record.update(needs_draft=True, reason='Excerpt contains a TODO or FIXME')
        elif not re.search(r'\b(?:file|we|prove[sd]?|show[sn]?|defin(?:e|es|ed)|construct(?:s|ed)?|theorem|lemma|establish(?:es|ed)?|provides?|is|are)\b', record['excerpt']['text'], re.I):
            record.update(needs_draft=True, reason='Excerpt may not be a standalone description')
    else:
        record.update(needs_draft=True, reason='No 40–180 word excerpt ends at a sentence boundary')
    return record


def main():
    edition = json.loads((INPUT / 'edition.json').read_text())
    edition['rawBaseUrl'] = '/src/sernau/' + edition['revision'] + '/'
    groups_list = json.loads((INPUT / 'groups.json').read_text())
    groups = {g['id']: g for g in groups_list}
    with (INPUT / 'modules.tsv').open() as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    files = {r['path']: (SOURCE / r['path'].removeprefix('grh/src/')).read_bytes() for r in rows}
    for g in groups_list:
        path = g['evidence']['path']
        if path not in files:
            files[path] = (SOURCE / path.removeprefix('grh/')).read_bytes()
    files['grh/CONTENTS.md'] = (SOURCE / 'CONTENTS.md').read_bytes()
    modules, edges = sd.build_modules(edition, files, rows, groups)
    sd.build_groups(edition, files, groups, modules, edges)
    directory = INPUT / 'readings'
    directory.mkdir(exist_ok=True)
    pilot_path = INPUT / 'readings.yaml'
    pilot = yaml.safe_load(pilot_path.read_text()) if pilot_path.exists() else {'groups': {}, 'files': {}}
    by_group = {}
    for g in groups_list:
        path = directory / (g['slug'] + '.yaml')
        data = yaml.safe_load(path.read_text()) if path.exists() else {'group': g['id'], 'overview': pilot['groups'].get(g['id']), 'files': {}}
        if not data.get('overview'):
            data['needs_draft'] = True
        by_group[g['id']] = data
    for row in rows:
        name = row['module']
        records = by_group[row['group']]['files']
        old = records.get(name) or pilot['files'].get(name)
        if old and (old.get('origin') == 'explorer-draft' or not old.get('mechanical') or not old.get('needs_draft') or old.get('standaloneReview')):
            records[name] = old
        else:
            records[name] = extract(row, modules[name], modules, files[row['path']].decode(), edition['revision'])
    for g in groups_list:
        (directory / (g['slug'] + '.yaml')).write_text(yaml.safe_dump(by_group[g['id']], allow_unicode=True, sort_keys=False, width=110))
    if pilot_path.exists():
        pilot_path.unlink()
    reasons = Counter(r.get('reason') for g in by_group.values() for r in g['files'].values() if r.get('needs_draft'))
    print('Files:', len(rows), 'Reasons:', dict(reasons))

if __name__ == '__main__':
    main()
