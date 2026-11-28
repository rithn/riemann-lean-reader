"""Publish the readable proof clusters and their weighted uses."""

from collections import defaultdict, deque
import json
from urllib.parse import quote


EXPORTS = ("parts.json", "edges.json", "labels.json")


def dependency_tree(size, root, edges):
    uses = [[] for _ in range(size)]
    for source, target, weight in edges:
        uses[source].append((target, weight))

    steps, parents, weights = [None] * size, [None] * size, [0] * size
    steps[root] = 0
    pending = deque([root])
    while pending:
        source = pending.popleft()
        step = steps[source] + 1
        for target, weight in uses[source]:
            if steps[target] is None:
                steps[target] = step
                pending.append(target)
            parent = parents[target]
            if steps[target] == step and (parent is None or (weight, -source) > (weights[target], -parent)):
                parents[target], weights[target] = source, weight
    return steps, parents


def build_part_graph(out, url, inputs, edition, modules, theorems, json_output, github):
    parts, imports, labels = (
        json.loads((inputs / filename).read_text(encoding="utf-8")) for filename in EXPORTS
    )
    pin = {key: edition[key] for key in ("id", "revision", "buildId")}
    root, = (index for index, part in enumerate(parts.values()) if part.get("final"))
    steps, parents = dependency_tree(len(parts), root, imports)
    base = url.rsplit("/", 1)[0]
    detail_urls = {}
    details = defaultdict(dict)
    clusters, search = [], []
    file_clusters = {}
    outline = {name: {declaration["name"] for declaration in module["declarations"]}
               for name, module in modules.items()}

    def declaration_links(declaration):
        module = modules[declaration["module"]]
        name, line = declaration["name"], declaration["line"]
        # The resolver gives anonymous declarations synthetic names. Open those at their source line.
        fragment = quote(name) if name in outline[module["name"]] else f"L{line}"
        return {**declaration, "href": f'{module["href"]}#{fragment}',
                "github": github(edition, module["path"], line)}

    for index, (key, part) in enumerate(parts.items()):
        step = steps[index]
        ring = str(step) if step is not None else "instances"
        files = part["files"]
        source_counts = {tree: sum(name.startswith(tree + ".") for name in files)
                         for tree in ("Lib", "New")}
        tree = max(source_counts, key=source_counts.get).lower() if any(source_counts.values()) else "main"
        label = labels[key]
        clusters.append({
            "id": key, "label": label["label"], "count": part["count"],
            "ring": ring, "parent": parents[index], "tree": tree,
        })
        search.append([label["description"], " ".join(name for names in files.values() for name in names)])
        for module, names in files.items():
            if module not in file_clusters or len(names) > file_clusters[module][1]:
                file_clusters[module] = (index, len(names))
        detail = {
            **label,
            "head": declaration_links(part["head"]),
            "mostUsed": [declaration_links(item) for item in part["mostUsed"]],
            "files": [[modules[name]["href"], name, len(names)] for name, names in files.items()],
        }
        if index == root:
            detail["theorems"] = [{key: theorem[key] for key in ("name", "href", "github")} for theorem in theorems]
        details[ring][key] = detail

    for ring, records in details.items():
        detail_urls[ring] = detail_url = f"{base}/part-rings/{ring}.json"
        json_output(out, detail_url, {"edition": pin, "parts": records})
    search_url = f"{base}/part-search.json"
    json_output(out, search_url, {"edition": pin, "search": search})
    json_output(out, url, {
        "edition": pin, "root": root, "clusters": clusters, "imports": imports,
        "fileClusters": {module: index for module, (index, _) in file_clusters.items()},
        "detailUrls": detail_urls, "searchUrl": search_url,
    })
