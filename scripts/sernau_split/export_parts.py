#!/usr/bin/env python3
"""Export the final research split and review records for the static site build."""

import argparse
from collections import Counter, defaultdict
import csv
import json
import os
from pathlib import Path

import analyze

def rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        yield from csv.DictReader(stream, delimiter="\t")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def choose_head(members, successors, predecessors):
    pool = set(members)
    candidates = ([name for name in members if not predecessors[name] & pool]
                  if len(pool) < 900 else members)

    def score(name):
        stack, reached = [name], set()
        while stack:
            current = stack.pop()
            if current not in reached:
                reached.add(current)
                stack.extend(successors[current] & pool)
        return len(reached), -len(name)

    return max((candidates or members)[:200], key=score)


def export(research, source, output):
    analyze.SRC = os.fspath(source)
    data = research / "data"
    nk = data / "naskrecki"
    assignment = {r["declaration"]: r["part"] for r in rows(data / "parts_N_naskrecki_upset_coarse_min5.tsv")}
    declarations = {r["name"]: r for r in rows(data / "declarations.tsv") if r["name"] in assignment}
    members = defaultdict(list)
    for name, part in assignment.items():
        members[part].append(name)

    successors, predecessors = defaultdict(set), defaultdict(set)
    for row in rows(data / "edges.tsv"):
        left, right = row["source"], row["target"]
        if left != right and left in assignment and right in assignment:
            successors[left].add(right)
            predecessors[right].add(left)
    weights, entries = Counter(), defaultdict(Counter)
    for left, targets in successors.items():
        for right in targets:
            source_part, target_part = assignment[left], assignment[right]
            if source_part != target_part:
                weights[source_part, target_part] += 1
                entries[target_part][right] += 1

    labels = {}
    for path in [research / "labels_final" / "labels.jsonl"]:
        for line in path.read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            part = record["id"]
            if part in labels:
                raise ValueError(f"Duplicate review record for {part}")
            labels[part] = {
                "label": record["label"], "description": record["description"],
                "evidence": [[item["quote"], item["link"]] for item in record["evidence"][:4]],
                **({"flag": True} if record["verdict"] == "flag" else {}),
            }
    if labels.keys() != members.keys():
        raise ValueError(f"Missing or extra review records: {labels.keys() ^ members.keys()}")

    raw = {}
    with (data / "raw" / "decls.jsonl").open(encoding="utf-8") as stream:
        for line in stream:
            record = json.loads(line)
            if record["n"] in declarations:
                raw[record["n"]] = record["r"]

    def declaration(name):
        record = declarations[name]
        return {"name": name, "module": record["module"], "line": raw[name][4]}

    parts = {}
    for part, names in sorted(members.items()):
        head = choose_head(names, successors, predecessors)
        doc, statement = analyze.split_decl(declarations[head]["module"], raw[head])
        files = defaultdict(list)
        for name in sorted(names):
            files[declarations[name]["module"]].append(name)
        ranked = sorted(entries[part], key=lambda name: (-entries[part][name], name))[:25]
        parts[part] = {
            "count": len(names), "files": dict(sorted(files.items())),
            "head": {**declaration(head), "doc": doc[:600], "statement": statement[:1200]},
            "mostUsed": [{**declaration(name), "users": entries[part][name]} for name in ranked],
            **({"final": True} if "riemannHypothesis" in names else {}),
        }

    summary = read_json(nk / "refine_summary.json")["upset_coarse_min5"]
    if (len(parts), len(weights), sum(weights.values())) != (
        summary["parts"], summary["part_edges"], summary["cross_decl_edges"]
    ):
        raise ValueError("Exported graph counts differ from the final research split")
    indices = {part: index for index, part in enumerate(parts)}
    output.mkdir(parents=True, exist_ok=True)
    for name, payload in {
        "parts": parts,
        "edges": [[indices[source], indices[target], weight] for (source, target), weight in sorted(weights.items())],
        "labels": dict(sorted(labels.items())),
    }.items():
        (output / f"{name}.json").write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("research", type=Path)
    parser.add_argument("source", type=Path, help="Pinned readable source, at the directory containing Main.lean")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    export(args.research, args.source, args.output)
