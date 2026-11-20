# Folder guide (best guess)

**How this was made:** from folder names, file counts and theorem names only. No proofs were read and the project has no comments. Treat every description as a guess.

**Caveat:** folder names are loose labels. Contents often don't match them (for example, `WeilBound` is mostly representation theory, and `AbelianVarietyTheory` holds over half of everything).

Not in any folder: `Statements.lean` and `Main.lean` (28 lines), the statements and headline theorems.

**Spot check (2 folders read):** one name-only guess was wrong and one hand guess was half right. Expect that error rate elsewhere. Folder name, namespace and content are three different things in this project.

## Top level

| Folder | Files | Lines | Best guess |
|---|---|---|---|
| Development | 142k | 12.2M | The bulk (81% of files): the main new argument plus big pieces of supporting theory. |
| Formalism | 18k | 3.2M | About 110 topic folders: from the final RH reduction and classical zeta bounds to lattices, mass formulas and p-adic Hodge theory. |
| GroundTheory | 9k | 1.1M | Textbook background not yet in Mathlib: class field theory, Galois cohomology, automorphic forms, heights. |
| ReciprocityTheory | 4k | 563k | Mixed: class field theory and Chebotarev, reductive groups, and several-complex-variables analysis. |
| CompanionTheory | 2k | 194k | Representation theory of real groups and Bessel models. |
| PositivityTheory | 449 | 55k | Published theorems re-proved as inputs. |
| Lemmata | 167 | 9k | 167 one-file folders of tiny general lemmas, with generic names ("GeneralBFactLeftBis", "MiscLemmasA"). No structure to summarise. |
| Supplements | 3 | 22 | Final glue. |
| BuildAid | 5 | 20 | Build helpers. |

## Development

| Folder | Files | Lines | Best guess |
|---|---|---|---|
| AbelianVarietyTheory | 99k | 8.1M | More than half of the whole project (99k files). Nominally abelian varieties, theta functions and line bundles, but it also holds Iwasawa decomposition, Satake parameters, lattices and measures. Sub-areas are listed below. |
| AutomorphicArithmetic | 18k | 1.8M | The arithmetic core: Galois representations, a modularity/patching argument, theta correspondence, local Langlands. The final GRH statement is assembled here, in CharacterBoxes. |
| AutomorphicSpectrum | 15k | 1.2M | Mostly proofs labelled BlockDecomposition, Geometry and Metric: decomposing spaces of automorphic forms and bounding them. |
| WeilBound | 7k | 849k | Despite the name, mostly representation theory of GL and unitary groups: Siegel–Weil formula, unitary dual, archimedean base change, p-adic Hodge comparison, theta lifts. |
| EtaleCohomology | 1k | 105k | Étale cohomology from scratch: sheaves, Tate twists, purity, Kummer theory, trace maps, a Weil-conjectures piece. |
| ResolutionOfSingularities | 499 | 141k | Embedded resolution of singularities (Hironaka-type), a classical big theorem. |
| DiscreteGroups | 215 | 24k | Irreducibility of global representations and invariants of discrete groups. |

## Formalism

| Folder | Files | Lines | Best guess |
|---|---|---|---|
| (loose files) | 9 | 449 | Nine loose files of top-level statements and zeta non-vanishing criteria (e.g. "RiemannHypothesisOfLowerBounds"). |
| LocalToGlobal | 6k | 956k | Large (5.5k files): Siegel lattice theory, torsion integrality, indefinite forms, Hermitian lattices, glued from local to global. |
| PeriodIntegrals | 4k | 452k | Mostly a mass formula for unitary groups (Siegel-mass style): volumes of stabilisers, local densities, counting. |
| SharpRestriction | 3k | 709k | Growth bounds, cocycles, cusp norm bounds, divisibility. Holds several of the largest machine-scale files. |
| HermitianCurvature | 2k | 461k | Curvature of Hermitian metrics and related measure computations (1.9k files, some very large). |
| GL3MeanSquares | 440 | 78k | Mean-square asymptotics over genera; uses primes in progressions. |
| ThetaLogCoordinates | 292 | 55k | Coordinates for theta lifts: dual Weyl coordinates, Fock-space resolutions, Jacobi weights. |
| WachLatticeTwists | 262 | 38k | Wach modules/lattices (p-adic Hodge theory of crystalline representations), Herr complex. |
| LocalRingCardinality | 173 | 35k | Counting elements of finite local rings; ideal-power membership. |
| GradedWeylDivisibility | 103 | 8k | Fock-space tableaux and divisibility in Weyl-type formulas. |
| PieriBlockIdeals | 98 | 29k | Pieri-rule minors and ideals. |
| AdmissibleDesigns | 93 | 20k | Representation-theory lemmas (guess from the folder name only). |
| GaussJetBounds | 90 | 14k | Elementary estimates and counting bounds (guess from the folder name only). |
| SatakeDualWeyl | 85 | 15k | Satake isomorphism and spherical Hecke algebras over adeles. |
| PadicSubsetSums | 82 | 16k | Elementary estimates and counting bounds (guess from the folder name only). |
| FlagUnipotentLattices | 77 | 31k | Lattice and Hermitian-form computations (guess from the folder name only). |
| SizeWindowBrackets | 64 | 28k | Chains of slope/size windows; contains "PowerBoundGivesRiemannHypothesis". |
| QuotientMetricDivisors | 63 | 15k | Divisor, valuation and height computations (guess from the folder name only). |
| LandauZeroFreeBounds | 58 | 7k | Landau-type zero-free bounds and exceptional (Siegel) zeros. |
| CharacterColumnKernels | 54 | 8k | Representation-theory lemmas (guess from the folder name only). |
| MahlerMeasure | 54 | 17k | Mahler measure, Gauss norms, Smith normal form over p-adics. |
| RealPlaceAnalysis | 54 | 11k | Small helper lemmas (guess from the folder name only). |
| EllipticTorsion | 48 | 9k | Torsion points on elliptic curves (Deuring). |
| DistinguishedUnitIdeals | 44 | 14k | Divisor, valuation and height computations (guess from the folder name only). |
| UnipotentAdelicQuotients | 44 | 5k | Analysis on adelic quotients (Sobolev, elliptic regularity). |
| HarderNarasimhan | 43 | 10k | Harder–Narasimhan slopes of lattices. |
| HermitianLattices | 43 | 7k | Lattice and Hermitian-form computations (guess from the folder name only). |
| PolynomialDimension | 41 | 16k | Small helper lemmas (guess from the folder name only). |
| TruncatedSeriesCounting | 39 | 4k | Elementary estimates and counting bounds (guess from the folder name only). |
| FilteredPoleLength | 36 | 4k | Small helper lemmas (guess from the folder name only). |
| ZeroFreeRegion | 34 | 3k | Classical zero-free region for zeta via log-derivative bounds. |
| FrobeniusOrbits | 32 | 8k | p-adic / Galois-side lemmas (guess from the folder name only). |
| SubspaceCounting | 32 | 7k | Elementary estimates and counting bounds (guess from the folder name only). |
| FormalDegreeBessel | 31 | 6k | Formal degrees and Bessel models. |
| JumpKernelCokernel | 27 | 2k | Representation-theory lemmas (guess from the folder name only). |
| LogVandermondeBounds | 26 | 4k | Elementary estimates and counting bounds (guess from the folder name only). |
| MirabolicMackeyTheory | 26 | 5k | **Checked by reading.** Half right: one file is elementary algebra of upper-triangular matrices in GL(n+1); another is about ramification at places of number fields and log p sums. Namespace is `EigenvalueLevelCeiling`. |
| MeanHeightDescent | 24 | 3k | Elementary estimates and counting bounds (guess from the folder name only). |
| BranchSandwichDivisors | 22 | 8k | Divisor, valuation and height computations (guess from the folder name only). |
| CyclotomicNorms | 21 | 4k | p-adic / Galois-side lemmas (guess from the folder name only). |
| FormalGroupWitt | 21 | 3k | Formal groups and Witt vectors. |
| IncomingBounds | 21 | 4k | Elementary estimates and counting bounds (guess from the folder name only). |
| WeaklyAdmissibleFiltrations | 20 | 2k | Weakly admissible filtered modules and crystalline lifts. |
| ThetaSupremumBounds | 19 | 3k | Elementary estimates and counting bounds (guess from the folder name only). |
| LatticeSlopes | 18 | 2k | Lattice and Hermitian-form computations (guess from the folder name only). |
| GaloisIrreducibility | 17 | 2k | Irreducibility of Galois actions (Jordan's theorem on permutation groups). |
| RankGapBounds | 17 | 2k | Elementary estimates and counting bounds (guess from the folder name only). |
| YangianSpanCharacter | 17 | 1k | Yangian (RTT) relations, a quantum-group tool. |
| CoboundaryTransfers | 16 | 2k | Small helper lemmas (guess from the folder name only). |
| GaussValuationBounds | 16 | 2k | Elementary estimates and counting bounds (guess from the folder name only). |
| LogSumExpBounds | 16 | 2k | Elementary estimates and counting bounds (guess from the folder name only). |
| DoubleCosetMeasures | 15 | 3k | Representation-theory lemmas (guess from the folder name only). |
| SuccessiveMinima | 15 | 2k | Minkowski's second theorem and successive minima. |
| TameInertiaTowers | 15 | 3k | p-adic / Galois-side lemmas (guess from the folder name only). |
| TorsionNormIteration | 15 | 3k | p-adic / Galois-side lemmas (guess from the folder name only). |
| ZetaNonvanishing | 15 | 2k | Non-vanishing of zeta: Landau's lemma, Mellin transforms. |
| BehrendSets | 14 | 1k | Behrend sets (large sets with no 3-term progressions); the note mentions a Behrend trick. |
| CMTypeGalois | 14 | 2k | CM types and Frobenius. |
| FockGram | 14 | 773 | Fock space and Gram determinants. |
| GrowthSums | 14 | 847 | Elementary estimates and counting bounds (guess from the folder name only). |
| HyperbolicPlaceProducts | 14 | 2k | Small helper lemmas (guess from the folder name only). |
| LatticeTheta | 14 | 1k | Theta series of lattices and Poisson summation. |
| NormUnitaryBounds | 14 | 2k | Elementary estimates and counting bounds (guess from the folder name only). |
| FrobeniusContraction | 13 | 2k | p-adic / Galois-side lemmas (guess from the folder name only). |
| ResultantValuation | 13 | 842 | Divisor, valuation and height computations (guess from the folder name only). |
| EisensteinCokernelLengths | 12 | 1k | Small helper lemmas (guess from the folder name only). |
| FrobeniusBaseCase | 12 | 2k | p-adic / Galois-side lemmas (guess from the folder name only). |
| LatticeRigidity | 12 | 1k | Lattice and Hermitian-form computations (guess from the folder name only). |
| SobolevGaussianKernels | 12 | 578 | Theta-function and Gauss-sum/jet computations (guess from the folder name only). |
| LogFactorialIndices | 11 | 1k | Elementary estimates and counting bounds (guess from the folder name only). |
| WindowSums | 11 | 1k | Elementary estimates and counting bounds (guess from the folder name only). |
| ThetaLiftIndependence | 10 | 802 | Theta-function and Gauss-sum/jet computations (guess from the folder name only). |
| LagrangeIdealLifts | 9 | 1k | Divisor, valuation and height computations (guess from the folder name only). |
| WachModuleLifts | 9 | 1k | Lifting Wach modules. |
| DirichletDensity | 8 | 1k | Dirichlet density of primes. |
| GelfandTransference | 7 | 793 | Small helper lemmas (guess from the folder name only). |
| LFunctionBounds | 7 | 988 | Bounds on L-functions and partial sums. |
| PairingDivisors | 7 | 700 | Divisor, valuation and height computations (guess from the folder name only). |
| TranslateCocycles | 7 | 2k | Small helper lemmas (guess from the folder name only). |
| GaloisCohomology | 6 | 400 | Small Galois-cohomology facts (local Euler characteristic). |
| MonomialMeanResidues | 6 | 1k | Elementary estimates and counting bounds (guess from the folder name only). |
| SelfDualUnimodular | 6 | 822 | Lattice and Hermitian-form computations (guess from the folder name only). |
| SmithDeterminants | 6 | 403 | Smith normal form. |
| DegreeFormula | 5 | 902 | Divisor, valuation and height computations (guess from the folder name only). |
| DivisorInequality | 5 | 1k | Divisor, valuation and height computations (guess from the folder name only). |
| FormalGroupLog | 5 | 935 | Logarithms of formal groups. |
| LogFactorialBounds | 5 | 371 | Elementary estimates and counting bounds (guess from the folder name only). |
| MoebiusJetDuality | 5 | 384 | Theta-function and Gauss-sum/jet computations (guess from the folder name only). |
| ThickAverageLoss | 5 | 1k | Small helper lemmas (guess from the folder name only). |
| DropLevelBounds | 4 | 366 | Elementary estimates and counting bounds (guess from the folder name only). |
| TowerValuationBounds | 4 | 2k | Elementary estimates and counting bounds (guess from the folder name only). |
| AdicCompletionExports | 3 | 202 | p-adic / Galois-side lemmas (guess from the folder name only). |
| ConjugateSelfDual | 3 | 146 | Small helper lemmas (guess from the folder name only). |
| CorankShare | 3 | 563 | Small helper lemmas (guess from the folder name only). |
| AlgebraicWeights | 2 | 228 | Small helper lemmas (guess from the folder name only). |
| ArtinHasse | 2 | 513 | Artin–Hasse exponential. |
| GammaFactorNonvanishing | 2 | 94 | The final two-file reduction: "no zeros right of ½" ⇒ RH, via the functional equation. |
| GaussIdealIdentity | 2 | 275 | Theta-function and Gauss-sum/jet computations (guess from the folder name only). |
| JacobiWeightFamilies | 2 | 209 | Contains "WeightedSieveImpliesRH": a criterion turning a weighted sieve bound into RH. |
| JacquetSubsetSums | 2 | 149 | Elementary estimates and counting bounds (guess from the folder name only). |
| LatticeLocalGlobal | 2 | 216 | Lattice and Hermitian-form computations (guess from the folder name only). |
| WeightedDeltaMeans | 2 | 241 | Elementary estimates and counting bounds (guess from the folder name only). |
| AlphaUniqueness | 1 | 97 | Small helper lemmas (guess from the folder name only). |
| HalfLinks | 1 | 186 | **Checked by reading.** Not helper lemmas: a statements-only file close to the core. Defines sums Σ Λ(n)(y/n − 1) over primes with a Frobenius condition, CM types, and parameter conditions with m ≈ √x. |
| PrimeAboveExistence | 1 | 76 | Small helper lemmas (guess from the folder name only). |
| ProductFormula | 1 | 162 | Small helper lemmas (guess from the folder name only). |
| TwistFamilyExistence | 1 | 87 | Small helper lemmas (guess from the folder name only). |
| WideWeightTheorem | 1 | 85 | One file: a three-parameter version of "weighted sieve implies RH". |

## GroundTheory

| Folder | Files | Lines | Best guess |
|---|---|---|---|
| HeightsAndTheta | 6k | 641k | Arakelov-style height theory (6.3k files): arithmetic Bézout, Hilbert–Samuel, ampleness, Chowla–Selberg, plus a small theta-function part. |
| AutomorphicForms | 542 | 150k | Background: automorphic forms on GL2, Whittaker models, multiplicity one, tensor product theorem, Godement–Jacquet zeta integrals. |
| ProfiniteCohomology | 450 | 85k | Galois cohomology: class formations, Poitou–Tate duality, Euler characteristics, restricted ramification. |
| GlobalFields | 384 | 72k | Global class field theory background: adeles, ideles, Tate's thesis, Artin map, complex multiplication. |
| PAdicHodge | 226 | 64k | p-adic Hodge theory background: period rings, Kummer theory. |
| ArithmeticGeometry | 218 | 45k | Background: cohomology of schemes, abelian varieties (Weil pairing), modular curves, toric varieties. |
| LocalFields | 159 | 41k | Local class field theory: Lubin–Tate, formal groups, local reciprocity. |
| TateCohomology | 56 | 9k | Tate cohomology of finite groups and cup products. |
| Brauer | 20 | 5k | Brauer groups and central simple algebras. |
| PowerSubgroups | 20 | 1k | Small topological/lattice lemmas. |
| FunctionField | 12 | 4k | Function fields of curves: genus, Riemann–Roch-style facts. |
| IdeleRoots | 10 | 2k | Small idele and torus facts. |

## ReciprocityTheory

| Folder | Files | Lines | Best guess |
|---|---|---|---|
| ReductiveGroups | 3k | 410k | Arithmetic geometry of reductive groups (Arakelov volumes, fundamental domains, heights) and discrete series (existence, formal degree, even the exceptional group G2). |
| L2DbarEstimates | 227 | 34k | Hörmander/Skoda-type L² estimates for the ∂̄ operator (complex analysis). |
| AnalyticForms | 192 | 37k | Several complex variables: plurisubharmonic functions, Levi forms, potential theory, regular local rings. |
| DualLattices | 183 | 25k | Dual lattices and towers of rings. |
| SemistableReduction | 119 | 15k | Semistable reduction and related estimates. |
| ClassFieldTheory | 91 | 12k | Local class field theory (mostly) and Artin reciprocity. |
| GroupCohomology | 56 | 8k | Group cohomology lemmas. |
| Chebotarev | 47 | 4k | Chebotarev density theorem. |
| GeometryOfNumbers | 39 | 5k | Lattice covolumes and asymptotics. |
| CommutativeAlgebra | 26 | 3k | Cohen–Macaulay rings, heights, dimension theory. |
| NeutralLocalFields | 20 | 5k | Comparing local fields and their Galois actions. |
| GaloisValuations | 9 | 2k | p-adic / Galois-side lemmas (guess from the folder name only). |
| ReducedBases | 9 | 1k | Small helper lemmas (guess from the folder name only). |
| ThetaSummability | 7 | 359 | Convergence of theta tail sums. |
| ThetaQuasiPeriods | 5 | 771 | Theta functions: summability and quasi-periodicity. |
| Automorphisms | 4 | 461 | Small helper lemmas (guess from the folder name only). |
| Hypotheses | 3 | 476 | Three files of named hypotheses/conditions (e.g. "SolubleDescentCMReal"). Worth a look: see whether they are assumed or proved. |
| BasicDefinitions | 2 | 136 | Small helper lemmas (guess from the folder name only). |
| EigenFrames | 2 | 136 | Small helper lemmas (guess from the folder name only). |
| AdeleApproximation | 1 | 178 | Small helper lemmas (guess from the folder name only). |
| AdicCompleteness | 1 | 111 | p-adic / Galois-side lemmas (guess from the folder name only). |
| BurnsideSurjectivity | 1 | 178 | Small helper lemmas (guess from the folder name only). |
| GeneralLinearIntegers | 1 | 34 | Small helper lemmas (guess from the folder name only). |
| ResidueCardinality | 1 | 151 | Small helper lemmas (guess from the folder name only). |

## CompanionTheory

| Folder | Files | Lines | Best guess |
|---|---|---|---|
| SpectralGeometry | 1k | 105k | Almost entirely "LocalGlobalProofs": local-to-global lattice arguments. The folder name is a loose label. |
| AutomorphicTheory | 457 | 48k | Representation-theory tools for automorphic forms: Pieri rules, uniqueness of local Bessel models, theta dilations, product formula. |
| RealGroups | 155 | 16k | Real unitary groups: discrete series, formal degrees, base change, admissibility. |
| HarishChandraModules | 130 | 21k | Representations of real Lie groups: K-finite and analytic vectors, Bessel integrals, low K-type multiplicities. |
| ThickeningEstimates | 22 | 4k | Reduction to Lie groups and Siegel-domain estimates (metaplectic covers). |
| EightfoldTheory | 9 | 9 | Nine one-line files; almost certainly just import/glue stubs. |

## PositivityTheory

| Folder | Files | Lines | Best guess |
|---|---|---|---|
| AutomorphicForms | 445 | 55k | "PublishedInputs": proofs of known published theorems used as inputs (Deligne–Ribet, Siegel–Klingen, partial zeta functional equations, CM main theorem). |
| PublishedTheorems | 3 | 105 | Three small published lemmas (towers, units, Weil representation). |
| Representations | 1 | 55 | One file on boundary cones. |

## Inside the big folders (adaptive depth)

**Rule:** keep splitting a folder while it has more than 1,000 files. Small siblings are merged into one "other" row. A folder marked **flat** is over 1,000 files with no subfolders; those get a word profile in the next section.

Each row: name (files), my guess where I have one, then the most common words in its file names. Rows without a guess are the folder name plus the words.


### Development/AbelianVarietyTheory (99,187 files)

- **Proofs** (95,418): the proofs; everything else in this area is definitions and statements
  - **DivisorProofs** (42,424) **flat**: the largest single block in the project (24% of all files)
  - **InertiaEigenvalues** (8,951) **flat**
  - **IwasawaDecomposition** (7,769) **flat**
  - **TwistedOperators** (6,642) **flat**
  - **DecoratedLatticeProofs** (5,063) **flat**
  - **FlagMeasures** (4,003) **flat**
  - **SatakeParameters** (3,462) **flat**
  - **FoundationProofs** (3,411) **flat**
  - **DegenerationProofs** (1,563) **flat**
  - **ModuliProofs** (1,539) **flat**
  - **JetHarmonics** (1,417) **flat**
  - **GlobalInterpolation** (1,298) **flat**
  - UniformizationProofs (869): complex uniformisation of abelian varieties. Words: abelian, torsion, theta, torus.
  - UnitaryExistence (767): existence of forms/representations on unitary groups. Words: frame, lattice, point, level.
  - HeightProofs (599): heights of abelian varieties. Words: unitary, field, compact, real.
  - AdelicLatticeProofs (594): lattices over the adeles. Words: units, norm, index, matrix.
  - CuspFormEvaluations (586): values of cusp forms at special points. Words: theta, frame, short, base.
  - SiegelThetaTransformation (516): how Siegel theta functions transform. Words: theta, hermitian, level, lattice.
  - UnramifiedDepth (506): unramified local computations. Words: integral, formal, group, series.
  - CubicalLineBundles (495): cubical structures on line bundles (theorem of the cube). Words: lattice, line, integral, curve.
  - ThetaShiftProofs (476): shifting theta functions. Words: point, theta, constant, section.
  - ThetaLawProofs (356): functional laws of theta functions. Words: theta, invariant, sections, base.
  - RingsOfIntegers (325): rings of integers of number fields. Words: integral, formal, section, value.
  - *other: 13 folders* (1,787), e.g. Generic Regularity, Character Theory, Torus Haar Measure, Formal Group Charts
- **Definitions** (2,198): definitions used by the proofs
  - Divisors (573). Words: base, rank, over, point.
  - AutomorphicMembership (334). Words: base, places, level, field.
  - NonGaloisDescent (207). Words: admissible, char, series, smul.
  - LatticeFrames (190). Words: true, single, comb, chart.
  - Foundations (175): foundational layer. Words: zeta, unitary, lift, measure.
  - GaloisGeometry (169). Words: split, level, forms, theta.
  - SemilocalFrames (97). Words: flag, const, unitary, base.
  - GlobalTwisting (79). Words: prime, points, level, rows.
  - TwistedInnerProducts (68). Words: witt, anisotropic, chain, class.
  - *other: 24 folders* (306), e.g. Degenerations, Theta Metrics, Jets, Moduli Spaces
- BlockTheory (753): block decompositions (representation theory). Words: lattice, theta, level, character.
- PublishedTheorems (493): known published results, re-proved. Words: unitary, discrete, siegel, series.
- Counterexamples (192): examples and "surveys"; likely checks that hypotheses are needed. Words: unique, base, good, level.
- Statements (121): named statements, proved elsewhere. Words: point, field, formula, theta.
- CrystallinePeriods (12): crystalline period rings. Words: cris, maps, factorial, ring.

### Development/AutomorphicArithmetic (18,431 files)

- **AutomorphicVarieties** (7,959): Shimura-variety and Galois-representation machinery
  - *loose files* (5)
  - **ModularityArgument** (2,515): looks like a Taylor–Wiles-style modularity lifting argument
    - ThresholdArguments (532): threshold/case analysis inside the modularity argument. Words: level, types, seed, rank.
    - SymmetricPowerTransfer (432): symmetric power functoriality. Words: unit, norm, unitary, conj.
    - TraceFormula (291): trace formula. Words: quot, hecke, unit, comm.
    - InductionEstimates (215): estimates for an induction. Words: line, laws, hecke, tens.
    - KatoQuadraticCharacters (200): quadratic characters (Kato-style). Words: kato, norm, frob, imports.
    - LinkedUnramifiedChains (153). Words: prime, norm, unit, unitary.
    - AutomorphyLifting (117): automorphy lifting theorems. Words: plain, rank, split, condition.
    - CrystallineOrdinaryIdeals (80): crystalline/ordinary deformation conditions. Words: crystalline, ideal, ordinary, saturated.
    - ClassCounting (74). Words: count, block, unit, exponent.
    - CuspidalDescent (56). Words: desc, weak, dual, weights.
    - ScatteringLimits (52). Words: spec, conv, laws, trace.
    - *other: 12 folders* (313), e.g. Base Change Units, Levi Smooth Localization, Cuspidal Twists, Multiplicity One
  - LiteratureResults (547): results taken from the literature, re-proved. Words: pull, exact, split, span.
  - WeakShimuraTheory (492): Shimura varieties (weak form). Words: conj, facts, cont, flag.
  - BuildingsResidueChars (460): Bruhat–Tits buildings and residue characteristic. Words: character, frobenius, level, fiber.
  - GaloisLibrary (444): general Galois-theory library. Words: char, conj, level, unit.
  - PatchingModules (441): Taylor–Wiles patching. Words: desc, lift, selmer, quot.
  - AutomorphicForms (373). Words: arch, conv, char, cont.
  - AlgebraTools (314). Words: quot, span, lift, units.
  - PadicHodgeTheory (212): p-adic Hodge theory. Words: lift, frobenius, crystalline, chart.
  - FrobeniusSmoothVectors (209). Words: frobenius, corner, frame, dual.
  - TheoremsMuLinked (176). Words: dual, imports, charpoly, single.
  - ConjugateRepresentations (166). Words: facts, harm, comm, conj.
  - *other: 42 folders* (1,605), e.g. Hecke Algebras, Commutative Algebra, Idele Generators, Unitary Three Deformations
- **Foundations** (4,413): foundational layer
  - **GaloisRepresentations** (2,965): Galois representations attached to automorphic forms
    - ThetaParseval (780): Parseval identities for theta lifts (the note mentions iterating Parseval). Words: weil, siegel, theta, base.
    - SphericalCoordinates (254). Words: coord, trace, diag, charpoly.
    - AnnihilatorModels (183). Words: frob, norm, read, split.
    - IntegralStructures (175): integral structures; holds the theorem that feeds the final step. Words: conj, down, char, flag.
    - RegularSemisimpleFibres (150). Words: norm, match, trace, elem.
    - PAdicWittLattices (148). Words: trans, desc, splits, uniq.
    - KunnethLefschetz (142): Künneth and Lefschetz formulas. Words: chart, blow, proj, cover.
    - TranscendenceTraces (118). Words: mult, spec, corr, push.
    - LocalMaximality (100). Words: degree, trace, criterion, koszul.
    - SeparatingAlgebras (82). Words: gamma, block, facts, count.
    - FiniteEtaleModels (75). Words: lift, base, unit, beta.
    - ProjectiveAutomorphicHecke (63). Words: conj, norm, proj, central.
    - AdmissibleResidues (62). Words: charpoly, defs, real, admissible.
    - *other: 29 folders* (633), e.g. Lefschetz Sigma Sums, Basic Open Sections, Inertia Quadratic Ramification, Type Conditions
  - **Convolution** (1,090): convolution algebras and analysis on groups
    - *loose files* (4)
    - RealGroupAnalysis (382): analysis on real groups. Words: imports, lift, continuous, fock.
    - SplitEigenfunctions (90). Words: cont, norm, char, laws.
    - ConvolutionKernels (70). Words: tens, comm, conv, norm.
    - IntegrableConvolution (64). Words: tens, split, trace, match.
    - EndomorphismSlices (51). Words: comm, hecke, read, test.
    - BlockHeckeSlices (48). Words: slice, kill, shift, band.
    - CentreSplitting (44). Words: summand, central, closure, conj.
    - *other: 13 folders* (337), e.g. Trace Splitting, Power Sum Traces, Twisted Local Orbits, Polynomial Coefficient Bounds
  - BaseChangeIdentities (106). Words: frame, narrow, dirac, split.
  - *other: 6 folders* (252), e.g. Iwahori Reduction, Etale Clopen Descent, Local Langlands, Unitary Spherical Fixing
- **ThetaCorrespondence** (3,201): theta correspondence between pairs of groups
  - *loose files* (1)
  - **ThetaPairLifts** (2,998): the chain of theta lifts the note describes
    - **ThirdPlaceSeries** (2,251) **flat**: main body of the theta-lift chain; holds the step that derives GRH from the lifts
    - LocalTypeDictionary (559): dictionary of local representation types. Words: theta, lift, twisted, twist.
    - HodgeBundleWeights (188): weights of Hodge bundles. Words: covering, weight, bundle, section.
  - *other: 15 folders* (202), e.g. General Linear Groups, Real Bands, Fock Models, Crystalline Comparison
- IntegralCasts (907): integrality arguments; includes Capelli identities and some of the largest files. Words: imports, integral, norm, span.
- CommutativeAlgebra (432). Words: etale, pullback, affine, cohomology.
- DivisorFrames (383): frames for divisors. Words: point, frame, flag, model.
- *other: 49 folders* (1,136), e.g. Cyclotomic Bounds, Whittaker Hecke, Twisted Traces, Adelic Quotients

### Development/AutomorphicSpectrum (15,147 files)

- **Proofs** (14,864): the proofs; everything else in this area is definitions and statements
  - **BlockDecomposition** (8,354) **flat**: decomposing spaces of automorphic forms into blocks
  - **GeometryProofs** (3,001) **flat**: geometry: Hodge structures, models, lattices
  - **MetricProofs** (1,576) **flat**: metrics on flag varieties and charts
  - AlgebraProofs (813): algebra. Words: lattice, order, hopf, chart.
  - GlobalProofs (509): global arguments. Words: smooth, cone, adelic, growth.
  - DivisibilityProofs (374): divisibility arguments. Words: tower, flag, height, intersection.
  - *other: 7 folders* (237), e.g. Adelic Proofs, Twisted Proofs, Membership Proofs, Non Galois Proofs
- *other: 5 folders* (283), e.g. Definitions, Statements, Published Theorems, Parallel Statements

### Development/WeilBound (7,051 files)

- **CoreStatements** (3,746): core statements and their proofs
  - AutomorphicKernels (932): kernel functions for automorphic forms. Words: siegel, norm, frame, continuous.
  - PublishedTheorems (540): known published results, re-proved. Words: ptfs, vanishing, final, divisor.
  - PadicHodgeComparison (538): p-adic Hodge comparison theorems. Words: chern, pull, hodge, cech.
  - HodgeTatePoints (299): Hodge–Tate points/periods. Words: htat, hopf, base, chart.
  - TorusUniformisation (196): uniformisation by tori. Words: lattice, point, model, function.
  - PluriharmonicCharts (118). Words: flags, minor, period, conj.
  - FlagImmersions (108). Words: tower, model, root, intersection.
  - TemperedRepresentationTheory (108). Words: cusp, development, defs, siegel.
  - HomogeneousNonvanishing (105). Words: height, models, twisted, arch.
  - PlurisubharmonicCones (101). Words: lattice, charts, smooth, family.
  - AbelianHeightsDuality (90). Words: ample, lift, metric, poly.
  - VolumeEquality (77). Words: push, unif, base, ball.
  - *other: 39 folders* (534), e.g. Sesquilinear Fractions, Gaussian Seminorm Bounds, Common Zero Evaluation, Minimal Prime Dimensions
- **RepresentationTheoryGL** (2,486): representation theory of GL(n)
  - ArchimedeanBaseChange (798): base change at the real/complex place. Words: chain, blocks, frame, split.
  - SiegelWeilProof (635): the Siegel–Weil formula. Words: block, deriv, gauss, continuous.
  - UnitaryDualProof (300): classification of unitary representations. Words: continuous, trace, char, imports.
  - RegularisedSiegelWeil (153): regularised Siegel–Weil formula. Words: approx, major, hermitian, good.
  - ResidualSpectrum (116): residual spectrum (Eisenstein residues). Words: slice, string, stages, measure.
  - CasimirAlgebra (95). Words: trans, tensor, contract, conj.
  - GenericUnitaryGL (66). Words: generic, unlinked, cusp, deriv.
  - HolomorphicDiscreteSeries (64). Words: identity, square, casimir, inputs.
  - *other: 14 folders* (259), e.g. Limit Multiplicity Weights, Eisenstein Series, Jacquet Shalika Bounds, Twisted Factors
- ThetaLifts (788): theta lifts. Words: plane, weil, theta, real.
- *other: 7 folders* (31), e.g. Hecke Vectors, Cuspidal Admissibility, Level Criteria, Simple Eigenvalues

### Development/EtaleCohomology (1,398 files)

- EtaleSheaves (688): étale sheaves. Words: leaf, etale, glue, chart.
- TateTwists (239): Tate twists. Words: etale, tensor, sheaf, twist.
- CohomologicalPurity (202): purity theorem. Words: leaf, hens, cont, free.
- KummerTheory (98): Kummer theory. Words: adic, dict, place, insep.
- EtaleTrace (70): trace maps. Words: etale, chart, twist, cover.
- DivisorCycles (56): cycle classes of divisors. Words: spec, poly, dense, struct.
- *other: 4 folders* (45), e.g. Weil Conjectures, Cyclotomic Discriminants, Kummer Extensions, Etale Duality

### Formalism/LocalToGlobal (5,501 files)

- *loose files* (18)
- **SiegelLatticeTheory** (2,085): lattice theory behind Siegel-type mass formulas
  - *loose files* (5)
  - **CokernelGLCounts** (1,028): counting cokernels / points over GL
    - *loose files* (13)
    - **RankPointCounts** (1,015): counting points by rank
      - *loose files* (552)
      - DualFamilyCounting (299). Words: real, witt, glue, ofib.
      - ThetaModuleTransport (143). Words: theta, proj, split, head.
      - RowFrameCoherence (18). Words: class, frame, lift, move.
      - SharpDualSpans (3). Words: glue, conv.
  - FlagStabilizerTensors (399): stabilisers of flags. Words: carrier, rows, dict, joint.
  - ClosedLocalOrbits (374): closed orbits of local groups. Words: const, slab, frame, norm.
  - HaarTransversals (106). Words: unip, rows, level, nilradical.
  - TraceIntegralEstimates (71). Words: energy, folner, schur, haar.
  - *other: 7 folders* (102), e.g. Casimir Reduction Theory, Casimir Volume Ratios, Closed Volume Statements, Siegel Mass Ratios
- TorsionIntegrality (489): integrality of torsion. Words: integral, gauss, norm, theta.
- IndefiniteReal (435): indefinite forms at the real place; one of the two custom-tactic files is here. Words: split, place, dual, real.
- GlobalTheory (389). Words: lattice, norm, class, basis.
- Columns (376). Words: tied, chain, level, forms.
- ProjectiveLattices (325). Words: free, curve, model, lift.
- CharacterGerms (238). Words: coeff, constant, germ, multiplication.
- GroupLattices (229). Words: span, tied, side, test.
- KernelLattices (162). Words: norm, link, kernel, base.
- InertKernelTheory (149). Words: defs, kernel, inert, frame.
- PairingIndexBounds (127). Words: split, model, unit, character.
- *other: 23 folders* (479), e.g. Divisibility, Lattice Geometry, Hermitian Forms, Normalized Hecke Factors

### Formalism/PeriodIntegrals (4,350 files)

- *loose files* (328)
- **UnitaryGroupMassFormula** (3,615): mass formula for unitary groups (the note mentions "Siegel mass")
  - *loose files* (1)
  - StabilizerVolume (155): volumes of stabilisers. Words: dens, stab, topo, restr.
  - ArchimedeanOrbitMeasures (153): orbit measures at the real place. Words: dens, place, chart, const.
  - StabilizerOrbitVolume (147). Words: dens, stab, topo, restr.
  - WeilStabilizerVolume (146). Words: dens, stab, topo, restr.
  - CountingFormula (113): the counting formula itself. Words: dens, good, lattice, mass.
  - LatticeIndices (95). Words: image, coords, split, basis.
  - ValuationLocalVolumes (84). Words: prim, inert, gram, lattice.
  - *other: 494 folders* (2,721), e.g. Local Unitary Orbits, Semidirect Volume, Weighted Limit Gauge, Lattice Columns
- OrbitalBoundsConclusion (380): final orbital bounds. Words: split, norm, dual, quot.
- *other: 6 folders* (27), e.g. Hermitian Genus Extension, Explicit Formula Counts, Joint Block Shapes, Nabla Spans

### Formalism/SharpRestriction (3,093 files)

- *loose files* (10)
- **GrowthBounds** (1,210): growth bounds (factorials, binomials, valuations)
  - *loose files* (87)
  - RootWeights (126). Words: weight, lattice, stable, integral.
  - MultisetValuation (99). Words: place, rest, integral, smul.
  - MonomialFactorials (88). Words: rest, closed, block, window.
  - ColumnSpanDensity (74). Words: facts, tensor, count, comparison.
  - SegmentDegree (74). Words: path, weight, count, degree.
  - BinomialRatio (61). Words: count, degree, coarse, kept.
  - StandardPolynomials (60). Words: monomial, rest, block, weighted.
  - CoarseMultiplicity (56). Words: block, coarse, tail, rest.
  - DualFockLinear (56). Words: cloud, rest, weight, fock.
  - DiagonalSupport (49). Words: memb, pick, parts, product.
  - HermitianTensor (47). Words: cloud, monomial, letter, block.
  - BinomialPolynomialIdentities (42). Words: admissible, weight, span, product.
  - *other: 23 folders* (291), e.g. Monomial Order Segments, Scale Edges, Plane Coefficients, Logarithmic Sums
- LevelLetterCocycles (758): cocycles indexed by level. Words: lift, length, smul, ring.
- CuspSpanNormBounds (399): norm bounds near cusps; several of the largest files. Words: bridge, rows, family, cell.
- Divisibility (274). Words: chart, uniq, gauge, germ.
- GlobalSchurBounds (158). Words: family, theorem, lattice, link.
- GenusPolyhedralBounds (88). Words: class, count, theorem, integral.
- *other: 6 folders* (196), e.g. Admissible Parameter Joins, Inert Jacobi Levels, Ramification Frobenius, Valuation Frobenius Epsilon

### Formalism/HermitianCurvature (1,922 files)

- *loose files* (68)
- **HermitianCurvatureProofs** (1,854): curvature computations; mostly one flat folder
  - **loose files** (1,810) **flat**
  - BesselDecayBounds (44). Words: norm, bessel, conv, growth.

### GroundTheory/HeightsAndTheta (6,410 files)

- **Heights** (6,348): Arakelov-style height theory
  - *loose files* (31)
  - ComplexAnalyticSets (994): complex analytic sets. Words: slice, normal, branch, germ.
  - HilbertSamuel (844): arithmetic Hilbert–Samuel theorem. Words: statements, block, section, fibre.
  - KleimanAmpleness (593): Kleiman's ampleness criterion. Words: imports, ample, twist, very.
  - DiscreteValuationNumbers (429). Words: statements, flag, blow, segre.
  - Intersections (385): intersection theory. Words: imports, statements, semiloc, chart.
  - HeightKernels (339). Words: dual, statements, chart, lines.
  - OrbitLimits (334). Words: chart, statements, curve, proj.
  - ArithmeticBezout (305): arithmetic Bézout theorem. Words: statements, cone, chow, chart.
  - HodgeLowerBound (276): Hodge-index-type lower bounds. Words: statements, flag, line, hodge.
  - RemainderTerms (175). Words: flag, comb, homogeneous, integral.
  - FiniteCovolume (168). Words: statements, lattice, unipotent, torus.
  - ElementarySymmetric (160). Words: inter, chart, frame, division.
  - FieldsOfNumbers (134). Words: statements, cone, semilocal, length.
  - *other: 34 folders* (1,181), e.g. Analytic Limit, Integral Models, Weighted Homogeneous, Vertical Divisors
- Theta (62). Words: fourier, cfun, real, statements.

### ReciprocityTheory/ReductiveGroups (2,799 files)

- **ArithmeticGeometry** (1,623): arithmetic geometry of reductive groups
  - *loose files* (1)
  - FundamentalDomains (194): fundamental domains (reduction theory). Words: coefficient, flow, lattice, isotropic.
  - ArakelovVolumes (189): Arakelov volumes. Words: interp, meas, onto, unfold.
  - BirationalGeometry (185): birational geometry, toroidal compactifications. Words: inter, bridge, good, push.
  - HeightTheory (183): heights. Words: height, disc, norm, substitution.
  - PullbackSections (165). Words: bridge, chart, model, place.
  - SquareIntegrability (136). Words: split, torus, norm, span.
  - TaylorDiscriminants (118). Words: gauge, wick, integral, connection.
  - DiscreteValuationRings (94). Words: theta, pull, valuation, thick.
  - ExtensionDescent (81). Words: base, pull, unif, change.
  - ArakelovGeometry (79). Words: sandwich, fibre, multi, homog.
  - ArithmeticIntersection (40). Words: length, inhabit, kappa, supp.
  - FirstCohomology (40). Words: lift, canonical, alpha, laws.
  - *other: 8 folders* (118), e.g. Rationality, Weighted Sum Bounds, Semiabelian Schemes, Place Divisors
- **DiscreteSeries** (1,021): discrete series representations
  - *loose files* (3)
  - LaplaceOperators (213): Laplace/Casimir operators. Words: norm, imports, lowest, weight.
  - MultiplicityOne (113): multiplicity one. Words: integrable, dicho, frame, haar.
  - FormalDegree (111): formal degrees. Words: haar, coef, polar, omega.
  - ExceptionalGroupG2 (96): the exceptional group G2. Words: formula, trace, decomp, props.
  - TensorRepresentations (88). Words: trace, formula, fock, coef.
  - DiscreteSeriesExistence (84): existence of discrete series. Words: smooth, datum, props, bridge.
  - CasimirCoefficients (73). Words: gelfand, chain, facts, continuous.
  - TailIntegrals (72). Words: heisenberg, formula, unitary, vector.
  - HighestWeights (61). Words: model, deriv, weyl, entry.
  - *other: 6 folders* (107), e.g. Trace Gap, Bochner Inequality, Infinitesimal Decay, Analytic Vectors
- UnramifiedIntegrals (125). Words: norm, defs, integral, unit.
- *other: 8 folders* (30), e.g. Symplectic Traces, Trace Formulas, Models, Lattice Embeddings

### CompanionTheory/SpectralGeometry (1,254 files)

- **LocalGlobalProofs** (1,250): local-to-global arguments
  - AdelicAnalysis (585): analysis on adelic groups. Words: gram, measure, product, fiber.
  - StableLattices (490): semistable lattices. Words: levi, congruence, decomposition, imports.
  - ConvexCones (135): convex cones. Words: cell, star, cone, function.
  - *other: 6 folders* (40), e.g. Weyl Group Actions, Smooth Morphisms, Global Theory, Nef Effective Cones
- CountingDefinitions (4). Words: count, euler, eval, mean.

## Word profiles of the flat folders

These folders have no subfolders, and namespaces don't split them either. The only cheap signal is which words appear in file names. A file can count under several words. This is rough: the spot check showed names are weak evidence.

| Folder | Files | Most common words in file names (share of files) |
|---|---|---|
| Proofs/DivisorProofs | 42,424 | integral 5%, theta 4%, point 4%, lattice 4%, pullback 3%, bundle 3%, unitary 3%, section 3%, base 3%, fibre 3% |
| Proofs/InertiaEigenvalues | 8,951 | lattice 7%, integral 5%, frobenius 5%, galois 4%, matrix 3%, norm 3%, unit 3%, prime 3%, kisin 3%, breuil 3% |
| Proofs/IwasawaDecomposition | 7,769 | level 6%, lattice 4%, frame 4%, base 4%, place 3%, point 3%, integral 3%, lift 3%, unitary 3%, prime 3% |
| Proofs/TwistedOperators | 6,642 | theta 9%, lattice 8%, place 7%, unitary 6%, level 5%, integral 5%, real 5%, weil 5%, split 4%, fock 4% |
| Proofs/DecoratedLatticeProofs | 5,063 | place 11%, theta 9%, lattice 9%, split 9%, level 8%, integral 8%, chain 5%, bessel 5%, true 5%, weil 4% |
| Proofs/FlagMeasures | 4,003 | lattice 12%, frame 8%, unitary 7%, hermitian 7%, unipotent 6%, integral 5%, bessel 5%, flag 5%, term 4%, measure 4% |
| Proofs/SatakeParameters | 3,462 | lattice 7%, place 7%, split 6%, integral 6%, prime 6%, kernel 5%, hecke 5%, dual 4%, level 4%, theta 4% |
| Proofs/FoundationProofs | 3,411 | integral 6%, theta 6%, level 6%, prime 5%, hecke 5%, norm 5%, series 5%, lattice 4%, dual 4%, modular 4% |
| Proofs/DegenerationProofs | 1,563 | torsion 11%, theta 10%, abelian 8%, model 8%, fibre 8%, point 8%, torus 7%, extension 6%, section 6%, closed 6% |
| Proofs/ModuliProofs | 1,539 | theta 10%, level 9%, abelian 7%, torsion 6%, family 5%, pullback 5%, ample 5%, scheme 5%, cover 5%, model 5% |
| Proofs/JetHarmonics | 1,417 | bessel 7%, integral 6%, level 6%, series 6%, norm 5%, depth 5%, chart 5%, theta 4%, capelli 4%, prime 4% |
| Proofs/GlobalInterpolation | 1,298 | lattice 7%, integral 6%, prime 6%, unitary 5%, dual 5%, norm 5%, class 4%, theta 4%, level 3%, period 3% |
| ThetaPairLifts/ThirdPlaceSeries | 2,251 | imports 4%, level 4%, rows 3%, good 2%, galois 2%, side 2%, base 2%, read 2%, split 2%, datum 2% |
| Proofs/BlockDecomposition | 8,354 | integral 5%, compact 4%, product 3%, character 3%, norm 3%, lattice 3%, whittaker 2%, continuous 2%, open 2%, formula 2% |
| Proofs/GeometryProofs | 3,001 | hodge 10%, model 8%, lattice 7%, frame 6%, point 5%, chart 5%, generic 5%, field 4%, component 4%, degree 4% |
| Proofs/MetricProofs | 1,576 | flag 14%, chart 10%, frame 7%, resolution 5%, analytic 5%, adjacent 4%, point 4%, metric 4%, degree 4%, integral 4% |
| HermitianCurvature/HermitianCurvatureProofs | 1,810 | germ 3%, parts 3%, level 2%, norm 2%, block 2%, smooth 2%, integral 2%, compact 2%, slice 2%, integrable 1% |

## Things I noticed while doing this

- **The main effort, by size:** `DivisorProofs` alone is 24% of all files. Add the theta-lift, modularity and mass-formula blocks and you have most of the project.
- **Many famous theorems appear as by-products**, going by names: resolution of singularities, étale cohomology and purity, class field theory, Poitou–Tate, Chebotarev, Siegel–Weil, the unitary dual, a modularity/patching argument, local Langlands. Each would be a major formalisation by itself. Whether the statements match their names is unchecked.
- **The giants are flat.** 17 folders of over 1,000 files have no subfolders at all, and `DivisorProofs` has 42,424 files in one directory. Their word profiles are generic (integral, lattice, theta), so names can't tell us how they are organised. The import graph could.
- **Leftover scaffolding:** `Lemmata` has 167 generically named one-file folders ("GeneralBFactLeftBisAlt"), and many theorems have names like `proof`, `key`, `main`. This looks machine-organised.
- **Worth a human look:** `ReciprocityTheory/Hypotheses` (3 files of named conditions) and `Development/AbelianVarietyTheory/Counterexamples`.
