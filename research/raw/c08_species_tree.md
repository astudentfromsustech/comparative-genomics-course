## Answer

A species tree is the shared coordinate system because it assigns every sampled genome to a lineage, orders speciation events, roots/polarizes substitutions, and defines the ancestral branch on which a gene gain/loss, rearrangement, rate shift, or trait transition is mapped. But it is a model of population splits, not a claim that every locus followed that topology: under the multispecies coalescent (MSC), alleles can fail to coalesce in a short ancestral interval, so gene trees are expected to vary around the species tree. [BEAST 2 MSC overview](https://doi.org/10.1371/journal.pcbi.1006650)

The current practical consensus is neither “concatenate is wrong” nor “ASTRAL is automatically right.” Concatenated ML can be statistically inconsistent under MSC gene-tree heterogeneity, including anomaly-zone parameter combinations; more sequence then yields confidence in the pseudo-true supermatrix tree. [Kubatko & Degnan 2007](https://doi.org/10.1080/10635150601146041) Summary MSC methods such as ASTRAL scale to genome-sized locus sets and are statistically consistent under their assumptions, but inherit gene-tree estimation error and are not robust to introgression, duplication/loss, or linked loci merely because they are coalescent-based. [ASTRAL paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4147915/) Full-likelihood MSC approaches (*BEAST/StarBEAST2, BPP) jointly model sequence and gene-tree uncertainty, but are usually computationally restricted relative to ASTRAL-scale datasets. [MSC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8692950/)

Thus, strong recent practice is plural: infer a partitioned concatenation tree and an MSC summary tree; quantify locus/site/quartet conflict; test topology robustness to locus definitions and filtering; then investigate biological causes of stable conflict. A recent angiosperm analysis explicitly ran concatenation and ASTRAL on multiple orthology datasets, collapsed weak gene-tree edges before ASTRAL, and interpreted discordance through both ILS and hybridization. [study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12785169/)

Bootstrap asks whether resampled characters recover the fitted analysis; it is not the fraction of genes or sites supporting a split. Hence 100% bootstrap with low gCF is routine under genome-scale data and model misspecification. Report gCF, likelihood-based sCF, ASTRAL quartet frequencies/local posterior probabilities, branch lengths in coalescent units, and sensitivity analyses—not one support number. [IQ-TREE documentation](https://www.iqtree.org/doc/Concordance-Factor)

For dates, sequence data primarily identify substitutions; absolute time depends materially on rate assumptions and fossil/time priors. Published dates must expose calibration justification, effective marginal priors, prior-only versus posterior plots, clock-model and calibration leave-one-out sensitivity, and uncertainty intervals. [dos Reis & Yang 2013](https://doi.org/10.1111/j.1759-6831.2012.00236.x)

## Key findings

- Under the MSC, ILS becomes more probable with short internodes and larger ancestral effective population size; with at least four taxa, the most probable gene tree can differ from the species tree in the anomaly zone. [BEAST 2 MSC overview](https://doi.org/10.1371/journal.pcbi.1006650)

- ML concatenation and bootstrap can converge on a strongly supported wrong tree under coalescence; this is a formal inferential failure, not merely a finite-data nuisance. [Kubatko & Degnan 2007](https://doi.org/10.1080/10635150601146041)

- ASTRAL is designed to estimate an MSC species tree from unrooted gene trees and was shown to be statistically consistent under its model; its comparative advantage rises with moderate/high ILS, whereas concatenation performed better in the authors’ low-ILS simulations. [Mirarab et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4147915/)

- gCF is the proportion of *decisive gene trees* containing a reference split; sCF is the proportion of decisive sites supporting it. They measure empirical concordance, whereas bootstrap measures resampling stability under the analysis. [IQ-TREE documentation](https://www.iqtree.org/doc/Concordance-Factor)

- Use likelihood-based `--scfl`, available since IQ-TREE 2.2.2, rather than the original parsimony sCF where feasible; it was designed to reduce homoplasy and taxon-sampling effects. [Mo et al. 2023](https://doi.org/10.1093/bioinformatics/btac741)

- Gene-tree error and missing data affect both concatenation and MSC summary inference; filtering can help or hurt depending on ILS and locus signal, so a single “occupancy threshold” is not a defensible universal rule. [Molloy & Warnow 2018](https://doi.org/10.1093/sysbio/syx077)

- Substitution saturation can misestimate topology even under the selected substitution model; saturation-based locus exclusion improved inference across the authors’ 36 empirical phylogenomic datasets, but this does not validate filtering by itself for a new dataset. [Dornburg et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9016599/)

- Full-likelihood MSC tools explicitly integrate gene-tree/species-tree uncertainty; the literature describes *BEAST and BPP as common Bayesian MSC implementations, while noting substantially poorer scaling for some joint network/species-tree applications. [Yang & Flouri 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8692950/)

- Fossil calibrations interact with tree priors, so the effective marginal prior for a calibrated node can differ when calibrations are used alone versus together; calibration “cross-validation” can therefore select bad constraints. [Warnock, Parham & Joyce 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4262156/)

- Specific documented disagreement: angiosperm crown estimates span early Cretaceous to Triassic across molecular studies, versus a much younger unambiguous fossil record; authors disagree over whether rate/calibration artefacts, fossil incompleteness, or both explain the gap. [Coiro et al. 2019](https://doi.org/10.1111/nph.15708) [Smith 2024](https://doi.org/10.1111/nph.20076)

- Specific documented disagreement: placental-mammal molecular dates have often implied a pre-K–Pg origin, whereas geomolecular calibration modelling yielded younger estimates compatible with a radiation near 66 Ma. [dos Reis et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3396900/) [Phillips 2016](https://doi.org/10.1093/sysbio/syv115)

- RelTime is a fast relative-rate framework; under matched alignment, topology, model, and calibration densities, one benchmark found node-age estimates closely comparable to MCMCtree and BEAST, which does **not** imply agreement when priors/calibrations differ. [Tao et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984362/)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Inconsistency of Phylogenetic Estimates from Concatenated Data under Coalescence — Kubatko, Degnan | 2007 | Systematic Biology | [DOI](https://doi.org/10.1080/10635150601146041) | Canonical concatenation-inconsistency demonstration. |
| ASTRAL: genome-scale coalescent-based species tree estimation — Mirarab et al. | 2014 | Bioinformatics | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4147915/) | ASTRAL theory, scaling, and simulations. |
| Multispecies Coalescent: Theory and Applications in Phylogenetics — Mirarab, Nakhleh, Warnow | 2021 | Annual Review of Ecology, Evolution, and Systematics | [DOI](https://doi.org/10.1146/annurev-ecolsys-012121-095340) | Broad MSC assumptions and limits. |
| New methods to calculate concordance factors for phylogenomic datasets — Minh, Hahn, Lanfear | 2020 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msaa106) | Defines gCF/sCF. |
| Updated site concordance factors minimize effects of homoplasy and taxon sampling — Mo et al. | 2023 | Bioinformatics | [DOI](https://doi.org/10.1093/bioinformatics/btac741) | Current likelihood-based sCF method. |
| To Include or Not to Include: The Impact of Gene Filtering on Species Tree Estimation Methods — Molloy, Warnow | 2018 | Systematic Biology | [DOI](https://doi.org/10.1093/sysbio/syx077) | Filtering/ILS/gene-tree-error benchmark. |
| Comparison of different strategies for using fossil calibrations to generate the time prior in Bayesian molecular clock dating — Barba-Montoya, Dos Reis, Yang | 2017 | Molecular Phylogenetics and Evolution | [DOI](https://doi.org/10.1016/j.ympev.2017.07.005) | Calibration combinations and time priors. |
| The unbearable uncertainty of Bayesian divergence time estimation — dos Reis, Donoghue, Yang | 2013 | Journal of Systematics and Evolution | [DOI](https://doi.org/10.1111/j.1759-6831.2012.00236.x) | Why more sequence alone need not fix absolute-time uncertainty. |
| BEAST 2.5: An advanced software platform for Bayesian evolutionary analysis — Bouckaert et al. | 2019 | PLOS Computational Biology | [DOI](https://doi.org/10.1371/journal.pcbi.1006650) | BEAST/MSC/clock framework. |
| MCMCtree / PAML source and documentation | current | GitHub | [PAML repository](https://github.com/abacus-gene/paml) | Official implementation; version history reports PAML 4.10.10 (20 Jan 2026). |

## What the standard corpus misses

- **2024–2025 interpretation of concordance factors:** Lanfear and Hahn argue that quartet frequencies, gCF/sCF, and statistical support answer different questions and should not be relabelled as interchangeable “support.” [paper](https://doi.org/10.1093/molbev/msae214)

- **Recent empirical norm:** the 2025 Mesangiospermae study compares alternative orthology construction, concatenation, ASTRAL, gene-tree-edge collapsing, and introgression/ILS explanations rather than presenting one pipeline as decisive. [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12785169/)

- **Tool changes in the last 18 months:** PAML 4.10.10 fixed an MCMCtree birth–death-prior bug and added MCMC-sample combining; verify software version in any reproduced analysis. [official history](https://github.com/abacus-gene/paml/blob/master/doc/pamlHistory.txt)

- **Tool changes in the last 18 months:** BEAST 2’s current release line is 2.7.8; the release notes specify it is a package release built on installation of 2.7.7. [official releases](https://github.com/CompEvol/beast2/releases)

- **Tool changes in the last 18 months:** MEGA 12.1 added/reworked calibration-management functionality for RelTime, including saved/reusable calibration sets and TimeTree API access. [official history](https://megasoftware.net/history)

## Caveats and open questions

The MSC is a null model for ILS, not a universal explanation for gene-tree conflict: introgression, hybridization, paralogy, recombination within loci, selection, alignment/model error, and reference/orthology error can mimic or compound it. ASTRAL’s consistency result does not transfer automatically to these violations. [MSC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8692950/)

There is no verified field-wide 2024–2026 vote for one estimator. The defensible consensus is conditional model comparison and transparent conflict reporting; credible authors still differ on how much to trust concatenation, gene-tree summary methods, and full MSC analyses in particular empirical regimes. [ASTRAL paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4147915/) [MSC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8692950/)

I could not verify a peer-reviewed, general 2025–2026 benchmark establishing that one dating engine dominates MCMCtree, BEAST2, and RelTime under realistic calibration error. Claims of software superiority should therefore be treated as dataset- and prior-conditional.