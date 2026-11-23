"""Tell IndexNow (Bing, Yandex, Seznam, Naver…) which pages of riemannhypothesissolved.com changed.

usage: python3 scripts/site/indexnow.py <site dir> [--all | --since YYYY-MM-DD | URL ...] [--baseline] [--submit] [--state FILE]
e.g.   python3 scripts/site/indexnow.py ../site                 # dry run: list the pages changed since the last submission
       python3 scripts/site/indexnow.py ../site --submit        # send them (only after the deploy is live)
       python3 scripts/site/indexnow.py ../site --all --submit  # force: send every page in the sitemap

Default: the pages whose content changed since the last successful submission. build_site.py keeps a content hash per
page in scripts/site/lastmod.json (path -> [hash, lastmod]); this script keeps the hash each page had when it was last
sent, in scripts/site/indexnow_state.json. A page is sent when its hash differs, when it is new, or when it left the
sitemap since (removed or renamed: IndexNow then sees its 404 or 301). After a send, the pages of every accepted batch
(HTTP 200 or 202) are recorded as sent; a failed batch stays pending for the next run.
  --all             every page in the sitemap (force a full submit)
  --since DATE      pages with sitemap lastmod >= DATE;  URL ...  just these (paths or full URLs)
  --baseline        record every page's current hash as sent, send nothing
  --submit          send; without it this is a dry run that prints what would be sent and writes nothing
  --state FILE      another state file (for tests)
With no state file yet, the first --submit run records the baseline and sends nothing (use --all to also send).
lastmod.json must come from the build in <site dir>: the script stops if the sitemap's dates disagree with it.
The key is scripts/site/indexnow.key; build_site.py publishes it at <site>/<key>.txt, which must be live first.
Standard library only.
"""
import os, re, sys, json, datetime, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://riemannhypothesissolved.com'
ENDPOINT = 'https://api.indexnow.org/indexnow'
BATCH = 10000                      # IndexNow accepts up to 10,000 URLs per request
SHOW = 40                          # URLs listed in the output per group

def opt(args, name):
    if name not in args:
        return None
    i = args.index(name)
    if i + 1 >= len(args):
        sys.exit(f'{name} needs a value')
    v = args[i + 1]
    del args[i:i + 2]
    return v

def show(label, paths):
    print(f'{label}: {len(paths)}')
    for p in paths[:SHOW]:
        print('  ' + SITE + p)
    if len(paths) > SHOW:
        print(f'  … and {len(paths) - SHOW} more')

def main(argv):
    if not argv or argv[0].startswith('-'):
        sys.exit(__doc__)
    out, args = argv[0], list(argv[1:])
    flags = {a for a in args if a in ('--submit', '--all', '--baseline')}
    args = [a for a in args if a not in flags]
    submit, since = '--submit' in flags, opt(args, '--since')
    state_f = opt(args, '--state') or os.path.join(HERE, 'indexnow_state.json')
    key = open(os.path.join(HERE, 'indexnow.key')).read().strip()
    if not os.path.exists(os.path.join(out, key + '.txt')):
        sys.exit(f'key file {key}.txt missing in {out}: run build_site.py first')
    pages = re.findall(r'<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>', open(os.path.join(out, 'sitemap.xml')).read())
    pages = [(u[len(SITE):], d) for u, d in pages if u.startswith(SITE + '/')]
    lm = json.load(open(os.path.join(HERE, 'lastmod.json')))
    bad = [p for p, d in pages if p not in lm or lm[p][1] != d]
    if bad:
        sys.exit(f'{len(bad)} sitemap pages disagree with scripts/site/lastmod.json (e.g. {bad[0]}): '
                 f'{out} was not built with this lastmod.json; rebuild it first')
    cur = {p: lm[p][0] for p, _ in pages}          # path -> content hash now
    state = json.load(open(state_f)) if os.path.exists(state_f) else None
    sent = dict(state['urls']) if state else {}

    if '--baseline' in flags or (state is None and not ('--all' in flags or since or args)):
        why = 'asked for (--baseline)' if '--baseline' in flags else f'no state file yet ({state_f})'
        print(f'baseline {why}: {len(cur)} pages recorded as sent with their current hashes; nothing sent')
        if submit or '--baseline' in flags:
            save(state_f, cur, 'baseline')
        else:
            print('(dry run: state not written; the first --submit run records it)')
        return

    removed = []
    if '--all' in flags:
        paths = sorted(cur)
        show('all pages in the sitemap (--all)', paths)
    elif since:
        datetime.date.fromisoformat(since)
        paths = sorted(p for p, d in pages if d >= since)
        show(f'pages with lastmod >= {since}', paths)
    elif args:
        paths = [a[len(SITE):] if a.startswith(SITE) else a for a in args]
        bad = [p for p in paths if not p.startswith('/')]
        if bad:
            sys.exit(f'not a path or {SITE} URL: {bad}')
        show('URLs given', paths)
    else:
        new = sorted(p for p in cur if p not in sent)
        changed = sorted(p for p in cur if p in sent and sent[p] != cur[p])
        removed = sorted(p for p in sent if p not in cur)
        print(f'last successful submission: {state.get("submitted", "?")}; {len(cur)} pages in the sitemap, '
              f'{len(cur) - len(new) - len(changed)} unchanged since')
        show('changed', changed)
        show('new', new)
        show('removed from the sitemap (404 or 301 now)', removed)
        paths = changed + new + removed
    print(f'{len(paths)} URLs to send' + ('' if submit else ' (dry run; add --submit to send)'))
    if not submit or not paths:
        return
    ok = []
    for i in range(0, len(paths), BATCH):
        part = paths[i:i + BATCH]
        body = json.dumps({'host': SITE.split('//')[1], 'key': key, 'keyLocation': f'{SITE}/{key}.txt',
                           'urlList': [SITE + p for p in part]}).encode()
        req = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                     headers={'Content-Type': 'application/json; charset=utf-8'})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                print(f'batch {i // BATCH + 1}: HTTP {r.status}')   # 200 or 202 = accepted
                if r.status in (200, 202):
                    ok += part
        except urllib.error.HTTPError as e:
            print(f'batch {i // BATCH + 1}: HTTP {e.code} {e.read()[:300]!r}')  # 403: key file not reachable yet
        except urllib.error.URLError as e:
            print(f'batch {i // BATCH + 1}: {e.reason}')
    for p in ok:                                   # record what was accepted; the rest stays pending
        if p in cur:
            sent[p] = cur[p]
        else:
            sent.pop(p, None)
    if ok:
        save(state_f, sent, f'{len(ok)} of {len(paths)} URLs accepted')
    print(f'state: {len(ok)} of {len(paths)} URLs recorded as sent in {state_f}')

def save(state_f, urls, note):
    json.dump({'submitted': datetime.date.today().isoformat(), 'note': note, 'urls': dict(sorted(urls.items()))},
              open(state_f, 'w'), indent=0, separators=(',', ':'))
    open(state_f, 'a').write('\n')

if __name__ == '__main__':
    main(sys.argv[1:])
