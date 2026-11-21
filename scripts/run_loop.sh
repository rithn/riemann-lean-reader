#!/bin/bash
# Mapping loop: prepare a round -> 6 parallel `claude -p` mappers (Sonnet, medium) -> merge.
# Repeats until every chunk is done, a mapper fails, or the usage limit is hit.
#
# usage: scripts/run_loop.sh [max_rounds] [agents] [lines_per_agent]
# Run it in tmux:  tmux new -s mapping 'scripts/run_loop.sh 2>&1 | tee -a ../notes/batches/loop.log'
#
# Work files (bundles hold the project's Lean source) go to ../notes/batches, outside the repo.
# Each mapper may only Read, Write (inside its batch dir, via acceptEdits) and run `uv run`.
set -u
REPO="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(cd "$REPO/.." && pwd)/notes/batches"
MAX=${1:-100000}; AGENTS=${2:-6}; LINES=${3:-5000}
PY=(uv run -q --with pyyaml python -I)
mkdir -p "$WORK"

for ((r = 1; r <= MAX; r++)); do
  if [ -f "$WORK/STOP" ]; then echo "$(date +%T) STOP file found, stopping"; exit 0; fi
  prep=$("${PY[@]}" "$REPO/scripts/batch.py" prepare "$WORK" "$AGENTS" "$LINES") || { echo "prepare failed"; exit 1; }
  if jq -e '.done' >/dev/null 2>&1 <<<"$prep"; then echo "$(date +%T) all chunks done"; exit 0; fi
  bdir=$(jq -r .dir <<<"$prep"); b=$(jq -r .batch <<<"$prep"); n=$(jq '.agents|length' <<<"$prep")
  echo "$(date +%T) round $r: batch $b, $(jq -r .files <<<"$prep") files, $n agents"
  start=$(date +%s); pids=()
  for ((k = 0; k < n; k++)); do
    bundle=$(jq -r ".agents[$k].bundle" <<<"$prep"); chunks=$(jq -r ".agents[$k].chunks|join(\", \")" <<<"$prep")
    prompt=$(sed -e "s|{BUNDLE}|$bundle|g" -e "s|{CHUNKS}|$chunks|g" -e "s|{FRAGDIR}|$bdir/fragments|g" \
             "$REPO/scripts/mapper_prompt.md")
    ( cd "$bdir" && claude -p "$prompt" --model sonnet --effort medium --permission-mode acceptEdits \
        --allowedTools "Read" "Write" "Bash(uv run:*)" --output-format json \
        > "agent-$k.json" 2> "agent-$k.err" ) &
    pids+=($!)
  done
  fail=0
  for p in "${pids[@]}"; do wait "$p" || fail=$((fail + 1)); done
  secs=$(( $(date +%s) - start ))
  errs=$(cat "$bdir"/agent-*.json 2>/dev/null | jq -s '[.[] | select(.is_error == true)] | length' 2>/dev/null || echo "?")
  limit=$(cat "$bdir"/agent-*.json "$bdir"/agent-*.err 2>/dev/null | grep -ciE 'usage limit|limit reached|limit will reset|rate.?limit' || true)
  tok=$(cat "$bdir"/agent-*.json 2>/dev/null | jq -s '[.[] | .usage // {} | ((.input_tokens//0)+(.cache_creation_input_tokens//0)+(.output_tokens//0))] | add' 2>/dev/null || echo "?")
  merged=$("${PY[@]}" "$REPO/scripts/batch.py" merge "$bdir")
  echo "  ${secs}s, tokens(in+cache-write+out)=$tok, failed=$fail, error results=$errs, limit hits=$limit"
  echo "  merged: $merged"
  "${PY[@]}" "$REPO/scripts/progress.py" next 0 >/dev/null
  if [ "$fail" -gt 0 ] || [ "$limit" -gt 0 ] || [ "$errs" != "0" ]; then
    echo "$(date +%T) stopping after batch $b (usage limit or failure). Rerun later; unfinished chunks are picked up again."
    exit 2
  fi
done
echo "$(date +%T) reached max rounds ($MAX)"
