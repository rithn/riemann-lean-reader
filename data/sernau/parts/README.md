# Readable proof parts

The graph comes from a text resolver that looks up declaration names in statements
and proofs. Its edges are approximate, derived from reading the source text. Lean was not built to extract this graph.
Each edge counts distinct declaration-to-declaration uses between its two parts.

The graph starts with the research mini-clusters in the dependency cone of the
five main theorems. In mini-clusters cited by more than one chapter, matched
declarations from each note's own unit are seeds. A declaration inherits the
notes whose seeds reach it along dependencies within the mini-cluster. A single
note gets its own part, multiple notes share a part, and unreached declarations
form the unattributed part. Single-note parts of fewer than five declarations
join the shared part. The resulting part graph is acyclic.

Grouping is based on Naskręcki's handout of the compact edition, edition 11,
[nasqret/riemann-rev at a2d6c1fa](https://github.com/nasqret/riemann-rev/tree/a2d6c1fa0400fd8b15271d4947a1299d07e4bd1f/writeup).
Chapter and note titles are quoted from the handout; its text is licensed under 0BSD. Citations were matched by name first, then by a model-checked statement match (Codex Sol), reaching 88% coverage. English part labels and descriptions are AI-written: drafted by Codex Terra and checked by Codex Sol. They have not been
reviewed by a person. The final review flags parts that mix topics.

From the generator checkout, export again using the final research inputs
(including the resolver's `data/raw/decls.jsonl` and the final labels)
and the pinned readable source directory containing `Main.lean`:

```sh
uv run --no-project python scripts/sernau_split/export_parts.py \
  ../research/plans/sernau-split ../site-parts/src/sernau/72fead102f663d5c7a407964a13dc0cf9d977207 \
  data/sernau/parts
```

The other scripts in that directory reproduce the source resolution, initial
partition and split in order (`resolve.py`, `analyze.py`, `refine_naskrecki.py`).
Set `SERNAU_SPLIT_SOURCE` to the pinned source directory and `SERNAU_SPLIT_DATA`
to a scratch copy of the research data with its concordance. Use the reviewed
partition and final labels together when exporting. The site build reads the
four checked-in JSON files directly.
