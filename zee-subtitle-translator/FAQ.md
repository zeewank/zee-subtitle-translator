# ❓ Frequently Asked Questions (FAQ)

Common questions and answers about Zee Subtitle Translator.

## 🔥 Installation & Setup

### Q: Do I need to download the project manually?

**A:** **No!** Just run one command and everything downloads automatically:

**Linux/macOS:**
```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

**Windows:**
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

**Android:**
```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

No git required! No manual downloads!

### Q: Do I need git installed?

**A:** **No!** The new bootstrap installer downloads everything directly from GitHub using `curl` or `wget`. Git is completely optional.

### Q: Do I need to pay for this?

**A:** No! Zee Subtitle Translator is completely **free and open-source** under MIT License. Google Translate is also free. Only DeepL API requires payment.

### Q: Which Python version do I need?

**A:** Python 3.7 or higher. The installer will:
- **Check if Python exists**
- **Auto-install Python if missing** (Windows)
- **Guide you to install Python** (Linux/macOS/Android)

Check with:
```bash
python --version
# or
python3 --version
```

### Q: Can I use this without internet?

**A:** No, you need internet for:
1. Initial installation (downloads project and dependencies)
2. Translation (accesses Google Translate or DeepL API)

### Q: How long does installation take?

**A:** 
- **Good connection:** 2-3 minutes
- **Slow connection:** 3-5 minutes
- **First time (includes Python):** 5-10 minutes (Windows only)

### Q: What does the installer do exactly?

**A:**
1. ✅ Checks for Python (installs if needed on Windows)
2. ✅ Downloads project ZIP from GitHub
3. ✅ Extracts all files
4. ✅ Installs Python dependencies (srt, deep-translator, etc.)
5. ✅ Sets up global `zeetranslator` command
6. ✅ Creates shortcuts (Android only)
7. ✅ Creates Termux widget (Android only)

### Q: The installer fails. What should I do?

**A:** 

**Linux/macOS:**
```bash
# Try wget if curl fails:
wget -qO- https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash

# Or download manually:
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh
chmod +x installer.sh
./installer.sh
```

**Windows:**
1. Download [install_windows.bat](https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat)
2. Right-click → Run as Administrator
3. If still fails, install Python manually first from [python.org](https://python.org)

**Android:**
```bash
# Update Termux first
pkg update -y && pkg upgrade -y

# Install required packages
pkg install -y python curl unzip

# Try again
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

### Q: "curl: command not found" error

**A:**

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install curl

# Arch
sudo pacman -S curl

# Or use wget instead:
wget -qO- [URL] | bash
```

**Windows:** curl is built-in on Windows 10+. If missing, use PowerShell method.

**Android:**
```bash
pkg install curl
```

### Q: Can I install to a different location?

**A:**

**Linux/macOS:** 
By default installs to `~/zee-subtitle-translator`. To change, edit the downloaded bootstrap script before running.

**Windows:** 
By default installs to `%USERPROFILE%\zee-subtitle-translator`. To change, edit the downloaded bootstrap script.

**Android:** 
The installer **asks you** during setup:
- Option 1: Termux Home (`~/zee-subtitle-translator`)
- Option 2: Shared Storage (`/storage/emulated/0/ZeeTranslator`) ⭐ **Recommended**

### Q: Do I still need the old `git clone` method?

**A:** No! The old method still works but is **not recommended**:

```bash
# Old method (not recommended):
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
./installer.sh

# New method (recommended):
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

The new method is:
- ✅ Easier (one command)
- ✅ Faster (no git needed)
- ✅ Automatic (downloads everything)

---

## 🎯 Usage & Features

### Q: What subtitle formats are supported?

**A:** 
- ✅ SRT (.srt) - SubRip
- ✅ VTT (.vtt) - WebVTT
- ✅ ASS/SSA (.ass) - Advanced SubStation Alpha

### Q: How many files can I translate at once?

**A:** Unlimited! But for best results:
- **1-20 files**: Use any mode
- **20-50 files**: Use Standard mode
- **50+ files**: Use Safe mode or split into batches

### Q: Which translation mode should I use?

**A:**
- **Safe** - For important content, complex formatting
- **Standard** - Best for most cases (recommended) ⭐
- **Aggressive** - Only for large batches with good connection

### Q: Can I translate to multiple languages at once?

**A:** Not currently. You need to run the program multiple times for different target languages.

### Q: Does it keep the original timing?

**A:** Yes! All timestamps are preserved exactly. Only the text is translated.

### Q: What does "Auto text cleaning" do?

**A:** Automatically removes:
- `[MUSIC]`, `[SOUND EFFECTS]`
- `(DOOR OPENS)`, `(SIGHS)`
- `<i>`, `</i>`, other HTML tags
- `{Translator notes}`

### Q: Can I disable text cleaning?

**A:** Not currently, but it's safe. The cleaning is smart and only removes common patterns. Request this feature on GitHub if needed!

---

## ⚡ Performance & Speed

### Q: Why is translation so slow?

**A:**
1. **Normal speed** (Standard mode):
   - ~1-2 minutes per file (500-1000 lines)
   - Depends on internet speed
   - Google Translate API limitations

2. **Very slow** (10+ min per file):
   - Poor internet connection
   - Rate limiting (too many requests)
   - Server issues

**Solutions:**
- Use WiFi instead of mobile data
- Try different time of day
- Use Safe mode (paradoxically more stable)

### Q: How long does it take to translate X files?

**A:** Rough estimates:

| Files | Lines/File | Mode | Time |
|-------|------------|------|------|
| 1-5 | 500-1000 | Standard | 5-10 min |
| 10-20 | 500-1000 | Standard | 15-30 min |
| 50+ | 500-1000 | Standard | 1-2 hours |
| 100+ | 500-1000 | Safe | 3-5 hours |

**Note:** Actual time varies based on connection and API response.

### Q: Can I speed it up?

**A:** 
1. Use Aggressive mode (risks rate limiting)
2. Use faster internet (wired > WiFi > mobile)
3. Process during off-peak hours
4. Use DeepL API (paid, but faster and higher limits)
5. Split large batches across multiple days

### Q: Why does it say "Slow API response"?

**A:** Google Translate is rate-limiting your requests. This is normal. Solutions:
- Wait between batches
- Use Safe mode
- Try VPN to different region
- Consider DeepL API

---

## 🌐 Translation Quality

### Q: Which is better: Google or DeepL?

**A:**

**Google Translate (Free):**
- ✅ Free, unlimited
- ✅ Supports 100+ languages
- ✅ Good for most content
- ❌ Sometimes awkward phrasing
- ❌ Rate limiting

**DeepL API (Paid):**
- ✅ Better quality
- ✅ More natural phrasing
- ✅ Higher rate limits
- ❌ Requires API key & payment
- ❌ Fewer languages (~30)

**Recommendation:** Start with Google. Upgrade to DeepL for professional work.

### Q: Can I improve translation quality?

**A:**
1. Clean source files first (remove formatting noise)
2. Use shorter sentences in original
3. Fix obvious errors in source
4. Review & edit output manually
5. Consider DeepL for critical content

### Q: Why are some names translated?

**A:** The tool tries to detect proper names (capitalizations, etc.) and skip them, but it's not perfect. Common issues:
- Generic names (like "King", "Doctor")
- Acronyms that look like words
- Non-English names

**Workaround:** Manually fix these in post-processing.

### Q: Can I use custom dictionaries?

**A:** Not yet, but it's planned! Track progress on GitHub Issues.

---

## 🛠️ Troubleshooting

### Q: "Command not found: zeetranslator"

**A:**

**Linux/macOS/Android:**
```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```

**Windows:**
Close and reopen Command Prompt/PowerShell.

**Or:** Open a new terminal window.

**Still not working?**
```bash
# Use traditional method:
cd ~/zee-subtitle-translator  # or your install location
./zee_translator.py
# or
python zee_translator.py
```

### Q: "Module not found" error

**A:**
```bash
# Reinstall dependencies
cd ~/zee-subtitle-translator  # or your install location
pip install --force-reinstall -r requirements.txt

# Or install individually:
pip install srt deep-translator tqdm chardet pysubs2
```

### Q: "Permission denied" error

**A:**

**Linux/macOS/Android:**
```bash
chmod +x zee_translator.py
```

**Windows:**
- Run Command Prompt as Administrator
- Or: `python zee_translator.py` instead of `./zee_translator.py`

### Q: Colors not showing in terminal

**A:**

**Windows:** Use Windows Terminal or PowerShell (better color support)

**Linux/macOS:** Should work by default. If not:
```bash
export TERM=xterm-256color
```

**Termux (Android):** Should work by default.

### Q: "Rate limit exceeded" error

**A:** Google is blocking excessive requests.

**Solutions:**
1. **Wait 1-2 hours** before retrying
2. Use **Safe mode** (slower = fewer requests per minute)
3. Process **smaller batches** (10-20 files max)
4. Use **VPN** to different region
5. Switch to **DeepL API** (higher limits)

### Q: Garbled characters in output

**A:**
1. Check input encoding (should be UTF-8)
2. Convert source to UTF-8 first
3. Try different text editor (e.g., VS Code, Sublime Text)
4. Report as bug if persistent

### Q: Program crashes/freezes

**A:**
1. Check available RAM (close other programs)
2. Process files individually
3. Use Safe mode
4. Check error_log.txt for details
5. Report as bug with log

---

## 📱 Platform-Specific

### Windows

**Q: "Python is not recognized"**

**A:** Python not in PATH.
1. The installer should auto-install Python
2. If manual install needed, check "Add Python to PATH"
3. Restart Command Prompt after installation

**Q: Can I use PowerShell?**

**A:** Yes! PowerShell supports all features and has better color support than Command Prompt. **Recommended!**

### Android (Termux)

**Q: Which Termux version should I use?**

**A:** Install from **F-Droid** or **GitHub**, **NOT** Google Play Store (outdated and broken).

**F-Droid:** https://f-droid.org/packages/com.termux/  
**GitHub:** https://github.com/termux/termux-app/releases

**Q: "Cannot access storage"**

**A:**
```bash
termux-setup-storage
# Click "Allow" in popup
```

**Q: Where should I install on Android?**

**A:** The installer asks you:
- **Option 1:** Termux Home (`~/zee-subtitle-translator`)
  - Faster
  - Not accessible from file manager
  - Deleted if Termux uninstalled
- **Option 2:** Shared Storage (`/storage/emulated/0/ZeeTranslator`) ⭐ **Recommended**
  - Accessible from phone file manager
  - Persists after Termux uninstall
  - Easy to backup/share

**Q: How to access phone files?**

**A:** The installer creates shortcuts:
```bash
cd ~/downloads  # Your Downloads folder
cd ~/movies     # Your Movies folder
cd ~/dcim       # Your Camera folder
```

**Q: App closes during long translation**

**A:**
1. Enable Wake Lock in Termux settings
2. Disable battery optimization for Termux
3. Use tmux: `tmux new -s trans`
4. Keep phone plugged in

### macOS

**Q: "command not found: python"**

**A:** macOS uses `python3`:
```bash
# Check version:
python3 --version

# The installer handles this automatically
```

**Q: "Operation not permitted"**

**A:** Grant terminal permission:
1. System Preferences → Security & Privacy
2. Privacy → Full Disk Access
3. Add Terminal or iTerm2

---

## 🔐 Security & Privacy

### Q: Is my data safe?

**A:** Yes! 
- Script runs locally on your device
- Only subtitle text is sent to translation API
- No personal data collected
- No tracking or analytics
- Open source - you can review the code

### Q: Can Google/DeepL see my subtitles?

**A:** Yes, translation APIs process your text. If you have highly sensitive content:
- Don't use online translation
- Or use local translation models (not supported yet)

### Q: Do you collect any data?

**A:** **No.** Zero data collection. 100% privacy.

### Q: Can I use this commercially?

**A:** Yes! MIT License allows commercial use. But note:
- Google Translate ToS may have limits for heavy commercial use
- DeepL has different pricing for commercial use

---

## 💰 Cost & Licensing

### Q: Is this really free?

**A:** Yes! Free and open-source under MIT License.

### Q: Do I need to pay for Google Translate?

**A:** No. Google Translate (via deep-translator) is free but has rate limits.

### Q: How much does DeepL cost?

**A:** DeepL offers:
- **Free tier**: 500,000 characters/month
- **Pro**: Starting at $5.49/month
- **API**: Pay per character

See [DeepL Pricing](https://www.deepl.com/pro-api)

---

## 🚀 Feature Requests

### Q: Can you add feature X?

**A:** Maybe! Check:
1. [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues) - Is it already requested?
2. Open new issue with `enhancement` label

### Q: Most requested features?

**A:**
1. ✅ Multiple folder support (Added!)
2. ✅ One-line installer (Added!)
3. 🔄 GUI version (Planned)
4. 🔄 Translation memory/cache (Planned)
5. 🔄 Custom dictionaries (Planned)

---

## 📚 Getting More Help

### Still have questions?

1. **Read documentation:**
   - [QUICKSTART.md](QUICKSTART.md) - 5-minute tutorial
   - [GUIDE.md](GUIDE.md) - Detailed guide
   - [README.md](README.md) - Overview

2. **Search existing issues:**
   - [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues)

3. **Ask community:**
   - [GitHub Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions)

4. **Report bugs:**
   - [Create new issue](https://github.com/zeewank/zee-subtitle-translator/issues/new)

---

## 📞 Quick Contact

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues)
- 💡 **Feature Requests**: [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues)
- 💬 **Questions**: [GitHub Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions)

---

**Didn't find your answer?**

Ask in [Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions) or create an [Issue](https://github.com/zeewank/zee-subtitle-translator/issues)!
