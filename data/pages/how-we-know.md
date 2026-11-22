---
title: "How do we know the Riemann proof is correct? Lean explained"
description: "How a computer-checked proof works: the Lean kernel, independent checkers, statement matching and reproducible builds, applied to the Riemann proof."
h1: "How do we know the Riemann hypothesis proof is correct?"
path: /how-we-know/
target_queries:
  - how do they know the riemann hypothesis proof is correct
  - is the lean proof of the riemann hypothesis verified
  - can you trust a lean proof
  - riemann hypothesis lean verification
  - claude checked claude riemann proof
  - how does lean verify a proof
  - lean kernel soundness
as_of: "22 Nov 2026"
---

# How do we know the Riemann hypothesis proof is correct?

*As of 22 Nov 2026. See [status](/status/) for the latest.*

**A program called a kernel tests every step of a Lean proof against fixed logical rules. Several independent programs have repeated that check on the exported proof. People also confirmed that the theorem proved is the Riemann hypothesis as Mathlib states it. The proof runs to 17.4 million lines, so the checking is done by machine.**

This page explains how that works for a reader new to Lean. An "Expert detail" section at the end gives the numbers.

## A proof that a machine can check

Most proofs are written for people. A referee reads them and decides whether each step follows.

A Lean proof is written as code. Lean is "an interactive theorem prover based on dependent type theory, designed for use both in cutting-edge mathematics and in software verification." ([Lean reference manual](https://lean-lang.org/doc/reference/latest/)) Mathlib is "a community-driven effort to build a unified library of mathematics formalized in the Lean proof assistant." ([Lean community](https://leanprover-community.github.io/)) Lean checks each step against fixed logical rules. If a step does not follow, Lean rejects the file.

Kevin Buzzard's Xena Project blog put it this way on 12 Nov, before this proof appeared: "“It’s true because it’s checked in Lean” can be made to make sense. But one has to do some work beyond “the Lean code compiles”." ([Xena](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/))

His post lists four questions to ask of a Lean repository. The Lean and Mathlib communities' joint statement says all four are satisfied. ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)) They are the frame for this page.

## Question 1: what statement was checked?

Mathlib's own definition of the Riemann hypothesis, `RiemannHypothesis`. It is part of Mathlib, and the joint statement says it "has been carefully vetted by experts in Lean and number theory." In Lean:

```lean
def RiemannHypothesis : Prop :=
  ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2
```

In one sentence: every zero of ζ that is not a trivial zero (−2, −4, −6, …) and is not s = 1 has real part ½. The condition `s ≠ 1` is there because Mathlib assigns ζ a conventional value at its pole. ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/0df444a3/Mathlib/NumberTheory/LSeries/RiemannZeta.lean#L185), [Sutherland](https://math.mit.edu/~drew/grh/))

The generalised statement for Dirichlet L-functions is in a short file that imports only Mathlib. One of its theorems, in Lean:

```lean
theorem LFunction_eq_zero_re :
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),
    0 < s.re → s.re < 1 → DirichletCharacter.LFunction χ s = 0 → s.re = 1 / 2
```

In one sentence: for every modulus N and every Dirichlet character χ mod N, every zero of the L-function L(χ, s) with 0 < Re s < 1 has real part ½. ([Sutherland](https://math.mit.edu/~drew/grh/))

The statement in plain words is also on [what is the Riemann hypothesis](/what-is-the-riemann-hypothesis/).

## Question 2: does it compile?

Compiling means Lean reads every file and accepts it. All 175,187 files compile with zero errors. Andrew Sutherland at MIT and Michael Rubinstein at Waterloo reported this in detail. The joint statement says "dozens of people have reported correct compilation of the codebase, reproducing the same raw proof export file." ([Sutherland](https://math.mit.edu/~drew/grh/), [Rubinstein](https://mrubinst.github.io/grh-lean-verification/))

Compiling is the first check. The proof also uses custom tools that can put a result in place without Lean's front end checking it first. For those, the verification notes say "the kernel is the only check." That is why the fourth question matters. ([notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))

## Question 3: does the library prove that statement?

The codebase "depends directly only on Mathlib". The community also added a short file that states the Riemann hypothesis and imports only Mathlib. A comparison tool checks that the theorem proved in Alpöge's library is exactly that statement. Two independent tools did this, comparator and `con-leche --compare`, and both confirmed the match. Sutherland also reports a pass from `con-ron --compare`. ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [Sutherland](https://math.mit.edu/~drew/grh/))

## Question 4: does an independent check accept the proof?

Lean's kernel is the final check. In the reference manual's words: "The core type theory is implemented in a minimal kernel that does nothing other than check proof terms." Each tactic produces a term that the kernel checks, "so bugs in tactics do not threaten the soundness of Lean as a whole." ([Lean reference manual](https://lean-lang.org/doc/reference/latest/))

Lean is designed so that the same core theory can be checked by independently implemented kernels. ([external kernels](https://lean-lang.org/doc/reference/latest/External-Kernels/)) The community exported the proof to a plain file and ran such checkers on it. The joint statement lists:

- Lean's official kernel;
- two checkers called con-leche and con-ron;
- "several independent checkers contributed by third parties".

Con-leche and con-ron "come with a formal proof, relative to set theory, that they cannot accept a false proof." The statement says this addresses "concerns that Lean's logic itself might have flaws that the proof could exploit."

The checks ran on an "inert export of the proof, out of reach of hypothetical malicious code in the Lean proof sources." ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/))

## "Did Claude just check its own work?"

- The checks were run by named people at several universities and by independent programs. Sutherland's page publishes file sizes and hashes, so anyone can confirm they are checking the same proof. ([Sutherland](https://math.mit.edu/~drew/grh/))
- Sutherland and Rubinstein both used Claude Code to help run their checks. The verdict comes from the checker programs.
- Scott Aaronson wrote on 20 Nov: "I note that, so far, not one of the AI results with Lean certificates has needed to be retracted (while several without Lean certificates have needed to be)." ([Aaronson](https://scottaaronson.blog/?p=10344))

Buzzard wrote on 12 Nov: "There may in theory be more soundness bugs in Lean’s kernel. However, this does not matter." His reason is that there are many independent kernels. Aaronson says Lean "still has issues, from kernel bugs ... to uncertain soundness of the underlying type theory". He adds: "I see zero indications that that’s happening right now."

## What you have to trust

- **Lean's kernel, cross-checked by independently implemented kernels.** Independent implementations reduce "the risk of bugs that affect soundness" ([Lean reference manual](https://lean-lang.org/doc/reference/latest/)). Each of these accepted the proof ([Sutherland](https://math.mit.edu/~drew/grh/)). What each adds, from the manual's [list of external kernels](https://lean-lang.org/doc/reference/latest/External-Kernels/):
    - nanoda: an implementation of the Lean kernel in Rust, by Chris Bailey, developed independently of Lean.
    - lean4lean: a port of the official kernel to Lean, by Mario Carneiro. Significant parts of it are formally verified against a specification of Lean's type theory.
    - con-leche: an implementation of the Lean kernel in Lean, by the Lean FRO, with a machine-checked proof that every environment it accepts has a model in set theory, so it never accepts a proof of `False`.
    - con-ron: a port of con-leche to Rust, by the Lean FRO.
- **The three standard axioms.** The five theorems depend only on `propext`, `Classical.choice` and `Quot.sound`. The reference manual calls them "standard axioms of Lean's logic, and benign." ([Sutherland](https://math.mit.edu/~drew/grh/), [Lean reference manual](https://lean-lang.org/doc/reference/latest/ValidatingProofs/))
- **Mathlib's definitions** of ζ (`riemannZeta`) and of `RiemannHypothesis`, and, for the GRH theorems, of Dirichlet L-functions. ([Sutherland](https://math.mit.edu/~drew/grh/))
- **The hardware and the build.** A sandboxed `lake build` on a separate machine, with no network and a read-only source tree, produced an export byte-identical to the published one. Every check on the published export applies to it. ([Sutherland](https://math.mit.edu/~drew/grh/))

## Understanding the proof

The formal check shows the proof is valid. Understanding why it holds is the work ahead.

- Sutherland: "There is much work to be done to understand the mathematical details of the proof." ([Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/))
- Maksym Radziwiłł, whom Alpöge's note thanks by name: "The object of mathematics as the rest of science is really the question ‘why?’ and this doesn’t answer it at all." ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- Aaronson: mathematicians "won’t be satisfied with 17 million lines of Lean". ([Aaronson](https://scottaaronson.blog/?p=10344))

The joint statement says it looks forward to "all the activity in the mathematical community that will help explain the new ideas in this proof." Alpöge says he intends to write the argument up. See [status](/status/) and [press](/press/).

## What the map adds

The map shows the shape of what was checked.

- The proof is 175,187 files, 175,027 of them on the map, in 2,647 clusters and 63 themes.
- The longest import chain is 203 files. The median file is 13 imports from `Main`, and the farthest is 43.
- By distance from the main-theorem cluster, the clusters fall into depth bands 0 to 8, with 1, 3, 22, 437, 1,443, 637, 76, 25 and 3 clusters.

See [how the proof is structured](/route/), the [main theorem's cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/) and the [full list](/list/). To learn the background, start with the [learning path](/learn/).

## Expert detail

**Statement.** Mathlib defines:

The release proves `riemannHypothesis : RiemannHypothesis` (see question 1) and the same statement in its own wording, which Lean accepts as equal by definition. It also proves three theorems on Dirichlet L-functions. The proof is written without hypotheses: `Main.lean` proves `riemannHypothesis` as `Formalism.VW.rh_of_every allChi`, where `allChi` says no Dirichlet L-function vanishes for Re s > 1/2. ([Sutherland](https://math.mit.edu/~drew/grh/), [notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))

**Axioms.** `propext`, `Classical.choice`, `Quot.sound` only. The environment has 15 axioms, all in `Init`. A static scan finds no `axiom`, `sorry`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `debug.*` or `skipKernelTC`. ([notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md))

**Custom metaprogramming.** The source defines tactics `kexactB` and `kcopy`, a command that copies declarations, and uses `run_tac` 33 times. For proofs made this way, "the elaborator has not checked the term against the goal, so the kernel is the only check."

**Builds.**
- Lean v4.33.1 and Mathlib v4.33.1. 175,187 of 175,187 modules compile. 8,322 Mathlib and 378 dependency `.olean` files match the official cache byte for byte.
- A sandboxed `lake build Main` (no network, read-only source) on a separate machine passes, and the export it makes is identical to the published one.
- Across two builds, 175,186 of 175,187 compiled files were byte-identical. One module is non-deterministic: a 38-byte difference in a bound variable name (Lean issue #15498, fixed in v4.36.0). The export is unaffected.
- A plain `lake build` was estimated at roughly 17 hours. Rubinstein's distributed build took 3 h 18 min. Checking needs roughly 100 GB of RAM and 70 GB of disk with Lean v4.36.0 and the exports.
- The notes say "The judging is done by Lean 4.36.0 and independent checkers." A pass by the 4.33.1 kernel alone "counts as limited evidence here."
- The community's public build cache "includes outputs from untrusted pull requests and volunteer machines. Download integrity checks do not verify proofs."

**Checkers.**
- `leanchecker` kernel replay: 175,187 of 175,187, zero rejections.
- nanoda (Rust): exit 0 in 27 min 42 s on 80 threads (Sutherland). Rubinstein's run: 1,484,729 declarations, no typechecker errors.
- con-leche in `--verified` mode: 1,468,418 declarations in 3 min 15 s on 64 threads.
- con-leche and con-ron `--compare`: all five theorems "justified by the solution".
- lean4lean: accepts every compiled module. Five needed a raised step limit on `decide +kernel` computations.
- Declaration counts differ by tool. We quote each with its checker.
- `comparator.json` names only Lean paranoid and nanoda. The bundled con-leche and con-ron refuse a mutual inductive block that has a reflexive member, and built from master they accept. The bundled v4.36.0 binaries "declined (exit 2, not a rejection)".

**Hashes.**
- Submission archive (14 parts joined): 239,275,554 bytes, SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`.
- Proof export: 61,570,595,788 bytes unpacked (7,699,933,588 compressed), SHA-256 beginning `5ea74b91`.
- Challenge export: 350,862,970 bytes, SHA-256 `bd484ac9886a96f26b1d9a7a59ebd45b7a70d102c015d4f31f9302bbdd6ab2b9`. It equals the one built by continuous integration in Deicyde/riemann-hypothesis.

**Cross-check outside Mathlib's zeta function.** Sutherland combined the proof with kimihiro64/Robin1984, an independent formalisation of Robin's and Lagarias's criteria, which are equivalent forms of the Riemann hypothesis. The combination gives Robin's inequality for the divisor sum for n > 5040 and Lagarias's inequality for n > 0 as theorems with no hypotheses. This is Sutherland's addition to the release. ([Sutherland](https://math.mit.edu/~drew/grh/), [Lagarias](https://arxiv.org/abs/math/0008177), [Robin's theorem](https://mathworld.wolfram.com/RobinsTheorem.html))

**Size.** Every file is imported by `Main`. The theorem's dependency closure is 1,478,198 declarations, and Rubinstein notes that many statements in the 175,187 files are "parallel or earlier formulations that it never uses". ([Rubinstein](https://mrubinst.github.io/grh-lean-verification/))

**Mirror.** The community repository's first commit, `40e56bab`, is the unmodified submission. Later clean-up removed 10,724 files, leaving 164,464 `.lean` files with `Challenge.lean`. Our "175,187 files" refers to the original archive.

Primary sources: [Sutherland](https://math.mit.edu/~drew/grh/), [Rubinstein](https://mrubinst.github.io/grh-lean-verification/), [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md), [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/).
