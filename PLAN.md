# Study plan: Comparative genomics — the research field

**Scope:** foundations → research/referee level · **Purpose:** to do research in the field and to review it
**Written:** 2026-08-17 · 16 chapters

> **Deliverable:** `course/` — one self-contained HTML page per chapter, named after its directory.
> Open `course/course.html`.

---

## Prerequisites — stated honestly

An earlier version of this plan claimed Chapter 1 assumed no genomics. **That was wrong.** A survey
of eleven public curricula (MIT 6.047, Stanford CS262/CS273A, Harvard OEB 275R, Bologna 91407,
Physalia, Evomics 2026, EMBL-EBI, Wellcome/Sanger, UCSD BIEB 146, edX) found the plan jumped
straight to orthology and selection while assuming the reader could already judge an alignment, a
substitution model and a likelihood calculation.

| | |
|---|---|
| **Assumed** | Programming, statistics, comfort with bioinformatics tooling — you have run MAFFT and IQ-TREE |
| **Taught here** | What those tools assume, and what their assumptions license you to claim |
| **Not taught** | Unix, workflow managers, wet-lab methods — see Evomics and Bologna 91407 |

Chapters 02 and 03 are the floor that survey found missing.

---

## The frame

> A genomic difference is interpretable only inside a **homology relationship** and an
> **evolutionary time frame**.

The field's methods stack into **six nested layers**. A failure at layer *n* invalidates everything
above it — and does so *silently*, emerging at the top as a plausible, publishable result rather
than an error. The corpus is filed `F0…F6`, so the directory tree is the dependency graph.

| Layer | Question | Characteristic failure | Chapters |
|---|---|---|---|
| **F1** Data standard | Are the objects comparable? | Assembly, annotation, contamination | 4 |
| **F2** Homology | Same evolutionary entity? | Paralogs, isoforms, HGT, repeats | 5 · 6 · 7 |
| **F3** Phylogeny | Which lineage, and when? | ILS, introgression, misspecification | 8 · 9 |
| **F4** Structure | How does architecture reshape units? | Scaffolding, collapsed repeats | 10 |
| **F5** Selection | Departs from neutral? | Alignment error, multiple testing, demography | 11 · 12 |
| **F6** Function | Adaptive hypothesis? | Correlation-as-cause, no validation | 13 · 14 |

The second device is the **evidence ladder** — candidate → association → mechanistic support →
causal — which gives each claim type a minimum reportable evidence level and an explicit fallback
wording. Chapter 15 states it in full; every chapter contributes one rung.

**What the field is not:** the pipeline `BUSCO → OrthoFinder → tree → CAFE → PAML → GO → Circos`.
That template substitutes *analysis coverage* for *evidence grade*.

---

## Chapters

Status: **all 16 written and built** in `course/`. Chapters 11 and 14 are written from verified
research findings because their primary literature is paywalled — flagged in-page.

### Part 0 · Foundations

| # | Chapter | Question it answers | Status |
|---|---|---|---|
| 00 | How the field got here | Which of the field's habits are historical accidents? | written |
| 01 | What the field asks | Where does comparative genomics end and its neighbours begin? | written |
| 02 | Sequence comparison | What must you understand about alignment, search and likelihood first? | written |
| 03 | Molecular evolution | What would this look like under neutrality? | written |

### Part I · Orientation to the data (F1)

| # | Chapter | Question | Status |
|---|---|---|---|
| 04 | The objects you compare | What must be true before a comparison means anything? | written |

### Part II · The homology layer (F2)

| # | Chapter | Question | Status |
|---|---|---|---|
| 05 | Orthology | What makes two genes the same object, and why does best-hit fail? | written |
| 06 | Synteny, WGA, ancestral genomes | What makes a gene-loss claim defensible? | written |
| 07 | Gene families & duplication | When is copy number innovation, and when a haplotig? | written |

### Part III · The tree layer (F3)

| # | Chapter | Question | Status |
|---|---|---|---|
| 08 | The species tree | How does the tree become the coordinate system for every comparison? | written |
| 09 | Phylogenetic comparative methods | Why are *N* species not *N* data points? | written |

### Part IV · The structural layer (F4)

| # | Chapter | Question | Status |
|---|---|---|---|
| 10 | SV, T2T, pangenome graphs | What changes when the unit becomes a path through a clade? | written |

### Part V · Selection and history (F5)

| # | Chapter | Question | Status |
|---|---|---|---|
| 11 | Selection inference | What does dN/dS actually license? | written · **corpus 2/15** |
| 12 | Population history & introgression | How do demography and gene flow masquerade as adaptation? | written |
| 13 | Convergence | What does it take to claim convergent adaptation rather than coincidence? | written |

### Part VI · Function, practice, frontier (F6 + X)

| # | Chapter | Question | Status |
|---|---|---|---|
| 14 | Regulatory & non-coding | Why does comparing proteins miss most phenotypic difference? | written · **corpus 1/8** |
| 15 | Frontier + referee checklist | Where is the field going, and what is the minimum reportable record? | written |

---

## Method

**Research** — the `research` skill: Claude plans and verifies, Codex executes the web search.
15 briefs, 826 sourced URLs (kept locally, not published). Every brief asked the
searcher to critique the plan; that is what found the missing prerequisite layer and the
OrthoFinder v3 gap. One citation was corrected on verification (the 12-*Drosophila* aligner study
is *Genome Research*, not MBE).

**Writing** — the `html_build` skill: one self-contained page per directory, named after it.
`course/restyle.py` pushes `_style.css` into every page so a design change is one edit.

---

## Corpus

Papers: real files in `~/Desktop/projects/papers/comparative_genomics/`, hard-linked into
`resources/papers/`. Catalogue `resources/papers/INDEX.md`; routing `scripts/remap_modules.py`
(one auditable line per paper). Books: `resources/books/INDEX.md`.

```
F0_foundations                8/8    F4_structure/sv_t2t             13
F1_data                      12/23   F4_structure/pangenome_graph    17
F2_homology                  16/27   F5_selection                 14/40
F3_phylogeny                  6/14   F6_function                   4/14
                                     X_practice                    7/16
```

**93 of 172 PDFs on disk.**

## Gaps — known, not hidden

1. **79 PDFs missing**, unevenly. `codon_models` 2/15 and `regulatory_noncoding` 1/8 are core
   chapters. These are paywalled; the open-access ladder and a Europe PMC recovery pass together
   got 93/172 and cannot reach the rest. Chapters 11 and 14 need institutional access.
2. **Two directories are empty on purpose** — `F2_homology/ancestral_reconstruction` and
   `X_practice/ml_constraint`. Chapter 06 lists what belongs in the first.
3. **The corpus inherits one article's citation list.** The research found what it omitted:
   OrthoFinder v3 (Nat Methods 2026), the annotation-mixing experiment, FCS-GX, the
   bidirectional-best-hit critique.
4. **Adopted from the curriculum survey but not yet folded in:** functional annotation and
   enrichment as an evidence problem; data-resource/browser literacy; comparative functional
   genomics beyond sequence; genome architecture as a coherent topic. A dedicated
   microbial/viral branch and a hands-on lab track were considered and deferred.
