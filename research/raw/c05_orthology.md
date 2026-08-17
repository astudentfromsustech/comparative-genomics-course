## Answer

Two genes are the same evolutionary entity only in the historical sense: their relationship is determined by the event at their last common gene ancestor—speciation gives orthology, duplication gives paralogy, and transfer complicates both labels. This makes orthology a relation between genes (usually pairs), not a synonym for “same function,” “most similar sequence,” or “one gene per species.” An orthogroup is a taxon-level gene-family clade descending from one gene in the relevant species-set LCA; it can deliberately contain within-species paralogs, so it is not a set of mutually pairwise orthologs. [OrthoFinder manual](https://gensoft.pasteur.fr/docs/OrthoFinder/2.5.5/OrthoFinder-manual.pdf)

Best-BLAST-hit / reciprocal-best-hit (RBH) fails because sequence closeness is an imperfect proxy for the event history: post-speciation duplications create one-to-many/many-to-many co-orthology; differential loss can make surviving paralogs reciprocal “best”; and rate variation, domain fusion/fission, and annotation errors perturb scores. RBH can retain high precision in simple prokaryotic settings, yet simulations and real datasets show it misses up to 60% of orthologous relations in duplication-rich animals/plants. [Altenhoff et al. 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814191/)

There is no defensible universal winner. On revised, curated OrthoBench (70 Bilaterian RefOGs), OrthoFinder v2.4 with outgroups had the highest precision and F-score, while default OrthoFinder had highest recall; even the best method was only ~77% accurate and exactly recovered 23/70 RefOGs. [Emms & Kelly 2020](https://academic.oup.com/gbe/article/12/12/2258/5918455) On QfO’s multi-axis service, SonicParanoid2’s authors report it top in their aggregate of three classifier schemes and Pareto-optimal on several species-tree tests—but the public comparisons used QfO results available in February 2023, and Broccoli was absent, so this is not an independent current leaderboard. [Cosentino et al. 2024](https://link.springer.com/article/10.1186/s13059-024-03298-4)

Practically: use OrthoFinder v3 when gene-tree/reconciliation output and scalable species addition matter; OMA/HOGs when a curated hierarchical database and explicit evolutionary levels matter; SonicParanoid2 or Proteinortho6 when many genomes and low compute/memory dominate. Treat eggNOG-mapper as reference-database functional annotation/assignment, not a replacement for de novo multi-genome orthogroup inference. [OrthoFinder v3](https://www.nature.com/articles/s41592-026-03126-6) [OMA](https://omabrowser.org/oma/home/) [eggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper)

## Key findings

- **Definitions.** Orthologs descend through a speciation event; paralogs through duplication; orthology/paralogy are relations of historical descent, not functional equivalence. [Fitch 1970](https://doi.org/10.2307/2412448)

- **In-paralogs** are paralogs whose duplication occurred after the speciation being considered; collectively they may be **co-orthologs** of a gene in the other lineage, yielding one-to-many/many-to-many orthology. [Altenhoff et al. 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814191/)

- **Ohnologs** are duplicates retained from a whole-genome duplication; they are a mechanistic subset of paralogs, not necessarily one-to-one or syntenically obvious after fractionation. [Singh et al. 2020](https://academic.oup.com/nar/article/48/D1/D724/5587630)

- **Xenolog** terminology remains genuinely unsettled: Fitch’s later definition calls genes xenologous when their connecting history includes interspecies horizontal transfer, whereas event-based orthology definitions and transfer-aware definitions need not return identical sets. [Górecki et al. 2017](https://academic.oup.com/bioinformatics/article/33/5/640/2725487)

- **Homoeologs** are genes/chromosomes that diverged by speciation and were reunited in one allopolyploid genome; some literature instead uses the term broadly for WGD duplicates, an ambiguity worth policing. [Glover et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4920642/)

- **Orthogroup boundary.** It is defined relative to a specified LCA/species set and may contain paralogs; it is neither an assertion of one-to-one orthology nor a universal, taxon-independent “gene family.” [OrthoFinder manual](https://gensoft.pasteur.fr/docs/OrthoFinder/2.5.5/OrthoFinder-manual.pdf)

- **QfO measures a trade-off, not truth.** Its 12 tests span species-tree discordance, reference gene trees, functional concordance, and curated mammalian relations; it evaluates method submissions against proxies because complete true histories are unknowable. [QfO 2022 service paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9252809/) [benchmark documentation](https://orthology.benchmarkservice.org/proxy/doc)

- **QfO ranking criticism.** Its “aggregate” depends on classifier choice; the square-quartile scheme explicitly privileges precision and can rank methods substantially differently from diagonal-quartile and k-means schemes. [SonicParanoid2 methods](https://link.springer.com/article/10.1186/s13059-024-03298-4)

- **OrthoBench criticism and repair.** The original benchmark contained 39% RefOGs judged incorrect on reanalysis; revised Open_OrthoBench publishes input sets, trees, evidence commentaries, and scoring code, but remains only 70 deliberately difficult Bilaterian groups, not a genome-wide ground truth. [Emms & Kelly 2020](https://academic.oup.com/gbe/article/12/12/2258/5918455) [repository](https://github.com/davidemms/Open_Orthobench)

- **OrthoFinder v3 is a material 2026 change.** Released/published in 2026, it adds core-set-plus-linear-species addition (`--assign`), FAMSA by default for scalable alignments, and ASTRAL-Pro species-tree inference. [paper](https://www.nature.com/articles/s41592-026-03126-6) [canonical repository](https://github.com/OrthoFinder/OrthoFinder)

- **SonicParanoid2 (2024)** adds ML-selected “essential” reciprocal searches plus domain-architecture inference; its paper reports 5× faster QfO runtime than OrthoFinder in fast mode and the best aggregate QfO classification rank, but these are author-run comparisons and not an independent complete tool bake-off. [Cosentino et al. 2024](https://link.springer.com/article/10.1186/s13059-024-03298-4)

- **Proteinortho6 (2023)** makes DIAMOND-sensitive pseudo-reciprocal alignment the default, halving directional searches; the authors report large speed/memory gains with small measured precision/sensitivity changes. This remains graph/best-match-derived inference, so its scalability does not remove RBH’s evolutionary blind spots. [Klemm et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10751348/)

- **Broccoli (v1.2 in the 2024 comparison)** combines fast similarity/network steps with phylogenetic placement; SonicParanoid2’s authors found it fast on QfO but memory-intensive and unable to finish their 2,000-MAG test, while public QfO accuracy results were unavailable to them. [Broccoli paper](https://academic.oup.com/mbe/article/37/11/3389/5865275) [comparison limitations](https://link.springer.com/article/10.1186/s13059-024-03298-4)

- **OMA is different in role and output.** Its current ecosystem supplies pairwise orthologs, OMA Groups, and hierarchical orthologous groups (HOGs), and its May 2026 release covers 2,983 species. [OMA current release](https://omabrowser.org/oma/home/) [OMA 2024 paper](https://doi.org/10.1093/nar/gkad1020)

- **eggNOG-mapper is not a de novo orthogrouper.** Stable v2.1.15 maps novel sequences to precomputed eggNOG groups for annotation; v3 is present but the canonical repository says it remains under heavy testing and is not officially released. [official repository](https://github.com/eggnogdb/eggnog-mapper)

- **Input annotation is part of the inference.** Different structural annotation sources yield materially different orthology calls; short proteins/fragmentation can split one biological gene across groups or prevent matching, and isoform choice changes sequence comparison, trees, and benchmark recall. [Prieto-Baños et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12263111/)

- **Recommended mitigation.** Use one protein per locus with a documented, consistent policy; longest isoform is common and required by many tools, whereas OMA can select an evolutionarily conserved isoform. Audit length/domain outliers, remove contamination/redundant near-identical proteomes, retain genomic coordinates/synteny, and reannotate suspicious families before biological interpretation. [revised OrthoBench protocol](https://academic.oup.com/gbe/article/12/12/2258/5918455) [annotation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12263111/)

- **PLM/structure methods are changing homology search, not yet validated orthology assignment.** PLMSearch and embedding-to-Foldseek-style methods improve remote-homology retrieval, especially below ~20% identity, but I found no independent QfO/OrthoBench evidence that they supplant gene-tree/species-tree reconciliation for orthology calls. [Johnson et al. 2024](https://elifesciences.org/articles/91415) [PLMSearch](https://doi.org/10.1038/s41467-024-46808-5)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Distinguishing Homologous from Analogous Proteins — Walter M. Fitch | 1970 | Systematic Zoology | [DOI](https://doi.org/10.2307/2412448) | Foundational event-history terminology |
| Bidirectional Best Hits Miss Many Orthologs in Duplication-Rich Clades such as Plants and Animals — Altenhoff et al. | 2013 | Genome Biology and Evolution | [article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814191/) | Direct RBH precision-versus-recall evidence |
| Standardized benchmarking in the quest for orthologs — Altenhoff et al. | 2016 | Nature Methods | [DOI](https://doi.org/10.1038/nmeth.3830) | QfO benchmark design |
| Benchmarking Orthogroup Inference Accuracy: Revisiting Orthobench — Emms & Kelly | 2020 | Genome Biology and Evolution | [DOI](https://doi.org/10.1093/gbe/evaa211) | Revised RefOGs and comparative winner by metric |
| OrthoFinder: phylogenetic orthology inference for comparative genomics — Emms & Kelly | 2019 | Genome Biology | [DOI](https://doi.org/10.1186/s13059-019-1832-y) | Gene-tree reconciliation workflow |
| SonicParanoid2: fast, accurate, and comprehensive orthology inference with machine learning and language models — Cosentino et al. | 2024 | Genome Biology | [DOI](https://doi.org/10.1186/s13059-024-03298-4) | Recent QfO/scalability claims |
| Proteinortho6: pseudo-reciprocal best alignment heuristic for graph-based detection of (co-)orthologs — Klemm, Stadler & Lechner | 2023 | Frontiers in Bioinformatics | [DOI](https://doi.org/10.3389/fbinf.2023.1322477) | Current graph-method speed/memory trade-off |
| Annotation matters: the effect of structural gene annotation on orthology inference — Prieto-Baños et al. | 2025 | Bioinformatics | [article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12263111/) | Isoform and annotation-quality effects |
| OrthoFinder: improved phylogenetic orthology inference with enhanced accuracy and scalability — Belcher et al. | 2026 | Nature Methods | [DOI](https://doi.org/10.1038/s41592-026-03126-6) | OrthoFinder v3 |
| Homoeologs: What Are They and How Do We Infer Them? — Glover et al. | 2016 | Trends in Plant Science | [DOI](https://doi.org/10.1016/j.tplants.2016.02.005) | Precise homoeolog definition and terminology dispute |

## What the standard corpus misses

The major additions since a typical 2015–2023 corpus are SonicParanoid2’s ML/domain-aware pipeline (2024), Proteinortho6’s pseudo-reciprocal acceleration (2023), the direct annotation/isoform sensitivity study (2025), and OrthoFinder v3’s core-set species-addition architecture (2026). [SonicParanoid2](https://link.springer.com/article/10.1186/s13059-024-03298-4) [Proteinortho6](https://pmc.ncbi.nlm.nih.gov/articles/PMC10751348/) [annotation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12263111/) [OrthoFinder v3](https://www.nature.com/articles/s41592-026-03126-6)

For remote homology, a 2015–2023 reading list will also miss PLM/structure search tools such as PLMSearch and embedding-derived Foldseek inputs. They are compelling candidate-generation tools, but presently lack a comparably mature, independent orthology-assignment benchmark record. [PLMSearch](https://doi.org/10.1038/s41467-024-46808-5) [embedding/Foldseek study](https://elifesciences.org/articles/91415)

## Caveats and open questions

- QfO does not yield a stable single “champion”: benchmark type, precision–recall preference, submitted configuration, and whether developers publish their result change the apparent leader. The SonicParanoid2 aggregate claim is therefore evidence, not a universal verdict. [QfO documentation](https://orthology.benchmarkservice.org/proxy/doc)

- Benchmark independence is imperfect: QfO accepts developer submissions, while the OrthoBench revision is authored by OrthoFinder’s developers—though it openly publishes data, trees, rationale, and scripts. [Open_OrthoBench](https://github.com/davidemms/Open_Orthobench)

- “Ohnolog” is usually WGD-derived duplicate, but whether it should include allopolyploid-derived duplicates or be reserved for autopolyploidy varies across credible sources. [Glover et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4920642/) [Thomas et al. 2017](https://academic.oup.com/sysbio/article/66/6/1007/3610602)

- I could not verify a 2025–2026 independent QfO/OrthoBench leaderboard comparing OrthoFinder v3, current OMA StandAlone, SonicParanoid2, Broccoli, and Proteinortho6 under one frozen dataset/configuration; any stronger “current winner” claim is **[unverified]**.