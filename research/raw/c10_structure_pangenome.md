## Answer

When comparison becomes a path through a clade, the reference coordinate is no longer the biological object: it is one projection of a multi-genome alignment. A “variant” becomes an alternative traversal between homologous graph contexts, and a genotype becomes support for one or more named paths—not merely a REF/ALT state at a GRCh38 position. This makes insertions, inversions, duplications, and sequence absent from the chosen reference directly representable, but it also makes equivalence conditional on graph construction, path set, repeat resolution, and coordinate convention. The HPRC graph contains 129.3 Mb of non-GRCh38 sequence; a reference-tree formulation identified 3.5 million variants not located on the linear reference, illustrating why VCF-against-GRCh38 is no longer sufficient as the sole comparison language. [Defining and cataloging variants in pangenome graphs](https://pmc.ncbi.nlm.nih.gov/articles/PMC12340789/)

Practically, comparative genomics shifts from “what differs at locus *x*?” to: “which paths are homologous, which sequence/path is traversed in each lineage, and is the apparent loss a true deletion, an unassembled repeat, or an annotation mismatch?” The latter distinction is decisive for PAV, copy number, and gene-family evolution. A negative call needs independent support—adequate read breadth/depth, assembly continuity and read evidence across flanks, repeat-aware homology search, and harmonized annotation—not just absence of a gene model. [GET_PANGENES](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552430/) [PAV methodological evaluation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12856356/)

This transition has real benefits: HPRC Release 1 reduced small-variant discovery errors by 34% and increased detected SVs per haplotype by 104% relative to GRCh38 workflows. [Liao et al., 2023](https://doi.org/10.1038/s41586-023-05896-x) T2T-CHM13 also adds/corrects 238 Mb of non-collinearly aligning sequence, largely centromeric satellites and segmental duplications, so these regions can finally be framed as comparative sequence rather than gaps. [Nurk et al., 2022](https://doi.org/10.1126/science.abj6987)

The cost is methodological: graph topology and path sampling can change the alleles and breakpoints reported. Therefore, claims should report graph build/version/parameters, input assemblies and order, coordinate projection, repeat handling, and benchmarks stratified by difficult regions—not only a merged VCF.

## Key findings

- **State at 2026-08-17:** the official HPRC site advertises Data Release 2 (announced 12 May 2025), with >230 samples, phased near-T2T assemblies, gene annotations, graph-based assembly alignments, and long-read methylation calls. [HPRC official site](https://humanpangenome.org/) [HPRC data-use documentation](https://humanpangenome.org/data-use/)

- **Changed in the last 18 months:** the July 2026 HPRC2 preprint describes 460 haplotypes, selected to cover >99% of common variation in All of Us v8, plus multi-assembly alignment, pantranscriptome, panepigenome, local ancestry, and formal pangenome coordinate systems. This is a major resource change, but remains a preprint as of the cutoff. [HPRC2 preprint](https://www.biorxiv.org/content/10.64898/2026.07.21.739710v1.full)

- **minigraph** incrementally maps assemblies onto an initially linear backbone and produces a compact SV-oriented GFA graph; its construction is fast and scalable, but approximate mapping omits much small variation and yields less precise SV breakpoints/allelic paths than base-level approaches. [Li, 2020](https://doi.org/10.1186/s13059-020-02168-z) [graph-construction comparison](https://pmc.ncbi.nlm.nih.gov/articles/PMC10691155/)

- **Minigraph-Cactus** first uses minigraph to establish large SV structure, then Cactus base-level alignment to add small variants; it outputs GFA, HAL multiple alignment, VCF, and `vg` mapping indexes. In the HPRC build, unalignable centromeric sequence may be clipped, so it should not be read as a fully repeat-complete graph. [Hickey et al., 2024](https://doi.org/10.1038/s41587-023-01793-w) [Cactus documentation](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/pangenome.md?plain=1)

- **PGGB** is reference-free/all-to-all: `wfmash` alignment → `seqwish` graph induction → `smoothxg` normalization → `gfaffix` simplification. Its identity/segment parameters materially determine graph topology. PGGB and Minigraph-Cactus retain substantially more small variation than minigraph; published comparisons find broadly similar SV sets but different breakpoint/path precision and graph complexity. [PGGB repository/docs](https://github.com/pangenome/pggb) [Garrison et al., 2024](https://doi.org/10.1038/s41592-024-02430-3) [Andreace et al., 2023](https://doi.org/10.1186/s13059-023-03098-2)

- **Newer additions:** `pangene` builds a gene graph by mapping proteins to assemblies and represents each genome as a walk, useful for gene-content comparison; `impg` is an emerging implicit-graph approach that queries an all-vs-all alignment network rather than materializing a whole-genome graph. Neither substitutes for a sequence-resolved assembly graph when the question is SV sequence or repeat architecture. [pangene repository](https://github.com/lh3/pangene) [impg repository](https://github.com/pangenome/impg)

- **Demonstrated reference-bias gains in variant calling:** HPRC Release 1 reported 34% fewer small-variant discovery errors and 104% more SVs per haplotype than GRCh38 workflows. A later pangenome-aware DeepVariant analysis reduced errors from the linear baseline by 5% using the full 88-haplotype HPRC-v1.1 graph. [Liao et al., 2023](https://doi.org/10.1038/s41586-023-05896-x) [pangenome-aware DeepVariant](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157594/)

- **Changed in the last 18 months:** HPRC2 reports reductions of 36.0–52.4% in total point-variant errors, and 50.1–67.7% in SNP errors, across tested technologies against GIAB v5.0; treat these as preprint results pending independent replication. [HPRC2 preprint](https://www.biorxiv.org/content/10.64898/2026.07.21.739710v1.full)

- **Expression quantification:** the strongest direct evidence is for allele-specific/haplotype-specific transcript quantification, where `mpmap`+`rpvg` infers transcript-path abundance from a spliced graph and was benchmarked against WASP in simulated and NA12878 RNA-seq analyses. The literature supports reduced ASE bias, but I did not find a general human bulk-RNA-seq percentage improvement that is comparably established across cohorts. [Sibbesen et al., 2023](https://doi.org/10.1038/s41592-022-01731-9) [rpvg repository](https://github.com/jonassibbesen/rpvg)

- **SV discovery:** long-read alignment callers include Sniffles2, cuteSV, SVIM, pbsv, SVDSS and assembly-comparison approaches such as dipcall/SVIM-asm. Caller, aligner, technology, coverage, SV class, and truth-set region all affect results; no caller is uniformly best. [Sniffles2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11217151/) [alignment-versus-assembly benchmark](https://doi.org/10.1038/s41467-024-46614-z)

- **Graph genotyping:** `vg`/Giraffe maps reads to haplotype-threaded graph paths and can call/genotype represented alleles; Giraffe was used to genotype 167,000 known SVs in 5,202 short-read genomes. PanGenie is a k-mer-based short-read genotyper for SNPs, indels, and SVs represented by a pangenome graph. [Hickey et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9365333/) [PanGenie documentation](https://pangenie.readthedocs.io/en/latest/)

- **SV merging is an equivalence problem, not bookkeeping:** Jasmine jointly refines/merges population SV calls; Truvari benchmarks and collapses variants using sequence and breakpoint similarity, and explicitly notes that its standard `bench` comparison is 1-to-1. Report thresholds and whether alleles were sequence-harmonized before comparison. [Jasmine preprint/repository record](https://repository.cshl.edu/id/eprint/40187/) [Truvari paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9793516/) [Truvari documentation](https://github.com/ACEnglish/truvari)

- **PAV evidence standard:** require a high-quality assembly with intact flanks, read remapping that demonstrates absence by breadth and depth, repeat/paralogue-aware sequence search, and uniform reannotation or annotation lift-over. One published Brassica rule classified genes absent only when all exon bases had <2 reads and <5% exon breadth; this is an example threshold, not a universal standard. [Brassica PAV methodology](https://onlinelibrary.wiley.com/doi/10.1111/pbi.13674) [GET_PANGENES](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552430/)

- **T2T changes the comparable substrate:** CHM13 is 3.055 Gb, closes all autosomes and X telomere-to-telomere, and adds/corrects 238 Mb non-collinear to GRCh38; 76% is centromeric satellite, 19% nonsatellite SD, and 4% rDNA. It enables direct analysis of centromere architecture, acrocentric/rDNA organization, repeat expansions, paralogous loci, and SD-mediated rearrangement—but CHM13 is one haplotype, not a population reference. [Nurk et al., 2022](https://doi.org/10.1126/science.abj6987)

- T2T comparison identified 81 Mb of previously unresolved or structurally variable segmental duplications and revised estimated human SD content from 5.4% to 6.7%; these are newly comparable loci, but orthology assignments remain difficult in high-identity duplications. [Vollger et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8979283/)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| The design and construction of reference pangenome graphs | 2020 | Genome Biology | [Li, DOI: 10.1186/s13059-020-02168-z](https://doi.org/10.1186/s13059-020-02168-z) | Defines minigraph’s reference-anchored incremental graph model. |
| A draft human pangenome reference | 2023 | Nature | [Liao et al., DOI: 10.1038/s41586-023-05896-x](https://doi.org/10.1038/s41586-023-05896-x) | HPRC Release 1; primary measured GRCh38 comparison. |
| Pangenome graph construction from genome alignments with Minigraph-Cactus | 2024 | Nature Biotechnology | [Hickey et al., DOI: 10.1038/s41587-023-01793-w](https://doi.org/10.1038/s41587-023-01793-w) | Defines the MC construction and deliverables. |
| Building pangenome graphs | 2024 | Nature Methods | [Garrison et al., DOI: 10.1038/s41592-024-02430-3](https://doi.org/10.1038/s41592-024-02430-3) | Primary PGGB paper. |
| Comparing methods for constructing and representing human pangenome graphs | 2023 | Genome Biology | [Andreace et al., DOI: 10.1186/s13059-023-03098-2](https://doi.org/10.1186/s13059-023-03098-2) | Empirical comparison of graph structures and retained variation. |
| HPRC2: A human pangenome reference with near-complete coverage of common genetic variation | 2026 | bioRxiv preprint | [HPRC Consortium et al.](https://www.biorxiv.org/content/10.64898/2026.07.21.739710v1.full) | Current second-release claims; not peer reviewed. |
| The complete sequence of a human genome | 2022 | Science | [Nurk et al., DOI: 10.1126/science.abj6987](https://doi.org/10.1126/science.abj6987) | Primary T2T-CHM13 reference and GRCh38 comparison. |
| Segmental duplications and their variation in a complete human genome | 2022 | Science | [Vollger et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC8979283/) | Establishes the SD sequence newly resolved by T2T. |
| Pangenomics enables genotyping known structural variants in 5,202 diverse genomes | 2022 | Science | [Hickey et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9365333/) | Giraffe SV genotyping at population scale. |
| Detection of mosaic and population-level structural variants with Sniffles2 | 2024 | Nature Biotechnology | [Smolka et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11217151/) | Modern long-read SV caller and benchmark framing. |
| Truvari: refined structural variant comparison preserves allelic diversity | 2022 | Genome Biology | [English et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9793516/) | Sequence-aware SV comparison/merging and limitations. |
| Haplotype-aware pantranscriptome analyses using spliced pangenome graphs | 2023 | Nature Methods | [Sibbesen et al., DOI: 10.1038/s41592-022-01731-9](https://doi.org/10.1038/s41592-022-01731-9) | Primary pantranscriptome/ASE quantification paper. |

## What the standard corpus misses

- HPRC Data Release 2 and the **2026 HPRC2 preprint**: 460 haplotypes, formal pangenome coordinate systems, pantranscriptome/panepigenome, and new error-rate claims. [Official release information](https://humanpangenome.org/) [HPRC2 preprint](https://www.biorxiv.org/content/10.64898/2026.07.21.739710v1.full)

- `pangenome-aware DeepVariant`, which uses a pangenome to improve calls while retaining linear read mappings—a pragmatic bridge for existing pipelines. [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157594/)

- Formal non-linear variant cataloguing: reference-tree coordinates exposed millions of variants invisible to a GRCh38-only definition. [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12340789/)

- Recent PAV work showing that mixed annotation pipelines can recover annotation provenance rather than biological gene-content variation. [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12856356/)

- Tools beyond the familiar trio: `pangene` for graph gene-content representation and `impg` for alignment-network/implicit graph queries. [pangene](https://github.com/lh3/pangene) [impg](https://github.com/pangenome/impg)

## Caveats and open questions

- “Release 2” is nomenclaturally confusing: the official HPRC page dates Data Release 2 to May 2025, whereas the 460-haplotype scientific description is a July 2026 preprint. I could verify both, but not a peer-reviewed HPRC2 paper or a single immutable graph release identifier that reconciles them. [HPRC](https://humanpangenome.org/) [HPRC2](https://www.biorxiv.org/content/10.64898/2026.07.21.739710v1.full)

- Minigraph-Cactus and PGGB are not contradictory so much as optimized for different representations: MC provides hierarchical Cactus alignment and graph products convenient for HPRC-style analysis; PGGB more directly preserves all-vs-all base-level relationships. Their “SV agreement” depends on the comparison definition, while small-variant content and local topology differ. [Comparison study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10691155/)

- There is no universal “best” long-read SV caller. Published benchmarks disagree as technology, depth, aligner, truth set, complex-SV representation, and difficult-region mask change. Evaluate on relevant GIAB/CMRG-style strata and manually inspect high-consequence calls. [Benchmark](https://doi.org/10.1038/s41467-024-46614-z)

- Claims that graph references improve *general* expression quantification are less mature than DNA-calling evidence. The strongest primary evidence is for haplotype/allele-specific quantification; broad transcriptome-wide effect sizes remain sparse and dataset-specific. [Sibbesen et al.](https://doi.org/10.1038/s41592-022-01731-9)

- A graph reduces reference bias only for variation represented by its input paths. Under-sampled clades, collapsed duplications, inaccurate assemblies, and arbitrary graph simplification can transfer rather than eliminate bias. [Pangenome graph evaluation](https://pmc.ncbi.nlm.nih.gov/articles/PMC10691155/)