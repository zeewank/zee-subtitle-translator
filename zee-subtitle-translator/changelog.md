# Changelog

All notable changes to this project will be documented in this file.



## [Unreleased]

Nothing yet.

---

## [1.0.0] - 2025-13-11

Initial release.

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

## Migration Guide



**Linux/macOS:**
```bash
cd zee-subtitle-translator
git pull origin main
./installer.sh
```

**Windows:**
```cmd
cd zee-subtitle-translator
git pull origin main
install_windows.bat
```

**Android:**
```bash
cd zee-subtitle-translator
git pull origin main
./setup_termux.sh
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
