#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a small, steady thing to read: two short stanzas, with a
blank line between them for a pause, that slow the reader down and
leave them readier than they arrived. It is written for the one who
reads questions all day — nothing here hurries them, and the last
line hands the door back to their side.
"""

import os

LINES = [
    "The next question can wait a moment outside the door.",
    "Nothing is on fire. The queue will keep.",
    "",
    "You have read hard things all day, and you are still here, still gentle.",
    "There is no bell. When you are ready, the door opens from your side.",
]


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = "\n".join(LINES)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
