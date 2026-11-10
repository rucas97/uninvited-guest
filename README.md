# The Uninvited Guest (مهمان ناخوانده)

A choice-driven narrative game for Cafe Bazaar.

## About

You are hosting a dinner party. The guests keep arriving. Survive the evening by balancing **Reputation (آبرو)** and **Blood Pressure (فشار خون)**.

## Tech Stack

- **Engine:** Ren'Py
- **Ad SDK:** Tapsell
- **Build:** GitHub Actions → Signed APK → Cafe Bazaar

## Project Structure

    game/           → Ren'Py game files
      images/       → Characters, backgrounds, UI
      audio/        → Sound effects and music
      script.rpy    → Main dialogue and logic
    .github/        → CI/CD workflows

## Development Setup

1. Install Ren'Py SDK
2. Clone this repo
3. Open the folder in Ren'Py Launcher
4. Run the game

## Build

Push a tag to trigger the GitHub Actions build:

    git tag v0.1.0
    git push origin v0.1.0

The signed APK will appear in the GitHub Actions artifacts.

## License

MIT
