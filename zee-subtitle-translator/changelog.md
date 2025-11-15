# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Nothing yet.

---

## [1.0.0] - 2025-11-15

### Added
- Global command `zeetranslator` - run from any directory
- Automatic shell configuration for Linux/macOS
- Windows global command support via WindowsApps directory
- Android Termux setup script with storage location choice
- Android storage shortcuts (downloads, movies, dcim)
- Termux widget support for quick launch
- Uninstaller script (uninstall.sh) for clean removal
- ANDROID_STORAGE_GUIDE.md - detailed Android storage explanation
- CONTRIBUTING.md guide for contributors
- Proper .gitignore file
- This CHANGELOG file

### Changed
- Fixed installer.sh to properly install Python dependencies
- Updated README.md with uninstall section and Android instructions
- Improved installer scripts with auto-reload and command testing
- Enhanced Android/Termux setup with storage location choice
- Updated all documentation to reference correct filenames

### Fixed
- installer.sh missing `pip install` command
- Windows batch file not creating global command properly
- Android storage access permission workflow
- Command not immediately available after installation (now auto-reloads)
- Termux installation location issue (now asks user preference)


### Features

**Translation Engines:**
- Google Translate (free, 100+ languages)
- DeepL API support (premium quality)

**Processing Modes:**
- Safe: Line-by-line translation (most reliable)
- Standard: 50-line batches (recommended)
- Aggressive: 100-line batches (fastest)

**File Management:**
- Single folder translation
- Multiple folder selection
- ZIP file support
- Recursive subdirectory scanning
- Custom output folder naming
- Preserve or merge folder structures

**Smart Features:**
- Automatic encoding detection (UTF-8, Latin-1, etc.)
- Proper name preservation (McDonald, New York, etc.)
- Tag removal ([MUSIC], (SOUND), HTML tags, notes)
- Duplicate file skip detection
- Error logging to error_log.txt
- Resume capability (skip existing translations)

**User Experience:**
- Color-coded terminal output
- Progress bars with tracking
- Detailed summary statistics
- Overwrite confirmation prompts
- Cancel operation support (Ctrl+C)
- Bilingual interface (English/Indonesian)

**Platform Support:**
- Linux (Ubuntu, Debian, Arch, etc.)
- macOS (Intel and Apple Silicon)
- Windows (10/11, PowerShell/CMD)
- Android (via Termux)

**Documentation:**
- Comprehensive README.md
- Quick start guide (QUICKSTART.md)
- Detailed usage guide (GUIDE.md)
- FAQ document (FAQ.md)
- Indonesian installation tutorial

**Format Support:**
- SRT (SubRip)
- VTT (WebVTT)
- ASS (Advanced SubStation Alpha)

---

## Version History

### Versioning Scheme

Given a version number MAJOR.MINOR.PATCH:

- MAJOR: Incompatible API changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

---

```

No breaking changes. All v1.0.0 commands still work. The `zeetranslator` global command is a new addition.

---

## Support

### Documentation
- [README](README.md)
- [FAQ](FAQ.md)
- [Usage Guide](GUIDE.md)

### Issues
- [Report Bug](https://github.com/zeewank/zee-subtitle-translator/issues)
- [Request Feature](https://github.com/zeewank/zee-subtitle-translator/issues)

### Donate
- PayPal: https://paypal.me/zeewank
- Trakteer: https://trakteer.id/zeewank/tip

---

