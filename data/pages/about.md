---
title: "About this map of the Lean Riemann hypothesis proof"
description: "What the map is, how its clusters and names were made, who made it, the licence (CC BY 4.0), how to report a wrong name, and where AI was used."
h1: "About this map"
path: /about/
target_queries:
  - riemann hypothesis lean proof map
  - riemann hypothesis lean explorer
as_of: "23 Nov 2026"
---

# About this map

*As of 23 Nov 2026.*

**riemannhypothesissolved.com is an interactive map of the Lean proof of the Riemann hypothesis released by Levent Alpöge on 20 Nov 2026. It groups the proof's 175,187 Lean files into clusters and themes, names them in plain English, and shows how they depend on each other.** For what was checked and by whom, see [status](/status/).

## What the map is

- A reading guide to the Lean files: 2,647 clusters in 63 themes and 9 fields of mathematics. [The proof in numbers](/proof-in-numbers/) has the counts.
- Every cluster has its own page. It shows the cluster's name and description, its distance from the main theorem, what it builds on and what needs it, and links to the Lean files.
- The [route](/route/) shows how the proof is structured from the main theorem outwards. The [list view](/list/) shows every cluster as text, and the [learning path](/learn/) goes from the theorem down to school mathematics.
- [The core of the proof](/core/) covers 16 clusters in route order, with names checked against the full code.
- Lines on the map are imports. A line from cluster A to cluster B means some file in A imports a file in B. It is a formal dependency between files.
- The source viewer shows the original archive as released: commit [`40e56bab`](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005) of the community mirror.
- Every page has a Markdown copy (add `index.md` to its address). Data for machines is at [/api/](/api/), and `llms.txt` lists the pages.

## How it was made

1. **Clusters.** Files are grouped by the words in them and by their imports. This gives 2,647 clusters, 175,027 files in all.
2. **Names and descriptions.** Claude drafted each cluster's name and description from a sample of about one tenth of the cluster's files. Theme names were drafted from the clusters and folders in each theme.
3. **Tags.** Each cluster has a field, an era (the decade of the newest concept it needs) and a level (the highest maths level among its concepts). They are derived from the descriptions and concept tags, and they drive the map's colours and filters.
4. **Core check.** The names of the 16 core clusters were checked against the full Lean code. Of the 16, 14 needed a minor fix and 2 were wrong. The corrected titles are on the [core page](/core/).
5. **Distances.** Distance counts import steps from `Main.lean`.

## Sources and method

Each kind of fact on this site has one source. Pages link their sources.

- **The Lean files, their counts and their imports.** These come from the archive at commit [`40e56bab`](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005), the first commit of the community mirror (20 Nov 2026, 14:36 UTC). Its commit message reads "Mirror the submission exactly as published". We counted files, lines and import steps by script from the source and compared the totals with the community's [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md). [The proof in numbers](/proof-in-numbers/) gives the check for each figure.
- **What was certified.** This comes from the [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) on the Lean community blog (21 Nov 2026, 13:55 UTC). Quotes are copied from the page.
- **Which checks passed.** These come from [Sutherland's verification page](https://math.mit.edu/~drew/grh/) (MIT) and [Rubinstein's check](https://mrubinst.github.io/grh-lean-verification/) (Waterloo). Sutherland's page changes as his checks finish, so [status](/status/) gives the "last updated" time of the version it cites. The checks were run by Sutherland, Rubinstein and the other people named there.
- **What the proof's author says.** This comes from [Alpöge's note](https://alpo.ge/remark.pdf). The PDF text was read with PyMuPDF and quotes are copied from it.
- **Names, descriptions and tags of clusters and themes.** Claude drafted them from samples of the code, as described above. The names of the 16 core clusters were then checked against the full Lean code. All other names remain Claude's drafts.
- **News, dates and times.** Each item links to its source. Times are in UTC only where the source gives UTC.
- **How facts were checked.** Each claim in the fact sheet behind the pages was read in its cited source on 22 Nov 2026, and the checks on [status](/status/) were read again on 23 Nov 2026. The pages were written from that fact sheet.

## Who made it

Made by Soumya Sharma ([@SomTheBuilder](https://x.com/SomTheBuilder)). Soumya studied computer science at IIT Delhi and is a founder of Livo Assistant, which builds AI systems that check documents against their sources. Soumya is not a number theorist: the maths on this site comes from the proof and its cited sources, and corrections are welcome.

Updates are posted on X by [@RiemannMap](https://x.com/RiemannMap). The [changelog](/changelog/) lists dated changes, with an RSS feed. The scripts and data are at [github.com/rithn/riemann-lean-reader](https://github.com/rithn/riemann-lean-reader).

## Licence

Everything this site made (page text, cluster and theme names and descriptions, the map layout, images and the JSON files) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The Lean source keeps its own licence.

## Corrections we've made

Dated changes that fixed something this site had wrong or unclear. The [changelog](/changelog/) lists every change.

- **22 Nov 2026. Core cluster names.** The names and descriptions of the 16 core clusters were checked against the Lean code at commit `40e56bab`. 14 needed a minor fix and 2 were wrong. k0250 was "Interlacing polynomials and transfer products" and is now "A concrete model transfer matrix: Yang-Baxter relation, frames and energy limit". k2395 was "Local Galois groups, completions and global Artin reciprocity" and is now "Local and global Galois groups of number fields and the Artin map". The 16 corrected titles are on the [core page](/core/).
- **22 Nov 2026. Files not on the map.** The 160 files in the archive but not on the map were recounted. An earlier version of this page gave 96 files that only list imports, 5 build helpers and 59 files with no readable statements. The recount gives 150 files that only list imports, 5 build helpers and 5 files with no theorem or definition. The total, 160, is the same.
- **22 Nov 2026. Theme names.** 20 themes whose names described only a small part of their content were renamed. The old addresses redirect.
- **22 Nov 2026. What "Builds on" and "Needed by" count.** Cluster panels now say that both count direct imports. The main theorem's line says it reaches every other cluster through chains of imports.

## Report a wrong name or a correction

- On any cluster page, "Report a wrong name" opens an X post to @SomTheBuilder with the cluster id and address filled in.
- For anything else, post to [@SomTheBuilder](https://x.com/SomTheBuilder) on X.

## AI disclosure

- Claude, Anthropic's AI model, drafted the names and descriptions of all 2,647 clusters, the 63 theme names, the field, era and level tags, and the first drafts of the text on this site.
- The proof itself was found by Levent Alpöge working with Claude. His note says so. ([note](https://alpo.ge/remark.pdf))
- Cluster names and descriptions can be wrong. The 16 core names were checked by reading the Lean code.

For the proof's status, checks and certification, see [status](/status/). Outside guides to the proof are listed on [guides](/guides/).
