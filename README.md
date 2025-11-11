# 🌐 Zee Subtitle Translator

**A powerful, user-friendly command-line tool for batch translating subtitle files with advanced features.**

Features

-  **Multiple Translation Engines**: Google Translate (free) & DeepL API support
-  **Batch Processing**: Translate multiple files and folders at once
-  **Smart File Selection**: Interactive file browser with multiple folder support
-  **Auto Text Cleaning**: Removes unwanted tags like `[MUSIC]`, `(SOUND)`, etc.
-  **Custom Credits**: Add your signature to translated subtitles
-  **Progress Tracking**: Real-time progress bars and detailed summary reports
-  **Format Support**: SRT, VTT, and ASS subtitle formats
-  **Smart Detection**: Auto-detects file encoding and proper names
-  **Speed Control**: Choose between Safe, Standard, or Aggressive translation modes
-  **Bilingual UI**: English and Indonesian interface support

  <img width="407" height="241" alt="Screenshot at 2025-11-11 15-52-56" src="https://github.com/user-attachments/assets/901a0e66-c335-46d8-bfb9-0ecabdb8dc8f" />

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
1. Download (https://github.com/zeewank/zee-subtitle-translator/releases)
2. Extract ZIP file
3. Double-click `install_windows.bat`
4. Double-click `run_translator.bat`

### 📱 Android (Termux)

```bash
# Install Termux from F-Droid, then:
pkg update -y && pkg install -y python git
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
pip install -r requirements.txt
termux-setup-storage
./zee_translator.py
```

### ⚡ Quick Start

New to the tool? Check out the [Quick Start Guide](https://github.com/zeewank/zee-subtitle-translator/blob/main/zee-subtitle-translator/QUICKSTART.md "QUICKSTART.md") for a 5-minute tutorial! 

⭐ Star this repo if you find it helpful
