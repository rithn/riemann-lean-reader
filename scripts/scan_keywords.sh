#!/usr/bin/env bash
# Text search for Lean "escape hatches" over an unpacked copy of the archive.
# Usage: scripts/scan_keywords.sh path/to/lean/src
set -euo pipefail
cd "$1"
for w in axiom sorry admit native_decide implemented_by extern csimp unsafe opaque skipKernelTC ofReduceBool sorryAx trustCompiler; do
  echo "$w: $(grep -rlwF --include='*.lean' "$w" . | wc -l | tr -d ' ') files"
done
echo "run_cmd/#eval/initialize:"; grep -rnE --include='*.lean' 'run_cmd|run_elab|run_meta|#eval|initialize\s' . || true
echo "import Lean:"; grep -rnE --include='*.lean' '^import\s+Lean' . || true
