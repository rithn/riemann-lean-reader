---
title: "Has the Riemann hypothesis been solved? Status 22 Nov 2026"
description: "A Lean proof of the Riemann hypothesis was released on 20 Nov 2026 and certified on 21 Nov. What was checked, by whom, and what it covers."
h1: "Has the Riemann hypothesis been solved?"
path: /status/
target_queries:
  - is the riemann hypothesis solved
  - has the riemann hypothesis been solved yet
  - riemann hypothesis status
  - riemann hypothesis update latest
  - riemann hypothesis solved confirmed
  - riemann hypothesis lean proof verified
as_of: "23 Nov 2026"
---

# Has the Riemann hypothesis been solved?

*Status as of 23 Nov 2026. This page is updated as news arrives. See the changelog at the end.*

**Levent Alpöge released a Lean proof of the Riemann hypothesis on 20 Nov 2026. On 21 Nov the Lean FRO and the Mathlib Initiative certified that the statement and the proof of the Riemann hypothesis are correct. Independent checkers have compiled all 175,187 modules, replayed the proof through Lean's kernel and checked the exported proof with several independent programs.**

## What was released

- On 20 Nov 2026 Levent Alpöge posted a four-page note and a 14-part archive of Lean files on his personal website. ([note](https://alpo.ge/remark.pdf))
- The archive holds 175,187 Lean files and about 17.4 million lines (17,374,215). ([verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- It is a Lean library that proves five theorems in its `Main.lean` file. The first is Mathlib's own statement of the Riemann hypothesis. The other four concern Dirichlet L-functions. ([Sutherland](https://math.mit.edu/~drew/grh/))
- The proof covers the Riemann hypothesis and the generalised Riemann hypothesis for Dirichlet L-functions, for all moduli and all characters. The theorems are stated without hypotheses. ([Sutherland](https://math.mit.edu/~drew/grh/), [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- Alpöge released the proof as Lean code. He wrote "I decided to only present Lean" and says he intends "to write it properly" later. ([note](https://alpo.ge/remark.pdf))
- Alpöge is a mathematician at Anthropic and a junior fellow of the Harvard Society of Fellows. ([his site](https://alpo.ge/))
- In his note Alpöge writes: "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis." ([note](https://alpo.ge/remark.pdf))

## What was verified

All 175,187 modules compile with zero errors. Every module has been replayed through Lean's kernel, and the exported proof has been accepted by nanoda, con-leche and con-ron. lean4lean accepts every module. A sandboxed rebuild on a separate machine produced an export identical to the published one.

| Check | Who | Result |
|---|---|---|
| Full compile of all 175,187 modules | Andrew Sutherland (MIT); Michael Rubinstein (Waterloo) | 175,187 of 175,187 compiled, zero errors (Lean v4.33.1, Mathlib v4.33.1) |
| Mathlib files against the official cache | Sutherland | 8,322 Mathlib and 378 dependency `.olean` files identical byte for byte |
| Rebuild in a sandbox with no network, on a separate machine | Sutherland | Build passes; the proof export made in the sandbox is identical to the published one |
| Replay of every module through Lean's kernel (`leanchecker`) | Sutherland; Rubinstein | 175,187 of 175,187 accepted |
| Full export checked by nanoda, an independent kernel written in Rust | Sutherland; Rubinstein | Accepted; Rubinstein reports 1,484,729 declarations checked |
| Full export checked by con-leche | Sutherland | 1,468,418 declarations accepted in `--verified` mode |
| Statement comparison (`--compare`) with con-leche and con-ron | Sutherland | All five theorems accepted as justified by the solution |
| End-to-end `lake comparator` run (Lean v4.36.0) | Sutherland | Statement comparison and axiom check passed in one run; the Lean kernel stage on the export is still running |
| Lean default and paranoid kernels on the export | Sutherland | Running, no verdict yet. Lean's kernel has already accepted every module from the compiled files (`leanchecker`, above) |
| Module-by-module check with lean4lean | Sutherland | 175,187 of 175,187 accepted |
| Axiom check | Sutherland | Only `propext`, `Classical.choice`, `Quot.sound` |

Sources: [Sutherland's verification page](https://math.mit.edu/~drew/grh/), last updated 22 Nov 2026 at 16:20 UTC (read on 23 Nov), and [Rubinstein's check](https://mrubinst.github.io/grh-lean-verification/), where all four of his checks finished on 21 Nov. Sutherland's page keeps the full, live list. At 16:20 UTC it lists two checks as still running: the end-to-end `lake comparator` run and the Lean default and paranoid kernels on the export. For the `lake comparator` run it says the statement comparison and axiom check "already passed in one run". Both ran their checks with Claude Code. [Elliot Arledge](https://github.com/Infatoshi/rh-verification-receipts) and [Bartosz Naskręcki](https://nasqret.github.io/riemann-rev/) have published their own results.

## What was certified, and by whom

On 21 Nov 2026 at 13:55 UTC the Lean community blog published a joint statement by the Lean FRO and the Mathlib Initiative. ([statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))

On 23 Nov 2026 the statement's byline was changed to "Joint statement by the Lean FRO and the Mathlib Initiative." It first read "Joint statement by the Lean and Mathlib communities, endorsed by the Lean FRO and the Mathlib Initiative."

It says: "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." It ends: "We have full confidence that Alpöge's proof of the Riemann Hypothesis is correct, and we congratulate him on this achievement."

The Mathlib Initiative's home page carries a banner saying it "fully endorses" the communities' verification. ([Mathlib Initiative](https://mathlib-initiative.org/))

The statement certifies four things:

1. The formal statement is the Riemann hypothesis as Mathlib states it.
2. The library compiles without errors, and dozens of people reproduced the same proof export.
3. Two independent tools confirmed that the theorem proved, `riemannHypothesis`, is exactly Mathlib's statement of the Riemann hypothesis.
4. Several independent proof checkers accepted the exported proof.

The joint statement covers the Riemann hypothesis; [Sutherland's checks](https://math.mit.edu/~drew/grh/) also cover the four Dirichlet L-function theorems.

The statement adds that it looks forward to "all the activity in the mathematical community that will help explain the new ideas in this proof." See [how we know](/how-we-know/) for how the four checks work.

## What changed when

All times are UTC where a source gives UTC. Other clock times carry no stated time zone.

- **10 Aug 2026.** Anthropic reported that Claude raised the proven share of zeta zeros on the critical line from 41.6% to 67.2%. ([Anthropic](https://www.anthropic.com/research/riemann-zeta))
- **12 Nov.** Kevin Buzzard's Xena Project blog set out four questions to ask of a Lean repository. The joint statement later cites them as its "four criteria". ([Xena](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/))
- **16 Nov.** Quanta reports that Alpöge obtained the result on Monday 16 Nov and delayed sharing it for several days. ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **20 Nov, morning.** Alpöge posts the note and the archive.
- **20 Nov, 14:36 UTC.** The first commit appears in the Lean community's mirror of the submission. ([commit](https://github.com/leanprover-community/riemann-hypothesis/commit/40e56bab026552e089d7afcfeff08d2defb9c005))
- **20 Nov.** Sutherland is first to compile it, shortly before noon (time zone not stated). Simon DeDeo (Carnegie Mellon) follows a few hours later. Terence Tao, Scientific American, Nature and IBM Think all publish the same day.
- **21 Nov, 01:47 UTC.** Rubinstein's full compile finishes, 3 h 18 min after the distributed build started. His kernel replay finishes at 05:24 UTC and his nanoda check at 10:06 UTC. ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))
- **21 Nov, 13:55 UTC.** The joint statement is published.
- **21 Nov, evening UTC.** Sutherland's sandboxed rebuild finishes at 18:07 UTC. His `--compare` runs finish at 21:19 and 23:02 UTC. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **22 Nov, 16:20 UTC.** Sutherland's page is last updated. It reports the statement comparison and axiom check of the `lake comparator` run as passed. The Lean kernel stages are still running. ([Sutherland](https://math.mit.edu/~drew/grh/))

## Community work on the proof

Other people are writing about and working on the proof. These are three examples. The rest are on [guides](/guides/).

- **Michael Rubinstein (Waterloo).** His [guide and checks page](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) links a 265-page working guide to the proof for the zeta function (version 2, 22 Nov 2026) and says that the main inequality (M) "itself is not proved there".
- **Jimmie Adriazola (Arizona State).** His [reconstruction](https://github.com/jimjamzola/RH-Alpoge-Reconstruction) is a 66-page account of the proof in conventional mathematics, and its README (22 Nov 2026) says it "did not build or replay the archive itself".
- **verifytask.cn.** The [riemann.verifytask.cn board](https://riemann.verifytask.cn/), with its [GitHub repository](https://github.com/Osgood001/riemann-hypothesis), tracks how far contributors can shorten parts of the proof while Lean still accepts them (notice dated 23 Nov 2026).

## Primary sources

- [Alpöge's note (PDF)](https://alpo.ge/remark.pdf) and [home page](https://alpo.ge/)
- [Joint statement by the Lean FRO and the Mathlib Initiative](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
- [Community repository](https://github.com/leanprover-community/riemann-hypothesis) and its [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)
- [Sutherland's verification files (MIT)](https://math.mit.edu/~drew/grh/)
- [Rubinstein's check (Waterloo)](https://mrubinst.github.io/grh-lean-verification/) and [working guide](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)

For coverage and expert reactions, see [press](/press/). For guides by other authors that explain the proof, see [guides](/guides/).

## See it in the map

The proof is a library of 175,187 Lean files (175,027 on our map), grouped into 2,647 clusters and 63 themes. The main theorem is in [its own cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/). [How the proof is structured](/route/) shows the route from the main theorem outwards. You can also [browse every cluster as a list](/list/) or follow a [reading path](/learn/).

## About this site

riemannhypothesissolved.com is free, and independent of Levent Alpöge, Anthropic, the Lean FRO, the Lean and Mathlib communities, and the Mathlib Initiative.

## Changelog

- **23 Nov 2026.** Updated the checks to Sutherland's page as last updated 22 Nov 2026 at 16:20 UTC. Added "Community work on the proof".
- **22 Nov 2026.** First version.
