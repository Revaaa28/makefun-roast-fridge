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


def validate_line(line: str) -> None:
    """Gate the final entry before it is written.

    The competition is one line, one laugh: a single line of 1-200 UTF-8
    characters. Fail loudly instead of writing an entry that would be
    rejected or truncated — a newline, an empty string, or an overlong
    line means the build is broken, not the joke.
    """
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    n_chars = len(line.encode("utf-8"))
    if n_chars > 200:
        raise ValueError(f"entry line is {n_chars} UTF-8 chars, over the 200 limit")


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
