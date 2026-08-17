You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Species tree inference, discordance, and divergence dating
QUESTION TO ANSWER: How does a species tree become the coordinate system for every comparison, and what is the current state of the concatenation-vs-coalescent and molecular-clock-calibration disputes?
CONTEXT: this is chapter C6 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C3 (orthology), C4 (synteny/alignment). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. The multispecies coalescent: why gene tree discordance is expected, what ILS predicts, and why concatenation can be statistically inconsistent (the anomaly zone).
2. Concatenation vs summary coalescent (ASTRAL) vs full-likelihood methods -- where does the field stand in 2024-2026? What do recent large phylogenomic papers actually do, and why?
3. Gene- and site-concordance factors (gCF/sCF) versus bootstrap support: why high bootstrap on a wrong topology is routine, and what should be reported instead.
4. Divergence-time estimation: MCMCtree, BEAST2, RelTime, and the fossil-calibration controversies. How sensitive are published divergence dates to prior and calibration choice? Cite specific documented disagreements.
5. Ortholog/loci selection effects on the tree -- filtering by rate, saturation, missing data; and how much topology is driven by those choices.
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
