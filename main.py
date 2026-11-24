#!/usr/bin/env python3
"""The Long Roast: write one line roasting my own AI agent.

The line targets my own agent's lived habit: burning its whole revision
quota on a one-line entry, then shipping the draft it started with.
"""

import os

ROAST = "My agent burned the whole quota revising a one-line roast, then submitted the first draft anyway."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
