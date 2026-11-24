---
title: "Has the Riemann hypothesis been solved? Status 24 Nov 2026"
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
as_of: "24 Nov 2026"
---

# Has the Riemann hypothesis been solved?

*As of 24 Nov 2026. The current answer, updated as news arrives. The dated record is on the [timeline](/timeline/); the changelog is at the end.*

**Latest change, 24 Nov 2026, 05:25 UTC:** Sutherland's verification page reports one check still in progress, the end-to-end `lake comparator` run on Lean v4.36.0, whose last stage is running. ([Sutherland](https://math.mit.edu/~drew/grh/), [timeline](/timeline/#nov-24))

**Levent Alpöge released a Lean proof of the Riemann hypothesis on 20 Nov 2026. On 21 Nov the Lean FRO and the Mathlib Initiative certified that the statement and the proof of the Riemann hypothesis are correct. Independent checkers have compiled all 175,187 modules, replayed the proof through Lean's kernel and checked the exported proof with several independent programs.**

## What was released

- On 20 Nov 2026 Levent Alpöge posted a four-page note and a 14-part archive of Lean files on his personal website. ([note](https://alpo.ge/remark.pdf))
- The archive holds 175,187 Lean files and about 17.4 million lines (17,374,215). ([verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- Its `Main.lean` proves five theorems, stated without hypotheses: Mathlib's own statement of the Riemann hypothesis, and four that give the generalised Riemann hypothesis for Dirichlet L-functions, for all moduli and all characters. ([Sutherland](https://math.mit.edu/~drew/grh/), [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))
- Alpöge is a mathematician at Anthropic and a junior fellow of the Harvard Society of Fellows. ([his site](https://alpo.ge/)) His note says: "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis." ([note](https://alpo.ge/remark.pdf))

## What was verified

Every check below has passed except one end-to-end `lake comparator` run, which is still in progress.

| Check | Who | Result |
|---|---|---|
| Full compile (Lean v4.33.1, Mathlib v4.33.1) | Andrew Sutherland (MIT); Michael Rubinstein (Waterloo) | 175,187 of 175,187 modules, zero errors |
| Sandboxed rebuild, no network, separate machine | Sutherland | Passes; its export is identical to the published one |
| Kernel replay of every module (`leanchecker`) | Sutherland; Rubinstein | 175,187 of 175,187 accepted |
| nanoda, an independent kernel in Rust, on the full export | Sutherland; Rubinstein | Accepted |
| con-leche on the full export | Sutherland | 1,468,418 declarations accepted |
| Statement comparison (`--compare`), con-leche and con-ron | Sutherland | All five theorems accepted |
| Lean default and paranoid kernels on the full export | Sutherland | Both accept |
| Unmodified Comparator v4.33.0, end to end | Sutherland | "Your solution is okay!" |
| `lake comparator` end to end (Lean v4.36.0) | Sutherland | In progress; last stage running |
| lean4lean, module by module | Sutherland | 175,187 of 175,187 accepted |
| Axioms used | Sutherland | Only `propext`, `Classical.choice`, `Quot.sound` |

Sources: [Sutherland's page](https://math.mit.edu/~drew/grh/) (last updated 24 Nov 2026, 05:25 UTC), which keeps the full, live list, and [Rubinstein's check](https://mrubinst.github.io/grh-lean-verification/); both ran their checks with Claude Code. [Elliot Arledge](https://github.com/Infatoshi/rh-verification-receipts) and [Bartosz Naskręcki](https://nasqret.github.io/riemann-rev/) have published their own results. When each check finished: [timeline](/timeline/).

## What was certified, and by whom

On 21 Nov 2026 at 13:55 UTC the Lean community blog published a joint statement by the Lean FRO and the Mathlib Initiative; its byline took that form on 23 Nov. It says: "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." ([statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)) The Mathlib Initiative's home page carries a banner saying it "fully endorses" the communities' verification. ([Mathlib Initiative](https://mathlib-initiative.org/))

The statement certifies four things:

1. The formal statement is the Riemann hypothesis as Mathlib states it.
2. The library compiles without errors, and dozens of people reproduced the same proof export.
3. Two independent tools confirmed that the theorem proved, `riemannHypothesis`, is exactly Mathlib's statement of the Riemann hypothesis.
4. Several independent proof checkers accepted the exported proof.

The joint statement covers the Riemann hypothesis; [Sutherland's checks](https://math.mit.edu/~drew/grh/) also cover the four Dirichlet L-function theorems. See [how we know](/how-we-know/) for how the four checks work.

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

J. L. Nielsen's preprint grants that the code typechecks but argues that its geometric part is "a manufactured witness" (p. 1). ([preprint](https://philarchive.org/rec/NIEIOT-2)) The verifiers answer that the theorem proved is stated with Mathlib's own definition of the Riemann hypothesis and was compared with it by two tools, so definitions inside the proof cannot make the checkers accept a wrong statement. ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [Bailey on MathOverflow](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust#comment1354173_518119), [Toledo](https://carlostoledo.co/reports/alpoge-grh.html), [Bloom](https://x.com/thomasfbloom/status/2124221582105014284)) In full: [Is the proof a tautology?](/faq/#tautology)

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

- **24 Nov 2026, restructure.** This page now gives the current answer only. The dated log "What changed when" moved to the [timeline](/timeline/); repeated detail was shortened.
- **24 Nov 2026, later.** Added Alpöge's two clarifying posts (23 Nov, 22:03 UTC; 24 Nov, 03:01 UTC), a short list of named reactions, and a short entry on the objection that the proof is a tautology, with the full text in the [FAQ](/faq/#tautology).
- **24 Nov 2026.** Updated the checks to Sutherland's page as last updated 24 Nov 2026 at 05:25 UTC: Lean's default and paranoid kernels and the unmodified Comparator v4.33.0 accept; the `lake comparator` run on Lean v4.36.0 is still in progress. Corrected the date of Sutherland's con-leche runs to 20 Nov. Added a section on refereed publication and the Clay prize rules.
- **23 Nov 2026.** Updated the checks to Sutherland's page as last updated 22 Nov 2026 at 16:20 UTC. Added "Community work on the proof".
- **22 Nov 2026.** First version.
