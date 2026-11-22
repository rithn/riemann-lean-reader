"""Tell IndexNow (Bing, Yandex, Seznam, Naver…) which pages of riemannhypothesissolved.com changed.

usage: python3 scripts/site/indexnow.py <site dir> [--since YYYY-MM-DD | --all | URL ...] [--submit]
e.g.   python3 scripts/site/indexnow.py ../site --since 2026-11-22            # dry run: list what would be sent
       python3 scripts/site/indexnow.py ../site --since 2026-11-22 --submit   # send (only after the deploy is live)

Changed pages come from <site>/sitemap.xml: build_site.py gives each page a lastmod that moves only when the page's
content changes (state in scripts/site/lastmod.json), so --since <last submission date> picks the changed URLs.
Without --since, --all or URLs, the default is pages with lastmod = today.
The key is scripts/site/indexnow.key; build_site.py publishes it at <site>/<key>.txt, which must be live first.
Standard library only.
"""
import os, re, sys, json, datetime, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://riemannhypothesissolved.com'
ENDPOINT = 'https://api.indexnow.org/indexnow'
BATCH = 10000                      # IndexNow accepts up to 10,000 URLs per request

def main(argv):
    if not argv or argv[0].startswith('-'):
        sys.exit(__doc__)
    out, args = argv[0], argv[1:]
    submit = '--submit' in args
    args = [a for a in args if a != '--submit']
    key = open(os.path.join(HERE, 'indexnow.key')).read().strip()
    if not os.path.exists(os.path.join(out, key + '.txt')):
        sys.exit(f'key file {key}.txt missing in {out}: run build_site.py first')
    pages = re.findall(r'<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>', open(os.path.join(out, 'sitemap.xml')).read())
    if '--all' in args:
        urls = [u for u, _ in pages]
    elif '--since' in args:
        since = args[args.index('--since') + 1]
        datetime.date.fromisoformat(since)
        urls = [u for u, d in pages if d >= since]
    elif args:
        urls = [a if a.startswith('http') else SITE + a for a in args]
    else:
        today = datetime.date.today().isoformat()
        urls = [u for u, d in pages if d == today]
    urls = [u for u in urls if u.startswith(SITE + '/')]
    print(f'{len(urls)} URLs' + ('' if submit else ' (dry run; add --submit to send)'))
    for u in urls[:20]:
        print('  ' + u)
    if len(urls) > 20:
        print(f'  … and {len(urls) - 20} more')
    if not submit or not urls:
        return
    for i in range(0, len(urls), BATCH):
        body = json.dumps({'host': SITE.split('//')[1], 'key': key, 'keyLocation': f'{SITE}/{key}.txt',
                           'urlList': urls[i:i + BATCH]}).encode()
        req = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                     headers={'Content-Type': 'application/json; charset=utf-8'})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                print(f'batch {i // BATCH + 1}: HTTP {r.status}')   # 200 or 202 = accepted
        except urllib.error.HTTPError as e:
            print(f'batch {i // BATCH + 1}: HTTP {e.code} {e.read()[:300]!r}')  # 403: key file not reachable yet

if __name__ == '__main__':
    main(sys.argv[1:])
