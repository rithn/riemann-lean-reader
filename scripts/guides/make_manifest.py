"""Write research/guides/sources/manifest.tsv: id, file, url, version, sha256, fetched_at.

usage: python3 -I make_manifest.py <sources dir>
Lists the pinned PDFs, every saved web page (from each pages.tsv) and the cloned repos (commit from .git/HEAD
read as a file; git is not run inside the clones). fetched_at for files is their modification time (UTC).
"""
import os, sys, csv, hashlib, datetime

S = sys.argv[1]


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def mtime(p):
    return datetime.datetime.fromtimestamp(os.path.getmtime(p), datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def head(repo):
    ref = open(os.path.join(repo, '.git', 'HEAD')).read().strip()
    if ref.startswith('ref: '):
        r = ref[5:]
        p = os.path.join(repo, '.git', r)
        if os.path.exists(p):
            return open(p).read().strip()
        for ln in open(os.path.join(repo, '.git', 'packed-refs')):
            if ln.strip().endswith(r):
                return ln.split()[0]
    return ref


REPOS = {'merten-riemann-blueprint': 'chrisflav/riemann-blueprint', 'naskrecki-riemann-rev': 'nasqret/riemann-rev',
         'adriazola-reconstruction': 'jimjamzola/RH-Alpoge-Reconstruction'}
FILES = [  # id, file, url, version
    ('rubinstein-zeta-guide', 'zeta-paper_v2.pdf',
     'https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf',
     'v2 (file rebuilt 23 Nov under the same name; server Last-Modified Mon, 23 Nov 2026 05:10:18 GMT)'),
    ('jaswal-zenodo-guide', 'v2.pdf',
     'https://zenodo.org/records/24432579/files/jaswal-rh-dirichlet-after-alpoge.pdf',
     'v2, Zenodo record 24432579 (md5 3024933685553636c1f9b8e93af708a5 per Zenodo API)'),
    ('merten-riemann-blueprint', 'site/index.html', 'https://riemann.fuxi.merten.dev/', 'site as fetched'),
    ('merten-riemann-blueprint', 'site/app.js.txt', 'https://riemann.fuxi.merten.dev/app.js', 'site as fetched (saved as .txt, not run)'),
    ('merten-riemann-blueprint', 'site/blueprint.json', 'https://riemann.fuxi.merten.dev/blueprint.json', 'site as fetched'),
]
for p in ('guide/proof-guide.pdf', 'blueprint/atlas-blueprint.pdf', 'digests/layer-descent.pdf',
          'digests/local-nilpotence.pdf', 'digests/tower-bound.pdf'):
    FILES.append(('naskrecki-riemann-rev', 'site/pdfs/' + p.replace('/', '_'), 'https://nasqret.github.io/riemann-rev/' + p,
                  'site as fetched'))

rows = []
for gid, f, url, ver in FILES:
    p = os.path.join(S, gid, f)
    rows.append((gid, f'{gid}/{f}', url, ver, sha(p), mtime(p)))
for gid, slug in REPOS.items():
    rp = os.path.join(S, gid, 'repo')
    c = head(rp)
    rows.append((gid, f'{gid}/repo', f'https://github.com/{slug}', c, '', mtime(os.path.join(rp, '.git'))))
    if gid == 'adriazola-reconstruction':
        for f, ver in (('manuscript/main.pdf', 'newest manuscript (23 Nov, 225 pages)'),
                       ('RH_Route_Notes.pdf', 'older manuscript (21 Nov, 67 pages)')):
            p = os.path.join(rp, f)
            rows.append((gid, f'{gid}/repo/{f}', f'https://github.com/{slug}/blob/{c}/{f}', f'{ver}, commit {c}',
                         sha(p), mtime(p)))
for root, dirs, fs in os.walk(S):
    dirs[:] = [d for d in dirs if d not in ('repo', '.git')]
    if 'pages.tsv' in fs:
        gid = os.path.relpath(root, S).split('/')[0]
        with open(os.path.join(root, 'pages.tsv')) as fh:
            for r in csv.DictReader(fh, delimiter='\t'):
                rows.append((gid, os.path.relpath(os.path.join(root, r['file']), S), r['final_url'],
                             'web page as fetched', r['sha256'], r['fetched_at']))
rows.sort(key=lambda r: (r[0], r[1]))
with open(os.path.join(S, 'manifest.tsv'), 'w') as fh:
    fh.write('id\tfile\turl\tversion\tsha256\tfetched_at\n')
    for r in rows:
        fh.write('\t'.join(r) + '\n')
print(len(rows), 'rows')
