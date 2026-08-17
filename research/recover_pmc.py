#!/usr/bin/env python3
"""Recovery pass: fetch papers the 13-source ladder missed, via Europe PMC render.

`https://europepmc.org/articles/<PMCID>?pdf=render` reliably returns the PDF for
PMC-deposited papers where the publisher and the NCBI OA FTP both fail — including
some flagged isOpenAccess=N. Documented in paper-downloader SKILL.md.

Run after run_download.py. Idempotent: papers that already have a valid PDF are skipped.
"""
from __future__ import annotations
import json, urllib.request, urllib.parse, sys, time
from pathlib import Path

ROOT   = Path(__file__).resolve().parent.parent
CORPUS = Path.home()/"Desktop/projects/papers/comparative_genomics"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

def valid_pdf(p: Path) -> bool:
    try:
        return p.is_file() and p.stat().st_size > 20000 and p.open('rb').read(5) == b'%PDF-'
    except OSError:
        return False

def pmcid_for(doi: str) -> str | None:
    q = urllib.parse.quote(f'DOI:"{doi}"')
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&format=json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30))
        res = d.get("resultList", {}).get("result", [])
        pid = res[0].get("pmcid") if res else None
        return pid if pid and str(pid).startswith("PMC") else None
    except Exception:
        return None

def fetch(pmcid: str, dest: Path) -> bool:
    url = f"https://europepmc.org/articles/{pmcid}?pdf=render"
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90)
        data = r.read()
    except Exception:
        return False
    if not data.startswith(b'%PDF-') or len(data) < 20000:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return True

def main() -> None:
    refs = json.load(open(ROOT/"research/refs.json"))
    got = fail = skip = 0
    for rec in refs:
        pdf = CORPUS/rec["module"]/rec["stem"]/f"{rec['stem']}.pdf"
        if valid_pdf(pdf):
            skip += 1; continue
        pid = pmcid_for(rec["doi"])
        if not pid:
            print(f"  no-pmcid  {rec['stem'][:52]:54s} {rec['doi']}", flush=True); fail += 1; continue
        if fetch(pid, pdf):
            print(f"  RECOVERED {rec['stem'][:52]:54s} {pid}", flush=True); got += 1
        else:
            print(f"  render-fail {rec['stem'][:50]:52s} {pid}", flush=True); fail += 1
        time.sleep(1.0)                       # be polite to EBI
    print(f"\nrecovered {got} · still missing {fail} · already had {skip}")

if __name__ == "__main__":
    main()
