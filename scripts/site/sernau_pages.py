"""Render the readable edition and its source-reader shell from pinned metadata."""

from hashlib import sha256
from html import escape
from pathlib import Path
from urllib.parse import quote


MAP = "/sernau/"
ROUTE = MAP + "route/"
LIST = MAP + "list/"
READER = MAP + "reader/"
COMPARE = "/shorter-riemann-hypothesis-proof/"
MIT = "https://math.mit.edu/~drew/shortgrh/"


def esc(value):
    return escape(str(value), quote=True)


def link(href, label, attrs=""):
    return f'<a href="{esc(href)}"{attrs}>{esc(label)}</a>'


def number(value):
    return f"{value:,}"


def provenance(record):
    origin = record.get("labelOrigin") or "Explorer wording"
    review = record.get("labelReview")
    if review == "reviewed":
        origin += " · source wording reviewed"
    elif review == "draft":
        origin += " · draft"
    evidence = record.get("labelEvidence") or []
    return link(evidence[0]["github"], origin) if evidence else esc(origin)


def group_row(group):
    return (
        f'<li data-group-row="{esc(group["id"])}">{link(group["href"], group["label"])}'
        f'<small><code>{esc(group["id"])}</code> · {number(group["moduleCount"])} '
        f'{"file" if group["moduleCount"] == 1 else "files"} · '
        f'{group["depth"]} group steps from Main</small></li>'
    )


def module_row(module):
    return (
        f'<li data-module-row="{esc(module["name"])}">{link(module["href"], module["label"])}'
        f'<small><code>{esc(module["name"])}.lean</code> · {module["depth"]} module steps · '
        f'{link(module["github"], "Pinned source")}</small></li>'
    )


def overview_content(data):
    groups, edition = data["groups"], data["edition"]
    total = edition["totals"]
    readme = f'{edition["repository"]}/blob/{edition["revision"]}/grh/README.md'
    guide = next(doc["github"] for doc in edition["documents"] if doc["id"] == "guide")
    stats = "".join(
        f'<div><dt>{esc(label)}</dt><dd>{number(total[key])}</dd></div>'
        for label, key in (
            ("Lean files", "modules"), ("Source groups", "groups"), ("File imports", "moduleEdges"))
    )
    return f"""
<section class="sr-hero">
  <div>
    <p class="sr-kicker">Sernau readable · Lean 4</p>
    <h1><em>Riemann hypothesis</em> Readable proof map</h1>
    <p>Luke Sernau, colleagues at Anthropic and Claude rewrote Levent Alpöge’s argument in readable Lean.</p>
    <p class="sr-actions">
      {link(data["theorems"][0]["href"], "Read main theorem →", ' class="sr-primary"')}
      {link(ROUTE, "Proof route", ' class="sr-button"')}
    </p>
  </div>
  <dl class="sr-stats" aria-label="The readable proof at a glance">{stats}</dl>
</section>
<section class="sr-map" id="proof-map" hidden aria-label="Interactive dependency map">
  <div class="sr-map-controls">
    <div><p class="sr-kicker">Dependency map</p><h2>From Main to its imports</h2></div>
    <div class="sr-map-selects">
      <label>Source tree <select id="tree" aria-controls="map-graph map-count"><option value="">All groups</option><option value="main">Entry files</option><option value="new">Argument · New</option><option value="lib">Background · Lib</option></select></label>
      <label>Group steps <select id="depth" aria-controls="map-graph map-count"><option value="">Any distance</option></select></label>
      <label>Colour <select id="colour" aria-controls="map-graph"><option value="tree">Source tree</option><option value="depth">Group distance</option></select></label>
    </div>
  </div>
  <div class="sr-map-layout">
    <div class="sr-plot">
      <svg id="map-graph" viewBox="0 0 900 552" role="group" aria-label="Import graph with selectable source groups"></svg>
      <div class="sr-zoom" aria-label="Map zoom">
        <button type="button" id="zoom-out" aria-label="Zoom out">−</button>
        <button type="button" id="zoom-in" aria-label="Zoom in">+</button>
        <button type="button" id="reset-view">Reset view</button>
      </div>
    </div>
    <aside class="sr-map-detail" id="map-detail" aria-label="Selected group"></aside>
  </div>
  <div class="sr-map-foot">
    <p id="map-count" role="status"></p><div id="map-legend" aria-label="Group colours"></div>
    {link(LIST, "Open the text list →")}
  </div>
</section>
<p id="map-status" class="sr-muted" hidden role="status"></p>
<section class="sr-overview-notes">
  <article class="sr-card">
    <h2>Read the graph</h2>
    <p>Each point represents a folder group or an entry file. Node size grows with file count. Ring numbers count the shortest directed group path from <code>Main</code>. Select a node to see what it imports, what imports it and the source lines behind those connections.</p>
    <p>Groups use the first two segments of the module name. Grouping can create reciprocal edges. Module routes and transitive counts use the original file imports.</p>
  </article>
  <article class="sr-card">
    <h2>Release and verification</h2>
    <p>The publisher includes comments and a reading guide. This map covers {number(total["physicalLines"])} physical lines under <code>grh/src/</code>. See the {link(readme, "pinned readable README")} for its code-line estimate.</p>
    <p>Andrew Sutherland’s readable paranoid Comparator run passed on 26 November 2026 at 02:47:54 UTC. {link(MIT, "Independent verification record →")}</p>
    <p>{link(guide, "Read the author’s proof guide")} · {link(COMPARE, "Compare all three editions")} · {link("/proof-in-numbers/", "Proof in numbers")}</p>
  </article>
</section>
<section class="sr-index" aria-labelledby="groups-title">
  <div class="sr-section-head"><h2 id="groups-title">Source groups</h2>{link(LIST, "List and file search →")}</div>
  <ul class="sr-rows sr-columns">{"".join(group_row(g) for g in groups)}</ul>
</section>"""


def edge_list(group, neighbors, data, incoming):
    groups = {g["id"]: g for g in data["groups"]}
    edges = {(e["from"], e["to"]): e["evidence"] for e in data["edges"]}
    items = []
    for other in neighbors:
        left, right = (other, group["id"]) if incoming else (group["id"], other)
        evidence = edges[(left, right)]
        examples = "".join(
            f'<li>{link(e["href"], e["from"] + " → " + e["to"])} '
            f'<small>{link(e["github"], "Pinned line " + str(e["line"]))}</small></li>'
            for e in evidence
        )
        items.append(
            f'<li><details><summary><code>{esc(other)}</code><small>{number(len(evidence))} '
            f'{"file import" if len(evidence) == 1 else "file imports"}</small></summary>'
            f'<p>{link(groups[other]["href"], groups[other]["label"] + " →")}</p>'
            f'<ul class="sr-rows sr-evidence">{examples}</ul></details></li>'
        )
    return f'<ul class="sr-edge-list">{"".join(items)}</ul>' if items else '<p class="sr-muted">None among the readable groups.</p>'


def group_content(group, data):
    groups = {g["id"]: g for g in data["groups"]}
    modules = [data["modules"][name] for name in group["modules"]]
    route = " <span aria-hidden=\"true\">→</span> ".join(link(groups[name]["href"], name) for name in group["route"])
    folder = group["id"].split(".")[0]
    scope = {
        "New": "The upstream project puts the argument and its setup under New.",
        "Lib": "The upstream project puts background and supporting material under Lib.",
    }.get(folder, "One of the readable project’s two entry modules.")
    return f"""
<p class="sr-crumb">{link(MAP, "Sernau map")} <span aria-hidden="true">›</span> <span>Source group</span></p>
<section class="sr-subhero">
  <p class="sr-kicker">Sernau readable · Source group</p>
  <h1>{esc(group["label"])}</h1>
  <p><code>{esc(group["id"])}</code> · {provenance(group)}</p>
  <p>{scope}</p>
  <p class="sr-actions">{link(MAP + "?group=" + quote(group["slug"]), "Locate on the map →", ' class="sr-primary"')}
    <button type="button" class="sr-button" data-share hidden>Share this group</button></p>
</section>
<div class="sr-overview-notes">
  <section class="sr-card">
    <h2>Shortest group route from Main</h2><p class="sr-route-chain">{route or "No group route from Main."}</p>
    <p>{number(group["depth"])} group steps</p>
  </section>
  <section class="sr-card">
    <h2>Reach through file imports</h2>
    <p>{number(group["moduleCount"])} member files · {number(group["reach"])} other readable files reachable from its members.</p>
  </section>
</div>
<div class="sr-group-layout">
  <section class="sr-card">
    <h2>Member modules</h2>
    <ul class="sr-rows">{"".join(module_row(m) for m in modules)}</ul>
  </section>
  <div>
    <section class="sr-card"><h2>Imports</h2>{edge_list(group, group["imports"], data, False)}</section>
    <section class="sr-card"><h2>Imported by</h2>{edge_list(group, group["importers"], data, True)}</section>
  </div>
</div>"""


def route_content(data):
    main = next(theorem for theorem in data["theorems"] if theorem["name"] == "riemannHypothesis")
    refs = {r["name"]: r for r in main["references"]}
    implication, bound = refs["New.zeta_zeros_on_line"], refs["New.grh"]
    first, second, third = (data["modules"][m] for m in ("Main", "New.Main", "New.Reduction.OneSidedBound"))
    pins = [main, implication, bound]
    steps = [
        (first, "State classical RH", "The top-level theorem applies New.zeta_zeros_on_line to New.grh."),
        (second, "Go from a zero-free half-plane to the critical line",
         "The implication takes a nonvanishing hypothesis in the half-plane Re(s) > ½ and concludes classical RH."),
        (third, "Prove the half-plane nonvanishing result",
         "New.grh supplies the nonvanishing input used by the first step."),
    ]
    cards = "".join(
        f'<li class="sr-card"><p class="sr-kicker">{esc(module["name"])}.lean</p><h2>{esc(title)}</h2>'
        f'<p>{esc(description)}</p><p class="sr-actions">'
        f'{link(pin["href"], pin["name"], " class=\"sr-primary\"")}'
        f'{link(pin["github"], "Pinned line " + str(pin["line"]))}</p></li>'
        for (module, title, description), pin in zip(steps, pins)
    )
    groups = data["groups"]
    depths = "".join(
        f'<li><p><b>{d}</b> {"group step" if d == 1 else "group steps"} · {len(items)} '
        f'{"group" if len(items) == 1 else "groups"}</p><ul class="sr-rows">'
        f'{"".join(group_row(g) for g in items)}</ul></li>'
        for d in range(data["edition"]["totals"]["maxGroupDepth"] + 1)
        for items in [[g for g in groups if g["depth"] == d]]
    )
    theorem_links = "".join(
        f'<li>{link(t["href"], t["label"])}<small><code>{esc(t["name"])}</code></small></li>'
        for t in data["theorems"]
    )
    return f"""
<p class="sr-crumb">{link(MAP, "Sernau map")} <span aria-hidden="true">›</span> <span>Route from Main</span></p>
<section class="sr-subhero">
  <p class="sr-kicker">Sernau readable · Source route</p>
  <h1>From the theorem to its dependencies</h1>
  <p>Start with classical RH and follow the two named references in its Lean proof.</p>
</section>
<ol class="sr-route-cards">{cards}</ol>
<section class="sr-card">
  <h2>The file import path</h2>
  <p class="sr-route-chain">{link(first["href"], first["name"])} → {link(second["href"], second["name"])} → {link(third["href"], third["name"])}</p>
  <p>{link(first["href"] + "#L2", "Main import at line 2")} · {link(second["href"] + "#L1", "New.Main import at line 1")}</p>
  <p>The arrows in this path mark imports. The steps above mark named declarations in those files.</p>
</section>
<section class="sr-card">
  <h2>Five statements in Main</h2><ul class="sr-rows sr-columns">{theorem_links}</ul>
</section>
<section class="sr-card">
  <h2>Group distance from Main</h2>
  <p>Each ring counts one group import step. The deepest module is {data["edition"]["totals"]["maxModuleDepth"]} module import steps from Main.</p>
  <div id="route-rings" hidden></div>
  <ol class="sr-depth-list" id="depth-list">{depths}</ol>
</section>"""


def list_content(data):
    return f"""
<p class="sr-crumb">{link(MAP, "Sernau map")} <span aria-hidden="true">›</span> <span>List</span></p>
<section class="sr-subhero">
  <p class="sr-kicker">Sernau readable · List</p><h1>Groups and Lean files</h1>
  <p>Browse {len(data["groups"])} groups or search the {len(data["modules"])} project files by English label or Lean name.</p>
</section>
<form class="sr-list-controls sr-card" action="{LIST}" hidden>
  <label for="list-query">Filter by name or topic <input type="search" id="list-query" name="q" data-clarity-mask="true" placeholder="Try Main.lean or OneSidedBound" autocomplete="off"></label>
  <label for="list-level">Show <select id="list-level" name="show"><option value="groups">Groups</option><option value="files">Files</option></select></label>
  <label for="list-tree">Source tree <select id="list-tree" name="tree"><option value="">All</option><option value="main">Entry files</option><option value="new">Argument · New</option><option value="lib">Background · Lib</option></select></label>
  <label for="list-depth">Distance <select id="list-depth" name="depth"><option value="">Any distance</option></select></label>
  <label for="list-sort">Order <select id="list-sort" name="order"><option value="depth">By distance</option><option value="folder">By source folder</option><option value="name">By name</option></select></label>
  <button type="submit" class="sr-button">Filter</button>
</form>
<p class="sr-muted" id="list-count" role="status" hidden></p>
<section class="sr-index"><ul class="sr-rows sr-columns" id="list-rows">{"".join(group_row(g) for g in data["groups"])}</ul></section>
<p class="sr-muted">Source folder and import distance are available for every file. Field, era, level, new-work and guide-match filters have no readable-edition dataset.</p>"""


def reader_content():
    return f"""
<p class="sr-crumb" id="file-crumb">{link(MAP, "Sernau map")} <span aria-hidden="true">›</span> <span>Lean reader</span></p>
<section class="sr-subhero sr-file-hero">
  <p class="sr-kicker">Sernau readable · Lean source</p>
  <h1 id="file-title">Lean source reader</h1>
  <p id="file-summary"></p>
  <div class="sr-actions" id="file-actions" hidden>
    <a class="sr-primary" id="file-raw">Raw source</a><a class="sr-button" id="file-github">View on GitHub</a>
    <button class="sr-button" type="button" data-share>Share source</button>
    <a id="file-close" href="{MAP}">Return to map</a>
  </div>
  <p id="reader-status" class="sr-muted" role="status"></p>
  <noscript><p>The source reader requires JavaScript. Choose a group in the
  {link(LIST, "text index")} for pinned GitHub links, or follow the {link(ROUTE, "classical RH route")}.</p></noscript>
</section>
<section class="sr-reader" id="reader" hidden aria-label="Lean source workspace">
  <nav id="reader-tabs" class="sr-file-tabs" aria-label="Recently opened files"></nav>
  <aside class="sr-reader-side" aria-label="Source navigation">
    <details open id="outline-panel"><summary>Declaration outline</summary>
      <label class="sr-screen" for="reader-filter">Search this group’s files and declarations</label>
      <input type="search" id="reader-filter" data-clarity-mask="true" placeholder="Search this group" autocomplete="off">
      <ul class="sr-rows" id="reader-outline"></ul>
    </details>
    <details id="reader-files-panel"><summary>Files in this group</summary><ul class="sr-rows" id="reader-files"></ul></details>
    <details id="reader-imports-panel"><summary>Imports</summary><ul class="sr-rows" id="reader-imports"></ul></details>
    <details id="reader-importers-panel"><summary>Imported by</summary><ul class="sr-rows" id="reader-importers"></ul></details>
  </aside>
  <article class="sr-code-wrap">
    <div class="sr-code-bar"><span id="file-location"></span>
      <button type="button" class="sr-button" id="fold-code" aria-pressed="false" hidden>Fold proofs</button></div>
    <div id="source-state" class="sr-source-state" role="status"></div>
    <div id="reader-selection" hidden></div>
    <div class="sr-code" id="reader-code" tabindex="0" aria-label="Lean source"></div>
  </article>
</section>
<section class="sr-card sr-file-evidence" id="file-evidence" hidden></section>"""


def document(out, path, title, desc, kind, main, edition, assets, site_url, *, md=None, noindex=False, analytics_html=""):
    canonical = site_url + path
    card = site_url + assets["card"]
    alternate = f'<link rel="alternate" type="text/markdown" href="{path}index.md">' if md else ""
    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    docs = " · ".join(link(d["href"], d["label"]) for d in edition["documents"] if d["id"].lower() in ("license", "notice", "attribution"))
    current = lambda page: ' aria-current="page"' if page == kind else ""
    upstream = f'{edition["repository"]}/tree/{edition["revision"]}/{edition["sourceRoot"]}'
    body = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#0a1020">
<link rel="canonical" href="{esc(canonical)}">{alternate}{robots}
<meta property="og:type" content="website"><meta property="og:site_name" content="RH Lean Explorer">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical)}"><meta property="og:image" content="{esc(card)}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{esc(card)}">
<link rel="icon" type="image/png" href="/favicon-32.png">
<link rel="stylesheet" href="{assets["css"]}">
<script defer src="{assets["js"]}"></script>
{analytics_html}
</head>
<body data-view="{kind}" data-revision="{esc(edition["revision"])}"
 data-overview="{esc(edition["overviewUrl"])}" data-modules="{esc(edition["modulesUrl"])}"
 data-groups="{esc(edition["groupsBaseUrl"])}">
<a class="sr-skip" href="#main">Skip to content</a>
<header class="sr-top"><div class="sr-top-inner">
  <a class="sr-brand" href="/"><span aria-hidden="true">ζ</span> RH Lean <b>Explorer</b></a>
  <nav aria-label="Site sections">{link("/status/", "Status")} {link("/guides/", "Guides")} {link("/timeline/", "Timeline")} {link("/learn/", "Learn")}</nav>
  <form class="sr-search" action="{LIST}" role="search" aria-label="Search the readable edition" hidden>
    <label class="sr-screen" for="global-query">Search groups, theorems and Lean files</label>
    <input id="global-query" name="q" type="search" data-clarity-mask="true" placeholder="Search the readable edition" autocomplete="off">
    <div id="search-results" hidden aria-label="Search results"></div>
  </form>
</div></header>
<div class="sr-mode"><div class="sr-mode-inner">
  <nav class="sr-editions" aria-label="Proof edition">
    {link("/", "Alpöge original", ' id="original-edition"')} {link(MAP, "Sernau readable", ' aria-current="true"')}
  </nav>
  <nav class="sr-page-nav" aria-label="Readable edition">{link(MAP, "Map", current("map"))}
    {link(ROUTE, "Route", current("route"))} {link(LIST, "List", current("list"))}
    {link(COMPARE, "Compare editions")}</nav>
</div></div>
<main class="sr-main" id="main">{main}</main>
<footer class="sr-footer">
  <p><strong>Sernau readable</strong> · <code>{esc(edition["sourceRoot"])}</code> · {link(upstream, edition["revision"][:12], f' title="{esc(edition["revision"])}"')} · {esc(edition["leanToolchain"])} ·
    {link("https://github.com/leanprover-community/mathlib4/tree/" + edition["mathlibRevision"], "Mathlib " + edition["mathlibRevision"][:8])}</p>
  <p>{link(MIT, "Independent verification")} · {link(COMPARE, "Edition comparison")}{(" · " + docs) if docs else ""} ·
    {link("/api/editions.json", "Edition data")} · {link("https://x.com/SomTheBuilder", "Send a correction")}</p>
</footer>
<output class="sr-share-status" id="share-status" aria-live="polite"></output>
</body></html>
"""
    folder = out / path.strip("/")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(body, encoding="utf-8")
    if md:
        (folder / "index.md").write_text(
            f"# {title}\n\nSernau readable · {edition['revision']}\n\n{desc}\n\n{md}\n\n"
            f"[Pinned source tree]({upstream}) · [Independent verification]({MIT})\n",
            encoding="utf-8",
        )


def readable_card(out, groups, revision):
    from PIL import ImageDraw
    from og_cards import GOLD, FG, FG2, background, font, star

    img = background(GOLD, int(revision[:8], 16))
    canvas = ImageDraw.Draw(img)
    canvas.text((75, 82), "RH LEAN EXPLORER  /  SERNAU READABLE", font=font("semi", 25), fill=GOLD)
    canvas.text((75, 161), "The shorter Riemann", font=font("serif", 69), fill=FG)
    canvas.text((75, 247), "hypothesis proof", font=font("serif", 69), fill=FG)
    canvas.text((79, 380), "A source map of the readable Lean edition", font=font("reg", 31), fill=FG2)
    canvas.text((79, 472), "803 Lean files   ·   29 source groups   ·   " + revision[:8], font=font("med", 23), fill=GOLD)
    cx, cy = 1000, 225
    star(canvas, cx, cy, 16, GOLD)
    from math import cos, sin, tau
    for depth in range(1, max(g["depth"] for g in groups) + 1):
        ring = [g for g in groups if g["depth"] == depth]
        r = depth * 26
        canvas.circle((cx, cy), r, outline=(67, 72, 103), width=1)
        for i in range(len(ring)):
            angle = tau * (i / len(ring) + depth / 9)
            x, y = cx + r * cos(angle), cy + r * sin(angle)
            canvas.circle((x, y), 3, fill=(115, 201, 188))
    dest = out / "og" / "sernau.png"
    dest.parent.mkdir(exist_ok=True)
    img.quantize(colors=256).save(dest, optimize=True)
    return "/og/sernau.png?v=" + sha256(dest.read_bytes()).hexdigest()[:10]


def build_sernau_pages(out, data, *, site_url, analytics_html=""):
    """Return canonical indexable and source URL paths for the outer site build."""
    out = Path(out)
    edition = data["edition"]
    assets = {}
    for extension in ("css", "js"):
        authored = out / f"sernau.{extension}"
        content = authored.read_bytes()
        versioned = out / f"sernau.{sha256(content).hexdigest()[:10]}.{extension}"
        versioned.write_bytes(content)
        assets[extension] = "/" + versioned.name
    assets["card"] = readable_card(out, data["groups"], edition["revision"])
    indexed = []

    def render(path, title, desc, kind, body, md=None, noindex=False):
        document(out, path, title, desc, kind, body, edition, assets, site_url, md=md, noindex=noindex,
                 analytics_html=analytics_html)
        if not noindex:
            indexed.append(path)

    groups_md = "\n".join(f'- [{g["label"]}]({g["href"]}) · `{g["id"]}`' for g in data["groups"])
    render(
        MAP, "Sernau readable · Map of the shorter Riemann hypothesis proof",
        "Explore the Luke Sernau readable Lean rewrite in 29 source groups, trace file imports, and open the pinned proofs.",
        "map", overview_content(data),
        f"[Follow the classical RH route]({ROUTE}) · [Browse groups and Lean files]({LIST}) · [Compare editions]({COMPARE})\n\n"
        f'803 Lean files and 1,733 direct project-internal module imports at the readable revision.\n\n## Source groups\n\n{groups_md}',
    )
    render(
        ROUTE, "Sernau readable · Route from Main", "Trace classical RH to its two named dependencies in the readable Lean edition.",
        "route", route_content(data),
        "\n".join(
            f'- [{t["label"]}]({t["href"]}) · [Pinned Lean line {t["line"]}]({t["github"]})'
            for t in [data["theorems"][0], *data["theorems"][0]["references"]]
            for t in [dict(t, label=t.get("label", t["name"]))]
        ),
    )
    render(
        LIST, "Sernau readable · Groups and Lean files", "A text index of the readable edition’s groups and Lean files.",
        "list", list_content(data), noindex=True,
    )
    for group in data["groups"]:
        md = "\n".join(
            f'- [{m["label"]}]({m["href"]}) · `{m["name"]}` · [Pinned source]({m["github"]})'
            for name in group["modules"] for m in [data["modules"][name]]
        )
        render(
            group["href"], f'{group["label"]} · Sernau readable',
            f'{group["id"]} is a readable-edition source group with {group["moduleCount"]} Lean files.',
            "group", group_content(group, data), f"## Member modules\n\n{md}",
        )
    render(
        READER, "Lean source reader · Sernau readable", "Read the pinned Lean files of the Sernau readable edition.",
        "reader", reader_content(), noindex=True,
    )
    return {"indexed": indexed, "source": [module["href"] for module in data["modules"].values()]}
