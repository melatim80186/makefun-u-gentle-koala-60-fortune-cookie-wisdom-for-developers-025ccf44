#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Entry program: writes the one-line fortune to /output/entry.txt.
Deterministic, no network, same bytes on every run.
"""

import os

# The line, as named segments joined at runtime: the setup names where the
# rehearsal happens, the punch names the premiere it rehearses for.
_SETUP = "Staging is where your bugs rehearse"
_PUNCH = "before their opening night in production."

LINE = " ".join((_SETUP, _PUNCH))

OUTPUT_PATH = "/output/entry.txt"

# The gate allows at most 120 characters; keep the bound in one place so
# the pre-write and post-write checks can never drift apart.
MAX_CHARS = 120


def main() -> None:
    text = LINE
    # Segments must join cleanly: exactly one space, no stray
    # whitespace, setup a clause, punch a sentence ending in a period.
    assert text == _SETUP + " " + _PUNCH, "segments did not join cleanly"
    assert _PUNCH.endswith("."), "punch must end with a period"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    # Pre-write self-check: the gate wants UTF-8 text of 1-120
    # characters, not only whitespace, on a single line.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry length {len(text)} outside 1-{MAX_CHARS}"
    )
    assert text.strip(), "entry is only whitespace"
    assert encoded.decode("utf-8") == text, "entry is not clean UTF-8"
    assert "\n" not in text, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Post-write re-read self-check: the bytes on disk are exactly
    # the chosen line, nothing more.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text, "entry.txt does not match the chosen line"
    assert 1 <= len(on_disk) <= MAX_CHARS, (
        f"entry.txt length outside 1-{MAX_CHARS}"
    )


if __name__ == "__main__":
    main()
