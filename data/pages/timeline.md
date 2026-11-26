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
as_of: "26 Nov 2026"
---

# Timeline of the Riemann hypothesis

*As of 26 Nov 2026. Times are UTC where a source gives UTC. Other clock times carry no stated time zone.*

**Riemann stated the hypothesis in 1859. Levent Alpöge released a Lean proof on 20 Nov 2026, and the Lean FRO and the Mathlib Initiative certified it on 21 Nov.**

For the current state, see [/status/](/status/).

## Background {#background}

- **1748.** Euler's book *Introductio in Analysin Infinitorum* gives the product over primes that connects primes to the zeta function. ([Bombieri, Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))
- **1859.** Riemann publishes a memoir with a formula for the number of primes up to a limit, written in terms of the zeros of the zeta function. In it he writes that it is very likely that all the zeros of his function ξ(t) are real. This is the Riemann hypothesis. ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))
- **24 May 2000.** The Clay Mathematics Institute announces seven Prize Problems at the Collège de France in Paris, with $1 million for each solution. The Riemann hypothesis is one of them. ([Clay](https://www.claymath.org/millennium-problems/))

## 2026: AI results before the proof {#before-the-proof}

- **10 Aug 2026.** Anthropic reports that Claude raised the proven share of nontrivial zeta zeros on the critical line from 41.6% to 67.2%. Anthropic writes that it does not expect these techniques to lead to a proof of the Riemann hypothesis. Alpöge and Ralph Furman, two of Anthropic's mathematicians, examined the work. ([Anthropic](https://www.anthropic.com/research/riemann-zeta))
- **8 Sep 2026.** OpenAI announces that its internal model proved finite-time blow-up for the Navier–Stokes equations, another Clay problem. Scientific American reports on 22 Oct that the proof reintroduces a force. ([Scientific American, 8 Sep](https://www.scientificamerican.com/article/openai-claims-blockbuster-math-breakthrough-amid-swirl-of-controversy/), [22 Oct](https://www.scientificamerican.com/article/the-inside-story-behind-openais-million-dollar-math-proof/))
- **6 Oct 2026.** OpenAI announces a batch of results that includes a proof of the quasi-Riemann hypothesis, which puts all the zeros in a strip narrower than the strip between 0 and 1. Quanta covers it on 19 Oct. ([Quanta](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/))
- **12 Nov 2026.** The Xena Project blog posts "…and the proof is checked in Lean", four questions to ask of a Lean repository. The joint statement of 21 Nov cites them as its "four criteria". ([Xena](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/))
- **16 Nov 2026.** Quanta reports that Alpöge obtained the result on Monday 16 Nov and delayed sharing it for several days. ([Quanta](https://www.quantamagazine.org/updates/transformation/))

## 20 Nov 2026: release {#nov-20}

- **20 Nov.** Terence Tao writes that Alpöge, "using an internal AI model, has generated an (enormous) Lean-only proof of the Generalized Riemann Hypothesis". The same post covers Euler and Navier–Stokes blow-up claims that Alpöge and Tristan Buckmaster released the same day. ([Tao](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/))
- **20 Nov.** Scientific American, Nature and IBM Think publish reports. ([Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/), [Nature](https://www.nature.com/articles/d41586-026-03812-7), [IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof))
- **20 Nov.** The Association for Human Mathematics publishes a statement criticising the announcement; it says no mathematician can yet confirm with full certainty that the proof is correct. ([AHM](https://www.ahmath.org/statements))
- **20 Nov, morning.** Alpöge uploads a four-page note and a 14-part archive of Lean files to his personal website. ([Quanta](https://www.quantamagazine.org/updates/transformation/), [note](https://alpo.ge/remark.pdf))
- **20 Nov, 10:18 am.** Ravi Vakil posts a separate, human-written draft proof of GRH by Alessandro Masullo. About 8 hours later he adds that several people report problems found with AI models. ([Vakil](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/))
- **20 Nov, shortly before noon.** Andrew Sutherland (MIT) is the first to compile the library independently. Simon DeDeo (Carnegie Mellon) follows a few hours later. ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **20 Nov, 12:29 pm.** Scott Aaronson posts "The stochastic parrots have apparently proved the Riemann Hypothesis". ([Shtetl-Optimized](https://scottaaronson.blog/?p=10344))
- **20 Nov, 14:36 UTC.** The first commit appears in the Lean community's mirror of the submission. ([commit](https://github.com/leanprover-community/riemann-hypothesis/commit/40e56bab026552e089d7afcfeff08d2defb9c005))
- **20 Nov, 21:19 UTC.** con-leche accepts the full export, and its `--compare` run accepts all five theorems. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **20 Nov, about 21:55 UTC.** lean4lean finishes accepting 175,187 of 175,187 modules. ([Sutherland](https://math.mit.edu/~drew/grh/))

## 21 Nov 2026: checks and certification {#nov-21}

- **21 Nov, 01:47 UTC.** Michael Rubinstein (Waterloo) finishes a full compile of all 175,187 modules, 3 h 18 min after the distributed build started. His kernel replay finishes at 05:24 UTC and his nanoda check at 10:06 UTC. ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))
- **21 Nov, 13:55 UTC.** The Lean community blog publishes the joint statement by the Lean FRO and the Mathlib Initiative: "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." ([statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))
- **21 Nov, 18:07 UTC.** Sutherland's sandboxed rebuild on a separate machine finishes. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **21 Nov, 19:21 UTC.** Thomas Bloom (University of Manchester) writes on X that finding "a small part of the massive formal RH proof that is vacuously true" does not invalidate the proof. ([X](https://x.com/thomasfbloom/status/2124221582105014284))
- **21 Nov, 23:02 UTC.** con-ron's `--compare` run accepts. ([Sutherland](https://math.mit.edu/~drew/grh/))

## 22 Nov 2026: kernel checks {#nov-22}

- **22 Nov.** A reader's post on dev.to confirms that a condition named `anyGeometry` is defined as `fun _ _ _ => True` in `OverIx.lean`, in response to a preprint on PhilArchive that calls the proof a tautology. It does not say whether the main route depends on it. ([Chu](https://dev.to/frankchu/grh-proofs-geometry-is-fun-true-in-24-files-2n2b))
- **22 Nov, 16:20 UTC.** Sutherland's page lists two runs still going: the Lean default and paranoid kernels on the export (running since 18:41 UTC on 20 Nov), and the end-to-end `lake comparator` run on Lean v4.36.0 (its statement comparison and axiom check have passed). ([Sutherland](https://math.mit.edu/~drew/grh/))
- **22 Nov, 18:44 UTC.** Lean's default kernel accepts the full export, after 48 hours on one thread. ([Sutherland](https://math.mit.edu/~drew/grh/))

## 23 Nov 2026: statements and objections {#nov-23}

- **23 Nov.** The joint statement's byline is changed to "Joint statement by the Lean FRO and the Mathlib Initiative." It first read "Joint statement by the Lean and Mathlib communities, endorsed by the Lean FRO and the Mathlib Initiative." ([statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))
- **23 Nov, 01:44 UTC.** Chris Bailey answers a MathOverflow question on the trust assumptions behind the Lean checks. At 06:38 UTC he comments that "the definitions used in the proof are irrelevant as long as they produce a term of the correct type". ([MathOverflow](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust))
- **23 Nov, 09:10 UTC.** Sutherland's standalone Comparator v4.33.0 passes the statement and axiom checks on files from the original build. Nanoda and Lean's default kernel accept. The comparator's build step uses a stub. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **23 Nov, 19:01 UTC.** Lean's paranoid kernel accepts the full export. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **By 23 Nov, 19:15 UTC.** The Clay Mathematics Institute's Riemann hypothesis page displays the label “Active”. A 21 Nov capture shows “Unsolved”. ([21 Nov capture](https://web.archive.org/web/20261121104538/https://www.claymath.org/millennium/riemann-hypothesis/), [23 Nov capture](https://web.archive.org/web/20261123191538/https://www.claymath.org/millennium/riemann-hypothesis/), [Clay's current page](https://www.claymath.org/millennium/Riemann-Hypothesis/))
- **23 Nov, about 19:53 UTC.** The Lean paranoid kernel stage of Sutherland's end-to-end `lake comparator` run (Lean v4.36.0) accepts. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **23 Nov, about 21:31 UTC.** The nanoda stage of the same `lake comparator` run accepts. Its last stage, Lean's default kernel, starts. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **23 Nov, 22:03 UTC.** Alpöge posts a list headed "Stupid things I did" on X. It says that "250,000+ pages was a joke guys!" and that "The Lean is full of garbage obviously, but compiles". ([X](https://x.com/__alpoge__/status/2124987173439209561))

## 24 Nov 2026: more checks, and a clarification {#nov-24}

- **24 Nov, 01:16 to 05:09 UTC.** On Robin1984 alone, the build passes at 01:16 UTC, con-leche accepts its statement comparison at 01:27 UTC, standalone Comparator v4.33.0 passes at 04:21 UTC, and `lake comparator` on Lean v4.36.0 passes at 05:09 UTC. Robin1984 is an independent formalisation of arithmetic criteria for RH and Dirichlet GRH. ([Sutherland](https://math.mit.edu/~drew/grh/#arithmetic-consequences))
- **24 Nov, 01:45 to 01:48 UTC.** An X user posts that he has "formally verified in Lean 4" that the proof is broken. His repository's README says it "does not claim that Alpöge's theorem is false"; its `Disproof.lean` imports only Mathlib and the repository's own file. ([X](https://x.com/JackyReaps/status/2125043056479240501), [repository](https://github.com/jackyreaps/X-files/tree/main/riemann-hypothesis))
- **24 Nov, 02:43 to 03:37 UTC.** The export combining Alpöge's proof with Robin1984 passes its arithmetic checks. Con-leche and con-ron match all three arithmetic statements at 02:43 and 03:08 UTC, respectively, and nanoda accepts the full combined export at 03:37 UTC. ([Sutherland](https://math.mit.edu/~drew/grh/#arithmetic-consequences))
- **24 Nov, 02:52 to 04:02 UTC.** In replies on X, Alpöge links Sutherland's page ("Still compiles"), says he used the word "garbage" too liberally, and says of the page-count joke "I should’ve cut it". ([X](https://x.com/__alpoge__/status/2125063891034186070), [X](https://x.com/__alpoge__/status/2125077588263465075))
- **24 Nov, 03:01 UTC.** Alpöge posts: "People seem to be reading this as me saying there’s something wrong with the proof. I’m pretty confused. No? It literally checked out days ago?" ([X](https://x.com/__alpoge__/status/2125062170207457583))
- **24 Nov, 04:17 UTC.** The Wall Street Journal links a profile of Alpöge on X; its post says "One day after the company’s IPO, an Anthropic employee says Claude helped discover a proof." (paywalled; we could not read the article. [X](https://x.com/WSJ/status/2125081353641222615))
- **24 Nov, 5:15 AM (no time zone stated).** WIRED publishes "AI Solved Math’s Most Famous Problem. Now Humans Are Struggling to Understand It" (Isabella Ward). ([WIRED](https://www.wired.com/story/ai-solved-maths-most-famous-problem/))
- **24 Nov, 05:25 UTC.** At that update, the original archive’s `lake comparator` run on Lean v4.36.0 had reached its final stage. [Completion on 25 November](#nov-25)
- **24 Nov, 10:08 UTC.** Carlos Toledo stops the `comparator` run of his independent audit after 53 hours for cost, with no verdict either way. His `con-leche` comparison matched all five theorems. ([Toledo](https://carlostoledo.co/reports/alpoge-grh.html))
- **24 Nov (date on the announcement).** Anurag Sahay, Will Sawin and Lior Silberman propose G.R.H. Polymath to coordinate work on Alpöge's Lean proof, develop a human-readable account of RH and Dirichlet GRH, and explore the mathematics behind the argument. ([G.R.H. Polymath announcement](https://terrytao.wordpress.com/2026/11/24/g-r-h-polymath/))

## 25 Nov 2026: original archive check {#nov-25}

- **25 Nov, 21:49 UTC.** Sutherland’s original-archive run of `lake comparator` on Lean v4.36.0 passes using the canonical challenge export. All five statements match, the axiom audit passes, and Lean’s paranoid kernel, nanoda and Lean’s default kernel accept. [MIT verification log](https://math.mit.edu/~drew/grh/)

For coverage and expert reactions, see [press](/press/). For the numbers, see [the proof in numbers](/proof-in-numbers/).
