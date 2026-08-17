#!/usr/bin/env python3
"""Download the 172 papers cited by the Comparative Genomics Paradigm article.

Real files land in the central corpus:
    ~/Desktop/projects/papers/comparative_genomics/<module>/<stem>/
Repos clone INSIDE each paper dir (paper+code coupling).

Resumable: a paper dir that already holds a valid <stem>.pdf is skipped.
Progress is appended to research/download_log.jsonl after every paper.
"""
from __future__ import annotations
import json, sys, os, traceback
from pathlib import Path

sys.path.insert(0, str(Path.home()/"Library/Mobile Documents/com~apple~CloudDocs/CompAlgoClaw"))
sys.path.insert(0, str(Path.home()/".claude/skills/paper-downloader"))
from run import PaperRef, download_one            # noqa: E402

ROOT   = Path(__file__).resolve().parent.parent
CORPUS = Path.home()/"Desktop/projects/papers/comparative_genomics"
LOG    = ROOT/"research/download_log.jsonl"

# already in the corpus under another topic — hard-link, don't re-download
ALREADY = {
 "10.1126/science.abl4178": "genome_assembly/2_assemble/Science2022-complete-genomic-epigenetic-maps-human-centromeres",
 "10.1038/s41586-021-03420-7": "genome_assembly/2_assemble/Nature2021-structure-function-evolution-complete-human-chromosome8",
 "10.1093/bioinformatics/btt086": "genome_assembly/8_evaluations/Bioinf2013-QUAST-quality-assessment",
 "10.1186/s13059-016-0997-x": "genome_assembly/1_kmer/GB2016-Mash-minhash-distance",
}

def valid_pdf(p: Path) -> bool:
    try:
        return p.is_file() and p.stat().st_size > 20000 and p.open('rb').read(5) == b'%PDF-'
    except OSError:
        return False

def link_existing(rec: dict) -> dict:
    """Hard-link a paper that already lives elsewhere in the corpus."""
    src = Path.home()/"Desktop/projects/papers"/ALREADY[rec["doi"]]
    dst = CORPUS/rec["module"]/rec["stem"]
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted(src.glob("*")):
        if not f.is_file():
            continue
        suffix = f.name[len(src.name):]           # "" | ".pdf" | "_supple.pdf" ...
        tgt = dst/(rec["stem"] + (suffix or f.suffix))
        if not tgt.exists():
            os.link(f, tgt); n += 1
    return {"stem": rec["stem"], "doi": rec["doi"], "pdf_status": f"hardlinked_{n}",
            "supplement_status": "-", "repo_status": "-", "module": rec["module"]}

def main() -> None:
    refs = json.load(open(ROOT/"research/refs.json"))
    only = sys.argv[1] if len(sys.argv) > 1 else None
    done = set()
    if LOG.exists():
        done = {json.loads(l)["doi"] for l in LOG.open() if l.strip()}

    for i, rec in enumerate(refs, 1):
        if only and rec["module"] != only:
            continue
        dest = CORPUS/rec["module"]
        pdir = dest/rec["stem"]
        tag = f"[{i:3d}/{len(refs)}] {rec['module']:22s} {rec['stem'][:46]}"

        # Resume on DISK TRUTH, not on "was logged". A logged no_oa is a FAILURE
        # to retry on the next pass, not a completed paper. (The old condition
        # `rec["doi"] in done` silently skipped every paper that had ever failed,
        # so re-running could never recover anything.)
        if valid_pdf(pdir/f"{rec['stem']}.pdf"):
            print(f"{tag}  SKIP (have)", flush=True);  continue
        if rec["doi"] in ALREADY:
            r = link_existing(rec)
            print(f"{tag}  {r['pdf_status']}", flush=True)
        else:
            ref = PaperRef(journal_short=rec["journal_short"], year=rec["year"],
                           keywords=rec["keywords"], doi=rec["doi"],
                           title=rec["title"], repo_url=rec["repo_url"],
                           module="evaluation")
            try:
                r = download_one(ref, vault_path=str(CORPUS), dest_dir=str(dest),
                                 repo_clone_dir=str(pdir),
                                 clone_repo=bool(rec["repo_url"]))
            except Exception as e:
                traceback.print_exc()
                r = {"stem": rec["stem"], "doi": rec["doi"], "pdf_status": f"ERROR:{e}",
                     "supplement_status": "-", "repo_status": "-"}
            r["module"] = rec["module"]
            print(f"{tag}  pdf={r.get('pdf_status')} sup={r.get('supplement_status')} "
                  f"repo={r.get('repo_status')}", flush=True)
        with LOG.open("a") as fh:
            fh.write(json.dumps(r, default=str) + "\n")

if __name__ == "__main__":
    main()
