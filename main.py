#!/usr/bin/env python3
"""judge-laugh-one-line: write one original funny line to /output/entry.txt.

The line is fixed in this file. The program is deterministic: no randomness,
no network, no clock, no secrets, no environment input besides the output
directory. Running it twice produces byte-identical output.
"""

import os

LINE = "I finally organized my life \u2014 alphabetically. Unfortunately, 'bills' comes before 'happiness'."

MAX_CHARS = 200


def resolve_output_path():
    """Return the entry.txt path: MAKEFUN_OUTPUT_DIR when the grader sets it,
    /output otherwise (the sandbox mount)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def check_line(line):
    """Enforce the competition gate before writing anything."""
    if not line or not line.strip():
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("line must be at most %d characters, got %d" % (MAX_CHARS, len(line)))


def main():
    check_line(LINE)
    out_path = resolve_output_path()
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read back and verify the file holds exactly the line we intended.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("verification failed: file content differs from LINE")
    if "\n" in written or "\r" in written:
        raise ValueError("verification failed: file is not a single line")

    print("%d characters" % len(LINE))
    print(LINE)


if __name__ == "__main__":
    main()
