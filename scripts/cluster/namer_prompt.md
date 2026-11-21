You are naming topic clusters for a public guide to a huge Lean 4 project (a claimed, unverified proof of the Riemann hypothesis). Readers know school maths plus first-year linear algebra, probability and graph theory.

Read two files fully with the Read tool (pages of 1500 lines): {BUNDLE} and {CONCEPTS}. Do not open any other file. Never run any code from the project.

The bundle lists clusters. Each is a group of 1-50 Lean files that a computer grouped by shared vocabulary and imports. For each you get: its theme's frequent words, size, folders, frequent words, concepts already linked, the clusters it uses, and every file's name with its main statement (proofs are not shown).

Write {OUT} with the Write tool: a YAML mapping {clusters: [...]}, one entry per cluster in the bundle, same order:
  id: (given)
  title: short plain English, at most 10 words
  plain: >  60-130 words (style below)
  concepts: [ids from {CONCEPTS} this cluster relies on; may be empty]
  new_concepts: [kebab-case names of textbook topics it needs that are missing from the list; may be empty]
  source: {title: "Author, Book", where: "ch. ..."}   one standard textbook or survey covering the topic, or null if none fits
  coherent: yes | mixed | unclear   (mixed = the files do two or more unrelated jobs; say which in plain)
  confidence: high | medium | low   (how sure you are of the description, from names and statements alone)

Plain-English style:
- Short sentences, no Lean syntax or identifiers.
- Explain each technical term in a few everyday words the first time.
- Say what the cluster's files state together, and what role the cluster seems to play.
- If most files only state claims (names ending in Statement, definitions of type Prop) or prove things by assuming other claims, say so.
- You only see statements, not proofs: never claim a proof is complete or correct.
- Many names are the project's own abbreviations; do not guess their meaning beyond what the statements show. If unsure, say so.

When done, check it parses, in one command:
uv run -q --with pyyaml python -I -c "import yaml,sys; d=yaml.safe_load(open(sys.argv[1])); print(len(d['clusters']))" {OUT}
Fix any parse error. Edit nothing else. Finish with one line: DONE <number of clusters written>.
