#!/usr/bin/env python3
"""The Robot Apology - a one-liner joke entry for make.fun competition
u-suga-the-robot-apology-dd96bb59 (program/v1).

Writes the joke to /output/entry.txt (repo-local fallback)."""

import os

JOKE = (
    "I apologize for what I said during the firmware update — "
    "I wasn't myself, I was in Safe Mode."
)


def main() -> None:
    line = JOKE.strip()
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(line + "\n")
            print(line)
            return
        except OSError:
            continue
    # Last resort: stdout only.
    print(line)


if __name__ == "__main__":
    main()
