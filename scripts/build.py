#!/usr/bin/env python3
"""Build teuteuguy.json (the installable T3 Code theme file) from src/.

src/palette.json  -> name, appearance, colour roles (Tokyo Night / Tokyo Night Light)
src/teuteuguy.css -> the structural CSS (framed tiles, folder frames, thread states)
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
theme = json.loads((root / "src" / "palette.json").read_text())
css = (root / "src" / "teuteuguy.css").read_text()
if len(css) > 50_000:
    raise SystemExit(f"CSS is {len(css)} chars; T3 Code allows 50,000.")
theme["css"] = css
(root / "teuteuguy.json").write_text(json.dumps(theme, indent=2) + "\n")
print(f"wrote teuteuguy.json ({len(css)} chars of CSS)")
