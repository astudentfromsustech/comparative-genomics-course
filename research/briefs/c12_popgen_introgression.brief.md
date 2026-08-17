You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Population history, demography, and introgression
QUESTION TO ANSWER: How do demography and gene flow masquerade as adaptation, and how is introgression distinguished from incomplete lineage sorting?
CONTEXT: this is chapter C10 of a systematic study plan on comparative genomics as a research
field. The reader has already covered C6 (species trees, the multispecies coalescent). They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. Demographic inference methods and their resolution limits: PSMC, MSMC2, SMC++, dadi, fastsimcoal2, Relate, tsinfer/tskit. What time ranges each can and cannot resolve.
2. Introgression statistics: Patterson's D (ABBA-BABA), f4/f-branch, fd, D-statistics in windows, QuIBL, HyDe, Dsuite. What each assumes and how each fails -- particularly for old introgression and for ghost lineages.
3. The specific statistical signature that separates ILS from introgression, and the conditions under which that signature breaks down.
4. Why demography produces false selection signals: how background selection and population structure generate Fst/dN/dS outliers, and what null models are required.
5. State of ancestral recombination graph (ARG) inference 2023-2026 -- ARG-Needle, SINGER, Relate, tsinfer -- and whether ARGs are displacing summary-statistic approaches.
6. Genomic islands of differentiation: the current consensus on whether they indicate speciation with gene flow or reduced diversity/recurrent selection.
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
