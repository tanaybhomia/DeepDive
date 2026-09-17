#!/bin/bash

echo "Setting up Deep Dive (Development) environment..."

APP_ID="io.github.tanaybhomia.DeepDive.Devel"
PROJECT_DIR="$(pwd)"
DESKTOP_FILE="$HOME/.local/share/applications/$APP_ID.desktop"
ICON_DIR="$HOME/.local/share/icons/hicolor/scalable/apps"

mkdir -p "$ICON_DIR"
cp "assets/icons/$APP_ID.svg" "$ICON_DIR/"

cat << DESKTOP > "$DESKTOP_FILE"
[Desktop Entry]
Name=Deep Dive (Development)
Comment=Submerge into Deep Focus
Exec=env DEEPDIVE_DEVEL=1 python3 "$PROJECT_DIR/main.py"
Icon=$APP_ID
Terminal=false
Type=Application
Categories=Utility;Productivity;
StartupNotify=true
DESKTOP

update-desktop-database "$HOME/.local/share/applications" || true
gtk-update-icon-cache "$HOME/.local/share/icons/hicolor" -t || true

echo "Development environment installed! You can now launch 'Deep Dive (Development)' from your app grid."
echo "Note: Test data will be safely isolated in ~/.local/share/deepdive-devel"
