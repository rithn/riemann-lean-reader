"""Small HTML views shared by both editions' content producers."""

from html import escape
import re


GUIDE_PRESENTATION = {
    'portrait': '<img class="gav" src="@SRC@" width="@SIZE@" height="@SIZE@" alt="@ALT@" loading="lazy" decoding="async">',
    'logo': '<img class="gav logo" src="@SRC@" width="@SIZE@" height="@SIZE@" alt="@ALT@ logo" loading="lazy" decoding="async">',
    'logos': '<span class="gav2" style="--lg:@SIZE@px">@CONTENT@</span>',
    'initials': '<span class="gav ini" style="--gh:@HUE@;--gs:@SIZE@px" role="img" aria-label="@ALT@">@INITIALS@</span>',
    'byline': '<a href="@HREF@">@AVATAR@<span class="t">@AUTHOR@<small>@TITLE@</small></span></a>',
    'citation': '<div class="ref gc">@CITATION@<small>cited on @PAGES@</small></div>',
}
RESULT_ROW = '<a href="@HREF@"@KEY@>@MARKER@<span class="t@MONO@">@LABEL@@DETAIL@</span>@END@</a>'


def guide_presentation(name, **slots):
    return fill_view(GUIDE_PRESENTATION[name], **slots)


def fill_view(template, **slots):
    return re.sub(r'@([A-Z]+)@', lambda match: str(slots[match[1].lower()]), template)


def result_link(href, label, detail, color, end):
    return fill_view(RESULT_ROW, href=escape(href), key='', mono='', label=escape(label),
                     marker=f'<span class="dot" style="color:{escape(color)}"></span>',
                     detail=f'<small>{escape(detail)}</small>', end=f'<span class="end">{escape(end)}</span>')


def breadcrumbs(items):
    """Use the same linked items for the visible trail and page metadata."""
    links = [f'<a href="{escape(path)}">{escape(label)}</a>' if path else escape(label)
             for label, path in items]
    return '<div class="crumbs" role="navigation" aria-label="Breadcrumb">' + '<span class="sep" aria-hidden="true">/</span>'.join(links) + '</div>'


def route_intro(edition, label, title, lede):
    map_url = '/sernau/' if edition == 'Sernau readable' else '/alpoge/'
    return (breadcrumbs([(edition, map_url), (label, '')]) +
            f'<div class="eyebrow">{escape(edition)} · {escape(label)}</div>'
            f'<h1>{escape(title)}</h1><p class="lede">{lede}</p>')


def stats_row(items):
    return ''.join(f'<div><dt>{escape(label)}</dt> <dd>{value}</dd></div>' for label, value in items)


def map_overview(*, edition, title, lede, stats, peek_actions, desktop_actions, verification,
                 body, peek_extra='', stats_extra='', id='map-overview'):
    return f'''<div id="{id}">
<!--phone-overview--><div class="mpeek">
  <h1 class="hero">{title}</h1>{peek_actions}{verification}{peek_extra}
</div><!--/phone-overview-->
<div class="eyebrow dk">{escape(edition)} · Interactive map · Lean 4</div>
<h1 class="hero dk">{title}</h1><p class="lede">{lede}</p>
<section class="glance" aria-label="The proof at a glance"><dl class="stat-row">{stats_row(stats)}</dl>{stats_extra}</section>
{desktop_actions}{body}
</div>'''
