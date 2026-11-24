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

*Status as of 24 Nov 2026. This page is updated as news arrives. See the changelog at the end.*

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

All 175,187 modules compile with zero errors. Every module has been replayed through Lean's kernel, and the exported proof has been accepted by nanoda, con-leche and con-ron, and by Lean's own kernel in its default and paranoid modes. lean4lean accepts every module. A sandboxed rebuild on a separate machine produced an export identical to the published one. One end-to-end `lake comparator` run is still in progress.

| Check | Who | Result |
|---|---|---|
| Full compile of all 175,187 modules | Andrew Sutherland (MIT); Michael Rubinstein (Waterloo) | 175,187 of 175,187 compiled, zero errors (Lean v4.33.1, Mathlib v4.33.1) |
| Mathlib files against the official cache | Sutherland | 8,322 Mathlib and 378 dependency `.olean` files identical byte for byte |
| Rebuild in a sandbox with no network, on a separate machine | Sutherland | Build passes; the proof export made in the sandbox is identical to the published one |
| Replay of every module through Lean's kernel (`leanchecker`) | Sutherland; Rubinstein | 175,187 of 175,187 accepted |
| Full export checked by nanoda, an independent kernel written in Rust | Sutherland; Rubinstein | Accepted; Rubinstein reports 1,484,729 declarations checked |
| Full export checked by con-leche | Sutherland | 1,468,418 declarations accepted in `--verified` mode |
| Statement comparison (`--compare`) with con-leche and con-ron | Sutherland | All five theorems accepted as justified by the solution |
| End-to-end run of the unmodified Comparator v4.33.0 | Sutherland | Passes: statement comparison and axiom check pass, nanoda and Lean's default kernel accept, "Your solution is okay!" (09:10 UTC, 23 Nov) |
| End-to-end `lake comparator` run (Lean v4.36.0) | Sutherland | Still in progress. Its Lean paranoid kernel stage accepted at about 19:53 UTC on 23 Nov and its nanoda stage at about 21:31 UTC; its last stage, Lean's default kernel, is running |
| Lean default and paranoid kernels on the full export (Lean v4.36.0) | Sutherland | Both accept: the default kernel at 18:44 UTC on 22 Nov, the paranoid kernel at 19:01 UTC on 23 Nov |
| Module-by-module check with lean4lean | Sutherland | 175,187 of 175,187 accepted |
| Axiom check | Sutherland | Only `propext`, `Classical.choice`, `Quot.sound` |

Sources: [Sutherland's verification page](https://math.mit.edu/~drew/grh/), last updated 24 Nov 2026 at 05:25 UTC (read on 24 Nov), and [Rubinstein's check](https://mrubinst.github.io/grh-lean-verification/), where all four of his checks finished on 21 Nov. Sutherland's page keeps the full, live list. Its summary at 05:25 UTC says: "Lean's own kernel also accepts the full export, and Comparator v4.33.0 reports “Your solution is okay!”. Lean's paranoid kernel accepts it too. The lake comparator (v4.36.0) run is still in progress." Both ran their checks with Claude Code. [Elliot Arledge](https://github.com/Infatoshi/rh-verification-receipts) and [Bartosz Naskręcki](https://nasqret.github.io/riemann-rev/) have published their own results.

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

## Publication and the Clay prize

As of 24 Nov 2026 we have found no announcement of a refereed paper on the proof, and Alpöge's four-page note is his only write-up of it so far; he says he intends "to write it properly". The Clay Mathematics Institute's rules for its Millennium Prize require a solution to be published in a qualifying outlet (a refereed mathematics publication, or one approved under relaxed conditions), at least two years to pass after publication, and the solution to gain general acceptance in the mathematics community. ([note](https://alpo.ge/remark.pdf), [Clay rules](https://www.claymath.org/millennium-problems/rules/), [rules in full, §4 and §6](https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf))

## What Alpöge has said since the release

On 23 Nov 2026 at 22:03 UTC Alpöge posted a list headed "Stupid things I did" on X. ([post](https://x.com/__alpoge__/status/2124987173439209561)) It includes three points that bear on this page; replies from the next day are added after them.

- **On length.** "250,000+ pages was a joke guys!" His note had said, in a footnote about an English write-up he did not post: "I of course amused myself, and hit 250, 000+ pages." ([note](https://alpo.ge/remark.pdf)) We do not use 250,000 pages as the length of the proof. The released archive is 175,187 Lean files and about 17.4 million lines.
- **On the code.** "The Lean is full of garbage obviously, but compiles, but all criticism of such garbage is totally reasonable and accepted, I should have cleaned it up but it was randomly difficult to for various strange reasons. Mea culpa…" Elsewhere in the post: "I really was yoloing a lot in there, I bet most is unnecessary in the end, admittedly the lazy thing to do would be to wait because it’ll simplify massively…"
- **On what he thinks the point is.** "I feel Riemann should be easy, and any real difficulty is an indication our setup is just dumb at the moment."
- **In replies on 24 Nov.** On the page count, at 04:02 UTC: "Yeah alas. I did say I amused myself before giving the number and gave an example from the main theorem of incredible pedantry, but I should’ve cut it." ([reply](https://x.com/__alpoge__/status/2125077588263465075)) On the word "garbage", at 03:08 UTC: "Yea i use the word garbage too liberally from video games of yore. “full of garbage” is a hilarious choice. Mb" ([reply](https://x.com/__alpoge__/status/2125063891034186070))

At 03:01 UTC on 24 Nov he added: "People seem to be reading this as me saying there’s something wrong with the proof. I’m pretty confused. No? It literally checked out days ago?" ([post](https://x.com/__alpoge__/status/2125062170207457583))

The checks above test the exported proof, not how tidy the source is, so these posts do not change them. They do confirm that the author regards the released code as unpolished, and that a readable account of the argument is still to come.

## Reactions

Eight named reactions from 20 to 21 Nov, with a stance for each. None of these people reports a failed check. The doubts are about whether the argument can be read, about how it was released, and about who is responsible for it. More are on [press](/press/).

- **Andrew Sutherland (MIT), 20–21 Nov. Accepts the formal check.** "Honestly the chance that anything is fishy here is approximately zero." ([Scientific American](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/))
- **Scott Aaronson, blog, 20 Nov and 21 Nov update. Accepts the check; says readability is the next job.** On 21 Nov, after the con-leche verification: "The proof is correct." On 20 Nov: "Mathematicians of course won’t be satisfied with 17 million lines of Lean. They’ll be satisfied when, and only when, they’re able to explain and distill and reconstruct the ideas for themselves." ([Shtetl-Optimized](https://scottaaronson.blog/?p=10344))
- **James Maynard (University of Oxford), Nature, 20 Nov. Expects it to hold; needs understanding.** "I suspect that the proof will turn out to be correct," ([Nature](https://www.nature.com/articles/d41586-026-03812-7))
- **Alex Kontorovich (Rutgers), AP, 20 Nov. Accepts the check; says he still has to read it.** "…if you can satisfy the computer, there's a very, very good chance you're going to satisfy me too," and "But I have to do the work." ([AP via ABC News](https://abcnews.com/Technology/wireStory/anthropic-worker-claims-solved-holy-grail-math-problems-138338426))
- **Kevin Buzzard (Imperial College London), Al Jazeera, 21 Nov. Cautious about readability.** "At the minute, we don’t even know why the theorem is true," He also said: "Experience shows you that you give the humans the Lean code, and within a week or two, they have a much better understanding of what’s actually going on in this code," ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked))
- **Maksym Radziwiłł (NYU), Quanta, 20 Nov, from an email. Cautious about understanding.** "The object of mathematics as the rest of science is really the question ‘why?’ and this doesn’t answer it at all." ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **Andrew Granville (University of Montreal), Nature, 20 Nov. Objects to the write-up and the timing.** "What he released is garbled," ([Nature](https://www.nature.com/articles/d41586-026-03812-7)) Alpöge's note calls the timing explanation "an obvious cynical view" and says it "is false".
- **Association for Human Mathematics (Communications Working Group), statement dated 20 Nov. Objects to the process.** "At this time, no human being can reasonably claim to be responsible for, or even to understand, such a document. Neither can any mathematician confirm with full certainty that the proof is correct." It was written before the joint statement. ([AHM](https://www.ahmath.org/statements))

## Objections and responses

J. L. Nielsen's preprint grants that the code typechecks ("Although the type comparison succeeds, it does not supply the missing mathematical content", p. 1) but argues that its geometric part is "a manufactured witness" (p. 1), so that "The formal comparison is Riemann to Riemann, not an independent geometric derivation of Riemann" (p. 15). ([preprint](https://philarchive.org/rec/NIEIOT-2)) The verifiers answer that the theorem proved is stated with Mathlib's own definition of the Riemann hypothesis and was compared with it by two tools, so definitions inside the proof cannot make the checkers accept a wrong statement. ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [Bailey on MathOverflow](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust#comment1354173_518119), [Toledo](https://carlostoledo.co/reports/alpoge-grh.html), [Bloom](https://x.com/thomasfbloom/status/2124221582105014284)) Whether the code checks is not in dispute; what is in dispute is what the code means. The objection, what is true in it and the responses in full: [Is the proof a tautology?](/faq/#tautology)

## What changed when

All times are UTC where a source gives UTC. Other clock times carry no stated time zone.

- **10 Aug 2026.** Anthropic reported that Claude raised the proven share of zeta zeros on the critical line from 41.6% to 67.2%. ([Anthropic](https://www.anthropic.com/research/riemann-zeta))
- **12 Nov.** Kevin Buzzard's Xena Project blog set out four questions to ask of a Lean repository. The joint statement later cites them as its "four criteria". ([Xena](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/))
- **16 Nov.** Quanta reports that Alpöge obtained the result on Monday 16 Nov and delayed sharing it for several days. ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **20 Nov, morning.** Alpöge posts the note and the archive.
- **20 Nov, 14:36 UTC.** The first commit appears in the Lean community's mirror of the submission. ([commit](https://github.com/leanprover-community/riemann-hypothesis/commit/40e56bab026552e089d7afcfeff08d2defb9c005))
- **20 Nov.** Sutherland is first to compile it, shortly before noon (time zone not stated). Simon DeDeo (Carnegie Mellon) follows a few hours later. Terence Tao, Scientific American, Nature and IBM Think all publish the same day.
- **20 Nov, 21:19 UTC.** Sutherland's con-leche run accepts the full export, and its `--compare` run accepts all five theorems. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **21 Nov, 01:47 UTC.** Rubinstein's full compile finishes, 3 h 18 min after the distributed build started. His kernel replay finishes at 05:24 UTC and his nanoda check at 10:06 UTC. ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))
- **21 Nov, 13:55 UTC.** The joint statement is published.
- **21 Nov, evening UTC.** Sutherland's sandboxed rebuild finishes at 18:07 UTC. His con-ron `--compare` run finishes at 23:02 UTC. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **22 Nov, 16:20 UTC.** Sutherland's page is last updated. It reports the statement comparison and axiom check of the `lake comparator` run as passed. The Lean kernel stages are still running. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **22 Nov, 18:44 UTC.** Lean's default kernel accepts the full export, after 48 hours on one thread. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **23 Nov, 09:10 UTC.** The unmodified Comparator v4.33.0 passes end to end: "Your solution is okay!" ([Sutherland](https://math.mit.edu/~drew/grh/))
- **23 Nov, 19:01 UTC.** Lean's paranoid kernel accepts the full export. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **24 Nov, 05:25 UTC.** Sutherland's page is last updated. One check is still in progress: the end-to-end `lake comparator` run on Lean v4.36.0, whose last stage is running. ([Sutherland](https://math.mit.edu/~drew/grh/))

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
- Alpöge's posts on X: [23 Nov, 22:03 UTC](https://x.com/__alpoge__/status/2124987173439209561) and [24 Nov, 03:01 UTC](https://x.com/__alpoge__/status/2125062170207457583)
- [Toledo's audit](https://carlostoledo.co/reports/alpoge-grh.html) (independent, last updated 24 Nov 2026 at 10:27 UTC) and the [MathOverflow thread on trust assumptions](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust)

For coverage and expert reactions, see [press](/press/). For guides by other authors that explain the proof, see [guides](/guides/).

## See it in the map

The proof is a library of 175,187 Lean files (175,027 on our map), grouped into 2,647 clusters and 63 themes. The main theorem is in [its own cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/). [How the proof is structured](/route/) shows the route from the main theorem outwards. You can also [browse every cluster as a list](/list/) or follow a [reading path](/learn/).

## About this site

riemannhypothesissolved.com is free, and independent of Levent Alpöge, Anthropic, the Lean FRO, the Lean and Mathlib communities, and the Mathlib Initiative.

## Changelog

- **24 Nov 2026, later.** Added Alpöge's two clarifying posts (23 Nov, 22:03 UTC; 24 Nov, 03:01 UTC), a short list of named reactions, and a short entry on the objection that the proof is a tautology, with the full text in the [FAQ](/faq/#tautology).
- **24 Nov 2026.** Updated the checks to Sutherland's page as last updated 24 Nov 2026 at 05:25 UTC: Lean's default and paranoid kernels and the unmodified Comparator v4.33.0 accept; the `lake comparator` run on Lean v4.36.0 is still in progress. Corrected the date of Sutherland's con-leche runs to 20 Nov. Added a section on refereed publication and the Clay prize rules.
- **23 Nov 2026.** Updated the checks to Sutherland's page as last updated 22 Nov 2026 at 16:20 UTC. Added "Community work on the proof".
- **22 Nov 2026.** First version.
