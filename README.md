# 🌐 Zee Subtitle Translator

A command-line tool for batch translating subtitle files with support for multiple engines and formats.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Android-lightgrey.svg)]()

## Features

- **Multiple translation engines:** Google Translate (free), DeepL API, and ChatGPT API
- Batch processing for multiple files and folders
- Interactive file browser with multi-folder selection
- Automatic text cleaning (removes tags like [MUSIC], (SOUND), etc.)
- Custom credits option for translated subtitles
- Real-time progress tracking and detailed reports
- Support for SRT, VTT, and ASS subtitle formats
- Smart encoding detection and proper name preservation
- Three speed modes: Safe, Standard, and Aggressive
- Bilingual interface (English and Indonesian)
- Global command - run from anywhere

## Requirements

- Python 3.7 or higher (auto-installed if not present on Windows)
- Internet connection for downloading and translation


## Documentation

- [Quick Start Guide](QUICKSTART.md) - 5-minute tutorial
- [Detailed Usage Guide](GUIDE.md) - All features explained
- [FAQ](FAQ.md) - Common questions and answers
- [Install from ZIP](INSTALL_FROM_ZIP.md) - Manual installation guide 
- [Fix Bootstrap Errors](FIX_BOOTSTRAP_ERRORS.md) - Troubleshooting 
- [Android Storage Guide](ANDROID_STORAGE_GUIDE.md) - Termux storage explanation

---

## Platform-Specific Notes

### Linux
- Tested on Ubuntu, Debian, Arch, Fedora
- Requires `curl` or `wget` and `unzip`
- Global command works in bash and zsh

### macOS
- Works on Intel and Apple Silicon
- Requires Homebrew for easy Python installation
- Use `python3` command

### Windows
- Windows 10/11 recommended
- PowerShell gives best experience
- Command Prompt also supported
- Python auto-installs if missing

### Android (Termux)
- **Must use F-Droid or GitHub version**
- Google Play Store version is broken
- Install to Shared Storage for file manager access
- Widget support for quick launch
- Storage shortcuts created automatically

---

## Acknowledgments

- [deep-translator](https://github.com/nidhaloff/deep-translator) - Translation API wrapper
- [pysrt](https://github.com/byroot/pysrt) - SRT file parsing
- [pysubs2](https://github.com/tkarabela/pysubs2) - ASS/SSA subtitle support
- [tqdm](https://github.com/tqdm/tqdm) - Progress bars
- [OpenAI](https://openai.com) - ChatGPT API

---

## Links

- [Report Bug](https://github.com/zeewank/zee-subtitle-translator/issues)
- [Request Feature](https://github.com/zeewank/zee-subtitle-translator/issues)
- [Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions)
- [Releases](https://github.com/zeewank/zee-subtitle-translator/releases)

---

## Screenshots

<img width="407" height="241" alt="Screenshot at 2025-11-11 15-52-56" src="https://github.com/user-attachments/assets/901a0e66-c335-46d8-bfb9-0ecabdb8dc8f" />

<img width="959" height="584" alt="Screenshot at 2025-11-11 15-58-22" src="https://github.com/user-attachments/assets/4c19f825-7152-4141-a885-900aad70d053" />




⭐ Star this repo if you find it helpful
