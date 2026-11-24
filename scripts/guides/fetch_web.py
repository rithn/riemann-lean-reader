"""Pin web guides as saved HTML, one file per page (guides-design.md section 5 step 1).

usage: uv run --no-project --with requests python -I fetch_web.py <out dir> <start url> [<start url> ...]
         [--prefix URL] [--max N] [--crawl] [--delay S]

Without --crawl only the start URLs are saved. With --crawl, links on saved pages are followed if they
start with --prefix (default: the first start URL up to its last '/'), are HTML pages (no file extension
other than .html/.htm), and fit under --max pages. One request per --delay seconds; robots.txt is read.
Writes <out dir>/pages/NNNN.html and <out dir>/pages.tsv (n, file, url, final_url, status, sha256, fetched_at).
Nothing fetched is executed; pages are treated as data.
"""
import sys, os, re, time, hashlib, datetime, urllib.parse, urllib.robotparser, argparse
import requests

ap = argparse.ArgumentParser()
ap.add_argument('out')
ap.add_argument('urls', nargs='+')
ap.add_argument('--prefix')
ap.add_argument('--max', type=int, default=300)
ap.add_argument('--crawl', action='store_true')
ap.add_argument('--delay', type=float, default=1.0)
ap.add_argument('--defer', help='regex: matching URLs are fetched after all others')
a = ap.parse_args()

UA = 'Mozilla/5.0 (compatible; guide-page-mapper/1.0)'
prefix = a.prefix or a.urls[0].rsplit('/', 1)[0] + '/'
os.makedirs(os.path.join(a.out, 'pages'), exist_ok=True)
sess = requests.Session()
sess.headers['User-Agent'] = UA

rp = urllib.robotparser.RobotFileParser()
pu = urllib.parse.urlparse(a.urls[0])
try:
    r = sess.get(f'{pu.scheme}://{pu.netloc}/robots.txt', timeout=20)
    rp.parse(r.text.splitlines() if r.status_code == 200 else [])
except Exception:
    rp.parse([])


def norm(u):
    u = urllib.parse.urldefrag(u)[0]
    p = urllib.parse.urlparse(u)
    path = p.path or '/'
    if path.endswith('/index.html'):
        path = path[:-len('index.html')]
    return urllib.parse.urlunparse((p.scheme, p.netloc, path, '', p.query, ''))


def is_page(u):
    if not u.startswith(prefix):
        return False
    last = urllib.parse.urlparse(u).path.rsplit('/', 1)[-1]
    if '.' in last and not re.search(r'\.html?$', last):
        return False
    return True


queue = [norm(u) for u in a.urls]
seen = set(queue)
deferred = []
rows = []
while queue and len(rows) < a.max:
    u = queue.pop(0)
    if not rp.can_fetch(UA, u):
        print('robots: skip', u, file=sys.stderr)
        continue
    try:
        r = sess.get(u, timeout=30)
    except Exception as e:
        print('error', u, e, file=sys.stderr)
        continue
    time.sleep(a.delay)
    ctype = r.headers.get('content-type', '')
    if r.status_code != 200 or 'html' not in ctype:
        print('skip', r.status_code, ctype, u, file=sys.stderr)
        continue
    n = len(rows) + 1
    fn = f'pages/{n:04d}.html'
    open(os.path.join(a.out, fn), 'wb').write(r.content)
    rows.append((n, fn, u, r.url, r.status_code, hashlib.sha256(r.content).hexdigest(),
                 datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')))
    if a.crawl:
        links = re.findall(r'''href\s*=\s*["']([^"'#][^"']*)["']''', r.text)
        links += re.findall(r'''http-equiv=["']Refresh["']\s+content=["'][^"']*url=([^"']+)["']''', r.text, re.I)
        for h in links:
            v = norm(urllib.parse.urljoin(r.url, h.strip()))
            if v not in seen and is_page(v):
                seen.add(v)
                if a.defer and re.search(a.defer, v):
                    deferred.append(v)
                else:
                    queue.append(v)
    if not queue and deferred:
        queue, deferred = deferred, []

with open(os.path.join(a.out, 'pages.tsv'), 'w') as fh:
    fh.write('n\tfile\turl\tfinal_url\tstatus\tsha256\tfetched_at\n')
    for row in rows:
        fh.write('\t'.join(map(str, row)) + '\n')
print(f'{len(rows)} pages saved, {len(queue) + len(deferred)} left in queue', file=sys.stderr)
open(os.path.join(a.out, 'not_fetched.txt'), 'w').write(''.join(u + '\n' for u in queue + deferred))
