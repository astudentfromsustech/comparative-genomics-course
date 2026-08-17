You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Assembly & annotation comparability
QUESTION TO ANSWER: What must be true of assemblies and annotations before a cross-species comparison is meaningful, and what does each defect manufacture downstream?
CONTEXT: this is chapter C2 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C1 (what the field asks; homology vs similarity). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. Current standards for assembly quality assessment beyond N50 -- BUSCO vs Merqury vs LAI vs compleasm; what each actually measures and where each is blind.
2. How structural annotation pipelines (BRAKER3, Helixer, TSEBRA, EGAPx, AUGUSTUS-based) differ, and how much cross-species gene-count variation is annotation artefact rather than biology.
3. Documented cases where an assembly or annotation defect produced a false biological conclusion (false gene family expansion, false gene loss, false HGT, false SV) -- give concrete examples.
4. What changed with T2T/VGP-era assemblies and the 2023-2026 annotation tools; is 'annotate all genomes with one pipeline' now standard practice for comparative studies?
5. Contamination screening (FCS-GX, Kraken-based) -- how much of the older comparative literature is affected by contamination that current screening would catch?
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
