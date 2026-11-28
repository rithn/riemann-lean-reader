---
title: "Riemann hypothesis proof: press, statements, reactions"
description: "Official statements and reporting on the Lean Riemann hypothesis proof, with sourced accounts of Jenny Lorraine Nielsen’s critique and Masullo’s claim."
h1: "Press and reactions"
path: /press/
target_queries:
  - riemann hypothesis proof news
  - riemann hypothesis mathematicians react
  - riemann hypothesis anthropic reaction
  - riemann hypothesis lean certified statement
  - alpöge riemann hypothesis criticism
  - riemann hypothesis proof scientific american nature quanta
layout: doc
---

# Press and reactions

News coverage and what mathematicians have said about the Lean proof of the Riemann hypothesis, newest first.

{{press_feed}}

## Controversies {#controversies}

### Jenny Lorraine Nielsen’s criticism of Alpöge’s proof {#nielsen-criticism}

The original Lean archive defines an internal condition, `anyGeometry`, to be true for every input. In a preprint and a 23 November post, Jenny Lorraine Nielsen argues that the geometric construction and its assigned height reuse analytic data in a circular way. Carlos Toledo’s audit confirms the always-true definition and leaves the geometric interpretation of that step open. [Nielsen’s preprint](https://philarchive.org/rec/NIEIOT-2) · [Original post](https://x.com/QualiaQuanta/status/2124992635605807308) · [Pinned Lean definition](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L19) · [Toledo’s audit](https://carlostoledo.co/reports/alpoge-grh.html)

Chris Bailey explained on MathOverflow that the check depends on the proof term having the required type. An internal definition that is always true still leaves the proof obliged to establish Mathlib’s Riemann hypothesis. The certification records how two tools matched that statement and how independent checkers accepted the exported proof. Alpöge clarified on 24 November that he understood the proof to have checked out. [Bailey’s response](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust#comment1354173_518119) · [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) · [Alpöge’s clarification](https://x.com/__alpoge__/status/2125062170207457583) · [Detailed FAQ](/faq/#tautology)

### Open gaps in Alessandro Masullo’s separate manuscript {#masullo-gaps}

Masullo’s *The Music of the Primes* proposes a proof of GRH for Hecke L-functions. In its Lean formalization of this manuscript, Ryan McCorvie’s project records a counterexample to the uniform bound as printed in §1.4.3 and an unproved cancellation of zeros outside a strip in Theorem 12.5.1.1. The project shows that this cancellation for every strip width is equivalent to the manuscript’s main claim. These findings concern Masullo’s argument. Follow the [verification record](/status/) for Alpöge’s Lean release. [Manuscript v1](https://clopen.solutions/submissions/the-music-of-the-primes/v1/) · [Formalization README](https://github.com/mccorvie/riemann-masullo/blob/9c791d74a81f1191d900e6d96f1270acee9b033e/README.md) · [Open issue #5571](https://github.com/mccorvie/riemann-masullo/issues/5571)

The objections above concern Alpöge’s original archive and Masullo’s separate manuscript. Luke Sernau’s 25 November rewrites have their own verification logs. [Edition comparison](/shorter-riemann-hypothesis-proof/) · [MIT shorter-edition checks](https://math.mit.edu/~drew/shortgrh/)

## Primary sources

- [Levent Alpöge’s announcement note (PDF)](https://alpo.ge/remark.pdf) · [home page](https://alpo.ge/)
- [First commit in the Lean community mirror](https://github.com/leanprover-community/riemann-hypothesis/commit/40e56bab026552e089d7afcfeff08d2defb9c005) · [repository](https://github.com/leanprover-community/riemann-hypothesis) · [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)
- [Joint Lean FRO and Mathlib Initiative verification statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
- [Mathlib Initiative endorsement](https://mathlib-initiative.org/)
- [Lean home page](https://lean-lang.org/)
- [Association for Human Mathematics statement](https://www.ahmath.org/statements)
- [Clay Mathematics Institute’s Millennium Prize rules](https://www.claymath.org/millennium-problems/rules/)
- [Andrew Sutherland’s verification files](https://math.mit.edu/~drew/grh/)
- [Michael Rubinstein’s four Lean checks](https://mrubinst.github.io/grh-lean-verification/) · [working draft for the zeta case](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
- [Elliot Arledge’s verification receipts](https://github.com/Infatoshi/rh-verification-receipts)
- [Bartosz Naskręcki’s verification record and map](https://nasqret.github.io/riemann-rev/)

## About this site

riemannhypothesissolved.com is free, and independent of Levent Alpöge, Anthropic, the Lean FRO, the Lean and Mathlib communities, and the Mathlib Initiative.

For quotable figures, reuse terms and contact details, see [For journalists](/about/#for-journalists).
