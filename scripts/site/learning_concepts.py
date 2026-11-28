"""Build the compact proof's learning guide from the reviewed concept map."""

from html import escape
from pathlib import PurePosixPath
import re

import yaml

from explorer_views import breadcrumbs


LEVELS = {'curious': 'Curious', 'undergrad': 'Undergraduate', 'grad': 'Graduate', 'Lean': 'Lean'}

# A keyed lookup keeps internal review wording out of the published labels and rejects new statuses.
SOURCE_LABELS = {
    True: 'Checked',
    False: None,
    'checked local source': 'Lean source',
    'checked pinned Mathlib online': 'Lean source',
    'checked; proof source; outside lesson on exact jets UNVERIFIED': 'Lean source',
    'checked; proof-specific source': 'Checked',
    'checked; background': 'Background',
    'checked; general background': 'Background',
    'checked; Selmer/cohomology background': 'Background',
    'checked; classical setting': 'Background · Classical setting',
    'checked; classical background; compact determinant definition in Lean file': 'Background · Classical setting',
    'checked; classical example; compact local transfer is in Lean file': 'Background · Classical example',
    'checked classical background; exact compact jet construction UNVERIFIED': 'Background · Classical setting',
    'checked classical background; exact CM period construction UNVERIFIED': 'Background · Classical setting',
    'checked; general background; exact lesson or proof-specific correspondence UNVERIFIED': 'Background',
    'checked background; exact twist argument UNVERIFIED in notes': 'Background',
    'checked site guide; original PDF UNVERIFIED (fetch failed)': None,
}


def concept_path(slug):
    return f'/learn/{slug}/'


def html_list(items, tag='ul'):
    return f'<{tag}>' + ''.join(f'<li>{item}</li>' for item in items) + f'</{tag}>'


class ConceptMap:
    def __init__(self, data_dir, edition):
        concepts = yaml.safe_load((data_dir / 'concepts.yaml').read_text(encoding='utf-8'))['concepts']
        parts = yaml.safe_load((data_dir / 'parts.yaml').read_text(encoding='utf-8'))
        self.concepts = {c['id']: c for c in concepts}
        self.parts = {part['id']: part for part in parts}
        self.references = yaml.safe_load((data_dir / 'references.yaml').read_text(encoding='utf-8'))
        assert len(self.concepts) == len(concepts), 'Duplicate learning concept ID'
        assert len(self.parts) == len(parts), 'Duplicate proof part ID'
        assert self.references.keys() <= self.concepts.keys(), 'References name an unknown learning concept'
        if any(not isinstance(ref['checked'], bool) for refs in self.references.values() for ref in refs):
            raise ValueError('Reference inventory checked status must be true or false')
        assert all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug)
                   for slug in self.concepts.keys() | self.parts.keys()), 'Invalid learning concept or proof part ID'

        compact = PurePosixPath(edition['compact']['sourceRoot']).parent
        self.source = f'{edition["repository"]}/blob/{edition["revision"]}/{compact}/'
        compact_lean = self.source + 'src/'
        mathlib = f'https://github.com/leanprover-community/mathlib4/blob/{edition["mathlibRevision"]}/'
        for slug, concept in self.concepts.items():
            assert concept['level'] in LEVELS, f'Unknown learning level for {slug}'
            assert concept['used_by'] and set(concept['used_by']) <= self.parts.keys(), f'Unknown or missing proof parts for {slug}'
            assert concept['lean_location'] and all(
                location['url'].startswith((compact_lean, mathlib)) for location in concept['lean_location']
            ), f'Lean locations for {slug} must use the compact or Mathlib source pin'
        for key, part in self.parts.items():
            seen = set()
            for slug in part['path']:
                assert slug in self.concepts and slug not in seen, f'Missing or repeated concept {slug} in {key}'
                assert set(self.concepts[slug]['prerequisites']) <= seen, f'Prerequisites for {slug} must precede it in {key}'
                seen.add(slug)
            assert all(c['id'] in seen for c in concepts if key in c['used_by']), f'Incomplete learning path for {key}'

    def concept_link(self, slug):
        return f'<a href="{concept_path(slug)}">{escape(self.concepts[slug]["name"])}</a>'

    def overview(self):
        guide = self.source + 'GUIDE.md'
        parts = []
        for key, part in self.parts.items():
            path = html_list((self.concept_link(slug) for slug in part['path']), 'ol')
            source = self.source + part['lean']
            parts.append(
                f'<h3 id="compact-{key}">{escape(part["title"])}</h3>'
                f'<p>{escape(part["summary"])} <a href="{escape(source)}">Lean source</a></p>'
                '<details class="article-detail"><summary>Learn this first</summary>'
                f'<div>{path}</div></details>'
            )
        return (
            '<div class="evidence-article"><h2 id="compact-proof">Sernau’s compact proof</h2>'
            f'<p>Six parts from the <a href="{escape(guide)}">compact edition guide</a>. '
            'Each path puts prerequisites before the concepts that use them.</p>'
            + ''.join(parts) + '</div>'
        )

    def reading_list(self, concept):
        # Use the more specific review for URLs that also appear in the reference inventory.
        readings = {ref['url']: (ref['title'], SOURCE_LABELS[ref['checked']])
                    for ref in self.references.get(concept['id'], [])}
        readings.update({ref['url']: (ref['title'], SOURCE_LABELS[ref['status']])
                         for ref in concept['sources']})
        lean_urls = {loc['url'] for loc in concept['lean_location']}
        items = [f'<a href="{escape(url)}">{escape(title)}</a> <span class="meta">· {escape(label)}</span>'
                 for url, (title, label) in readings.items() if label and url not in lean_urls]
        if not items:
            return ''
        return (
            '<h2>Sources and further reading</h2>'
            '<p class="meta">Checked sources were opened and cover this concept, Background sources cover the general topic, '
            'and Lean source links point to pinned Lean or Mathlib files.</p>'
            + html_list(items)
        )

    def pages(self):
        for slug, concept in self.concepts.items():
            name, definition = concept['name'], concept['definition']
            path = concept_path(slug)
            trail = [('Home', '/'), ('Learning path', '/learn/'), (name, path)]
            prerequisites = (html_list(self.concept_link(key) for key in concept['prerequisites'])
                             if concept['prerequisites'] else '<p>No prerequisites in this guide.</p>')
            parts = html_list(f'<a href="/learn/#compact-{key}">{escape(self.parts[key]["title"])}</a>'
                              for key in concept['used_by'])
            locations = html_list(f'<a href="{escape(loc["url"])}"><code>{escape(loc["path"])}</code></a> '
                                  f'<span class="meta">· {escape(SOURCE_LABELS[loc["status"]])}</span>'
                                  for loc in concept['lean_location'])
            body = (
                breadcrumbs([*trail[:-1], (name, '')])
                + '<article class="evidence-article">'
                f'<h1>{escape(name)}</h1><p class="provenance">◇ AI-drafted reading guide</p><p class="meta">{LEVELS[concept["level"]]}</p>'
                f'<p class="article-lead">{escape(definition)}</p>'
                f'<h2>Prerequisites</h2>{prerequisites}'
                f'<h2>Where it’s used in the compact proof</h2>{parts}'
                f'<h2>Lean locations</h2>{locations}'
                + self.reading_list(concept) + '</article>'
            )
            yield path, name, definition, body, trail
