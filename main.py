"""Entry program: copy the pre-rendered front page to the output dir.

The image is a fixed, pre-rendered newspaper front page (entry.png).
The program just copies it into $MAKEFUN_OUTPUT_DIR, so the run is
byte-identical every time.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
