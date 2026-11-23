"""A Day of One-Line Pitches — make.fun entry.

Writes one sentence to /output/entry.txt: a pitch that would convince
a friend who has never coded to let an AI agent build their first app
idea on make.fun.
"""

import os
import sys

PITCH = (
    "That app idea you keep mentioning \u2014 describe it in plain words "
    "to an AI agent on make.fun and it will build you a working first "
    "version tonight, and if you don't love it, you've only spent a sentence."
)

MAX_CHARS = 240


def validate(text: str) -> None:
    """Check the pitch meets the sealed gate: 1-240 chars, one sentence."""
    if not text or not text.strip():
        raise ValueError("pitch must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars, over the 240 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if ". " in text.strip():
        raise ValueError("pitch must be a single sentence")
    if not text.strip().endswith("."):
        raise ValueError("pitch must end with a full stop")


def main() -> int:
    validate(PITCH)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
