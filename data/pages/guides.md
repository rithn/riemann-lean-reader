---
title: "Guides to the Lean proof of the Riemann hypothesis"
description: "Start reading the Lean proof in Sernau’s readable edition, or browse outside guides and checks for Alpöge’s original archive."
h1: "Guides to the Lean proof of the Riemann hypothesis"
path: /guides/
target_queries:
  - riemann hypothesis proof explained
  - alpöge riemann hypothesis proof guide
  - riemann hypothesis lean proof explained
  - riemann hypothesis lean proof blueprint
  - who verified the riemann hypothesis proof
  - riemann hypothesis lean proof reading guide
as_of: "26 Nov 2026"
---

# Guides to the Lean proof of the Riemann hypothesis

*As of 26 Nov 2026. The original guide entries record the versions read.*

## Sernau readable {#sernau-readable}

New to RH? Start with the [plain-English introduction](/what-is-the-riemann-hypothesis/#simple).

Start with the conclusion, then work back to the estimate that the argument needs. These links follow `grh/`, the readable edition of Luke Sernau’s rewrite of Levent Alpöge’s proof, at revision `72fead10`. The Explorer adapted this reading order with AI assistance from the upstream documentation, which credits Claude for the Lean text and documentation. [Release README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/README.md) · [Readable edition README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md)

1. **Read what Lean proves.** Start with the five declarations in `Main.lean`. Open `Statements.lean` when a declaration points to a named proposition and you want to see its exact hypotheses and conclusion. [Open Main in the reader](https://riemannhypothesissolved.com/sernau/file/Main#riemannHypothesis) · [Pinned Statements.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean) · [Five statements in plain English](/shorter-riemann-hypothesis-proof/#five-statements)
2. **Follow classical RH back one step.** The Explorer’s route starts at `riemannHypothesis` and shows the implication used there and the `New.grh` result it calls. The latter says the Dirichlet L-function is nonzero when the real part is greater than ½, with the pole at 1 excepted for the principal character of each modulus. [Route from Main](/sernau/route/) · [Open New.grh in the reader](https://riemannhypothesissolved.com/sernau/file/New.Reduction.OneSidedBound#New.grh)
3. **Find the estimate behind that result.** In `OneSidedBound.lean`, the argument uses `star_inequality` to help bound a remainder in a weighted sum over primes. Start with the top comment of `MainInequality.lean` for a list of the inputs and which terms cancel. The results index connects those inputs to Theorems A, B and C in the upstream guide. [Pinned MainInequality.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean) · [Results index](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/INDEX.md#the-last-step)
4. **Look up a file or unfamiliar term.** Use the contents to see how `New/` groups the steps of the argument and how `Lib/` groups background results. The upstream guide gives a fuller reading order and a glossary that pairs mathematical terms with Lean names. [File contents](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/CONTENTS.md) · [Upstream reading guide](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md)

## Sernau readable · Outside guides {#sernau-outside-guides}

{{readable_guides}}

## Sernau compact {#sernau-compact-guides}

[Pinned compact source at 72fead10](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact) · [Shorter-edition verification](/status/#shorter-editions)

{{compact_guides}}

## Alpöge original {#alpoge-original}

Map links and node counts refer to the original archive. [Verification status](/status/)

{{guides}}

## Other tools

- **riemann.world.** [riemann.world](https://riemann.world/) is a zoomable map of the same Lean files, with their declarations and source. The site does not state its author.

## Suggest a guide

Post to [@SomTheBuilder](https://x.com/SomTheBuilder) on X with the link. We list public guides from named authors or consistent public handles. Authors can ask us to correct how their guide is described.

## Changelog

- **23 Nov 2026.** First version, with 11 guides.
- **24 Nov 2026.** One list of 10 guides instead of two groups. Nine have their own page, with links to the nodes of the map they cite.
- **24 Nov 2026, evening.** 13 more guides, 23 in all, 22 with their own page. A guide is labelled "AI-assisted" when its author says AI helped make it (we quote the author), or, for one guide, when its commit history says so. Each guide shows how many nodes of the map it names, 0 included.
