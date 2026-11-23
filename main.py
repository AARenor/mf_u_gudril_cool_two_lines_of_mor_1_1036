"""Write the two-line micro poem for make.fun bounty u-gudril-cool-two-lines-of-morning-light-ade94fc5."""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)


def resolve_output_dir() -> Path:
    """Return the folder the entry text is written into."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
