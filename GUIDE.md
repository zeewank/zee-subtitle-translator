# 📖 Detailed Usage Guide

This guide covers all features and usage scenarios for Zee Subtitle Translator.

## Table of Contents
- [Installation Methods](#installation-methods)
- [Basic Workflow](#basic-workflow)
- [Translation Engines](#translation-engines)
- [Translation Modes](#translation-modes)
- [Multiple Folder Selection](#multiple-folder-selection)
- [Output Options](#output-options)
- [Advanced Features](#advanced-features)
- [Tips & Tricks](#tips--tricks)
- [Troubleshooting](#troubleshooting)

---

## Installation Methods

##(Method 1: Bootstrap, Method 2: ZIP)

### Method 1: One-Line Auto-Install (Recommended)

**No git required!** Downloads everything automatically.

**Linux/macOS:**
```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.sh | bash
```

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

**Android (Termux):**
```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_termux.sh | bash
```

Wait 2-5 minutes for automatic installation to complete.

### Method 2: Download ZIP + Local Install

**For users who prefer manual download or have connectivity issues.**

1. Download ZIP from [GitHub](https://github.com/zeewank/zee-subtitle-translator/archive/refs/heads/main.zip)
2. Extract ZIP file
3. Run installer:
   - **Linux/macOS:** `./installer.sh`
   - **Windows:** `install_windows.bat`
   - **Android:** `./setup_termux.sh`

**📖 Detailed guide:** [INSTALL_FROM_ZIP.md](INSTALL_FROM_ZIP.md)

### Installation Issues?

- **Bootstrap errors (404, PowerShell issues):** [FIX_BOOTSTRAP_ERRORS.md](FIX_BOOTSTRAP_ERRORS.md)
- **Android storage issues:** [ANDROID_STORAGE_GUIDE.md](ANDROID_STORAGE_GUIDE.md)

### Activate Command

After installation:

**Linux/macOS/Android:**
```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```

**Windows:**
Close and reopen Command Prompt/PowerShell

### Verify Installation

```bash
zeetranslator
```

Should display the main menu.

---

## Basic Workflow

### Simple Translation

```bash
# Start the program
zeetranslator

# Follow the prompts:
# 1. Choose translation engine (Google/DeepL/ChatGPT)
# 2. Select subtitle source
# 3. Choose files to translate
# 4. Select output location
# 5. Choose translation speed
# 6. Set target language
# 7. Enable/disable credits
# 8. Confirm and start
```

### Direct Path Input

```bash
# Translate specific folder
zeetranslator /path/to/subtitles/

# Translate ZIP file
zeetranslator /path/to/subtitles.zip
```

---

## Translation Engines

Zee Translator supports 4 translation engines:

### Comparison Table

| Engine | Quality | Speed | Cost | Languages | Best For |
|--------|---------|-------|------|-----------|----------|
| **Google Translate** | ⭐⭐⭐ | ⚡⚡⚡ | Free | 100+ | Daily use, large batches |
| **DeepL API** | ⭐⭐⭐⭐ | ⚡⚡ | $5-20/1M chars | ~30 | Professional work |
| **ChatGPT 3.5** 🆕 | ⭐⭐⭐⭐ | ⚡⚡ | $0.50-1.50/1M tokens | 50+ | Natural translations |
| **ChatGPT 4** 🆕 | ⭐⭐⭐⭐⭐ | ⚡ | $10-30/1M tokens | 50+ | Critical content |

### 1. Google Translate (Free)

**Pros:**
- ✅ Completely free
- ✅ Supports 100+ languages
- ✅ Fast and reliable
- ✅ No setup required

**Cons:**
- ❌ Sometimes awkward phrasing
- ❌ Rate limiting on heavy use
- ❌ Less context-aware

**When to use:** Daily subtitle translation, large batches, multiple languages.

### 2. DeepL API (Paid)

**Pros:**
- ✅ Better quality than Google
- ✅ More natural phrasing
- ✅ Professional results

**Cons:**
- ❌ Requires API key
- ❌ Limited to ~30 languages
- ❌ Pay per use

**Setup:** Get API key from [DeepL](https://www.deepl.com/pro-api)

**When to use:** Professional translations, important content.

### 3. ChatGPT API (Paid) 🆕

**Pros:**
- ✅ AI-powered, context-aware
- ✅ Most natural translations
- ✅ Understands nuance and tone
- ✅ Two models: 3.5 (cheap) and 4 (best)

**Cons:**
- ❌ Requires OpenAI API key
- ❌ Not the same as ChatGPT Plus subscription
- ❌ Pay per use


**Cost estimate (GPT-3.5):**
- 100 subtitle files ≈ $0.60 (Rp 10,000)
- Very affordable for quality

**When to use:** Best quality translations, natural dialogue, creative content.

**⚠️ Important:** ChatGPT Plus subscription ≠ ChatGPT API access. See guide for details.

---

## Translation Modes

### 1. Safe Mode (Line-by-Line)

**When to use:**
- First-time translation of important files
- Files with complex formatting
- When stability is priority over speed
- Troubleshooting translation issues

**Characteristics:**
- Translates one line at a time
- Slowest but most reliable
- Best error recovery
- ~2-3 minutes per file

**Example:**
```
Speed Choice: 1

Processing: movie.srt
Progress: |████████████████████| 450/450 lines
✅ Saved: movie.id.srt
```

### 2. Standard Mode (Recommended)

**When to use:**
- Regular translation tasks
- Balanced speed and reliability
- Most file types and sizes
- Default choice for most users

**Characteristics:**
- Translates 50 lines per batch
- Good speed/stability balance
- Handles most edge cases
- ~1-2 minutes per file

**Example:**
```
Speed Choice: 2

Processing: episode01.srt
Progress: |████████████████████| 9/9 batches
✅ Saved: episode01.id.srt
```

### 3. Aggressive Mode

**When to use:**
- Large batch jobs (>20 files)
- Stable network connection
- Less critical content
- When speed is priority

**Characteristics:**
- Translates 100 lines per batch
- Fastest mode
- May trigger rate limits
- ~30-45 seconds per file

**Warning:** May get blocked if overused, especially with free APIs.

---

## Multiple Folder Selection

### Navigation Commands

| Command | Action | Example |
|---------|--------|---------|
| `14` | Open/browse folder 14 | Opens Downloads folder |
| `s14` | Select folder 14 without opening | Adds folder to selection |
| `u1` | Remove folder 1 from selection | Removes from list |
| `.` | Select current folder | Adds pwd to selection |
| `0` | Finish and proceed | Starts processing |
| `q` | Cancel selection | Returns to menu |

### Workflow Example

**Scenario:** Translate Season 1 and Season 2 from different locations

```bash
# Start program
zeetranslator

# Choose: 3. Select multiple folders

# Navigate to Season 1
Current: /home/user
> 14           # Open Downloads
> s5           # Select "TV Show S01" folder
✅ Added: TV Show S01

# Navigate to Season 2
> 24           # Go to parent
> 13           # Open Documents
> s8           # Select "TV Show S02" folder
✅ Added: TV Show S02

# Finish
> 0            # Start processing

📂 Selected folders:
  [1] /home/user/Downloads/TV Show S01
  [2] /home/user/Documents/TV Show S02
```

### Visual Indicators

```
📂 Folder list:
  1) Archive/
  2) Movies/
  3) TV Shows/ ✓    ← Already selected
  4) Downloads/
```

---

## Output Options

### Single Folder Mode

**Option 1: New Subfolder**
```
Input:  /media/movies/subtitles/
Output: /media/movies/subtitles/translated/
```

**Option 2: Same Folder**
```
Input:  /media/movies/subtitles/movie.srt
Output: /media/movies/subtitles/movie.id.srt
```

### Multiple Folder Mode

**Option 1: Keep Structure (Recommended)**
```
Input:  /downloads/season1/ep01.srt
        /downloads/season2/ep01.srt
Output: /downloads/season1/ep01.id.srt
        /downloads/season2/ep01.id.srt
```

**Option 2: Merge to One Folder**
```
Input:  /downloads/season1/ep01.srt
        /downloads/season2/ep01.srt
Output: /downloads/translated/ep01.id.srt
        /downloads/translated/ep01.id.srt
```

⚠️ **Warning:** Option 2 may overwrite files with same names!

---

## Advanced Features

### Custom Credits

Add your signature to translated subtitles:

```
🎬 Add creator credit? (y/n): y

Result:
1
00:00:02,000 --> 00:00:07,000
Subtitle by Z33

2
00:00:10,000 --> 00:00:12,000
[Original subtitle text]
```

### Automatic Text Cleaning

Removes common noise automatically:

**Input:**
```
[MUSIC PLAYING]
(DOOR CREAKS)
<i>Internal thoughts</i>
{Translator note: Context}
```

**Output:**
```
[Empty - removed]
[Empty - removed]
Internal thoughts
Context
```

**Cleaned tags:**
- `[...]` - Sound effects
- `(...)` - Sound descriptions
- `<...>` - Formatting tags
- `{...}` - Notes

### Smart Name Detection

Proper names are NOT translated:

**Input:**
```
Hello, my name is McDonald.
Visit New York City.
Call 911!
```

**Output (to Indonesian):**
```
Halo, nama saya McDonald.
Kunjungi New York City.
Hubungi 911!
```

Names detected: `McDonald`, `New York City` (kept as-is)

### File Selection Patterns

**Select all:**
```
> 0
```

**Select specific:**
```
> 1, 5, 8, 12
```

**Select range:**
```
> 1-10
```

**Combined:**
```
> 1-5, 8, 12-15
```

---

## Tips & Tricks

### Faster Translation

1. **Use Standard mode** - Good balance
2. **Select fewer files** - Process in batches
3. **Stable connection** - Wired > WiFi
4. **Avoid peak hours** - Less API congestion
5. **Use ChatGPT 3.5** - Faster than GPT-4

### Better Quality

1. **Use Safe mode** - More accurate
2. **Check sample first** - Test 1-2 files
3. **Review output** - Spot-check results
4. **Use ChatGPT 4 or DeepL** - Best quality
5. **Clear source files** - Remove noise before translation

### Large Batches

1. **Split by folder** - Organize before translate
2. **Use Aggressive mode** - If you accept risks
3. **Process overnight** - For 100+ files
4. **Resume capability** - Skip existing `.id.srt`
5. **Monitor costs** - For paid APIs

### Organizing Output

**Before translation:**
```
/subtitles/
  ├── Season 1/
  ├── Season 2/
  └── Season 3/
```

**After translation (keep structure):**
```
/subtitles/
  ├── Season 1/
  │   ├── ep01.srt
  │   └── ep01.id.srt
  ├── Season 2/
  │   ├── ep01.srt
  │   └── ep01.id.srt
  └── Season 3/
      ├── ep01.srt
      └── ep01.id.srt
```

---

## Troubleshooting

### Slow Translation

**Problem:** Taking much longer than expected

**Solutions:**
1. Check internet speed
2. Switch to Safe mode
3. Reduce batch size
4. Try different time of day
5. Use VPN if region-blocked
6. Try different engine

### Garbled Output

**Problem:** Strange characters in translated files

**Solutions:**
1. Check input encoding (should auto-detect)
2. Convert source to UTF-8 first
3. Try Safe mode
4. Report as bug if persistent

### API Rate Limits

**Problem:** "Rate limit exceeded" or similar errors

**Solutions:**
1. Wait 1-2 hours
2. Switch to Safe mode (slower = less likely to hit limits)
3. Process smaller batches
4. Use different engine
5. For ChatGPT: Top up to increase tier limits

### Files Not Found

**Problem:** "No subtitle files found"

**Solutions:**
1. Check file extensions (.srt, .vtt, .ass)
2. Enable recursive search
3. Check file permissions
4. Ensure files aren't hidden

### Translation Errors

**Problem:** Some lines failed to translate

**Solutions:**
1. Check `error_log.txt` for details
2. Retry failed files in Safe mode
3. Split very long lines manually
4. Try different engine
5. Report persistent errors

### Memory Issues

**Problem:** Program crashes on large files

**Solutions:**
1. Process files individually
2. Close other programs
3. Use Aggressive mode (less memory)
4. Split large files (<5000 lines each)

### Installation Issues

**Problem:** One-line installer failed

**Solutions:**

See detailed troubleshooting guides:
- **Bootstrap errors:** [FIX_BOOTSTRAP_ERRORS.md](FIX_BOOTSTRAP_ERRORS.md)
- **Manual install:** [INSTALL_FROM_ZIP.md](INSTALL_FROM_ZIP.md)
- **Android issues:** [ANDROID_STORAGE_GUIDE.md](ANDROID_STORAGE_GUIDE.md)

### ChatGPT API Issues

**Problem:** ChatGPT errors or high costs

**Solutions:**

See complete guide: [CHATGPT_API_GUIDE.md](CHATGPT_API_GUIDE.md)

Common issues:
- **Invalid API Key** - Check key at platform.openai.com
- **Insufficient quota** - Top up credit
- **Rate limit** - Use Safe mode or upgrade tier
- **High costs** - Use GPT-3.5 instead of GPT-4

### Command Not Found

**Problem:** `zeetranslator` command not recognized

**Solutions:**

**Linux/macOS/Android:**
```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```

**Windows:**
Restart Command Prompt/PowerShell

**Alternative:**
```bash
cd ~/zee-subtitle-translator  # or your install location
python zee_translator.py
```

---

## Command Reference

### Main Menu
- `1` - Translate Subtitles
- `2` - UI Language Settings
- `3` - Exit

### Engine Selection
- `1` - Google Translate (free)
- `2` - DeepL API (paid)
- `3` - ChatGPT API (paid) 🆕

### Source Selection
- `1` - Browse folders/ZIP
- `2` - Current folder
- `3` - Multiple folders

### Output Selection
- `1` - New subfolder (custom name)
- `2` - Same as originals

### Speed Selection
- `1` - Safe (line-by-line)
- `2` - Standard (50/batch) ✅ Recommended
- `3` - Aggressive (100/batch)

### Language Codes (Common)

| Code | Language |
|------|----------|
| `id` | Indonesian |
| `en` | English |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `it` | Italian |
| `pt` | Portuguese |
| `ru` | Russian |
| `ja` | Japanese |
| `ko` | Korean |
| `zh-CN` | Chinese (Simplified) |
| `ar` | Arabic |
| `hi` | Hindi |
| `th` | Thai |
| `vi` | Vietnamese |

See [full list](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages) for all supported languages.

---

## Platform-Specific Notes

### Linux
- Requires `curl` or `wget` and `unzip`
- Global command works in bash and zsh
- Tested on Ubuntu, Debian, Arch, Fedora

### macOS
- Use `python3` command
- Works on Intel and Apple Silicon
- Requires Homebrew for easy setup

### Windows
- PowerShell recommended over Command Prompt
- Python auto-installs if missing
- WindowsApps batch file for global command

### Android (Termux)
- **Must use F-Droid or GitHub version**
- Choose Shared Storage for file manager access
- Widget support for quick launch
- Storage shortcuts created automatically

---

## Updating

### Update to Latest Version

**Option 1: Reinstall (Recommended)**
```bash
# Uninstall old version
cd ~/zee-subtitle-translator  # or your install location
./uninstall.sh

# Install latest
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.sh | bash
```

**Option 2: Git Pull (if installed via git clone)**
```bash
cd ~/zee-subtitle-translator
git pull
pip install --upgrade -r requirements.txt
```

---

## Uninstalling

```bash
# Navigate to install directory
cd ~/zee-subtitle-translator  # or your install location

# Run uninstaller
./uninstall.sh

# Optionally remove folder
cd ..
rm -rf zee-subtitle-translator
```
The uninstaller will:
- Remove global `zeetranslator` command
- Remove alias from shell config
- Remove Termux widget (if exists)
- Remove configuration files
- Create backup of shell config


## What's New

### Version 1.1 (Latest)

- ✅ **ChatGPT API support** - AI-powered translation with GPT-3.5 and GPT-4
- ✅ **Traditional installers** - For users who download ZIP files
- ✅ **Better error handling** - Fixed bootstrap installation errors
- ✅ **Improved documentation** - More guides and troubleshooting

### Version 1.0

- Initial release with Google Translate and DeepL support
- Multi-folder selection
- Three speed modes
- Bilingual interface



---

**Need more help?** 
- [FAQ](FAQ.md) - Common questions
- [ChatGPT API Guide](CHATGPT_API_GUIDE.md) - AI-powered translation
- [Install from ZIP](INSTALL_FROM_ZIP.md) - Manual installation
- [Fix Bootstrap Errors](FIX_BOOTSTRAP_ERRORS.md) - Troubleshooting
- [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues) - Report bugs
- [GitHub Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions) - Ask questions
