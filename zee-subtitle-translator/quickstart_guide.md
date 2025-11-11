# ⚡ Quick Start Guide

Get started with Zee Subtitle Translator in 5 minutes!

## 🐧 Linux / macOS

```bash
# 1. Clone repository
git clone https://github.com/yourusername/zee-subtitle-translator.git
cd zee-subtitle-translator

# 2. Run installer
chmod +x installer.sh
./installer.sh

# 3. Start translating!
./zee_translator.py
```

**That's it!** 🎉

---

## 🪟 Windows

```powershell
# 1. Download and extract ZIP from GitHub

# 2. Double-click: install_windows.bat

# 3. Double-click: run_translator.bat
```

**Done!** 🎉

---

## 📱 Android (Termux)

```bash
# 1. Install Termux from F-Droid

# 2. In Termux:
pkg update -y && pkg install -y python git
git clone https://github.com/yourusername/zee-subtitle-translator.git
cd zee-subtitle-translator
pip install -r requirements.txt

# 3. Setup storage & run
termux-setup-storage
./zee_translator.py
```

**Ready!** 🎉

---

## 🎯 First Translation

### Step-by-Step:

1. **Start program**
   ```bash
   ./zee_translator.py
   ```

2. **Choose engine**
   ```
   Choose translation engine:
     1. Google Translate (free) ← Choose this
     2. DeepL API
   > 1
   ```

3. **Select source**
   ```
   Choose subtitle source:
     1. Browse folder
     2. Current folder ← Easy choice
     3. Multiple folders
   > 2
   ```

4. **Select files**
   ```
   Found 5 files:
     1. episode01.srt
     2. episode02.srt
     ...
   
   0. [PROCESS ALL] ← Select this
   > 0
   ```

5. **Choose output**
   ```
   Output location:
     1. New subfolder ← Recommended
     2. Same folder
   > 1
   
   Folder name: hasil_terjemahan
   ```

6. **Pick speed**
   ```
   Processing speed:
     1. Safe (Slow)
     2. Standard (Fast) ← Best choice
     3. Aggressive (Very Fast)
   > 2
   ```

7. **Set language**
   ```
   Target language: id  (Indonesian)
   Or: en, es, fr, de, ja, ko, etc.
   > id
   ```

8. **Add credit?**
   ```
   Add creator credit? (y/n)
   > y
   ```

9. **Confirm & Go!**
   ```
   Start processing? (y/n)
   > y
   ```

10. **Wait for completion**
    ```
    Processing file 1/5: episode01.srt
    [████████████████████] 100%
    ✅ Saved: episode01.id.srt
    
    ... (continues for all files)
    
    ========================================
    09:15:32 [🚀] --- PROCESS SUMMARY ---
    ✅ 5 files succeeded
    ⚠️ 0 skipped
    ❌ 0 failed
    ℹ️ Total duration: 3 minutes 45 seconds
    ========================================
    ```

**Congratulations!** Your subtitles are translated! 🎊

---

## 🔥 Pro Tips

### Faster Workflow

```bash
# Translate specific folder directly
./zee_translator.py /path/to/subtitles

# Process ZIP file
./zee_translator.py /path/to/subtitles.zip
```

### Multiple Folders

1. Choose option `3. Multiple folders`
2. Navigate: Type number to open folder
3. Select: Type `s + number` (e.g., `s5`)
4. Finish: Type `0`

Example:
```
> 14        # Open Downloads
> s5        # Select Season1
> 24        # Go back
> 13        # Open Documents  
> s8        # Select Season2
> 0         # Done!
```

### Keyboard Shortcuts

During folder browsing:
- `s14` - Select folder 14
- `u1` - Unselect folder 1
- `.` - Select current folder
- `0` - Finish selection
- `q` - Cancel

---

## 🆘 Common Issues

### "Python not found"

**Linux/Mac:**
```bash
sudo apt install python3  # Ubuntu/Debian
brew install python3      # macOS
```

**Windows:**
- Download from [python.org](https://python.org)
- Check "Add to PATH" during install

**Android:**
```bash
pkg install python
```

### "Permission denied"

```bash
chmod +x zee_translator.py
# Or:
python zee_translator.py
```

### "Module not found"

```bash
pip install -r requirements.txt
```

### Translation very slow

1. Use Standard mode (option 2)
2. Check internet connection
3. Try different time of day
4. Use WiFi instead of mobile data


---

## 🎬 Example Workflows

### Single Movie

```bash
# Place movie.srt in folder
cd ~/Movies/MyMovie
~/zee-subtitle-translator/zee_translator.py

# Select:
# - Current folder
# - All files
# - Same folder output
# - Standard speed
# - Language: id

# Result: movie.id.srt created
```

### TV Series (One Season)

```bash
# Navigate to season folder
cd ~/Series/BreakingBad/Season1

# Run translator
~/zee-subtitle-translator/zee_translator.py

# Select:
# - Current folder
# - All files  
# - New subfolder: "Indonesian"
# - Standard speed
# - Language: id

# Result: Indonesian/ folder with all .id.srt files
```

### Multiple Seasons

```bash
# Run translator
~/zee-subtitle-translator/zee_translator.py

# Select:
# - Multiple folders
# - Browse to Season1 → s (select)
# - Browse to Season2 → s (select)
# - Browse to Season3 → s (select)
# - 0 (finish)
# - Keep structure (option 1)
# - Standard speed
# - Language: id

# Result: Each season gets translated files in original folders
```

---

## 💡 Quick Tips

✅ **DO:**
- Start with Standard mode
- Test with 1-2 files first
- Keep originals as backup
- Use WiFi for large batches
- Organize files before translating

❌ **DON'T:**
- Use Aggressive mode on first try
- Translate 100+ files at once
- Delete originals immediately
- Close terminal during processing
- Use mobile data for large batches

---

## 🎉 You're Ready!

Start translating and enjoy your content in any language!

**Questions?** Check [USAGE.md](USAGE.md) or open an [issue](https://github.com/yourusername/zee-subtitle-translator/issues).

**Happy Translating!** 🌍✨
