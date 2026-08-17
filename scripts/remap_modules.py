#!/usr/bin/env python3
"""Option B restructure: re-file the corpus so the directory tree encodes the
six nested frameworks of the comparative-genomics paradigm.

Old tree: 15 flat dirs mixing analysis-stage / biological-object / taxon axes.
New tree: F0..F6 + X_practice, where the framework layer is the top level and a
failure at layer n invalidates everything above it -- the article's own thesis,
made visible in the filesystem.

Routing is an explicit stem -> module table (not keyword rules) so every one of
the 172 papers is auditable. Papers whose old dir splits are listed individually;
whole-dir moves are expanded from OLD_DIR_MOVES.

Run with --dry-run first. Moves real dirs in the central corpus, rewrites the
`module` field in refs.json, and leaves the hard-link tree to link_into_topic.py.
"""
from __future__ import annotations
import argparse, json, shutil, sys
from pathlib import Path

ROOT   = Path(__file__).resolve().parent.parent
CORPUS = Path.home()/"Desktop/projects/papers/comparative_genomics"
REFS   = ROOT/"scripts/refs.json"

# ---------------------------------------------------------------- the new tree
# Order matters: it is the reading order, and link_into_topic.py sorts by it.
MODULE_ORDER = [
    "F0_foundations",
    "F1_data/qc_annotation",
    "F1_data/repeats_te",
    "F2_homology/orthology",
    "F2_homology/synteny_alignment",
    "F2_homology/ancestral_reconstruction",
    "F2_homology/gene_family_wgd",
    "F3_phylogeny/tree_inference",
    "F3_phylogeny/dating_calibration",
    "F3_phylogeny/comparative_methods_traits",
    "F4_structure/sv_t2t",
    "F4_structure/pangenome_graph",
    "F5_selection/codon_models",
    "F5_selection/convergence",
    "F5_selection/popgen_demography",
    "F5_selection/introgression",
    "F6_function/regulatory_noncoding",
    "F6_function/speciation_landscape",
    "X_practice/microbial_taxonomy",
    "X_practice/ml_constraint",
    "X_practice/reproducibility",
    "X_practice/cases",
]

# Dirs that exist to mark a declared gap in the corpus -- empty on purpose.
GAP_MODULES = {
    "F2_homology/ancestral_reconstruction",
    "X_practice/ml_constraint",
}

# ------------------------------------------------- whole-dir moves (no split)
OLD_DIR_MOVES = {
    "1_orthology":            "F2_homology/orthology",
    "2_synteny_alignment":    "F2_homology/synteny_alignment",
    "3_qc_annotation":        "F1_data/qc_annotation",
    "6_gene_family_wgd":      "F2_homology/gene_family_wgd",
    "8_sv_t2t":               "F4_structure/sv_t2t",
    "9_pangenome_graph":      "F4_structure/pangenome_graph",
    "11_regulatory_noncoding":"F6_function/regulatory_noncoding",
    "13_reproducibility":     "X_practice/reproducibility",
}

# ------------------------------------------- per-paper routing for split dirs
# Every stem in a split dir must appear here or the script refuses to run.
STEM_MOVES = {
    # -- 0_foundations: keeps its own, gains the field-defining manifesto ------
    "PNAS1977_Woese-primary-kingdoms-16S":                 "F0_foundations",
    "GR1998_Eisen-phylogenomics-function":                 "F0_foundations",
    "Nature2001_IHGSC-human-genome-sequencing":            "F0_foundations",
    "Science2001_Venter-human-genome-sequence":            "F0_foundations",
    "Nature2002_mouse-genome-comparative-sequencing":      "F0_foundations",
    "PLOSBiol2003_Hardison-comparative-genomics-primer":   "F0_foundations",
    "Nature2012_ENCODE-DNA-elements-encyclopedia":         "F0_foundations",
    "PNAS2018_Earth-BioGenome-Project-sequencing-life":    "F0_foundations",

    # -- 4_repeats_te: LAI is an assembly-QC metric, not a TE paper -----------
    "NatRevGenet2007_unified-classification-system":       "F1_data/repeats_te",
    "CurrProtBioinf2009_RepeatMasker-identify-repetitive": "F1_data/repeats_te",
    "NatRevGenet2017_Regulatory-activities-transposable":  "F1_data/repeats_te",
    "GB2018_things-you-should":                            "F1_data/repeats_te",
    "GB2019_Benchmarking-transposable-element":            "F1_data/repeats_te",
    "PNAS2020_RepeatModeler2-automated-genomic":           "F1_data/repeats_te",
    "AnnRevGenet2020_field-guide-eukaryotic":              "F1_data/repeats_te",
    "NAR2018_genome-assembly-quality":                     "F1_data/qc_annotation",

    # -- 5_phylogenomics splits three ways ------------------------------------
    "SystBiol1997_Gene-trees-species":                     "F3_phylogeny/tree_inference",
    "TREE2009_Gene-tree-discordance":                      "F3_phylogeny/tree_inference",
    "Bioinf2014_RAxML-version-8-phylogenetic-post-analysis":"F3_phylogeny/tree_inference",
    "Bioinf2014_ASTRAL-genome-scale-coalescent-based":     "F3_phylogeny/tree_inference",
    "MBE2015_IQ-TREE-fast-effective":                      "F3_phylogeny/tree_inference",
    "BMCBioinf2018_ASTRAL-III-polynomial-time":            "F3_phylogeny/tree_inference",
    "Bioinf2019_RAxML-NG-fast-scalable":                   "F3_phylogeny/tree_inference",
    "MBE2020_IQ-TREE-2-models-efficient":                  "F3_phylogeny/tree_inference",
    "BMCEvolBiol2007_BEAST-Bayesian-evolutionary":         "F3_phylogeny/dating_calibration",
    "MBE2011_Approximate-likelihood-calculation":          "F3_phylogeny/dating_calibration",
    "PLOSCB2019_BEAST-25-advanced-software":               "F3_phylogeny/dating_calibration",
    "AmNat1985_Felsenstein-phylogenetic-comparative-method":"F3_phylogeny/comparative_methods_traits",
    "Bioinf2008_GEIGER-investigating-evolutionary":        "F3_phylogeny/comparative_methods_traits",
    "MEE2012_phytools-package-phylogenetic":               "F3_phylogeny/comparative_methods_traits",

    # -- 7_selection: convergence is its own module (PLAN M10) ----------------
    "MBE1986_Simple-numbers-synonymous":                   "F5_selection/codon_models",
    "Nature1991_McDonald-Kreitman-Adh-Drosophila":         "F5_selection/codon_models",
    "MBE1994_codon-based-model-nucleotide":                "F5_selection/codon_models",
    "Genetics2000_Codon-substitution-models-heterogeneous":"F5_selection/codon_models",
    "MBE2002_Codon-substitution-models-molecular":         "F5_selection/codon_models",
    "Bioinf2005_HyPhy-hypothesis-testing":                 "F5_selection/codon_models",
    "AnnRevGenet2005_Molecular-signatures-natural":        "F5_selection/codon_models",
    "MBE2007_PAML-4-phylogenetic-maximum":                 "F5_selection/codon_models",
    "PLOSGenet2012_individual-sites-subject":              "F5_selection/codon_models",
    "AnnRevGenet2013_natural-selection-genomic":           "F5_selection/codon_models",
    "MBE2015_Gene-wide-episodic-selection":                "F5_selection/codon_models",
    "MBE2015_Less-is-more-adaptive-branch-site":           "F5_selection/codon_models",
    "MBE2015_RELAX-relaxed-selection":                     "F5_selection/codon_models",
    "BMCBiol2017_positive-selection-genome":               "F5_selection/codon_models",
    "MBE2020_HyPhy-25-customizable-platform":              "F5_selection/codon_models",
    "NatRevGenet2013_genetic-causes-convergent":           "F5_selection/convergence",
    "Nature2013_Genome-wide-signatures-convergent":        "F5_selection/convergence",
    "MBE2015_convergent-parallel-amino":                   "F5_selection/convergence",
    "NatRevGenet2016_Causes-molecular-convergence":        "F5_selection/convergence",

    # -- 10_popgen_speciation splits three ways -------------------------------
    "SPA1982_Kingman-coalescent":                          "F5_selection/popgen_demography",
    "Bioinf2002_Hudson-ms-coalescent-simulator":           "F5_selection/popgen_demography",
    "AJHG2007_PLINK-set-whole-genome":                     "F5_selection/popgen_demography",
    "PLOSGenet2009_joint-demographic-history":             "F5_selection/popgen_demography",
    "Nature2011_Inference-human-population":               "F5_selection/popgen_demography",
    "Bioinf2011_VCFtools-VCF-format":                      "F5_selection/popgen_demography",
    "PLOSGenet2013_Robust-demographic-inference":          "F5_selection/popgen_demography",
    "TREE2014_population-genetics-understand":             "F5_selection/popgen_demography",
    "NG2014_human-population-size":                        "F5_selection/popgen_demography",
    "MBE2014_PopGenome-efficient-Swiss":                   "F5_selection/popgen_demography",
    "BMCBioinf2014_ANGSD-next-generation":                 "F5_selection/popgen_demography",
    "GigaScience2015_PLINK2-second-generation":            "F5_selection/popgen_demography",
    "NG2017_Robust-scalable-inference":                    "F5_selection/popgen_demography",
    "GigaScience2021_SAMtools-BCFtools-twelve-years":      "F5_selection/popgen_demography",
    "Science2010_draft-sequence-Neandertal":               "F5_selection/introgression",
    "MBE2011_Testing-ancient-admixture":                   "F5_selection/introgression",
    "Genetics2012_Ancient-admixture-human":                "F5_selection/introgression",
    "Nature2014_genomic-landscape-Neanderthal":            "F5_selection/introgression",
    "MBE2015_ABBA-BABA-statistics-locate":                 "F5_selection/introgression",
    "Science2019_Genomic-architecture-introgression":      "F5_selection/introgression",
    "MolEcolRes2021_Dsuite-fast-D-statistics":             "F5_selection/introgression",
    "Nature2012_genomic-landscape-species":                "F6_function/speciation_landscape",
    "NatRevGenet2013_origin-species-genome-scale":         "F6_function/speciation_landscape",
    "NatRevGenet2014_Genomics-origin-species":             "F6_function/speciation_landscape",
    "MolEcol2014_Reanalysis-suggests-genomic":             "F6_function/speciation_landscape",
    "NatRevGenet2017_genomic-islands-differentiation":     "F6_function/speciation_landscape",
    "JEB2017_Interpreting-genomic-landscape":              "F6_function/speciation_landscape",

    # -- 12_microbial: method papers rejoin pangenome; taxon practice stays ----
    "CurrOpinGenDev2005_microbial-pan-genome":             "F4_structure/pangenome_graph",
    "PNAS2005_Genome-multiple-pathogenic":                 "F4_structure/pangenome_graph",
    "Bioinf2015_Roary-rapid-large-scale":                  "F4_structure/pangenome_graph",
    "GB2020_polished-prokaryotic-pangenomes":              "F4_structure/pangenome_graph",
    "PLOSCB2020_PPanGGOLiN-depicting-microbial":           "F4_structure/pangenome_graph",
    "PNAS2005_Genomic-advance-species":                    "X_practice/microbial_taxonomy",
    "NAR2015_Rapid-phylogenetic-large":                    "X_practice/microbial_taxonomy",
    "PLOSCB2015_ClonalFrameML-efficient-inference":        "X_practice/microbial_taxonomy",
    "NC2018_High-throughput-ANI":                          "X_practice/microbial_taxonomy",
    "NBT2018_standardized-bacterial-taxonomy":             "X_practice/microbial_taxonomy",
    "NBT2020_domain-to-species-taxonomy-Bacteria":         "X_practice/microbial_taxonomy",

    # -- 14_cases: infrastructure papers leave, real case studies stay ---------
    "Nature2021_error-free-genome-assemblies":             "F1_data/qc_annotation",
    "GB2018_Genomic-studying-crop":                        "X_practice/cases",
    "Nature2020_barley-pan-genome-reveals":                "X_practice/cases",
    "Cell2020_Pan-genome-wild-cultivated":                 "X_practice/cases",
    "Science2021_novo-assembly-annotation":                "X_practice/cases",
    "Nature2023_pangenome-reference-Chinese":              "X_practice/cases",
    "NG2026_Graph-pan-genome-illuminates":                 "X_practice/cases",
}


def resolve(rec: dict) -> str:
    """New module for a ref record. Explicit stem table wins over dir moves."""
    if rec["stem"] in STEM_MOVES:
        return STEM_MOVES[rec["stem"]]
    if rec["module"] in OLD_DIR_MOVES:
        return OLD_DIR_MOVES[rec["module"]]
    raise KeyError(f"unrouted: {rec['module']}/{rec['stem']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    refs = json.loads(REFS.read_text())

    # 1. resolve every record first -- refuse to move anything if one is unrouted
    plan = []
    for rec in refs:
        plan.append((rec, rec["module"], resolve(rec)))
    for _, _, new in plan:
        if new not in MODULE_ORDER:
            sys.exit(f"ERROR: target module not in MODULE_ORDER: {new}")

    counts: dict[str, int] = {m: 0 for m in MODULE_ORDER}
    for _, _, new in plan:
        counts[new] += 1
    print(f"routed {len(plan)}/172 refs into {len(MODULE_ORDER)} modules\n")
    for m in MODULE_ORDER:
        tag = "  (gap -- empty on purpose)" if m in GAP_MODULES else ""
        print(f"  {counts[m]:>3}  {m}{tag}")

    # 2. any dir in the corpus not accounted for by refs.json?
    known = {f"{old}/{rec['stem']}" for rec, old, _ in plan}
    orphans = []
    if CORPUS.is_dir():
        for d in sorted(CORPUS.iterdir()):
            if not d.is_dir() or d.name.startswith(("F", "X")):
                continue
            for s in sorted(d.iterdir()):
                if s.is_dir() and f"{d.name}/{s.name}" not in known:
                    orphans.append(f"{d.name}/{s.name}")
    if orphans:
        print(f"\n!! {len(orphans)} corpus dirs not in refs.json (left in place):")
        for o in orphans:
            print(f"     {o}")

    if args.dry_run:
        print("\n[dry run] nothing moved")
        return

    # 3. move the real dirs in the central corpus
    moved = skipped = 0
    for rec, old, new in plan:
        src, dst = CORPUS/old/rec["stem"], CORPUS/new/rec["stem"]
        if dst.exists():
            skipped += 1; continue
        if not src.is_dir():
            skipped += 1; continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        moved += 1
    for m in MODULE_ORDER:                       # gap dirs + any empty target
        (CORPUS/m).mkdir(parents=True, exist_ok=True)

    # 4. prune the old dirs if now empty
    pruned = []
    for d in sorted(CORPUS.iterdir()):
        if d.is_dir() and not d.name.startswith(("F", "X")) and not any(d.iterdir()):
            d.rmdir(); pruned.append(d.name)

    # 5. rewrite refs.json
    REFS.with_suffix(".json.bak").write_text(json.dumps(refs, indent=2, ensure_ascii=False))
    for rec, _, new in plan:
        rec["module"] = new
    REFS.write_text(json.dumps(refs, indent=2, ensure_ascii=False))

    print(f"\nmoved {moved} · skipped {skipped} · pruned {len(pruned)} empty old dirs")
    print(f"refs.json rewritten (backup at {REFS.with_suffix('.json.bak').name})")
    print("next: rm -rf resources/papers && python3 scripts/link_into_topic.py")


if __name__ == "__main__":
    main()
