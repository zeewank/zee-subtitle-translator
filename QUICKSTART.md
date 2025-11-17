# 🚀 Quick Start Guide

Get started with Zee Subtitle Translator in 5 minutes!

#(Method 1: Bootstrap, Method 2: ZIP)

## Step 1: Install (Choose Method)

### Method A: One-Line Auto-Install (Fastest)

#### Linux

Open terminal and paste:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.sh | bash
```

#### macOS

Open Terminal and paste:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.sh | bash
```

#### Windows

Open **PowerShell** (right-click Start → Windows PowerShell) and paste:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

#### Android (Termux)

1. Install Termux from [F-Droid](https://f-droid.org/packages/com.termux/) (**NOT Google Play**)
2. Open Termux and paste:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_termux.sh | bash
```

**Wait 2-5 minutes** for installation to complete.

---

### Method B: Download ZIP + Install Locally

**For users who prefer manual download or have connectivity issues.**

1. **Download ZIP:** https://github.com/zeewank/zee-subtitle-translator/archive/refs/heads/main.zip
2. **Extract ZIP file**
3. **Run installer:**
   - **Linux/macOS:** `./installer.sh`
   - **Windows:** `install_windows.bat` (double-click)
   - **Android:** `./setup_termux.sh`

**📖 See:** [INSTALL_FROM_ZIP.md](INSTALL_FROM_ZIP.md) for detailed guide.

---

### Installation Issues?

- **404 Error or wrong URL?** See [FIX_BOOTSTRAP_ERRORS.md](FIX_BOOTSTRAP_ERRORS.md)
- **PowerShell error?** See [FIX_BOOTSTRAP_ERRORS.md](FIX_BOOTSTRAP_ERRORS.md)
- **Download ZIP instead:** See [INSTALL_FROM_ZIP.md](INSTALL_FROM_ZIP.md)

---

## Step 2: Activate Command

After installation completes:

### Linux / macOS / Android

```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```

### Windows

Close and reopen PowerShell/Command Prompt.

**Or simply open a new terminal window!**

---

## Step 3: Run It!

```bash
zeetranslator
```

You should see:

```
╔═══════════════════════════════════════════╗
║        ZEE SUBTITLE TRANSLATOR v1         ║
╚═══════════════════════════════════════════╝

Welcome!
------------------------------------------------------------
1. Translate Subtitles
2. UI Language Settings
3. Exit
------------------------------------------------------------
Choice [1-3]:
```

---

## Step 4: Your First Translation

Let's translate a subtitle file!

### Example Workflow

1. **Press `1`** (Translate Subtitles)

2. **Choose engine:**
   ```
   🤖 Choose translation engine:
     1. Google Translate (free, auto-detect)
     2. DeepL API (requires API key)
     3. ChatGPT API (requires API key) 🆕
   Choice [1-3]: 1
   ```
   **Press `1`** for Google (free)

3. **Choose source:**
   ```
   📂 Choose subtitle source:
     1. Browse folder / .zip file
     2. Current folder
     3. Select multiple folders
   Choice [1-3]: 1
   ```
   **Press `1`** to browse

4. **Navigate to your subtitle folder:**
   - Type number to open folder
   - Press Enter when you find your subtitle files

5. **Choose search depth:**
   ```
   🔍 Search in sub-folders too? (y/n): n
   ```
   **Type `n`** for simple folder

6. **Select files:**
   ```
   📋 Found 5 files:
     1. episode01.srt
     2. episode02.srt
     3. episode03.srt
     4. episode04.srt
     5. episode05.srt
   
   Select files:
     0. [PROCESS ALL]
     (e.g., 1, 3, 5) or range (e.g., 1-10):
   >
   ```
   **Type `0`** to process all, or **`1-3`** for range

7. **Choose output location:**
   ```
   📂 Choose output location:
     1. Create a new sub-folder (You can name it)
     2. Same folder as original files
   Choice [1-2] (default 1):
   ```
   **Press `1`** and name folder (e.g., "Indonesian")

8. **Choose processing speed:**
   ```
   ⚙️ Choose 'Processing Engine' (Speed):
     1. Safe (Slow)
     2. Standard (Fast / Recommended)
     3. Aggressive (Very Fast)
   Choice [1-3] (default 2): 2
   ```
   **Press `2`** for Standard (recommended)

9. **Set target language:**
   ```
   🎯 Target language (default: id): id
   ```
   **Press Enter** for Indonesian, or type code (e.g., `es` for Spanish)

10. **Add credits:**
    ```
    🎬 Add creator credit at the beginning? (y/n default y): y
    ```
    **Press `y`** to add your name

11. **Confirm and start:**
    ```
    ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
        CONFIRMATION SUMMARY
    ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
      Source      : Movies
      Engine      : google
      Speed       : Fast (Batch)
      Target      : id
      Files       : Processing 5 files
      Output      : /path/to/Indonesian
      Cleaning    : Always On
      Credit      : ✅ Yes
    ============================================================
    
    Start processing? (y/n): y
    ```
    **Press `y`** to start!

12. **Watch the progress:**
    ```
    🚀 Starting translation...
    ============================================================
    
    📄 Processing file 1/5: episode01.srt
    episode01.srt: |████████████████████| 9/9 batches
    ✅ Saved: episode01.id.srt
    
    📄 Processing file 2/5: episode02.srt
    ...
    ```

13. **Done!**
    ```
    ============================================================
        PROCESS SUMMARY
    ============================================================
    ✅ 5 files succeeded
    ⚠️ 0 skipped
    ❌ 0 failed
    ℹ️ Total duration: 3 minutes 24 seconds
    ============================================================
    ```

---

## Common Use Cases

### Translate One Movie

```bash
zeetranslator ~/Movies/MyMovie/
```

Select all subtitle files, choose Indonesian, done!

### Translate TV Series (One Season)

```bash
zeetranslator ~/Series/BreakingBad/Season1/
```

All episodes translated in one go.

### Translate Multiple Seasons

```bash
zeetranslator
```

1. Choose: Multiple folders
2. Browse and select Season 1 (type `s1`)
3. Browse and select Season 2 (type `s2`)
4. Browse and select Season 3 (type `s3`)
5. Type `0` to finish
6. Choose "Keep structure" for output
7. Start!

Each season gets translated in its own folder.

### Translate ZIP File

```bash
zeetranslator ~/Downloads/subtitles.zip
```

Automatically extracts and translates.

---

## 🆕 Using ChatGPT API

### Setup

1. Get API key from https://platform.openai.com/api-keys
2. Set environment variable:

**Linux/macOS/Android:**
```bash
export OPENAI_API_KEY="sk-proj-your-key-here"
```

**Windows:**
```cmd
setx OPENAI_API_KEY "sk-proj-your-key-here"
```

### Usage

1. Run `zeetranslator`
2. Choose option **3** (ChatGPT API)
3. Select model (GPT-3.5 recommended for cost)
4. Continue as normal




---

## Quick Tips

### Speed Modes

- **Safe (Slow):** Most reliable, ~2-3 min per file
- **Standard (Fast):** Best balance, ~1-2 min per file ⭐ **Recommended**
- **Aggressive:** Fastest, ~30-45 sec per file, may get rate limited

### Language Codes

Common target languages:
- `id` - Indonesian
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `ja` - Japanese
- `ko` - Korean
- `zh-CN` - Chinese (Simplified)

### File Selection

- `0` - Process all files
- `1,3,5` - Process files 1, 3, and 5
- `1-10` - Process files 1 through 10
- `1-5,8,12-15` - Combined selection

### Folder Navigation

- Type number to open folder
- `s14` - Select folder 14 without opening
- `u1` - Unselect folder 1
- `.` - Select current folder
- `0` - Finish selection
- `q` - Cancel

---

## Troubleshooting

### Command Not Found

```bash
# Linux/macOS/Android
source ~/.bashrc  # or source ~/.zshrc

# Windows: Restart PowerShell
```

### Slow Translation

- Use WiFi, not mobile data
- Try Safe mode (more stable)
- Translate during off-peak hours
- Process smaller batches

### Installation Failed

See detailed troubleshooting guides:

- **Bootstrap errors:** [FIX_BOOTSTRAP_ERRORS.md](FIX_BOOTSTRAP_ERRORS.md)
- **Manual install:** [INSTALL_FROM_ZIP.md](INSTALL_FROM_ZIP.md)
- **Android issues:** [ANDROID_STORAGE_GUIDE.md](ANDROID_STORAGE_GUIDE.md)

### Missing Dependencies

```bash
cd ~/zee-subtitle-translator
pip install --force-reinstall -r requirements.txt
```

---

## Translation Engine Comparison

| Engine | Quality | Speed | Cost |
|--------|---------|-------|------|
| Google | ⭐⭐⭐ | Fast | Free |
| DeepL | ⭐⭐⭐⭐ | Medium | $5-20/1M |
| ChatGPT 3.5 🆕 | ⭐⭐⭐⭐ | Medium | $0.50/1M |
| ChatGPT 4 🆕 | ⭐⭐⭐⭐⭐ | Slow | $10/1M |

**Recommendation:**
- **Free:** Google Translate
- **Best quality:** ChatGPT 4 or DeepL
- **Best value:** ChatGPT 3.5-turbo

---

## Next Steps

Now that you know the basics:

1. **Read full guide:** [GUIDE.md](GUIDE.md)
2. **Check FAQ:** [FAQ.md](FAQ.md)
3. **Android users:** [ANDROID_STORAGE_GUIDE.md](ANDROID_STORAGE_GUIDE.md)

---

## Need Help?

- [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues) - Report bugs
- [GitHub Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions) - Ask questions
- [FAQ](FAQ.md) - Common questions

---

## Support

If this tool helps you, consider supporting:

**International:** https://paypal.me/zeewank  
**Indonesia:** https://trakteer.id/zeewank/tip

---

**Happy translating! 🎬**
