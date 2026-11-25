# Reader's guide to the Lean proof of the Riemann hypothesis

On 20 Nov 2026 Levent Alpöge released a [Lean formalization and announcement note](https://alpo.ge/remark.pdf) for a proof of the Riemann hypothesis developed with Claude. On 21 Nov the [Lean FRO and Mathlib Initiative](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) certified the formal statement and proof. [Andrew Sutherland's verification log](https://math.mit.edu/~drew/grh/) records independent builds, kernel checks, and comparisons with the target theorem.

The release contains 175,187 Lean files and about 17.4 million lines. [RH Lean Explorer](https://riemannhypothesissolved.com/) maps the source, links to [reading guides](https://riemannhypothesissolved.com/guides/), and maintains a dated [verification status](https://riemannhypothesissolved.com/status/). This repository contains the site's generator and the original source-text audit. The original folder descriptions are inferred from file and folder names.

## What's here

| File | What it is |
|---|---|
| [FINDINGS.md](FINDINGS.md) | The launch-day source audit, including the main theorem, its definitions, and a keyword scan. |
| [FOLDERS.md](FOLDERS.md) | Best-guess guide to every folder. It goes deeper wherever a folder has more than 1,000 files, and gives word profiles for the huge flat folders. |
| [evidence/](evidence/) | sha256 of the archive and its parts, plus raw search hits. |
| [scripts/](scripts/) | The scripts that produced the above, so you can regenerate or improve it. |

## Key facts (details and file:line evidence in FINDINGS.md)

- **The statement uses only Mathlib's own definitions.** The headline theorem is `riemannHypothesis : RiemannHypothesis` (`Main.lean:4`), using Mathlib's long-standing definition. The restated versions live in `Statements.lean`, which imports nothing but Mathlib.
- **The source-text audit found no matches for the scanned keywords.** The scan checked `sorry`, `axiom`, `admit`, `native_decide`, `implemented_by`, `extern`, `csimp`, `unsafe`, `opaque`, `skipKernelTC` and `ofReduceBool`.
- **The last steps of the proof are short and readable.** "No zeros to the right of ½" implies RH via the functional equation (`Formalism/GammaFactorNonvanishing/`).

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

- **Correct the folder guesses** in FOLDERS.md by opening an issue or PR, ideally with a file you actually read.
- **Map the import graph,** especially for the flat folders with 40k files, where names don't help.

Prepared with Claude Code. Corrections are very welcome.
