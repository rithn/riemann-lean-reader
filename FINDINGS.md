# Reader's notes: the claimed Lean proof of the Riemann hypothesis

Compiled 20 Nov 2026 from public downloads only. **This is a reading of the claim's source code. It is not a check of the proof.**
Nothing here was compiled. `#print axioms` was **not** run (see §4).

Lean paths below are relative to `lean/src/` inside the archive. This repo does not include the Lean source; download it from alpo.ge.

---

## 1. Sources

| Item | Value |
|---|---|
| Note | https://alpo.ge/remark.pdf. 4 pages, no author name, no title. PDF created 2026-11-20 12:52:48Z (pdfTeX). sha256 `3fc97784…a0cfeb8d`. |
| Host | alpo.ge is Levent Alpöge's homepage. The homepage itself does not link to the note; I found it by guessing the URL `remark.pdf`. |
| Lean source | The note's footnote 1 points to `https://alpo.ge/lean.tar.gz.part01` … `part14`. That is 13 parts of 18,000,000 bytes plus 5,275,554 bytes, **239,275,554 bytes (~239 MB) compressed**. This confirms the "~240 MB" figure. |
| Joined archive | sha256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`. Per-part hashes are in `evidence/SHA256SUMS`. |
| Unpacked size | ~1.27 GB. 175,190 regular files: 175,187 `.lean` files plus `lakefile.toml`, `lake-manifest.json` and `lean-toolchain`. |
| Archive safety | No symlinks, no absolute paths, no `..` paths. All timestamps are set to 1970 (normalised), so they carry no date information. |
| Commit / hash | **None.** There is no `.git` folder in the archive and no repository is linked. The archive's sha256 above is the only fixed identifier. |
| Lean version | `leanprover/lean4:v4.33.1` (`lean-toolchain`). This is a real release, dated 2026-08-21. |
| Mathlib | Commit `0df444a360eaa60ab8c11dca51a86af692955474` (`lakefile.toml`, `lake-manifest.json`). It is a real commit, dated 2026-08-21 ("chore: bump toolchain to v4.33.1"). |
| Lean code | 17,374,215 lines in total. |
| Build settings | `lakefile.toml`: `maxHeartbeats = 4000000` (the default is 200000), `--tstack=400000`, `autoImplicit = false`. The lakefile is plain TOML, so it runs no project code at configure time. Mathlib's own `lakefile.lean` would run as usual. |

## 2. The main theorem

`Main.lean:4`

```lean
theorem riemannHypothesis : RiemannHypothesis := rhOfAll
```

`RiemannHypothesis` here is **Mathlib's own definition**. At the pinned commit it is `Mathlib/NumberTheory/LSeries/RiemannZeta.lean:185-186`:

```lean
def RiemannHypothesis : Prop :=
  ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2
```

In plain English: take any complex number s.
- `riemannZeta s = 0`: s is a zero of the zeta function. Mathlib's `riemannZeta` is the analytically continued function, defined on all of ℂ.
- `¬∃ n : ℕ, s = -2 * (n + 1)`: s is not one of the "trivial zeros" −2, −4, −6, …
- `s ≠ 1`: excludes the pole. Mathlib assigns zeta a placeholder value at s = 1, so that point has to be ruled out by hand.
- Conclusion `s.re = 1 / 2`: the real part of s is ½.

That is the standard statement of RH.

`Statements.lean` (imports **only** `Mathlib`) restates it in its own words and adds GRH-type statements for Dirichlet L-functions. `Main.lean:6-12` proves each one:

| Lean name (`Main.lean`) | Statement (`Statements.lean`) | Plain English |
|---|---|---|
| `riemannZeta_eq_zero_re` (l.6) | `RiemannZetaZerosOnLine` (l.3-4) | Identical in content to Mathlib's `RiemannHypothesis`. |
| `LFunction_ne_zero_of_half_lt_re` (l.8) | `DirichletLNonvanishingRightOfHalf` (l.6-8) | For every modulus N, every Dirichlet character χ mod N, and every s with Re s > ½: L(χ, s) ≠ 0. The only exception is the pole (χ trivial and s = 1). This is GRH for Dirichlet L-functions, stated as "no zeros to the right of ½". |
| `LFunction_eq_zero_re` (l.10) | `DirichletLZerosOnLine` (l.10-12) | Every zero of L(χ, s) with 0 < Re s < 1 has Re s = ½. |
| `LFunction_eq_zero_re_of_isPrimitive` (l.12) | `PrimitiveDirichletLZerosOnLine` (l.14-16) | The same, for primitive χ. |

"GRH" in the Lean statements means **Dirichlet L-functions only**. The note also says it "expect[s], with more time, the Extended Riemann Hypothesis". That part is not claimed in Lean.

## 3. Definitions the statements depend on

The key risk in any formal claim is a custom definition that quietly changes the meaning. **Here the top-level statements use only Mathlib's definitions.**

- `Statements.lean:1` is `import Mathlib` and nothing else. So `riemannZeta`, `DirichletCharacter`, `DirichletCharacter.LFunction` and `IsPrimitive` in that file can only be Mathlib's.
- In `Main.lean:4`, `RiemannHypothesis` resolves to Mathlib's. I searched all 175k files for a declaration or redefinition of `RiemannHypothesis`, `riemannZeta`, `completedRiemannZeta` or `hurwitzZeta`. I also searched for `notation`, `macro`, `syntax` or `export` lines touching those names, and for a top-level `LFunction`. **No hits.**
- The project does define two functions called `LFunction`, but each sits inside its own namespace:
  - `GroundTheory/AutomorphicForms/GL2/GJLocalZeta.lean:431`, in `GroundTheory.Automorphic.GodementJacquet`
  - `GroundTheory/GlobalFields/TateThesis/HeckeLFunction.lean:363`, in `GroundTheory.Global`

  Neither is visible in `Statements.lean`.
- **What remains to trust:** Mathlib's `riemannZeta` / `LFunction` are what they claim to be (widely used and reviewed), and the Mathlib commit is unmodified. Lake fetches it from GitHub at the pinned hash; it is not shipped in the archive.

### The chain from the main theorem down (all read by me)

- `Main.lean:4` `riemannHypothesis := rhOfAll`
- `Supplements/Kernels/MainTheorems.lean:9` `rhOfAll := Formalism.VW.rh_of_every allChi`
- `Formalism/GammaFactorNonvanishing/CritLine.lean:29-32` `rh_of_every`: GRH for the trivial character mod 1 is the statement for ζ (`LFunction_modOne_eq`).
- `Formalism/GammaFactorNonvanishing/RhOfRight.lean:5-…` `rh_of_right`: "no zeros with Re s > ½" implies RH, using Mathlib's functional equation `riemannZeta_one_sub`.
  - This reduction is short and standard. It matches footnote 2 of the note ("because the reals are totally ordered…").
- `Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean:13-14` defines `UpperTheory.EveryCharacter`. It is word for word the same as `DirichletLNonvanishingRightOfHalf`, written with Mathlib's objects.
- `Supplements/Kernels/MainTheorems.lean:7` `allChi := UpperTheory.FinalTheorems.everyCharacter`
- `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7-11` `everyCharacter := everyCharacter_of_row galoisLocalGlobalStrong_recParameter` (`…/GaloisRepresentations/IntegralStructures/RowSrc.lean:6`)
  - It also passes an `OpenLiteratureStatements` bundle, built from proved theorems.
- `…/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:215-218`: `OpenLiteratureStatements` has three fields, named after big published results:
  - `caraianiLocalGlobalDual`
  - `localLanglandsExists`
  - `galoisRepOfPolarizedPairLit`

  These are **not assumed**: `MainConclusion.lean:8` supplies them from theorems. So the development claims to formalise those results too, which is a big claim in its own right. Lines 219-245 likewise take Deligne–Ribet, Siegel–Klingen, Hecke–Tate functional equations and others from `…_holds` theorems in the project.

Below this, the 17M lines are the actual argument. I did not read it.

## 4. Axioms and red-flag keywords

**Not built, so `#print axioms riemannHypothesis` was not run.** Reasons:
- No Lean toolchain is installed on this machine.
- The project is ~17.4M lines, several times the size of Mathlib.
- Even with Mathlib's cache, the project itself would have to be compiled from scratch, with heartbeat limits raised 20×. On a typical laptop that is days at best, and may not fit in memory.

Text search over all 175,187 `.lean` files, with the counts confirmed by fixed-string whole-word search:

| Keyword | Hits |
|---|---|
| `axiom` | 0 |
| `sorry` / `sorryAx` | 0 |
| `admit` | 0 |
| `native_decide` | 0 |
| `implemented_by` | 0 |
| `extern` | 0 |
| `csimp` | 0 |
| `unsafe` | 0 |
| `opaque` | 0 |
| `debug.skipKernelTC` | 0 |
| `Lean.ofReduceBool` / `trustCompiler` | 0 |

Other things worth knowing (hit lists in `evidence/`; re-run with `scripts/scan_keywords.sh`):
- `run_cmd Lean.modifyEnv`: 5 files, `BuildAid/D1.lean:4` to `D5.lean:4`. Each only adds a namespace (CompanionTheory, CrystallineSemistableComparison, GlobalTheory, PositivityTheory, UpperTheory) to `LibrarySuggestions.nameDenyListExt`. That is a search-hint deny list. It adds no declarations.
- Custom meta-programming. `import Lean` appears only in `Formalism/LocalToGlobal/IndefiniteReal/HeckeNonvanishing/Imports.lean:1` and `Formalism/LocalToGlobal/NumberFieldFamilies/OwnStruct.lean:1`.
  - `Imports.lean:5-8` defines tactic `kexactB`, which assigns the goal **without an elaborator type check**. `OwnStruct.lean:53,60` defines `kcopy` / `#kcopy_probe`.
  - `Formalism/HermitianCurvature/HermitianCurvatureProofs/CutCptCopy.lean:87` defines the command `cpt_copy_thms`, which calls `addDecl` to copy theorems.
  - None of these bypass Lean's kernel, which re-checks every declaration. But they mean "it elaborated" is not the same as "it's kernel-checked" until someone actually builds the project.
- `simp (config := {decide := true})`: 26 occurrences, ordinary kernel-checked `decide`. 1,695 `local notation` and ~100 macros. These are local proof conveniences and cannot affect `Statements.lean`.

**Bottom line for §4:** no listed escape hatch appears anywhere in the text. That is *necessary, not sufficient*. Only a full build plus `#print axioms` (expected: `propext`, `Classical.choice`, `Quot.sound`) would confirm it. Ideally the build would also be re-checked with an independent kernel checker such as `lean4checker` or nanoda.

## 5. Structure

| Folder | .lean files | Lines | Size |
|---|---|---|---|
| Development | 141,928 | 12.2M | 1.0 GB |
| Formalism | 18,254 | 3.2M | 195 MB |
| GroundTheory | 8,507 | 1.1M | 71 MB |
| ReciprocityTheory | 3,845 | 563k | 35 MB |
| CompanionTheory | 2,027 | 194k | 15 MB |
| PositivityTheory | 449 | 55k | 3.8 MB |
| Lemmata | 167 | 9k | 0.8 MB |
| BuildAid | 5 | 20 | (search deny-lists) |
| Supplements | 3 | 22 | `Kernels/`: the final glue theorems |
| `Statements.lean`, `Main.lean` | 2 | 28 | the statements and the headline theorems |

What each part appears to cover, judging only from folder and file names:
- **Development/AbelianVarietyTheory**: 99k files, the bulk of the project.
- **Development/AutomorphicArithmetic**: 18k files. Theta correspondence, local Langlands, Galois representations, `CharacterBoxes` (where the final GRH statement is assembled).
- **Development/AutomorphicSpectrum** (15k), **Development/WeilBound** (7k), **Development/EtaleCohomology** (1.4k).
- **Formalism**: LocalToGlobal, PeriodIntegrals, SharpRestriction, HermitianCurvature, ZeroFreeRegion, GammaFactorNonvanishing (the final RH reduction).
- **GroundTheory**: background theories such as heights and theta, global and local fields, Tate's thesis, p-adic Hodge theory, Brauer groups, profinite and Tate cohomology.

These match the note's timeline: theta lifts, unitary groups, Bessel/GGP periods, Iwasawa towers, Chowla–Selberg, Siegel mass, relative trace formula.

Largest single files are 0.3–0.9 MB each, which is machine-scale. For example:
- `Formalism/HermitianCurvature/HermitianCurvatureProofs/IsAdmissibleSplittingCharPairMulTwist.lean` (914 KB)
- `Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities/FixPiIff.lean` (732 KB)

**Where the core argument lives:** the final glue is in `Development/AutomorphicArithmetic/CharacterBoxes/` and `Formalism/GammaFactorNonvanishing/`. The real mathematical content sits upstream of `UpperTheory.Top.plugAll` (`EveryCharacter.lean:16`) and `galoisLocalGlobalStrong_recParameter`, which spread across most of `Development`.

## 6. What I could not check

- Whether the project compiles at all, and whether the Lean kernel accepts it.
- `#print axioms` output.
- Any of the mathematics. I read ~10 short top-level files out of 175k.
- That Mathlib at `0df444a3` is unmodified and correct. It is fetched from GitHub; I only fetched the two files that define the statements.
- Whether the archive on alpo.ge will stay the same. Compare against the sha256 in §1.
- Who wrote the note. It is unsigned, but hosted on Alpöge's personal domain.

## 7. Open questions

1. Will someone with large compute do an independent full build and publish the `#print axioms` output for `riemannHypothesis`?
2. Does the archive also build cleanly with an independent kernel checker (`lean4checker`, external checkers)?
3. How long does a build take, and how much memory does it need? The 20× heartbeat limit suggests it is heavy.
4. Is there a git repository with history? A tarball with zeroed timestamps gives no provenance.
5. The project claims formal proofs of local Langlands existence, Caraiani-type local–global compatibility and Deligne–Ribet as by-products. Each of those would be news by itself. Do the definitions inside them mean what their names say? (This matters for understanding, not for the soundness of the final statement.)
6. When will there be a human-readable written account? The note says one is intended.

## 8. What acceptance would still need

- **Independent rebuilds** by several groups, from the published hash, with `#print axioms` showing only the three standard axioms, plus an external kernel re-check.
- **Expert review of the statement**: confirm that `Statements.lean`, `Main.lean` and the Mathlib definitions say what RH/GRH say. This part is small and could be done quickly.
- **A written paper** that experts in automorphic forms and number theory can read and referee. Formal verification shows the argument is valid; it does not explain it. The community will want to understand the proof as well as trust it.
- **Time.** No independent person had checked anything as of 20 Nov 2026.
