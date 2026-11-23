"""Shares for the report from occurrences.tsv.gz and summary.json (output of resolve.py).

usage: uv run --no-project python -I stats.py <xref data dir>   -> prints and writes stats.json
"""
import os, sys, gzip, json, collections

d = sys.argv[1]
summ = json.load(open(os.path.join(d, 'summary.json')))
fields = set()
with gzip.open(os.path.join(d, 'decls.tsv.gz'), 'rt', encoding='utf-8') as fh:
    next(fh)
    for ln in fh:
        n, _, _, k, _ = ln.split('\t')
        if k == 'field':
            fields.add(n.rsplit('.', 1)[-1])
chain = set(open(os.path.join(d, 'sample.txt')).read().split('\n')[1:1 + summ['chain_files']])
cnt = {'all': collections.Counter(), 'chain': collections.Counter(), 'random': collections.Counter()}
dot_field = collections.Counter()
with gzip.open(os.path.join(d, 'occurrences.tsv.gz'), 'rt', encoding='utf-8') as fh:
    next(fh)
    for ln in fh:
        mod, _, tok, cat = ln.split('\t', 4)[:4]
        top = cat.split(':')[0] if not cat.startswith(('excl', 'blind')) else cat
        for g in ('all', 'chain' if mod in chain else 'random'):
            cnt[g][top] += 1
            cnt[g]['detail:' + cat] += 1
        if cat in ('excl:local_dot', 'blind:dot'):
            dot_field[(cat, tok.rsplit('.', 1)[-1] in fields)] += 1


def shares(c):
    tot = sum(v for k, v in c.items() if not k.startswith('detail:'))
    excl = c['excl:keyword'] + c['excl:local'] + c['excl:local_dot']
    kept = tot - excl
    r, a = c['resolved'], c['ambiguous']
    u = c['unresolved'] + c['blind:dot']
    out = {'occurrences': tot,
           'overall': {'resolved': r / tot, 'ambiguous': a / tot, 'unresolved': (tot - r - a) / tot},
           'excluded': {'keyword_or_tactic': c['excl:keyword'], 'local': c['excl:local'],
                        'dot_on_local': c['excl:local_dot']},
           'after_exclusion': {'n': kept, 'resolved': r / kept, 'ambiguous': a / kept, 'unresolved': u / kept,
                               'of_which_dot_notation': c['blind:dot'] / kept,
                               'of_which_outside_imports': c['detail:unresolved:outside_imports'] / kept},
           'project_refs_found_by_rules': {'n': r + a + c['detail:unresolved:outside_imports'],
                                           'resolved': r / max(1, r + a + c['detail:unresolved:outside_imports'])},
           'resolved_same_file': (c['detail:resolved:same_file'] + c['detail:resolved:same_file:proj']) / max(1, r)}
    return out


res = {g: shares(c) for g, c in cnt.items()}
res['dot_tokens_whose_last_part_is_a_project_field_name'] = {f'{k[0]}|{k[1]}': v for k, v in dot_field.items()}
res['runtime'] = {'files': summ['n_files'], 'seconds_resolve': summ['seconds_resolve'],
                  'seconds_index_load': summ['seconds_index_load'],
                  'ms_per_file': 1000 * summ['seconds_resolve'] / summ['n_files'],
                  'estimate_all_175187_files_minutes_one_core': summ['seconds_resolve'] / summ['n_files'] * 175187 / 60}
json.dump(res, open(os.path.join(d, 'stats.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
