#!/bin/bash
# Naming loop: AGENTS parallel `claude -p` sessions (Sonnet, medium), one bundle each, until all
# bundles have an answer, a session fails, a usage limit is hit, or a STOP file appears.
#
# usage: scripts/cluster/name_loop.sh <cluster dir> [max_rounds] [agents] [naming subdir, default naming]
#   e.g. scripts/cluster/name_loop.sh ../notes/cluster2 1 1      (pilot: one bundle)
# Answers go to <dir>/naming/out/bundle-NNNN.yaml. Each session may only Read, Write
# (via acceptEdits, run from inside the naming dir) and `uv run`.
set -u
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
DIR="$(cd "$1" && pwd)"; MAX=${2:-100000}; AGENTS=${3:-6}
N="$DIR/${4:-naming}"; OUT="$N/out"; mkdir -p "$OUT" "$N/logs"
for ((r = 1; r <= MAX; r++)); do
  [ -f "$N/STOP" ] && { echo "$(date +%T) STOP file found"; exit 0; }
  todo=()
  for b in "$N"/bundle-*.md; do
    k=$(basename "$b" .md); [ -s "$OUT/$k.yaml" ] || todo+=("$k")
    [ ${#todo[@]} -ge "$AGENTS" ] && break
  done
  [ ${#todo[@]} -eq 0 ] && { echo "$(date +%T) all bundles named"; exit 0; }
  echo "$(date +%T) round $r: ${todo[*]}"; start=$(date +%s); pids=()
  for k in "${todo[@]}"; do
    prompt=$(sed -e "s|{BUNDLE}|$N/$k.md|g" -e "s|{CONCEPTS}|$N/concepts.md|g" -e "s|{OUT}|$OUT/$k.yaml|g" \
             "$REPO/scripts/cluster/namer_prompt.md")
    ( cd "$N" && claude -p "$prompt" --model sonnet --effort medium --permission-mode acceptEdits \
        --allowedTools "Read" "Write" "Bash(uv run:*)" --output-format json \
        > "logs/$k.json" 2> "logs/$k.err" ) &
    pids+=($!)
  done
  fail=0; for p in "${pids[@]}"; do wait "$p" || fail=$((fail + 1)); done
  errs=0; limit=0; tok=0
  for k in "${todo[@]}"; do
    jq -e '.is_error == true' "$N/logs/$k.json" >/dev/null 2>&1 && errs=$((errs + 1))
    grep -qiE 'usage limit|limit reached|limit will reset|rate.?limit' "$N/logs/$k.json" "$N/logs/$k.err" 2>/dev/null && limit=$((limit + 1))
    t=$(jq '.usage // {} | ((.input_tokens//0)+(.cache_creation_input_tokens//0)+(.output_tokens//0))' "$N/logs/$k.json" 2>/dev/null || echo 0)
    tok=$((tok + ${t:-0}))
  done
  echo "  $(( $(date +%s) - start ))s, tokens(in+cache-write+out)=$tok, failed=$fail, errors=$errs, limit hits=$limit"
  NAMING="${4:-naming}" uv run -q --with pyyaml python -I "$REPO/scripts/cluster/name_check.py" "$DIR" "${todo[@]}"
  if [ "$fail" -gt 0 ] || [ "$limit" -gt 0 ] || [ "$errs" -gt 0 ]; then
    echo "$(date +%T) stopping (failure or usage limit). Rerun later; unanswered bundles are picked up again."; exit 2
  fi
done
