# Reader's guide to the Lean proof of the Riemann hypothesis

On 20 Nov 2026 Levent Alpöge released a [Lean formalization and announcement note](https://alpo.ge/remark.pdf) for a proof of the Riemann hypothesis developed with Claude. On 21 Nov the [Lean FRO and Mathlib Initiative](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) certified the formal statement and proof. [Andrew Sutherland's verification log](https://math.mit.edu/~drew/grh/) records independent builds, kernel checks, and comparisons with the target theorem.

The release contains 175,187 Lean files and about 17.4 million lines. [RH Lean Explorer](https://riemannhypothesissolved.com/) maps the source, links to [reading guides](https://riemannhypothesissolved.com/guides/), and maintains a dated [verification status](https://riemannhypothesissolved.com/status/). This repository contains the site's generator and the original source-text audit. The original folder descriptions are inferred from file and folder names.

**How to cite** — Cite the Alpöge original dataset on Zenodo. [10.5281/zenodo.24628409](https://doi.org/10.5281/zenodo.24628409)

## Find the import graph and source

The Explorer publishes static JSON under `/api/` and `/data/`. Start with the API catalogue for endpoint descriptions and the edition index for the full source revision of each map. [API catalogue](https://riemannhypothesissolved.com/api/) · [OpenAPI JSON](https://riemannhypothesissolved.com/api/openapi.json) · [Edition index](https://riemannhypothesissolved.com/api/editions.json)

| Edition | Where to look |
|---|---|
| Alpöge original | The [cluster index](https://riemannhypothesissolved.com/api/clusters.json) maps an ID to its current page. The [map overview](https://riemannhypothesissolved.com/data/overview.json) has cluster coordinates and import edges in `clusters[].uses`, expressed as cluster numbers such as `677` for `k0677`. The [cluster detail](https://riemannhypothesissolved.com/data/c/k0677.json) lists modules in `files[].m` and their direct imports in `files[].imp`. The [module index](https://riemannhypothesissolved.com/data/modules.json) provides the reverse lookup in rows of `[folderIndex, moduleName, clusterNumber]`, with the module prefix in `folders[folderIndex]`. |
| Sernau readable | The [edition API](https://riemannhypothesissolved.com/api/sernau/index.json) links to groups, dependencies, and module source links. Read `overviewUrl` and `fileGraphUrl` from the [map manifest](https://riemannhypothesissolved.com/data/sernau/manifest.json) to find the versioned map JSON and file import graph. |

An import edge points from the importing module or group to its dependency. Record the edition and full source revision with a lookup so readers can distinguish the original archive from the readable rewrite.

### Reproduce a pinned lookup

Run this from the generator checkout with the built site at `../site-sharing`, or pass your build directory as the argument. This example looks up cluster `k0677`, finds its `Main` module, and reads the published copy of the file.

```sh
uv run --no-project python - ../site-sharing <<'PY'
import json
import sys
from pathlib import Path

site = Path(sys.argv[1])

def read_json(path):
    return json.loads((site / path).read_text(encoding="utf-8"))

edition = next(e for e in read_json("api/editions.json")["editions"] if e["id"] == "alpoge")
cluster_id = "k0677"
cluster = next(c for c in read_json("api/clusters.json")["clusters"] if c["id"] == cluster_id)
detail = read_json(f"data/c/{cluster_id}.json")
module = next(f for f in detail["files"] if f["m"] == "Main")
source_file = "src/" + module["m"].replace(".", "/") + ".lean"
assert (site / cluster["path"].lstrip("/") / "index.html").is_file()
source = (site / source_file).read_text(encoding="utf-8")
line, statement = next(
    (line, text) for line, text in enumerate(source.splitlines(), 1)
    if text.startswith("theorem riemannHypothesis :")
)
print(cluster_id, edition["revision"], f"{source_file}:{line}")
print(f'{edition["source"]}/blob/{edition["revision"]}/{source_file}#L{line}')
print(statement)
PY
```

For the current original archive pin, the first line is `k0677 40e56bab026552e089d7afcfeff08d2defb9c005 src/Main.lean:4`. [Pinned Main.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4)

### Report a correction

Open an issue in the generator repository. Include the edition, cluster ID, full source revision, file and line, plus the text or import edge to correct and the change the source supports. For example, use `Alpöge original · k0677 · 40e56bab026552e089d7afcfeff08d2defb9c005 · src/Main.lean:4` to identify the statement in the lookup above. [Generator GitHub issues](https://github.com/rithn/riemann-lean-reader/issues)

## Building the readable edition

The site generator builds Alpöge's original map and Sernau's readable edition together. The readable source, group inventory, English labels and theorem references are pinned in [data/sernau](data/sernau/edition.json). The first build fetches the exact upstream Git revision into a temporary object cache. Set `SERNAU_CACHE_DIR` to a durable location, or set `SERNAU_SOURCE_DIR` to a Git checkout at the pinned revision for an offline source build.

Run the full build with the usual original archive and cluster data and with the paired site worktree containing `sernau.js` and `sernau.css`.

```sh
RH_N3=./data uv run -q --with pyyaml --with networkx --with scipy --with markdown-it-py --with pillow \
  python -I scripts/site/build_site.py ../notes/cluster3 ../site
python -I scripts/site/check_editions.py ../site
```

`RH_N3=./data` uses the checked-in guide citations. The checker validates the readable source bytes, generated URLs and group links, plus the distinct original and readable versions of `Main.lean`. Pass `--baseline-revision <site-revision>` to also compare the original sitemap, redirects, map data and API against the site before this preview.

The build stages the site and generator state, verifies the sitemap and retained assets, then updates the paired checkout. For an existing site with original reader data, supply the original cross-reference inputs at the usual workspace path or through `RH_XREF`. A failed build keeps the previous release available.

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
- **Correct the import map** using the [source lookup and issue instructions](#report-a-correction) above.

Prepared with Claude Code. Corrections are very welcome.
