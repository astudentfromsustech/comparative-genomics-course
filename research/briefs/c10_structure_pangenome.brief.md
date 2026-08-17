You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Structural variation, T2T genomes, and pangenome graphs
QUESTION TO ANSWER: What changes when the unit of comparison stops being a position on a linear reference and becomes a path through a clade?
CONTEXT: this is chapter C8 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C2 (assembly QC), C4 (whole-genome alignment). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. State of pangenome graph construction 2024-2026: minigraph, Minigraph-Cactus, PGGB, and newer. What each produces, and the documented differences in the variants they represent.
2. The human pangenome reference (HPRC) -- what release we are at now, what the second release changed, and what it demonstrably fixed relative to GRCh38.
3. Evidence on reference bias: quantified effects on variant calling, expression quantification, and comparative conclusions. Cite measurements, not assertions.
4. SV calling and comparison across genomes: long-read callers, graph-based genotyping (vg, Giraffe, PanGenie), and how SV callsets are merged/compared (Jasmine, Truvari). Known reproducibility problems between callers.
5. Presence/absence variation (PAV) in pangenomes: what evidence a PAV call needs before it counts as real absence rather than assembly or annotation failure.
6. How T2T assemblies changed what is comparable -- centromeres, segmental duplications, previously-unassemblable regions -- and what comparative questions they newly permit.
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
