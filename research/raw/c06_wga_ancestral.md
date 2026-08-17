## Answer

For a clade-scale analysis, first curate haplotype-resolved, contamination-screened assemblies and a defensible species tree; then use a non-collinear multiple WGA when sequence-level homology across divergent genomes is required. Progressive Cactus is the general reference-free choice for hundreds of vertebrate-scale genomes; it reconstructs internal-node assemblies and emits a HAL alignment. Minigraph-Cactus is designed chiefly for many closely related assemblies/pangenomes. AnchorWave is particularly useful where conserved coding anchors survive extensive structural polymorphism or whole-genome duplication; GSAlign is pairwise and explicitly intra-species; SibeliaZ is a fast multiple-WGA/locally-collinear-block method for closely related genomes. There is no credible universal divergence cutoff: repeat content, duplications, assembly continuity, and rearrangement rate matter at least as much as ANI. [Progressive Cactus](https://pmc.ncbi.nlm.nih.gov/articles/PMC7673649/) [Cactus documentation](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/progressive.md) [AnchorWave](https://pubmed.ncbi.nlm.nih.gov/34934012/) [GSAlign](https://pmc.ncbi.nlm.nih.gov/articles/PMC7041101/) [SibeliaZ](https://doi.org/10.1038/s41467-020-19777-8)

Pairwise-to-one-reference alignments make non-reference-specific sequence, duplications, and rearranged loci difficult or impossible to represent; a reference-free MSA instead represents homology among all genomes and permits multiple orthology. HAL stores the phylogenetically hierarchical alignment, including ancestral nodes; Cactus/HAL tooling exports MAF, chains, FASTA, conservation tracks and supports liftover/comparative annotation. [Progressive Cactus](https://pmc.ncbi.nlm.nih.gov/articles/PMC7673649/) [HAL](https://academic.oup.com/bioinformatics/article/29/10/1341/256598) [Cactus HAL documentation](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/progressive.md)

Similarity alone cannot establish loss: a failed BLAST/orthology hit also follows from gene-model failure, assembly gap/collapse, high divergence, pseudogenization, or paralogue reassignment. The evidential test is whether *both flanking syntelogs* map in conserved order/orientation to a single orthologous interval, whether that interval lacks an intact gene despite direct DNA/protein/transcript search, and whether read/assembly evidence excludes a gap. Thus collinearity locates the expected locus independently of the missing gene and distinguishes loss from “not detected.” [MCScanX](https://pubmed.ncbi.nlm.nih.gov/22217600/) [GENESPACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9462846/) [SynGAP](https://pmc.ncbi.nlm.nih.gov/articles/PMC11323386/)

Ancestral reconstruction is now useful, but not literal time-travel. Cactus infers ancestral *sequence assemblies* conditional on its guide tree/alignment; DESCHRAMBLER infers ordered/oriented syntenic fragments, reference-assisted; AGORA and the 2025 EdgeHOG infer ancestral gene content/order from gene histories and adjacencies. They legitimately support comparative coordinates, rearrangement mapping, hypotheses about ancestral karyotype and conserved neighborhoods—not confident base-perfect ancient genomes or unqualified claims about absent/rearranged repetitive DNA. [Cactus](https://pmc.ncbi.nlm.nih.gov/articles/PMC7673649/) [DESCHRAMBLER](https://pmc.ncbi.nlm.nih.gov/articles/PMC5502614/) [AGORA](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998269/) [EdgeHOG](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507687/)

## Key findings

- Progressive Cactus is a reference-free, duplication-tolerant progressive MSA requiring a guide tree; its published implementation scaled the approach to hundreds/thousands of large genomes, while current documentation specifically recommends Minigraph-Cactus for samples from the same species. [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7673649/) [official documentation](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/progressive.md)

- Minigraph-Cactus combines minigraph’s graph construction with Cactus base-level alignment and was demonstrated on 90 human haplotypes; use it primarily for population/species-complex pangenomes, not as a substitute for deeply divergent clade alignment without sensitivity evaluation. [Hickey et al.](https://www.nature.com/articles/s41587-023-01793-w)

- AnchorWave uses lifted-over full-length CDS anchors and explicitly targets high sequence diversity, SVs, and WGD; this makes it unusually relevant to plant clades, but it also means its sensitivity depends on coding-gene annotation and retained anchor homology. [Song et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC8740769/)

- GSAlign is a fast *pairwise* intra-species whole-genome aligner/variant caller; it is not a clade-wide MSA method. [Lin & Hsu](https://pmc.ncbi.nlm.nih.gov/articles/PMC7041101/)

- SibeliaZ detects locally collinear blocks through a compacted de Bruijn graph and globally aligns those blocks; it is a practical fast option for closely related, largely collinear genomes, especially microbial-style analyses. [Minkin & Medvedev](https://doi.org/10.1038/s41467-020-19777-8)

- HAL represents a phylogenetically hierarchical WGA as parent–child breakpoint-graph relationships; current Cactus tools provide `cactus-hal2maf`, chain export, FASTA extraction, conservation scoring/PhyloP, liftover, and comparative annotation workflows. [HAL paper](https://academic.oup.com/bioinformatics/article/29/10/1341/256598) [HAL repository](https://github.com/ComparativeGenomicsToolkit/hal) [Cactus documentation](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/progressive.md)

- For a claimed loss, require convergent evidence: conserved flanks, absence from the orthologous DNA interval, search against unannotated sequence, assembly/read support, and sampling of close relatives/outgroups to polarize the event. MCScanX supplies anchor-based collinearity; GENESPACE constrains orthology with synteny and explicitly models copy-number/tandem-array context; SynGAP can repair annotation using syntenic evidence. [MCScanX](https://pubmed.ncbi.nlm.nih.gov/22217600/) [GENESPACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9462846/) [SynGAP](https://pmc.ncbi.nlm.nih.gov/articles/PMC11323386/)

- Pairwise WGA plus SyRI identifies syntenic regions first, then classifies inversions, translocations, duplications and local sequence differences; clade-scale inference should map each event onto a species tree and validate key breakpoints with independent assemblies, long reads, optical maps/Hi-C, or cytogenetics. [SyRI](https://pmc.ncbi.nlm.nih.gov/articles/PMC6913012/) [DESCHRAMBLER](https://pmc.ncbi.nlm.nih.gov/articles/PMC5502614/)

- Scaffold joins can mimic inversions, relocations, or translocations; Hi-C itself has orientation limitations at short distances, and reference-guided scaffolding can impose the reference arrangement. [GAGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3290791/) [scaffolding review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6550390/)

- **Changed in the last 18 months:** Cactus releases through v3.2.1 (20 May 2026) added/changed graph-mapping, HAL compression, conservation and pangenome-pipeline behavior; record the exact container/version and configuration in any analysis. [release notes](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/ReleaseNotes.md)

- **Changed in the last 18 months:** EdgeHOG (2025) introduced linear-time HOG-based ancestral gene-order inference and applied it to 2,845 genomes/1,133 ancestors. SynGAP (2024) is a synteny-based annotation-polishing tool, not an aligner. [EdgeHOG](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507687/) [SynGAP](https://pmc.ncbi.nlm.nih.gov/articles/PMC11323386/)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| *Progressive Cactus is a multiple-genome aligner for the thousand-genome era* — Armstrong et al.; DOI: 10.1038/s41587-020-0646-5 | 2020 | Nature Biotechnology | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7673649/) | Canonical clade-scale reference-free WGA and Cactus ancestral-sequence method. |
| *Pangenome graph construction from genome alignments with Minigraph-Cactus* — Hickey et al.; DOI: 10.1038/s41587-023-01793-w | 2024 | Nature Biotechnology | [paper](https://www.nature.com/articles/s41587-023-01793-w) | Canonical minigraph-Cactus method and population-scale demonstration. |
| *HAL: a hierarchical format for storing and analyzing multiple genome alignments* — Hickey et al.; DOI: 10.1093/bioinformatics/btt128 | 2013 | Bioinformatics | [paper](https://academic.oup.com/bioinformatics/article/29/10/1341/256598) | Format/data model underpinning Cactus downstream use. |
| *AnchorWave: Sensitive alignment of genomes with high sequence diversity, extensive structural polymorphism, and whole-genome duplication* — Song et al.; DOI: 10.1073/pnas.2113075119 | 2022 | PNAS | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8740769/) | Gene-anchor WGA for divergent/WGD-rich genomes. |
| *GSAlign: an efficient sequence alignment tool for intra-species genomes* — Lin & Hsu; DOI: 10.1186/s12864-020-6569-1 | 2020 | BMC Genomics | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7041101/) | Correct scope for this pairwise tool. |
| *Scalable multiple whole-genome alignment and locally collinear block construction with SibeliaZ* — Minkin & Medvedev; DOI: 10.1038/s41467-020-19777-8 | 2020 | Nature Communications | [paper](https://doi.org/10.1038/s41467-020-19777-8) | Multiple WGA based on local collinear blocks. |
| *MCScanX: a toolkit for detection and evolutionary analysis of gene synteny and collinearity* — Wang et al.; DOI: 10.1093/nar/gkr1293 | 2012 | Nucleic Acids Research | [paper](https://pubmed.ncbi.nlm.nih.gov/22217600/) | Canonical gene-anchor collinearity toolkit. |
| *GENESPACE tracks regions of interest and gene copy number variation across multiple genomes* — Lovell et al.; DOI: 10.7554/eLife.78526 | 2022 | eLife | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9462846/) | Multi-genome synteny/orthology framework for copy-number questions. |
| *SynGAP: a synteny-based toolkit for gene structure annotation polishing* — Wu et al.; DOI: 10.1186/s13059-024-03359-8 | 2024 | Genome Biology | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11323386/) | Directly addresses annotation artefacts behind false “losses.” |
| *SyRI: finding genomic rearrangements and local sequence differences from whole-genome assemblies* — Goel et al.; DOI: 10.1186/s13059-019-1911-0 | 2019 | Genome Biology | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6913012/) | Pairwise structural-rearrangement classification from WGA. |
| *Reconstruction and evolutionary history of eutherian chromosomes* — Kim et al.; DOI: 10.1073/pnas.1702012114 | 2017 | PNAS | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5502614/) | DESCHRAMBLER; ancestral syntenic-fragment/chromosome reconstruction. |
| *Reconstruction of hundreds of reference ancestral genomes across the eukaryotic kingdom* — Muffato et al.; DOI: 10.1038/s41559-022-01956-z | 2023 | Nature Ecology & Evolution | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998269/) | AGORA and its broad ancestor resource/benchmarks. |
| *ANGES: reconstructing ANcestral GEnomeS maps* — Jones et al.; DOI: 10.1093/bioinformatics/bts381 | 2012 | Bioinformatics | [paper](https://academic.oup.com/bioinformatics/article/28/18/2388/253938) | Canonical adjacency/ancestral-map approach. |
| *Breakpoint graphs and ancestral genome reconstructions* — Alekseyev & Pevzner; DOI: 10.1101/gr.082784.108 | 2009 | Genome Research | [paper](https://genome.cshlp.org/content/early/2009/02/12/gr.082784.108) | MGRA’s rearrangement/breakpoint-graph formulation. |
| *EdgeHOG: a method for fine-grained ancestral gene order inference at large scale* — Bernard et al.; DOI: 10.1038/s41559-025-02818-0 | 2025 | Nature Ecology & Evolution | [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507687/) | Current scalable ancestral-adjacency entrant. |

## What the standard corpus misses

- **Minigraph-Cactus (2024):** the practical bridge between pangenome graphs and base-level WGA; include it alongside, not instead of, Progressive Cactus. [Hickey et al.](https://www.nature.com/articles/s41587-023-01793-w)

- **SynGAP (2024):** makes explicit that comparative synteny can be used to repair gene structures, an essential alternative explanation for apparent loss. [Wu et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11323386/)

- **EdgeHOG (2025):** major scale expansion for ancestral *gene order*, using HOGs rather than reconciled gene trees; its Tree-of-Life-scale outputs should not be conflated with reconstructed nucleotide chromosomes. [Bernard et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507687/)

- **Cactus v3.1–3.2 (2025–26):** active software changes affect pangenome construction, outgroup behavior, ancestral-contig parameters and HAL output; historical papers do not specify these defaults. [release notes](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/ReleaseNotes.md)

- **wgatools (2024 preprint):** emerging high-throughput tooling for conversion, statistics and visualization across WGA formats; useful infrastructure, but its peer-reviewed status was not verified here. [preprint](https://arxiv.org/abs/2409.08569)

## Caveats and open questions

- “Best aligner by divergence” is genuinely contested because benchmarks do not transfer cleanly across repeat landscapes, ploidy/WGD, assembly quality, and desired output. I found no primary source that justifies a universal ANI or Myr threshold; treat tool selection as a benchmarkable design decision, not a lookup table. [unverified]

- AGORA reports very high agreement in simulations and contrasts favorably with DESCHRAMBLER in a duplication-inclusive simulation, but this is method-authored benchmarking; it is evidence of capability, not an external guarantee for a particular clade. [AGORA](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998269/)

- DESCHRAMBLER and AGORA make different representational choices—reference-dependent sequence blocks versus gene-order reconstruction—and can disagree on ancestral chromosome number/fragment structure; DESCHRAMBLER itself reports conflicts with FISH-based reconstructions for the simian ancestor. [DESCHRAMBLER](https://pmc.ncbi.nlm.nih.gov/articles/PMC5502614/)

- EdgeHOG’s large-scale claim concerns HOG-adjacency/order inference. It does not validate base-by-base ancestral sequence, centromeres, repeat architecture, or extinct haplotype diversity. [EdgeHOG](https://pmc.ncbi.nlm.nih.gov/articles/PMC12507687/)

- A clade-scale rearrangement paper should report assembly provenance, phasing/scaffolding method, alignment parameters, breakpoint uncertainty, independent support, and sensitivity to excluding low-quality taxa. Otherwise scaffolding error and reference-guided ordering can be misreported as evolution. [scaffolding review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6550390/)