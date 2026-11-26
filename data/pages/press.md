---
title: "Riemann hypothesis proof: press, statements, reactions"
description: "Official statements and reporting on the Lean Riemann hypothesis proof, with sourced accounts of Jenny Lorraine Nielsen’s critique and Masullo’s claim."
h1: "Press, official statements and reactions"
path: /press/
target_queries:
  - riemann hypothesis proof news
  - riemann hypothesis mathematicians react
  - riemann hypothesis anthropic reaction
  - riemann hypothesis lean certified statement
  - alpöge riemann hypothesis criticism
  - riemann hypothesis proof scientific american nature quanta
as_of: "26 Nov 2026"
---

# Press, official statements and reactions

*As of 26 Nov 2026. Dates are as printed on each page. For current verification, see [status](/status/). For the predicate criticism and the gaps in Masullo’s manuscript, see [controversies](#controversies).*

> **For journalists**
>
> **What the map offers.** An independent, interactive map of the submitted Lean archive: 175,187 Lean files (175,027 on the map) in 2,647 clusters and 63 themes, about 17.4 million lines. It shows how the proof is structured: the main theorem's cluster, and how far each cluster is from it. [How the proof is structured](/route/) · [main theorem's cluster](/cluster/k0677-explicit-formula-perron-kernel-and-zero-free-conditions-for/) · [browse the list](/list/) · [learning path](/learn/).
>
> **Numbers you can quote.** The longest import chain is 203 files. The median file is 13 imports from `Main`, and the farthest is 43. By import distance from the main-theorem cluster, the clusters fall into bands 0 to 8, with 1, 3, 22, 437, 1,443, 637, 76, 25 and 3 clusters. The 175,187 figure is for the submitted archive. The community repository has since removed most of those files: at its main commit [6866a9c6](https://github.com/leanprover-community/riemann-hypothesis/commit/6866a9c6260d77b88a7b5477433e3044b6844f9b) (24 Nov 2026, 13:39 UTC) it has 60,156 `.lean` files, 60,147 of them under `src/`. The count changes with every merge.
>
> **Free to use.** Everything we made, including data, page text, images and clips, is free to use under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit "RH Lean Explorer (riemannhypothesissolved.com)".
>
> **Contact.** X: [@RiemannMap](https://x.com/RiemannMap)
>
> **Wording we suggest.** "Certified" refers to the four formal criteria in the joint statement. The certification is a "joint statement by the Lean FRO and the Mathlib Initiative". Cluster names on the map were drafted by AI. For claims about the proof, cite the primary sources.

## Official statements and primary documents

- **20 Nov 2026. Levent Alpöge, [note (4-page PDF)](https://alpo.ge/remark.pdf).** The announcement note, linking the 14 archive parts. His [home page](https://alpo.ge/) lists Anthropic and a Harvard junior fellowship.
- **20 Nov 2026. Lean community, [first commit in the mirror](https://github.com/leanprover-community/riemann-hypothesis/commit/40e56bab026552e089d7afcfeff08d2defb9c005).** An unmodified copy of the submission. The [repository](https://github.com/leanprover-community/riemann-hypothesis) was later trimmed. Its [verification notes](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md) give sizes, a static scan and caveats.
- **21 Nov 2026, 13:55 UTC. Lean FRO and Mathlib Initiative, [Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/).** A joint statement by the Lean FRO and the Mathlib Initiative. It certifies the statement and proof and lists four checks.
- **Read 22 Nov 2026. [Mathlib Initiative](https://mathlib-initiative.org/).** A home-page banner saying it "fully endorses" the communities' verification.
- **Read 22 Nov 2026. [Lean home page](https://lean-lang.org/).** A November 2026 timeline entry: "Levent Alpöge releases a Lean-verified proof of the Riemann Hypothesis".
- **20 Nov 2026. Association for Human Mathematics, [statement](https://www.ahmath.org/statements).** A critical statement on the way the announcement was made. Written before the joint statement.
- **Clay Mathematics Institute, [rules for the Millennium Prizes](https://www.claymath.org/millennium-problems/rules/).** Publication in a qualifying outlet, two years, general acceptance.

### People who ran checks

- **Updated 25 Nov 2026, 22:05 UTC. Andrew Sutherland (MIT), [verification files](https://math.mit.edu/~drew/grh/).** Logs of the original archive’s build, axiom audit, independent kernels and proof exports, including the completed Lean v4.36.0 Comparator run.
- **Michael Rubinstein (Waterloo).** His [four Lean checks](https://mrubinst.github.io/grh-lean-verification/) finished on 21 Nov. His [265-page working draft for the zeta case](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) is dated 22 Nov (version 2).
- **Elliot Arledge, [verification receipts](https://github.com/Infatoshi/rh-verification-receipts).** An independent rebuild, an axiom audit and nanoda check receipts.
- **Bartosz Naskręcki, [riemann-rev](https://nasqret.github.io/riemann-rev/).** A community site with a map, an 11-page guide and a record of who checked what. It says it is "not an official companion".

## Controversies {#controversies}

### Jenny Lorraine Nielsen’s criticism of Alpöge’s proof {#nielsen-criticism}

The original Lean archive defines an internal condition, `anyGeometry`, to be true for every input. In a preprint and a 23 November post, Jenny Lorraine Nielsen argues that the geometric construction and its assigned height reuse analytic data in a circular way. Carlos Toledo’s audit confirms the always-true definition and leaves the geometric interpretation of that step open. [Nielsen’s preprint](https://philarchive.org/rec/NIEIOT-2) · [Original post](https://x.com/QualiaQuanta/status/2124992635605807308) · [Pinned Lean definition](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L19) · [Toledo’s audit](https://carlostoledo.co/reports/alpoge-grh.html)

Chris Bailey explained on MathOverflow that the check depends on the proof term having the required type. An internal definition that is always true still leaves the proof obliged to establish Mathlib’s Riemann hypothesis. The certification records how two tools matched that statement and how independent checkers accepted the exported proof. Alpöge clarified on 24 November that he understood the proof to have checked out. [Bailey’s response](https://mathoverflow.net/questions/518109/after-the-lean-verification-of-the-riemann-hypothesis-proof-what-residual-trust#comment1354173_518119) · [Joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) · [Alpöge’s clarification](https://x.com/__alpoge__/status/2125062170207457583) · [Detailed FAQ](/faq/#tautology)

### Open gaps in Alessandro Masullo’s separate manuscript {#masullo-gaps}

Masullo’s *The Music of the Primes* proposes a proof of GRH for Hecke L-functions. In its Lean formalization of this manuscript, Ryan McCorvie’s project records a counterexample to the uniform bound as printed in §1.4.3 and an unproved cancellation of zeros outside a strip in Theorem 12.5.1.1. The project shows that this cancellation for every strip width is equivalent to the manuscript’s main claim. These findings concern Masullo’s argument. Follow the [verification record](/status/) for Alpöge’s Lean release. [Manuscript v1](https://clopen.solutions/submissions/the-music-of-the-primes/v1/) · [Formalization README](https://github.com/mccorvie/riemann-masullo/blob/9c791d74a81f1191d900e6d96f1270acee9b033e/README.md) · [Open issue #5571](https://github.com/mccorvie/riemann-masullo/issues/5571)

## News coverage, November 2026

- **20 Nov, updated 21 Nov. Scientific American (Joseph Howlett), [Anthropic mathematician proves Riemann hypothesis, most famous problem in all of math](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/).** Breaking report with comments from Pasten, Pagano and Sutherland. The web address says "claims to prove".
- **20 Nov, updated 21 Nov. Nature (Davide Castelvecchi), [Mathematicians astounded by AI and human-written proofs of iconic Riemann hypothesis](https://www.nature.com/articles/d41586-026-03812-7).** Covers the Alpöge and Masullo claims, with Maynard, Granville and Buckmaster. Partly paywalled.
- **20 Nov. Quanta Magazine (Konstantin Kakaes), [A claimed proof of the Riemann hypothesis](https://www.quantamagazine.org/updates/transformation/#169564).** Quanta's first report, on its "Transformation" page.
- **20 Nov. Quanta Magazine (Konstantin Kakaes), [As mathematicians race to verify AI Riemann proof, a human proof emerges](https://www.quantamagazine.org/updates/transformation/#169569).** The verification race, the first public signal on X, the Masullo draft and Radziwiłł's criticism.
- **20 Nov. IBM Think (Sascha Brodsky), [Anthropic mathematician claims AI helped solve a 167-year-old math mystery](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof).** Interviews with Maynard and Lamzouri.
- **20 Nov, updated 21 Nov. Scientific American (Clara Moskowitz), [The AI Riemann hypothesis proof is true, independent mathematicians confirm](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/).** Reports independent compiles and the joint statement, with Buzzard and Sutherland.
- **About 20–21 Nov. The Next Web (Ana Maria Constantin), [Anthropic mathematician says he and Claude proved the Riemann hypothesis](https://thenextweb.com/news/anthropic-alpoge-claude-riemann-hypothesis-proof-lean).** A summary that relays New York Times quotes from Conrad and Maynard.
- **20–21 Nov. OfficeChai, [How mathematicians have reacted to claimed Riemann hypothesis proof](https://officechai.com/ai/how-mathematicians-have-reacted-to-claimed-riemann-hypothesis-proof-by-anthropics-levent-alpoge/).** A roundup embedding posts from X.
- **22 Nov. Startup Fortune (Dave Barr), [Lean groups certify Claude-assisted Riemann hypothesis proof from Anthropic](https://startupfortune.com/lean-groups-certify-claude-assisted-riemann-hypothesis-proof-from-anthropic/).** Summarises the certification and notes Clay's rules. It relies on other outlets.
- **24 Nov, 5:15 AM (no time zone stated). WIRED (Isabella Ward), [AI Solved Math’s Most Famous Problem. Now Humans Are Struggling to Understand It](https://www.wired.com/story/ai-solved-maths-most-famous-problem/).** Quotes Abhishek Saha (Queen Mary University of London): "Knowing there is a proof is one thing, … but when we understand the proof, that would allow us to actually go beyond what has happened". Anton Shakov (Principia Math) expects it "will take mathematicians months" to understand. WIRED describes the 250,000 pages as a paper version that "clocks in at 250,000 pages" and adds that Alpöge later called the figure a "joke".
- **24 Nov. The Wall Street Journal, [article on Alpöge and Claude](https://www.wsj.com/tech/ai/anthropic-mathematician-says-claude-has-solved-the-most-famous-problem-in-math-9361920b) (headline not seen).** Paywalled; we have not read it. WSJ's post on X (24 Nov, 04:17 UTC) says "One day after the company’s IPO, an Anthropic employee says Claude helped discover a proof." ([X](https://x.com/WSJ/status/2125081353641222615))
- **24 Nov, 11:30 as printed (time zone not stated). Nikkei, [数学難問リーマン予想、アンソロピック証明は「正しいと確信」 専門家](https://www.nikkei.com/article/DGXZQOSG222470S6A121C2000000/)** (roughly: "Hard math problem, the Riemann hypothesis: Anthropic proof 'convinced it is correct', expert"). Paywalled; we read the headline and opening only. The visible text refers to "an outside expert" and the joint statement, and names no one.

## Blogs and commentary

- **20 Nov. Terence Tao, [Unforced Euler singularity, unforced Navier-Stokes singularity, and the Generalized Riemann Hypothesis](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/).** A short post listing three AI-assisted results. The Riemann one points to the Lean Zulip thread. On 21 Nov his [link roundup](https://terrytao.wordpress.com/2026/11/21/even-more-posts-opinion-pieces-interviews-and-position-statements/) lists the AHM statement first.
- **20 Nov. Scott Aaronson, [The stochastic parrots have apparently proved the Riemann Hypothesis](https://scottaaronson.blog/?p=10344).** A personal reaction that bets the proof will stand and discusses Lean's remaining soundness issues.
- **20 Nov. Ravi Vakil, [Hurried Announcement: Alessandro Masullo GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/).** Posts a separate, human-written GRH draft by Alessandro Masullo and, about eight hours later, an update on reported problems.
- **12 Nov. Kevin Buzzard's Xena Project, [and the proof is checked in Lean](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/).** Written before the release. It sets out the four questions the joint statement later cites.

## Reactions from mathematicians and others

Quotes are exact and link to where we read them. Summaries are marked "paraphrase".

### Supportive or enthusiastic

- **Andrew Sutherland (MIT), Scientific American, 20–21 Nov.** "This is indeed an historic moment," ... "The world has changed.... I know there will be a wide range of reactions in our community, but to me this is a human triumph, and a day for celebration." He also said: "Honestly the chance that anything is fishy here is approximately zero." ([article 1](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/), [article 2](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/))
- **Filippo Nuccio (Jean Monnet University), 20 Nov, a Lean Zulip post quoted by Quanta.** "WOW, this is gorgeous: it basically contains all number theory produced in the last 50 years, in all branches of the discipline." ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **Youness Lamzouri (University of Lorraine), IBM Think, 20 Nov.** "I don’t have words to describe what I am feeling right now. I am just in awe," ... and, on understanding: "Mathematics is mainly about understanding why something is true". ([IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof))

### Cautiously positive

- **James Maynard (Oxford), Nature, 20 Nov.** "If this fully checks out, it is clearly a historic milestone in mathematics," and "I suspect that the proof will turn out to be correct," ([Nature](https://www.nature.com/articles/d41586-026-03812-7)). In IBM Think he added: "So somewhat frustratingly, it looks like it will require quite a lot of work to really gain this understanding," ([IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof)).
- **Scott Aaronson, blog, 20 Nov.** "So I’m not 100% sure, but my bet is that the proof will stand." ([blog](https://scottaaronson.blog/?p=10344))
- **Simon DeDeo (Carnegie Mellon), Quanta, 20 Nov, from an email.** "I’d be very surprised if there were any secret tricks," ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **Tristan Buckmaster (NYU), Nature, 20 Nov.** "At the moment, it apparently is crazily complicated. It’s going to take a long time for mathematicians to digest," ([Nature](https://www.nature.com/articles/d41586-026-03812-7)). He is Alpöge's co-author on other results and was in a public priority dispute with OpenAI in September.

### Neutral or procedural

- **Terence Tao, blog, 20 Nov.** "I imagine the digestion process will take some time, though in this case at least we have a human author to communicate with to assist with this task." ([blog](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/))
- **Kevin Buzzard, 12 Nov blog, before this claim (paraphrase).** The first question to ask of a Lean proof that comes with a PDF is whether the theorem stated in the code matches the real theorem. ([Xena](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/))

### Cautious

- **Pierre Richemond, X, 20 Nov (Cohere, per OfficeChai).** "The Riemann Hypothesis may be solved (pending Lean review) – not totally unexpected, yet raising more questions than it answers. We’re now in a bizarre epistemic zone that barely existed before 2026: unmistakably serious mathematics, yet completely unverified in human terms." ([X](https://x.com/TheOneKloud/status/2123804288921027070))
- **Thomas Bloom, X, 20 Nov (University of Manchester, per OfficeChai).** He was surprised at the claim of a coherent proof "that, written out in human-readable format, is 250,000+ pages long." ([X](https://x.com/thomasfbloom/status/2123796489197514945)) Alpöge's note says, in a footnote about a write-up he did not post: "I of course amused myself, and hit 250, 000+ pages." ([note](https://alpo.ge/remark.pdf)) On 23 Nov, 22:03 UTC, he wrote on X: "250,000+ pages was a joke guys!" ([post](https://x.com/__alpoge__/status/2124987173439209561))

- **Kevin Buzzard (Imperial College London), Al Jazeera, 21 Nov.** "At the minute, we don’t even know why the theorem is true," He also said: "Experience shows you that you give the humans the Lean code, and within a week or two, they have a much better understanding of what’s actually going on in this code," ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked))

### Critical

- **Andrew Granville (Université de Montréal), Nature, 20 Nov.** "What he released is garbled," ([Nature](https://www.nature.com/articles/d41586-026-03812-7)). Paraphrase: Nature reports that he says Alpöge should have prepared a clearer write-up first, and cites the downturn in the company's stock value as the reason for the timing. Alpöge's note calls the timing explanation "an obvious cynical view" and says it "is false". ([note](https://alpo.ge/remark.pdf))
- **Maksym Radziwiłł (NYU), Quanta, 20 Nov, from an email.** "The object of mathematics as the rest of science is really the question ‘why?’ and this doesn’t answer it at all." Quanta also reports, in its own words, that he says the four-page note contains "nonsensical statements". Alpöge's note thanks him by name. ([Quanta](https://www.quantamagazine.org/updates/transformation/))
- **Association for Human Mathematics, 20 Nov.** "At this time, no human being can reasonably claim to be responsible for, or even to understand, such a document. Neither can any mathematician confirm with full certainty that the proof is correct." Written before the joint statement. ([AHM](https://www.ahmath.org/statements))
- **Brian Conrad (Stanford), 20 Nov. Second-hand: The Next Web, quoting The New York Times.** The Next Web writes that he criticised the release and called it "frankly completely outrageous" to put out a proof that Alpöge does not fully understand. ([The Next Web](https://thenextweb.com/news/anthropic-alpoge-claude-riemann-hypothesis-proof-lean))

### The author

- **Levent Alpöge, note, 20 Nov.** "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis." On timing: "The precise timing is horrible." On limits: "I may have baked lots of strange suboptimal choices into the argument". ([note](https://alpo.ge/remark.pdf))
- **Levent Alpöge, X, 23 Nov, 22:03 UTC.** In a list headed "Stupid things I did": "I feel Riemann should be easy, and any real difficulty is an indication our setup is just dumb at the moment." ([post](https://x.com/__alpoge__/status/2124987173439209561))

### Common threads

Across the cautious and critical voices, a common thread is that a formal check can settle whether the statement is true but not why it is. Supporters and critics differ on how much that matters.

## Earlier background

- **10 Aug 2026.** Anthropic, [zeros result (41.6% to 67.2%)](https://www.anthropic.com/research/riemann-zeta). **12 Aug.** Scientific American, [No, Anthropic's AI didn't just solve math's hardest problem](https://www.scientificamerican.com/article/no-ai-didnt-just-solve-the-thorniest-problem-in-math/).
- **8 Sep 2026.** Scientific American, [OpenAI claims blockbuster math breakthrough amid swirl of controversy](https://www.scientificamerican.com/article/openai-claims-blockbuster-math-breakthrough-amid-swirl-of-controversy/), on OpenAI's Navier–Stokes claim. **22 Oct.** [The inside story behind OpenAI's million-dollar math proof](https://www.scientificamerican.com/article/the-inside-story-behind-openais-million-dollar-math-proof/).
- **19 Oct 2026.** Quanta, [AI Proved the Quasi-Riemann Hypothesis. What Happens Now?](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/) On OpenAI's October result.

## About this site

riemannhypothesissolved.com is free, and independent of Levent Alpöge, Anthropic, the Lean FRO, the Lean and Mathlib communities, and the Mathlib Initiative.
