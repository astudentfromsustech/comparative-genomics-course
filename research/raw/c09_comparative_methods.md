## Answer

Species are not \(N\) independent replicates because each tip inherits much of its phenotype and genome from shared ancestors; close relatives therefore contribute correlated observations, not new evolutionary trials. Ordinary correlation/regression treats clade membership as repeated evidence and can turn one ancestral change plus many descendants into a small \(P\)-value (“phylogenetic pseudoreplication”). This is more acute in genomics: loci can also share linkage, rate, annotation, alignment, and gene-tree histories. [Dewar, Belcher & West 2025](https://doi.org/10.1038/s41576-024-00803-0)

PIC converts tip values to standardized, non-overlapping ancestral contrasts under Brownian-motion (BM) evolution; PGLS instead fits regression with a phylogeny-derived residual covariance matrix (under BM, PIC and PGLS regression estimators are equivalent). Phylogenetic mixed models generalize this to random phylogenetic effects and can include nonphylogenetic, individual/species-level, and multivariate variance components. None “corrects for phylogeny” without assumptions: tree/topology/branch lengths, trait model, measurement error, and—especially for genomic traits—the relevant history must be adequate. [Felsenstein 1985](https://doi.org/10.1086/284325) [Blomberg et al. 2012](https://doi.org/10.1093/sysbio/syr118) [Housworth, Martins & Lynch 2004](https://doi.org/10.1086/380570)

Model choice is scientific, not a preprocessing checkbox. BM is constant-variance random-walk evolution; OU adds attraction to one or more optima; Early Burst (EB) assumes an exponentially declining rate. OU support is not direct evidence of stabilizing selection: OU parameters/shifts may be weakly identifiable from extant tips, and searching unknown shifts creates a large-\(p\), small-\(n\) model-selection problem. AIC-only OU claims on small or uninformative trees require simulation-based calibration/model adequacy and ideally fossils or independent experimental support. [Ho & Ané 2014](https://doi.org/10.1111/2041-210X.12285) [Boettiger, Coop & Ralph 2012](https://doi.org/10.1111/j.1558-5646.2012.01574.x)

Comparative-genomics scans are association screens, not causal identification. RERconverge tests phenotype-associated relative rate shifts; PhyloAcc tests posterior support for conserved-element acceleration patterns; Forward Genomics tests repeated loss/divergence. Their nulls can still fail through rate heterogeneity, incorrect foreground histories, gene-tree discordance, and correlated genomic features. Report reconstructed transition counts and uncertainty, phylogenetic effective sample size (parameter- and model-specific), calibrated null/permutation results, genome-wide FDR, alternative-tree sensitivity, and independent functional validation. There is no defensible universal minimum number of origins: one origin supports a lineage-specific hypothesis, not a general cross-species genotype–phenotype claim; power depends on tree geometry, effect size, background lineages, and error. [Maddison & FitzJohn 2015 discussion](https://doi.org/10.1093/sysbio/syx014) [Saputra et al. 2021](https://doi.org/10.1093/molbev/msab068)

## Key findings

- PIC assumes BM-like variance accumulation and independent standardized contrasts; BM-PGLS uses the same covariance logic but accommodates regression designs directly. [Felsenstein 1985](https://doi.org/10.1086/284325) [Blomberg et al. 2012](https://doi.org/10.1093/sysbio/syr118)

- PGLS corrects residual covariance conditional on a supplied phylogeny and evolutionary covariance model; it does not establish causality or repair an incorrect tree/model. [PLOS Biology review, 2024](https://doi.org/10.1371/journal.pbio.3002847) [Díaz-Uriarte & Garland 1998](https://doi.org/10.1086/303327)

- Phylogenetic mixed models partition phylogenetic versus residual variance and extend naturally to multivariate/categorical hierarchical models, but retain assumptions about the phylogenetic covariance and exchangeable residual structure. [Housworth, Martins & Lynch 2004](https://doi.org/10.1086/380570) [Hadfield & Nakagawa 2010](https://doi.org/10.1111/j.1420-9101.2009.01915.x)

- BM is a constant diffusion-rate model; OU is mean reversion toward an optimum; EB is an exponential rate slowdown. In a broad trait survey, EB was rarely supported, but that does not prove adaptive radiations are rare because extant-tip EB inference itself can lack power. [Harmon et al. 2010](https://doi.org/10.1111/j.1558-5646.2010.01025.x) [Ingram & Mahler 2013](https://doi.org/10.1111/j.1420-9101.2012.02566.x)

- OU multi-regime fitting is routinely overinterpreted: unknown shift placement makes candidate models proliferate, ML parameters can be non-unique/inaccurately estimated, and conventional criteria can favor excessive complexity. [Ho & Ané 2014](https://doi.org/10.1111/2041-210X.12285)

- Credible nuance: simulations by Cressler, Butler and King found that even relatively small trees can sometimes discriminate simple OU models, while parameter estimates remain poor; “small tree means OU is invalid” is therefore too strong. [Cressler, Butler & King 2015](https://doi.org/10.1093/sysbio/syv043)

- RERconverge estimates branchwise relative evolutionary rates after genome-wide branch-rate normalization, then associates those rates with binary/continuous/categorical phenotype histories; input gene trees are expected to share topology in the basic workflow. [RERconverge repository](https://github.com/nclark-lab/RERconverge) [Kowalczyk et al. 2019](https://doi.org/10.1093/bioinformatics/btz468)

- Raw parametric \(P\)-values from phenotype-rate scans can be non-uniform because of phylogenetic/non-genetic dependence; phylogenetic “permulations” preserve phenotype distribution and phylogenetic structure to calibrate the null, but still require multiple-testing correction. [Saputra et al. 2021](https://doi.org/10.1093/molbev/msab068)

- PhyloAcc is a Bayesian branch-category model for acceleration of conserved noncoding elements, comparing null, target-lineage, and unrestricted rate-shift models; it targets rate-pattern evidence, not a causal mechanism. [Hu et al. 2019](https://doi.org/10.1093/molbev/msz049)

- Original Forward Genomics required an all-or-none “perfect match” loss pattern and lacked phylogenetic/rate correction; the 2016 methods added both controls and formal significance testing. [Prudent et al. 2016](https://doi.org/10.1093/molbev/msw098)

- There is no portable “false-positive rate” for RERconverge, PhyloAcc, or Forward Genomics: published benchmarks are simulation/design dependent. Papers should show empirical null calibration for their own tree/foreground configuration rather than quote a tool-level rate. [Saputra et al. 2021](https://doi.org/10.1093/molbev/msab068) [Hu et al. 2019](https://doi.org/10.1093/molbev/msz049)

- A documented comparative-genomics correction failure: previously reported Rubisco kinetic trade-offs were greatly reduced after phylogenetic reanalysis; the cited CO\(_2\)-specificity/carboxylation-turnover relationship fell from 37.4% to 2.2% explained variance, while phylogeny explained 56.1%. [Dewar, Belcher & West 2025](https://doi.org/10.1038/s41576-024-00803-0)

- A second failure mode is pairwise cross-species functional-genomics comparisons: duplicated/ancestral comparisons are non-independent, and node-age/clade structure can manufacture apparent ortholog–paralog differences under null simulations. [Dunn et al. 2018](https://doi.org/10.1093/gbe/evx254)

- Using a species tree for loci whose gene trees differ can inflate phylogenetic-regression false positives; gene-tree discordance should be treated as a model component or sensitivity analysis, directly connecting this chapter to C6. [Mendes, Fuentes-González, Schraiber & Hahn 2024](https://doi.org/10.1073/pnas.2220389120)

- Effective sample size is below the tip count except on a star tree, is parameter-specific, and should be reported alongside tip \(N\), number/placement/posterior uncertainty of transitions, and model-based power/calibration. [Bartoszek 2016](https://doi.org/10.1016/j.jtbi.2016.06.038) [Boettiger, Coop & Ralph 2012](https://doi.org/10.1111/j.1558-5646.2012.01574.x)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Phylogenies and the comparative method | 1985 | American Naturalist | https://doi.org/10.1086/284325 | Foundational PIC and phylogenetic non-independence argument. |
| Independent contrasts and PGLS regression estimators are equivalent | 2012 | Systematic Biology | https://doi.org/10.1093/sysbio/syr118 | Establishes the BM-regression equivalence. |
| The phylogenetic mixed model | 2004 | American Naturalist | https://doi.org/10.1086/380570 | Canonical phylogenetic random-effects formulation. |
| Intrinsic inference difficulties for trait evolution with Ornstein–Uhlenbeck models | 2014 | Methods in Ecology and Evolution | https://doi.org/10.1111/2041-210X.12285 | Identifiability and unknown-shift-selection pitfalls. |
| Is your phylogeny informative? Measuring the power of comparative methods | 2012 | Evolution | https://doi.org/10.1111/j.1558-5646.2012.01574.x | Simulation-based assessment of model-selection error/power. |
| Detecting adaptive evolution in phylogenetic comparative analysis using the OU model | 2015 | Systematic Biology | https://doi.org/10.1093/sysbio/syv043 | Important qualified counterpoint on OU discrimination and estimation. |
| RERconverge: an R package for associating evolutionary rates with convergent traits | 2019 | Bioinformatics | https://doi.org/10.1093/bioinformatics/btz468 | Tool paper and canonical repository. |
| Phylogenetic Permulations | 2021 | Molecular Biology and Evolution | https://doi.org/10.1093/molbev/msab068 | Empirical-null strategy for comparative genomic rate scans. |
| Bayesian Detection of Convergent Rate Changes of Conserved Noncoding Elements on Phylogenetic Trees | 2019 | Molecular Biology and Evolution | https://doi.org/10.1093/molbev/msz049 | PhyloAcc primary method paper. |
| Controlling for Phylogenetic Relatedness and Evolutionary Rates Improves the Discovery of Associations Between Species’ Phenotypic and Genomic Differences | 2016 | Molecular Biology and Evolution | https://doi.org/10.1093/molbev/msw098 | Corrected Forward Genomics framework and simulations. |
| A phylogenetic approach to comparative genomics | 2025 | Nature Reviews Genetics | https://doi.org/10.1038/s41576-024-00803-0 | Current field-level review with concrete reanalysis critiques. |
| Phylogenomic comparative methods: Accurate evolutionary inferences in the presence of gene tree discordance | 2024 | PNAS | https://doi.org/10.1073/pnas.2220389120 | C6-relevant discordance-aware comparative machinery. |

## What the standard corpus misses

- **2024:** RERconverge’s categorical-trait expansion adds ancestral-state reconstruction, categorical tests, and phylogeny-aware categorical permulations. [Kowalczyk et al. 2024](https://doi.org/10.1093/molbev/msae210)

- **2024:** The statistical-genetics/PCM synthesis explicitly connects phylogenetic covariance models to mixed models for structured populations and highlights shared confounding logic. [Link et al. 2024](https://doi.org/10.1371/journal.pbio.3002847)

- **2024/2025:** Gene-tree/species-tree mismatch is now demonstrated to cause high false-positive rates in comparative regression simulations; analyses of genomic traits should no longer treat a single species tree as automatically sufficient. [Adams et al. 2025](https://doi.org/10.1093/sysbio/syae078) [Mendes et al. 2024](https://doi.org/10.1073/pnas.2220389120)

- **2025:** `phyloConverge` combines nucleotide substitution modeling with phylogeny-aware trait permutation and benchmarks against phyloP, RERconverge+permulation, and Forward Genomics. [Zhang et al. 2025](https://doi.org/10.1093/molbev/msaf101)

- **2025:** The field now has a dedicated recent PhyloG2P review, useful for mapping a fragmented methods vocabulary but secondary to the tools’ primary papers. [From Trees to Traits](https://pmc.ncbi.nlm.nih.gov/articles/PMC12410988/)

## Caveats and open questions

- I could not verify a published universal numerical minimum—such as “three,” “five,” or “ten” independent origins—for defensible claims. Treat any such rule as **[unverified]** unless tied to a prespecified simulation/power analysis for the actual tree, trait coding, and effect size.

- Tool papers demonstrate improved performance under their simulations; they do not establish a single real-world false-positive rate. This is an evidence gap, not a reason to infer one.

- “OU = stabilizing selection” remains contested and generally too strong. OU is a phenomenological process; mechanistic selection claims need independent ecological, population-genetic, fossil, or experimental evidence. [Ho & Ané 2014](https://doi.org/10.1111/2041-210X.12285) [Cressler et al. 2015](https://doi.org/10.1093/sysbio/syv043)

- Whether phylogenetic correction should remove versus partition phylogenetically conserved correlation is a substantive causal question, not a universal statistical rule; multivariate phylogenetic mixed models make that partition explicit. [Housworth et al. 2004](https://doi.org/10.1086/380570)

- **Changed within the last 18 months:** the 2024 categorical RERconverge expansion, 2024 discordance-aware PCM work, 2025 broad comparative-genomics review, and 2025 phyloConverge benchmark materially update a 2015–2023 syllabus.