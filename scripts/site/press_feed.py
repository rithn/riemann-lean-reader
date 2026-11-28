"""Render and validate the data behind the Press page and its Markdown mirror."""
import datetime
import re
import unicodedata
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

import yaml


KINDS = {'article', 'editorial', 'blog', 'interview', 'post', 'video', 'statement', 'podcast'}
SEARCH_FIELDS = ('headline', 'original_headline', 'name', 'role', 'source', 'description',
                 'quote', 'tag', 'stance', 'language')


def press_error(label, message):
    raise ValueError(f'data/press.yaml: {label}: {message}')


def press_date(entry):
    return entry.get('date_label') or datetime.date.fromisoformat(entry['date']).strftime('%-d %b')


def iso_date(value, field, label):
    value = str(value)
    try:
        if datetime.date.fromisoformat(value).isoformat() == value:
            return value
    except ValueError:
        pass
    press_error(label, f'{field} must be an ISO date (YYYY-MM-DD)')


def valid_url(value):
    parts = urlsplit(value)
    return parts.scheme in {'https', 'http'} and bool(parts.hostname)


def load_press(path, reserved_ids):
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('entries'), list):
        press_error('entries', 'expected a list')
    seen = set()
    for position, entry in enumerate(data['entries'], start=1):
        if not isinstance(entry, dict):
            press_error(f'entry {position}', 'expected a mapping')
        label = entry.get('id') or f'entry {position}'
        fields = ('id', 'tag', 'kind', 'headline', 'name', 'source', 'date_precision',
                  'description', 'description_status', 'url')
        for field in fields:
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                press_error(label, f'missing {field}' + (' (title)' if field == 'headline' else ''))
        for field in ('date', 'added'):
            if not entry.get(field):
                press_error(label, f'missing {field}')
            entry[field] = iso_date(entry[field], field, label)
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', label):
            press_error(label, 'id must be a lowercase slug')
        if label in seen:
            press_error(label, 'duplicate id')
        if label in reserved_ids:
            press_error(label, 'id conflicts with a page anchor')
        seen.add(label)
        if entry['tag'] not in {'reaction', 'media'} or entry['kind'] not in KINDS:
            press_error(label, 'unknown tag or kind')
        if entry.get('date_verified') is not True:
            press_error(label, 'date_verified must be true')
        if entry['description_status'] not in {'reused', 'final'} or len(entry['description']) > 160:
            press_error(label, 'description must be reused or final and at most 160 characters')
        if not valid_url(entry['url']):
            press_error(label, 'url must be an absolute HTTP(S) link')
        if entry.get('language', 'en') != 'en' and not entry.get('original_headline'):
            press_error(label, 'a translated title needs original_headline')
        archive = entry.get('archive_url')
        if entry['source'] == 'X' and not archive:
            press_error(label, 'X posts require archive_url')
        if archive and not valid_url(archive):
            press_error(label, 'archive_url must be an absolute HTTP(S) link')
        image = entry.get('image') or {}
        if not isinstance(image, dict):
            press_error(label, 'image must be a mapping')
        if image.get('file'):
            source = Path(image['file'])
            if source.name != str(source) or not (path.parent / 'press-images' / source).is_file():
                press_error(label, 'image.file must name a file under data/press-images/')
            if (image.get('kind') not in {'photo', 'logo'} or not image.get('licence')
                    or not image.get('credit') or not valid_url(image.get('source_url', ''))):
                press_error(label, 'image needs kind, licence, credit and source_url')
    return sorted(data['entries'], key=lambda entry: (entry['date'], entry['added']), reverse=True)


def fold(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text.lower()) if not unicodedata.category(c).startswith('M')).replace('ł', 'l')


def is_outlet(entry):
    return entry['name'] in ('Editorial', entry['source'], f'{entry["source"]} Team')


def press_feed_html(entries, initials, pictures):
    tiles = []
    for entry in entries:
        id_, source = entry['id'], entry['source']
        image = entry.get('image') or {}
        outlet = image['kind'] == 'logo' if id_ in pictures else is_outlet(entry)
        shape = 'outlet' if outlet else 'person'
        if id_ in pictures:
            lazy = ' loading="lazy"' if len(tiles) >= 4 else ''
            avatar = f'<img class="press-avatar {shape}" src="{escape(pictures[id_])}" width="56" height="56" alt=""{lazy}>'
        else:
            # A long outlet name fits as a short wordmark. The full source is shown below the tile.
            wordmark = source if len(source) <= 16 else initials(source)
            avatar = f'<div class="press-avatar {shape}" aria-hidden="true">{escape(wordmark if outlet else initials(entry["name"]))}</div>'
        query = fold(' '.join(entry.get(key) or '' for key in SEARCH_FIELDS))
        verb = 'Watch' if entry['kind'] == 'video' else 'Listen' if entry['kind'] == 'podcast' else 'Read'
        tiles.append(
            f'<li><article class="press-tile" id="{id_}" data-q="{escape(query)}">'
            f'<div class="press-who">{avatar}<div><div class="press-name">{escape(entry["name"])}</div>'
            f'<div class="press-source">{escape(source)} · <time datetime="{entry["date"]}">{escape(press_date(entry))}</time></div>'
            f'</div></div><div class="press-story"><h2>{escape(entry["headline"])}</h2>'
            f'<p>{escape(entry["description"])}</p><a class="btn" href="{escape(entry["url"])}">'
            f'{verb} on {escape(source)}</a></div></article></li>')
    return (
        '<label class="press-search" hidden><span class="sr">Search press and reactions</span>'
        '<input id="press-q" type="search" placeholder="Search people, outlets, headlines…" '
        'aria-controls="press-list" autocomplete="off"></label>\n'
        '<p class="sr" id="press-live" aria-live="polite"></p>\n'
        '<ul id="press-list" role="list">\n' + '\n'.join(tiles) + '\n</ul>\n'
        '<p id="press-empty" hidden>Nothing matches. <button type="button">Clear search</button>.</p>')


def press_feed_md(entries):
    blocks = []
    for entry in entries:
        heading = f'## [{entry["headline"]}]({entry["url"]})'
        meta = f'{entry["name"]} · {entry["source"]} · {press_date(entry)} · {entry["tag"]}'
        lines = [heading, meta, entry['description']]
        if entry.get('original_headline'):
            lines.append(entry['original_headline'])
        if entry.get('archive_url'):
            lines.append(f'[Archived copy]({entry["archive_url"]})')
        links = entry.get('related_links', [])
        if links:
            lines.append(' · '.join(f'[{link["title"]}]({link["url"]})' for link in links))
        blocks.append('\n\n'.join(lines))
    return '\n\n'.join(blocks)


def press_feed_ld(entries):
    items = []
    for position, entry in enumerate(entries, start=1):
        organisation = is_outlet(entry)
        item = {
            '@type': 'NewsArticle' if entry['tag'] == 'media' and entry['kind'] in {'article', 'editorial'} else 'CreativeWork',
            'url': entry['url'],
            'headline': entry.get('original_headline') or entry['headline'],
            'datePublished': entry['date'],
            'publisher': {'@type': 'Organization', 'name': entry['source']},
            'author': {'@type': 'Organization' if organisation else 'Person',
                       'name': entry['source'] if organisation else entry['name']},
            'inLanguage': entry.get('language', 'en'),
            'keywords': entry['tag'],
        }
        items.append({'@type': 'ListItem', 'position': position, 'item': item})
    return {'@type': 'ItemList', 'itemListElement': items}


def press_images(entries, data_dir, out):
    """Generate 2x fallback-ready WebP copies and the shared credit list."""
    from PIL import Image, ImageOps

    folder = out / 'press' / 'img'
    pictures, credits = {}, []
    for entry in entries:
        image = entry.get('image') or {}
        if not image.get('file'):
            continue
        id_ = entry['id']
        filename = f'{id_}-112.webp'
        folder.mkdir(parents=True, exist_ok=True)
        with Image.open(data_dir / 'press-images' / image['file']) as original:
            pixels = ImageOps.exif_transpose(original).convert('RGBA')
            square = ImageOps.fit(pixels, (112, 112), Image.Resampling.LANCZOS)
            # Recreate the image from pixel data to strip source metadata.
            Image.frombytes(square.mode, square.size, square.tobytes()).save(folder / filename, quality=78, method=6)
        if (folder / filename).stat().st_size > 8192:
            press_error(id_, '112 px WebP exceeds 8 KB')
        pictures[id_] = f'/press/img/{filename}'
        credits.append(f'- [{entry["name"]}]({image["source_url"]}) · {image["credit"]} · {image["licence"]}')
    keep = {Path(url).name for url in pictures.values()}
    for existing in folder.glob('*-112.webp'):
        if existing.name not in keep:
            existing.unlink()
    return pictures, '## Image credits\n\n' + '\n'.join(credits) + '\n' if credits else ''
