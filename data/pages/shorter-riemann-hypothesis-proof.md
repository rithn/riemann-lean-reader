---
title: "Luke Sernau’s shorter Lean proof of the Riemann hypothesis"
description: "Compare Alpöge’s original Lean archive with Luke Sernau’s readable and compact rewrites. Find all five statements, pinned source and independent checks."
h1: "Luke Sernau’s shorter Lean proof of the Riemann hypothesis"
path: /shorter-riemann-hypothesis-proof/
published: "2026-11-26"
as_of: "26 Nov 2026"
target_queries:
  - luke sernau riemann hypothesis proof
  - shorter riemann hypothesis proof lean
  - 76000 line riemann hypothesis proof
  - riemann hypothesis readable lean proof
  - grh compact lean verification
---

# Luke Sernau’s shorter Lean proof of the Riemann hypothesis

On 25 November 2026, Luke Sernau published two shorter Lean reworkings of the proof Levent Alpöge developed with Claude. Both establish the same five theorems as the original, covering classical RH and GRH for Dirichlet L-functions. Andrew Sutherland independently verified both shorter editions at commit `72fead10`. [Pinned release](https://github.com/lsernau/grh-lean/commit/72fead102f663d5c7a407964a13dc0cf9d977207) · [MIT verification](https://math.mit.edu/~drew/shortgrh/)

## Which edition should I open? {#which-edition}

- **Read the argument.** Start with the readable edition (`grh/`). The guide gives a reading order, and the Explorer’s source route follows the classical RH theorem to the result it uses. [Pinned reading guide](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md) · [Follow the Lean source](/sernau/route/) · [Readable map](/sernau/)
- **Build and check the smaller project.** Start with the compact edition (`grh-compact/`). Its proofs are written for brevity. [Pinned compact project](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact) · [Build and verification steps](/how-we-know/#verify-compact)
- **Trace the first release.** Use the original archive for Alpöge’s 20 November submission and the Explorer’s original cluster references. [Original map](/alpoge/) · [Pinned original mirror](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005) · [MIT original verification](https://math.mit.edu/~drew/grh/)

## How much shorter is it? {#size}

| Edition and source scope | Lean files | Physical lines including blanks | Nonblank lines including comments | Code lines reported by the rewrite |
|---|---:|---:|---:|---:|
| Alpöge–Claude original archive, `40e56bab/src` | 175,187 | 17,374,215 | 15,531,759 | — |
| Sernau readable, `72fead10/grh/src` | 803 | ≈477,000 | ≈433,000 | ≈300,000 |
| Sernau compact, `72fead10/grh-compact/src` | 794 | ≈113,000 | ≈95,000 | ≈76,000 |

Using physical lines across editions, the compact source is about **0.65%** of the original. These totals exclude the Mathlib dependency. The familiar 17.4 million figure counts physical lines, while 76,000 counts code lines. RH Shrink tracks a separate community branch with its own code-line rule. [Original archive figures](/proof-in-numbers/#release-figures) · [Readable README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#layout) · [Compact README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/README.md#layout) · [RH Shrink method](/proof-in-numbers/#community-proof-size)

## The five statements side by side {#five-statements}

Each source link opens the final declaration in that edition’s `Main.lean`. In the shorter projects, `Statements.lean` contains the four explicit proposition definitions and imports only Mathlib. The three Dirichlet statements use positive integer moduli. The half-plane and full critical-strip results cover every Dirichlet character, including imprimitive ones. [Pinned proposition definitions](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean) · [MIT’s fully elaborated statements](https://math.mit.edu/~drew/shortgrh/explicit-statements.out)

| Lean theorem | What it says | Original | Readable | Compact |
|---|---|---|---|---|
| `riemannHypothesis` | Mathlib’s classical RH. Every nontrivial zero of ζ has real part ½. | [L4](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4) | [L5](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L5) | [L4](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean#L4) |
| `riemannZeta_eq_zero_re` | If ζ(s) = 0, s differs from 1 and s is outside the negative even integers, then Re s = ½. | [L6](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L6) | [L8](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L8) | [L6](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean#L6) |
| `LFunction_ne_zero_of_half_lt_re` | L(s, χ) is nonzero for Re s > ½, with an exception at s = 1 for the principal character. | [L8](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L8) | [L13](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L13) | [L8](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean#L8) |
| `LFunction_eq_zero_re` | If L(s, χ) = 0 and 0 < Re s < 1, then Re s = ½. | [L10](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L10) | [L17](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L17) | [L10](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean#L10) |
| `LFunction_eq_zero_re_of_isPrimitive` | The same critical-strip statement restricted to primitive χ. | [L12](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L12) | [L21](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L21) | [L12](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean#L12) |

## What changed in the proof files? {#what-changed}

The rewrite follows Alpöge’s method, uses different arguments in some steps and reworks some ported background code. Sernau credits colleagues at Anthropic and Claude for the rewrite. The edition READMEs credit Claude with writing the Lean code and documentation. The release describes machine checks, with a full human read-through and accompanying paper still outstanding at release. [Pinned release README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/README.md) · [Readable acknowledgements](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#acknowledgements)

At the classical RH declaration, the original uses `rhOfAll`. Both shorter editions apply `New.zeta_zeros_on_line` to `New.grh`. The first name is the implication from Dirichlet nonvanishing to RH, using the functional equation for ζ. The second supplies the nonvanishing input. Follow the two names in the readable source and see the imports that connect their files. [Original declaration](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4) · [Readable implication](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L47) · [Readable nonvanishing](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L239) · [Explorer source route](/sernau/route/)

For a reading order that continues from these declarations into the main estimate, see the [readable edition section of Guides](/guides/#sernau-readable).

## What did independent checks confirm? {#verification}

On Lean v4.35.0, Sutherland’s sandboxed checks built both shorter projects, matched all five statements against the challenge, found only Lean’s three standard axioms and replayed the checked proofs with several kernels. The full paranoid Comparator run passed for the compact edition on two machines and for the readable edition on the larger machine. The other readable run was stopped at a memory threshold and has no verdict. The original archive has its own independent verification record and a 21 November joint certification covering classical RH. [MIT shorter-edition results](https://math.mit.edu/~drew/shortgrh/) · [MIT original results](https://math.mit.edu/~drew/grh/) · [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) · [Dated results](/status/#shorter-editions)
