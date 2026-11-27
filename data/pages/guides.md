---
title: "Guides to the Lean proof of the Riemann hypothesis"
description: "Browse guides and verification reports for Alpöge’s original Lean proof and Sernau’s readable and compact editions."
h1: "Guides to the Lean proof of the Riemann hypothesis"
path: /guides/
target_queries:
  - riemann hypothesis proof explained
  - alpöge riemann hypothesis proof guide
  - riemann hypothesis lean proof explained
  - riemann hypothesis lean proof blueprint
  - who verified the riemann hypothesis proof
  - riemann hypothesis lean proof reading guide
as_of: "27 Nov 2026"
fold_sections: [sernau-reading-help]
---

# Guides to the Lean proof of the Riemann hypothesis

*As of 27 Nov 2026. The original guide entries record the versions read.*

## Sernau readable {#sernau-readable}

New to RH? Start with the [plain-English introduction](/what-is-the-riemann-hypothesis/#simple).

## Need help reading the proof? {#sernau-reading-help}

Start with the conclusion, then work back to the estimate that the argument needs. These links follow `grh/`, the readable edition of the rewrite that Luke Sernau produced with colleagues at Anthropic and Claude, based on Levent Alpöge’s proof. The Explorer adapted this reading order with AI assistance from the upstream documentation at `72fead10`. The readable edition credits Claude with writing the Lean text and documentation. [Release README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/README.md) · [Readable edition README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md)

1. **Read what Lean proves.** Start with the five declarations in `Main.lean`. Open `Statements.lean` when a declaration points to a named proposition and you want to see its exact hypotheses and conclusion. [Open Main in the reader](https://riemannhypothesissolved.com/sernau/file/Main#riemannHypothesis) · [Pinned Statements.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean) · [Five statements in plain English](/shorter-riemann-hypothesis-proof/#five-statements)
2. **Follow classical RH back one step.** The Explorer’s route starts at `riemannHypothesis` and shows how `New.zeta_zeros_on_line` deduces it from `New.grh`. That result asserts nonvanishing for every Dirichlet character of every positive modulus when Re(s) > ½. The one exception is s = 1 for the principal character, where the L-function has a pole. [Route from Main](/sernau/route/) · [Open New.grh in the reader](https://riemannhypothesissolved.com/sernau/file/New.Reduction.OneSidedBound#New.grh)
3. **Find the estimate behind that result.** `OneSidedBound.lean` uses `star_inequality` and a prime number theorem estimate at a second cutoff to bound a weighted prime-sum remainder from above. The opening comment of `MainInequality.lean` lists the inputs and shows how a common main term cancels. The results index identifies Theorem A (short forms and an index bound), B (near spanning), and C (a lower bound for covolume plus twice the index, in logarithmic terms). [Pinned MainInequality.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean) · [Results index](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/INDEX.md#the-last-step)
4. **Look up a file or unfamiliar term.** Use the contents to see how `New/` groups the steps of the argument and how `Lib/` groups background results. The upstream guide gives a fuller reading order and a glossary that pairs mathematical terms with Lean names. [File contents](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/CONTENTS.md) · [Upstream reading guide](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md)

## Sernau readable · Outside guides {#sernau-outside-guides}

{{readable_guides}}

## Sernau compact {#sernau-compact-guides}

[Pinned compact source at 72fead10](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact) · [Shorter-edition verification](/status/#shorter-editions)

{{compact_guides}}

## Alpöge original {#alpoge-original}

Map links and node counts refer to the original archive. The counts show where guides point into the map. [Verification status](/status/)

{{guides}}

## Other tools

- **riemann.world.** [riemann.world](https://riemann.world/) is a zoomable map of Alpöge’s original Lean files, with their declarations and source.
- **GRH proof explorer (draft).** [GRH proof explorer](https://math.mit.edu/~drew/grhexplorer/) by Andrew Sutherland is a map, dependency graph and search for both editions of Sernau’s shorter proof. The page marks itself as a draft.

## Suggest a guide

Post to [@SomTheBuilder](https://x.com/SomTheBuilder) on X with the link. We list public guides from named authors or consistent public handles. Authors can ask us to correct how their guide is described.

## Changelog

- **23 Nov 2026.** First version, with 11 guides.
- **24 Nov 2026.** One list of 10 guides instead of two groups. Nine have their own page, with links to the nodes of the map they cite.
- **24 Nov 2026, evening.** 13 more guides, 23 in all, 22 with their own page. A guide is labelled "AI-assisted" when its author says AI helped make it (we quote the author), or, for one guide, when its commit history says so. Each guide shows how many nodes of the map it names, 0 included.
- **27 Nov 2026.** Added Nelson’s exercise sheets and Bolan’s manuscript; recorded Hexagon v2 for Zhang’s note; listed Sutherland’s GRH proof explorer under Other tools.
