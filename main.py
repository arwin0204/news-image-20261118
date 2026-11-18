"""Entry program: copy the pre-rendered front page to the output dir.

The image is a fixed, pre-rendered newspaper front page (entry.png).
The program just copies it into $MAKEFUN_OUTPUT_DIR, so the run is
byte-identical every time.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png is missing next to main.py", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
