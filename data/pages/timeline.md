---
title: "Riemann hypothesis timeline: 1748 to the 2026 Lean proof"
description: "Dated events from Euler's product in 1748 and Riemann's 1859 memoir to the Lean proof released on 20 Nov 2026, certified on 21 Nov, with a source for each."
h1: "Timeline of the Riemann hypothesis"
path: /timeline/
target_queries:
  - riemann hypothesis history
  - riemann hypothesis timeline
  - when was the riemann hypothesis proved
  - riemann hypothesis proof date
as_of: "22 Nov 2026"
---

# Timeline of the Riemann hypothesis

*As of 22 Nov 2026. Times are UTC where a source gives UTC. Other clock times carry no stated time zone.*

**Riemann stated the hypothesis in 1859. Levent Alpöge released a Lean proof on 20 Nov 2026, and the Lean FRO and the Mathlib Initiative certified it on 21 Nov.** See [status](/status/) for what was checked.

## Background

- **1748.** Euler's book *Introductio in Analysin Infinitorum* gives the product over primes that connects primes to the zeta function. ([Bombieri, Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))
- **1859.** Riemann publishes a memoir with a formula for the number of primes up to a limit, written in terms of the zeros of the zeta function. In it he writes that it is very likely that all the zeros of his function ξ(t) are real. This is the Riemann hypothesis. ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))
- **24 May 2000.** The Clay Mathematics Institute announces seven Prize Problems at the Collège de France in Paris, with $1 million for each solution. The Riemann hypothesis is one of them. ([Clay](https://www.claymath.org/millennium-problems/))

## 2026: AI results before the proof

- **10 Aug 2026.** Anthropic reports that Claude raised the proven share of nontrivial zeta zeros on the critical line from 41.6% to 67.2%. Anthropic writes that it does not expect these techniques to lead to a proof of the Riemann hypothesis. Alpöge and Ralph Furman, two of Anthropic's mathematicians, examined the work. ([Anthropic](https://www.anthropic.com/research/riemann-zeta))
- **8 Sep 2026.** OpenAI announces that its internal model proved finite-time blow-up for the Navier–Stokes equations, another Clay problem. Scientific American reports on 22 Oct that the proof reintroduces a force. ([Scientific American, 8 Sep](https://www.scientificamerican.com/article/openai-claims-blockbuster-math-breakthrough-amid-swirl-of-controversy/), [22 Oct](https://www.scientificamerican.com/article/the-inside-story-behind-openais-million-dollar-math-proof/))
- **6 Oct 2026.** OpenAI announces a batch of results that includes a proof of the quasi-Riemann hypothesis, which puts all the zeros in a strip narrower than the strip between 0 and 1. Quanta covers it on 19 Oct. ([Quanta](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/))
- **12 Nov 2026.** The Xena Project blog posts "…and the proof is checked in Lean", four questions to ask of a Lean repository. The joint statement of 21 Nov cites them as its "four criteria". ([Xena](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/))
- **16 Nov 2026.** Alpöge obtains the result. He delays sharing it for several days. ([Quanta](https://www.quantamagazine.org/updates/transformation/))

## 20 Nov 2026: release

- **20 Nov, morning.** Alpöge uploads a four-page note and a 14-part archive of Lean files to his personal website. ([Quanta](https://www.quantamagazine.org/updates/transformation/), [note](https://alpo.ge/remark.pdf))
- **20 Nov, 10:18 am.** Ravi Vakil posts a separate, human-written draft proof of GRH by Alessandro Masullo. About 8 hours later he adds that several people report problems found with AI models. ([Vakil](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/))
- **20 Nov, shortly before noon.** Andrew Sutherland (MIT) is the first to compile the library independently. Simon DeDeo (Carnegie Mellon) follows a few hours later. ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **20 Nov, 12:29 pm.** Scott Aaronson posts "The stochastic parrots have apparently proved the Riemann Hypothesis". ([Shtetl-Optimized](https://scottaaronson.blog/?p=10344))
- **20 Nov, 14:36 UTC.** The first commit appears in the Lean community's mirror of the submission. ([commit](https://github.com/leanprover-community/riemann-hypothesis/commit/40e56bab026552e089d7afcfeff08d2defb9c005))
- **20 Nov.** Terence Tao writes that Alpöge, "using an internal AI model, has generated an (enormous) Lean-only proof of the Generalized Riemann Hypothesis". The same post covers Euler and Navier–Stokes blow-up claims that Alpöge and Tristan Buckmaster released the same day. ([Tao](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/))
- **20 Nov.** Scientific American, Nature and IBM Think publish reports. ([Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/), [Nature](https://www.nature.com/articles/d41586-026-03812-7), [IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof))

## 21 Nov 2026: checks and certification

- **21 Nov, 01:47 UTC.** Michael Rubinstein (Waterloo) finishes a full compile of all 175,187 modules, 3 h 18 min after the distributed build started. His kernel replay finishes at 05:24 UTC and his nanoda check at 10:06 UTC. ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))
- **21 Nov, 13:55 UTC.** The Lean community blog publishes the joint statement by the Lean FRO and the Mathlib Initiative: "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." ([statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))
- **21 Nov, 18:07 UTC.** Sutherland's sandboxed rebuild on a separate machine finishes. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **21 Nov, 21:19 UTC.** con-leche accepts the full export, and its `--compare` run accepts all five theorems. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **21 Nov, about 21:55 UTC.** lean4lean finishes accepting 175,187 of 175,187 modules. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **21 Nov, 23:02 UTC.** con-ron's `--compare` run accepts. ([Sutherland](https://math.mit.edu/~drew/grh/))

## 22 Nov 2026: checks still running

- **22 Nov, 16:20 UTC.** Sutherland's page lists two runs still going: the Lean default and paranoid kernels on the export (running since 18:41 UTC on 20 Nov), and the end-to-end `lake comparator` run on Lean v4.36.0 (its statement comparison and axiom check have passed). ([Sutherland](https://math.mit.edu/~drew/grh/))

For coverage and expert reactions, see [press](/press/). For the numbers, see [the proof in numbers](/proof-in-numbers/).
