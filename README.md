<div align="center">
  <img src="/assets/icons/io.github.tanaybhomia.DeepDive.svg" alt="Deep Dive Icon" width="192" height="192"> 
  <h1>Deep Dive</h1>
  <p><strong>Submerge into Deep Focus</strong></p>

  <a href="https://flathub.org/apps/io.github.tanaybhomia.DeepDive">
    <img src="https://flathub.org/api/badge?svg&locale=en" alt="Download on Flathub" height="84">
  </a>
  <br><br>

  <a href="LICENSE"><img src="https://img.shields.io/badge/LICENSE-GPL--3.0-0AB3BB?labelColor=242424&style=flat-square" alt="License: GPLv3"></a>
  <a href="#"><img src="https://img.shields.io/badge/BUILD-PASSING-3CB32A?labelColor=242424&style=flat-square" alt="Build Status"></a>
  <a href="https://flathub.org/apps/io.github.tanaybhomia.DeepDive"><img src="https://img.shields.io/flathub/downloads/io.github.tanaybhomia.DeepDive?style=flat-square&logo=flathub&color=blue" alt="Flathub Downloads"></a>
  <br><br>

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/websiteimages/DarkMode/heroDark.png">
    <source media="(prefers-color-scheme: light)" srcset="docs/websiteimages/LightMode/heroLight.png">
    <img alt="Deep Dive Main Interface" src="docs/websiteimages/DarkMode/heroDark.png" style="max-width: 100%; height: auto;">
  </picture>
</div>

<br>

Deep Dive is a focused productivity application built natively for the GNOME desktop environment using GTK4 and Libadwaita. It goes beyond standard Pomodoro timers by introducing strict mechanisms designed to prevent cheating and enforce true deep work.

## Why Deep Dive?

Most pomodoro timers are just simple countdowns. Deep Dive is designed with the "Submerge" productivity philosophy in mind, stopping you from cheating yourself out of focus time.
- **Submerge Discipline**: The ultimate "commit or quit" setting. When activated, you cannot pause or skip a session. You must either finish the 25 minutes or hit "Give Up" to discard the entire session completely.
- **Seamless Distraction Blocking**: Deep Dive can automatically restrict access to distracting websites the second a Pomodoro starts, and instantly unblock them when you take a break.
- **Deep GNOME Integration**: Deep Dive feels at home on Linux. It automatically puts your desktop in Do Not Disturb mode when focusing and creates full-screen Break Overlays to physically force you away from the screen when it's time to rest.

## Core Features

- **Submerge Mode**: A strict, custom deep-sea themed mode where skipping and pausing are disabled, ensuring uninterrupted focus.
- **Break Overlays**: When a break starts, a fullscreen overlay forces you to stop working. It flawlessly supports multi-monitor setups and displays motivational quotes.
- **Compact Mini-Player**: Minimize the window into a sleek, floating mini-player that dynamically adapts to your Light/Dark system theme while you work.
- **Project Tracking**: Manage different projects from a dedicated Preferences tab and automatically log your focused time for each, backed by a local SQLite database.
- **Do Not Disturb Sync**: Automatically silences system notifications during focus sessions and restores them during breaks.

## Installation

Deep Dive is officially distributed through Flathub, making it easy to install on any Linux distribution.

```bash
flatpak install flathub io.github.tanaybhomia.DeepDive
```

## Contribution & Development

If you'd like to contribute to Deep Dive or build your own version, we have set up scripts to make local development frictionless.

### Local Testing
You do not need to install the app or compile it with Meson just to test Python code changes. Run the following command in the project root to instantly launch the app from the source code:
```bash
./run.sh
```

### Development Environment Setup
If you want to use the official Flathub release for your daily work, but also want a separate development version of Deep Dive in your app launcher for testing, run:
```bash
./install-dev.sh
```
This script creates a separate "Deep Dive (Development)" entry in your GNOME app grid. It uses a custom development icon and saves your test databases to a completely isolated folder, keeping your official Flatpak data safe. Any code changes you make in your IDE will instantly be reflected the next time you click the Development app icon.

## Architecture

Deep Dive follows the GNOME Human Interface Guidelines (HIG) perfectly. It utilizes native Libadwaita widgets, Adwaita preferences windows, and leverages Polkit for secure, password-less `/etc/hosts` manipulation.

## License

Deep Dive is free and open-source software licensed under the **GNU General Public License v3.0** (GPL-3.0). See the [LICENSE](LICENSE) file for more details.
