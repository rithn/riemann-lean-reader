---
title: "Why the Riemann hypothesis matters: primes and proof"
description: "What follows from the Riemann hypothesis: primes, named results in number theory, cryptography and what a formal proof means for mathematics."
h1: "Why does the Riemann hypothesis matter?"
path: /why-it-matters/
target_queries:
  - why is the riemann hypothesis important
  - riemann hypothesis implications
  - riemann hypothesis consequences
  - riemann hypothesis cryptography
  - what if the riemann hypothesis was solved
  - what is the riemann hypothesis used for
  - riemann hypothesis solved what does it mean
as_of: "22 Nov 2026"
---

# Why does the Riemann hypothesis matter?

*As of 22 Nov 2026. The proof's status is on the [status page](/status/).*

**With the proof certified in Lean, the Riemann hypothesis is a theorem. Results that were stated "assuming the Riemann hypothesis" no longer need the assumption.**

For the claim itself, see [what is the Riemann hypothesis](/what-is-the-riemann-hypothesis/).

## For primes and number theory

**In one line.** Mathematicians have long asked "what if the Riemann hypothesis is true?" and worked out what would follow. A proof turns those "what ifs" into facts.

**Student level.** Many theorems in number theory carry a condition: "assume the Riemann hypothesis" or "assume the generalised Riemann hypothesis". Named examples:

- Miller's deterministic polynomial-time primality test, which Miller showed in 1976 runs in polynomial time if GRH holds. ([GRH article](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis), [Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))
- Chowla's 1934 result that, if GRH holds, the first prime in the arithmetic progression a mod m is at most K·m²·log(m)² for some fixed constant K. ([GRH article](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis))
- Hooley's 1967 result that GRH implies Artin's conjecture on primitive roots. ([GRH article](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis))
- The error term for counting primes: the Riemann hypothesis is equivalent to π(x) = Li(x) + O(√x log x). ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))

With the proof, each of these stands on its own for the cases the proof covers.

**Expert level.** The conditional results that become unconditional are those that assume RH or GRH for Dirichlet L-functions. Alpöge expects the Extended Riemann Hypothesis to follow "with more time". ([Sutherland](https://math.mit.edu/~drew/grh/), [Alpöge](https://alpo.ge/remark.pdf))

One concrete example from the checks: Sutherland combined the proof with an independent formalisation of Robin's work. The combination gives Robin's inequality for the divisor sum for n > 5040, and Lagarias's inequality for n > 0, as theorems with no hypotheses. This is Sutherland's addition to the release. ([Sutherland](https://math.mit.edu/~drew/grh/))

## What the proof may teach

Mathematicians commented on the proof's ideas on 20 Nov, before the 21 Nov certification. Each comment is conditional.

- **Hector Pasten** (Pontifical Catholic University of Chile): "If the proof is correct and understood, this completes a dictionary between different branches of math where the connections were only partial," ... "something like a Rosetta Stone." ([Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/))
- **Carlo Pagano** (Concordia University): "If true, ... it is very plausible to me that the new ideas in the proof will open up brand new avenues of thinking in number theory". (same article)
- **Terence Tao** (UCLA): from "very initial analysis", the proof "appears to use the full power of modern developments on the Langlands program and arithmetic geometry". ([Tao's blog](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/))
- **James Maynard** (Oxford): "assuming we do get the corresponding understanding, this will surely be viewed as one of the absolute pinnacles of mathematical results". ([Nature](https://www.nature.com/articles/d41586-026-03812-7))

On the original map, the archive’s files fall into nine fields. Classical number theory, the field that holds the main theorem, is 3.2% of the mapped files. Automorphic forms (20.6%) and abelian varieties (19.8%) are the two largest. See [the nine fields](/what-is-the-riemann-hypothesis/#expert) and [how the proof is structured](/route/).

## Cryptography

Scientific American wrote that the result "won’t upend global banking or make the internet run faster." ([Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/)) The security of RSA is related to the difficulty of factoring the product of two large primes. ([RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem)) Diffie–Hellman key exchange rests on the discrete logarithm problem. ([Diffie–Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)) The proof concerns where the zeros of the zeta function and of Dirichlet L-functions lie.

## What a formal proof means for mathematics

**A new kind of evidence.** The proof is checked by programs, not read by referees. Scott Aaronson noted that "not one of the AI results with Lean certificates has needed to be retracted (while several without Lean certificates have needed to be)". ([Aaronson](https://scottaaronson.blog/?p=10344)) Kevin Buzzard wrote on 12 Nov, before this proof appeared, that "It’s true because it’s checked in Lean" can make sense, with work beyond "the Lean code compiles". ([Xena](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)) See [how we know](/how-we-know/).

**Understanding the proof.** Mathematicians say the next step is to understand why it holds.

- Andrew Sutherland (MIT), who ran the main verification, wrote: "There is much work to be done to understand the mathematical details of the proof ... But perhaps the single most important step in the proof was building a machine that can think." ([Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/))
- Maksym Radziwiłł (NYU): "The object of mathematics as the rest of science is really the question ‘why?’ and this doesn’t answer it at all." ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- Youness Lamzouri (University of Lorraine): "Mathematics is mainly about understanding why something is true". He says we need to understand the ideas "well enough to explain them, teach them and build on them". ([IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof))
- The Association for Human Mathematics, 20 Nov: the announcement "foregrounds technical validity of logical statements over accountability, clarity, accessibility, and understanding." ([AHM](https://www.ahmath.org/statements))

**What happens next.** Alpöge says he intends "to understand and impart understanding of this argument", and he expects it to be "massively simplified, likely immediately". His note says he is "presenting the world with a complete argument before having mastered a massive neighbourhood around its mathematics." Tao wrote: "in this case at least we have a human author to communicate with". ([note](https://alpo.ge/remark.pdf), [Tao](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/))

**Size.** The original archive is 17.4 million physical lines in 175,187 files. Every file is imported by `Main`, and the main theorem's dependency closure is 1,478,198 declarations. Many statements are "parallel or earlier formulations that it never uses". On our map the median file is 13 imports from `Main`, the farthest is 43, and the longest import chain is 203 files. The [main theorem's cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/) is a good place to start. ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))

## See it in the map

- [Original proof structure](/route/)
- [Readable path from classical RH to the Dirichlet nonvanishing theorem](/sernau/route/)
- [The main theorem's cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/)
- [Browse every cluster](/list/)
- [A reading path by level](/learn/)
