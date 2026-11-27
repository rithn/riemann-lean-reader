---
title: "Riemann hypothesis proof FAQ: Claude, Lean, prize, crypto"
description: "Short, sourced answers to 24 common questions on the Lean proof of the Riemann hypothesis: who, how it was checked, how long, the prize and cryptography."
h1: "Frequently asked questions about the Lean proof of the Riemann hypothesis"
path: /faq/
target_queries:
  - did ai solve the riemann hypothesis
  - did claude solve the riemann hypothesis
  - who is levent alpöge
  - riemann hypothesis prize
  - what is lean riemann hypothesis
  - riemann hypothesis lean proof size
  - riemann hypothesis cryptography
  - generalized riemann hypothesis proof
structured_data: FAQPage
as_of: "28 Nov 2026"
---

# Frequently asked questions about the Lean proof of the Riemann hypothesis

*As of 28 Nov 2026. Each answer links to its source. For dates and the latest checks, see [status](/status/).*

### Has the Riemann hypothesis been solved?

Levent Alpöge released a Lean proof of the Riemann hypothesis on 20 Nov 2026. On 21 Nov the Lean FRO and the Mathlib Initiative certified that the statement and the proof are correct. Independent checkers compiled all 175,187 modules and replayed the proof through several kernels. Alpöge says he intends to write the argument up later.

Source: [Joint statement by the Lean FRO and the Mathlib Initiative](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

### What is the Riemann hypothesis?

It is a statement about the zeros of the Riemann zeta function. Apart from the "trivial" zeros at the negative even integers, and the point s = 1 where the function has a pole, every zero should have real part exactly 1/2. In Mathlib, the Lean library, this is the definition `RiemannHypothesis`.

Source: [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis)

### Did AI solve the Riemann hypothesis?

Levent Alpöge, who works at Anthropic, says he found the proof "working with Claude", and that Claude "far outpaced me near the finish line". He describes his own part as guiding the setup. Terence Tao wrote that Alpöge, "using an internal AI model, has generated an (enormous) Lean-only proof". Independent checker programs have accepted the Lean proof.

Source: [Alpöge's note](https://alpo.ge/remark.pdf) and [Tao's blog](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)

### What did Claude prove in August 2026?

In August 2026 Anthropic reported that Claude raised the proven share of nontrivial zeros on the critical line from 41.6% to 67.2%. Anthropic wrote that it did not expect those techniques to lead to a proof of the Riemann hypothesis. The November proof is a separate release by Levent Alpöge.

Source: [Anthropic, 10 Aug 2026](https://www.anthropic.com/research/riemann-zeta)

### Who is Levent Alpöge?

Levent Alpöge is a mathematician at Anthropic and a junior fellow of the Harvard Society of Fellows. His PhD thesis at Princeton was "Points on curves". His most recent paper, with Manjul Bhargava, Wei Ho and Ari Shnidman, solves Hilbert's tenth problem over all number fields. The one before it, with Brian Lawrence, gives a conditional algorithm for finding all rational or integral solutions of a polynomial equation in two variables.

Source: [Alpöge's website](https://alpo.ge/)

### Did Alpöge retract or apologise for the proof?

No. On 24 Nov at 03:01 UTC he wrote: "People seem to be reading this as me saying there’s something wrong with the proof. I’m pretty confused. No? It literally checked out days ago?" On 23 Nov he had said that the "250,000+ pages" figure was a joke and that the Lean code is "full of garbage" that still "compiles". Both posts are quoted on [status](/status/).

Source: [24 Nov post](https://x.com/__alpoge__/status/2125062170207457583), [23 Nov post](https://x.com/__alpoge__/status/2124987173439209561)

### What is Lean?

Lean is an interactive theorem prover based on dependent type theory, designed for use in cutting-edge mathematics and in software verification. Mathlib is a community-driven effort to build a unified library of mathematics formalized in Lean. Mathlib already contained the statement of the Riemann hypothesis, which the new proof uses.

Source: [Lean reference manual](https://lean-lang.org/doc/reference/latest/) and [Lean community](https://leanprover-community.github.io/)

### How do we know the proof is correct?

For the original archive, experts vetted Mathlib’s statement, the library compiled, multiple people reproduced the same export, and separate tools matched the statement and accepted the proof. MIT’s checks of Sernau’s readable and compact rewrites matched all five statements, audited their axioms and accepted both proof exports. Waterloo and Sho Sonoda report additional runs. [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) · [Shorter-edition checks by verifier](/status/#shorter-editions)

### Do mathematicians still need to confirm that the Lean code proves the real Riemann hypothesis? {#real-riemann-hypothesis}

No. On 21 Nov 2026 the Lean FRO and the Mathlib Initiative certified that the formal statement is the Riemann hypothesis as Mathlib states it. Two independent tools confirmed that the theorem proved in the Lean archive matches that statement. The [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) records those checks, and [How we know](/how-we-know/) explains how they were carried out.

What remains is to understand why the proof works. A readable mathematical account would explain the ideas in the argument and how they fit together. See [Publication and the Clay prize](/status/#publication-and-the-clay-prize) for the status of the write-up.

### Is the proof a tautology? (the `True` definitions) {#tautology}

Not in the sense the checkers test, but the objection has a true part. A condition named `anyGeometry` is defined as `fun _ _ _ => True`, which accepts every input, at [line 19 of `OverIx.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L19). The route from the main theorem reaches it, and Alpöge says the code is "full of garbage". A preprint by J. L. Nielsen grants that the code typechecks but argues its geometric part is a manufactured stand-in, so the argument is circular ("Riemann to Riemann"). The checkers' answer is about the theorem: it is stated with Mathlib's own definition of the Riemann hypothesis, two tools compared it with what was proved, and several independent checkers accepted the proof. A dummy definition inside a proof cannot make a checker accept a proof of the wrong statement. On MathOverflow, Chris Bailey wrote that "the definitions used in the proof are irrelevant as long as they produce a term of the correct type". Thomas Bloom (University of Manchester) made the same point on X: a vacuously true part of the proof "does not invalidate the proof". What is open is what the code means and where the mathematics sits.

#### The claim

J. L. Nielsen (Center for Topological Physics, Lawrence, Kansas) posted a preprint on PhilArchive, "The Invalidity of Alpöge’s Proof of the Riemann Hypothesis: Vacuous Truth in a Geometric Argument with a Custom Bundle Built to Match Zeta". ([preprint](https://philarchive.org/rec/NIEIOT-2)) It does not say the code fails to check. It says the geometric part of the argument is "a manufactured witness" (p. 1): a condition defined as `True`, a degenerate geometric model, lattice data copied from the analytic side, and a divisor height that is assigned a formula and then "verified" by `rfl`. Its conclusion: "The formal comparison is Riemann to Riemann, not an independent geometric derivation of Riemann." (p. 15) It states what it grants: "Although the type comparison succeeds, it does not supply the missing mathematical content" (p. 1), and "The defect identified here is structural rather than axiomatic" (p. 15). It also says the analytic estimates exist but "do not prove RiemannHypothesis on their own; they prove conditional bounds parameterized by the divisor datum" (p. 12). On compiling, it says both that "Remove the manufactured bundle, and the proof term does not compile" (p. 14) and that an empty `none` witness or "any other inhabitable filler" leaves the chain compilable, so that only a constant `False` blocks it (p. 3). The word "tautology" appears in its section 8, "The tautology in the height comparison"; the phrase "nested tautology" is not in it.

#### What is true in it

The code does define `anyGeometry` as `fun _ _ _ => True`, at [line 19 of `OverIx.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L19), and it is passed on as `geoCl anyGeometry` on the route from the main theorem. We checked the preprint's code claims in our copy of the source: the name occurs on 118 lines in 24 files (its figure); the zero map `iMj`, the degenerate model (`geoDegenerate`, `mdlJunk`, `divXFl`) and the height `ht := hExpl6 …` exist; and the six "extraction lemmas" it lists each appear once, at their own definition. It also concedes that `everyE₂` "is not the witness on the final everyCharacter route" (p. 3), which matches our reading. Toledo's audit adds another example: a theorem named `siegel_eisenstein_simple_pole` proves a statement defined as `True`. Alpöge calls the code "full of garbage" (see [status](/status/)). Three independent reads of the code ([Chu, 22 Nov](https://dev.to/frankchu/grh-proofs-geometry-is-fun-true-in-24-files-2n2b), [Toledo, 24 Nov](https://carlostoledo.co/reports/alpoge-grh.html), [dial481](https://github.com/dial481/riemann-hypothesis-rosetta/blob/main/results/anygeometry.md)) confirm the definition and its reach. We did not check its claims about the heights and the forty or so matrix estimates.

#### What the verifiers say

They agree with the preprint that the code checks; they say this makes the theorem proved whatever the intermediate definitions are.

- The theorem proved, `riemannHypothesis`, has the type of Mathlib's own `RiemannHypothesis`. The Lean FRO and Mathlib Initiative say two tools (`comparator` and `con-leche --compare`) confirmed that the theorem proved is exactly Mathlib's statement. ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))
- Several checkers accept the exported proof, using only the three standard axioms. ([Sutherland](https://math.mit.edu/~drew/grh/))
- Chris Bailey, the author of the nanoda checker according to another answer in the thread, wrote on MathOverflow on 23 Nov: "the definitions used in the proof are irrelevant as long as they produce a term of the correct type, and (2) comparator checks that the definitions used to construct the type (which do matter) match those used in the challenge." ([comment](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust#comment1354173_518119))
- Carlos Toledo's audit says the formal theorem "is decided by the kernels, not by the names", and that the preprint's title "goes further than its analysis". The preprint agrees on the first point: "ordinary definitions and lemmas suffice to typecheck the term without extra axioms or kernel errors" (p. 1). Toledo also reports a Lean proof that Mathlib's `RiemannHypothesis` is equivalent to the textbook statement about zeros in the critical strip. ([Toledo](https://carlostoledo.co/reports/alpoge-grh.html))
- Thomas Bloom (University of Manchester) wrote on X on 21 Nov at 19:21 UTC: "Finding a small part of the massive formal RH proof that is vacuously true, or where the definitions seem weird, does not invalidate the proof. It just means the proof is a little longer than it needs to be." ([post](https://x.com/thomasfbloom/status/2124221582105014284))
- Sutherland combined the proof with a separate formalisation of Robin's and Lagarias's criteria (Robin1984, by someone else) and checked two inequalities about divisor sums that do not mention the zeta function. They still rely on Mathlib's definitions of the divisor sum, exp, log and so on. ([Sutherland](https://math.mit.edu/~drew/grh/))

#### Other tests on X are not checks

Two repositories shared on 24 Nov are circulating. One claims a Lean "countermodel"; its own README says it "does not claim that Alpöge's theorem is false", and its `Disproof.lean` imports only Mathlib and the repository's own file, not the archive. ([repo](https://github.com/jackyreaps/X-files/tree/main/riemann-hypothesis)) The other reports that deleting the geometry field still builds; it says it did not rebuild upstream modules from source or replay the result, and we have not reproduced it. ([repo](https://github.com/mrnathanhumphrey-droid/levent-rh-proof-anygeometry-excision-test))

#### What remains open

Whether the code checks is not in dispute: the preprint grants it. What is in dispute is what the code means. Toledo's audit says whether the inputs that feed the key inequalities "carry the argument, and what they mean, is a question for number theorists, not for a kernel". There is no human-readable proof yet, Alpöge calls the code garbage, and no refereed paper has been announced. One independent audit, Toledo's, also reports that its own `comparator` run was stopped for cost after 53 hours with no verdict; its `con-leche` comparison matched all five theorems.

Source: [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [Bloom](https://x.com/thomasfbloom/status/2124221582105014284), [MathOverflow comment](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust#comment1354173_518119), [Toledo's audit](https://carlostoledo.co/reports/alpoge-grh.html)

### Has anyone disproved the proof in Lean?

No. On 24 Nov a user on X said he had "formally verified in Lean 4" that the proof is "mathematically broken on its live path". His repository's own README says it "does not claim that Alpöge's theorem is false". The file `Disproof.lean` imports only Mathlib and another file of the same repository, and works with copies of the archive's hypotheses that the repository itself defines as `True`. What it refutes is a lemma stated in that repository and left as `sorry`, not a theorem in Alpöge's archive. A second repository reports that deleting the `geo` field still builds; it has not been reproduced.

Source: [JackyReaps's repository](https://github.com/jackyreaps/X-files/tree/main/riemann-hypothesis), [excision test](https://github.com/mrnathanhumphrey-droid/levent-rh-proof-anygeometry-excision-test)

### Has the proof been peer reviewed?

The joint statement certifies four formal checks: the statement, compilation, statement matching and independent proof checking. A refereed paper has not been announced. The statement also says it looks forward to mathematical activity that will "help explain the new ideas in this proof".

Source: [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

### Did Claude just check its own proof?

Named people at several universities ran the checks, using independent checker programs, some written by third parties in other languages. Sutherland and Rubinstein used Claude Code to help run their checks, and the verdict comes from the checkers. Scott Aaronson wrote on 20 Nov that he saw "zero indications" of an AI exploiting a Lean bug.

Source: [Sutherland's verification page](https://math.mit.edu/~drew/grh/)

### How long is the proof?

The original archive has 175,187 Lean files and about 17.4 million physical lines. Sernau’s readable edition has about 477,000 physical lines, of which the release reports about 300,000 code lines. The compact edition has about 113,000 physical lines and about 76,000 code lines. These source totals exclude Mathlib. [Edition comparison](/shorter-riemann-hypothesis-proof/#size) · [Counting methods](/proof-in-numbers/#shorter-editions)

RH Shrink tracks the community cleanup of the original. Its figures use an import-excluding code-line rule and describe a separate branch from Sernau’s rewrite. [Community proof-size series](/proof-in-numbers/#community-proof-size)

### Is there a human-readable version of the proof?

Sernau’s readable Lean edition comes with a guide and comments. Its release says a full human read-through and accompanying paper are still outstanding. Alpöge released the original as Lean code with a four-page note, and Michael Rubinstein’s 265-page working draft for the zeta case (version 2, 22 Nov) traces inputs from that original. [Pinned readable guide](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md) · [Readable source route](/sernau/route/) · [Alpöge’s note](https://alpo.ge/remark.pdf) · [Rubinstein’s guide and versions](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)

### Is there a prize?

The Clay Mathematics Institute's rules for the Millennium Prizes say a proposed solution must be published in a qualifying outlet. At least two years must pass after publication, and the solution must have received general acceptance in the global mathematics community. Alpöge released his proof on 20 Nov 2026.

Source: [Clay Mathematics Institute rules](https://www.claymath.org/millennium-problems/rules/)

### What does it mean for cryptography?

Scientific American wrote that the result "won’t upend global banking or make the internet run faster". The security of RSA is related to the difficulty of factoring the product of two large primes, and Diffie–Hellman key exchange rests on the discrete logarithm problem. The proof concerns where the zeros of the zeta function and of Dirichlet L-functions lie.

Source: [Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/), [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem) and [Diffie–Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)

### What is the generalised Riemann hypothesis, and does the proof cover it?

It extends the same claim to Dirichlet L-functions, with the zeta function as the simplest case. The release proves it for all moduli and all Dirichlet characters. Alpöge writes that he expects the Extended Riemann Hypothesis to follow "with more time".

Source: [Sutherland's verification page](https://math.mit.edu/~drew/grh/)

### What is the quasi-Riemann hypothesis?

OpenAI's October 2026 result, the quasi-Riemann hypothesis, places all zeros in a vertical strip narrower than the known strip between 0 and 1. The first version used the strip from 1/8 to 7/8 and a later one 1/12 to 11/12. The November proof places the zeros on the critical line, where the real part is 1/2.

Source: [Quanta Magazine, 19 Oct 2026](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)

### What about the Masullo proof?

Alessandro Masullo's draft is a human-written claim of the generalised Riemann hypothesis, posted by Ravi Vakil on 20 Nov. About eight hours later Vakil added that several people had reported problems, found with the help of AI models. The draft is a separate claim from Alpöge's Lean proof.

Source: [Ravi Vakil's blog](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/)

### Can I check the proof myself?

Yes. The compact edition is the smaller project to build. Its authors estimate one to two hours on 12 cores with 24 GB of memory for the build, and a full checker run takes additional time and memory. The original build and the readable edition’s full checker run have their own resource requirements and published logs. [Compact walkthrough](/how-we-know/#verify-compact) · [MIT original checks](https://math.mit.edu/~drew/grh/) · [MIT shorter-edition checks](https://math.mit.edu/~drew/shortgrh/)

### What happens next?

Alpöge says he intends to understand the argument and explain it, and expects it to be "massively simplified, likely immediately". Terence Tao wrote that he imagines "the digestion process will take some time". The joint statement looks forward to mathematical activity that will help explain the new ideas in the proof.

Source: [Alpöge's note](https://alpo.ge/remark.pdf) and [Tao's blog](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)

### How have mathematicians reacted?

On 20 Nov James Maynard said "I suspect that the proof will turn out to be correct", and Andrew Sutherland said the chance that anything is fishy is "approximately zero". Andrew Granville called what Alpöge released "garbled". Terence Tao, Maynard and Tristan Buckmaster each said understanding it will take time. See [press](/press/).

Source: [Nature, 20 Nov 2026](https://www.nature.com/articles/d41586-026-03812-7) and [Scientific American](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/)

### How does the proof work?

Alpöge describes the argument as "a descendant of Stepanov’s", with multiplicity supplied by chaining theta lifts. Terence Tao wrote that, from very initial analysis, it "appears to use the full power of modern developments on the Langlands program and arithmetic geometry". Alpöge says he intends to write the argument up properly.

Source: [Alpöge's note](https://alpo.ge/remark.pdf) and [Tao's blog](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)

---

More: [status](/status/) · [how we know](/how-we-know/) · [what is the Riemann hypothesis](/what-is-the-riemann-hypothesis/) · [why it matters](/why-it-matters/) · [the proof's structure](/route/) · [browse the map](/list/)
