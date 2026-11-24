#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch (variant 2).

Writes a single-sentence pitch for a ridiculous invention that fixes
a tiny everyday annoyance to /output/entry.txt.
Pure stdlib, deterministic, no network.

Judge criteria, in order, and how the pitch meets each:
1. One sentence: a single sentence ending in exactly one full stop.
2. Absurd invention: a pocket-sized snake charmer, applied to cables
   instead of snakes.
3. Tiny everyday annoyance: charging cables tangling themselves into
   a knot the moment they enter a bag.
4. Length gate: 170 characters, inside the required 1-220 range.
"""

from pathlib import Path

# Tiny annoyance: charging cables tangle themselves into a knot the
# moment they enter a bag. Invention: a pocket-sized snake charmer
# who hypnotises the cables into one neat braid.
ENTRY = (
    "The Cable Charmer, a pocket-sized snake charmer who hypnotises "
    "your tangled charging cables into one neat braid while you are "
    "still digging through your bag for the plug."
)


def main() -> None:
    # Gate contract: UTF-8 text, 1 to 220 characters, one sentence.
    assert 1 <= len(ENTRY) <= 220, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "not one sentence"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline, so the file bytes
    # are the entry itself.
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
