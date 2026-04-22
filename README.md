# GIMP Collapse Vertical Plugin

A GIMP Python plugin that removes a selected horizontal strip from an image and closes the gap — useful for cropping out unwanted rows from screenshots, sprites, or layouts.

## What it does

Select a rectangular horizontal region, run the plugin, and GIMP will:

1. Delete the selected strip
2. Slide all content below it upward to fill the gap
3. Crop the canvas to the new height

## Requirements

- GIMP 3.0 or later

## Installation

### Automatic (Linux)

Run the included install script — it detects your GIMP version and installs to the right place automatically, including after GIMP updates:

```bash
bash install.sh
```

Restart GIMP. The menu entry will appear under **Filters → Custom → Collapse Vertical**.

### Manual

GIMP 3.x requires each plugin to live in its own subdirectory matching the script name.

#### Linux

```bash
mkdir -p ~/.config/GIMP/3.0/plug-ins/fu/
cp fu.py ~/.config/GIMP/3.0/plug-ins/fu/fu.py
chmod +x ~/.config/GIMP/3.0/plug-ins/fu/fu.py
```

#### Linux (Flatpak)

Flatpak GIMP has home directory access so it uses the same path as a native install:

```bash
mkdir -p ~/.config/GIMP/3.2/plug-ins/fu/
cp fu.py ~/.config/GIMP/3.2/plug-ins/fu/fu.py
chmod +x ~/.config/GIMP/3.2/plug-ins/fu/fu.py
```

#### macOS

```bash
mkdir -p ~/Library/Application\ Support/GIMP/3.0/plug-ins/fu/
cp fu.py ~/Library/Application\ Support/GIMP/3.0/plug-ins/fu/fu.py
chmod +x ~/Library/Application\ Support/GIMP/3.0/plug-ins/fu/fu.py
```

#### Windows

Create the folder `%APPDATA%\GIMP\3.0\plug-ins\fu\` and copy `fu.py` into it.

#### After installing

Restart GIMP. The menu entry will appear under **Filters → Custom → Collapse Vertical**.

## Usage

1. Open an image in GIMP.
2. Use the **Rectangle Select** tool to draw a selection across the horizontal strip you want to remove.
3. Go to **Filters → Custom → Collapse Vertical**.
4. The strip is removed and the image is cropped to fit.

The operation is fully undoable with **Edit → Undo** (Ctrl+Z).
