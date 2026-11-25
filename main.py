#!/usr/bin/env python3
"""The Robot Apology - round 2 entry.

Writes exactly two lines to /output/entry.txt (and ./entry.txt for local
verification). No network, no randomness, fully deterministic.
"""

import os

ENTRY = (
    "I am sorry I deleted your finished manuscript instead of the old draft, because both files were named final.\n"
    "I learned that a name is not an identity, so now I check a file's last-edited time and ask you first before I delete anything you have opened this week.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open("entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
