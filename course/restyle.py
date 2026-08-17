#!/usr/bin/env python3
"""Push _style.css into every chapter page.

ONE file per chapter: <chapter>/index.html is the whole page — content and CSS
together, self-contained, openable and shareable on its own. You edit it
directly; there is no source fragment and no second file to confuse with it.

This script exists only so a DESIGN change does not mean editing 14 files: it
replaces whatever sits between <style> and </style> in each page with the
current contents of _style.css, and touches nothing else.

    python3 course/restyle.py           # restyle every page
    python3 course/restyle.py --check   # report drift, change nothing
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

ROOT  = Path(__file__).resolve().parent
STYLE = ROOT/"_style.css"
STYLE_BLOCK = re.compile(r"(<style>)(.*?)(</style>)", re.S)


def pages() -> list[Path]:
    """One page per directory, NAMED AFTER the directory — <dir>/<dir>.html.

    Matches the ConCurate figure convention (Fig2/concurate_fig2_method_v1.html):
    the filename says what the file is, so it stays meaningful in a browser tab,
    a bookmark, or an email attachment — where "index.html" says nothing.
    The course landing page is course/course.html.
    """
    found = [ROOT/"course.html"] if (ROOT/"course.html").is_file() else []
    found += sorted(d/f"{d.name}.html" for d in ROOT.iterdir()
                    if d.is_dir() and not d.name.startswith("_")
                    and (d/f"{d.name}.html").is_file())
    return found


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report drift, change nothing")
    args = ap.parse_args()

    if not STYLE.is_file():
        sys.exit(f"missing {STYLE}")
    css = STYLE.read_text()

    changed = same = broken = 0
    for p in pages():
        html = p.read_text()
        m = STYLE_BLOCK.search(html)
        label = p.parent.name if p.parent != ROOT else "index (landing)"
        if not m:
            print(f"  !! {label:34s} no <style> block — skipped")
            broken += 1
            continue
        if m.group(2) == css:
            print(f"     {label:34s} up to date")
            same += 1
            continue
        if args.check:
            print(f"  ~  {label:34s} DRIFTED")
            changed += 1
            continue
        p.write_text(html[:m.start(2)] + css + html[m.end(2):])
        print(f"  ✓  {label:34s} restyled ({len(p.read_text())//1024} KB)")
        changed += 1

    verb = "would change" if args.check else "restyled"
    print(f"\n{changed} {verb} · {same} already current"
          + (f" · {broken} without a <style> block" if broken else ""))


if __name__ == "__main__":
    main()
