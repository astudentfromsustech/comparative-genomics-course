You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Sequence comparison and the statistical models underneath it
QUESTION TO ANSWER: What does a computational biologist need to understand about alignment,
scoring, search significance and likelihood-on-trees before any comparative-genomics result is
interpretable — and which of those assumptions actually break real published conclusions?

CONTEXT: This is chapter 02 of a 16-chapter self-study course on comparative genomics as a
research field. It was added after a survey of real curricula (MIT 6.047, Stanford CS262,
Bologna 91407, Evomics) found that my course jumped straight to orthology and selection while
assuming the reader could already judge an alignment, a substitution model and a likelihood
calculation. This chapter is that missing floor.

The reader is a computational biologist: fluent in programming, statistics and bioinformatics
TOOLING, but has never been taught these methods formally — they have run MAFFT and IQ-TREE
without being able to say what either assumes. They will use this to DO research and to REFEREE
papers, so the failure modes and the "what does this license you to claim" angle matter more
than implementation detail. Chapters that depend on this one: orthology (05), whole-genome
alignment (06), species trees (08), selection/dN-dS (11), conservation scoring (14).

DEPTH: research-level, but it is a foundations chapter — prioritise the concepts whose
VIOLATION shows up later over algorithmic completeness.

FIND AND REPORT:
1. Pairwise alignment: global vs local (Needleman-Wunsch, Smith-Waterman), affine gap penalties,
   and — the part that matters downstream — what the choice of gap penalty and scoring matrix
   actually does to the resulting alignment. Where do PAM/BLOSUM matrices come from, and what
   divergence is each appropriate for?
2. Search significance: how BLAST/DIAMOND E-values are computed (Karlin-Altschul), what an E-value
   does and does not mean, low-complexity and compositional bias, and why "top hit" is not
   "homolog". Include the current state of sensitive search (DIAMOND ultra-sensitive, MMseqs2,
   HMMER/profile methods, and structure/PLM search) and where each is appropriate.
3. Multiple sequence alignment as a source of ERROR, not just a preprocessing step: how much do
   MAFFT / MUSCLE / PRANK / Clustal disagree; what is the documented effect of alignment error
   and of alignment filtering (Gblocks, trimAl, ZORRO, HmmClean) on downstream phylogenetic and
   dN/dS inference? There is a real literature arguing filtering can HURT — report both sides.
   Codon-aware alignment (MACSE, PAL2NAL) and why it matters for chapter 11.
4. Substitution models and likelihood: what a Markov substitution model assumes (JC69 -> GTR,
   +G, +I, codon and amino-acid models), how likelihood on a tree is computed conceptually
   (Felsenstein pruning), what model selection (ModelFinder/jModelTest) does, and the current
   evidence on whether model choice materially changes topology or only branch lengths.
   Also: model ADEQUACY versus model SELECTION — the distinction most users never make.
5. Profile methods: PSSMs, profile HMMs, Pfam/InterPro, and how profile-based homology detection
   differs in reach and in failure mode from pairwise search.
6. CRITIQUE MY CHAPTER PLAN. I intend to cover, in this order: (a) alignment as a hypothesis, not
   a fact; (b) scoring matrices and gap penalties; (c) BLAST statistics and what a top hit means;
   (d) MSA error and the filtering controversy; (e) substitution models and likelihood; (f) profile
   HMMs; (g) how each of these propagates into later chapters. What is MISSING or MISORDERED,
   ranked by what would actually change the chapter? What am I including that a research-level
   reader does not need?
7. Primary sources: papers (title, year, authors, DOI), textbook chapters, official docs.
8. The current state as of 2026-08-17 -- flag explicitly anything that changed in the last 18 months.
9. Disagreements: where do credible sources conflict? Say so rather than picking one silently.

OUTPUT FORMAT (markdown, no preamble):
## Answer
<direct answer to the question above, 250-450 words>
## Key findings
<bulleted; EVERY factual claim carries an inline source URL>
## Primary sources
<table: title | year | venue | URL | why it matters>
## What my chapter plan is MISSING
<ranked, most important first>
## Caveats and open questions
<what you could not verify, and what is genuinely contested>

RULES:
- Every non-obvious claim needs a URL you actually visited. No URL = mark it "[unverified]".
- Prefer primary sources and official docs over blog summaries or tutorials.
- If the evidence is thin, SAY it is thin. Do not pad with plausible-sounding filler.
- Where credible sources disagree — especially on alignment filtering — report the disagreement
  rather than silently picking one.
- Do not pad the ranked list to look thorough. Rank by what would change the chapter.
