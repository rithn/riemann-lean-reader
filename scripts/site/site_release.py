"""Build and validate a site snapshot before replacing its generated files."""

import fcntl
from contextlib import ExitStack
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit
from xml.etree import ElementTree


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
STATE_FILES = (
    'lastmod.json', 'theme_slugs_history.json', 'cluster_slugs_history.json',
    'indexnow.key', 'guide-cited-refs.tsv', 'references-n3.yaml',
)
HASHED_ASSET = re.compile(r'.+\.[a-f0-9]{10}\.(?:js|css)$')


def state_path(name):
    return (REPO / 'data' if name in STATE_FILES[-2:] else HERE) / name


def inventory(folder, *, site=False):
    files = {}
    if folder.is_dir():
        for path in folder.rglob('*'):
            relative = path.relative_to(folder)
            if '.git' in relative.parts or (site and relative.parts[0] == '.wrangler'):
                continue
            if path.is_symlink():
                files[relative] = ('link', os.readlink(path))
            elif path.is_file():
                with path.open('rb') as stream:
                    files[relative] = ('file', hashlib.file_digest(stream, 'sha256').hexdigest())
    return files


def retained(path):
    name = path.as_posix()
    return (len(path.parts) == 1 and HASHED_ASSET.fullmatch(name)
            or name.startswith(('data/alpoge/files/', 'src/sernau/', 'fonts/'))
            or (name.startswith('data/sernau/') and name != 'data/sernau/manifest.json'))


def validate_release(stage, previous, current, state):
    lost = sorted(str(path) for path in previous if retained(path) and previous[path] != current.get(path))
    if lost:
        raise ValueError(f'Build changed retained release files: {", ".join(lost[:5])}')
    dates = json.loads((state / 'lastmod.json').read_text(encoding='utf-8'))
    sitemap = ElementTree.parse(stage / 'sitemap.xml')
    seen = set()
    for entry in sitemap.findall('{*}url'):
        path = urlsplit(entry.findtext('{*}loc')).path
        if (path in seen or dates[path][1] != entry.findtext('{*}lastmod')
                or not (stage / path.strip('/') / 'index.html').is_file()):
            raise ValueError(f'Invalid generated sitemap entry: {path}')
        seen.add(path)
    if '/' not in seen:
        raise ValueError('The staged sitemap is missing Home')
    old_reader = {path for path in previous if path.parts[:2] == ('data', 'lean') and path.suffix == '.gz'}
    if old_reader and not any(path.parts[:2] == ('data', 'lean') and path.suffix == '.gz' for path in current):
        raise ValueError('Original reader bundles disappeared from the staged site')


def replace_file(source, target):
    """Replace one file atomically even when output is on another filesystem."""
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.explorer-write-', dir=target.parent) as td:
        copy = Path(td) / 'file'
        shutil.copy2(source, copy, follow_symlinks=False)
        os.replace(copy, target)


def recover(transaction):
    journal = transaction / 'journal.json'
    if journal.is_file():
        entries = json.loads(journal.read_text(encoding='utf-8'))
        for target, backup in reversed(entries):
            target = Path(target)
            if backup is None:
                target.unlink(missing_ok=True)
            else:
                replace_file(transaction / 'backups' / backup, target)
        journal.unlink()


def promote(transaction, changes):
    """Keep rollback copies until a complete output and its date state are installed."""
    backups = transaction / 'backups'
    backups.mkdir()
    entries = []
    for i, (target, source) in enumerate(changes):
        backup = str(i) if target.exists() or target.is_symlink() else None
        if backup is not None:
            shutil.copy2(target, backups / backup, follow_symlinks=False)
        entries.append((str(target), backup))
    draft = transaction / 'prepared.json'
    draft.write_text(json.dumps(entries), encoding='utf-8')
    journal = transaction / 'journal.json'
    draft.rename(journal)
    try:
        for target, source in changes:
            if source is None:
                target.unlink()
            else:
                replace_file(source, target)
    except BaseException:
        recover(transaction)
        raise
    journal.unlink()


def file_changes(target, old, stage, new):
    return [(target / path, stage / path if path in new else None)
            for path in sorted(old.keys() | new.keys()) if old.get(path) != new.get(path)]


def run(argv):
    if len(argv) < 2:
        sys.exit('Usage: build_site.py <cluster dir> <site dir> [--src-bundles[=DIR]]')
    cluster, output = (Path(value).resolve() for value in argv[:2])
    if not output.is_dir():
        sys.exit(f'Seed the site directory with its authored assets first: {output}')
    release_id = hashlib.sha256(os.fsencode(REPO) + b'\0' + os.fsencode(output)).hexdigest()[:16]
    transaction = output.parent / f'.explorer-build-{release_id}'
    with ExitStack() as locks:
        for path in sorted({REPO, output}):
            lock_id = hashlib.sha256(os.fsencode(path)).hexdigest()[:24]
            lock = locks.enter_context(open(Path(tempfile.gettempdir()) / f'explorer-build-{lock_id}.lock', 'a'))
            fcntl.flock(lock, fcntl.LOCK_EX)
        if transaction.exists():
            recover(transaction)
            shutil.rmtree(transaction)
        transaction.mkdir()
        try:
            build_in_stage(cluster, output, transaction, argv[2:])
        finally:
            # Keep the journal for the next invocation if rollback was itself interrupted.
            if not (transaction / 'journal.json').exists():
                shutil.rmtree(transaction)


def build_in_stage(cluster, output, transaction, options):
    stage, state = transaction / 'site', transaction / 'state'
    old_site = inventory(output, site=True)
    xref = Path(os.environ.get('RH_XREF') or REPO.parent / 'research/lean-reader/xref')
    if any(path.parts[:2] == ('data', 'lean') and path.suffix == '.gz' for path in old_site):
        if not (xref / 'full/decl_stats.tsv.gz').is_file():
            raise ValueError(f'Original reader data exists, but the XREF input is missing: {xref}')
    shutil.copytree(output, stage, symlinks=True, ignore=shutil.ignore_patterns('.git', '.wrangler'))
    state.mkdir()
    old_state = {}
    for name in STATE_FILES:
        path = state_path(name)
        old_state[name] = path.read_bytes() if path.exists() else None
        if old_state[name] is not None:
            shutil.copy2(path, state / name)

    bundle = next((option for option in options if option.startswith('--src-bundles')), None)
    external = None
    if bundle and '=' in bundle:
        target = Path(bundle.split('=', 1)[1]).resolve()
        if target.is_relative_to(output):
            bundle_stage = stage / target.relative_to(output)
        else:
            bundle_stage = transaction / 'bundles'
            external = (target, inventory(target), bundle_stage)
            if target.is_dir():
                shutil.copytree(target, bundle_stage, symlinks=True)
        options = [f'--src-bundles={bundle_stage}' if option == bundle else option for option in options]

    subprocess.run([sys.executable, '-B', '-I', str(HERE / 'build_site.py'), str(cluster), str(stage), *options],
                   env={**os.environ, '_RH_SITE_STAGE_STATE': str(state)}, check=True)
    new_site = inventory(stage, site=True)
    validate_release(stage, old_site, new_site, state)
    if inventory(output, site=True) != old_site:
        raise ValueError('The original site changed during the build. Retry with the current assets.')
    changes = file_changes(output, old_site, stage, new_site)
    if external:
        target, old_bundles, bundle_stage = external
        if inventory(target) != old_bundles:
            raise ValueError(f'Source bundles changed during the build: {target}')
        changes += file_changes(target, old_bundles, bundle_stage, inventory(bundle_stage))
    for name in STATE_FILES:
        path, built = state_path(name), state / name
        if (path.read_bytes() if path.exists() else None) != old_state[name]:
            raise ValueError(f'Build state changed during generation: {path}')
        if built.exists() and built.read_bytes() != old_state[name]:
            changes.append((path, built))
    promote(transaction, changes)
    print(f'Validated staged build and updated {len(changes):,} site or state files.')
