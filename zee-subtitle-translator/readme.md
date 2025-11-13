# 🌍 Zee Subtitle Translator

**A powerful, user-friendly command-line tool for batch translating subtitle files with advanced features.**

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Android-lightgrey.svg)]()

## Features

- Multiple Translation Engines: Google Translate (free) & DeepL API support
- Batch Processing: Translate multiple files and folders at once
- Smart File Selection : Interactive file browser with multiple folder support
- Auto Text Cleaning : Removes unwanted tags like `[MUSIC]`, `(SOUND)`, etc.
- Custom Credits : Add your signature to translated subtitles
- Progress Tracking: Real-time progress bars and detailed summary reports
- Format Support: SRT, VTT, and ASS subtitle formats
- Smart Detection: Auto-detects file encoding and proper names
- Speed Control: Choose between Safe, Standard, or Aggressive translation modes
- Bilingual UI: English and Indonesian interface support
- Global Command: Type `zeetranslator` from anywhere!

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection (for translation APIs)

## 🚀 Quick Install

### 🐧 Linux / macOS

```bash
# Clone the repository
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator

# Run the installer (automatically sets up everything!)
chmod +x installer.sh
./installer.sh

# Start translating from anywhere!
zeetranslator
```

**What the installer does:**
- ✅ Installs all Python dependencies
- ✅ Sets up executable permissions
- ✅ Creates global `zeetranslator` command
- ✅ Configures shell aliases automatically

---

### 🪟 Windows

**Method 1: Auto Installer (Recommended)**

1. **Download:**
   - Go to [Releases](https://github.com/zeewank/zee-subtitle-translator/releases)
   - Download `zee-subtitle-translator.zip`
   - Extract to `C:\ZeeTranslator\` (or any folder)

2. **Install:**
   - Double-click `install_windows.bat`
   - Wait for installation to complete
   - **That's it!** 🎉

3. **Use:**
   ```cmd
   # From any directory:
   zeetranslator
   
   # Or double-click:
   run_translator.bat
   ```

**Method 2: Manual Install**

```cmd
# 1. Install Python from python.org (check "Add to PATH"!)

# 2. Clone repository
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator

# 3. Install dependencies
python -m pip install -r requirements.txt

# 4. Run installer
install_windows.bat
```

**Windows Usage:**
```cmd
zeetranslator                       # Interactive mode
zeetranslator "C:\Videos\Subs"      # Translate specific folder
```

---

### 📱 Android (Termux)

**Step 1: Install Termux**
- ⚠️ **Don't use Google Play Store version!**
- Download from [F-Droid](https://f-droid.org/packages/com.termux/) or [GitHub](https://github.com/termux/termux-app/releases)

**Step 2: Quick Setup**

```bash
# Update Termux
pkg update -y && pkg upgrade -y

# Install Git
pkg install -y git

# Clone repository
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator

# Run Termux setup script
chmod +x setup_termux.sh
./setup_termux.sh
```

**The setup script automatically:**
- ✅ Installs Python and dependencies
- ✅ Sets up storage access
- ✅ Creates shortcuts to Downloads, Movies, DCIM
- ✅ Creates global `zeetranslator` command
- ✅ Creates Termux widget shortcut

**Android Usage:**
```bash
# From anywhere:
zeetranslator

# Translate downloads folder:
zeetranslator ~/downloads/Subtitles

# Translate movies:
zeetranslator ~/movies/MyMovie/
```

**Bonus: Widget Setup**
1. Long-press home screen
2. Select "Widgets"
3. Find "Termux:Widget"
4. Select "ZeeTranslator"
5. Tap widget to launch translator! 🎯

---

## 📖 Usage

### Basic Usage

Simply type from anywhere:
```bash
zeetranslator
```

### Command-Line Arguments

```bash
# Translate specific folder
zeetranslator /path/to/subtitle/folder

# Translate ZIP file
zeetranslator /path/to/subtitles.zip

# Traditional way still works:
./zee_translator.py
python zee_translator.py
```

### Translation Modes

| Mode | Speed | Reliability | Best For |
|------|-------|-------------|----------|
| **Safe** | Slow | Highest | Important content, complex formats |
| **Standard** | Fast | High | General use (recommended) |
| **Aggressive** | Very Fast | Medium | Large batches, good connection |

### Multiple Folder Selection

When browsing folders:

| Command | Action | Example |
|---------|--------|---------|
| `14` | Open folder 14 | Navigate into Downloads |
| `s14` | Select folder 14 | Add to selection without opening |
| `u1` | Unselect folder 1 | Remove from selection |
| `.` | Select current folder | Add current directory |
| `0` | Finish selection | Start processing |
| `q` | Cancel | Return to menu |

---

## 🎨 Examples

### Example 1: Quick Translation

```bash
# Just type from anywhere:
zeetranslator

# Follow the prompts:
# 1. Choose Google Translate
# 2. Browse to your subtitle folder
# 3. Select files (or press 0 for all)
# 4. Choose output location
# 5. Pick Standard speed
# 6. Enter language: id
# 7. Add credit: y
# 8. Confirm: y
```

### Example 2: Direct Folder Translation

```bash
# Linux/macOS:
zeetranslator ~/Videos/BreakingBad/Season1/

# Windows:
zeetranslator "C:\Users\YourName\Videos\Season1\"

# Android:
zeetranslator ~/downloads/Subtitles/
```

### Example 3: Multiple Seasons

```bash
zeetranslator

# Select: Multiple folders
# Navigate and select:
# s → Season 1
# s → Season 2  
# s → Season 3
# 0 → Start
```

---

## 🛠️ Configuration

### Using DeepL API (Optional)

For better translation quality:

**Linux/macOS/Android:**
```bash
# Add to ~/.bashrc or ~/.zshrc:
export DEEPL_API_KEY="your-api-key-here"

# Reload shell:
source ~/.bashrc
```

**Windows:**
```cmd
# Set environment variable:
setx DEEPL_API_KEY "your-api-key-here"

# Or add via System Properties → Environment Variables
```

Get free API key: [DeepL API](https://www.deepl.com/pro-api)

---

## 📊 Output Format

Translated files are named with language code suffix:
```
original_file.srt → original_file.id.srt
movie.vtt → movie.id.vtt
episode_01.ass → episode_01.id.ass
```

---

## 🛠️ Troubleshooting

### "zeetranslator: command not found"

**Linux/macOS:**
```bash
# Reload shell config:
source ~/.bashrc  # or ~/.zshrc

# Or open new terminal
```

**Windows:**
- Restart Command Prompt
- Or use: `python zee_translator.py`

**Android:**
```bash
# Reload:
source ~/.bashrc

# Or restart Termux
```

### Slow Translation

**Solutions:**
- Use WiFi instead of mobile data
- Try Safe mode (more stable)
- Translate during off-peak hours
- Check internet speed

### Permission Denied

**Linux/macOS/Android:**
```bash
chmod +x zee_translator.py
# Or:
python3 zee_translator.py
```

**Windows:**
- Run Command Prompt as Administrator

### Module Not Found

```bash
# Reinstall dependencies:
pip install --force-reinstall -r requirements.txt
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request



---

## 💖 Support Project

If this tool helps you, consider supporting development:

**🌍 International (PayPal):**
```
https://paypal.me/zeewank
```

**🇮🇩 Indonesia (Trakteer):**
```
https://trakteer.id/zeewank/tip
```

Every donation helps keep this project free and actively maintained! 🙏

---

## 🙏 Acknowledgments

- [deep-translator](https://github.com/nidhaloff/deep-translator) - Translation API wrapper
- [pysrt](https://github.com/byroot/pysrt) - SRT file parsing
- [pysubs2](https://github.com/tkarabela/pysubs2) - ASS/SSA subtitle support
- [tqdm](https://github.com/tqdm/tqdm) - Progress bars

---

## 📚 Documentation

- 📖 [Quick Start Guide](QUICKSTART.md) - 5-minute tutorial
- 📘 [Usage Guide](GUIDE.md) - Detailed features
- ❓ [FAQ](FAQ.md) - Common questions
- 🌏 [Tutorial Indonesia](Complete%20Install%20Tutorial%20(Bahasa%20Indonesia).md)

---


⭐ Star this repo if you find it helpful!

🐛 [Report Bug](https://github.com/zeewank/zee-subtitle-translator/issues) | 💡 [Request Feature](https://github.com/zeewank/zee-subtitle-translator/issues)
