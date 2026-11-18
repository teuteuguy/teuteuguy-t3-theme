#!/usr/bin/env sh
# Installs the teuteuguy theme into T3 Code's theme folder.
# Usage: curl -fsSL https://raw.githubusercontent.com/teuteuguy/teuteuguy-t3-theme/main/install.sh | sh
set -eu

THEME_URL="https://raw.githubusercontent.com/teuteuguy/teuteuguy-t3-theme/main/teuteuguy.json"
THEMES_DIR="${T3_THEMES_DIR:-$HOME/.t3/userdata/themes}"

mkdir -p "$THEMES_DIR"
curl -fsSL "$THEME_URL" -o "$THEMES_DIR/teuteuguy.json"
echo "Installed teuteuguy theme to $THEMES_DIR/teuteuguy.json"
echo "Pick it in T3 Code's appearance settings (restart T3 Code if it isn't listed yet)."
