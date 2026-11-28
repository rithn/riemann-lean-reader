---
title: "About this map of the Lean Riemann hypothesis proof"
description: "How the original and readable Lean maps were made, which revisions they show, their author credits and licences, and how to report a correction."
h1: "About this map"
path: /about/
target_queries:
  - riemann hypothesis lean proof map
  - riemann hypothesis lean explorer
as_of: "28 Nov 2026"
---

# About this map

*As of 28 Nov 2026.*

**RH Lean Explorer maps imports in two Lean editions of the Riemann hypothesis proof.** The original map covers the 20 November Alpöge–Claude archive. The readable map follows the source folders in Luke Sernau’s 25 November rewrite. [Original map](/alpoge/) · [Readable map](/sernau/) · [Verification status](/status/)

## Alpöge original {#alpoge-original}

- A reading guide to the Lean files: 2,647 clusters in 63 themes and 9 fields of mathematics. [The proof in numbers](/proof-in-numbers/) has the counts.
- Every cluster has its own page. It shows the cluster's name and description, its distance from the main theorem, what it builds on and what needs it, and links to the Lean files.
- The [route](/route/) shows how the proof is structured from the main theorem outwards. The [list view](/list/) shows every cluster as text, and the [learning path](/learn/) goes from the theorem down to school mathematics.
- [The core of the proof](/core/) covers 16 clusters in route order, with names checked against the full code.
- Lines on the map are imports. A line from cluster A to cluster B means some file in A imports a file in B. It is a formal dependency between files.
- The source viewer shows the original archive as released: commit [`40e56bab`](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005) of the community mirror.
- Every page has a Markdown copy (add `index.md` to its address). Data for machines is at [/api/](/api/), and `llms.txt` lists the pages.

## How the original map was made

1. **Clusters.** Files are grouped by the words in them and by their imports. This gives 2,647 clusters, 175,027 files in all.
2. **Names and descriptions.** Claude drafted each cluster's name and description from a sample of about one tenth of the cluster's files. Theme names were drafted from the clusters and folders in each theme.
3. **Tags.** Each cluster has a field, an era (the decade of the newest concept it needs) and a level (the highest maths level among its concepts). They are derived from the descriptions and concept tags, and they drive the map's colours and filters.
4. **Core check.** The names of the 16 core clusters were checked against the full Lean code. Of the 16, 14 needed a minor fix and 2 were wrong. The corrected titles are on the [core page](/core/).
5. **Distances.** Distance counts import steps from `Main.lean`.

## Sernau readable {#sernau-readable}

Sernau released the rewrite in his GitHub repository and credits his colleagues at Anthropic and Claude. The release credits Claude with writing the Lean code and upstream documentation. The Explorer uses the readable project’s `grh/src` at commit `72fead102f663d5c7a407964a13dc0cf9d977207`. [Release README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/README.md) · [Readable source tree](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src)

- The 29 groups follow the first two segments of the Lean module names, or the full module name when it has fewer segments. This follows the source folder structure. `Main` and `Statements` have their own groups.
- The 803 project modules contribute 1,733 direct imports between project files. Every module can be reached from `Main` by following imports. A group-to-group edge means at least one source file in the first group directly imports a source file in the second.
- The route follows specific imports and declarations in the readable edition. The upstream guide describes the background in `Lib/` and the argument in `New/`. [Readable source route](/sernau/route/) · [Pinned upstream guide](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md)
- Explorer wording for the 29 groups and 27 module labels was checked against the pinned guide or source. The other 776 module labels use the upstream wording. The label review covers how each name describes its source. [Independent proof checks](/status/#shorter-editions)
- The compact project has its own source and checks in the same repository. [Edition comparison](/shorter-riemann-hypothesis-proof/) · [Independent shorter-edition checks](https://math.mit.edu/~drew/shortgrh/)

## Sources and method

Each kind of fact on this site has one source. Pages link their sources.

- **The Lean files, their counts and their imports.** These come from the archive at commit [`40e56bab`](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005), the first commit of the community mirror (20 Nov 2026, 14:36 UTC). Its commit message reads "Mirror the submission exactly as published". We counted files, lines and import steps by script from the source and compared the totals with the community's [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md). [The proof in numbers](/proof-in-numbers/) gives the check for each figure.
- **What was certified.** This comes from the [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) on the Lean community blog (21 Nov 2026, 13:55 UTC). Quotes are copied from the page.
- **Which checks passed.** These come from [Sutherland's verification page](https://math.mit.edu/~drew/grh/) (MIT) and [Rubinstein's check](https://mrubinst.github.io/grh-lean-verification/) (Waterloo). Sutherland's page changes as his checks finish, so [status](/status/) gives the "last updated" time of the version it cites. The checks were run by Sutherland, Rubinstein and the other people named there.
- **What the proof's author says.** This comes from [Alpöge's note](https://alpo.ge/remark.pdf). The PDF text was read with PyMuPDF and quotes are copied from it.
- **Names, descriptions and tags of clusters and themes.** Claude drafted them from samples of the code, as described above. The names of the 16 core clusters were then checked against the full Lean code. All other names remain Claude's drafts.
- **News, dates and times.** Each item links to its source. Times are in UTC only where the source gives UTC.
- **How facts were checked.** Each claim in the fact sheet behind the pages was read in its cited source on 22 Nov 2026, and the checks on [status](/status/) were read again on 23 Nov 2026. The pages were written from that fact sheet.

## Who made it {#author}

![Soumya Sharma](/about/soumya-sharma.webp)

**Soumya Sharma** built and edits RH Lean Explorer.

Computer Science, IIT Delhi · MBA, IIM Ahmedabad · [Founder, Livo Assistant](https://livoassistant.com)

[X](https://x.com/SomTheBuilder) · [LinkedIn](https://www.linkedin.com/in/rithn) · [GitHub](https://github.com/rithn) · [Contact](#contact)

Soumya is not a number theorist: the maths on this site comes from the proof and its cited sources, and corrections are welcome.

Updates are posted on X by [@RiemannMap](https://x.com/RiemannMap). The [changelog](/changelog/) lists dated changes, with an RSS feed. The scripts and data are at [github.com/rithn/riemann-lean-reader](https://github.com/rithn/riemann-lean-reader).

## Licence

Everything this site made (page text, cluster and theme names and descriptions, the map layout, images and the JSON files) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The Lean source and upstream documentation keep their own licences. The readable source and guide are Apache 2.0, copyright Anthropic, PBC, with project-specific notice and attribution. [Apache licence](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/LICENSE) · [Readable notice](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/NOTICE) · [Upstream attribution](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/ATTRIBUTION.md)

## Corrections we've made

Dated changes that fixed something this site had wrong or unclear. The [changelog](/changelog/) lists every change.

- **22 Nov 2026. Core cluster names.** The names and descriptions of the 16 core clusters were checked against the Lean code at commit `40e56bab`. 14 needed a minor fix and 2 were wrong. k0250 was "Interlacing polynomials and transfer products" and is now "A concrete model transfer matrix: Yang-Baxter relation, frames and energy limit". k2395 was "Local Galois groups, completions and global Artin reciprocity" and is now "Local and global Galois groups of number fields and the Artin map". The 16 corrected titles are on the [core page](/core/).
- **22 Nov 2026. Files not on the map.** The 160 files in the archive but not on the map were recounted. An earlier version of this page gave 96 files that only list imports, 5 build helpers and 59 files with no readable statements. The recount gives 150 files that only list imports, 5 build helpers and 5 files with no theorem or definition. The total, 160, is the same.
- **22 Nov 2026. Theme names.** 20 themes whose names described only a small part of their content were renamed. The old addresses redirect.
- **22 Nov 2026. What "Builds on" and "Needed by" count.** Cluster panels now say that both count direct imports. The main theorem's line says it reaches every other cluster through chains of imports.

## For journalists {#for-journalists}

> **For journalists**
>
> **What the original map offers.** An interactive map of Alpöge’s 20 November Lean archive: 175,187 Lean files (175,027 on the map) in 2,647 clusters and 63 themes, about 17.4 million lines. It shows how the proof is structured: the main theorem's cluster, and how far each cluster is from it. [How the proof is structured](/route/) · [main theorem's cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/) · [browse the list](/list/) · [learning path](/learn/).
>
> **Numbers you can quote.** The longest import chain is 203 files. The median file is 13 imports from `Main`, and the farthest is 43. By import distance from the main-theorem cluster, the clusters fall into bands 0 to 8, with 1, 3, 22, 437, 1,443, 637, 76, 25 and 3 clusters. The 175,187 figure is for the submitted archive. The community repository has since removed most of those files: at its main commit [6866a9c6](https://github.com/leanprover-community/riemann-hypothesis/commit/6866a9c6260d77b88a7b5477433e3044b6844f9b) (24 Nov 2026, 13:39 UTC) it has 60,156 `.lean` files, 60,147 of them under `src/`. The count changes with every merge.
>
> **Free to use.** Everything we made, including data, page text, images and clips, is free to use under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit "RH Lean Explorer (riemannhypothesissolved.com)".
>
> **Contact.** [Soumya Sharma](/about/#author), who built the site: soumyasharma98 (at) gmail.com · X: [@RiemannMap](https://x.com/RiemannMap)
>
> **Wording we suggest.** "Certified" refers to the four formal criteria in the joint statement. The certification is a "joint statement by the Lean FRO and the Mathlib Initiative". Cluster names on the map were drafted by AI. For claims about the proof, cite the primary sources.

## Contact and corrections {#contact}

- Email Soumya Sharma at soumyasharma98 (at) gmail.com for press, teaching, collaboration or anything else. On X: [@SomTheBuilder](https://x.com/SomTheBuilder).
- On any cluster page, "Report a wrong name" opens an X post to @SomTheBuilder with the cluster id and address filled in.
- Post corrections to [@SomTheBuilder](https://x.com/SomTheBuilder) on X. For a readable-map correction, include the edition and the map or source URL, plus the Lean declaration or group if applicable.

## AI disclosure

- Claude, Anthropic's AI model, drafted the names and descriptions of all 2,647 clusters, the 63 theme names, the field, era and level tags, and the first drafts of the text on this site.
- The proof itself was found by Levent Alpöge working with Claude. His note says so. ([note](https://alpo.ge/remark.pdf))
- Cluster names and descriptions can be wrong. The 16 core names were checked by reading the Lean code.

For the proof's status, checks and certification, see [status](/status/). Outside guides to the proof are listed on [guides](/guides/).
