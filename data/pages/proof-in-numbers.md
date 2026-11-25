---
title: "The Lean proof of the Riemann hypothesis in numbers"
description: "175,187 Lean files, 17.4 million lines, 2,647 clusters, 43 steps from the main theorem, 203-module longest chain: every figure of the proof, with sources."
h1: "The proof in numbers"
path: /proof-in-numbers/
target_queries:
  - riemann hypothesis lean proof size
  - riemann hypothesis proof length
  - how long is the riemann hypothesis proof
  - riemann hypothesis lean proof lines of code
  - lean proof structure riemann hypothesis
as_of: "24 Nov 2026"
---

# The proof in numbers

*As of 24 Nov 2026. The figures for size come from the released archive (commit [`40e56bab`](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005)). The shape figures come from this map's data and were recomputed from the Lean source.*

**The proof is 175,187 Lean files and about 17.4 million lines. The map groups 175,027 of the files into 2,647 clusters and 63 themes. The median file is 13 import steps from `Main.lean`, the farthest is 43, and the longest import chain is 203 modules.**

## Size

- **175,187 Lean files.** This is the archive Levent Alpöge released on 20 Nov 2026, and the number of modules in the full compile check. ([verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- **17,374,215 lines, about 17.4 million.** Of these, 15,531,759 are non-blank. Mathlib, which the proof builds on, is about 2 million lines. ([verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md), [Rubinstein](https://mrubinst.github.io/grh-lean-verification/))
- **1,030,531,854 bytes of source.** About 1 GB of text, which is what a reader or a checker has to take in. ([verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- **818,755 theorems and lemmas, and 242,067 definitions, abbreviations, structures, classes, instances and inductive types.** These are the statements the files contain. ([verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- **175,027 files on the map.** The map covers every file that has a theorem or definition of its own. The other 160 are 150 files that only list imports, the 5 build helpers `BuildAid.D1` to `D5`, and 5 files with no theorem or definition (only `open`, `section`, `namespace` or `set_option` lines).
- **14 parts, 239,275,554 bytes.** This is the size of the joined archive as posted. ([Sutherland](https://math.mit.edu/~drew/grh/))

### How much has the community version shrunk?

The Lean community removes unused files and simplifies the code on the `main` branch of its [Riemann hypothesis repository](https://github.com/leanprover-community/riemann-hypothesis). At [commit 6866a9c6](https://github.com/leanprover-community/riemann-hypothesis/commit/6866a9c6260d77b88a7b5477433e3044b6844f9b) on 24 Nov 2026 at 13:39 UTC, it had 60,156 Lean files, compared with 175,187 in the original release.

Follow [RH Shrink’s live proof-size tracker](https://rh-shrink.github.io/) to see how the file and line counts change with each commit. Its code-line measure excludes blank lines, comment-only lines and the import block at the top of each file. The [tracker’s source code](https://github.com/rh-shrink/rh-shrink.github.io) measures the text directly. For checks that run Lean on the proof, see [how the proof was verified](/how-we-know/).

## Shape

- **2,647 clusters.** The map groups files by the words in them and by their imports. This is the unit of the map: each cluster has its own page.
- **63 themes.** A theme groups clusters on one topic, so a reader can browse by subject.
- **9 fields of mathematics.** Each theme belongs to one field. The shares are in the table below.
- **13 import steps: the median file.** Distance is the number of import steps from `Main.lean`. Half the files are 13 steps or fewer from the main theorem.
- **43 import steps: the farthest file.** Every file is reached from `Main.lean`, and the farthest needs 43 steps.
- **203 modules: the longest import chain.** The longest chain from `Main.lean` through imports passes through 203 modules. ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))

### Clusters by distance from the main theorem

Distance counts import steps between clusters, starting at the cluster that holds `Main.lean`.

| Distance | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Clusters | 1 | 3 | 22 | 437 | 1,443 | 637 | 76 | 25 | 3 |

The three clusters at distance 1 are the ones `Main.lean`'s own cluster imports directly: [zero-free region](/cluster/k0680-zero-free-region-for-zeta-and-dirichlet-l-functions/), [primes in progressions](/cluster/k0683-primes-in-progressions-siegel-walfisz-and-exceptional-zero/) and [Mertens-type estimates](/cluster/k0694-mertens-type-estimates-and-zero-sums-for-dirichlet-l/). Most of the proof, 1,443 clusters, sits four steps out. See [how the proof is structured](/route/).

### Files by field

Share of the 175,027 mapped files, by the field of the file's theme.

| Field | Themes | Clusters | Files | Share |
|---|---|---|---|---|
| Automorphic forms | 11 | 552 | 36,120 | 20.6% |
| Abelian varieties | 9 | 484 | 34,614 | 19.8% |
| Theta & Siegel–Weil | 11 | 353 | 26,433 | 15.1% |
| Heights & Arakelov | 9 | 361 | 22,273 | 12.7% |
| Lattices & mass | 6 | 293 | 16,495 | 9.4% |
| p-adic Hodge theory | 6 | 229 | 16,172 | 9.2% |
| Harmonic analysis | 3 | 140 | 9,315 | 5.3% |
| Algebraic geometry | 6 | 139 | 7,941 | 4.5% |
| Classical number theory | 2 | 96 | 5,664 | 3.2% |

The largest field, automorphic forms, holds 20.6% of the files (36,120 of 175,027), just over a fifth; no other field holds more than 19.8%. Classical number theory holds the main theorem and all four clusters within one step of it, and 3.2% of the files.

## Age and level of the mathematics

Each cluster has an era (the decade of the newest concept it needs) and a level (the highest maths level among its concepts). Both are editorial tags derived from the cluster descriptions and concept tags, and the map shows them as filters. They can be wrong.

| Era | Clusters | Share |
|---|---|---|
| Before 1900 | 127 | 4.8% |
| 1900–1949 | 630 | 23.8% |
| 1950s | 238 | 9.0% |
| 1960s | 888 | 33.5% |
| 1970s | 419 | 15.8% |
| 1980s | 237 | 9.0% |
| 1990s | 75 | 2.8% |
| 2000s | 14 | 0.5% |
| 2010s | 16 | 0.6% |
| 2020s | 3 | 0.1% |

The largest group, 888 clusters, needs mathematics from the 1960s. The four clusters nearest the main theorem date from 1895 to 1937.

| Level | Clusters | Share |
|---|---|---|
| School | 1 | under 0.1% |
| Undergraduate | 114 | 4.3% |
| Graduate | 846 | 32.0% |
| PhD | 1,666 | 62.9% |
| Research | 20 | 0.8% |

Nearly two thirds of the clusters (62.9%) need PhD-level mathematics.

**66 clusters are new in this proof (2.5%).** They rest on the proof's own named constructions rather than on published mathematics. They sit in 11 themes.

## How it was checked

- **175,187 of 175,187 modules compile with zero errors.** Sutherland (MIT) and Rubinstein (Waterloo) each ran a full compile, on Lean v4.33.1 and Mathlib v4.33.1. Dozens of people reported the same result and the same proof export. ([Sutherland](https://math.mit.edu/~drew/grh/), [Rubinstein](https://mrubinst.github.io/grh-lean-verification/), [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))
- **3 h 18 min, against about 17 hours.** Rubinstein's distributed compile took 3 h 18 min on university servers. A plain `lake build` pointed to a finish in roughly 17 hours. This is the cost of reproducing the first check. ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))
- **61,570,595,788 bytes: the exported proof.** Unpacked, it is 61.6 GB (7,699,933,588 bytes compressed). The independent checkers read this export. The smaller challenge export, which isolates the statement, is 350,862,970 bytes. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **1,468,418 declarations accepted by con-leche, 1,484,729 by nanoda.** The two figures come from different checkers. Rubinstein gives a third, 1,478,198, for the dependency closure of the main theorem, and notes that many statements in the files are parallel or earlier formulations the theorem never uses. ([Sutherland](https://math.mit.edu/~drew/grh/), [Rubinstein](https://mrubinst.github.io/grh-lean-verification/))
- **5 checkers have accepted the proof.** They are Lean's own kernel (`leanchecker`, which replayed all 175,187 of 175,187 modules and, on 22 and 23 Nov, accepted the full export in its default and paranoid modes), nanoda (a kernel written in Rust), con-leche, con-ron and lean4lean. con-leche and con-ron come with a formal proof that they cannot accept a false proof. ([Sutherland](https://math.mit.edu/~drew/grh/), [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))
- **3 axioms.** The five main theorems depend only on `propext`, `Classical.choice` and `Quot.sound`. The environment holds 15 axioms, all in Lean core. This keeps the logical base to the standard one. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **5 theorems in `Main.lean`.** Two formulations of the classical Riemann hypothesis and three statements about Dirichlet L-functions. ([pinned `Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean), [Sutherland](https://math.mit.edu/~drew/grh/))

Sutherland's page keeps the live list of checks. See [status](/status/) for who checked what and [how we know](/how-we-know/) for what each check shows.

## See it in the map

[The core of the proof](/core/) covers the 16 clusters nearest the main theorem. [The route](/route/) shows every distance ring. You can also [browse every cluster as a list](/list/).
