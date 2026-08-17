## Answer

Comparative genomics is moving from a single linear reference plus small orthology sets toward three complementary, not interchangeable, evidence layers: dense phylogenetically explicit whole-genome alignments; population/species pangenome graphs that retain structural and presence–absence variation; and learned sequence/structure representations that prioritize hypotheses. Alignment-derived inference remains the only one of these that directly estimates evolutionary rate on a specified tree and null model. It is therefore not being displaced by DNA language models. [Zoonomia](https://doi.org/10.1126/science.abn3943) and the [239-primate alignment](https://doi.org/10.1038/s41586-023-06798-8) make lineage-aware constraint, acceleration, and regulatory-variant interpretation routine at mammal/primate scale.

ML’s demonstrated role is strongest in predicting molecular consequences from sequence—regulatory tracks, splicing, expression coverage, and some variant-ranking tasks—especially where an assay-trained model can score arbitrary alleles. Borzoi improves fine-mapped eQTL discrimination over Enformer, and AlphaGenome reports broad variant-effect benchmark gains; Evo 2 and Nucleotide Transformer show useful zero/few-shot representations and variant prioritization. [Borzoi](https://doi.org/10.1038/s41588-024-02053-6), [AlphaGenome](https://doi.org/10.1038/s41586-025-10014-0), [Evo 2](https://doi.org/10.1038/s41586-026-10176-5), [NT](https://doi.org/10.1038/s41592-024-02523-z) Yet these models do not supply an evolutionary substitution model, calibrated branch-specific selection test, orthology proof, or causal validation; independent benchmarking finds broad performance heterogeneity and specialized models outperform general frozen embeddings on regulatory QTL tasks. [Benchmark](https://doi.org/10.1038/s41467-025-65823-8)

The practical frontier is integration: use graphs to avoid reference bias and represent SV/CNV/gene-content variation; use alignment/phylogeny to test evolutionary claims; use ML and AlphaFold/Foldseek to triage candidate variants, functions, and remote homologs; then validate experimentally. Graph-native association and selection inference remain immature because graph deconstruction commonly returns multiallelic, linear-reference-oriented records incompatible with much classical population-genetic software. [Loegler, Friedrich & Schacherer](https://doi.org/10.1016/j.xgen.2025.101067)

## Key findings

- Zoonomia released a reference-free 240-placental-mammal Cactus alignment, 131 new assemblies, TOGA orthology annotations, codon alignments, and PHAST conservation tracks; its stated 5% FDR phyloP call identifies 3.1% of human bases as constrained. [Zoonomia data portal](https://zoonomiaproject.org/the-data/) [Christmas *et al.*](https://doi.org/10.1126/science.abn3943)

- At this scale, phyloP is used for basewise rate deviation/constraint and variant/regulatory prioritization; phastCons supplies element-like conserved calls, but the published primate-wide phastCons analysis is 43 primates while phyloP uses all 239 primates. Do not describe these as identical tests or interchangeable thresholds. [Kuderna *et al.*](https://doi.org/10.1038/s41586-023-06798-8)

- The central limit of “constraint” is observability: power depends on branch length, taxon sampling, alignment coverage and neutral-model choice; Zoonomia explicitly reports sitewise species coverage ranging from one to 240 and increased detected constraint where close relatives are available. [Christmas *et al.* PDF](https://pgl.soe.ucsc.edu/christmas23.pdf)

- Constraint is not synonymous with function, nor does nonconstraint establish neutrality: rapidly evolving, turnover-prone, lineage-specific, repetitive, or unalignable functional sequence is systematically disadvantaged by the test. This is an inference from the documented alignment/power limits, not a Zoonomia result. [Christmas *et al.*](https://doi.org/10.1126/science.abn3943)

- Nucleotide Transformer (NT-v2), trained on 3,202 human and 850 diverse-species genomes, supports low-data fine-tuning and variant prioritization; DNABERT-2 is a 135-species BPE model. [NT](https://doi.org/10.1038/s41592-024-02523-z) [DNABERT-2](https://proceedings.iclr.cc/paper_files/paper/2024/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf)

- Independent benchmarking found frozen DNA-model embeddings useful for many sequence classifications, but general models underperformed a task-trained CNN in several multispecies/epigenetic tasks; Enformer achieved eQTL AUC 0.77 versus 0.65 for the best general model in that comparison, and NT-v2 attention showed no zero-shot TAD-boundary signal. [Wang *et al.*](https://doi.org/10.1038/s41467-025-65823-8)

- Enformer predicts human/mouse chromatin and expression from sequence; Borzoi extends this to RNA-seq coverage across >500 kb and reported mean eQTL AUROC 0.794 versus Enformer’s 0.747 across GTEx tissues, while being only marginally better than TSS distance when identifying the target gene around an eQTL. [Enformer](https://doi.org/10.1038/s41592-021-01252-x) [Borzoi](https://doi.org/10.1038/s41588-024-02053-6)

- AlphaGenome, formally published **28 January 2026**, accepts up to 1-Mb sequence and predicts expression, splicing, chromatin and contact-map outputs; its public API is explicitly intended for small-to-medium analyses rather than >1 million predictions. [AlphaGenome paper](https://doi.org/10.1038/s41586-025-10014-0) [official API](https://github.com/google-deepmind/alphagenome)

- Evo 2, formally published **4 March 2026**, is a 7B/40B open model trained on ~9 trillion bases with a 1-million-token context. Its paper demonstrates variant scoring and model-guided generation, but those are not comparative evolutionary inference or replacement for a multi-species alignment. [Brixi *et al.*](https://doi.org/10.1038/s41586-026-10176-5)

- No visited primary source demonstrates that Evo/Evo 2, NT, DNABERT-2, Enformer, Borzoi, or AlphaGenome has replaced phyloP/phastCons for genome-wide, phylogeny-calibrated constraint or branch-specific selection inference; claims that they have should be treated as unsupported. [DNA-model benchmark](https://doi.org/10.1038/s41467-025-65823-8)

- AlphaFold DB plus Foldseek made proteome-scale structural similarity search operational: Foldseek encodes local tertiary interactions as a 3Di alphabet and was benchmarked for remote-homology sensitivity on SCOPe and full-length multidomain sets. This changes candidate discovery and domain/family annotation, not the definition of orthology. [Foldseek](https://doi.org/10.1038/s41586-023-06510-w) [AlphaFold DB documentation](https://alphafold.ebi.ac.uk/faq)

- Structure-derived homology calls require confidence filtering and reconciliation with gene trees, synteny and domain architecture: AlphaFold DB itself cautions that predictions do not place ligands, cofactors, ions, nucleic acids or PTMs and are not expected to model destabilizing-mutant unfolding. [AlphaFold DB limitations](https://alphafold.ebi.ac.uk/faq)

- Usable graph infrastructure now includes `vg` for graph mapping/genotyping/calling, Minigraph-Cactus for assembly-to-graph construction, `odgi` for graph manipulation/visualization, and `pangene` for gene-order/orientation/copy-number graphs. [vg](https://github.com/vgteam/vg) [Minigraph-Cactus](https://doi.org/10.1038/s41587-023-01793-w) [odgi](https://github.com/pangenome/odgi) [pangene](https://pubmed.ncbi.nlm.nih.gov/39041615/)

- What is still missing is genuinely graph-native population-genetic inference at routine scale: current workflows frequently deconstruct to VCF, produce difficult multiallelic records, and reintroduce a reference path; scaling, coordinate interoperability, annotation and visualization remain active bottlenecks. [Loegler *et al.*](https://doi.org/10.1016/j.xgen.2025.101067)

- Consortium data are already research-grade rather than aspirational: VGP reports 85% completion of its 271-species Phase I target; B10K’s ordinal phase is complete and its 363-genome release covers 92% of bird families; DToL provides an open production/data portal; EBP provides a live Phase-I dashboard. [VGP](https://vertebrategenomesproject.org/phase-one/) [B10K](https://b10k.genomics.cn/) [DToL](https://www.darwintreeoflife.org/data/) [EBP dashboard](https://earthbiogenome.github.io/dashboard/)

- HPRC’s **May 2025 Data Release 2** added progressively released sequencing data and assemblies; Release 1 retains three published graph constructions (Minigraph, Minigraph-Cactus, PGGB). The data explorer currently lists 466 assembly files, not necessarily 466 people. [HPRC data](https://www.humanpangenome.org/data/) [Data Explorer](https://data.humanpangenome.org/assemblies)

- Recent perspectives name durable-data usability, standardized annotation—especially transposable elements—uncertainty-aware inference, scalable graph algorithms, and connecting genomic change to phenotype as major unresolved issues. [Gavriilidou *et al.*](https://doi.org/10.1093/bioadv/vbaf223) [Loegler *et al.*](https://doi.org/10.1016/j.xgen.2025.101067)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Evolutionary constraint and innovation across hundreds of placental mammals — Christmas, Kaplow *et al.* | 2023 | *Science* | [DOI](https://doi.org/10.1126/science.abn3943) | Zoonomia 240-mammal alignment, phyloP constraint, alignment/power limits |
| Identification of constrained sequence elements across 239 primates — Kuderna *et al.* | 2023 | *Nature* | [DOI](https://doi.org/10.1038/s41586-023-06798-8) | Primate-scale phyloP/phastCons comparison |
| Nucleotide Transformer: building and evaluating robust foundation models for human genomics — Dalla-Torre *et al.* | 2025 | *Nature Methods* | [DOI](https://doi.org/10.1038/s41592-024-02523-z) | Multispecies DNA foundation-model resource |
| DNABERT-2: Efficient foundation model and benchmark for multi-species genome — Zhou *et al.* | 2024 | ICLR | [paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/b633e7052970b8f5aa1a69164d99e9e8-Paper-Conference.pdf) | Canonical DNABERT-2 model/benchmark |
| Benchmarking DNA foundation models for genomic and genetic tasks — Wang *et al.* | 2025 | *Nature Communications* | [DOI](https://doi.org/10.1038/s41467-025-65823-8) | Independent comparative evidence and negative results |
| Effective gene expression prediction from sequence by integrating long-range interactions — Avsec *et al.* | 2021 | *Nature Methods* | [DOI](https://doi.org/10.1038/s41592-021-01252-x) | Enformer baseline |
| Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation — Linder *et al.* | 2025 | *Nature Genetics* | [DOI](https://doi.org/10.1038/s41588-024-02053-6) | Borzoi’s evaluated gains and limits |
| Advancing regulatory variant effect prediction with AlphaGenome — Avsec, Latysheva *et al.* | 2026 | *Nature* | [DOI](https://doi.org/10.1038/s41586-025-10014-0) | 1-Mb multimodal sequence-to-function model |
| Genome modelling and design across all domains of life with Evo 2 — Brixi, Durrant, Ku *et al.* | 2026 | *Nature* | [DOI](https://doi.org/10.1038/s41586-026-10176-5) | Evo 2’s peer-reviewed claims and open release |
| Fast and accurate protein structure search with Foldseek — van Kempen *et al.* | 2023 | *Nature* | [DOI](https://doi.org/10.1038/s41586-023-06510-w) | Structural-search method and benchmarks |
| Pangenome graph construction from genome alignments with Minigraph-Cactus — Hickey *et al.* | 2023 | *Nature Biotechnology* | [DOI](https://doi.org/10.1038/s41587-023-01793-w) | Major graph-construction pipeline |
| Dynamics of genome evolution in the era of pangenome analysis — Loegler, Friedrich & Schacherer | 2026 | *Cell Genomics* | [DOI](https://doi.org/10.1016/j.xgen.2025.101067) | Current synthesis of graph/pangenome limitations |
| Advances and challenges in understanding evolution through genome comparison — Gavriilidou *et al.* | 2025 | *Bioinformatics Advances* | [DOI](https://doi.org/10.1093/bioadv/vbaf223) | 2024 meeting-derived field priorities |

## What the standard corpus misses

- The post-2024 peer-reviewed DNA-model evidence base: NT (published November 2024), Borzoi (2025), the broad benchmark (2025), AlphaGenome (January 2026), and Evo 2 (March 2026). [NT](https://doi.org/10.1038/s41592-024-02523-z) [benchmark](https://doi.org/10.1038/s41467-025-65823-8) [AlphaGenome](https://doi.org/10.1038/s41586-025-10014-0) [Evo 2](https://doi.org/10.1038/s41586-026-10176-5)

- The Zoonomia public HAL alignment, conservation tracks and TOGA annotations, plus the 239-primate constrained-element resource. [Zoonomia](https://zoonomiaproject.org/the-data/) [239 primates](https://doi.org/10.1038/s41586-023-06798-8)

- Graph-tool maturity since the original HPRC draft: Minigraph-Cactus, `vg`/GBZ workflows, `odgi`, `pangene`, and HPRC Release 2 data. [Cactus](https://github.com/ComparativeGenomicsToolkit/cactus) [vg](https://github.com/vgteam/vg) [odgi](https://github.com/pangenome/odgi) [HPRC](https://www.humanpangenome.org/data/)

- Structure search as a routine comparative screen at AlphaFold-DB scale, via Foldseek and AFDB structural clustering. [AFDB](https://alphafold.ebi.ac.uk/faq) [Foldseek](https://doi.org/10.1038/s41586-023-06510-w)

## Caveats and open questions

- “Constraint at scale” is not a single resource: Zoonomia’s 240-mammal phyloP result and the 239-primate study’s phyloP/phastCons analyses differ in tree depth, sampling, neutral models and thresholds. Cross-study score comparisons need recalibration. [Zoonomia](https://doi.org/10.1126/science.abn3943) [239 primates](https://doi.org/10.1038/s41586-023-06798-8)

- AlphaGenome and Evo 2 headline performance comes substantially from the authors’ evaluations. AlphaGenome now has a formal paper, but broad, independently replicated, assay-based comparative-genomics validation remains thin. [AlphaGenome](https://doi.org/10.1038/s41586-025-10014-0) [benchmark](https://doi.org/10.1038/s41467-025-65823-8)

- Credible sources disagree in emphasis: one recent review calls graph pangenomes a disruptive replacement for linear pipelines, whereas the 2026 *Cell Genomics* perspective documents continued reference-path dependence and incompatibility with classical analyses. The latter better describes present-day analytical practice. [Frontiers review](https://doi.org/10.3389/fgene.2025.1679660) [Loegler *et al.*](https://doi.org/10.1016/j.xgen.2025.101067)

- Exact EBP/DToL/VGP totals change continuously; I verified only the live dashboards/status pages above, not a frozen August 17, 2026 census. [unverified]