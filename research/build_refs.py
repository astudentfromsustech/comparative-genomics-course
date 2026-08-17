#!/usr/bin/env python3
"""Build the PaperRef list for the 172 references cited in the
"比较基因组学范式" (Comparative Genomics Paradigm) article.

Reads 0_source/references.tsv, assigns each paper to a corpus module dir that
mirrors the article's own structure, derives a strict stem, and attaches a
repo_url for genuine tool papers.
"""
from __future__ import annotations
import csv, re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- journal name -> short prefix (extends s0_background_survey JOURNAL_MAP) ---
JOURNAL_MAP = {
    "Nature": "Nature", "Science": "Science", "Cell": "Cell",
    "Nature Methods": "NatMethods", "Nature Biotechnology": "NBT",
    "Nature Plants": "NatPlants", "Nature Genetics": "NG",
    "Nature Communications": "NC", "Nature Reviews Genetics": "NatRevGenet",
    "Genome Biology": "GB", "Genome Research": "GR",
    "Bioinformatics": "Bioinf", "BMC Bioinformatics": "BMCBioinf",
    "BMC Biology": "BMCBiol", "BMC Evolutionary Biology": "BMCEvolBiol",
    "Nucleic Acids Research": "NAR", "Molecular Biology and Evolution": "MBE",
    "Molecular Plant": "MolPlant", "Molecular Ecology": "MolEcol",
    "Molecular Ecology Resources": "MolEcolRes", "GigaScience": "GigaScience",
    "Genetics": "Genetics", "Systematic Biology": "SystBiol",
    "Systematic Zoology": "SystZool", "Cell Genomics": "CellGenomics",
    "Scientific Data": "SciData", "Genome Medicine": "GenomeMed",
    "Trends in Plant Science": "TrendsPlantSci",
    "Trends in Ecology & Evolution": "TREE",
    "Trends in Genetics": "TrendsGenet",
    "Annual Review of Genetics": "AnnRevGenet",
    "Annual Review of Biochemistry": "AnnRevBiochem",
    "Annual Review of Genomics and Human Genetics": "AnnRevGenomics",
    "Proceedings of the National Academy of Sciences": "PNAS",
    "PLoS Biology": "PLOSBiol", "PLoS Genetics": "PLOSGenet",
    "PLoS ONE": "PLOSONE", "PLoS Computational Biology": "PLOSCB",
    "PLOS Computational Biology": "PLOSCB",
    "Plant Biotechnology Journal": "PBJ",
    "Current Opinion in Microbiology": "CurrOpinMicro",
    "Current Opinion in Genetics & Development": "CurrOpinGenDev",
    "Current Protocols in Bioinformatics": "CurrProtBioinf",
    "American Journal of Human Genetics": "AJHG",
    "The American Naturalist": "AmNat",
    "Journal of Evolutionary Biology": "JEB",
    "Methods in Ecology and Evolution": "MEE",
    "Methods in Molecular Biology": "MiMB",
    "NAR Genomics and Bioinformatics": "NARGAB",
    "Stochastic Processes and their Applications": "SPA",
}

def journal_short(j: str) -> str:
    j = j.strip()
    if j in JOURNAL_MAP:
        return JOURNAL_MAP[j]
    # fall back: CamelCase-squash the journal name
    return re.sub(r"[^A-Za-z]", "", j.title())[:16] or "Jrnl"

# --- module assignment: ordered (regex-on-title-or-journal, module) rules ---
# Mirrors the article's own section order.
RULES = [
    # 12_microbial — before generic pangenome rules
    (r"prokaryot|bacteri|archaea|Roary|Panaroo|PPanGGOLiN|Gubbins|ClonalFrame|"
     r"species definition for prokaryotes|Streptococcus|microbial pan-genome|"
     r"ANI analysis|standardized bacterial taxonomy|domain-to-species", "12_microbial"),
    # 9_pangenome_graph
    (r"pan-?genom|pangenom|variation graph|minigraph|\bgraphs?\b|Ten years of pan", "9_pangenome_graph"),
    # 8_sv_t2t
    (r"structural variation|structural variant|complete sequence|telomere-to-telomere|"
     r"complete reference genome|centromere|complete human|Y chromosome|chromosome 8|"
     r"Jasmine|gap-free|difficult-to-map", "8_sv_t2t"),
    # 4_repeats_te
    (r"transposable element|RepeatModeler|RepeatMasker|repetitive element|"
     r"LTR Assembly Index|transposable", "4_repeats_te"),
    # 3_qc_annotation
    (r"BUSCO|QUAST|Merqury|assembly quality|completeness|gene prediction|"
     r"MAKER2|BRAKER2|intron position conservation|InterProScan|Pfam|"
     r"Gene Ontology|KEGG|hidden Markov model and a new intron", "3_qc_annotation"),
    # 1_orthology
    (r"ortholog|OrthoMCL|OrthoFinder|OMA orthology|eggNOG|OrthoDB|paralog|"
     r"homologous from analogous", "1_orthology"),
    # 2_synteny_alignment
    (r"MCScanX|synteny|collinear|Alignment of whole genomes|comparing large genomes|"
     r"Minimap2|progressiveMauve|HAL:|Progressive Cactus|SibeliaZ|Mash:|"
     r"whole-genome alignment tools", "2_synteny_alignment"),
    # 5_phylogenomics
    (r"IQ-TREE|RAxML|ASTRAL|BEAST|phylogen|Gene trees in species trees|"
     r"gene tree discordance|divergence time|Approximate likelihood|GEIGER|phytools|"
     r"comparative method|primary kingdoms|coalescent$", "5_phylogenomics"),
    # 6_gene_family_wgd
    (r"CAFE|BadiRate|gene family|duplicate genes|duplicated genes|polyploid|"
     r"Ancestral polyploidy|Preservation of duplicate", "6_gene_family_wgd"),
    # 7_selection
    (r"selection|dN/dS|codon|synonymous|PAML|HyPhy|RELAX|episodic|"
     r"Adaptive protein evolution|convergent|parallelism|local adaptation|"
     r"molecular adaptation", "7_selection"),
    # 10_popgen_speciation
    (r"population history|population size|demographic|coalescent|admixture|"
     r"Neandertal|Neanderthal|introgress|speciation|origin of species|"
     r"genomic islands|gene flow|Dsuite|D-statistics|ABBA|Wright-Fisher|"
     r"PopGenome|ANGSD|PLINK|VCFtools|SAMtools|BCFtools|flycatcher|butterfly", "10_popgen_speciation"),
    # 11_regulatory_noncoding
    (r"cis-regulatory|enhancer|regulatory variation|noncoding|non-coding|"
     r"lncRNA|long noncoding|transcriptome|ENCODE|two levels in humans", "11_regulatory_noncoding"),
    # 13_reproducibility
    (r"Snakemake|Nextflow|FAIR|Bioconda|workflow", "13_reproducibility"),
    # 14_cases
    (r"maize genomes|barley pan|soybean|cotton|rice|vertebrate species|"
     r"Earth BioGenome|Chinese populations|crop evolution|crop improvement", "14_cases"),
    # 0_foundations — catch-all landmarks
    (r"human genome|mouse genome|Comparative genomics|Phylogenomics:", "0_foundations"),
]

def assign_module(title: str, journal: str) -> str:
    hay = f"{title} || {journal}"
    for pat, mod in RULES:
        if re.search(pat, hay, re.I):
            return mod
    return "0_foundations"

# --- explicit overrides where the regex order misfires (DOI -> module) ---
MODULE_OVERRIDE = {
    "10.1073/pnas.74.11.5088": "0_foundations",       # Woese & Fox
    "10.1101/gr.8.3.163": "0_foundations",            # Eisen phylogenomics
    "10.1146/annurev.genet.39.073003.114725": "1_orthology",   # Koonin orthologs
    "10.1038/nrg3456": "1_orthology",                 # Gabaldon & Koonin
    "10.1093/nar/gkaa1009": "1_orthology",            # OrthoDB
    "10.1093/molbev/msab293": "3_qc_annotation",      # eggNOG-mapper v2
    "10.1093/nar/gky1085": "1_orthology",             # eggNOG 5.0
    "10.1038/nrg.2016.139": "4_repeats_te",           # Chuong TE regulatory
    "10.1146/annurev-genet-040620-022145": "4_repeats_te",
    "10.1016/0304-4149(82)90011-4": "10_popgen_speciation",   # Kingman coalescent
    "10.1093/bioinformatics/18.2.337": "10_popgen_speciation",  # Hudson ms
    "10.1086/284325": "5_phylogenomics",              # Felsenstein
    "10.1038/nrg3373": "8_sv_t2t",                    # Weischenfeldt SV phenotype
    "10.1038/s41586-020-2547-7": "8_sv_t2t",          # T2T X chromosome
    "10.1016/j.molp.2021.06.018": "8_sv_t2t",         # rice gap-free centromere
    "10.1038/s41576-024-00691-4": "9_pangenome_graph",
    "10.1111/pbi.12499": "9_pangenome_graph",         # towards plant pangenomics
    "10.1038/s41586-020-2947-8": "14_cases",          # barley pangenome
    "10.1126/science.abg5289": "14_cases",            # 26 maize genomes
    "10.1016/j.cell.2020.05.023": "14_cases",         # soybean pangenome
    "10.1038/s41588-025-02462-1": "14_cases",         # cotton graph pangenome
    "10.1038/s41586-023-06173-7": "14_cases",         # 36 Chinese populations
    "10.1186/s13059-018-1528-8": "14_cases",          # crop evolution
    "10.1038/s41586-021-03451-0": "14_cases",         # VGP
    "10.1073/pnas.1720115115": "14_cases",            # Earth BioGenome
    "10.1038/nature11584": "10_popgen_speciation",    # Ficedula
    "10.1126/science.aaw2090": "10_popgen_speciation",# Heliconius
    "10.1016/j.tplants.2023.08.013": "2_synteny_alignment",  # WGA tools for plants
    "10.1038/s41592-018-0046-7": "13_reproducibility",# Bioconda
    "10.1038/sdata.2016.18": "13_reproducibility",    # FAIR
    "10.1146/annurev-biochem-051410-092902": "11_regulatory_noncoding",
    "10.1038/nrg3802": "11_regulatory_noncoding",
    "10.1038/nature12511": "7_selection",             # echolocating mammals
    "10.1016/j.tree.2014.10.004": "10_popgen_speciation",  # local adaptation limits
    "10.1186/s12915-017-0434-y": "7_selection",       # detecting positive selection
    "10.1093/molbev/msab199": "3_qc_annotation",      # BUSCO update (matched "prokaryotic")
    "10.1093/bioinformatics/bti079": "7_selection",   # HyPhy — used for selection in the article
    "10.1093/molbev/msz197": "7_selection",           # HyPhy 2.5
    "10.1093/molbev/msu400": "7_selection",           # RELAX
    "10.1093/molbev/msm088": "7_selection",           # PAML 4 (codeml); MCMCtree paper stays in 5_
}

# --- tool papers -> GitHub repo (paper+code coupling) ---
REPOS = {
    "10.1101/gr.1224503": "https://github.com/stajichlab/OrthoMCL",
    "10.1186/s13059-015-0721-2": "https://github.com/davidemms/OrthoFinder",
    "10.1186/s13059-019-1832-y": "https://github.com/davidemms/OrthoFinder",
    "10.1093/molbev/msab293": "https://github.com/eggnogdb/eggnog-mapper",
    "10.1093/nar/gkr1293": "https://github.com/wyp1125/MCScanX",
    "10.1093/bioinformatics/bty191": "https://github.com/lh3/minimap2",
    "10.1186/gb-2004-5-2-r12": "https://github.com/mummer4/mummer",
    "10.1093/bioinformatics/btt128": "https://github.com/ComparativeGenomicsToolkit/hal",
    "10.1038/s41586-020-2871-y": "https://github.com/ComparativeGenomicsToolkit/cactus",
    "10.1038/s41467-020-19777-8": "https://github.com/medvedevgroup/SibeliaZ",
    "10.1186/s13059-016-0997-x": "https://github.com/marbl/Mash",
    "10.1038/s41467-018-07641-9": "https://github.com/ParBLiSS/FastANI",
    "10.1093/bioinformatics/btv351": "https://gitlab.com/ezlab/busco",
    "10.1093/molbev/msab199": "https://gitlab.com/ezlab/busco",
    "10.1093/bioinformatics/btt086": "https://github.com/ablab/quast",
    "10.1186/s13059-020-02134-9": "https://github.com/marbl/merqury",
    "10.1093/nar/gky730": "https://github.com/oushujun/LTR_retriever",
    "10.1073/pnas.1921046117": "https://github.com/Dfam-consortium/RepeatModeler",
    "10.1186/s13059-019-1905-y": "https://github.com/oushujun/EDTA",
    "10.1186/1471-2105-12-491": "https://github.com/Yandell-Lab/maker",
    "10.1093/nargab/lqaa108": "https://github.com/Gaius-Augustus/BRAKER",
    "10.1093/bioinformatics/btu031": "https://github.com/ebi-pf-team/interproscan",
    "10.1093/molbev/msu300": "https://github.com/iqtree/iqtree2",
    "10.1093/molbev/msaa015": "https://github.com/iqtree/iqtree2",
    "10.1093/bioinformatics/btu033": "https://github.com/stamatak/standard-RAxML",
    "10.1093/bioinformatics/btz305": "https://github.com/amkozlov/raxml-ng",
    "10.1093/bioinformatics/btu462": "https://github.com/smirarab/ASTRAL",
    "10.1186/s12859-018-2129-y": "https://github.com/smirarab/ASTRAL",
    "10.1371/journal.pcbi.1006650": "https://github.com/CompEvol/beast2",
    "10.1093/molbev/msm088": "https://github.com/abacus-gene/paml",
    "10.1111/j.2041-210X.2011.00169.x": "https://github.com/liamrevell/phytools",
    "10.1093/bioinformatics/btl097": "https://github.com/hahnlab/CAFE",
    "10.1093/bioinformatics/btaa1022": "https://github.com/hahnlab/CAFE5",
    "10.1093/bioinformatics/bti079": "https://github.com/veg/hyphy",
    "10.1093/molbev/msz197": "https://github.com/veg/hyphy",
    "10.1038/s41592-018-0001-7": "https://github.com/fritzsedlazeck/Sniffles",
    "10.1038/nbt.4227": "https://github.com/vgteam/vg",
    "10.1186/s13059-020-02168-z": "https://github.com/lh3/minigraph",
    "10.1038/s41587-023-01793-w": "https://github.com/ComparativeGenomicsToolkit/cactus",
    "10.1093/bioinformatics/btv421": "https://github.com/sanger-pathogens/Roary",
    "10.1186/s13059-020-02090-4": "https://github.com/gtonkinhill/panaroo",
    "10.1371/journal.pcbi.1007732": "https://github.com/labgem/PPanGGOLiN",
    "10.1371/journal.pgen.1000695": "https://github.com/niuhuifei/dadi",
    "10.1038/ng.3748": "https://github.com/popgenmethods/smcpp",
    "10.1111/1755-0998.13265": "https://github.com/millanek/Dsuite",
    "10.1093/nar/gku1196": "https://github.com/nickjcroucher/gubbins",
    "10.1371/journal.pcbi.1004041": "https://github.com/xavierdidelot/ClonalFrameML",
    "10.1093/molbev/msu136": "https://github.com/pievos101/PopGenome",
    "10.1186/s12859-014-0356-4": "https://github.com/ANGSD/angsd",
    "10.1186/s13742-015-0047-8": "https://github.com/chrchang/plink-ng",
    "10.1093/bioinformatics/btr330": "https://github.com/vcftools/vcftools",
    "10.1093/gigascience/giab008": "https://github.com/samtools/bcftools",
    "10.1093/bioinformatics/bts480": "https://github.com/snakemake/snakemake",
    "10.1038/nbt.3820": "https://github.com/nextflow-io/nextflow",
    "10.1038/s41592-022-01753-3": "https://github.com/mkirsche/Jasmine",
    "10.1093/bioinformatics/btr623": "https://github.com/fgvieira/badirate",
}

# --- keyword extraction for the stem ---
STOP = set("""a an the of and or for from with without in on to by via using use
into is are as at its their this that new novel toward towards more less than
between among across during over under within analysis analyses study studies
approach approaches method methods tool tools data based complete first second
ten twelve years insights advances limits detecting inferring assessing making
sense light understanding evaluating comparing producing turning distinguishing
identification identifying estimation estimating construction constructing
""".split())

MANUAL_KW = {
    "10.1038/35057062": ["IHGSC", "human-genome", "sequencing"],
    "10.1126/science.1058040": ["Venter", "human-genome", "sequence"],
    "10.1038/nature01262": ["mouse-genome", "comparative", "sequencing"],
    "10.1101/gr.8.3.163": ["Eisen", "phylogenomics", "function"],
    "10.1371/journal.pbio.0000058": ["Hardison", "comparative-genomics", "primer"],
    "10.1073/pnas.74.11.5088": ["Woese", "primary-kingdoms", "16S"],
    "10.2307/2412448": ["Fitch", "homology", "analogy"],
    "10.1086/284325": ["Felsenstein", "phylogenetic", "comparative-method"],
    "10.1016/0304-4149(82)90011-4": ["Kingman", "coalescent"],
    "10.1093/bioinformatics/18.2.337": ["Hudson", "ms", "coalescent-simulator"],
    "10.1038/351652a0": ["McDonald-Kreitman", "Adh", "Drosophila"],
    "10.1126/science.1090005": ["King-Wilson", "two-levels", "chimpanzee"],
    "10.1038/nature11247": ["ENCODE", "DNA-elements", "encyclopedia"],
    "10.1093/gigascience/giab008": ["SAMtools", "BCFtools", "twelve-years"],
    "10.1186/s13742-015-0047-8": ["PLINK2", "second-generation"],
    "10.1093/bioinformatics/btr330": ["VCFtools", "VCF-format"],
}

def keywords_for(doi: str, title: str) -> list[str]:
    if doi in MANUAL_KW:
        return MANUAL_KW[doi]
    # tool name = leading token before ':' if it looks like a tool
    kws: list[str] = []
    head = title.split(":")[0].strip()
    if len(title.split(":")) > 1 and len(head.split()) <= 3:
        kws.append(re.sub(r"[^\w.+-]", "-", head))
        rest = title.split(":", 1)[1]
    else:
        rest = title
    for w in re.findall(r"[A-Za-z][\w'-]+", rest):
        lw = w.lower()
        if lw in STOP or len(w) < 3:
            continue
        if any(lw == k.lower() for k in kws):
            continue
        kws.append(w)
        if len(kws) >= 3:
            break
    kws = [re.sub(r"[^\w+-]", "", k).strip("-") for k in kws if k]
    return (kws or ["paper"])[:3]


def main() -> None:
    # ---------------------------------------------------------------- RETIRED
    # This script built the ORIGINAL 15 flat module dirs from the source
    # article's bibliography. That layout was replaced (2026-08-17) by the
    # framework-layered tree F0..F6 + X_practice, and refs.json is now the
    # authoritative record of which module each paper belongs to.
    #
    # Re-running this would silently overwrite refs.json with the OLD flat
    # module names, orphaning every paper on disk. The source it reads
    # (0_source/references.tsv) has also been retired. Routing now lives in
    # research/remap_modules.py, one auditable line per paper.
    src = ROOT / "0_source/references.tsv"
    if not src.exists():
        raise SystemExit(
            "build_refs.py is RETIRED and its input is gone.\n"
            "  refs.json is authoritative; module routing lives in remap_modules.py.\n"
            "  Running this would revert the F0..F6 layout. Nothing was changed."
        )
    rows = list(csv.DictReader(open(src), delimiter="\t"))
    out = []
    seen: dict[str, int] = {}
    for r in rows:
        doi, title, jrnl = r["doi"], r["title"], r["journal"]
        year = int(r["year"])
        js = journal_short(jrnl)
        kws = keywords_for(doi, title)
        stem = f"{js}{year}_" + "-".join(kws)
        if stem in seen:                      # disambiguate collisions
            seen[stem] += 1
            kws = kws[:2] + [f"v{seen[stem]}"]
            stem = f"{js}{year}_" + "-".join(kws)
        else:
            seen[stem] = 1
        out.append({
            "doi": doi, "title": title, "journal": jrnl, "year": year,
            "journal_short": js, "keywords": kws, "stem": stem,
            "module": MODULE_OVERRIDE.get(doi) or assign_module(title, jrnl),
            "repo_url": REPOS.get(doi),
            "authors": r["authors"],
        })
    (ROOT / "research/refs.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    from collections import Counter
    for m, n in sorted(Counter(x["module"] for x in out).items()):
        print(f"{n:4d}  {m}")
    print(f"{len(out):4d}  TOTAL   ({sum(1 for x in out if x['repo_url'])} with repos)")


if __name__ == "__main__":
    main()
