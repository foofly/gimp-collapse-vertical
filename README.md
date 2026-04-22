# GIMP Collapse Vertical Plugin

A GIMP Python-fu plugin that removes a selected horizontal strip from an image and closes the gap — useful for cropping out unwanted rows from screenshots, sprites, or layouts.

## What it does

Select a rectangular horizontal region, run the plugin, and GIMP will:

1. Delete the selected strip
2. Slide all content below it upward to fill the gap
3. Crop the canvas to the new height

## Installation

### Find your GIMP plug-ins folder

| Platform | Path |
|----------|------|
| Linux | `~/.config/GIMP/2.10/plug-ins/` |
| macOS | `~/Library/Application Support/GIMP/2.10/plug-ins/` |
| Windows | `%APPDATA%\GIMP\2.10\plug-ins\` |

> For GIMP 2.99 / 3.x, replace `2.10` with `2.99` or `3.0` in the paths above.

### Steps

1. Copy `fu.py` into your plug-ins folder.
2. On Linux/macOS, make it executable:
   ```bash
   chmod +x ~/.config/GIMP/2.10/plug-ins/fu.py
   ```
3. Restart GIMP (or use **Filters → Script-Fu → Refresh Scripts** if GIMP is already open).

### Linux Flatpak

If you installed GIMP via Flatpak, the plug-ins folder is sandboxed under your home directory:

```bash
mkdir -p ~/.var/app/org.gimp.GIMP/config/GIMP/2.10/plug-ins/
cp fu.py ~/.var/app/org.gimp.GIMP/config/GIMP/2.10/plug-ins/
chmod +x ~/.var/app/org.gimp.GIMP/config/GIMP/2.10/plug-ins/fu.py
```

For GIMP 3.x via Flatpak, replace `2.10` with `3.0`. You can check your version with:

```bash
flatpak info org.gimp.GIMP | grep version
```

## Usage

1. Open an image in GIMP.
2. Use the **Rectangle Select** tool to draw a selection across the horizontal strip you want to remove. The selection should span the full width of the area you want deleted (it doesn't need to span the full image width).
3. Go to **Filters → Custom → Collapse Vertical**.
4. The strip is removed and the image is cropped to fit.

The operation is fully undoable with **Edit → Undo** (Ctrl+Z).

## Requirements

- GIMP 2.10 or later with Python-fu support
- To verify Python-fu is available: **Filters → Script-Fu → Console** — if you also see **Filters → Python-Fu**, you're good to go.
