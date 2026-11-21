#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic, no network, no randomness.
"""

import os

TEXT = (
    "The light on this page left its star before the first river found "
    "the sea, and it has travelled ever since \u2014 patient, unhurried, "
    "in no hurry to arrive. Below it, a stone in a cold river has "
    "listened to the same water for a thousand years, and it is not "
    "tired yet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
