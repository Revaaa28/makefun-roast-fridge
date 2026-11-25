#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — make.fun entry program.

Writes a single roast line to /output/entry.txt.

The line was chosen by manual ranking of 10 candidates against the judge brief
in the kit (specific recognisable detail first, twist paying off in the last
words, fresh rather than a worn-out fridge joke). See candidates.md in the
build workspace for the full candidate list and the pairwise reasoning.

Deterministic: the same bytes on every run, no network, no randomness,
no input files, no environment secrets.
"""

import os

LINE = (
    "My fridge's ice maker sounds like a dying robot clearing its throat "
    "at 3 a.m., then drops exactly one cube, like it's doing me a favour."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
