You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: Molecular evolution and population genetics — the generative theory under comparative genomics
QUESTION TO ANSWER: What theory of how genomes actually change over time must a comparative
genomicist hold in their head, so that later results (a dN/dS value, an Fst outlier, a gene tree
that disagrees with the species tree, a fixed structural variant) are interpreted against the
right null rather than treated as findings on their own?

CONTEXT: This is chapter 03 of a 16-chapter self-study course on comparative genomics as a
research field. It was added after a survey of real curricula found my course taught the
DOWNSTREAM results — species trees, selection scans, introgression statistics — without the
shared generative theory that all of them are estimating from. The critique was specific:
"neutral and nearly-neutral theory, mutation/recombination/drift/linked selection, coalescent
basics, allele-frequency spectra, LD and genotype likelihoods should precede species trees,
selection and introgression."

The reader is a computational biologist: strong in statistics and probability, comfortable with
stochastic processes, but has NOT had a formal population-genetics course. They will use this to
DO research and to REFEREE papers. The point of the chapter is not to derive results but to make
them able to say, of any comparative claim, "what would this look like under neutrality?"

Chapters that depend on this one: species trees / multispecies coalescent (08), selection
inference (11), population history and introgression (12), convergence (13).

DEPTH: research-level, but foundations — prioritise the ideas whose ABSENCE causes
misinterpretation downstream over mathematical completeness.

FIND AND REPORT:
1. The neutral theory and the nearly-neutral theory: what each actually claims, what evidence
   supports and challenges each now, and — most importantly — why "neutral" is the NULL rather
   than a belief about biology. Include the modern state of the neutralist/selectionist question
   and the role of linked selection.
2. The forces and their scales: mutation (rates, spectra, and how directly-measured rates changed
   older divergence-time and Ne estimates), genetic drift, effective population size Ne and what
   it actually is, recombination, gene conversion including GC-biased gene conversion, and linked
   selection (background selection and selective sweeps). For each: what comparative-genomics
   artefact does it produce if ignored?
3. The coalescent: the intuition (backwards-in-time genealogy), what the standard coalescent
   assumes, the SITE FREQUENCY SPECTRUM as a summary and what demography vs selection do to it,
   and how the multispecies coalescent extends this — since chapter 08 depends on it. What breaks
   the standard coalescent (population structure, selection, recombination)?
4. Linkage disequilibrium, haplotypes and ancestral recombination graphs: what LD measures, how it
   decays, why it matters for both selection scans and demographic inference, and the current
   state of ARG inference (Relate, tsinfer/tskit, ARG-Needle, SINGER) — is the field moving from
   summary statistics to ARGs?
5. Genotype likelihoods and low-coverage data (ANGSD-style): why calling genotypes then analysing
   them is a documented source of bias, and when likelihood-based approaches are required.
6. Divergence vs polymorphism: the conceptual bridge between population genetics (within species)
   and comparative genomics (between species) — why the same locus looks different through the two
   lenses, and where the boundary actually is.
7. CRITIQUE MY CHAPTER PLAN. I intend to cover, in this order: (a) neutrality as a null, not a
   belief; (b) the forces and their timescales; (c) Ne and why it is not a headcount; (d) the
   coalescent and the SFS; (e) LD and haplotypes; (f) divergence vs polymorphism as the bridge to
   the rest of the course. What is MISSING or MISORDERED, ranked by what would actually change
   the chapter? What am I including that a research-level reader does not need?
8. Primary sources: papers (title, year, authors, DOI), textbook chapters (I have access to Yang,
   Molecular Evolution: A Statistical Approach), official docs.
9. The current state as of 2026-08-17 -- flag explicitly anything that changed in the last 18 months.
10. Disagreements: where do credible sources conflict? Say so rather than picking one silently.

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
- Prefer primary sources and authoritative reviews over textbook summaries on the open web.
- If the evidence is thin, SAY it is thin. Do not pad with plausible-sounding filler.
- The neutralist/selectionist question is genuinely contested — report the disagreement and who
  holds which position, rather than presenting a settled consensus.
- Do not pad the ranked list to look thorough. Rank by what would change the chapter.
