## Answer

Interpret comparative-genomics results as conditional statements: *if* the sequences are homologous, the chosen alignment represents positional homology, and the evolutionary/search model is adequate, then the reported tree, orthology, selection, or conservation estimate follows. None of the software names supplies those premises. [Karlin & Altschul 1990](https://pubmed.ncbi.nlm.nih.gov/2315319/) [Felsenstein 1981](https://pubmed.ncbi.nlm.nih.gov/7288891/)

Pairwise alignment optimizes a score, not historical truth. Global alignment assumes the full lengths should correspond; local alignment seeks one high-scoring region. Affine gaps encode a preference for one indel event over many short ones; changing gap-open, gap-extension, or the substitution matrix can move indel boundaries and force different residues into columns—thereby changing what downstream programs call substitutions. [NCBI BLAST matrix guide](https://www.ncbi.nlm.nih.gov/blast/html/sub_matrix.html)

BLAST/DIAMOND E-values are expected numbers of chance local scores at least as good under a specified random-sequence model and effective search space; they are neither posterior probabilities of homology nor evidence of orthology/function. Composition, repeats, query length, database size, domains, and missing taxa matter. [Karlin & Altschul 1990](https://pubmed.ncbi.nlm.nih.gov/2315319/) [NCBI BLAST statistics tutorial](https://www.ncbi.nlm.nih.gov/BLAST/tutorial/)

The most publication-threatening violations are usually upstream: unrelated or paralogous sequences treated as comparable, over-aligned divergent regions, unrecognized frameshifts/annotation errors, and reporting a single filtered alignment/tree as if it were robust. Simulations show ordinary MSA error can generate false positive branch-site selection calls; gap stripping does not necessarily remove the erroneous nonhomologous codons. [Markova-Raina & Petrov 2011](https://academic.oup.com/mbe/article/27/10/2257/965427) Filtering is genuinely contested: aggressive block filtering often worsened single-gene trees by discarding signal, whereas targeted detection of sequence-error segments reduced false positive selection in another study. [Tan et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4538881/) [Di Franco et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6330419/)

Likelihood on trees is powerful but not an oracle: it sums unobserved ancestral states under a continuous-time Markov model. Selection chooses a comparatively better model from a candidate set; adequacy asks whether even that model can plausibly generate the observed data. The latter, plus sensitivity to alignment, model, taxon sampling, and paralog choice, licenses defensible claims. [ModelFinder](https://pmc.ncbi.nlm.nih.gov/articles/PMC5453245/) [model-adequacy study](https://link.springer.com/article/10.1186/s12859-019-2905-3)

## Key findings

- Needleman–Wunsch is a global dynamic-programming formulation; Smith–Waterman is local and resets poor-scoring extensions. Use global only when end-to-end correspondence is a meaningful hypothesis; use local for shared domains, fragments, fusions, and rearranged proteins. [Needleman & Wunsch 1970](https://doi.org/10.1016/0022-2836(70)90057-4) [Smith & Waterman 1981](https://doi.org/10.1016/0022-2836(81)90087-5)

- Affine cost `open + k×extend` makes long gaps cheaper than repeatedly opening gaps, reflecting clustered indel events; its values are coupled to the score matrix and are empirically calibrated, not universal biological constants. [NCBI BLAST matrix guide](https://www.ncbi.nlm.nih.gov/blast/html/sub_matrix.html)

- PAM matrices extrapolate replacements observed among close proteins; one PAM is an average accepted change at 1% of positions. BLOSUM matrices instead estimate log-odds scores from conserved ungapped blocks, clustering sequences above the matrix’s identity threshold. [NCBI BLAST statistics tutorial](https://www.ncbi.nlm.nih.gov/BLAST/tutorial/) [Henikoff & Henikoff 1992](https://pmc.ncbi.nlm.nih.gov/articles/PMC50453/)

- Practical matrix choice: higher-number BLOSUM matrices suit closer/shorter matches; lower-number BLOSUM matrices suit more distant matches. NCBI recommends BLOSUM62 as a general default, BLOSUM45 for long weak similarity, and PAM30/70 for short queries. These are detection heuristics, not estimates of divergence time. [NCBI guide](https://www.ncbi.nlm.nih.gov/blast/html/sub_matrix.html)

- Karlin–Altschul theory gives approximately \(E=Kmn e^{-\lambda S}\) for ungapped local scores, with extensions/calibration for gapped search; an E-value depends on score system and search space, so “significant” changes with database size. [Karlin & Altschul 1990](https://pubmed.ncbi.nlm.nih.gov/2315319/) [NCBI tutorial](https://www.ncbi.nlm.nih.gov/BLAST/tutorial/)

- Mask low-complexity/repetitive sequence and inspect compositional bias: NCBI protein BLAST uses conditional compositional score adjustment by default, while DIAMOND applies tantan repeat masking by default. [NCBI BLAST glossary](https://ncbi.nlm.nih.gov/books/NBK62051/) [DIAMOND documentation](https://github.com/bbuchfink/diamond/wiki/3.-Command-line-options)

- A top hit means “best database match under this query, database, and scoring/search procedure,” not “homolog,” much less “ortholog.” Domain sharing, uneven database representation, fast evolution, gene loss, fusion/fission, and paralogy invalidate that leap. [BLAST original paper](https://doi.org/10.1016/S0022-2836(05)80360-2) [HMMER guide](https://eddylab.org/software/hmmer/CURRENT/Userguide.pdf)

- Sensitive search is tiered: DIAMOND `--ultra-sensitive` is appropriate for scalable protein sequence search below the twilight zone; MMseqs2 offers adjustable sensitivity and iterative sequence–profile searches; HMMER/profile methods are preferred for known remote domain families; structure search is valuable when a credible experimental/predicted structure exists. [DIAMOND documentation](https://github.com/bbuchfink/diamond/wiki/3.-Command-line-options) [MMseqs2 documentation](https://github.com/soedinglab/mmseqs2) [HMMER guide](https://eddylab.org/software/hmmer/CURRENT/Userguide.pdf) [Foldseek](https://doi.org/10.1038/s41587-023-01773-0)

- **Changed within the last 18 months:** DIAMOND’s current repository lists v2.2.1 (25 May 2026), and current documentation still distinguishes `--ultra-sensitive` from `--very-sensitive`; MMseqs2’s 2026 release adds CLI changes and warns that precomputed indices above sensitivity 6 need a workaround. Treat exact command defaults as versioned methods metadata. [DIAMOND release status](https://github.com/bbuchfink/diamond) [MMseqs2 releases](https://github.com/soedinglab/MMseqs2/releases)

- MSA disagreement is substantial in difficult regions, not a marginal nuisance: one empirical/simulated assessment found only 34–52% correctly aligned columns on difficult empirical cases across PRANK, MAFFT, ClustalW, and T-Coffee. No aligner wins under every simulation, data type, indel process, or downstream task. [GUIDANCE2 benchmark](https://pmc.ncbi.nlm.nih.gov/articles/PMC4489236/) [ancestral-reconstruction benchmark](https://pmc.ncbi.nlm.nih.gov/articles/PMC5995191/)

- In selection simulations, codon-aware PRANK was more accurate than PRANK amino-acid, MAFFT, MUSCLE, and ClustalW; ordinary aligners could place nonhomologous codons together, creating false branch-site positives even after gap-column removal. [Markova-Raina & Petrov 2011](https://academic.oup.com/mbe/article/27/10/2257/965427)

- Codon-aware alignment is mandatory when the question is dN/dS: protein-guided back-translation preserves reading-frame/codon columns; MACSE additionally models frameshifts and stop codons, whereas PAL2NAL-style workflows cannot automatically handle unexpected frameshifts. [MACSE](https://doi.org/10.1371/journal.pone.0022594)

- Filtering evidence conflicts. Gblocks-style removal improved some simulated protein-tree analyses, but a later broad study found Gblocks, trimAl, BMGE, and ZORRO generally worsened single-gene phylogeny as more columns were removed; targeted HmmCleaner/PREQUAL-like segment filtering can help specifically with primary-sequence errors. [Talavera & Castresana 2007](https://academic.oup.com/sysbio/article/56/4/564/1654176) [Tan et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4538881/) [Di Franco et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6330419/)

- A tree substitution model is a continuous-time Markov process: JC69 assumes equal base frequencies and equal rates; GTR allows unequal frequencies and reversible exchangeabilities; `+G` models site-rate heterogeneity, while `+I` adds invariant sites. Amino-acid and codon models change the state space and biological constraints. [Felsenstein 1981](https://pubmed.ncbi.nlm.nih.gov/7288891/) [ModelFinder](https://pmc.ncbi.nlm.nih.gov/articles/PMC5453245/)

- Felsenstein pruning computes site likelihood efficiently by recursively summing over unobserved states at internal nodes; likelihood compares \(P(\mathrm{alignment}\mid\mathrm{tree,model})\), not the probability that the inferred tree is true. [Felsenstein 1981](https://pubmed.ncbi.nlm.nih.gov/7288891/)

- ModelFinder/jModelTest-style selection compares candidate models using criteria such as AIC/BIC. In many empirical/simulation settings the selection criterion has little topological effect, while branch lengths, support, and hard regions can be more sensitive; under misspecification in difficult parameter regions, topology can change. [ModelFinder](https://pmc.ncbi.nlm.nih.gov/articles/PMC5453245/) [model-selection assessment](https://pmc.ncbi.nlm.nih.gov/articles/PMC6389923/) [model adequacy paper](https://link.springer.com/article/10.1186/s12859-019-2905-3)

- Profile HMMs retain position-specific residue and indel distributions from an MSA, so they commonly detect remote family/domain relationships missed by pairwise similarity. Their failure mode is different: a profile can be biased by its seed alignment, represent only a domain rather than a full-gene history, and yield false functional transfer from a weak/partial domain match. [HMMER guide](https://eddylab.org/software/hmmer/CURRENT/Userguide.pdf) [InterPro documentation](https://interpro-documentation.readthedocs.io/_/downloads/en/latest/pdf/)

- Structure and protein-language-model retrieval are promising remote-homology complements, not replacements for evolutionary inference: Foldseek reports fast sensitive structure comparisons but notes discrimination of true and false positives can be challenging; PLMSearch was published in 2024 and needs independent, task-specific calibration before it becomes a default annotation authority. [Foldseek paper](https://doi.org/10.1038/s41587-023-01773-0) [PLMSearch](https://doi.org/10.1038/s41467-024-46808-5)

## Primary sources

| title | year | venue | URL | why it matters |
|---|---:|---|---|---|
| Global similarity and biological comparisons | 1970 | Journal of Molecular Biology | [DOI](https://doi.org/10.1016/0022-2836(70)90057-4) | Global alignment |
| Identification of common molecular subsequences | 1981 | Journal of Molecular Biology | [DOI](https://doi.org/10.1016/0022-2836(81)90087-5) | Local alignment |
| An improved algorithm for matching biological sequences | 1982 | Journal of Molecular Biology | [DOI](https://doi.org/10.1016/0022-2836(82)90398-9) | Affine-gap dynamic programming |
| Amino acid substitution matrices from protein blocks | 1992 | PNAS | [DOI](https://doi.org/10.1073/pnas.89.22.10915) | BLOSUM construction |
| Methods for assessing the statistical significance of molecular sequence features by using general scoring schemes | 1990 | PNAS | [DOI](https://doi.org/10.1073/pnas.87.6.2264) | Karlin–Altschul statistics |
| Basic local alignment search tool | 1990 | Journal of Molecular Biology | [DOI](https://doi.org/10.1016/S0022-2836(05)80360-2) | BLAST method |
| Gapped BLAST and PSI-BLAST: a new generation of protein database search programs | 1997 | Nucleic Acids Research | [DOI](https://doi.org/10.1093/nar/25.17.3389) | Gapped and profile-iterative search |
| Effect of insertions, deletions, and alignment errors on the branch-site test of positive selection | 2011 | Molecular Biology and Evolution | [DOI](https://doi.org/10.1093/molbev/msq115) | Direct dN/dS failure mode |
| Current methods for automated filtering of multiple sequence alignments frequently worsen single-gene phylogenetic inference | 2015 | Systematic Biology | [URL](https://pmc.ncbi.nlm.nih.gov/articles/PMC4538881/) | Filtering counter-evidence |
| Evaluating the usefulness of alignment filtering methods to reduce the impact of errors on evolutionary inferences | 2019 | BMC Evolutionary Biology | [DOI](https://doi.org/10.1186/s12862-019-1350-2) | Targeted-filtering evidence |
| Evolutionary trees from DNA sequences: a maximum likelihood approach | 1981 | Journal of Molecular Evolution | [DOI](https://doi.org/10.1007/BF01734359) | Likelihood and pruning foundation |
| ModelFinder: fast model selection for accurate phylogenetic estimates | 2017 | Nature Methods | [DOI](https://doi.org/10.1038/nmeth.4285) | Current practical model selection |
| MACSE: Multiple Alignment of Coding SEquences Accounting for Frameshifts and Stop Codons | 2011 | PLOS ONE | [DOI](https://doi.org/10.1371/journal.pone.0022594) | Codon-aware alignment |
| Sensitive protein alignments at tree-of-life scale using DIAMOND | 2021 | Nature Methods | [DOI](https://doi.org/10.1038/s41592-021-01101-x) | Modern scalable sequence search |
| Fast and accurate protein structure search with Foldseek | 2023 | Nature Biotechnology | [DOI](https://doi.org/10.1038/s41587-023-01773-0) | Structure-based homology search |
| PLMSearch: Protein language model powers accurate and fast sequence search for remote homology | 2024 | Nature Communications | [DOI](https://doi.org/10.1038/s41467-024-46808-5) | PLM-based search |

## What my chapter plan is MISSING

1. **Homology is a historical claim; alignability, similarity, domain membership, orthology, and function are different claims.** Put this before BLAST, or readers will silently convert an E-value into evolutionary and functional annotation. [BLAST](https://doi.org/10.1016/S0022-2836(05)80360-2) [HMMER guide](https://eddylab.org/software/hmmer/CURRENT/Userguide.pdf)

2. **Uncertainty propagation as an explicit workflow.** Require a sensitivity set—alternative aligners/settings, masking/filtering choices, models, and homolog sets—and teach readers to report claims stable across it. Alignment uncertainty is empirically large in difficult cases. [GUIDANCE2](https://pmc.ncbi.nlm.nih.gov/articles/PMC4489236/)

3. **An “is this sequence even usable?” gate.** Cover ORF integrity, contamination, assembly/annotation artifacts, pseudogenes, chimeras, and domain architecture before any alignment. Primary-sequence errors can dominate some phylogenetic/selection analyses. [HmmCleaner evaluation](https://pmc.ncbi.nlm.nih.gov/articles/PMC6330419/) [MACSE](https://doi.org/10.1371/journal.pone.0022594)

4. **Indels, saturation, and nonhomogeneous processes.** `+G` is not a general cure for lineage-specific composition, heterotachy, recombination, or saturation; this bridge is essential before species trees and dN/dS. [model-adequacy study](https://link.springer.com/article/10.1186/s12859-019-2905-3)

5. **Model adequacy and posterior-predictive/parametric-bootstrap thinking.** Move adequacy immediately after model selection, not as a footnote: a selected model can still be inadequate. [model-adequacy study](https://link.springer.com/article/10.1186/s12859-019-2905-3)

6. **Minor reorder:** introduce profile methods immediately after “top hit ≠ homolog,” before the MSA section. They are the natural answer to what to do when pairwise search has insufficient reach; then show that profiles inherit MSA/seed-family error. [HMMER guide](https://eddylab.org/software/hmmer/CURRENT/Userguide.pdf)

7. **De-emphasize algorithm mechanics.** A research reader needs one worked score/path example and the assumptions/consequences, not recurrence derivations or exhaustive MSA-tool histories. The important distinction is downstream robustness, not memorizing implementations. [Markova-Raina & Petrov 2011](https://academic.oup.com/mbe/article/27/10/2257/965427)

## Caveats and open questions

- There is no defensible universal ranking of MAFFT, MUSCLE, PRANK, and Clustal: rankings reverse with divergence, indels, guide tree, sequence type, and target inference. [ancestral-reconstruction benchmark](https://pmc.ncbi.nlm.nih.gov/articles/PMC5995191/) [phylogenetic alignment assessment](https://pmc.ncbi.nlm.nih.gov/articles/PMC2884540/)

- Filtering is the central genuine disagreement. Early/some targeted studies find benefit; the strongest contrary evidence says automated column removal often loses more true phylogenetic signal than it removes error. Teach filtering as a hypothesis requiring diagnostics and sensitivity analysis, never as mandatory cleanup. [Talavera & Castresana 2007](https://academic.oup.com/sysbio/article/56/4/564/1654176) [Tan et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4538881/) [Di Franco et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6330419/)

- “Model choice usually does not change topology” is an average empirical claim, not permission to ignore misspecification: difficult trees and systematic compositional/rate violations are precisely where topology can be wrong with high support. [model-selection assessment](https://pmc.ncbi.nlm.nih.gov/articles/PMC6389923/) [model-adequacy study](https://link.springer.com/article/10.1186/s12859-019-2905-3)

- Evidence for PLM/structure search is rapidly moving, but independent calibration for genome-wide evolutionary annotation, especially specificity and orthology assignment, remains thinner than the mature BLAST/HMMER literature. [PLMSearch](https://doi.org/10.1038/s41467-024-46808-5) [Foldseek](https://doi.org/10.1038/s41587-023-01773-0)