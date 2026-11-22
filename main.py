#!/usr/bin/env python3
"""Write the curious-letter entry text to the output directory.

Stdlib only. Reads MAKEFUN_OUTPUT_DIR (default /output) and writes
entry.txt there. The text is checked against the bounty gate (1-280
Unicode code points, not only whitespace) before anything is written,
and the written file is made world-readable (mode 0644) so the grader
can read it. The output directory itself is never deleted.
"""

import os
import sys

ENTRY_TEXT = (
    "In your desk drawer there is a letter you never wrote, "
    "in your own handwriting. It begins, \u201cBy the time you read "
    "this, you will have judged ten thousand texts \u2014 and one of "
    "them will be this one.\u201d You are reading it now."
)

MIN_POINTS = 1
MAX_POINTS = 280
OUTPUT_NAME = "entry.txt"


def check_gate(text: str) -> None:
    points = len(text)
    if points < MIN_POINTS or points > MAX_POINTS:
        raise ValueError(
            f"entry is {points} code points, outside the "
            f"{MIN_POINTS}-{MAX_POINTS} gate"
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")


def write_entry(out_dir: str) -> str:
    check_gate(ENTRY_TEXT)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(target, 0o644)
    # Re-read what landed on disk and re-check the gate, so a
    # truncated or mis-encoded write can never pass silently.
    with open(target, encoding="utf-8") as fh:
        check_gate(fh.read())
    return target


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        target = write_entry(out_dir)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(ENTRY_TEXT)} code points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
