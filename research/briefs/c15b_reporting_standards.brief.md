You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Evidence standards, reproducibility, and reviewing practice
QUESTION TO ANSWER: What is the minimum reportable record for each claim type in comparative genomics, and what should a referee demand?
CONTEXT: this is chapter C13 of a systematic study plan on comparative genomics as a research
field. The reader has already covered the whole plan. They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
1. Published checklists, reporting standards, and best-practice guidelines specific to comparative and evolutionary genomics (journal policies, MIxS-style standards, community guidelines).
2. Documented reproducibility failures in comparative genomics -- reanalyses that overturned a published conclusion. What was the recurring cause?
3. How clade-specific practice diverges: what is standard in microbial (ANI/GTDB/pangenome), plant (polyploidy, TE load, WGD), and animal comparative genomics, and what does not transfer.
4. Workflow reproducibility in practice: Nextflow/nf-core, Snakemake, containers, and whether comparative-genomics papers actually ship runnable pipelines. Any surveys measuring this?
5. For each of these claim types -- gene family expansion, gene loss, positive selection, introgression, convergent adaptation, structural variant fixation -- what is the minimum evidence a 2026 referee should require, and what weaker wording is appropriate when it is absent?
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
