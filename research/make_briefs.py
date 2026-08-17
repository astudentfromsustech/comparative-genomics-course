#!/usr/bin/env python3
"""Emit one Codex research brief per chapter that needs live web research.

Chapters marked `brief: no` in PLAN.md are written from the corpus instead and
get no file here. Every brief carries the identical output contract so the
returned findings are directly comparable and every claim is URL-backed.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT  = ROOT/"research/briefs"
TODAY = "2026-08-17"

CONTRACT = """
OUTPUT FORMAT (markdown, no preamble):
## Answer
<direct answer to the question above, 250-450 words>
## Key findings
<bulleted; EVERY factual claim carries an inline source URL>
## Primary sources
<table: title | year | venue | URL | why it matters>
## What the standard corpus misses
<papers/tools a reader working from a 2015-2023 reading list would not know about>
## Caveats and open questions
<what you could not verify, and what is genuinely contested in the field>

RULES:
- Every non-obvious claim needs a URL you actually visited. No URL = mark it "[unverified]".
- Prefer primary sources (papers, official docs, source code, benchmark repos) over blog summaries.
- If the evidence is thin, SAY it is thin. Do not pad with plausible-sounding filler.
- Where credible sources disagree, report the disagreement rather than silently picking one.
- Name specific tools with versions and specific papers with DOIs wherever possible.
""".strip()

# slug, chapter, topic, question, prior-context, sub-questions
BRIEFS = [
("c02_data_comparability", "C2", "Assembly & annotation comparability",
 "What must be true of assemblies and annotations before a cross-species comparison is meaningful, "
 "and what does each defect manufacture downstream?",
 "C1 (what the field asks; homology vs similarity)",
 ["Current standards for assembly quality assessment beyond N50 -- BUSCO vs Merqury vs LAI vs "
  "compleasm; what each actually measures and where each is blind.",
  "How structural annotation pipelines (BRAKER3, Helixer, TSEBRA, EGAPx, AUGUSTUS-based) differ, and "
  "how much cross-species gene-count variation is annotation artefact rather than biology.",
  "Documented cases where an assembly or annotation defect produced a false biological conclusion "
  "(false gene family expansion, false gene loss, false HGT, false SV) -- give concrete examples.",
  "What changed with T2T/VGP-era assemblies and the 2023-2026 annotation tools; is 'annotate all "
  "genomes with one pipeline' now standard practice for comparative studies?",
  "Contamination screening (FCS-GX, Kraken-based) -- how much of the older comparative literature is "
  "affected by contamination that current screening would catch?"]),

("c03_orthology", "C3", "Orthology inference and its benchmarks",
 "What makes two genes the same evolutionary entity across species, why does best-BLAST-hit fail, "
 "and which orthology methods actually win on independent benchmarks?",
 "C2 (assemblies, annotation, QC)",
 ["The precise definitions and their boundaries: ortholog, paralog, in-paralog/co-ortholog, ohnolog, "
  "xenolog, homoeolog -- and what an 'orthogroup' is and is NOT.",
  "Quest for Orthologs (QfO) benchmark results and OrthoBench: which methods lead, on which metrics, "
  "and what the benchmarks are criticised for.",
  "State of the tools 2023-2026: OrthoFinder2/3, OMA, SonicParanoid2, Broccoli, Proteinortho, "
  "eggNOG-mapper, and any newer entrants. What are the real accuracy/scalability trade-offs?",
  "How isoform selection, fragmented genes, and unequal annotation quality bias orthogroup inference "
  "-- and what the recommended mitigations are.",
  "Whether protein-language-model or structure-based (Foldseek-era) approaches are changing remote "
  "homology detection and orthology assignment."]),

("c04_wga_ancestral", "C4", "Whole-genome alignment, synteny, and ancestral genome reconstruction",
 "How do you align whole genomes across a clade, why does collinearity rather than similarity "
 "adjudicate a claimed gene loss, and what is the current state of ancestral genome reconstruction?",
 "C3 (orthology)",
 ["Current whole-genome aligners for clade-scale work: Progressive Cactus, minigraph-cactus, "
  "AnchorWave, GSAlign, SibeliaZ, and 2024-2026 entrants. Which is appropriate at which divergence?",
  "Why pairwise-to-reference alignment introduces bias and what reference-free multiple WGA buys you; "
  "the HAL format and what tooling consumes it.",
  "ANCESTRAL GENOME RECONSTRUCTION -- this is a deliberate gap in our corpus, so treat it as the "
  "priority: what are the canonical methods and papers (Cactus ancestral sequences, DESCHRAMBLER, "
  "AGORA, ANGES, infer-ancestral-gene-order approaches)? How reliable are reconstructed ancestors, "
  "and what are they legitimately used for?",
  "Synteny/collinearity detection: MCScanX, JCVI/MCscan, GENESPACE, SynGAP and successors -- and how "
  "syntenic evidence is used to confirm or refute a gene-loss claim.",
  "How rearrangement inference (inversions, translocations, fusions) is done and validated at "
  "clade scale, and the error modes introduced by assembly scaffolding."]),

("c06_species_tree", "C6", "Species tree inference, discordance, and divergence dating",
 "How does a species tree become the coordinate system for every comparison, and what is the current "
 "state of the concatenation-vs-coalescent and molecular-clock-calibration disputes?",
 "C3 (orthology), C4 (synteny/alignment)",
 ["The multispecies coalescent: why gene tree discordance is expected, what ILS predicts, and why "
  "concatenation can be statistically inconsistent (the anomaly zone).",
  "Concatenation vs summary coalescent (ASTRAL) vs full-likelihood methods -- where does the field "
  "stand in 2024-2026? What do recent large phylogenomic papers actually do, and why?",
  "Gene- and site-concordance factors (gCF/sCF) versus bootstrap support: why high bootstrap on a "
  "wrong topology is routine, and what should be reported instead.",
  "Divergence-time estimation: MCMCtree, BEAST2, RelTime, and the fossil-calibration controversies. "
  "How sensitive are published divergence dates to prior and calibration choice? Cite specific "
  "documented disagreements.",
  "Ortholog/loci selection effects on the tree -- filtering by rate, saturation, missing data; and "
  "how much topology is driven by those choices."]),

("c07_comparative_methods", "C7", "Phylogenetic comparative methods for cross-species claims",
 "Why are N species not N independent data points, what corrects for that, and how is this "
 "machinery misused in comparative-genomics papers?",
 "C6 (species trees and discordance)",
 ["Phylogenetically independent contrasts, PGLS, and phylogenetic mixed models: what each corrects "
  "for and what each assumes.",
  "Model choice for trait evolution -- Brownian motion vs Ornstein-Uhlenbeck vs Early Burst; how "
  "often OU is fitted inappropriately and what the known statistical pitfalls are (e.g. OU model "
  "support with small trees).",
  "Methods that link genomic features to phenotypes across species: RERconverge, PhyloAcc, "
  "forward-genomics, PhyloG2P approaches. What are their assumptions and documented false-positive "
  "rates?",
  "Concrete critiques from the literature of comparative-genomics papers that correlated a genomic "
  "feature with a trait across species WITHOUT phylogenetic correction -- what went wrong.",
  "How many independent origins of a trait are needed for a defensible claim, and how the effective "
  "sample size of a comparative dataset should be reported."]),

("c08_structure_pangenome", "C8", "Structural variation, T2T genomes, and pangenome graphs",
 "What changes when the unit of comparison stops being a position on a linear reference and becomes "
 "a path through a clade?",
 "C2 (assembly QC), C4 (whole-genome alignment)",
 ["State of pangenome graph construction 2024-2026: minigraph, Minigraph-Cactus, PGGB, and newer. "
  "What each produces, and the documented differences in the variants they represent.",
  "The human pangenome reference (HPRC) -- what release we are at now, what the second release "
  "changed, and what it demonstrably fixed relative to GRCh38.",
  "Evidence on reference bias: quantified effects on variant calling, expression quantification, and "
  "comparative conclusions. Cite measurements, not assertions.",
  "SV calling and comparison across genomes: long-read callers, graph-based genotyping (vg, "
  "Giraffe, PanGenie), and how SV callsets are merged/compared (Jasmine, Truvari). Known "
  "reproducibility problems between callers.",
  "Presence/absence variation (PAV) in pangenomes: what evidence a PAV call needs before it counts "
  "as real absence rather than assembly or annotation failure.",
  "How T2T assemblies changed what is comparable -- centromeres, segmental duplications, "
  "previously-unassemblable regions -- and what comparative questions they newly permit."]),

("c09_selection", "C9", "Selection inference: what dN/dS licenses",
 "What does a dN/dS or branch-site result actually entitle you to say, and what generates false "
 "positives?",
 "C3 (orthology), C6 (species trees)",
 ["The model family: NG86 through GY94, site models (M1a/M2a, M7/M8), branch, branch-site, and the "
  "HyPhy family (aBSREL, BUSTED, MEME, RELAX). What hypothesis each actually tests.",
  "The four classic false-positive generators -- paralog contamination, misaligned codons, "
  "recombination, uncorrected multiple testing. Quantified evidence for each from the literature.",
  "Confounders that raise dN/dS WITHOUT positive selection: relaxed constraint, small effective "
  "population size, GC-biased gene conversion, nonstationary base composition. How are they "
  "controlled for in good practice?",
  "The critique literature on branch-site tests specifically -- known false-positive rates under "
  "alignment error and model misspecification; what the recommended pre-flight checks are.",
  "Alternatives and complements: MK-test variants and asymptotic MK, DFE-based inference, "
  "polymorphism-aware approaches, and machine-learning selection scans. Where is the field moving?",
  "Current best-practice checklists for reporting a positive-selection result -- what a referee "
  "should demand to see."]),

("c10_popgen_introgression", "C10", "Population history, demography, and introgression",
 "How do demography and gene flow masquerade as adaptation, and how is introgression distinguished "
 "from incomplete lineage sorting?",
 "C6 (species trees, the multispecies coalescent)",
 ["Demographic inference methods and their resolution limits: PSMC, MSMC2, SMC++, dadi, "
  "fastsimcoal2, Relate, tsinfer/tskit. What time ranges each can and cannot resolve.",
  "Introgression statistics: Patterson's D (ABBA-BABA), f4/f-branch, fd, D-statistics in windows, "
  "QuIBL, HyDe, Dsuite. What each assumes and how each fails -- particularly for old introgression "
  "and for ghost lineages.",
  "The specific statistical signature that separates ILS from introgression, and the conditions "
  "under which that signature breaks down.",
  "Why demography produces false selection signals: how background selection and population "
  "structure generate Fst/dN/dS outliers, and what null models are required.",
  "State of ancestral recombination graph (ARG) inference 2023-2026 -- ARG-Needle, SINGER, Relate, "
  "tsinfer -- and whether ARGs are displacing summary-statistic approaches.",
  "Genomic islands of differentiation: the current consensus on whether they indicate speciation "
  "with gene flow or reduced diversity/recurrent selection."]),

("c11_convergence", "C11", "Convergent evolution and adaptive explanation",
 "What does it take to claim convergent adaptation rather than coincidence?",
 "C7 (comparative methods), C9 (selection), C10 (population history)",
 ["The echolocating-mammals convergence episode (Parker et al. 2013) and its rebuttals -- what "
  "specifically was wrong, and what the episode established as required practice.",
  "Methods for detecting molecular convergence: convergent substitution counts, RERconverge, "
  "PhyloAcc, TRACCER, and how each handles the null expectation of convergence by chance.",
  "How to count INDEPENDENT origins of a trait on a phylogeny, and how phylogenetic "
  "non-independence inflates apparent convergence.",
  "The evidence ladder for an adaptive claim -- candidate, association, mechanistic support, causal. "
  "What functional validation is expected in a high-tier paper in 2024-2026.",
  "Documented cases where a convergence/adaptation claim was retracted or substantially walked "
  "back, and what the failure mode was in each."]),

("c12_regulatory", "C12", "Regulatory and non-coding comparative genomics",
 "Why does comparing proteins miss most phenotypic difference, and what makes a cross-species "
 "regulatory comparison interpretable?",
 "C4 (alignment), C7 (comparative methods)",
 ["The King & Wilson problem restated for 2026: what evidence now exists that regulatory rather "
  "than coding change drives phenotypic divergence, and how strong is it?",
  "Comparative epigenomics and enhancer evolution: turnover rates, the Villar 2015 result and what "
  "has revised it, and how conserved non-coding elements are defined and detected (phastCons, "
  "phyloP, GERP, and successors).",
  "Cross-species transcriptome comparison: cell-type homology, developmental-stage matching, and "
  "the confounders (batch, species, cell composition) that make expression differences "
  "uninterpretable. What normalisation/design is now considered adequate?",
  "Single-cell cross-species atlases -- what they have established about cell-type conservation, and "
  "the methodological disputes about cross-species cell-type mapping.",
  "Functional validation of a regulatory element across species: MPRA, enhancer reporter assays, "
  "CRISPR perturbation. What counts as evidence a sequence difference is causal?"]),

("c13a_frontier_ml", "C13", "The 2024-2026 frontier: ML, sequence constraint, and pangenome-native comparison",
 "Where is comparative genomics actually moving right now, and what do machine-learning approaches "
 "replace versus merely accelerate?",
 "the whole plan -- treat the reader as knowing the classical stack",
 ["Alignment-derived constraint at scale: Zoonomia/240-mammal results, phyloP/phastCons at that "
  "scale, and what constraint scores are now used for. What are the documented limits?",
  "Genomic language models (Evo/Evo2, Nucleotide Transformer, DNABERT-2, AlphaGenome, Borzoi, "
  "Enformer lineage): what tasks they demonstrably do well, what they demonstrably do NOT do, and "
  "whether any are displacing alignment-based comparative inference. Be skeptical and cite "
  "benchmark evidence.",
  "Protein structure comparison as a comparative-genomics tool -- AlphaFold DB, Foldseek, and "
  "structure-informed orthology/remote homology. What has this actually changed?",
  "Pangenome-native comparative genomics: doing selection, gene-family, and association analysis on "
  "a graph rather than a linear reference. What tooling exists and what is still missing?",
  "Large consortium efforts active now (Earth BioGenome, VGP, Zoonomia, Bird10K, Darwin Tree of "
  "Life, HPRC) -- current status and what data they have released that comparative studies can use.",
  "What do people working in the field currently name as the major UNSOLVED problems? Cite "
  "perspective/opinion pieces from 2024-2026."]),

("c13b_reporting_standards", "C13", "Evidence standards, reproducibility, and reviewing practice",
 "What is the minimum reportable record for each claim type in comparative genomics, and what should "
 "a referee demand?",
 "the whole plan",
 ["Published checklists, reporting standards, and best-practice guidelines specific to comparative "
  "and evolutionary genomics (journal policies, MIxS-style standards, community guidelines).",
  "Documented reproducibility failures in comparative genomics -- reanalyses that overturned a "
  "published conclusion. What was the recurring cause?",
  "How clade-specific practice diverges: what is standard in microbial (ANI/GTDB/pangenome), plant "
  "(polyploidy, TE load, WGD), and animal comparative genomics, and what does not transfer.",
  "Workflow reproducibility in practice: Nextflow/nf-core, Snakemake, containers, and whether "
  "comparative-genomics papers actually ship runnable pipelines. Any surveys measuring this?",
  "For each of these claim types -- gene family expansion, gene loss, positive selection, "
  "introgression, convergent adaptation, structural variant fixation -- what is the minimum evidence "
  "a 2026 referee should require, and what weaker wording is appropriate when it is absent?"]),
]


def render(slug, chapter, topic, question, prior, subs) -> str:
    numbered = "\n".join(f"{i}. {s}" for i, s in enumerate(subs, 1))
    n = len(subs)
    return f"""You are the research leg of a study plan. Do WEB RESEARCH and report findings.
Do not write files. Do not modify anything. Report only.

TOPIC: {topic}
QUESTION TO ANSWER: {question}
CONTEXT: this is chapter {chapter} of a systematic study plan on comparative genomics as a research
field. The reader has already covered {prior}. They are a computational biologist: assume fluency in
bioinformatics tooling and statistics, but do NOT assume they already know this subfield's
literature. The purpose is to do research in this field AND to referee others' papers, so failure
modes and evidence standards matter as much as methods.
DEPTH: research-level.

FIND AND REPORT:
{numbered}
{n + 1}. Primary sources: papers (title, year, authors, DOI), official docs, canonical repos.
{n + 2}. The current state as of {TODAY} -- flag explicitly anything that changed in the last 18 months.
{n + 3}. Disagreements: where do credible sources conflict? Say so rather than picking one silently.

{CONTRACT}
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, chapter, topic, question, prior, subs in BRIEFS:
        p = OUT/f"{slug}.brief.md"
        p.write_text(render(slug, chapter, topic, question, prior, subs))
        print(f"  {p.relative_to(ROOT)}  ({len(subs)} sub-questions)")
    print(f"\n{len(BRIEFS)} briefs written to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
