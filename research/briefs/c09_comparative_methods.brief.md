You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Phylogenetic comparative methods for cross-species claims
QUESTION TO ANSWER: Why are N species not N independent data points, what corrects for that, and how is this machinery misused in comparative-genomics papers?
CONTEXT: this is chapter C7 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C6 (species trees and discordance). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. Phylogenetically independent contrasts, PGLS, and phylogenetic mixed models: what each corrects for and what each assumes.
2. Model choice for trait evolution -- Brownian motion vs Ornstein-Uhlenbeck vs Early Burst; how often OU is fitted inappropriately and what the known statistical pitfalls are (e.g. OU model support with small trees).
3. Methods that link genomic features to phenotypes across species: RERconverge, PhyloAcc, forward-genomics, PhyloG2P approaches. What are their assumptions and documented false-positive rates?
4. Concrete critiques from the literature of comparative-genomics papers that correlated a genomic feature with a trait across species WITHOUT phylogenetic correction -- what went wrong.
5. How many independent origins of a trait are needed for a defensible claim, and how the effective sample size of a comparative dataset should be reported.
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
