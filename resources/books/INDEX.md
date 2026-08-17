# Books — open-access texts, filed like papers

`<Stem>/<Stem>.pdf`, same convention as `resources/papers/`. Only openly licensed or freely
published texts are stored here.

| Book | Year | Pages | Licence | Supports |
|---|---|---|---|---|
| [Coop, *Population and Quantitative Genetics*](Book2023_Coop-population-quantitative-genetics/) | v1.2 | 324 | **CC-BY 3.0** | Ch 03 · molecular evolution & popgen |
| [Harmon, *Phylogenetic Comparative Methods*](Book2019_Harmon-phylogenetic-comparative-methods/) | — | 234 | freely published, lukejharmon.github.io/pcm | Ch 09 · comparative methods |

## Not downloadable — commercial

The curriculum survey named these as standard. All are paywalled; get them through a library.

| Book | Why it matters |
|---|---|
| Yang, *Molecular Evolution: A Statistical Approach* (OUP) | The reference for codon models and likelihood — Ch 02, 11 |
| Anisimova (ed.), *Evolutionary Genomics*, 2e (MiMB) | Method-by-method survey — Ch 03, 11, 12 |
| *Comparative Genomics: Methods and Protocols*, 2e (MiMB) | Has dedicated prokaryotic gene-family, pangenome-core and AMR chapters |
| Lesk, *Introduction to Genomics* 3e / *Bioinformatics* 5e | Undergraduate floor |
| Compeau & Pevzner, *Bioinformatics Algorithms* 3e | Algorithms for Ch 02 |

---

## What their structure teaches

### Coop — the ordering argument for Chapter 03

```
allele & genotype frequencies  →  population structure & correlations among loci
  →  drift & neutral diversity (THE COALESCENT)
  →  divergence & molecular substitution  →  TESTS of molecular evolution
  →  neutral diversity & population structure: split models, migration, INCOMPLETE LINEAGE SORTING
  →  phenotypic variation  →  response to selection  →  one-locus selection
  →  selection × mutation × migration  →  drift on selected alleles
  →  LINKED SELECTION (genome-wide effects)  →  multiple selected loci
  →  appendix: calculus & probability
```

Four things worth copying:

1. **Frequencies and HWE come first**, before drift or selection. My draft plan for Ch 03 opened
   with "neutrality as a null" — that is a step too high. The floor is allele/genotype frequencies.
2. **The coalescent sits inside neutral diversity**, not in a phylogenetics chapter. It is a
   population-genetic object that phylogenetics later borrows.
3. **Incomplete lineage sorting is taught as a population-structure consequence** — before species
   trees, not during them. That independently confirms placing Ch 03 before Ch 08.
4. **Tests of molecular evolution follow immediately from the neutral substitution process.** The
   null for dN/dS is derived where the substitution process is, not where the test is applied — an
   argument for introducing the null in Ch 03 and the test in Ch 11.

Also note the **maths appendix**: even a foundations text admits a floor under its floor.
Quantitative genetics (breeder's equation, multivariate response) is a large part of Coop and is
mostly **out of scope** for this course.

### Harmon — the model for Chapter 09

```
research program  →  FITTING STATISTICAL MODELS TO DATA (ML, Bayes, AIC)
  →  Brownian motion  →  fitting BM (contrasts, ML, Bayesian)
  →  multiple characters & evolutionary correlation
  →  beyond BM: rate variation, OU/stabilizing selection, early burst, peak shifts
  →  discrete characters: Mk  →  fitting Mk  →  beyond Mk (Pagel's λ/δ/κ, threshold)
  →  birth–death  →  fitting BD  →  beyond BD
  →  characters AND diversification rates (SSE) + "potential pitfalls"
  →  what have we learned from the trees
```

Three lessons:

1. **An entire chapter on statistical model fitting comes before any biology** — hypothesis
   testing, maximum likelihood, Bayes, AIC-versus-Bayes. This is the third independent source
   saying my course lacks a statistical floor.
2. **Continuous traits before discrete**, and *fitting* is separated from *the model* at every
   step — model, then fitting, then "beyond". A clean template for Ch 09.
3. **Section 8.5 is called "the total garbage test."** A foundations text builds in a
   does-this-model-mean-anything check. That is the same instinct as this course's evidence ladder,
   and worth borrowing explicitly.

**Scope note:** Harmon's Chapters 10–13 (birth–death, diversification, state-dependent
diversification) are macroevolution, not comparative genomics — out of scope here. But the
birth–death maths is *the same maths* as CAFE's gene-family model in Ch 07, so his treatment is
the best available explanation of what CAFE actually fits.
