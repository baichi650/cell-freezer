"""Windows launcher for freezer-1.3.

This script is designed to be packaged with PyInstaller as a single-file EXE.
It opens the bundled `freezer-1.3.html` (or `index.html`) in the default browser
and exits immediately.
"""

from __future__ import annotations

import sys
import webbrowser
from pathlib import Path


def _bundle_dir() -> Path:
    # PyInstaller onefile extracts bundled files into sys._MEIPASS.
    if hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"))
    return Path(__file__).resolve().parent


def _resolve_entry(base: Path) -> Path:
    primary = base / "freezer-1.3.html"
    fallback = base / "index.html"
    if primary.exists():
        return primary
    if fallback.exists():
        return fallback
    raise FileNotFoundError("Neither freezer-1.3.html nor index.html was found in bundle.")


def main() -> int:
    base = _bundle_dir()
    entry = _resolve_entry(base)
    webbrowser.open(entry.as_uri(), new=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
