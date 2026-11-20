# Reader's guide to the claimed Lean proof of the Riemann hypothesis

> **This is a map, not a check.** Nothing here was compiled and no proofs were read. The folder descriptions are guesses from file and folder names. In a spot check, one of two sampled guesses was wrong.

On 20 Nov 2026 an unsigned note appeared at [alpo.ge/remark.pdf](https://alpo.ge/remark.pdf), claiming a proof of the Riemann hypothesis formalised in Lean with Claude. The Lean source is linked from the note's footnote as `lean.tar.gz.part01`–`part14`. As of writing, no one independent has verified it.

The source is hard to approach: 175,187 Lean files, 17.4 million lines, and not a single comment. This repo is a starting point for anyone who wants to read it.

## What's here

| File | What it is |
|---|---|
| [FINDINGS.md](FINDINGS.md) | Where the main theorem is, what it states in plain English, which definitions it relies on, and the keyword scan (no `sorry`, `axiom`, `native_decide`, …). Also lists what is still unchecked. |
| [FOLDERS.md](FOLDERS.md) | Best-guess guide to every folder. It goes deeper wherever a folder has more than 1,000 files, and gives word profiles for the huge flat folders. |
| [evidence/](evidence/) | sha256 of the archive and its parts, plus raw search hits. |
| [scripts/](scripts/) | The scripts that produced the above, so you can regenerate or improve it. |

## Key facts (details and file:line evidence in FINDINGS.md)

- **The statement uses only Mathlib's own definitions.** The headline theorem is `riemannHypothesis : RiemannHypothesis` (`Main.lean:4`), using Mathlib's long-standing definition. The restated versions live in `Statements.lean`, which imports nothing but Mathlib.
- **The text has no escape hatches.** There are zero hits for `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `csimp`, `unsafe`, `opaque`, `skipKernelTC` and `ofReduceBool`. This is a text search, not a kernel check.
- **The last steps of the proof are short and readable.** "No zeros to the right of ½" implies RH via the functional equation (`Formalism/GammaFactorNonvanishing/`).
- **The build has not been verified.** `#print axioms` has not been run by me. The project is several times the size of Mathlib.

## Get the same source

```sh
for i in $(seq -w 1 14); do curl -O "https://alpo.ge/lean.tar.gz.part$i"; done
cat lean.tar.gz.part{01..14} > lean.tar.gz
shasum -a 256 lean.tar.gz   # expect 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc
tar -xzf lean.tar.gz        # -> lean/  (lakefile.toml, lean-toolchain, src/)
```

The archive is not redistributed here: it is the author's work and carries no licence.

## Regenerate the index and folder guide

```sh
python scripts/build_index.py lean/src file_index.tsv    # one row per file (~69 MB)
python scripts/folder_tree.py file_index.tsv             # writes adapt.json
python scripts/render_tree.py file_index.tsv             # writes partB.json (markdown lines)
scripts/scan_keywords.sh lean/src                        # the keyword scan
```

`build_index.py` reads files as text only. Nothing here runs Lean or any code from the archive.

## Help wanted

- **Run a full build** and post `#print axioms riemannHypothesis`. Bonus: an independent kernel re-check (`lean4checker` or similar).
- **Correct the folder guesses** in FOLDERS.md by opening an issue or PR, ideally with a file you actually read.
- **Map the import graph,** especially for the flat folders with 40k files, where names don't help.

Prepared with Claude Code. Corrections are very welcome.
