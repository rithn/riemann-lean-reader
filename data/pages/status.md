---
title: "Has the Riemann hypothesis been solved? Proof status"
description: "The 20 November Lean proof was certified on 21 November. See the independent verification results for the original archive and both Sernau rewrites."
h1: "Has the Riemann hypothesis been solved?"
path: /status/
target_queries:
  - is the riemann hypothesis solved
  - has the riemann hypothesis been solved yet
  - riemann hypothesis status
  - riemann hypothesis update latest
  - riemann hypothesis solved confirmed
  - riemann hypothesis lean proof verified
as_of: "26 Nov 2026"
---

# Has the Riemann hypothesis been solved?

*As of 26 Nov 2026. See the [timeline](/timeline/) for the dated record.*

**Levent Alpöge released a Lean proof of the Riemann hypothesis on 20 Nov 2026. On 21 Nov the Lean FRO and the Mathlib Initiative certified that the statement and the proof of the Riemann hypothesis are correct. Independent checkers have compiled all 175,187 modules, replayed the proof through Lean's kernel and checked the exported proof with several independent programs.**

**Verification update, 26 Nov 2026.** Andrew Sutherland reports a full paranoid Comparator pass for each of Luke Sernau’s two shorter editions. Michael Rubinstein’s Waterloo team reports a compact-edition paranoid pass, and Sho Sonoda reports standard Comparator passes for both editions. [Shorter-edition checks](#shorter-editions) · [Timeline](/timeline/#nov-26)

[Follow updates via RSS](/changelog/feed.xml). Paste the link into your feed reader to get new updates.

## What was released

- On 20 Nov 2026 Levent Alpöge posted a four-page note and a 14-part archive of Lean files on his personal website. ([note](https://alpo.ge/remark.pdf))
- The archive holds 175,187 Lean files and about 17.4 million lines (17,374,215). ([verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- `Main.lean` proves five theorems, two formulations of the classical Riemann hypothesis and three statements about Dirichlet L-functions. The two RH formulations use Mathlib's statement and an explicit statement about zeta zeros. For Dirichlet characters of every modulus, the L-functions have no zeros to the right of the critical line, with the pole at `s = 1` excluded for the trivial character, and all zeros in the critical strip lie on the critical line. A third statement gives the critical-strip result for primitive characters. ([pinned `Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean), [Sutherland](https://math.mit.edu/~drew/grh/))
- Alpöge is a mathematician at Anthropic and a junior fellow of the Harvard Society of Fellows. ([his site](https://alpo.ge/)) His note says: "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis." ([note](https://alpo.ge/remark.pdf))

## What was verified

These checks cover the original 20 November release.

| Check | Who | Result |
|---|---|---|
| Full compile (Lean v4.33.1, Mathlib v4.33.1) | Andrew Sutherland (MIT); Michael Rubinstein (Waterloo) | 175,187 of 175,187 modules, zero errors |
| Sandboxed rebuild, no network, separate machine | Sutherland | Passes; its export is identical to the published one |
| Kernel replay of every module (`leanchecker`) | Sutherland; Rubinstein | 175,187 of 175,187 accepted |
| nanoda, an independent kernel in Rust, on the full export | Sutherland; Rubinstein | Accepted |
| con-leche on the full export | Sutherland | 1,468,418 declarations accepted |
| Statement comparison (`--compare`), con-leche and con-ron | Sutherland | All five theorems accepted |
| Lean default and paranoid kernels on the full export | Sutherland | Both accept |
| Unmodified Comparator v4.33.0 on the original build files | Sutherland | Statement and axiom checks pass. Two kernels accept. The build step used a stub. |
| `lake comparator` (Lean v4.36.0) on the submitted archive’s exports | Sutherland | Passes with the canonical challenge export. Statement and axiom checks pass. Lean’s paranoid kernel, nanoda and Lean’s default kernel accept. |
| lean4lean, module by module | Sutherland | 175,187 of 175,187 accepted |
| Axioms used | Sutherland | Only `propext`, `Classical.choice`, `Quot.sound` |

Sutherland’s log was last updated on 25 November 2026 at 22:05 UTC. Sutherland and Rubinstein ran their checks with Claude Code. Elliot Arledge and Bartosz Naskręcki published their own results. [Sutherland](https://math.mit.edu/~drew/grh/) · [Rubinstein](https://mrubinst.github.io/grh-lean-verification/) · [Arledge](https://github.com/Infatoshi/rh-verification-receipts) · [Naskręcki](https://nasqret.github.io/riemann-rev/) · [Timeline](/timeline/)

## Independent checks of the shorter editions {#shorter-editions}

Luke Sernau released the readable and compact rewrites on 25 November. Both use Lean v4.35.0 and Mathlib at commit `56a00585`, and prove the same five theorems as the original. Sutherland’s independent checks used pinned commit `72fead10`. [Release and five-statement comparison](/shorter-riemann-hypothesis-proof/) · [Pinned source](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207)

| Check | Readable (`grh/`) | Compact (`grh-compact/`) |
|---|---|---|
| Sandboxed build and module replay | Passed, 803 of 803 modules replayed | Passed, 794 of 794 modules replayed |
| Axiom audit and statement matching | Each theorem uses only `propext`, `Classical.choice` and `Quot.sound`. Con-leche and con-ron each matched all five statements to the challenge. | Same three axioms and all five matches in both checkers. |
| Full sandboxed `lake comparator --paranoid` on 26 November | Passed on machine B at 02:47:54 UTC. On machine A, the operator stopped lean4lean at a memory threshold. That run has no verdict. | Passed on machine B at 00:49:14 UTC and on machine A at 01:39:22 UTC. |

On both editions the proof exports were reproduced byte for byte across the two machines and accepted by nanoda, con-leche and con-ron. These results are Sutherland’s independent checks. The joint certification below concerns the original 20 November release. [MIT results, updated 26 November at 02:50 UTC](https://math.mit.edu/~drew/shortgrh/) · [Compact verification walkthrough](/how-we-know/#verify-compact)

### Additional verification reports {#additional-shorter-checks}

- **Waterloo · 26 November, 05:34 UTC.** Michael Rubinstein’s Waterloo team reports compiling and replaying all 794 compact-edition modules at `72fead10` and completing paranoid Comparator on 26 November at 05:34 UTC. Its cluster run disabled the sandbox. MIT’s separate run used a sandbox. [Waterloo report](https://mrubinst.github.io/grh-lean-compact-check/)
- **Sho Sonoda · 26 November.** Sonoda reports building both editions at `72fead10` (803 readable modules and 794 compact modules) and running standard Comparator v4.35.0. Lean’s default kernel and nanoda accepted both. His report describes the sandbox setup and a seccomp wrapper. [Report and run details](https://shosonoda.github.io/lean-rh-alpoge/grh.html#grh-comparator)

## What was certified, and by whom

On 21 Nov 2026 at 13:55 UTC the Lean community blog published a joint statement by the Lean FRO and the Mathlib Initiative; its byline took that form on 23 Nov. It says: "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." ([statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)) The Mathlib Initiative's home page carries a banner saying it "fully endorses" the communities' verification. ([Mathlib Initiative](https://mathlib-initiative.org/))

The statement certifies four things:

1. The formal statement is the Riemann hypothesis as Mathlib states it.
2. The library compiles without errors, and dozens of people reproduced the same proof export.
3. Two independent tools confirmed that the theorem proved, `riemannHypothesis`, is exactly Mathlib's statement of the Riemann hypothesis.
4. Several independent proof checkers accepted the exported proof.

The joint statement covers the Riemann hypothesis. Sutherland's checks also cover all three Dirichlet L-function statements. See [how we know](/how-we-know/) for how the four certification criteria work. ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [Sutherland](https://math.mit.edu/~drew/grh/))

## Publication and the Clay prize

As of 24 Nov 2026 we have found no announcement of a refereed paper on the proof. Alpöge's four-page note is his only write-up so far; he says he intends "to write it properly". The Clay Millennium Prize rules require a solution to be published in a qualifying outlet, at least two years to pass after publication, and general acceptance in the mathematics community. ([note](https://alpo.ge/remark.pdf), [Clay rules](https://www.claymath.org/millennium-problems/rules/), [rules in full, §4 and §6](https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf))

## What Alpöge has said since the release

On 23 Nov Alpöge posted on X that "250,000+ pages was a joke guys!" and that "The Lean is full of garbage obviously, but compiles". ([post](https://x.com/__alpoge__/status/2124987173439209561)) We do not use 250,000 pages as the length of the proof. On 24 Nov he added: "People seem to be reading this as me saying there’s something wrong with the proof. I’m pretty confused. No? It literally checked out days ago?" ([post](https://x.com/__alpoge__/status/2125062170207457583))

The checks test the exported proof, not how tidy the source is, so these posts do not change them; they do confirm that a readable account of the argument is still to come. Times and his replies: [timeline](/timeline/#nov-24).

## Reactions

Named reactions from 20 to 21 Nov. None reports a failed check; the doubts are about readability, the release and responsibility. More on [press](/press/).

- **Andrew Sutherland (MIT). Accepts the formal check.** "Honestly the chance that anything is fishy here is approximately zero." ([Scientific American](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/))
- **Scott Aaronson, blog. Accepts the check.** On 21 Nov: "The proof is correct." On 20 Nov: mathematicians will be satisfied "when, and only when, they’re able to explain and distill and reconstruct the ideas for themselves." ([Shtetl-Optimized](https://scottaaronson.blog/?p=10344))
- **James Maynard (University of Oxford), 20 Nov. Expects it to hold.** "I suspect that the proof will turn out to be correct," ([Nature](https://www.nature.com/articles/d41586-026-03812-7))
- **Alex Kontorovich (Rutgers), 20 Nov. Accepts the check; still has to read it.** "…if you can satisfy the computer, there's a very, very good chance you're going to satisfy me too," and "But I have to do the work." ([AP via ABC News](https://abcnews.com/Technology/wireStory/anthropic-worker-claims-solved-holy-grail-math-problems-138338426))
- **Kevin Buzzard (Imperial College London), 21 Nov. Cautious about readability.** "At the minute, we don’t even know why the theorem is true," ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked))
- **Maksym Radziwiłł (NYU), 20 Nov. Cautious about understanding.** "The object of mathematics as the rest of science is really the question ‘why?’ and this doesn’t answer it at all." ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **Andrew Granville (University of Montreal), 20 Nov. Objects to the write-up.** "What he released is garbled," ([Nature](https://www.nature.com/articles/d41586-026-03812-7))
- **Association for Human Mathematics, 20 Nov, before the joint statement. Objects to the process.** "Neither can any mathematician confirm with full certainty that the proof is correct." ([AHM](https://www.ahmath.org/statements))

## Objections and responses

J. L. Nielsen's preprint grants that the code typechecks but argues that its geometric part is "a manufactured witness" (p. 1). ([preprint](https://philarchive.org/rec/NIEIOT-2)) The verifiers answer that the theorem proved is stated with Mathlib's own definition of the Riemann hypothesis and was compared with it by two tools, so definitions inside the proof cannot make the checkers accept a wrong statement. ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [Bailey on MathOverflow](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust#comment1354173_518119), [Toledo](https://carlostoledo.co/reports/alpoge-grh.html), [Bloom](https://x.com/thomasfbloom/status/2124221582105014284)) [Detailed FAQ](/faq/#tautology) · [Controversies and responses](/press/#controversies)

## Community work on the proof

Three examples; the rest are on [guides](/guides/).

- **Michael Rubinstein (Waterloo):** a 265-page [working guide](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) to the proof for the zeta function (version 2, 22 Nov 2026).
- **Jimmie Adriazola (Arizona State):** a 66-page [reconstruction](https://github.com/jimjamzola/RH-Alpoge-Reconstruction) in conventional mathematics, which "did not build or replay the archive itself".
- **verifytask.cn:** a [board](https://riemann.verifytask.cn/) ([GitHub](https://github.com/Osgood001/riemann-hypothesis)) tracking how far contributors can shorten parts of the proof while Lean still accepts them.

## Primary sources

- [Alpöge's note (PDF)](https://alpo.ge/remark.pdf) and [home page](https://alpo.ge/)
- [Joint statement by the Lean FRO and the Mathlib Initiative](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
- [Community repository](https://github.com/leanprover-community/riemann-hypothesis) and its [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)
- [Sutherland's verification files (MIT)](https://math.mit.edu/~drew/grh/)
- [Rubinstein's check (Waterloo)](https://mrubinst.github.io/grh-lean-verification/) and [working guide](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
- [Toledo's audit](https://carlostoledo.co/reports/alpoge-grh.html) (independent, last updated 24 Nov 2026 at 10:27 UTC) and the [MathOverflow thread on trust assumptions](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust)

For coverage and expert reactions, see [press](/press/). For guides by other authors that explain the proof, see [guides](/guides/).

## See it in the map

The proof is a library of 175,187 Lean files (175,027 on our map), grouped into 2,647 clusters and 63 themes. The main theorem is in [its own cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/). [How the proof is structured](/route/) shows the route from the main theorem outwards. You can also [browse every cluster as a list](/list/) or follow a [reading path](/learn/).

## About this site

riemannhypothesissolved.com is free, and independent of Levent Alpöge, Anthropic, the Lean FRO, the Lean and Mathlib communities, and the Mathlib Initiative.

## Changelog

- **26 Nov 2026.** Recorded the completed v4.36.0 Comparator run on the original archive’s exports.
- **25 Nov 2026.** Corrected the scope of the five theorems in `Main.lean` and clarified the scope of the verification runs on the [timeline](/timeline/#nov-24).
- **24 Nov 2026, restructure.** This page now gives the current answer only. The dated log "What changed when" moved to the [timeline](/timeline/); repeated detail was shortened.
- **24 Nov 2026, later.** Added Alpöge's two clarifying posts (23 Nov, 22:03 UTC; 24 Nov, 03:01 UTC), a short list of named reactions, and a short entry on the objection that the proof is a tautology, with the full text in the [FAQ](/faq/#tautology).
- **24 Nov 2026.** Updated the checks to Sutherland's page as last updated 24 Nov 2026 at 05:25 UTC: Lean's default and paranoid kernels and the unmodified Comparator v4.33.0 accept; the `lake comparator` run on Lean v4.36.0 is still in progress. Corrected the date of Sutherland's con-leche runs to 20 Nov. Added a section on refereed publication and the Clay prize rules.
- **23 Nov 2026.** Updated the checks to Sutherland's page as last updated 22 Nov 2026 at 16:20 UTC. Added "Community work on the proof".
- **22 Nov 2026.** First version.
