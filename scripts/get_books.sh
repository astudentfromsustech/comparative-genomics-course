#!/usr/bin/env bash
# Fetch the two open-access textbooks into resources/books/.
# They are gitignored because of size (96 MB + 12 MB), not licence.
set -euo pipefail
cd "$(dirname "$0")/../resources/books"
dl () { mkdir -p "$1"; [ -s "$1/$1.pdf" ] && { echo "  have $1"; return; }
        echo "  fetching $1 …"; curl -sL --max-time 600 "$2" -o "$1/$1.pdf"; }
dl "Book2023_Coop-population-quantitative-genetics" \
   "https://github.com/cooplab/popgen-notes/releases/download/v1.2/release_popgen_notes.pdf"
dl "Book2019_Harmon-phylogenetic-comparative-methods" \
   "https://lukejharmon.github.io/pcm/pdf/phylogeneticComparativeMethods.pdf"
echo "done — see resources/books/INDEX.md for what their structure teaches"
