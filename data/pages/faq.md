---
title: "Riemann hypothesis proof FAQ: Claude, Lean, prize, crypto"
description: "Short, sourced answers to 20 common questions on the Lean proof of the Riemann hypothesis: who, how it was checked, how long, the prize and cryptography."
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
as_of: "22 Nov 2026"
---

# Frequently asked questions about the Lean proof of the Riemann hypothesis

*As of 22 Nov 2026. Each answer links to its source. For dates and the latest checks, see [status](/status/).*

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

### What is Lean?

Lean is an interactive theorem prover based on dependent type theory, designed for use in cutting-edge mathematics and in software verification. Mathlib is a community-driven effort to build a unified library of mathematics formalized in Lean. Mathlib already contained the statement of the Riemann hypothesis, which the new proof uses.

Source: [Lean reference manual](https://lean-lang.org/doc/reference/latest/) and [Lean community](https://leanprover-community.github.io/)

### How do we know the proof is correct?

Four checks were made. The statement is Mathlib's, which experts vetted. The library compiles, and dozens of people reproduced the same proof export. Two tools confirmed that the theorem proved is exactly Mathlib's statement. Lean's kernel and independent checkers, written in different languages, accepted the exported proof.

Source: [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

### Has the proof been peer reviewed?

The joint statement certifies four formal checks: the statement, compilation, statement matching and independent proof checking. A refereed paper has not been announced. The statement also says it looks forward to mathematical activity that will "help explain the new ideas in this proof".

Source: [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

### Did Claude just check its own proof?

Named people at several universities ran the checks, using independent checker programs, some written by third parties in other languages. Sutherland and Rubinstein used Claude Code to help run their checks, and the verdict comes from the checkers. Scott Aaronson wrote on 20 Nov that he saw "zero indications" of an AI exploiting a Lean bug.

Source: [Sutherland's verification page](https://math.mit.edu/~drew/grh/)

### How long is the proof?

The submitted archive has 175,187 Lean files and 17,374,215 lines, about 17.4 million, in 1,030,531,854 bytes of source. The accompanying note is four pages. The main theorem's dependency closure is 1,478,198 declarations. For scale, Mathlib is about 2 million lines.

Source: [Verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md) for the files, lines and bytes; [Rubinstein](https://mrubinst.github.io/grh-lean-verification/) for the dependency closure and the size of Mathlib

### Is there a human-readable version of the proof?

Alpöge released the proof as Lean code with a four-page note. He wrote "I decided to only present Lean" and says he intends to write the argument properly later. Michael Rubinstein has posted a 164-page working draft for the zeta case, which takes one key inequality from the Lean code.

Source: [Alpöge's note](https://alpo.ge/remark.pdf)

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

The source is public. A plain build was estimated at roughly 17 hours, and Rubinstein's distributed build took 3 h 18 min on shared university servers. Checking needs roughly 100 GB of RAM and 70 GB of disk. The community repository says its build cache includes outputs from untrusted pull requests and volunteer machines.

Source: [Community repository](https://github.com/leanprover-community/riemann-hypothesis)

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
