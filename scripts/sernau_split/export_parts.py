#!/usr/bin/env python3
"""Export the final research split and review records for the static site build."""

import argparse
from collections import Counter, defaultdict
import csv
import json
import os
from pathlib import Path
import re
from graphlib import TopologicalSorter

import analyze

CHAPTER_LABELS = (
    "Final\ntheorems", "Primes to\nzeros", "Data and\nCM field", "Heights",
    "Theorem A:\nshort forms", "Theorem B:\nenough forms",
    "Theorem C:\nintegral forms", "The twists",
)
CHAPTERS = dict(zip(("I", "II", "III", "IV", "V", "VI", "VII", "VIII"), CHAPTER_LABELS))
HANDOUT = ("https://github.com/nasqret/riemann-rev/blob/"
           "a2d6c1fa0400fd8b15271d4947a1299d07e4bd1f/writeup/handout.pdf")


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
    weights, entries, dependencies = Counter(), defaultdict(Counter), defaultdict(set)
    for left, targets in successors.items():
        for right in targets:
            source_part, target_part = assignment[left], assignment[right]
            if source_part != target_part:
                weights[source_part, target_part] += 1
                entries[target_part][right] += 1
                dependencies[source_part].add(target_part)
    heights = {}
    for part in TopologicalSorter({part: dependencies[part] for part in members}).static_order():
        heights[part] = 1 + max((heights[target] for target in dependencies[part]), default=-1)

    note_map = read_json(nk / "note_chapters.json")
    notes = {note["slug"]: {"title": note["title"], "chapter": note_map["chapter"][note["slug"]]}
             for note in read_json(nk / "MANIFEST.json")["notes"]}
    titles = {title.split(".")[0]: title for level, title, _ in read_json(nk / "toc.json")
              if level == 1 and re.match(r"[IVX]+\. ", title)}
    votes, base_votes = defaultdict(Counter), defaultdict(Counter)
    for row in rows(nk / "concordance_matches.tsv"):
        if row["in_unit"] == "True" and row["match"] in assignment:
            part = assignment[row["match"]]
            chapter = notes[row["note"]]["chapter"]
            votes[part][chapter] += 1
            base_votes[part.partition("#")[0]][chapter] += 1

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
        base, _, tag = part.partition("#")
        head = choose_head(names, successors, predecessors)
        doc, statement = analyze.split_decl(declarations[head]["module"], raw[head])
        note = tag if tag in notes else None
        chapter = notes[note]["chapter"] if note else None
        if not chapter:
            chapters = votes[part] or (base_votes[base] if tag else Counter())
            if chapters:
                chapter = chapters.most_common(1)[0][0]
        kind = {"·shared": "shared", "·top": "not attributed"}.get(tag)
        kind = kind or ("note" if note else "unsplit" if chapter else "not cited")
        if chapter:
            cloud = f"ch:{chapter}"
        else:
            cloud = "src:" + ".".join(declarations[head]["module"].split(".")[:2])
        ranked = sorted(entries[part], key=lambda name: (-entries[part][name], name))[:25]
        parts[part] = {
            "cloud": cloud, "kind": kind, "count": len(names), "height": heights[part],
            "head": {**declaration(head), "doc": doc[:600], "statement": statement[:1200]},
            "mostUsed": [{**declaration(name), "users": entries[part][name]} for name in ranked],
            **({"note": note} if note else {}),
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
        "handout": {"url": HANDOUT, "chapters": {chapter: {"title": titles[chapter], "label": label}
                                               for chapter, label in CHAPTERS.items()}, "notes": notes},
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
