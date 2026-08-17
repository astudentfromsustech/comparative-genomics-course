You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Whole-genome alignment, synteny, and ancestral genome reconstruction
QUESTION TO ANSWER: How do you align whole genomes across a clade, why does collinearity rather than similarity adjudicate a claimed gene loss, and what is the current state of ancestral genome reconstruction?
CONTEXT: this is chapter C4 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C3 (orthology). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. Current whole-genome aligners for clade-scale work: Progressive Cactus, minigraph-cactus, AnchorWave, GSAlign, SibeliaZ, and 2024-2026 entrants. Which is appropriate at which divergence?
2. Why pairwise-to-reference alignment introduces bias and what reference-free multiple WGA buys you; the HAL format and what tooling consumes it.
3. ANCESTRAL GENOME RECONSTRUCTION -- this is a deliberate gap in our corpus, so treat it as the priority: what are the canonical methods and papers (Cactus ancestral sequences, DESCHRAMBLER, AGORA, ANGES, infer-ancestral-gene-order approaches)? How reliable are reconstructed ancestors, and what are they legitimately used for?
4. Synteny/collinearity detection: MCScanX, JCVI/MCscan, GENESPACE, SynGAP and successors -- and how syntenic evidence is used to confirm or refute a gene-loss claim.
5. How rearrangement inference (inversions, translocations, fusions) is done and validated at clade scale, and the error modes introduced by assembly scaffolding.
6. Primary sources: papers (title, year, authors, DOI), official docs, canonical repos.
7. The current state as of 2026-08-17 -- flag explicitly anything that changed in the last 18 months.
8. Disagreements: where do credible sources conflict? Say so rather than picking one silently.

OUTPUT FORMAT (markdown, no preamble):
## Answer
<direct answer to the question above, 250-450 words>
## Key findings
<bulleted; EVERY factual claim carries an inline source URL>
## Primary sources
<table: title | year | venue | URL | why it matters>
## What the standard corpus misses
<papers/tools a reader working from a 2015-2023 reading list would not know about>
## Caveats and open questions
<what you could not verify, and what is genuinely contested in the field>

RULES:
- Every non-obvious claim needs a URL you actually visited. No URL = mark it "[unverified]".
- Prefer primary sources (papers, official docs, source code, benchmark repos) over blog summaries.
- If the evidence is thin, SAY it is thin. Do not pad with plausible-sounding filler.
- Where credible sources disagree, report the disagreement rather than silently picking one.
- Name specific tools with versions and specific papers with DOIs wherever possible.
