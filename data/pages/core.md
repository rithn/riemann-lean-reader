---
title: "The core of the proof: 16 clusters, names checked"
description: "The 16 core clusters of the Lean proof of the Riemann hypothesis, in route order from Main.lean, with names checked against the full Lean code."
h1: "The core of the proof"
path: /core/
target_queries:
  - riemann hypothesis lean proof structure
  - natural language riemann hypothesis proof lean
  - riemann hypothesis lean code
  - what is in the lean proof of the riemann hypothesis
  - lean proof main theorem riemann hypothesis
as_of: "25 Nov 2026"
---

# The core of the proof

*As of 25 Nov 2026.*

**The proof is 2,647 clusters of Lean files. This page covers 16 core clusters, from the cluster that holds `Main.lean` outwards. The name of each was checked against the full Lean code.**

## How the last step works

`Main.lean` proves five theorems, two formulations of the classical Riemann hypothesis and three statements about Dirichlet L-functions. Three clusters carry the step, and each name was checked against the code. ([pinned `Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean))

1. **k0677, `Main.lean`.** `riemannHypothesis : RiemannHypothesis := rhOfAll`. Each of the five proofs is a one-line pointer to a theorem in `Supplements.Kernels.MainTheorems` (`rhOfAll`, `allChi`, `claimAll` or `critAll`).
2. **k1091, the step from GRH to RH.** In `Supplements.Kernels.MainTheorems`, `rhOfAll := rh_of_every allChi`. `rh_of_every` takes "no Dirichlet L-function vanishes for Re s > 1/2" and, through the functional equation, returns the Riemann hypothesis. `critLine` returns the critical-line statement for primitive characters.
3. **k2463, `everyCharacter`.** `allChi` is `UpperTheory.FinalTheorems.everyCharacter`: L(χ, s) ≠ 0 for every Dirichlet character χ and every s with Re s > 1/2, apart from the pole at s = 1. The proof takes no hypotheses. It feeds `galoisLocalGlobalStrong_recParameter`, which comes from the theta-lift theorem `TP.K.tLiftK`, into `every_character_of_literature_of_vWin` and `vwin_of_row`.

`Main` imports `Supplements.Kernels.MainTheoremsAll`, which imports `MainTheoremsCritical`, which imports `MainTheorems`, which imports `MainConclusion`. The theorem `UpperTheory.riemannHypothesis_of_everyCharacter` in `RiemannHypothesisOfEveryCharacter` (cluster k2342) uses χ = 1 to get ζ ≠ 0 for Re s > 1/2, and the functional equation for the left half. `MainConclusion` also holds a second copy of `riemannHypothesis`, built on the same `everyCharacter`.

The check read the Lean source at commit [`40e56bab`](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005), the original archive. Of the 16 titles, 14 needed a minor fix and 2 were wrong (k0250 and k2395). The titles below are the checked ones.

## The 16 clusters, in route order

Order: distance from the main theorem (import steps between clusters, `dist` on the map), then, within a distance, the `uses` links from the final step k1091 outwards. Clusters that no link from k1091 reaches come last at their distance, in id order. See [how the proof is structured](/route/) for the full route.

### 1. k0677: Main theorem statements, plus the explicit formula for Dirichlet L-functions

[Cluster page](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/) · distance 0 · 65 files

`Statements.lean` states the Riemann hypothesis and its Dirichlet L-function versions, `Main.lean` proves them by pointing to the final assembly, and most other files prove a standard explicit formula that ties a prime sum twisted by a character to the zeros of its L-function.

- `riemannHypothesis` in `Main`, with `LFunction_ne_zero_of_half_lt_re`, `LFunction_eq_zero_re` and `LFunction_eq_zero_re_of_isPrimitive`
- `DirichletLNonvanishingRightOfHalf` in `Statements`
- `explicitFormula_closed` in `Formalism.PeriodIntegrals.ExplicitFormulaCounts.ExplicitFormula`: the truncated explicit formula, proved

### 2. k0695: An alternative route to GRH for Dirichlet L-functions, from three inputs

[Cluster page](/cluster/k0695-host-field-conditions-inertness-of-primes-and-character-box/) · distance 3 · 80 files

Its top theorem, `plugAll`, proves that no Dirichlet L-function vanishes for Re s > 1/2 from three named inputs: Green's description of the cuspidal characters of finite GL, a bound on certain Galois cohomology groups of cyclotomic subfields, and a bundle of further assumptions. The rest of the cluster builds the tools for it: an abelian "host" number field inside a cyclotomic field, Jacobi-symbol rules for which primes are inert, and counting lemmas.

- `UpperTheory.Top.plugAll` in `Development.AutomorphicArithmetic.CharacterBoxes.EveryCharacter`
- `UpperTheory.GL.isInert_iff` in `Development.AutomorphicArithmetic.ConductorsKronecker.IsInertIff`: a prime is inert exactly when it is prime, does not divide the level, and a Jacobi symbol equals −1
- `landau_zero_free_half_plane` in `Formalism.SharpRestriction.GlobalSchurBounds.GlobalRankLatticeProofs.LandauZeroFreeHalfPlane`: a power bound on a smoothed prime-sum error makes zeta zero-free past that exponent

### 3. k2404: Local Langlands for GL(n): tempered parameters, uniqueness and literature inputs

[Cluster page](/cluster/k2404-published-inputs-for-local-langlands-tempered-and-converse/) · distance 3 · 49 files

Proves that a local Langlands map sends tempered representations to tempered parameters, that a character of GL(1) is tempered exactly when its absolute value is 1, and that the map is unique once local converse and a few other named results hold. It also names published results (local converse, existence of local Langlands, Caraiani's temperedness) as hypotheses and bundles them into packages.

- `LocalConverseGL` in `Development.AbelianVarietyTheory.PublishedTheorems.GaloisCohomology₂.LocalConverseGL`: a named statement that cuspidal representations with equal twisted epsilon factors are isomorphic
- `tempered_of_isTemperedGL` in `Development.AbelianVarietyTheory.Proofs.SatakeParameters.TemperedRepTemperedParameter`
- `recUnique_of_localConverse` in `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ReciprocityUniqueOf`: five named hypotheses imply the local Langlands map is unique

### 4. k0704: Hecke characters on ideles: local factors, finiteness and rigidity

[Cluster page](/cluster/k0704-ideles-idele-characters-and-their-local-factorization/) · distance 3 · 89 files

Defines Hecke characters of a number field (continuous characters of the ideles that are trivial on the field's own nonzero elements) and proves their basic properties. A continuous idele character is unramified at almost all primes and splits into local pieces. Hecke characters with fixed behaviour at infinity and bounded conductor are finite in number and are determined by their values at almost all primes.

- `continuous_char_factor` in `Development.AbelianVarietyTheory.Proofs.SatakeParameters.ContinuousIdeleCharLocalFactorization`
- `heckeFin` in `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.KeyFinitenessGlobal`: characters of given infinity type and bounded level are finitely many
- `finite_infinite_product_eq_one` in `Development.WeilBound.CoreStatements.PublishedTheorems.SmoothVectorEstimates.FiniteInfinitePlaceProduct`: proves `HeckeCharacterRigidity`

### 5. k0427: Hermitian lattices over number fields: trace form, genus, class-number finiteness

[Cluster page](/cluster/k0427-hermitian-lattices-over-number-fields-trace-forms-and-class/) · distance 3 · 27 files

Proves results about lattices over the integers of a number field that carry a Hermitian form. Taking the trace of the form gives an ordinary Euclidean lattice. From that, lattices in one genus have the same covolume, a genus holds finitely many lattices up to isometry, and each lattice has finitely many symmetries.

- `classSetFinite` in `Formalism.HermitianLattices.HermitianLatticesProofs.ClassSetFinite`
- `genusCovol` in `Formalism.HermitianLattices.HermitianLatticesProofs.GenusCovol`
- `autFinite` in `Formalism.HermitianLattices.HermitianLatticesProofs.AutFinite`

### 6. k1091: Bernoulli numbers for Dirichlet characters, plus the final step from GRH to RH

[Cluster page](/cluster/k1091-bernoulli-numbers-and-dirichlet-characters/) · distance 4 · 45 files

Most files are a proved library on generalised Bernoulli numbers attached to Dirichlet characters: their relation to L-values at negative integers, their denominators, their size, and how they change with the modulus. A few small files carry the last step of the project. They take "no Dirichlet L-function vanishes right of the line Re s = 1/2" and turn it, through the functional equation, into the Riemann hypothesis and the critical-line statements that `Main.lean` exports.

- `rhOfAll` in `Supplements.Kernels.MainTheorems`: `RiemannHypothesis := rh_of_every allChi`, with `critAll` and `claimAll`
- `Formalism.VW.rh_of_right` in `Formalism.GammaFactorNonvanishing.RhOfRight`: ζ ≠ 0 for Re s > 1/2 implies `RiemannHypothesis`
- `UpperTheory.V.Bern.b_lprim` in `Development.AutomorphicArithmetic.AutomorphicVarieties.GaloisLibrary.BernoulliNumbers.BLprim`: L(χ, 1−k) = −B(k,χ)/k

### 7. k2463: Final assembly: GRH for Dirichlet L-functions, then the Riemann hypothesis

[Cluster page](/cluster/k2463-final-assembly-step-including-the-riemann-hypothesis/) · distance 4 · 34 files

The file `MainConclusion` proves that no Dirichlet L-function vanishes to the right of the line Re s = 1/2 and deduces the Riemann hypothesis from it in one step. The headline theorem in `Main.lean` rests on this step. The other files are named bundles of results quoted from the literature, plus conditional automorphy lemmas of the form "if these published results hold, then this follows".

- `UpperTheory.FinalTheorems.everyCharacter` and `UpperTheory.FinalTheorems.riemannHypothesis` in `Development.AutomorphicArithmetic.CharacterBoxes.MainConclusion`
- `galoisLocalGlobalStrong_recParameter` in `Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.RowSrc`: proved from the theta-lift theorem `TP.K.tLiftK`

### 8. k2401: A proved depth-zero local Langlands map for GL(n) over p-adic fields

[Cluster page](/cluster/k2401-depth-zero-local-langlands-and-characters-of-finite-gl/) · distance 4 · 117 files

Proves, with no extra hypotheses, that at every place of a number field there is a map from irreducible representations of GL(n) to Weil–Deligne representations with the expected properties. On depth-zero cuspidals the map matches Green's description of cuspidal characters of finite GL(n). One further result takes four published theorems as inputs.

- `UpperTheory.Zero.LLC.recTExists` in `Development.AutomorphicArithmetic.Foundations.LocalLanglands.LocalCentralUnits.RecTExists`
- `greenRegularCharacters` in `Development.WeilBound.CoreStatements.StandardPublishedResults.StandardTheoremStatements.GreenRegularCharacters`: Green's parametrization of cuspidal characters of GL(d) over a finite field by regular characters
- `narrowBig_holds` in `Development.DiscreteGroups.GlobalIrreducibility.NarrowBigHolds`: `NarrowBig` from four published-result hypotheses

### 9. k0293: Characters of finite groups and Brauer's induction theorem

[Cluster page](/cluster/k0293-characters-of-finite-groups-virtual-characters-and-induction/) · distance 4 · 141 files

Character theory for finite groups, built from scratch: characters, virtual characters, induction, the inner product and orthogonality. The main result is Brauer's induction theorem. Every character is an integer combination of characters induced from one-dimensional characters of small subgroups.

- `mem_spanZ_of_mono` in `GroundTheory.LocalFields.BrauerInductionAssembly`
- `brauerDegreeZero` in `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BrauerDegreeZero`
- `character_pairing_eq_finrank_hom` in `Development.AbelianVarietyTheory.Proofs.CharacterTheory.FiniteGroupFunctionPairingAddNatPosSymm`

### 10. k2009: Local Langlands bookkeeping at split places for the theta-lift argument

[Cluster page](/cluster/k2009-third-place-series-and-local-langlands-correspondence/) · distance 4 · 171 files

Assuming a local Langlands map exists, these files work out what it says at the split places of a CM field. Spherical components get unramified parameters whose Frobenius eigenvalues match the Hecke eigenvalues. Tame and depth-zero components get inertia data read off from Green's labels. Almost every result also assumes a bundle of published inputs.

- `exists_isRc_alt` in `Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsIsRc`: a series correspondence agreeing with the local map exists
- `GlobalTheory.T.locRecT_unr_of_sphAt` in `Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsTerTailStatement`: spherical at a split place implies an unramified local parameter
- `IsSeriesCorrespondence` in `Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.IsRc`

### 11. k2395: Local and global Galois groups of number fields and the Artin map

[Cluster page](/cluster/k2395-local-galois-groups-completions-and-global-artin-reciprocity/) · distance 4 · 101 files

Compares the Galois group of a number field's algebraic closure with the local Galois groups at each prime, by embedding the closure into completions. Proves that the global Artin reciprocity map is unique and compatible with the local Artin maps, norms and restriction to subfields, and proves Chevalley's theorem that units close enough to 1 are m-th powers.

- `globalArtin_unique` in `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.GlobalArtinReciprocityMapUnique`: any two global Artin maps are equal
- `GlobalTheory.Published.chevalleyUnits'` in `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ChevalleyUnits`
- `decomposition_mulEquiv_galLoc` in `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.DecompositionGroupLocalGaloisIso`: a decomposition group is isomorphic to the local absolute Galois group

### 12. k0913: Twisted trace on unitary-invariant maps is ±2^n, via highest-weight counting

[Cluster page](/cluster/k0913-simultaneous-diagonalisation-and-highest-weight-counting/) · distance 4 · 172 files

Proves that a certain twisted trace, taken over the maps from a finite-dimensional unitary-group representation into an irreducible module for GL(n) viewed as a real group, is always plus or minus 2^n. The proof counts highest-weight vectors, shows that only one candidate weight occurs and its space is a line, and uses Weyl-character product identities and simultaneous diagonalisation of commuting Hermitian matrices.

- `UpperTheory.V.Z.GSp4Splitting.coreG` in `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.TraceFormula.GL4GeometricSide.CoreG`: the twisted trace on invariants is ±2^n
- `countG` in `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.DiagonalMemUnitary`
- `exists_unitary_isDiag` in `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.CommutingHermitianSimultaneousDiag`

### 13. k1394: Galois action on p-adic complex numbers: Ax–Sen–Tate, Tate traces, twists

[Cluster page](/cluster/k1394-galois-symmetries-of-the-p-adic-algebraic-closure/) · distance 4 · 21 files

Proves how Galois symmetries act on the completed algebraic closure of the p-adic numbers. The headline results are the Ax–Sen–Tate lemma (a number that every symmetry moves only slightly lies close to the base field), Tate's normalized trace along the cyclotomic tower, and the fact that a nonzero Tate twist C_p(j) has no Galois-fixed vectors.

- `ax_lemma` and `fixedPoints_gal_eq` in `GroundTheory.PAdicHodge.AxLemma`: the Galois-fixed points of C_p over a finite extension K are exactly K
- `cpTwistRep_invariants_eq_bot` in `GroundTheory.PAdicHodge.ExistsGalFixCyclotomicLayerCycloCharNeOne`

### 14. k2033: Unitary groups over local fields: Satake parameters of spherical representations

[Cluster page](/cluster/k2033-weyl-cells-satake-parameters-and-spherical-eigenvalues-for/) · distance 4 · 129 files

Proves that every irreducible spherical representation of an unramified unitary group over a local field sits inside a principal series whose Satake parameter can be reordered so its sizes decrease and are all at least 1. The supporting work includes the Iwasawa, Bruhat and Iwahori decompositions and Haar-measure counts on Weyl cells.

- `extremeU` in `Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.IwahoriFactorisation.StrictDominance.UnitaryExtremality.ExtremeU`
- `bruhat_iwasawa` in `Development.AutomorphicSpectrum.Proofs.BlockDecomposition.UnitaryIwasawaBruhatDecomposition`: every element of GU is Borel × permutation × Iwahori
- `hasSum_series` in `Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSumSu21RankOneSeriesDifferences`: a rank-one shell series sums to (1 − z/q²)(1 + z/q)/(1 − z²)

### 15. k2384: Weil-representation Fock models and multiplicity-one steps for theta lifts

[Cluster page](/cluster/k2384-fock-space-models-archimedean-compactness-and-theta-lifts/) · distance 4 · 186 files

Works with the Weil representation of unitary groups over a CM field, on the polynomial Fock space spanned by Gaussians and their repeated Heisenberg derivatives at the real places. It proves this space and its degree filtration are preserved by the maximal compact subgroup. Assuming a bundle of published results named KP, it proves multiplicity-one statements for the induction steps of theta lifts in two set-ups, A and B.

- `pol_stable_kInf` in `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PolynomialFockSpaceStableArchimedeanMaximalCompa`
- `pol_eq_iSup_fockDeg` in `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PolEqISupFockDeg`
- `GlobalTheory.T.config_a_induction_theta_lift` in `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ConfigAInductionThetaLiftStatement`: under KP, in configuration A, two maps are proportional on the low part

### 16. k0250: A concrete model transfer matrix: Yang-Baxter relation, frames and energy limit

[Cluster page](/cluster/k0250-interlacing-polynomials-and-transfer-products/) · distance 5 · 34 files

Builds an explicit 2×2 transfer matrix whose entries are operators on functions, indexed by patterns of numbers that interlace two given sequences. Proves it is Hermitian, satisfies the Yang–Baxter (RTT) relation and has a prescribed quantum determinant. On top of this model it proves frame and positivity statements for admissible words and an energy-limit lemma.

- `transfer_rtt` in `Formalism.HermitianCurvature.HermitianCurvatureProofs.TransferRtt`: the model transfer matrix satisfies the RTT relation
- `transfer_determinant` in `Formalism.HermitianCurvature.HermitianCurvatureProofs.WeightedSumDifferenceIdentity`
- `lemma_model` in `Formalism.HermitianCurvature.HermitianCurvatureProofs.IsAdmissibleSplittingCharPairMulTwist`: the cutoff energy form of an admissible word tends to size(w) times the squared norm

## Where to go next

- [How the proof is structured](/route/): the route from the main theorem outwards.
- [Every cluster as a list](/list/), or follow a [reading path](/learn/).
- [The proof in numbers](/proof-in-numbers/).
- [Status](/status/) and [how we know](/how-we-know/) cover what was checked and by whom.
- Report a wrong name or description with the "Report a wrong name" link on any cluster page. See [About this map](/about/).
