You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Orthology inference and its benchmarks
QUESTION TO ANSWER: What makes two genes the same evolutionary entity across species, why does best-BLAST-hit fail, and which orthology methods actually win on independent benchmarks?
CONTEXT: this is chapter C3 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C2 (assemblies, annotation, QC). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. The precise definitions and their boundaries: ortholog, paralog, in-paralog/co-ortholog, ohnolog, xenolog, homoeolog -- and what an 'orthogroup' is and is NOT.
2. Quest for Orthologs (QfO) benchmark results and OrthoBench: which methods lead, on which metrics, and what the benchmarks are criticised for.
3. State of the tools 2023-2026: OrthoFinder2/3, OMA, SonicParanoid2, Broccoli, Proteinortho, eggNOG-mapper, and any newer entrants. What are the real accuracy/scalability trade-offs?
4. How isoform selection, fragmented genes, and unequal annotation quality bias orthogroup inference -- and what the recommended mitigations are.
5. Whether protein-language-model or structure-based (Foldseek-era) approaches are changing remote homology detection and orthology assignment.
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
