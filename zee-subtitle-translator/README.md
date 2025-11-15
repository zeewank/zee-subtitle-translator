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

- Python 3.7 or higher
- pip package manager
- Internet connection for translation APIs

## Quick Install

### Linux / macOS

```bash
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
chmod +x installer.sh
./installer.sh
```

After installation:
```bash
zeetranslator
```

**Note:** If the command doesn't work immediately, run:
```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```
Or simply open a new terminal window.

### Windows

**Easy Installation:**

1. Download the latest release from [GitHub Releases](https://github.com/zeewank/zee-subtitle-translator/releases)
2. Extract the ZIP file to any location (example: `C:\ZeeTranslator\`)
3. Double-click `install_windows.bat`
4. Wait for installation to complete

**Manual Installation:**

```cmd
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
install_windows.bat
```

After installation:
```cmd
zeetranslator
```

**Note:** Restart Command Prompt if command not found.

### Android (Termux)

**Important:** Install Termux from [F-Droid](https://f-droid.org/packages/com.termux/) or [GitHub](https://github.com/termux/termux-app/releases), not Google Play Store.

```bash
pkg update -y && pkg upgrade -y
pkg install -y git
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
chmod +x setup_termux.sh
./setup_termux.sh
```

The setup script will:
- Install Python and dependencies
- Configure storage access
- **Ask where to install** (Termux home or Shared storage)
- Create shortcuts to Downloads, Movies, DCIM
- Set up global command
- Create Termux widget shortcut

**Recommended:** Choose Option 2 (Shared Storage) during setup. This installs to `Internal Storage/ZeeTranslator/` which is:
- Accessible from phone file manager
- Persists after uninstalling Termux
- Easy to backup and share

After setup:
```bash
zeetranslator
```

**Note:** If command not found, run `source ~/.bashrc` or restart Termux.

**Android Storage Guide:**
For detailed explanation about Termux storage and why "permission denied" occurs, see [ANDROID_STORAGE_GUIDE.md](ANDROID_STORAGE_GUIDE.md).

## Usage

### Basic Usage

Run the program from any directory:
```bash
zeetranslator
```

### With Specific Path

```bash
# Linux/macOS
zeetranslator ~/Videos/Subtitles/

# Windows
zeetranslator "C:\Users\YourName\Videos\Subtitles"

# Android
zeetranslator ~/downloads/Subtitles/
```

### Traditional Method

If global command doesn't work:
```bash
python zee_translator.py
# or
./zee_translator.py
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

### Command Not Found

**Linux/macOS:**
```bash
source ~/.bashrc  # or ~/.zshrc
```

**Windows:**
Restart Command Prompt or use:
```cmd
python zee_translator.py
```

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
cd zee-subtitle-translator  # or your install location
chmod +x uninstall.sh
./uninstall.sh
```

The uninstaller will:
- Remove global `zeetranslator` command
- Remove alias from shell config
- Remove Termux widget (if exists)
- Remove configuration files
- Create backup of shell config

**Note:** The uninstaller does NOT delete:
- Project folder (delete manually if desired: `rm -rf zee-subtitle-translator`)
- Python packages (uninstall manually if desired: `pip uninstall srt deep-translator tqdm chardet pysubs2`)

**Windows:**
1. Delete `%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\zeetranslator.bat`
2. Delete project folder manually
3. (Optional) Uninstall Python packages: `pip uninstall srt deep-translator tqdm chardet pysubs2`

## Documentation

- [Quick Start Guide](QUICKSTART.md) - 5-minute tutorial
- [Detailed Usage Guide](GUIDE.md) - All features explained
- [FAQ](FAQ.md) - Common questions and answers
- [Indonesian Tutorial](Complete%20Install%20Tutorial%20(Bahasa%20Indonesia).md) - Panduan lengkap
- [Android Storage Guide](ANDROID_STORAGE_GUIDE.md) - Termux storage explanation



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
