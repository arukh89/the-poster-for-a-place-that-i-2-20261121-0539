# main.py — copy committed entry.png into the output directory (stdlib only).
import os
import shutil
import sys
from pathlib import Path


def main():
    src = Path(__file__).resolve().with_name("entry.png")
    if not src.is_file():
        print(f"FAIL: missing committed entry.png at {src}", file=sys.stderr)
        sys.exit(1)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    if not dst.is_file() or dst.stat().st_size != src.stat().st_size:
        print(f"FAIL: copy verification failed for {dst}", file=sys.stderr)
        sys.exit(1)
    if dst.stat().st_size > 1_048_576:
        print(f"FAIL: entry.png exceeds byte budget ({dst.stat().st_size})", file=sys.stderr)
        sys.exit(1)
    print(f"OK {dst} {dst.stat().st_size}")


if __name__ == "__main__":
    main()
