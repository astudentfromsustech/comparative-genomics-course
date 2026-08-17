#!/usr/bin/env python3
"""Hard-link the corpus papers into this study topic's resources/papers/ tree.

Corpus (~/Desktop/projects/papers/comparative_genomics/) holds the ONE real copy of
every PDF and supplement. This topic gets hard links — same inode, zero extra disk.
Tool repos are directories and cannot be hard-linked, so they are symlinked.

Also writes resources/papers/INDEX.md: the module -> paper catalogue with DOIs and status.
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from remap_modules import MODULE_ORDER, GAP_MODULES   # the framework-layered tree

ROOT   = Path(__file__).resolve().parent.parent
CORPUS = Path.home()/"Desktop/projects/papers/comparative_genomics"
DEST   = ROOT/"resources/papers"

def valid_pdf(p: Path) -> bool:
    try:
        return p.is_file() and p.stat().st_size > 20000 and p.open('rb').read(5) == b'%PDF-'
    except OSError:
        return False

def main() -> None:
    refs = json.load(open(ROOT/"research/refs.json"))
    linked = repos = missing = 0
    by_mod: dict[str, list] = {}

    for rec in refs:
        src = CORPUS/rec["module"]/rec["stem"]
        dst = DEST/rec["module"]/rec["stem"]
        pdf = src/f"{rec['stem']}.pdf"
        has = valid_pdf(pdf)
        if not has:
            missing += 1
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
            for f in sorted(src.iterdir()):
                tgt = dst/f.name
                if f.is_file():
                    if not tgt.exists():
                        os.link(f, tgt); linked += 1
                elif f.is_dir() and not tgt.exists():      # tool repo -> symlink
                    os.symlink(f, tgt); repos += 1
        by_mod.setdefault(rec["module"], []).append((rec, has))

    for mod in GAP_MODULES:                       # declared gaps stay visible
        (DEST/mod).mkdir(parents=True, exist_ok=True)

    lines = ["# Comparative genomics — paper corpus", "",
             "Filed by **framework layer** (F0..F6 + X_practice): a failure at layer *n*",
             "invalidates everything above it. Real files live in",
             "`~/Desktop/projects/papers/comparative_genomics/`; these are hard links.",
             "Tool repos are symlinks (directories cannot be hard-linked).", ""]
    total = sum(len(v) for v in by_mod.values())
    have  = sum(1 for v in by_mod.values() for _, h in v if h)
    lines += [f"**{have}/{total} PDFs present.**", ""]
    for mod in MODULE_ORDER:
        rows = by_mod.get(mod, [])
        if not rows:
            lines += [f"## {mod}  (0/0)", "",
                      "*Declared gap — no papers yet. The field has this literature; "
                      "this corpus does not.*", ""]
            continue
        n = sum(1 for _, h in rows if h)
        lines += [f"## {mod}  ({n}/{len(rows)})", "",
                  "| ✓ | Paper | Year | Journal | DOI | Repo |",
                  "|---|-------|------|---------|-----|------|"]
        for rec, h in sorted(rows, key=lambda x: x[0]["year"]):
            repo = rec["repo_url"].rsplit("/", 1)[-1] if rec["repo_url"] else ""
            t = rec["title"].replace("|", "\\|")
            lines.append(f"| {'✓' if h else '·'} | {t} | {rec['year']} | "
                         f"{rec['journal']} | [{rec['doi']}](https://doi.org/{rec['doi']}) | {repo} |")
        lines.append("")
    (DEST/"INDEX.md").write_text("\n".join(lines))

    print(f"hard-linked {linked} files · symlinked {repos} repos · {missing} papers still without a PDF")
    print(f"catalogue -> {DEST/'INDEX.md'}")

if __name__ == "__main__":
    main()
