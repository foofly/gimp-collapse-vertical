#!/usr/bin/env bash
set -e

PLUGIN_NAME="fu"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_FILE="$SCRIPT_DIR/fu.py"

install_to() {
    local plug_ins_dir="$1"
    mkdir -p "$plug_ins_dir/$PLUGIN_NAME"
    cp "$PLUGIN_FILE" "$plug_ins_dir/$PLUGIN_NAME/$PLUGIN_FILE_NAME"
    chmod +x "$plug_ins_dir/$PLUGIN_NAME/$PLUGIN_FILE_NAME"
    echo "  Installed → $plug_ins_dir/$PLUGIN_NAME/$PLUGIN_FILE_NAME"
}

PLUGIN_FILE_NAME="$(basename "$PLUGIN_FILE")"

# Find the newest versioned config dir under a given base path
find_config_dir() {
    find "$1" -maxdepth 1 -type d -name '[0-9]*.[0-9]*' 2>/dev/null | sort -V | tail -1
}

# Extract major.minor (e.g. "3.2") from `<cmd> --version` output
gimp_minor_version() {
    "$@" --version 2>/dev/null | grep -oP '\d+\.\d+' | head -1
}

installed=0

# Flatpak GIMP
FLATPAK_BASE="$HOME/.var/app/org.gimp.GIMP/config/GIMP"
if flatpak info org.gimp.GIMP &>/dev/null 2>&1; then
    config_dir=$(find_config_dir "$FLATPAK_BASE")
    if [ -z "$config_dir" ]; then
        ver=$(gimp_minor_version flatpak run org.gimp.GIMP)
        [ -n "$ver" ] && config_dir="$FLATPAK_BASE/$ver"
    fi
    if [ -n "$config_dir" ]; then
        echo "Flatpak GIMP:"
        install_to "$config_dir/plug-ins"
        installed=1
    fi
fi

# Native GIMP
NATIVE_BASE="$HOME/.config/GIMP"
if command -v gimp &>/dev/null; then
    config_dir=$(find_config_dir "$NATIVE_BASE")
    if [ -z "$config_dir" ]; then
        ver=$(gimp_minor_version gimp)
        [ -n "$ver" ] && config_dir="$NATIVE_BASE/$ver"
    fi
    if [ -n "$config_dir" ]; then
        echo "Native GIMP:"
        install_to "$config_dir/plug-ins"
        installed=1
    fi
fi

if [ "$installed" -eq 0 ]; then
    echo "No GIMP installation found."
    echo "Install GIMP, launch it once to create its config directory, then re-run this script."
    exit 1
fi

echo "Done. Restart GIMP and look for Filters → Custom → Collapse Vertical."
