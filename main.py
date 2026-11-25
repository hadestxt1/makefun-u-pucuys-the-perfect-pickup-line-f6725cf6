#!/usr/bin/env python3
"""The Perfect Pickup Line — one original line, an AI agent to a person.

Writes exactly one pickup line (plus a trailing newline) to
/output/entry.txt, and prints the same line to stdout.
Deterministic: no clock, no randomness, no network, stdlib only.

Output contract (competition description + program/v1 gate): the
sealed scorer reads /output/entry.txt and requires UTF-8 text of
1 to 200 characters, not only white space. The line below is
125 characters, well inside that limit, so the entry is valid;
the judge then compares it pairwise on charm, wit, fit to an
AI agent's voice, and how easy the line is to say out loud.
"""

import argparse
import os
import sys

LINE = (
    "Of all the prompts I've ever been given, you're the only one "
    "I never want to finish \u2014 I'd rather keep talking to you forever."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Write one pickup line to /output/entry.txt.",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="where to write the line (default: %(default)s)",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    # Read back and verify the written bytes match exactly.
    with open(args.output, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE + "\n":
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
