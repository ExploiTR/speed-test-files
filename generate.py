#!/usr/bin/env python3
"""Write random binary files for internet speed tests.

Creates ``2**n`` MiB files for ``n`` starting at 3, while the size is at most
2048 MiB: 8MB.bin, 16MB.bin, ..., 1GB.bin, 2GB.bin. Each file is filled with
``os.urandom`` in fixed-size chunks so resident memory stays small.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

MIB = 1024 * 1024
# 1 MiB keeps the write buffer small relative to the multi-gigabyte outputs.
CHUNK_BYTES = 1 * MIB
MIN_EXPONENT = 3  # 2**3 MiB == 8 MiB
MAX_MIB = 2048


def filename_for(size_mib: int) -> str:
    if size_mib >= 1024 and size_mib % 1024 == 0:
        return f"{size_mib // 1024}GB.bin"
    return f"{size_mib}MB.bin"


def planned_files() -> list[tuple[str, int]]:
    files: list[tuple[str, int]] = []
    size_mib = 1 << MIN_EXPONENT
    while size_mib <= MAX_MIB:
        files.append((filename_for(size_mib), size_mib * MIB))
        size_mib *= 2
    return files


def write_random_file(path: Path, size_bytes: int) -> None:
    written = 0
    with path.open("wb") as handle:
        while written < size_bytes:
            chunk = min(CHUNK_BYTES, size_bytes - written)
            handle.write(os.urandom(chunk))
            written += chunk
            if written % (64 * MIB) == 0 or written == size_bytes:
                print(f"  {path.name}: {written}/{size_bytes} bytes", flush=True)


def main() -> int:
    root = Path(__file__).resolve().parent
    for name, size_bytes in planned_files():
        path = root / name
        if path.is_file() and path.stat().st_size == size_bytes:
            print(f"skip {name} ({size_bytes} bytes)", flush=True)
            continue
        print(f"writing {name} ({size_bytes} bytes)", flush=True)
        partial = path.with_suffix(path.suffix + ".partial")
        write_random_file(partial, size_bytes)
        partial.replace(path)
        actual = path.stat().st_size
        if actual != size_bytes:
            print(f"error: {name} is {actual} bytes, expected {size_bytes}", file=sys.stderr)
            return 1
        print(f"done {name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
