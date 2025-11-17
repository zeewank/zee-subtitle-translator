# 🚀 Quick Start Guide

Get started with Zee Subtitle Translator in 5 minutes!

## Step 1: Install (One Command)

### Linux

Open terminal and paste:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

### macOS

Open Terminal and paste:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

### Windows

Open **PowerShell** (right-click Start → Windows PowerShell) and paste:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

### Android (Termux)

1. Install Termux from [F-Droid](https://f-droid.org/packages/com.termux/) (**NOT Google Play**)
2. Open Termux and paste:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

**Wait 2-5 minutes** for installation to complete. The installer will:
- ✅ Download everything automatically
- ✅ Install Python (if needed)
- ✅ Set up all dependencies
- ✅ Create global `zeetranslator` command

## Step 2: Activate Command

After installation completes:

### Linux / macOS / Android

```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```

### Windows

Close and reopen PowerShell/Command Prompt.

**Or simply open a new terminal window!**

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

## Step 4: Your First Translation

Let's translate a subtitle file!

### Example Workflow

1. **Press `1`** (Translate Subtitles)

2. **Choose engine:**
   ```
   🤖 Choose translation engine:
     1. Google Translate (free, auto-detect)
     2. DeepL API (requires API key)
   Choice [1-2]: 1
   ```
   **Press `1`** for Google

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

## Quick Tips

### Speed Modes

- **Safe (Slow):** Most reliable, ~2-3 min per file
- **Standard (Fast):** Best balance, ~1-2 min per file
- **Aggressive:** Fastest, ~30-45 sec per file, may get rate limited

**Recommendation:** Start with Standard. Use Safe if Standard fails.

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

**Linux/macOS:**
```bash
# Try wget instead:
wget -qO- https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

**Windows:**
Download [install_windows.bat](https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat) manually and run.

**Android:**
```bash
# Update Termux first
pkg update -y && pkg upgrade -y

# Then try again
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

### Missing Dependencies

```bash
cd ~/zee-subtitle-translator
pip install --force-reinstall -r requirements.txt
```

## Next Steps

Now that you know the basics:

1. **Read full guide:** [GUIDE.md](GUIDE.md)
2. **Check FAQ:** [FAQ.md](FAQ.md)
3. **Android users:** [ANDROID_STORAGE_GUIDE.md](ANDROID_STORAGE_GUIDE.md)
4. **Indonesian guide:** [Complete Install Tutorial (Bahasa Indonesia).md](Complete%20Install%20Tutorial%20(Bahasa%20Indonesia).md)

## Need Help?

- [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues) - Report bugs
- [GitHub Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions) - Ask questions
- [FAQ](FAQ.md) - Common questions

## Support

If this tool helps you, consider supporting:

**International:** https://paypal.me/zeewank  
**Indonesia:** https://trakteer.id/zeewank/tip

---

**Happy translating! 🎬**
