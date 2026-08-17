You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: The 2024-2026 frontier: ML, sequence constraint, and pangenome-native comparison
QUESTION TO ANSWER: Where is comparative genomics actually moving right now, and what do machine-learning approaches replace versus merely accelerate?
CONTEXT: this is chapter C13 of a systematic study plan on comparative genomics as a research
field. The reader has already covered the whole plan -- treat the reader as knowing the classical stack. They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. Alignment-derived constraint at scale: Zoonomia/240-mammal results, phyloP/phastCons at that scale, and what constraint scores are now used for. What are the documented limits?
2. Genomic language models (Evo/Evo2, Nucleotide Transformer, DNABERT-2, AlphaGenome, Borzoi, Enformer lineage): what tasks they demonstrably do well, what they demonstrably do NOT do, and whether any are displacing alignment-based comparative inference. Be skeptical and cite benchmark evidence.
3. Protein structure comparison as a comparative-genomics tool -- AlphaFold DB, Foldseek, and structure-informed orthology/remote homology. What has this actually changed?
4. Pangenome-native comparative genomics: doing selection, gene-family, and association analysis on a graph rather than a linear reference. What tooling exists and what is still missing?
5. Large consortium efforts active now (Earth BioGenome, VGP, Zoonomia, Bird10K, Darwin Tree of Life, HPRC) -- current status and what data they have released that comparative studies can use.
6. What do people working in the field currently name as the major UNSOLVED problems? Cite perspective/opinion pieces from 2024-2026.
7. Primary sources: papers (title, year, authors, DOI), official docs, canonical repos.
8. The current state as of 2026-08-17 -- flag explicitly anything that changed in the last 18 months.
9. Disagreements: where do credible sources conflict? Say so rather than picking one silently.

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
