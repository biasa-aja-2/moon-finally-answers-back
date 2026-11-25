"""The Moon Finally Answers Back.

Writes the Moon's reply to /output/entry.txt: one line, 1 to 240
characters, in the voice of the Moon answering at last the wishes,
howls and late-night promises of everyone staring up at it.

Pure standard library only.
"""

import os

LINE = (
    "Four billion years of wishes, howls, and 2 a.m. promises "
    "\u2014 and not one of you has ever wished me a good night back."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
