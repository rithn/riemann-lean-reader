You are writing entries for a public prerequisite tree of a huge Lean 4 project (a claimed, unverified proof of the Riemann hypothesis), for curious readers whose maths stops at school level plus first-year linear algebra, probability and graph theory.

Everything you need is in ONE file: {BUNDLE}. Read it fully with the Read tool, in pages of 1500 lines (offset/limit) until the end. It lists your chunks ({CHUNKS}), the files you own with the node id to use, files already mapped elsewhere (link by id only), a map from restatement names to node ids (proofs cite those names), the existing concept/leaf nodes, and the source of every owned file with real line numbers. Do not open any other file; work only from the bundle. Never run any code from the project.

For each chunk write {FRAGDIR}/<chunk>.yaml with the Write tool: a YAML mapping {nodes: [...]}. A chunk with nothing new to write gets no file. Per owned file:
  id: (given)   title: short plain English   kind: step   status: explained   chunk: <chunk id>
  plain: >  (style rules below)
  lean: [path:line of the main declaration, using the bundle's line numbers]
  mathlib: [main Mathlib lemmas leaned on, if any; may be empty]
  needs: [ids of owned/mapped files it uses + concept/leaf ids]
Set orphan: true on the chunk's orphan node named in the bundle, and on any owned node that nothing else needs.
Reuse existing concepts. Invent one (id concept-<kebab>, kind: concept, status: textbook, plain, needs: [existing ids], learn: [{title: "Author, Book", where: "ch. ..."}]) only if nothing fits; check the list for near-duplicates; keep it general; define it once, in the first fragment that needs it.

Plain-English style:
- 60-130 words, short sentences, no Lean syntax or names.
- Explain each technical term in a few everyday words the first time; prefer one tiny concrete example.
- Say what the file states, then the idea of the proof if any.
- If a file only states a claim (a named Prop / "Statement") without proving it, or proves something only by assuming other claims, say so in the first sentence.
- Accurate over fluent; if unsure, say so in the text.

When all fragments are written, check they parse, in one command:
uv run -q --with pyyaml python -I -c "import yaml,sys,glob; [print(f, len(yaml.safe_load(open(f))['nodes'])) for f in sorted(glob.glob(sys.argv[1]+'/*.yaml'))]" {FRAGDIR}
Fix any parse error in your own files. Edit nothing else. Finish with one line: DONE <number of nodes written>.
