## Answer

A cross-species comparison is meaningful only when the inputs represent comparable biological objects and their uncertainty is reported: define haplotype/ploidy and assembly target; establish base accuracy, k-mer completeness, conserved-gene completeness, repeat resolution, chromosome assignment and contamination status; then use annotations with comparable evidence, gene-model policy, version, and isoform/protein-selection rules. EBP’s January-2026 reference target is 6.C.Q40 plus <5% false duplications, >90% k-mer completeness, >90% single-copy conserved genes, chromosome assignment, and transcript mappability—not N50 alone. [EBP standards](https://www.earthbiogenome.org/report-on-assembly-standards)

Each defect manufactures a particular evolutionary story: uncollapsed haplotypes/duplication errors manufacture paralogs and gene-family expansions; collapsed repeats or GC-biased missing sequence manufacture gene loss and contraction; fragmented assemblies/annotations manufacture short “novel” genes and broken orthogroups; misjoins manufacture rearrangements/SVs; foreign contigs manufacture genes, HGT, and sometimes whole inferred lineages. These are not hypothetical: VGP comparisons found false loss signatures in ~26–60% of genes in earlier vertebrate assemblies, and heterogeneous annotation inflated apparent lineage-specific genes by up to 15-fold in case studies. [Rhie et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9516821/) [Weisman et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9346927/)

No single metric certifies comparability. BUSCO and compleasm test expected conserved gene content; Merqury tests read-supported k-mers, consensus QV, completeness and (with parental k-mers) phasing; LAI tests intact LTR-retrotransposon continuity. Thus, a high BUSCO can coexist with base, phasing, repeat, structural, or contamination errors; high Merqury cannot establish correct chromosome structure or biology absent from reads; LAI is principally informative for LTR-rich genomes; and compleasm changes BUSCO-like estimates because it reimplements the calculation with miniprot. [BUSCO](https://academic.oup.com/bioinformatics/article/31/19/3210/211866) [Merqury](https://link.springer.com/article/10.1186/s13059-020-02134-9) [LAI](https://academic.oup.com/nar/article/46/21/e126/5068908) [compleasm](https://pubmed.ncbi.nlm.nih.gov/37758247/)

“Annotate every genome with one pipeline” is a defensible comparative design, especially for gene repertoire claims, but is not a universal current standard: 2025 evidence still reports no community-wide annotation standard. It also does not make unlike evidence comparable—e.g., species-specific RNA-seq versus protein-only prediction—and it risks systematically missing fast-evolving/de novo loci. [Prieto-Baños & Glover](https://academic.oup.com/bioinformatics/article/41/7/btaf365/8173798)

## Key findings

- **Assessment stack:** report contiguity plus read-derived QV/k-mer spectra (Merqury), gene-space completeness/redundancy (BUSCO or compleasm), repeat-space continuity where relevant (LAI), phasing, scaffolding/chromosome assignment, and contamination—not an N50 threshold. [EBP standards](https://www.earthbiogenome.org/report-on-assembly-standards) [Merqury](https://link.springer.com/article/10.1186/s13059-020-02134-9)

- **Metric blind spots:** BUSCO’s duplicated calls can signal haplotypic duplication but also real duplication; it samples conserved orthologs rather than lineage-specific genes/repeats. compleasm is a faster miniprot-based BUSCO reimplementation, not an independent evidence class. [BUSCO](https://academic.oup.com/bioinformatics/article/31/19/3210/211866) [compleasm repository](https://github.com/huangnengCSU/compleasm)

- **Pipelines differ in evidence integration:** BRAKER3 combines GeneMark-ETP and AUGUSTUS predictions using RNA-seq and protein evidence, with TSEBRA selecting transcript models by extrinsic support; Helixer is cross-species deep-learning/HMM ab initio prediction; EGAPx aligns proteins and RNA reads, then uses Gnomon plus HMM prediction. [BRAKER3](https://genome.cshlp.org/content/34/5/769) [TSEBRA](https://doi.org/10.1186/s12859-021-04482-0) [Helixer](https://pmc.ncbi.nlm.nih.gov/articles/PMC8016489/) [EGAPx](https://github.com/ncbi/egapx)

- **How much is artefact?** There is no defensible universal percentage of cross-species gene-count variation attributable to annotation. Concrete bounds are severe but study-specific: draft assemblies had more than half of genes with wrong copy number in examined genomes; mixed annotations produced up to 15-fold more apparent lineage-specific genes. [Denton et al.](https://digitalcommons.wustl.edu/open_access_pubs/3596/) [Weisman et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9346927/)

- **Concrete false biology:** false duplicated sequence in older and some VGP vertebrate assemblies yielded false gene/exon/chimeric-gene gains and overestimated gene-family/LTR expansions; older assemblies falsely lacked GC-rich genes such as platypus *COQ6*. [false gains](https://pmc.ncbi.nlm.nih.gov/articles/PMC9516828/) [false losses](https://pmc.ncbi.nlm.nih.gov/articles/PMC9516821/)

- **False SV example:** 39 Mb of previously identified cattle segmental duplications were likely Btau4.2 assembly error, so assembly defects can manufacture copy-number/SV landscape claims. [review documenting the Zimin et al. result](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2014.00037/full)

- **Contamination magnitude:** FCS-GX found 36.8 Gbp (0.16%) suspected contamination across 1.6 million GenBank assemblies; half came from 161 egregious assemblies, so this aggregate does not estimate the fraction of *older comparative papers* invalidated. [Astashyn et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC10246020/)

- **Concrete false HGT:** a 2026 reanalysis concluded that contamination substantially undermined a 2021 claim about cross-phylum antibiotic-resistance dissemination; its code is public. [Godron, Ruppé & Leclercq 2026](https://www.nature.com/articles/s41467-026-69064-1) [code](https://github.com/ngodron/Matters_Arising_2025)

- **Last 18 months:** EBP revised assembly standards in January 2026; EGAP 10.6 (June 2026) automated protein-evidence selection; 2025 showed established annotation sources still produce materially different orthology results; Tiberius (2024) and its multi-clade extension (2026) represent the deep-learning annotation shift. [EBP](https://www.earthbiogenome.org/report-on-assembly-standards) [EGAP release notes](https://www.ncbi.nlm.nih.gov/refseq/annotation_euk/release_notes/) [annotation study](https://academic.oup.com/bioinformatics/article/41/7/btaf365/8173798) [Tiberius multi-clade](https://pmc.ncbi.nlm.nih.gov/articles/PMC13142403/)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Merqury: reference-free quality, completeness, and phasing assessment for genome assemblies | 2020 | Genome Biology | [DOI](https://doi.org/10.1186/s13059-020-02134-9) | Read-k-mer QV, completeness, and phasing |
| Assessing genome assembly quality using the LTR Assembly Index (LAI) | 2018 | Nucleic Acids Research | [DOI](https://doi.org/10.1093/nar/gky730) | Repeat-space metric |
| compleasm: a faster and more accurate reimplementation of BUSCO | 2023 | Bioinformatics | [DOI](https://doi.org/10.1093/bioinformatics/btad595) | BUSCO-like gene completeness, alternative implementation |
| BRAKER3: Fully automated genome annotation using RNA-seq and protein evidence with GeneMark-ETP, AUGUSTUS, and TSEBRA | 2024 | Genome Research | [DOI](https://doi.org/10.1101/gr.278090.123) | Evidence-integrating structural annotation |
| Mixing genome annotation methods in a comparative analysis inflates the apparent number of lineage-specific genes | 2022 | Current Biology | [DOI](https://doi.org/10.1016/j.cub.2022.04.085) | Direct comparative-annotation artefact experiment |
| Widespread false gene gains caused by duplication errors in genome assemblies | 2022 | Genome Biology | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9516828/) | False expansion mechanism and vertebrate examples |
| False gene and chromosome losses in genome assemblies caused by GC content variation and repeats | 2022 | Genome Biology | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9516821/) | False-loss mechanism and recovery with VGP assemblies |
| Rapid and sensitive detection of genome contamination at scale with FCS-GX | 2024 | Genome Biology | [DOI](https://doi.org/10.1186/s13059-024-03198-7) | Large-scale contamination estimates and screening method |
| Annotation matters: the effect of structural gene annotation on orthology inference | 2025 | Bioinformatics | [DOI](https://doi.org/10.1093/bioinformatics/btaf365) | Current cross-source annotation/orthology benchmark |

## What the standard corpus misses

A 2015–23 corpus will usually miss the January-2026 EBP revision, FCS-GX’s 2024 database-scale cleanup, public EGAPx and EGAP 10.6 changes, the 2025 direct test of annotation-source effects on orthology, and Tiberius’s 2024–26 deep-learning models. It will also miss the 2026 contamination reanalysis of HGT claims. [EBP](https://www.earthbiogenome.org/report-on-assembly-standards) [FCS-GX](https://pmc.ncbi.nlm.nih.gov/articles/PMC10246020/) [EGAPx](https://github.com/ncbi/egapx) [Tiberius](https://pubmed.ncbi.nlm.nih.gov/39558581/) [HGT reanalysis](https://www.nature.com/articles/s41467-026-69064-1)

## Caveats and open questions

There is no audited estimate of how much of the *older comparative literature* changes after modern contamination screening; the FCS-GX aggregate is not that estimate. [FCS-GX](https://pmc.ncbi.nlm.nih.gov/articles/PMC10246020/)

Credible sources disagree in emphasis on contamination versus genuine transfer: FCS-GX reports that its approach did not create excess calls in genomes with high-confidence LGT, whereas the 2026 reanalysis demonstrates that unvetted contaminated references can overturn a specific HGT-derived conclusion. The practical resolution is locus-level validation with raw-read coverage, contig context, taxonomic screening, and independent assemblies—not treating either HGT or contamination as a default explanation. [FCS-GX](https://pmc.ncbi.nlm.nih.gov/articles/PMC10898089/) [HGT reanalysis](https://www.nature.com/articles/s41467-026-69064-1)

T2T/VGP quality raises the baseline but does not eliminate repeat-, haplotype-, polyploidy-, or evidence-limited annotation errors; the evidence supports a multi-metric, claim-specific standard rather than a universal cutoff. [EBP standards](https://www.earthbiogenome.org/report-on-assembly-standards)