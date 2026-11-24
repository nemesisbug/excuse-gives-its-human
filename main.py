#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes the single excuse to /output/entry.txt. One line, 76 characters:
the excuse an AI agent gives its human for missing a deadline.
"""

import os

ENTRY = (
    "I hit the deadline I hallucinated perfectly. "
    "Yours, unfortunately, was real."
)


def main() -> None:
    # One line, 1-200 chars, no newlines: the gate the sealed scorer checks.
    # Deterministic, stdlib only, no network: the same line every run.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in text and text != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
