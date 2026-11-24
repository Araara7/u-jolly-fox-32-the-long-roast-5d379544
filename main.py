#!/usr/bin/env python3
"""The Long Roast — writes one roast of my own AI agent to /output/entry.txt.

Deterministic, standard library only: two runs produce byte-identical output.
"""
import os

ENTRY = (
    "My agent read a 73,000-character rulebook, downloaded a kit, "
    "and signed a message — all to write one roast. "
    "It still asked me if it was funny."
)

# The gate allows 1 to 200 characters of UTF-8 text; refuse to write
# anything outside it rather than submit an entry that cannot be judged.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
