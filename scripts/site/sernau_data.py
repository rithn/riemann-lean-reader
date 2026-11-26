"""Build the readable Sernau edition from the pinned upstream Git objects."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
import csv
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tarfile
import tempfile
from urllib.parse import quote


REPO = Path(__file__).resolve().parents[2]
INPUTS = REPO / "data" / "sernau"
XREF = REPO / "scripts" / "xref"
sys.path.insert(0, str(XREF))
import leansrc

DOCUMENTS = (
    ("license", "Apache License 2.0", "grh/LICENSE"),
    ("notice", "Notice", "grh/NOTICE"),
    ("attribution", "Source attribution", "grh/ATTRIBUTION.md"),
    ("guide", "Upstream reading guide", "grh/GUIDE.md"),
    ("contents", "Upstream contents", "grh/CONTENTS.md"),
    ("index", "Upstream index", "grh/INDEX.md"),
    ("references", "Upstream reference audit", "grh/REFERENCES.md"),
    ("readme", "Readable release and checks", "grh/README.md"),
    ("release", "Upstream release README", "README.md"),
    ("toolchain", "Lean toolchain pin", "grh/lean-toolchain"),
    ("lake-manifest", "Lake dependency pins", "grh/lake-manifest.json"),
    ("lake-project", "Lake project settings", "grh/lakefile.toml"),
    ("comparator", "Comparator settings", "grh/comparator.json"),
    ("challenge", "Comparator challenge", "grh/Challenge.lean"),
    ("axioms", "Axiom inspection script", "grh/scripts/PrintAxioms.lean"),
)
CONTENTS_ENTRY = re.compile(r"^- `([^`]+)` \((\d+)\):\s+(.+)$")
IMPORT = re.compile(r"^(?:(?:public|private|meta)\s+)*import\s+(\S.*)$")
NAME_ATOM = r"(?:[^\W\d][\w'!?]*|«[^»]*»)"
DECLARATION_HEADER = re.compile(
    rf"\b(?:class\s+(?:abbrev|inductive)|{'|'.join(sorted(leansrc.DECL_KINDS - {'example'}))})"
    rf"\s+(?:\(priority\s*:=\s*[^)]+\)\s*)?(?P<name>{NAME_ATOM}(?:\.{NAME_ATOM})*)"
)


def require(condition, message):
    if not condition:
        raise ValueError(f"Sernau data: {message}")


def git(directory, *args):
    try:
        return subprocess.check_output(
            ["git", "-C", str(directory), *args], stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as error:
        reason = error.stderr.decode(errors="replace").strip()
        raise ValueError(f"Sernau source: git {' '.join(args)} in {directory}: {reason}") from error


def source_repository(edition):
    explicit = os.environ.get("SERNAU_SOURCE_DIR")
    revision = edition["revision"]
    if explicit:
        source = Path(explicit).expanduser().resolve()
        require(git(source, "rev-parse", "HEAD").decode().strip() == revision,
                f"SERNAU_SOURCE_DIR must point to a Git checkout at {revision}")
        return source

    owner = getattr(os, "getuid", lambda: 0)()
    default_cache = Path(tempfile.gettempdir()) / f"rh-lean-explorer-{owner}"
    cache = Path(os.environ.get("SERNAU_CACHE_DIR") or default_cache).expanduser()
    cache.mkdir(parents=True, exist_ok=True)
    cached = cache / f"sernau-{revision}.git"
    if not cached.exists():
        with tempfile.TemporaryDirectory(prefix="sernau-fetch-", dir=cache) as staging:
            staged = Path(staging) / "source.git"
            staged.mkdir()
            git(staged, "init", "--bare", "--quiet")
            git(staged, "fetch", "--quiet", "--depth=1", edition["repository"] + ".git",
                f"{revision}:refs/heads/sernau-source")
            validate_source(staged, edition)
            try:
                staged.rename(cached)
            except OSError:
                if not cached.is_dir():
                    raise
    return cached


def validate_source(source, edition):
    revision = edition["revision"]
    require(git(source, "rev-parse", f"{revision}^{{commit}}").decode().strip() == revision,
            "upstream commit object does not match the manifest")
    for pin in (edition, edition["compact"]):
        root = pin["sourceRoot"]
        tree = git(source, "rev-parse", f"{revision}:{root}").decode().strip()
        require(tree == pin["sourceTree"], f"{root} Git tree does not match the manifest")


def archive_inputs(edition):
    source = source_repository(edition)
    validate_source(source, edition)
    compact = edition["compact"]["sourceRoot"]
    compact_list = git(source, "ls-tree", "-r", "--name-only", "-z", edition["revision"], compact)
    require(sum(path.endswith(b".lean") for path in compact_list.split(b"\0")) == edition["compact"]["modules"],
            "compact source file count differs from the manifest")
    archive = git(
        source, "archive", "--format=tar", edition["revision"], edition["sourceRoot"],
        *(path for _, _, path in DOCUMENTS),
        f"{compact}/Main.lean", f"{compact}/Statements.lean", "grh-compact/comparator.json",
        "grh-compact/lean-toolchain", "grh-compact/lake-manifest.json",
    )
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        return {member.name: tar.extractfile(member).read() for member in tar if member.isfile()}


def json_output(out, url, data):
    target = out / url.lstrip("/")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")


def binary_output(out, url, data):
    target = out / url.lstrip("/")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def github(edition, path, line=None, end_line=None):
    url = f"{edition['repository']}/blob/{edition['revision']}/{quote(path)}"
    if line:
        url += f"#L{line}"
        if end_line and end_line != line:
            url += f"-L{end_line}"
    return url


def evidence(edition, files, path, line, end_line):
    require(0 < line <= end_line <= len(files[path].splitlines()),
            f"invalid label evidence range {path}:{line}–{end_line}")
    return {
        "path": path, "line": line, "endLine": end_line,
        "github": github(edition, path, line, end_line),
        "sha256": hashlib.sha256(files[path]).hexdigest(),
    }


def module_label(edition, files, inventory, contents):
    name = inventory["module"]
    path = inventory["path"]
    start, end = (int(value) for value in inventory["sourceLines"].split("-"))
    record = {
        "labelEvidence": [evidence(edition, files, path, start, end)],
        "sourceTitle": None,
    }
    if inventory["contentsLine"]:
        line = int(inventory["contentsLine"])
        match = CONTENTS_ENTRY.fullmatch(contents[line - 1])
        require(match and match[1].replace("/", ".") == name,
                f"contents entry at line {line} does not name {name}")
        record["sourceTitle"] = match[3]
        record["upstreamCodeLines"] = int(match[2])
        record["labelEvidence"].insert(0, evidence(edition, files, "grh/CONTENTS.md", line, line))
    label, review = inventory["draftLabel"], inventory["labelReview"]
    require(label or record["sourceTitle"], f"missing label for {name}")
    require(review in ("draft", "reviewed") if label else not review, f"invalid review state for {name}")
    record.update(
        label=label or record["sourceTitle"],
        labelOrigin="AI-assisted Explorer wording" if label else "Upstream contents",
        labelReview=review if label else "upstream",
    )
    return record


def source_declarations(source):
    records = []
    for command in leansrc.parse(source)["cmds"]:
        if command.kind not in leansrc.DECL_KINDS or command.kind == "example":
            continue
        # Recover the spelling from the command header. The original parser's identifier
        # alphabet omits accented letters found in this edition and predates class abbrev.
        head = leansrc.strip_attrs(command.text)
        match = DECLARATION_HEADER.search(head.split("\n", 1)[0])
        if not match:
            continue
        name = match["name"]
        full = name.removeprefix("_root_.") if name.startswith("_root_.") else ".".join((*command.ns, name))
        prefix = len(command.text) - len(head)
        line = command.line + command.text.count("\n", 0, prefix + match.start())
        end = command.line + command.text.rstrip().count("\n")
        records.append({"name": full, "kind": command.kind, "line": line, "endLine": end})
    return records


def import_statements(source):
    for line, text in enumerate(leansrc.clean(source).splitlines(), 1):
        match = IMPORT.fullmatch(text.strip())
        if match:
            for module in match[1].split():
                require(leansrc.IDENT.fullmatch(module), f"unrecognized import on line {line}: {text}")
                yield module, line


def build_modules(edition, files, inventory, groups):
    contents = files["grh/CONTENTS.md"].decode().splitlines()
    modules = {}
    root = edition["sourceRoot"] + "/"
    lean_files = {path for path in files if path.startswith(root) and path.endswith(".lean")}
    require(len(inventory) == len(lean_files) and {row["path"] for row in inventory} == lean_files,
            "readable Git tree and tracked module inventory differ")
    require(len({row["module"] for row in inventory}) == len(inventory), "duplicate module name")
    upstream_entries = {line for line, text in enumerate(contents, 1) if CONTENTS_ENTRY.fullmatch(text)}
    catalogued = [int(row["contentsLine"]) for row in inventory if row["contentsLine"]]
    require(len(catalogued) == len(upstream_entries) and set(catalogued) == upstream_entries,
            "the upstream Contents entries do not resolve one-to-one")
    for row in sorted(inventory, key=lambda entry: entry["module"]):
        name, path, group = row["module"], row["path"], row["group"]
        relative = path.removeprefix(root)
        require(relative.removesuffix(".lean").replace("/", ".") == name,
                f"module name does not match Git path {path}")
        require(group == ".".join(name.split(".")[:2]) and group in groups,
                f"module {name} has unexpected group {group}")

        raw = files[path]
        source = raw.decode("utf-8")
        require(len(raw) == int(row["bytes"]) and hashlib.sha256(raw).hexdigest() == row["sha256"],
                f"pinned bytes fail inventory validation for {path}")
        lines = len(source.split("\n")) - source.endswith("\n")
        declarations = source_declarations(source)
        require(len({item["name"] for item in declarations}) == len(declarations)
                and all(1 <= item["line"] <= item["endLine"] <= lines for item in declarations),
                f"invalid declaration outline for {path}")
        modules[name] = {
            "name": name, "group": group, "groupSlug": groups[group]["slug"], "path": path,
            "href": f"/sernau/file/{quote(name)}",
            "raw": edition["rawBaseUrl"] + quote(relative),
            "upstreamRaw": f"https://raw.githubusercontent.com/lsernau/grh-lean/{edition['revision']}/{quote(path)}",
            "github": github(edition, path),
            "lines": lines,
            "bytes": len(raw), "sha256": row["sha256"],
            "imports": [], "importers": [], "externalImports": [],
            "declarations": declarations,
            **module_label(edition, files, row, contents),
        }

    grouped_evidence = defaultdict(list)
    mathlib = f"https://github.com/leanprover-community/mathlib4/blob/{edition['mathlibRevision']}/"
    for name, module in modules.items():
        seen = set()
        for target, line in import_statements(files[module["path"]].decode()):
            if target in seen:
                continue
            seen.add(target)
            edge = {
                "from": name, "to": target, "line": line,
                "href": f"{module['href']}#L{line}", "github": f"{module['github']}#L{line}",
            }
            if target not in modules:
                require(target.partition(".")[0] == "Mathlib", f"unknown external import: {target}")
                edge.update(external=True, targetGithub=mathlib + target.replace(".", "/") + ".lean")
                module["externalImports"].append(edge)
                continue
            module["imports"].append(edge)
            modules[target]["importers"].append(edge)
            target_group = modules[target]["group"]
            if module["group"] != target_group:
                grouped_evidence[module["group"], target_group].append(edge)
    return modules, grouped_evidence


def graph_routes(adjacency, start):
    routes = {start: [start]}
    todo = deque([start])
    while todo:
        node = todo.popleft()
        for target in adjacency[node]:
            if target not in routes:
                routes[target] = routes[node] + [target]
                todo.append(target)
    return routes


def graph_reach(adjacency, starting_nodes):
    seen = set(starting_nodes)
    todo = list(starting_nodes)
    while todo:
        for target in adjacency[todo.pop()]:
            if target not in seen:
                seen.add(target)
                todo.append(target)
    return len(seen) - len(starting_nodes)


def build_groups(edition, files, groups, modules, grouped_evidence):
    for id_, group in groups.items():
        provenance = group.pop("evidence")
        group.update(
            href=f"/sernau/group/{group['slug']}/",
            labelOrigin="AI-assisted Explorer wording",
            labelEvidence=[evidence(edition, files, provenance["path"], provenance["line"], provenance["endLine"])],
            modules=[], imports=[], importers=[],
        )
        require(id_ == group["id"], "group ID mismatch")

    grouped_edges = []
    for (source, target), references in sorted(grouped_evidence.items()):
        groups[source]["imports"].append(target)
        groups[target]["importers"].append(source)
        grouped_edges.append({"from": source, "to": target, "evidence": references})

    module_adj = {name: sorted(edge["to"] for edge in item["imports"]) for name, item in modules.items()}
    group_adj = {name: group["imports"] for name, group in groups.items()}
    routes = graph_routes(module_adj, "Main")
    group_routes = graph_routes(group_adj, "Main")
    require(len(routes) == len(modules), "a module lies outside Main's import closure")
    require(len(group_routes) == len(groups), "a group lies outside Main's import closure")
    for name, module in modules.items():
        groups[module["group"]]["modules"].append(name)
        module.update(depth=len(routes[name]) - 1, route=routes[name], reach=graph_reach(module_adj, [name]))
    for name, group in groups.items():
        group.update(
            depth=len(group_routes[name]) - 1,
            route=group_routes[name],
            moduleCount=len(group["modules"]),
            reach=graph_reach(module_adj, group["modules"]),
        )
    return grouped_edges


def build_theorems(edition, files, modules):
    inputs = json.loads((INPUTS / "theorems.json").read_text(encoding="utf-8"))
    names = [entry["name"] for entry in inputs]
    compact_root = edition["compact"]["sourceRoot"]
    readable_project = str(PurePosixPath(edition["sourceRoot"]).parent)
    compact_project = str(PurePosixPath(compact_root).parent)
    for project in (readable_project, compact_project):
        comparator = json.loads(files[f"{project}/comparator.json"])
        require(comparator["theorem_names"] == names, f"headline theorem list differs in {project}")
        require(files[f"{project}/lean-toolchain"].decode().strip() == edition["leanToolchain"],
                f"Lean toolchain pin differs in {project}")
        manifest = json.loads(files[f"{project}/lake-manifest.json"])
        mathlib_revision = next(package["rev"] for package in manifest["packages"] if package["name"] == "mathlib")
        require(mathlib_revision == edition["mathlibRevision"], f"Mathlib pin differs in {project}")

    readable_path = modules["Main"]["path"]
    compact_path = f"{compact_root}/Main.lean"
    readable_lines = files[readable_path].decode().splitlines()
    compact_lines = files[compact_path].decode().splitlines()
    require(files[f"{edition['sourceRoot']}/Statements.lean"] == files[f"{compact_root}/Statements.lean"],
            "readable and compact statement definitions differ")
    readable_declarations = {record["name"]: record for record in modules["Main"]["declarations"]}
    compact_declarations = {record["name"]: record for record in source_declarations(files[compact_path].decode())}
    require(set(readable_declarations) == set(compact_declarations) == set(names),
            "headline theorem names differ between the shorter editions")

    original = edition["original"]
    for entry in inputs:
        name = entry["name"]
        declaration = readable_declarations[name]
        readable_line = declaration["line"]
        compact_line = compact_declarations[name]["line"]
        head = f"theorem {name} : {entry['type']} :="
        require(readable_lines[readable_line - 1].startswith(head)
                and compact_lines[compact_line - 1].startswith(head),
                f"headline theorem statement does not match the crosswalk for {name}")

        fragment = "#" + quote(name)
        readable = {
            "module": "Main", "line": readable_line, "href": modules["Main"]["href"] + fragment,
            "github": github(edition, readable_path, readable_line),
        }
        original_line = entry.pop("originalLine")
        original_github = github(original, original["sourceRoot"] + "/Main.lean", original_line)
        compact_github = github(edition, compact_path, compact_line)
        entry.update(**readable, editions={
            "original": {
                "module": "Main", "line": original_line, "href": "/file/Main" + fragment,
                "github": original_github, "revision": original["revision"],
            },
            "sernau": {**readable, "revision": edition["revision"]},
            "compact": {
                "module": "Main", "line": compact_line, "href": compact_github,
                "github": compact_github, "revision": edition["revision"],
            },
        })
        body = "\n".join(readable_lines[readable_line - 1:declaration["endLine"]]).split(":=", 1)[1]
        for reference in entry["references"]:
            module = modules[reference["module"]]
            ref_name, ref_line = reference["name"], reference["line"]
            require(any(item["name"] == ref_name and item["line"] == ref_line
                        for item in module["declarations"]), f"unknown named reference {ref_name}")
            require(ref_name in leansrc.IDENT.findall(body), f"{name} does not name {ref_name} in its proof")
            reference.update(
                href=module["href"] + "#" + quote(ref_name),
                github=github(edition, module["path"], ref_line),
                evidence={"module": "Main", "line": readable_line, "github": readable["github"]},
            )
    return inputs


def build_sernau_data(out: Path):
    """Write edition-scoped reader data and return records for static page rendering."""
    out = Path(out)
    edition = json.loads((INPUTS / "edition.json").read_text(encoding="utf-8"))
    files = archive_inputs(edition)
    with (INPUTS / "modules.tsv").open(encoding="utf-8", newline="") as handle:
        inventory = list(csv.DictReader(handle, delimiter="\t"))
    group_inputs = json.loads((INPUTS / "groups.json").read_text(encoding="utf-8"))
    groups = {record["id"]: record for record in group_inputs}
    require(len(groups) == len(group_inputs) == len({group["slug"] for group in group_inputs}),
            "duplicate group IDs or slugs")

    digest = hashlib.sha256()
    input_files = ("edition.json", "groups.json", "modules.tsv", "theorems.json")
    for path in [Path(__file__), XREF / "leansrc.py", *(INPUTS / name for name in input_files)]:
        digest.update(path.name.encode() + b"\0" + path.read_bytes() + b"\0")
    build_id = digest.hexdigest()[:16]
    base = f"/data/sernau/{build_id}/"
    edition.update(
        buildId=build_id, manifestUrl="/data/sernau/manifest.json", overviewUrl=base + "overview.json",
        modulesUrl=base + "modules.json", groupsBaseUrl=base + "groups/",
        rawBaseUrl=f"/src/sernau/{edition['revision']}/", apiUrl="/api/sernau/index.json",
    )
    modules, grouped_evidence = build_modules(edition, files, inventory, groups)
    edges = build_groups(edition, files, groups, modules, grouped_evidence)
    theorems = build_theorems(edition, files, modules)
    group_depths = Counter(group["depth"] for group in groups.values())
    totals = {
        "modules": len(modules),
        "groups": len(groups),
        "moduleEdges": sum(len(module["imports"]) for module in modules.values()),
        "groupEdges": len(edges),
        "physicalLines": sum(module["lines"] for module in modules.values()),
        "bytes": sum(module["bytes"] for module in modules.values()),
        "maxModuleDepth": max(module["depth"] for module in modules.values()),
        "maxGroupDepth": max(group_depths),
        "groupDepthCounts": [group_depths[depth] for depth in range(max(group_depths) + 1)],
        "upstreamLabels": sum(bool(module["sourceTitle"]) for module in modules.values()),
        "draftOverrides": sum(module["labelReview"] == "draft" for module in modules.values()),
    }
    for key, value in edition.pop("expected").items():
        require(totals[key] == value, f"expected {value} for {key}, found {totals[key]}")

    documents = []
    for id_, label, path in DOCUMENTS:
        relative = "RELEASE.md" if id_ == "release" else path.removeprefix("grh/")
        url = edition["rawBaseUrl"] + quote(relative)
        binary_output(out, url, files[path])
        documents.append({"id": id_, "label": label, "path": path, "href": url, "github": github(edition, path)})
    for module in modules.values():
        binary_output(out, module["raw"], files[module["path"]])

    edition.update(totals=totals, documents=documents)
    for group in groups.values():
        group["dataUrl"] = edition["groupsBaseUrl"] + group["slug"] + ".json"
        json_output(out, group["dataUrl"], {
            "edition": edition, "group": group, "modules": {name: modules[name] for name in group["modules"]},
        })
    groups_list = list(groups.values())
    overview = {"edition": edition, "groups": groups_list, "edges": edges, "theorems": theorems, "documents": documents}
    large_fields = {"imports", "importers", "externalImports", "declarations", "route", "labelEvidence"}
    module_index = {
        "edition": edition,
        "modules": {
            key: {k: v for k, v in module.items() if k not in large_fields}
            for key, module in modules.items()
        },
    }
    json_output(out, edition["manifestUrl"], edition)
    json_output(out, edition["overviewUrl"], overview)
    json_output(out, edition["modulesUrl"], module_index)
    json_output(out, edition["apiUrl"], {
        "edition": edition,
        "groups": "/api/sernau/groups.json",
        "modules": "/api/sernau/modules.json",
        "theorems": "/api/sernau/theorems.json",
    })
    json_output(out, "/api/sernau/groups.json", {"edition": edition, "groups": groups_list, "edges": edges})
    json_output(out, "/api/sernau/modules.json", module_index)
    json_output(out, "/api/sernau/theorems.json", {"edition": edition, "theorems": theorems})
    return {**overview, "modules": modules}


if __name__ == "__main__":
    build_sernau_data(Path(sys.argv[1]))
