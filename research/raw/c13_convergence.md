## Answer

Claiming *convergent adaptation* requires more than finding the same phenotype—or even the same substitution—in multiple taxa. The minimum case is: (1) the phenotype has multiple genuinely independent origins under a defensible trait-evolution reconstruction; (2) the molecular pattern exceeds a realistic null incorporating branch length, mutation/compositional bias, constraint, phylogenetic uncertainty, and gene-tree discordance; and (3) the association is specifically aligned with the phenotype rather than a correlated ecological variable, shared ancestry, relaxed constraint, or annotation bias. [Storz 2016](https://doi.org/10.1038/nrg.2016.11)

Parker et al. reported nearly 200 convergent loci across 2,326 proteins in echolocating mammals. The 2015 rebuttals showed that their tree-distortion signal had no appropriate matched null: equivalent “convergence” appeared for echolocators versus nonecholocating controls, and their selection test was misapplied. The genome-wide claim therefore did not survive; a small set of auditory candidates remained plausible, but not evidence that echolocation had a pervasive shared coding-sequence basis. [Parker et al. 2013](https://doi.org/10.1038/nature12511) [Thomas & Hahn 2015](https://doi.org/10.1093/molbev/msv013) [Zou & Zhang 2015](https://doi.org/10.1093/molbev/msv014)

A useful evidence ladder is: **candidate** (outlier/homoplasy), **phylogenetically controlled association** (trait-linked excess after calibrated nulls and multiplicity control), **mechanistic support** (the allele/element reproducibly changes the relevant molecular, cellular, or organismal function), and **causal adaptive evidence** (ancestral/derived swaps or precise editing, ideally reciprocal rescue and fitness/performance measurements in the relevant environment). This is an evidential standard, not a formal journal rule; high-tier papers increasingly need the latter two before wording a hit as “causal adaptation,” rather than “associated with convergence.” [Storz 2016](https://doi.org/10.1038/nrg.2016.11) [Liu et al. 2014](https://doi.org/10.1093/molbev/msu195)

Independent trait origins should be counted as posterior-distributed transitions, not tip labels: fit alternative discrete-trait models on a dated species-tree posterior, stochastic-map transitions, and propagate uncertainty into the genomic test. Closely related trait-positive tips are replication-poor; treating them as independent inflates significance. Worse, incomplete lineage sorting, introgression, or recombination can make one change on a discordant gene tree appear as two changes on the species tree (“hemiplasy”). [Hahn & Nakhleh 2016](https://doi.org/10.1093/molbev/msw197) [Guerrero & Hahn 2018](https://doi.org/10.1073/pnas.1811268115)

## Key findings

- Simple convergent-substitution counts must be compared to an explicit substitution-model expectation: chance convergence rises with total divergence, amino-acid accessibility, site constraint, and reconstruction error; divergent substitutions or matched branches are useful empirical controls. [Zou & Zhang 2015](https://doi.org/10.1093/molbev/msv014) [Storz 2016](https://doi.org/10.1038/nrg.2016.11)

- Parker et al.’s simulation-based locus null did not solve the central phenotype-specific-control problem: the rebuttals compared equally distorted, nonecholocating alternative topologies and found no echolocator-specific genome-wide excess. [Parker et al. 2013](https://doi.org/10.1038/nature12511) [Thomas & Hahn 2015](https://doi.org/10.1093/molbev/msv013)

- The rebuttal was a substantial walk-back, not a retraction: the original article remains published, while later work recovered a narrower functional enrichment—cochlear-ganglion-associated genes—using a convergence-versus-divergence enrichment screen. This supports a credible disagreement over *localized functional signal*, not the original “widespread genome-wide convergence” conclusion. [Marcovitz et al. 2019](https://doi.org/10.1073/pnas.1818532116)

- **RERconverge** (package paper 2019; GitHub repository current state, version number not independently verified) correlates gene/element relative evolutionary rates with a binary or continuous phenotype after normalizing each branch against genome-wide rate; it uses phylogeny-aware branch-level association, robust transforms, FDR, and can use phenotype-aware “permulations” to calibrate confidence. It tests rate association, not identical substitutions or adaptive causality. [Kowalczyk et al. 2019](https://doi.org/10.1093/bioinformatics/btz468) [Partha et al. 2019](https://doi.org/10.1093/molbev/msz107) [official repository](https://github.com/nclark-lab/RERconverge)

- **PhyloAcc v1** fits Bayesian conserved/background/accelerated-rate models to conserved noncoding elements and compares them with Bayes factors; target-lineage acceleration is evidence of changed constraint or selection, not automatically positive selection. **PhyloAcc-GT** (2023) additionally integrates gene-tree uncertainty under the multispecies coalescent, reducing ILS-driven false calls. [Hu et al. 2019](https://doi.org/10.1093/molbev/msz049) [Yan et al. 2023](https://doi.org/10.1093/molbev/msad195) [official documentation](https://phyloacc.github.io/)

- **TRACCER** (2021; repository release/version not independently verified) compares trait-bearing branches to their closest trait-lacking relatives, ranking comparisons by topology and using permutations. This deliberately avoids treating distant or non-independent branches as equivalent replicates, but still identifies rate–trait associations rather than causation. [Treaster et al. 2021](https://doi.org/10.1093/molbev/msab226) [official repository](https://github.com/harris-fishlab/TRACCER)

- A complementary count-based method, **ωC**, normalizes nonsynonymous convergence by synonymous convergence to correct phylogenetic errors that inflate both; its authors caution that raw convergent-event counts remain essential with only two or three focal lineages. [Fukushima & Pollock 2023](https://doi.org/10.1038/s41559-022-01932-7)

- Trait-positive tips do not equal independent origins. Count transitions on stochastic maps across uncertainty in topology, dates, character model, and missing/extinct taxa; report the distribution of origins and effective independent contrasts. Standard ancestral reconstructions can be biased by rate heterogeneity and state-dependent diversification. [Joy et al. 2016](https://doi.org/10.1371/journal.pcbi.1004763) [Molina-Venegas et al. 2020](https://doi.org/10.1093/sysbio/syaa022)

- Hemiplasy is especially dangerous in rapid radiations: a single mutation on a discordant genealogy is falsely mapped as repeated convergence on the species tree. Analyze local genealogies/recombination blocks, apply coalescent-aware methods, and treat gene-tree/species-tree concordance as a required diagnostic. [Guerrero & Hahn 2018](https://doi.org/10.1073/pnas.1811268115) [Mendes et al. 2019](https://doi.org/10.1098/rstb.2018.0229)

- A second major walk-back involved high-altitude waterfowl: claims that parallel haemoglobin substitutions explained repeated high-affinity haemoglobin were weakened by protein engineering/functional measurements—most parallel substitutions were irrelevant to oxygen affinity, and most functional convergence came from nonparallel substitutions. [McCracken et al. 2015](https://doi.org/10.1371/journal.pgen.1005681) [Natarajan et al. 2016](https://doi.org/10.1126/science.aaf9070)

- Branch-site positive-selection evidence is not by itself a safeguard: multinucleotide mutations can create false positives under standard branch-site tests, so codon-model hits require models/diagnostics robust to this process. [Venkat et al. 2018](https://doi.org/10.1371/journal.pgen.1007251)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Genome-wide signatures of convergent evolution in echolocating mammals — Parker, Tsagkogeorga, Cotton et al. | 2013 | Nature | [DOI](https://doi.org/10.1038/nature12511) | The claim later reanalysed; 22 mammals, 2,326 orthologues. |
| Determining the Null Model for Detecting Adaptive Convergence from Genomic Data — Thomas & Hahn | 2015 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msv013) | Rebuttal establishing phenotype-matched controls as necessary practice. |
| No Genome-Wide Protein Sequence Convergence for Echolocation — Zou & Zhang | 2015 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msv014) | Reanalysis of counts, controls, and selection tests. |
| Causes of molecular convergence and parallelism in protein evolution — Storz | 2016 | Nature Reviews Genetics | [DOI](https://doi.org/10.1038/nrg.2016.11) | Canonical treatment of nulls, epistasis, functional validation, and hemiplasy. |
| RERconverge: an R package for associating evolutionary rates with convergent traits — Kowalczyk et al. | 2019 | Bioinformatics | [DOI](https://doi.org/10.1093/bioinformatics/btz468) | Tool paper. |
| Robust methods for detecting convergent shifts in evolutionary rates — Partha et al. | 2019 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msz107) | RER normalization and robustness details. |
| Bayesian Detection of Convergent Rate Changes of Conserved Noncoding Elements — Hu, Sackton, Edwards & Liu | 2019 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msz049) | PhyloAcc v1. |
| PhyloAcc-GT — Yan, Hu, Thomas et al. | 2023 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msad195) | Coalescent/gene-tree-aware PhyloAcc. |
| Refining Convergent Rate Analysis with Topology — Treaster, Daane & Harris | 2021 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msab226) | TRACCER. |
| Detecting macroevolutionary genotype–phenotype associations using error-corrected rates of protein convergence — Fukushima & Pollock | 2023 | Nature Ecology & Evolution | [DOI](https://doi.org/10.1038/s41559-022-01932-7) | ωC and error correction. |
| Quantifying the risk of hemiplasy in phylogenetic inference — Guerrero & Hahn | 2018 | PNAS | [DOI](https://doi.org/10.1073/pnas.1811268115) | Quantifies false convergence risk. |
| Predictable convergence in hemoglobin function has unpredictable molecular underpinnings — Natarajan et al. | 2016 | Science | [DOI](https://doi.org/10.1126/science.aaf9070) | Exemplary functional adjudication of a convergence claim. |

## What the standard corpus misses

- **Changed in the last 18 months:** **MoleRate** (2026) introduces an explicit phylogenetic rate test for focal-versus-background nucleotide/protein rates; it is a new candidate alongside RERconverge/PhyloAcc/TRACCER, not yet a replacement benchmark. [Sackton et al. 2026](https://doi.org/10.1093/evolut/qpaf240)

- **Changed in the last 18 months:** a 2025 RERconverge expansion supports complex categorical traits and phenotype-aware timing/relaxation analyses. [Meyer et al. 2025](https://doi.org/10.1093/molbev/msae210)

- **Changed in the last 18 months:** a 2026 synthesis explicitly broadens “genetic convergence” beyond identical sites to rate shifts, amino-acid preference shifts, recurrent gene/element gain-loss, and pathways—useful corrective to site-centric reading lists. [Allard & Kumar 2026](https://doi.org/10.1038/s41576-026-00933-7)

- RERconverge has a 2026 runtime/API update preprint, but it is not peer-reviewed as of the stated date; treat performance claims as provisional. [Meyer et al. 2026 preprint](https://doi.org/10.64898/2026.06.06.730612)

## Caveats and open questions

- There is no universally accepted numerical threshold or formal “four-rung” journal standard for causal convergence. The ladder above is a conservative synthesis of comparative and functional-evolution literature, not an editorial policy.

- The echolocation literature remains genuinely divided at the narrow level: the broad Parker genome-wide coding claim was rebutted, whereas later functional-enrichment work argues for a restricted auditory signal. Neither line alone demonstrates that individual substitutions caused echolocation. [Zou & Zhang 2015](https://doi.org/10.1093/molbev/msv014) [Marcovitz et al. 2019](https://doi.org/10.1073/pnas.1818532116)

- Rate acceleration is directionally ambiguous: it can reflect positive selection, relaxed purifying selection, mutation-rate shifts, GC-biased gene conversion, or model misspecification. Functional and population-genetic evidence is needed to assign mechanism. [Hu et al. 2019](https://doi.org/10.1093/molbev/msz049)

- I found substantial published walk-backs and rebuttals, but did not verify a formal journal retraction of a major molecular-convergence/adaptation paper; therefore no such retraction is claimed here.