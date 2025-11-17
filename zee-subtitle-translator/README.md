# Zee Subtitle Translator

A command-line tool for batch translating subtitle files with support for multiple engines and formats.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Android-lightgrey.svg)]()

## Features

- Multiple translation engines: Google Translate (free) and DeepL API
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

- Python 3.7 or higher (auto-installed if not present)
- Internet connection for downloading and translation

**No manual downloads needed!** Just run one command.

## ⚡ Quick Install (One-Line)

### Linux / macOS

**Easiest way** - Copy and paste this into your terminal:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

Or with wget:

```bash
wget -qO- https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

### Windows

**Easiest way** - Open PowerShell (right-click Start → Windows PowerShell) and paste:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

Or **Command Prompt**:

```cmd
curl -o "%TEMP%\zee-install.bat" https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat && "%TEMP%\zee-install.bat"
```

### Android (Termux)

**Important:** Install Termux from [F-Droid](https://f-droid.org/packages/com.termux/) or [GitHub](https://github.com/termux/termux-app/releases), **NOT** Google Play Store.

**Easiest way** - Open Termux and paste:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

## What Happens During Installation?

The auto-installer will:

1. ✅ Check/install Python (if needed)
2. ✅ Download project from GitHub
3. ✅ Extract all files
4. ✅ Install Python dependencies
5. ✅ Set up global `zeetranslator` command
6. ✅ Create shortcuts (Android only)
7. ✅ Create Termux widget (Android only)

**Total time:** 2-5 minutes depending on your connection.

**No git required!** Everything downloads automatically.

## Usage

After installation, simply run:

```bash
zeetranslator
```

**That's it!** The program will guide you through the rest.

### With Specific Path

```bash
# Linux/macOS
zeetranslator ~/Videos/Subtitles/

# Windows
zeetranslator "C:\Users\YourName\Videos\Subtitles"

# Android
zeetranslator ~/downloads/Subtitles/
```

### If Global Command Doesn't Work

**Linux/macOS/Android:**
```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
# Then try again: zeetranslator
```

**Windows:**
Restart Command Prompt or PowerShell, then try again.

## Manual Installation (Alternative)

If the one-line installer doesn't work, you can install manually:

### Linux / macOS / Android

```bash
# 1. Download bootstrap script
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh

# 2. Make executable
chmod +x installer.sh

# 3. Run
./installer.sh
```

### Windows

```cmd
REM 1. Download bootstrap script
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat

REM 2. Run
install_windows.bat
```

## Translation Modes

| Mode | Speed | Best For |
|------|-------|----------|
| Safe | Slow | Important content, complex formatting |
| Standard | Fast | General use (recommended) |
| Aggressive | Very Fast | Large batches with stable connection |

## Multiple Folder Selection

When browsing folders, use these commands:

| Command | Action |
|---------|--------|
| `14` | Open folder 14 |
| `s14` | Select folder 14 without opening |
| `u1` | Unselect folder 1 from selection |
| `.` | Select current folder |
| `0` | Finish selection and proceed |
| `q` | Cancel and return to menu |

## Examples

**Quick translation:**
```bash
zeetranslator
# Follow prompts: choose engine, browse folder, select files, translate
```

**Direct folder translation:**
```bash
zeetranslator ~/Videos/BreakingBad/Season1/
```

**Multiple seasons:**
```bash
zeetranslator
# Select: Multiple folders
# Type: s5 (Season 1), s6 (Season 2), s7 (Season 3), 0 (start)
```

## Configuration

### DeepL API (Optional)

For better translation quality, get a free API key from [DeepL](https://www.deepl.com/pro-api).

**Linux/macOS/Android:**
```bash
echo 'export DEEPL_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Windows:**
```cmd
setx DEEPL_API_KEY "your-api-key-here"
```

## Output Format

Translated files use language code suffix:
```
movie.srt → movie.id.srt
episode.vtt → episode.id.vtt
subtitle.ass → subtitle.id.ass
```

## Troubleshooting

### Installation Failed

**Linux/macOS:**
```bash
# If curl fails, try wget:
wget -qO- https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash

# Or download manually:
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh
chmod +x installer.sh
./installer.sh
```

**Windows:**
```powershell
# If PowerShell fails, download manually:
# 1. Go to: https://github.com/zeewank/zee-subtitle-translator/releases
# 2. Download install_windows.bat
# 3. Double-click to run
```

**Android:**
```bash
# Update Termux first:
pkg update -y && pkg upgrade -y

# Then try again:
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

### Command Not Found

**Linux/macOS:**
```bash
source ~/.bashrc  # or ~/.zshrc
```

**Windows:**
Restart Command Prompt

**Android:**
```bash
source ~/.bashrc
```

### Slow Translation

- Use WiFi instead of mobile data
- Try Safe mode for better stability
- Translate during off-peak hours
- Check internet connection speed

### Permission Denied

**Linux/macOS/Android:**
```bash
chmod +x zee_translator.py
```

**Windows:**
Run Command Prompt as Administrator

### Missing Dependencies

```bash
pip install --force-reinstall -r requirements.txt
```

## Uninstall

To completely remove Zee Subtitle Translator:

**Linux/macOS/Android:**
```bash
cd ~/zee-subtitle-translator  # or your install location
./uninstall.sh
```

**Windows:**
```cmd
cd %USERPROFILE%\zee-subtitle-translator
uninstall.bat
```

The uninstaller will:
- Remove global `zeetranslator` command
- Remove alias from shell config
- Remove Termux widget (if exists)
- Remove configuration files
- Create backup of shell config

**Note:** To also delete the project folder:
```bash
# Linux/macOS/Android
rm -rf ~/zee-subtitle-translator

# Windows
rmdir /s "%USERPROFILE%\zee-subtitle-translator"
```

## Documentation

- [Quick Start Guide](QUICKSTART.md) - 5-minute tutorial
- [Detailed Usage Guide](GUIDE.md) - All features explained
- [FAQ](FAQ.md) - Common questions and answers
- [Indonesian Tutorial](Complete%20Install%20Tutorial%20(Bahasa%20Indonesia).md) - Panduan lengkap
- [Android Storage Guide](ANDROID_STORAGE_GUIDE.md) - Termux storage explanation

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

## Support

If you find this tool useful, consider supporting development:

**International (PayPal):**
```
https://paypal.me/zeewank
```

**Indonesia (Trakteer):**
```
https://trakteer.id/zeewank/tip
```

## Acknowledgments

- [deep-translator](https://github.com/nidhaloff/deep-translator) - Translation API wrapper
- [pysrt](https://github.com/byroot/pysrt) - SRT file parsing
- [pysubs2](https://github.com/tkarabela/pysubs2) - ASS/SSA subtitle support
- [tqdm](https://github.com/tqdm/tqdm) - Progress bars

## Links

- [Report Bug](https://github.com/zeewank/zee-subtitle-translator/issues)
- [Request Feature](https://github.com/zeewank/zee-subtitle-translator/issues)
- [Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions)

---

Made by Zee | [GitHub](https://github.com/zeewank)
