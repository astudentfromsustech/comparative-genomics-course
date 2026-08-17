You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Selection inference: what dN/dS licenses
QUESTION TO ANSWER: What does a dN/dS or branch-site result actually entitle you to say, and what generates false positives?
CONTEXT: this is chapter C9 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C3 (orthology), C6 (species trees). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. The model family: NG86 through GY94, site models (M1a/M2a, M7/M8), branch, branch-site, and the HyPhy family (aBSREL, BUSTED, MEME, RELAX). What hypothesis each actually tests.
2. The four classic false-positive generators -- paralog contamination, misaligned codons, recombination, uncorrected multiple testing. Quantified evidence for each from the literature.
3. Confounders that raise dN/dS WITHOUT positive selection: relaxed constraint, small effective population size, GC-biased gene conversion, nonstationary base composition. How are they controlled for in good practice?
4. The critique literature on branch-site tests specifically -- known false-positive rates under alignment error and model misspecification; what the recommended pre-flight checks are.
5. Alternatives and complements: MK-test variants and asymptotic MK, DFE-based inference, polymorphism-aware approaches, and machine-learning selection scans. Where is the field moving?
6. Current best-practice checklists for reporting a positive-selection result -- what a referee should demand to see.
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
