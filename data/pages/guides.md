---
title: "Guides to the Lean proof of the Riemann hypothesis"
description: "Outside guides to Alpöge's Lean proof of the Riemann hypothesis. Who checked it, who explains it, with author, date and what each one covers."
h1: "Guides to the Lean proof of the Riemann hypothesis"
path: /guides/
target_queries:
  - riemann hypothesis proof explained
  - alpöge riemann hypothesis proof guide
  - riemann hypothesis lean proof explained
  - riemann hypothesis lean proof blueprint
  - who verified the riemann hypothesis proof
  - riemann hypothesis lean proof reading guide
as_of: "23 Nov 2026"
---

# Guides to the Lean proof of the Riemann hypothesis

*As of 23 Nov 2026. We read each page on this list on 23 Nov.*

**This page lists guides and checks written by other people about Levent Alpöge's Lean proof of the Riemann hypothesis. A guide is listed when its author is named, the page is public and it is about this proof. For each one we say whether the author checked the proof or only explains it. Listing a guide does not mean we have checked its mathematics.** For what was checked and by whom, see [status](/status/).

## Authors who checked the proof

These authors ran checks of the Lean proof themselves, or certify them.

- **Michael Rubinstein (University of Waterloo).** [The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) ([PDF](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf)). Version 2, 22 Nov 2026. A guide to the zeta case only, from the strategy to step-by-step checks. The page also lists his own four checks of the Lean proof, which finished with no errors, and the checks of others.
- **Andrew Sutherland (MIT).** [Verification files for the Lean proof of the Riemann Hypothesis](https://math.mit.edu/~drew/grh/). Last updated 22 Nov 2026. Compile, axiom and kernel checks for all moduli and all characters. It explains no mathematics. At its last update some later stages were still running.
- **Lean FRO and Mathlib Initiative.** [Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/). 21 Nov 2026. The joint statement that certifies the proof, with the four criteria it checked: the statement, the compile, the match between the statement and the theorem, and the proof checkers.
- **Michael Rubinstein (University of Waterloo).** [GRH Lean Check](https://mrubinst.github.io/grh-lean-verification/). 21 Nov 2026. The log of his checks, with scripts: source hash, static audit, compile, axioms, kernel replay and nanoda. The page has no byline and links to his page. It explains no mathematics.

## Guides that explain the proof

These authors explain or map the proof. None of them ran a check of the full archive.

- **Manvir Jaswal (independent researcher, Toronto).** [The Riemann hypothesis for Dirichlet L-functions [after Levent Alpöge]](https://zenodo.org/records/24410057). 21 Nov 2026, with a second version on 22 Nov. A preprint under CC BY 4.0. It states the five theorems of `Main.lean` in ordinary notation, then the reduction to an inequality that excludes zeros right of 1/2, the analytic argument and the bound for Tate twists.
- **Jimmie Adriazola (Arizona State University).** [An End-to-End Reconstruction of the Alpöge–Claude Route to the Riemann Hypothesis](https://github.com/jimjamzola/RH-Alpoge-Reconstruction). 22 Nov 2026. A 66-page manuscript and repository under CC BY 4.0. It rebuilds the proof in conventional mathematics, with a dependency map and a list of the external theorems. The author says it is incomplete.
- **Bartosz Naskręcki.** [The announced proof of the Riemann hypothesis: map, guide and record of checks](https://nasqret.github.io/riemann-rev/) ([repository](https://github.com/nasqret/riemann-rev)). 21 Nov 2026. The site names no person. The repository belongs to the GitHub account nasqret, whose profile reads Bartosz Naskręcki. It gives the route in 7 steps, an atlas of 14 components and 107 declarations, and a record of who checked what.
- **chrisflav (GitHub).** [riemann-blueprint](https://github.com/chrisflav/riemann-blueprint). 21 Nov 2026. A reading blueprint in 4 chapters. It gives the five main theorems, the reduction to "no L-function vanishes for Re s > 1/2", an outline, the shared foundations and the published results used. The repository gives no name.
- **tamnd (GitHub).** [A written proof of the Lean proof of the Riemann Hypothesis](https://riemann.tamnd.com). 21 Nov 2026. A site with four levels, from the proof on one page to one Lean declaration, and about 50 steps. The site names no author. It was written before the 21 Nov certification.
- **John Baez.** [Masullo on the Riemann Hypothesis](https://johncarlosbaez.wordpress.com/2026/11/22/masullo-on-the-riemann-hypothesis/). 22 Nov 2026. A blog post that is mostly about another claim. It gives a one-line sketch of the strategy and links to the guides by Rubinstein and Adriazola.
- **Scott Aaronson.** [The stochastic parrots have apparently proved the Riemann Hypothesis](https://scottaaronson.blog/?p=10344). 20 Nov 2026, with an update on 21 Nov. A blog post on trust and verification, not on the mathematics. It reports checks made by others.

## Other tools

- **riemann.world.** [riemann.world](https://riemann.world/) is a zoomable map of the same Lean files, with their declarations and source. The site does not state its author.

## Suggest a guide

Post to [@SomTheBuilder](https://x.com/SomTheBuilder) on X with the link. We add guides that meet the bar above. Authors can ask us to correct how their guide is described.

## Changelog

- **23 Nov 2026.** First version, with 11 guides.
