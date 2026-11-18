# teuteuguy — a T3 Code theme

A theme for [T3 Code](https://t3.codes) that turns the thread list into framed, translucent tiles which show what each thread is doing at a glance.

## Credits and inspiration

This theme stands on other people's work, and says so:

- **Colours: [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme)** by enkia. The palette is a T3 Code port of Tokyo Night (dark) and Tokyo Night Light (light), used as-is. The state colours (green, amber, purple, red, cyan) are Tokyo Night's accent colours too.
- **Look and feel: screenshots by [@MADshadowman](https://x.com/MADshadowman) on X**, who shared a Cyberpunk-styled T3 Code UI. The framed tiles, the cut corners, the corner squares and the see-through panels in this theme are modelled on those screenshots. The colours are not.

## What it does

- **Framed thread tiles.** Every thread in the sidebar sits in a thin frame with a cut bottom-right corner and a small square in the top-left corner. The fill is translucent over a barely visible grid.
- **Thread state in the tile.** The tile colour follows the status T3 Code shows on the row:

  | Status in T3 Code | Tile |
  | --- | --- |
  | Working, Setting up, Goal | Blue-violet gradient rotating around the frame |
  | Done (finished since you last opened it) | Green tint and green frame |
  | Approval, Limited, Woke | Amber |
  | Input, Request | Purple |
  | Failed | Red |
  | Waiting | Slightly lighter fill |

  "Done" is T3 Code's *unread* marker. It goes away once you open the thread, and the tile goes back to neutral with it.
- **Project folders as containers.** In the folder view, a project and its threads are drawn as one frame, with the threads as smaller tiles inside it. A collapsed folder is a closed box.
- **The open thread** is outlined in the accent blue.
- **Light and dark.** The theme carries both palettes and follows T3 Code's light/dark setting.

Only the sidebar's structure changes. Chat, terminal and code colours are plain Tokyo Night.

## Install

T3 Code has no "install from URL" button. Themes are JSON files in `~/.t3/userdata/themes/`. There are two ways to get this one there.

### Option 1: one command

```sh
curl -fsSL https://raw.githubusercontent.com/teuteuguy/teuteuguy-t3-theme/main/install.sh | sh
```

This downloads [`teuteuguy.json`](teuteuguy.json) into `~/.t3/userdata/themes/`. Set `T3_THEMES_DIR` first if your T3 Code data lives elsewhere. Then pick **teuteuguy** in T3 Code's appearance settings, restarting T3 Code if it isn't listed yet.

### Option 2: ask T3 Code

In a T3 Code thread with full access, paste:

> Install and switch to the T3 Code theme at https://raw.githubusercontent.com/teuteuguy/teuteuguy-t3-theme/main/teuteuguy.json, using its id `teuteuguy`.

The agent reads the file and applies it with T3 Code's own theme tool.

### Uninstall

Switch back to a built-in theme in the appearance settings, then delete `~/.t3/userdata/themes/teuteuguy.json`.

## Editing the theme

| File | What it holds |
| --- | --- |
| [`src/palette.json`](src/palette.json) | Name, appearance and colour roles (Tokyo Night / Tokyo Night Light) |
| [`src/teuteuguy.css`](src/teuteuguy.css) | All the structural CSS: tiles, folder frames, state colours |
| [`teuteuguy.json`](teuteuguy.json) | The built, installable theme file. Don't edit it by hand |

After editing anything in `src/`, rebuild:

```sh
python3 scripts/build.py
```

The CSS keys off T3 Code's stable `data-*` attributes and the status pill's colour classes. A T3 Code update that renames those can break the state colours, while the frames and palette keep working.

## Licence

MIT. See [LICENSE](LICENSE). Tokyo Night is © enkia, also under MIT.
