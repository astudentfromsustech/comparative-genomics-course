You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: How comparative genomics is actually taught — existing courses and curricula
QUESTION TO ANSWER: What do real university courses, workshops and MOOCs on comparative /
evolutionary genomics actually teach, in what order, and what do they cover that a
self-designed syllabus is likely to miss?

CONTEXT: I am building a 14-chapter self-study course on comparative genomics as a research
field, aimed at a computational biologist who wants to do research in it AND referee papers.
My current chapter list is:

  0  How the field got here (history: one molecule -> genomes -> clade scale -> pangenome -> evidence)
  1  What the field asks (homology + time frame; the six nested framework layers)
  2  The objects you compare (assembly QC, annotation comparability, repeats, contamination)
  3  Orthology (ortholog/paralog vocabulary, RBH failure, benchmarks)
  4  Synteny, whole-genome alignment, ancestral genome reconstruction
  5  Gene families, duplication, WGD (CAFE, Ks, dosage balance)
  6  Species tree as coordinate system (MSC, ILS, concatenation vs coalescent, dating)
  7  Phylogenetic comparative methods (PIC/PGLS/OU, RERconverge, N species != N data points)
  8  Structural variation, T2T, pangenome graphs
  9  Selection inference (dN/dS, codon models, branch-site, false positives)
  10 Population history and introgression (demography, D-statistics, ILS vs introgression)
  11 Convergence and adaptive explanation
  12 Regulatory and non-coding comparison
  13 Frontier (ML, constraint at scale) + evidence ladder / referee checklist

DEPTH: research-level. I need to know what I got wrong or left out, not encouragement.

FIND AND REPORT:
1. SPECIFIC named courses with syllabi you can actually see. Prioritise ones where the module
   list or lecture schedule is public. Look for: MIT (e.g. 7.91/6.874 computational biology),
   Harvard, Stanford, UC Davis, Cornell, EMBL-EBI training, Cold Spring Harbor Laboratory
   courses, Physalia-courses, Evomics / Workshop on Genomics (Cesky Krumlov), Wellcome Connecting
   Science, Coursera/edX offerings, and any well-known comparative-genomics-specific course.
   For each: institution, course title/code, level, and its actual module/lecture list.
2. The COMMON SPINE: what topics appear in nearly every such course? What is the usual teaching
   ORDER, and does it differ from the dependency order I used?
3. What do these courses teach that is ABSENT from my 14 chapters? Be specific and concrete.
   I especially want to know about: sequence alignment algorithms and substitution models taught
   as fundamentals; molecular evolution theory (neutral theory, nearly-neutral, coalescent
   basics); genome architecture/evolution topics; functional annotation and enrichment done
   properly; data resources and browsers (Ensembl Compara, UCSC, NCBI, OrthoDB); microbial vs
   eukaryote split; metagenomics; ancient DNA; and anything on scientific writing/reproducibility.
4. What do they include that a RESEARCH-LEVEL reader would consider background or out of scope?
5. HANDS-ON structure: what practical exercises, datasets and tools are standard? Do courses
   teach a canonical worked pipeline end-to-end, and on what data?
6. Standard TEXTBOOKS and lecture-note sets for this field, with current editions.
7. Where courses DISAGREE on framing — e.g. is comparative genomics taught as a branch of
   molecular evolution, of bioinformatics methods, or of genomics-as-technology? Does the framing
   change the syllabus?
8. Primary sources: course pages, syllabi PDFs, GitHub repos of course materials, textbook pages.
9. The current state as of 2026-08-17 -- flag anything that changed in the last 18 months.
10. Disagreements: where do credible sources conflict? Say so rather than picking one silently.

OUTPUT FORMAT (markdown, no preamble):
## Answer
<direct answer to the question above, 250-450 words>
## Key findings
<bulleted; EVERY factual claim carries an inline source URL>
## Course inventory
<table: institution | course | level | module list in brief | URL>
## What my 14 chapters are MISSING
<ranked list, most important first, each with why it matters and which chapter it belongs in>
## What my chapters have that courses typically DON'T
<so I know what is genuinely my own framing vs an omission>
## Caveats and open questions
<what you could not verify, and what is contested>

RULES:
- Every non-obvious claim needs a URL you actually visited. No URL = mark it "[unverified]".
- Prefer actual syllabus/course pages over aggregator listings or marketing copy.
- If a course's syllabus is not public, SAY so rather than guessing its contents.
- Do not pad the "missing" list to look thorough — rank by what would actually change the course.
