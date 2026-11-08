"""
Spyder Editor.

Created on Sat Nov  7 20:39:19 2026
@author: BRICE NELSON

Update file paths and run in terminal
"""

# to run from terminal add the commented section to the script

# python - <<'PY'
from pathlib import Path

files = [
    Path(
        "docs/02_engineering_documentation/01_engineering_background_outline.md"
    ),
    Path(
        "docs/02_engineering_documentation/02_engineering_background_foundation.md"
    ),
    Path("scripts/gitbash_lf_crlf_fix.py"),
]

for path in files:
    content = path.read_bytes()
    normalized = content.replace(b"\r\n", b"\n")
    if normalized != content:
        path.write_bytes(normalized)
        print(f"Converted: {path}")
    else:
        print(f"Already normalized: {path}")
# PY
