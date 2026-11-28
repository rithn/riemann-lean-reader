"""Write the chapter view from the checked-in Sernau parts export."""

from collections import defaultdict
import json
from urllib.parse import quote


EXPORTS = ("parts.json", "edges.json", "labels.json", "handout.json")


def build_part_graph(out, url, inputs, edition, modules, groups, map_labels, theorems,
                     json_output, github):
    parts, imports, labels, handout = (
        json.loads((inputs / filename).read_text(encoding="utf-8")) for filename in EXPORTS
    )
    edition_pin = {key: edition[key] for key in ("id", "revision", "buildId")}
    chapters = handout["chapters"]
    chapter_clouds = {
        f"ch:{chapter}": {"label": info["label"], "title": info["title"], "chapter": chapter}
        for chapter, info in chapters.items()
    }
    source_groups = sorted({part["cloud"][4:] for part in parts.values() if part["cloud"].startswith("src:")})
    clouds = {**chapter_clouds, **{
        f"src:{group}": {"label": map_labels[group], "title": groups[group]["label"]}
        for group in source_groups
    }}
    # Put the eight chapters above the source groups. Within each row reserve
    # space for the largest cloud, so fitting and caption placement can be shared.
    chapter_ids = list(chapter_clouds)
    source_ids = [f"src:{group}" for group in source_groups]
    rows = [chapter_ids[:4], chapter_ids[4:]]
    rows.extend(source_ids[start:start + 5] for start in range(0, len(source_ids), 5))
    centers = {}
    for row, members in enumerate(rows):
        offset = (5 - len(members)) * 235 // 2
        for column, cloud in enumerate(members):
            centers[cloud] = [column * 235 + offset, row * 200]
    graph = {
        "edition": edition_pin,
        "groupLabels": {key: info["label"] for key, info in clouds.items()},
        "groupCenters": centers,
        "files": [[key, labels[key]["label"], part["height"], part["cloud"],
                   part["count"], part["kind"], part.get("final", False)] for key, part in parts.items()],
        "imports": imports,
        "groups": {},
    }

    outline = {name: {declaration["name"] for declaration in module["declarations"]}
               for name, module in modules.items()}

    def declaration_links(declaration):
        module = modules[declaration["module"]]
        name, line = declaration["name"], declaration["line"]
        # The research resolver gives anonymous declarations synthetic names.
        # Those declarations can be opened in the reader at their source line.
        fragment = quote(name) if name in outline[module["name"]] else f"L{line}"
        return {**declaration, "href": f'{module["href"]}#{fragment}',
                "github": github(edition, module["path"], line)}

    siblings = defaultdict(list)
    for part in parts:
        siblings[part.partition("#")[0]].append(part)
    details = {key: {} for key in clouds}
    for key, part in parts.items():
        cloud = part["cloud"]
        info = clouds[cloud]
        detail = {
            **labels[key],
            "kind": part["kind"],
            "splitSiblings": [sibling for sibling in siblings[key.partition("#")[0]] if sibling != key],
            "head": declaration_links(part["head"]),
            "mostUsed": [declaration_links(item) for item in part["mostUsed"]],
        }
        if chapter := info.get("chapter"):
            detail["chapter"] = info["title"]
        if note := part.get("note"):
            detail["note"] = handout["notes"][note]["title"]
        if part.get("final"):
            detail["theorems"] = [{key: theorem[key] for key in ("name", "href", "github")} for theorem in theorems]
        details[cloud][key] = detail

    base = url.rsplit("/", 1)[0]
    for key, info in clouds.items():
        detail_url = f"{base}/part-groups/{key.replace(':', '-')}.json"
        graph["groups"][key] = {"title": info["title"], "dataUrl": detail_url}
        json_output(out, detail_url, {"edition": edition_pin, "handout": handout["url"], "parts": details[key]})
    json_output(out, url, graph)
