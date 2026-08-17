## Answer

Demography and gene flow mimic adaptation because most scan statistics measure departures from a simplistic neutral, panmictic baseline—not selection itself. A bottleneck, range expansion, or unmodelled structure changes allele-frequency variance and can make neutral loci extreme in \(F_{ST}\); background selection (BGS) reduces linked neutral diversity most strongly in low-recombination, gene-dense regions, inflating relative differentiation without requiring locus-specific barriers to gene flow. [Cruickshank & Hahn 2014](https://doi.org/10.1111/mec.12796) [Lotterhos & Whitlock 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4228763/)

For a rooted quartet \((((P1,P2),P3),O)\), ILS alone predicts symmetric discordance: ABBA and BABA (and the two discordant gene-tree topologies) have equal expectation. Introgression breaks that symmetry, producing excess sharing/topologies involving the exchanging lineages; critically, those loci also tend to have shorter coalescence times/internal branches (often a mixture of recent introgressed and older MSC coalescences), whereas ILS discordance has symmetric branch-length distributions. [Hibbins & Hahn 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9208645/) [Edelman et al. 2019](https://www.science.org/doi/10.1126/science.aaw2090)

That distinction is not absolute. Old introgression approaches the speciation-time coalescent distribution and recombination erases tract-length evidence; bidirectional or symmetric gene flow can cancel \(D\); ancestral structure, lineage-specific rate variation, selection, erroneous tree/polarization, and unsampled “ghost” donors can all generate or misattribute the same site-pattern asymmetry. Thus a significant \(D\) is evidence against a narrow no-gene-flow quartet null, not an identified donor, direction, date, or adaptive function. [Tricou et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9366450/) [Koppetsch et al. 2024](https://doi.org/10.1093/sysbio/syae028)

Demographic and ARG inference should be used to build competing, simulation-calibrated nulls, not as a single “true history.” PSMC’s original human validation had useful signal roughly 20 ka–3 Ma; MSMC2/SMC++ improve recent resolution with many samples, but all estimates remain coalescent-rate histories, confounded by structure and gene flow. [Li & Durbin 2011](https://doi.org/10.1038/nature10231) [Terhorst et al. 2017](https://doi.org/10.1038/ng.3748)

## Key findings

- **Resolution is measured in coalescent time, not portable calendar years.** Mutation rate, recombination map, sample size, phasing, genome length, recent growth, bottlenecks, and migration determine the observable interval; periods with few coalescences are intrinsically “invisible.” [Terhorst 2025](https://doi.org/10.1038/s41588-025-02323-x)

- **PSMC** uses one diploid genome and, in its original human simulations, was accurate approximately 20 ka–3 Ma; it has little information at more recent or much older times. [Li & Durbin 2011](https://www.nature.com/articles/nature10231)

- **MSMC/MSMC2** use first coalescences across multiple haplotypes, improving recent resolution; MSMC’s human application reported information to ~2 ka, but MSMC2 warns that limited phasing compromises very recent inference and becomes impractical beyond roughly 16 haplotypes. [Schiffels & Durbin 2014](https://doi.org/10.1038/ng.3015) [MSMC2 documentation](https://github.com/stschiff/msmc2)

- **SMC++** combines SMC and frequency-spectrum information, accepts unphased genomes, and gains recent-time power from hundreds of samples; it is still a model-based coalescent-rate estimate, not direct evidence for a size change. [Terhorst, Kamm & Song 2017](https://doi.org/10.1038/ng.3748)

- **dadi** fits a user-specified demographic model to a multidimensional joint SFS (originally up to three simultaneous populations); **fastsimcoal2** uses simulated expected SFS and supports more complex split/migration/admixture models. Both discard most linkage information and their uncertainty must use genome/block bootstrap rather than treating SNPs as independent. [Gutenkunst et al. 2009](https://doi.org/10.1371/journal.pgen.1000695) [Excoffier et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8665742/)

- **Relate** reconstructs genome-wide genealogies for thousands of samples and estimates coalescence rates/selection; current binaries are v1.2.4 (13 September 2025). **tsinfer** infers correlated genealogies/tree sequences and **tskit** stores and analyzes them; neither has a universal calendar-time resolution guarantee. [Relate documentation](https://myersgroup.github.io/relate/) [tsinfer documentation](https://tskit.dev/tsinfer/docs/latest/index.html) [tskit documentation](https://tskit.dev/tskit/docs/stable/)

- **Patterson’s \(D\)** tests ABBA–BABA imbalance genome-wide; **\(f_4\)/\(f\)-branch** summarize correlated allele-frequency covariance across a supplied tree; **\(f_d\)** is a window-oriented, dynamically normalized estimator; and **Dsuite v0.5 r53** implements Dtrios, \(f_4\)-ratio, \(f\)-branch, and windowed \(f_d/f_{dM}\). \(D\) is not a local admixture proportion estimator and has high variance in short windows. [Martin et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4271521/) [Dsuite repository](https://github.com/millanek/Dsuite)

- **QuIBL** compares ILS-only versus ILS+introgression mixtures of discordant-tree internal branch lengths; it therefore supplies the key extra signature beyond \(D\), but relies on sufficiently accurate, approximately independent local trees and loses separability for old events. [QuIBL repository](https://github.com/miriammiyagi/QuIBL) [Edelman et al. 2019](https://www.science.org/doi/10.1126/science.aaw2090)

- **HyDe** tests hybridization using phylogenetic invariants under the coalescent-with-hybridization and can test individuals, but its hybrid-speciation parameterization does not identify donor/recipient reliably under all introgression/ghost scenarios. [Blischak et al. 2018](https://doi.org/10.1093/sysbio/syy023) [Pang & Zhang 2024](https://doi.org/10.1093/sysbio/syad077)

- A credible selection null should jointly simulate the fitted demographic graph, recombination/mutation-rate variation, ascertainment/calling filters, and BGS or a matched low-recombination baseline; report \(F_{ST}\) with \(\pi\), \(d_{XY}\), LD/haplotypes, and replicate contrasts—not an \(F_{ST}\) tail alone. [Lotterhos & Whitlock 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4228763/) [Johri et al. 2017](https://doi.org/10.1098/rstb.2016.0471)

- BGS/recurrent selection can create high-\(F_{ST}\), low-\(\pi\) “islands”; a high-\(F_{ST}\) region without elevated \(d_{XY}\) is therefore not evidence for reduced gene flow. [Cruickshank & Hahn 2014](https://doi.org/10.1111/mec.12796) [Burri 2017](https://academic.oup.com/evlett/article/1/3/118/6697077)

- Demographic change also alters the efficacy of purifying selection: bottlenecks can allow mildly deleterious nonsynonymous substitutions to fix, making elevated lineage \(d_N/d_S\) or MK-style inference ambiguous rather than proof of adaptation. [Hughes 2007](https://doi.org/10.1038/sj.hdy.6801031) [Kryazhimskiy & Plotkin 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2596312/)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Inference of human population history from individual whole-genome sequences — Li, Durbin | 2011 | Nature | [DOI](https://doi.org/10.1038/nature10231) | PSMC and its explicit empirical resolution limits |
| Inferring human population size and separation history from multiple genome sequences — Schiffels, Durbin | 2014 | Nature Genetics | [DOI](https://doi.org/10.1038/ng.3015) | MSMC, cross-coalescence, recent-time improvement |
| Robust and scalable inference of population history from hundreds of unphased whole genomes — Terhorst, Kamm, Song | 2017 | Nature Genetics | [DOI](https://doi.org/10.1038/ng.3748) | SMC++ |
| Inferring the Joint Demographic History of Multiple Populations from Multidimensional SNP Frequency Data — Gutenkunst et al. | 2009 | PLoS Genetics | [DOI](https://doi.org/10.1371/journal.pgen.1000695) | dadi / joint-SFS inference |
| fastsimcoal2: demographic inference under complex evolutionary scenarios — Excoffier et al. | 2021 | Bioinformatics | [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8665742/) | Current fastsimcoal2 formulation |
| A method for estimating genome-wide genealogies for thousands of samples — Speidel et al. | 2019 | Nature Genetics | [DOI](https://doi.org/10.1038/s41588-019-0484-5) | Relate |
| Inferring whole-genome histories in large population datasets — Kelleher et al. | 2019 | Nature Genetics | [DOI](https://doi.org/10.1038/s41588-019-0483-y) | tsinfer/tree-sequence population scale |
| Ancient Admixture in Human History — Patterson et al. | 2012 | Genetics | [DOI](https://doi.org/10.1534/genetics.112.145037) | \(f_2/f_3/f_4\), admixture graphs |
| Evaluating the Use of ABBA–BABA Statistics to Locate Introgressed Loci — Martin et al. | 2015 | Molecular Biology and Evolution | [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4271521/) | Why local \(D\) fails; rationale for \(f_d\) |
| HyDe: A Python Package for Genome-Scale Hybridization Detection — Blischak et al. | 2018 | Systematic Biology | [DOI](https://doi.org/10.1093/sysbio/syy023) | Hybridization invariants |
| Dsuite—fast D-statistics and related admixture evidence from VCF files — Malinsky, Matschiner, Svardal | 2021 | Molecular Ecology Resources | [DOI](https://doi.org/10.1111/1755-0998.13265) | Dsuite and \(f\)-branch implementation |
| Reanalysis suggests that genomic islands of speciation are due to reduced diversity, not reduced gene flow — Cruickshank, Hahn | 2014 | Molecular Ecology | [DOI](https://doi.org/10.1111/mec.12796) | Essential correction to “islands = barriers” inference |

## What the standard corpus misses

- **Changed in the last 18 months:** **SINGER** (Deng, Nielsen & Song, 2025; DOI [10.1038/s41588-025-02317-9](https://doi.org/10.1038/s41588-025-02317-9)) introduced posterior ARG sampling for hundreds of WGS genomes, uncertainty quantification, and benchmarks claiming better robustness to misspecified \(N_e\) than Relate, tsinfer+tsdate, and ARG-Needle. Its current repository reports beta v0.1.9 compatibility with tskit ≥1.0. [SINGER repository](https://github.com/popgenmethods/SINGER)

- **Changed in the last 18 months:** **PHLASH** (Terhorst, 2025; DOI [10.1038/s41588-025-02323-x](https://doi.org/10.1038/s41588-025-02323-x)) is a Bayesian population-size-history method benchmarked against SMC++ and MSMC2; its paper importantly emphasizes formal non-identifiability where coalescences are absent.

- **Changed in the last 18 months:** among-species molecular-clock variation was shown to produce false introgression calls in D-type methods; Dsuite now links an ABBA-clustering workflow to this problem. [Koppetsch, Malinsky & Matschiner 2024](https://doi.org/10.1093/sysbio/syae028)

- A 2015–2023 corpus often underweights ghost lineages: heuristic quartet statistics can detect non-tree signal but cannot generally distinguish sampled donor/recipient exchange from ghost introgression; full-likelihood approaches using topology plus branch lengths are more informative but substantially more demanding. [Pang & Zhang 2024](https://doi.org/10.1093/sysbio/syad077)

## Caveats and open questions

- There is **no defensible universal “time range”** for MSMC2, SMC++, dadi, fastsimcoal2, Relate, or tsinfer. The PSMC 20 ka–3 Ma figure is a human-specific validation, not a transferable rule. [Li & Durbin 2011](https://www.nature.com/articles/nature10231)

- The 2025 SINGER benchmark is strong new evidence, but its superiority claims are primarily from its authors’ simulations and selected human analyses; it does **not** establish that ARGs have displaced SFS/summary-statistic workflows across non-model taxa. Its own paper notes infinite-sites and WGS-data requirements. [SINGER paper](https://doi.org/10.1038/s41588-025-02317-9)

- The “genomic islands are mostly reduced diversity” conclusion is influential but not universal: barriers to gene flow, divergent selection, inversions, and reduced diversity can all yield heterogeneous landscapes. The current defensible consensus is that islands are patterns requiring joint evidence, not a mechanism. [Burri 2017](https://academic.oup.com/evlett/article/1/3/118/6697077) [Ravinet et al. 2017](https://academic.oup.com/jeb/article/30/8/1450/7381696)

- Ghost-lineage error rates are simulation/model dependent; the claim that most significant \(D\) tests reflect ghosts is a warning about realistic undersampling, not a universal empirical estimate. [Tricou et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9366450/)