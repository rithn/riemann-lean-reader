---
title: "What is the Riemann hypothesis? Simple, student, expert"
description: "The Riemann hypothesis at three levels: simple, student (zeta zeros, critical line) and expert (precise statement, GRH for Dirichlet L-functions)."
h1: "What is the Riemann hypothesis?"
path: /what-is-the-riemann-hypothesis/
target_queries:
  - what is the riemann hypothesis
  - riemann hypothesis eli5
  - what is the riemann hypothesis in simple terms
  - riemann hypothesis for kids
  - riemann hypothesis explained
  - riemann zeta function zeros critical line
  - generalized riemann hypothesis
  - riemann hypothesis statement
as_of: "29 Nov 2026"
---

# What is the Riemann hypothesis?

*As of 29 Nov 2026. Pick the level that suits you: [Simple](#simple) · [Student](#student) · [Expert](#expert).*

**The Riemann hypothesis is a claim about where a famous function, the Riemann zeta function, equals zero. It says that every "non-trivial" zero lies on one straight line.** A Lean-checked proof was released on 20 Nov 2026. See [status](/status/) for what was checked.

Alpöge’s original release includes Lean code and a four-page note. Sernau’s two shorter rewrites prove the same statements. [How the proof was checked](/how-we-know/) · [Compare the editions](/shorter-riemann-hypothesis-proof/)

## Simple {#simple}

*For a curious 12-year-old, or anyone who wants the idea without formulas.*

**Primes.** A prime is a whole number bigger than 1 that you can only divide evenly by 1 and by itself. 2, 3, 5, 7 and 11 are primes. 4 is not, because 2 times 2 makes 4.

**A machine called zeta.** Mathematicians have a function called the Riemann zeta function. Think of it as a machine. You feed in a point on a flat sheet, and it hands back another point. For some inputs it hands back exactly zero. Those inputs are called the *zeros*.

**How primes and zeta are connected.** The zeta function can be built entirely out of the primes. For inputs far enough along the sheet, multiply together one simple factor for each prime, one for 2, one for 3, one for 5 and so on, and you get zeta. Euler found this in 1748. In 1859 Riemann went further. He wrote down a formula for the number of primes up to any limit, and the formula is built from the zeros of zeta. ([Bombieri, Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))

**Why the zeros control the primes.** Gauss noticed that the number of primes up to a number x is close to a smooth, simple curve. The real count wobbles around that curve. The zeros decide how big the wobble can be. The Riemann hypothesis is equivalent to saying the wobble stays small, about the size of the square root of x. If it failed, Bombieri writes, that "would create havoc in the distribution of prime numbers". ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))

**Where the zeros are.** Some zeros are boring. They sit at known places on the sheet: -2, -4, -6, and so on. The other zeros lie inside a strip of the sheet between 0 and 1. The Riemann hypothesis says every one of those zeros sits exactly on the line down the middle of the strip. That is the line at 1/2. Computers have found the first 103,800,788,359 of them, and all have real part 1/2. ([LMFDB](https://www.lmfdb.org/zeros/zeta/))

{{figure:zeros}}

**Why it is hard.** A proof has to show that no zero anywhere strays off the line, even by a tiny amount.

**What happened in November 2026.** On 20 Nov 2026 a mathematician called Levent Alpöge released a proof written in Lean. Lean is a proof assistant: a program that checks mathematics step by step. ([Lean reference manual](https://lean-lang.org/doc/reference/latest/)) On 21 Nov the Lean FRO and the Mathlib Initiative said it had been checked and that it is correct. The proof is 17.4 million lines of code, and Alpöge says he intends to write it up for readers later. Read more on [how we know it is right](/how-we-know/) and on [why it matters](/why-it-matters/).

## Student {#student}

*For high school or early undergraduate level. You know complex numbers.*

**The zeta function.** For a complex number s = σ + it with real part σ greater than 1, the zeta function is the sum

ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + …

It extends to the whole complex plane as a function with a single simple pole, at s = 1, with residue 1. ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)) Mathlib proves the series formula for 1 < Re(s) and notes that "when re s ≤ 1 the sum is divergent, and we use a different definition to obtain the analytic continuation to all s." Mathematically ζ(s) is undefined at s = 1, and Mathlib assigns it a conventional value there. ([Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html))

**The link to primes.** For σ > 1 the sum can be rewritten as a product over the primes, the Euler product:

ζ(s) = ∏ over primes p of 1 / (1 − p^(−s))

Euler gave it in 1748. ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))

**Zeros and counting primes.** Gauss observed that the number π(x) of primes up to x is well approximated by Li(x), the integral of 1/log t from 0 to x. Riemann's 1859 memoir gave a formula for the number of primes up to a limit in terms of the zeros of ζ. The Riemann hypothesis is equivalent to π(x) = Li(x) + O(√x log x). ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))

**Trivial and non-trivial zeros.** The zeros at s = -2, -4, -6, … are called trivial. The Lean statement excludes them in the form `¬∃ n : ℕ, s = -2 * (n + 1)`. All other zeros are non-trivial, and they lie in the *critical strip*, where 0 < Re(s) < 1. Quanta Magazine calls this "the known strip between zero and 1". ([Quanta](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/))

**The hypothesis.** Every non-trivial zero has real part exactly 1/2. The vertical line Re(s) = 1/2 is the *critical line*. ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))

{{figure:zeros}}

**In Mathlib's words.** The Lean library Mathlib states it as: for every complex s with ζ(s) = 0, if s is not a trivial zero and s ≠ 1, then Re(s) = 1/2. ([Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis))

**Where this sits on the original map.** The main theorem is in the cluster ["Explicit formula, Perron kernel and zero-free conditions for Dirichlet L-functions"](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/). The clusters nearest to it are all classical number theory: [zero-free region for zeta and Dirichlet L-functions](/cluster/k0680-zero-free-region-for-zeta-and-dirichlet-l-functions/), [primes in progressions, Siegel–Walfisz and the exceptional zero](/cluster/k0683-primes-in-progressions-siegel-walfisz-and-exceptional-zero/) and [Mertens-type estimates and zero sums for Dirichlet L-functions](/cluster/k0694-mertens-type-estimates-and-zero-sums-for-dirichlet-l/). Cluster titles on the map were drafted by AI.

> **Visual B (to build): "Walking along the critical line".** A slider for t. Left panel: the point ζ(1/2 + it) traced as a curve in the plane as t increases. The curve passes through the origin at each zero. Right panel: the critical strip with a marker moving up the line Re(s) = 1/2 and a dot dropped at each zero found so far. Add a toggle to show a line at, say, Re(s) = 0.6 with the label "The hypothesis puts every zero on the middle line." Compute values client-side and check the zero heights against the [LMFDB list](https://www.lmfdb.org/zeros/zeta/).

## Expert {#expert}

*For readers who know the analytic theory of L-functions.*

**Statement.** The release proves Mathlib's definition:

`def RiemannHypothesis : Prop := ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2`

The clause `s ≠ 1` is there "because Mathlib assigns ζ a conventional value at its pole." Bombieri's Clay description gives the usual form: the zeros at −2, −4, … are the trivial zeros, and "the nontrivial zeros of ζ(s) have real part equal to ½". ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)) The release also proves `riemannZeta_eq_zero_re`, the same statement in the submission's own words, which Lean accepts as equal by definition. ([Sutherland](https://math.mit.edu/~drew/grh/))

{{figure:zeros}}

**Generalised Riemann hypothesis for Dirichlet L-functions.** The release has three further theorems:

- `LFunction_ne_zero_of_half_lt_re`: for every modulus N ≥ 1 and every Dirichlet character χ mod N, primitive or not, L(χ, s) ≠ 0 whenever Re(s) > 1/2, except for the trivial character at s = 1.
- `LFunction_eq_zero_re`: every zero of a Dirichlet L-function with 0 < Re(s) < 1 has Re(s) = 1/2.
- `LFunction_eq_zero_re_of_isPrimitive`: the same for primitive characters, "the form in which the Generalized Riemann Hypothesis for Dirichlet L-functions is usually stated".

The Riemann hypothesis is the case N = 1. The proof of `riemannHypothesis` goes through the statement that no Dirichlet L-function vanishes for Re(s) > 1/2, and the theorems are stated without hypotheses. ([Sutherland](https://math.mit.edu/~drew/grh/), [Rubinstein](https://mrubinst.github.io/grh-lean-verification/), [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))

**Scope.** The proof covers the Riemann hypothesis and GRH for Dirichlet L-functions: all moduli and all characters. Alpöge writes that he expects, "with more time", the Extended Riemann Hypothesis too. ([note](https://alpo.ge/remark.pdf))

**Equivalent forms.** Robin proved in 1984 that his inequality for the divisor sum, σ(n) < e^γ n log log n, holds for all n > 5040 if and only if the Riemann hypothesis is true ([Robin, J. Math. Pures Appl. 63 (1984), 187–213](https://mathworld.wolfram.com/RobinsTheorem.html), as cited by MathWorld). Lagarias showed in 2002 that the Riemann hypothesis is equivalent to a sequence of elementary inequalities involving the harmonic numbers, a modification of Robin's criterion ([Lagarias](https://arxiv.org/abs/math/0008177)). Another equivalent form is π(x) = Li(x) + O(√x log x). ([Bombieri](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf))

Sutherland ran a cross-check that avoids Mathlib's ζ. Combined with an independent formalisation of Robin's work, the proof gives Robin's inequality for n > 5040 and Lagarias's inequality for n > 0 as hypothesis-free theorems. This was Sutherland's addition to the release. ([Sutherland](https://math.mit.edu/~drew/grh/))

**What the author says about the method.** Alpöge describes the argument as "a descendant of Stepanov’s", with multiplicity supplied by chaining theta lifts. In his note, Claude's suggested chain length for a von Mangoldt sum of length X was √X. Terence Tao wrote that "from very initial analysis" it "appears to use the full power of modern developments on the Langlands program and arithmetic geometry". ([note](https://alpo.ge/remark.pdf), [Tao](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/))

**The nine fields on the original map.** The Explorer groups the original archive’s 63 themes into nine fields. The shares are of the 175,027 mapped files. The grouping is our own and is AI-drafted.

| Field | Files | Share | What it covers |
|---|---|---|---|
| Automorphic forms | 36,120 | 20.6% | Highly symmetric functions and the matrix-group representations they generate |
| Abelian varieties | 34,614 | 19.8% | Abelian varieties, their moduli, degenerations and complex multiplication |
| Theta & Siegel–Weil | 26,433 | 15.1% | Theta lifts and the Siegel–Weil formula |
| Heights & Arakelov | 22,273 | 12.7% | Arithmetic size of points and objects, arithmetic intersection numbers |
| Lattices & mass | 16,495 | 9.4% | Counting and measuring lattices, mass formulas and local densities |
| p-adic Hodge theory | 16,172 | 9.2% | p-adic Galois symmetries acting on geometric objects |
| Harmonic analysis | 9,315 | 5.3% | Fourier transforms, wave and heat operators, estimates on matrix and Lie groups |
| Algebraic geometry | 7,941 | 4.5% | Scheme theory and cohomology |
| Classical number theory | 5,664 | 3.2% | Primes, ideals, class field theory, Hecke characters and L-functions |

Classical number theory is the smallest field by size, but it holds the main theorem and every cluster at depth 1 or less. By import distance from the main-theorem cluster, the 2,647 clusters fall into depth bands 0 to 8, with 1, 3, 22, 437, 1,443, 637, 76, 25 and 3 clusters. See [how the proof is structured](/route/).

## Keep going

- [Status](/status/): what has been released, checked and claimed.
- [How we know](/how-we-know/): how a computer-checked proof works.
- [Why it matters](/why-it-matters/): what follows from the proof.
- [Learning path](/learn/): where to start reading, by level.
- [Browse the original themes and clusters](/list/)
- [Trace the statement in the readable edition](/sernau/route/)
- Bernhard Riemann’s 1859 paper, [On the Number of Prime Numbers less than a Given Quantity](https://mellow-atlas-vp47.here.now), in D. R. Wilkins’s English translation, in a web edition with linkable sections.
- [What is the Riemann hypothesis? A guide to the famed conjecture that rules prime numbers](https://www.nature.com/articles/d41586-026-03854-x), by Davide Castelvecchi (Nature, 25 Nov 2026).
