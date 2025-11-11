# 🌐 Zee Subtitle Translator

**A powerful, user-friendly command-line tool for batch translating subtitle files with advanced features.**

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()

## ✨ Features

- 🚀 **Multiple Translation Engines**: Google Translate (free) & DeepL API support
- 📁 **Batch Processing**: Translate multiple files and folders at once
- 🎯 **Smart File Selection**: Interactive file browser with multiple folder support
- 🧹 **Auto Text Cleaning**: Removes unwanted tags like `[MUSIC]`, `(SOUND)`, etc.
- 🎬 **Custom Credits**: Add your signature to translated subtitles
- 📊 **Progress Tracking**: Real-time progress bars and detailed summary reports
- 🔤 **Format Support**: SRT, VTT, and ASS subtitle formats
- 🧠 **Smart Detection**: Auto-detects file encoding and proper names
- ⚡ **Speed Control**: Choose between Safe, Standard, or Aggressive translation modes
- 🌍 **Bilingual UI**: English and Indonesian interface support

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

# Run the installer
chmod +x installer.sh
./installer.sh

# Start translating!
./zee_translator.py
```

### 🪟 Windows

**Easy Install:**
1. Download [latest release](https://github.com/zeewank/zee-subtitle-translator)
2. Extract ZIP file
3. Double-click `install_windows.bat`
4. Double-click `run_translator.bat`

📖 **Detailed Guide:** [Windows Installation](INSTALL_WINDOWS.md)

### 📱 Android (Termux)

```bash
# Install Termux from F-Droid, then:
pkg update -y && pkg install -y python git
git clone https://github.com/yourusername/zee-subtitle-translator.git
cd zee-subtitle-translator
pip install -r requirements.txt
termux-setup-storage
./zee_translator.py
```


### ⚡ Quick Start

New to the tool? Check out the [Quick Start Guide](QUICKSTART.md) for a 5-minute tutorial!

## 📖 Usage

### Basic Usage

Simply run the program and follow the interactive prompts:

```bash
./zee_translator.py
```

### Command-Line Arguments

```bash
# Translate a specific folder
./zee_translator.py /path/to/subtitle/folder

# Translate a ZIP file
./zee_translator.py /path/to/subtitles.zip
```

### Translation Modes

**1. Safe Mode (Line-by-Line)**
- Translates each line individually
- Most stable, best for problematic files
- Slower but more reliable

**2. Standard Mode (Recommended)**
- Translates 50 lines per batch
- Best balance of speed and reliability
- Ideal for most use cases

**3. Aggressive Mode**
- Translates 100 lines per batch
- Fastest but may trigger rate limits
- Use for large batches with caution

### Multiple Folder Selection

When selecting multiple folders:
- Type a **number** to OPEN/browse a folder
- Type **s + number** (e.g., `s14`) to SELECT a folder without opening
- Type **u + number** (e.g., `u1`) to UNSELECT a folder
- Type `.` (dot) to select the current folder
- Type `0` to finish selection and proceed
- Type `q` to cancel

### Output Options

**For Single Folder:**
1. Create a new subfolder with custom name
2. Save in the same folder as originals

**For Multiple Folders:**
1. Save to original folders (keeps structure)
2. Save to one combined output folder

## 🎨 Examples

### Example 1: Translate Single Season

```bash
./zee_translator.py
# Select: Browse folder → Navigate to "Breaking Bad S01" → Select All → Translate
```

### Example 2: Multiple Seasons

```bash
./zee_translator.py
# Select: Multiple folders → s5 (S01) → s6 (S02) → 0 (finish) → Translate
```

### Example 3: ZIP Archive

```bash
./zee_translator.py subtitles.zip
# Select files → Choose output → Translate
```

## 🛠️ Configuration

### Using DeepL API

For better translation quality, you can use DeepL:

1. Get a free API key from [DeepL](https://www.deepl.com/pro-api)
2. Set environment variable:

```bash
export DEEPL_API_KEY="your-api-key-here"
```

Or add to `~/.bashrc` or `~/.zshrc` for permanent use.

### UI Language

Choose your preferred language on first run or via:
- Menu → Settings → Language Settings

## 📊 Output Format

Translated files are named with language code suffix:
```
original_file.srt → original_file.id.srt
movie.vtt → movie.id.vtt
```

## 🐛 Troubleshooting

### Slow Translation Speed

**Problem**: Translation taking longer than expected
**Solution**: 
- Use Standard or Safe mode
- Check your internet connection
- Google Translate may have rate limits - wait a few hours

### Encoding Errors

**Problem**: Strange characters in output
**Solution**: The tool auto-detects encoding, but if issues persist:
- Ensure original files are UTF-8 encoded
- Try Safe mode for better handling

### API Rate Limiting

**Problem**: "Rate limit" or "API blocked" errors
**Solution**:
- Switch to Safe mode
- Reduce batch size
- Wait before retrying
- Use VPN if persistent

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

- ❓ FAQ: Check [Frequently Asked Questions](FAQ.md)
- 📖 Documentation: See [Documentation Index](DOCS_INDEX.md)

## 💖 Support Project

**🌍 PayPal (International):**
```
https://paypal.me/zeewank
```

**🇮🇩 Trakteer (Indonesia):**
```
https://trakteer.id/zeewank/tip
```

## 🙏 Acknowledgments

- [deep-translator](https://github.com/nidhaloff/deep-translator) - Translation API wrapper
- [pysrt](https://github.com/byroot/pysrt) - SRT file parsing
- [pysubs2](https://github.com/tkarabela/pysubs2) - ASS/SSA subtitle support
- [tqdm](https://github.com/tqdm/tqdm) - Progress bars

---

**Zee-Subtitle-Translator**

⭐ Star this repo if you find it helpful!
