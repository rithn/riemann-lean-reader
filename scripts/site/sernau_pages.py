"""Render the readable edition and its source-reader shell from pinned metadata."""

from hashlib import sha256
from html import escape
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


def overview_content(data, *, home=False):
    groups, edition = data["groups"], data["edition"]
    total = edition["totals"]
    readme = f'{edition["repository"]}/blob/{edition["revision"]}/grh/README.md'
    guide = next(doc["github"] for doc in edition["documents"] if doc["id"] == "guide")
    theorem = next(t for t in data["theorems"] if t["name"] == "riemannHypothesis")
    stats = "".join(
        f'<div><dt>{label}</dt> <dd>{number(total[key])}</dd></div>'
        for label, key in (("Source groups", "groups"), ("Lean files", "modules"), ("File imports", "moduleEdges"))
    )
    title = 'The <em>Lean</em> proof of the Riemann hypothesis, mapped' if home else 'Sernau’s <em>readable</em> Lean proof'
    introduction = (
        'Explore Luke Sernau’s readable rewriting of Levent Alpöge’s proof, or switch to the original archive map.'
        if home else 'Luke Sernau, colleagues at Anthropic and Claude rewrote Levent Alpöge’s argument in readable Lean.'
    )
    browse = [
        (MAP, "Sernau readable map"), (LIST, "Browse readable groups and files"),
        (ROUTE, "Follow the readable route"), (theorem["href"], "Read the readable main theorem"),
    ]
    if home:
        browse.extend([
            ("/alpoge/", "Alpöge original map"), ("/list/", "Browse original clusters"),
            ("/route/", "Follow the original route"), (theorem["editions"]["original"]["href"], "Read the original main theorem"),
            ("/learn/", "Learning path"), ("/proof-in-numbers/#community-proof-size", "Track community proof size"),
        ])
    browse.append((COMPARE, "Compare all three editions"))
    browse_links = "".join(f'<li>{link(href, label)}</li>' for href, label in browse)
    actions = (
        '<div class="cta">'
        f'{link(theorem["href"], "Read the main theorem →", ' class="btn primary"')} '
        f'{link(ROUTE, "Proof route", ' class="btn"')}</div>'
    )
    return f"""
<div id="map-detail">
  <!--phone-overview--><div class="mpeek">
    <h1 class="hero">{title}</h1>{actions}
    <a class="mstatus" href="{MIT}"><i></i>Comparator passed <span>· verification ›</span></a>
  </div><!--/phone-overview-->
  <div class="eyebrow dk">Sernau readable · Interactive map · Lean 4</div>
  <h1 class="hero dk">{title}</h1>
  <p class="lede">{introduction}</p>
  <section class="glance" aria-label="The readable proof at a glance"><dl>{stats}</dl></section>
  <div class="dk">{actions}</div>
  <h2>Read the graph</h2>
  <p>Each dot is a Lean file. Select a dot to see its direct imports, or select a group label to see its files and connections. An arrow points from the importing file to the file it imports.</p>
  <p class="meta">Zoom in for file labels. With a keyboard, Tab to a group, then use the arrow keys to move between its files and Enter to select.</p>
  <p>The readable release contains {number(total["physicalLines"])} physical lines under <code>grh/src/</code>. The pinned README gives its code-line estimate.</p>
  <p class="meta">Andrew Sutherland’s paranoid Comparator run passed on 26 November 2026 at 02:47:54 UTC. {link(MIT, "Independent verification record")}.</p>
  <h2>Explore the proof</h2>
  <ul class="rows">{browse_links}</ul>
  <p class="meta">{link(readme, "Pinned readable README")} · {link(guide, "Upstream reading guide")}</p>
  <h2 id="groups-title">Source groups</h2><ul class="rows">{"".join(group_row(g) for g in groups)}</ul>
</div>"""


def map_filters(data):
    depths = range(data["edition"]["totals"]["maxGroupDepth"] + 1)
    options = ''.join(f'<option value="{d}">{d}</option>' for d in depths)
    return f"""
<div class="sr-map-selects">
  <label>Source tree <select id="tree" aria-controls="map-graph map-count"><option value="">All groups</option><option value="main">Entry files</option><option value="new">Argument · New</option><option value="lib">Background · Lib</option></select></label>
  <label>Group steps <select id="depth" aria-controls="map-graph map-count"><option value="">Any distance</option>{options}</select></label>
  <label>Colour <select id="colour" aria-controls="map-graph"><option value="tree">Source tree</option><option value="depth">Group distance</option></select></label>
</div>
<p id="map-count" role="status"></p>
<div id="map-legend" aria-label="File colours"></div>"""


def source_provenance(edition):
    docs = " · ".join(link(d["href"], d["label"]) for d in edition["documents"] if d["id"].lower() in ("license", "notice", "attribution"))
    upstream = f'{edition["repository"]}/tree/{edition["revision"]}/{edition["sourceRoot"]}'
    mathlib = edition["mathlibRevision"]
    return (
        f'<p><strong>Sernau readable</strong> · <code>{esc(edition["sourceRoot"])}</code> · '
        f'{link(upstream, edition["revision"][:12], f' title="{esc(edition["revision"])}"')} · {esc(edition["leanToolchain"])} · '
        f'{link("https://github.com/leanprover-community/mathlib4/tree/" + mathlib, "Mathlib " + mathlib[:8])}</p>'
        f'<p>{link(MIT, "Independent verification")} · {link(COMPARE, "Edition comparison")}'
        f'{(" · " + docs) if docs else ""} · {link("/api/editions.json", "Edition data")}</p>'
    )


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
    <button type="button" class="sr-button" data-share>Share this group</button></p>
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
<ol class="sr-route-cards route-steps">{cards}</ol>
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
<div class="eyebrow">Sernau readable · List view</div>
<h1 id="lv-h" tabindex="-1">Groups and Lean files</h1>
<p class="meta">Browse {len(data["groups"])} groups or search the {len(data["modules"])} project files by English label or Lean name.</p>
<form class="sr-list-controls lv-ctl" action="{LIST}" hidden
  data-max-group-depth="{data["edition"]["totals"]["maxGroupDepth"]}"
  data-max-module-depth="{data["edition"]["totals"]["maxModuleDepth"]}">
  <label for="list-query"><span class="sr-screen">Filter by name or topic</span> <input type="search" id="list-query" name="q" data-clarity-mask="true" placeholder="Filter groups or Lean files…" autocomplete="off"></label>
  <label for="list-level">Show <select id="list-level" name="show"><option value="groups">Groups</option><option value="files">Files</option></select></label>
  <label for="list-tree">Source tree <select id="list-tree" name="tree"><option value="">All</option><option value="main">Entry files</option><option value="new">Argument · New</option><option value="lib">Background · Lib</option></select></label>
  <label for="list-depth">Distance <select id="list-depth" name="depth"><option value="">Any distance</option></select></label>
  <label for="list-sort">Order <select id="list-sort" name="order"><option value="depth">By distance</option><option value="folder">By source folder</option><option value="name">By name</option></select></label>
</form>
<p class="meta lv-n" id="list-count" role="status" hidden></p>
<section class="lv-out"><ul class="rows" id="list-rows">{"".join(group_row(g) for g in data["groups"])}</ul></section>
<p class="sr-muted">Source folder and import distance are available for every file. Field, era, level, new-work and guide-match filters have no readable-edition dataset.</p>"""


def reader_content(data):
    pins = "".join(f'<li>{link(t["github"], t["label"] + " (pinned source)")}</li>' for t in data["theorems"])
    return f"""
<p class="sr-crumb" id="file-crumb">{link(MAP, "Sernau map")} <span aria-hidden="true">›</span> <span>Lean reader</span></p>
<section class="sr-subhero sr-file-hero vhead">
  <p class="sr-kicker">Sernau readable · Lean source</p>
  <h1 class="vpath" id="file-title">Lean source reader</h1>
  <p id="file-summary"></p>
  <div class="sr-actions" id="file-actions" hidden>
    <a class="sr-primary" id="file-raw">Raw source</a><a class="vbtn" id="file-github">View on GitHub</a>
    <button class="vbtn" type="button" data-share>Share source</button>
    <button type="button" class="vbtn sr-outline-link" id="reader-outline-link">Outline</button>
    <a id="file-locate" href="{MAP}">Locate on map</a>
    <a id="file-close" href="{MAP}">Return to map</a>
  </div>
  <p id="reader-status" class="sr-muted" role="status"></p>
  <noscript><p>The source reader requires JavaScript. Choose a group in the
  {link(LIST, "text index")} for pinned GitHub links, or follow the {link(ROUTE, "classical RH route")}.</p><ul class="rows">{pins}</ul></noscript>
</section>
<section class="sr-reader" id="reader" hidden aria-label="Lean source workspace">
  <nav id="reader-tabs" class="sr-file-tabs" aria-label="Recently opened files"></nav>
  <article class="sr-code-wrap">
    <div class="sr-code-bar"><span id="file-location"></span>
      <button type="button" class="vbtn" id="fold-code" aria-pressed="false" hidden>Fold proofs</button></div>
    <div id="source-state" class="sr-source-state" role="status"></div>
    <div id="reader-selection" hidden></div>
    <div class="sr-code" id="reader-code" tabindex="0" aria-label="Lean source"></div>
  </article>
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
</section>
<section class="sr-card sr-file-evidence" id="file-evidence" hidden></section>"""


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


def build_sernau_pages(data, render):
    """Supply the shared writer with readable page content and its Markdown mirrors."""
    groups_md = "\n".join(f'- [{g["label"]}]({g["href"]}) · `{g["id"]}`' for g in data["groups"])
    totals = data["edition"]["totals"]
    render(
        MAP, "Sernau readable · Map of the Riemann hypothesis proof",
        "Explore Luke Sernau’s readable Lean rewrite in 29 source groups, trace file imports, and open the pinned proofs.",
        "map", overview_content(data),
        f"[Follow the classical RH route]({ROUTE}) · [Browse groups and Lean files]({LIST}) · [Compare editions]({COMPARE})\n\n"
        f'{number(totals["modules"])} Lean files and {number(totals["moduleEdges"])} direct project-internal module imports at the readable revision.\n\n'
        f'## Source groups\n\n{groups_md}',
    )
    render(
        ROUTE, "Sernau readable · Route from Main", "Trace classical RH to its two named dependencies in the readable Lean edition.",
        "route", route_content(data),
        "\n".join(
            f'- [{t.get("label", t["name"])}]({t["href"]}) · [Pinned Lean line {t["line"]}]({t["github"]})'
            for t in [data["theorems"][0], *data["theorems"][0]["references"]]
        ),
    )
    render(
        LIST, "Sernau readable · Groups and Lean files", "A text index of the readable edition’s groups and Lean files.",
        "list", list_content(data), groups_md, noindex=True,
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
        "reader", reader_content(data), noindex=True,
    )
