# Comparative genomics — a research-level course

Sixteen chapters, foundations to referee level, built as self-contained web pages.
**Start at [`course/course.html`](course/course.html).**

The organising idea: the field's methods are **nested**, and a failure at any layer does not
raise an error — it emerges at the top as a plausible, publishable evolutionary story.

```
F1 data standard → F2 homology → F3 phylogeny → F4 structure → F5 selection → F6 function
```

---

## Reading it

Clone and open `course/course.html` in a browser. No build step, no server, no dependencies.

```bash
git clone <this repo>
open comparative_genomics/course/course.html      # macOS
xdg-open comparative_genomics/course/course.html  # Linux
```

The pages are theme-aware — they follow your OS light/dark setting.

## Editing it

Chapters are hand-edited HTML. One directory per chapter, one file inside it, named after the
directory:

```
course/
├── course.html                    the landing page / map
├── _style.css                     ONE stylesheet, shared by all pages
└── 05_orthology/
    └── 05_orthology.html          the whole chapter
```

**Edit the chapter HTML directly.** The CSS is external on purpose: a design change touches one
file instead of seventeen, which is what makes this co-editable without constant merge conflicts.

The markup vocabulary is small and worth skimming before your first edit — `section.stage` for a
numbered band, `.card` in a `.grid`, `.callout` / `.callout.warn` / `.callout.bad`, `pre.fml` for
worked examples, `.tblwrap > table`, `details.walk` for the self-check. Copy an existing block
rather than inventing a class.

Three accent colours carry meaning, so keep them consistent:

| token | means |
|---|---|
| `--signal` red | an artefact, a failure mode, the boring explanation |
| `--accept` teal | what you are entitled to claim; a check that passed |
| `--refuse` amber | contested, unverified, or a claim to withhold |

### Working together

Two people, small repo — branch for anything substantial, push straight to `main` for typos.

```bash
git switch -c ch11-tighten
# edit course/11_selection_inference/11_selection_inference.html
git commit -am "ch11: tighten the pre-flight section"
git push -u origin ch11-tighten     # then open a PR
```

Conflicts are rare as long as you stay out of `_style.css` unless you mean it.

---

## The papers

**The PDFs are not in this repo** — 402 MB of publisher material cannot be redistributed. What is
here is the catalogue you need to find them yourself:

- **[`resources/papers/INDEX.md`](resources/papers/INDEX.md)** — all **172 papers** grouped by
  framework layer, each with a **clickable DOI** and a ✓/· flag for what the author had on disk
- **[`resources/books/INDEX.md`](resources/books/INDEX.md)** — two open-access textbooks, and what
  their *structure* teaches about how this syllabus is ordered:
  - Coop, *Population and Quantitative Genetics* (CC-BY 3.0) — pairs with chapter 03
  - Harmon, *Phylogenetic Comparative Methods* (free) — pairs with chapter 09

Roughly 93 of the 172 are openly available; the rest need institutional access. You do not need any
of them to read the course — every chapter states its own evidence.

## How this was made

Each chapter was researched against the live literature before it was written — **826 sourced
URLs across 15 research briefs** — and the load-bearing claims were verified against their
sources. One citation was corrected in the process: the 12-*Drosophila* aligner study is
*Genome Research*, not MBE.

Two findings changed the syllabus itself. A survey of eleven public curricula found the course
was missing a prerequisite layer — chapters 02 and 03 exist because of it. And the corpus, which
came from one article's citation list, turned out to omit OrthoFinder v3, the annotation-mixing
experiment, FCS-GX and the bidirectional-best-hit critique.

## Known gaps — deliberate, not hidden

1. **Chapters 11 and 14 are written from verified research findings, not from the primary
   literature.** Their corpora are 2/15 and 1/8 because those papers are paywalled. Each page says
   so. The arguments are sourced; you cannot check them against PAML or King & Wilson without
   library access.
2. **Two corpus directories are empty on purpose** — `F2_homology/ancestral_reconstruction` and
   `X_practice/ml_constraint`. The field has those literatures; this corpus does not. Chapters 06
   and 15 list what belongs in them.
3. **Four adopted-but-unfolded topics** from the curriculum survey are recorded in `PLAN.md`:
   annotation-as-evidence, browser literacy, comparative functional genomics, genome architecture.

See [`PLAN.md`](PLAN.md) for the full syllabus, prerequisites and method.

## Licence

Course content (`course/`, `PLAN.md`, `resources/**/INDEX.md`) — **CC BY 4.0**

Third-party PDFs are not covered by either and are not distributed here.
