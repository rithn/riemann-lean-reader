"""Stable page dates and content fingerprints used by the sitemap and IndexNow."""

import hashlib
import re


NOISE_RE = re.compile(r'\?v=[0-9a-f]+|\s?data-v="[^"]*"|(?<=/app)\.[0-9a-f]{10}(?=\.js)|(?<=/style)\.[0-9a-f]{10}(?=\.css)')


def chash(*parts):
    return hashlib.sha256('\x00'.join(NOISE_RE.sub('', part) for part in parts).encode()).hexdigest()[:12]


def content_revision(old, today, parts, *, mirror=None):
    """Keep legacy hashes when first recording the explicit Markdown fingerprint."""
    body_hash = chash(*parts)
    mirror_hash = chash(mirror) if mirror is not None else None
    parts_hash = [body_hash, mirror_hash]
    if old and len(old) > 2:
        unchanged = old[2:] == parts_hash
    else:
        unchanged = old is not None and old[0] == body_hash
    if unchanged:
        revision = old[:2]
    else:
        revision = [chash(body_hash, mirror_hash) if mirror_hash else body_hash, today]
    if mirror_hash:
        revision += parts_hash
    return revision
