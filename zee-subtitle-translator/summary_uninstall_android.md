# Summary: Uninstall Script & Android Storage Fix

## Issue 1: No Uninstall Script

### Problem

The user did not have a clean way to uninstall the tool.

### Solution

Created an `uninstall.sh` script that: - Removes global command
`zeetranslator` - Removes alias from `.bashrc` / `.zshrc` - Removes
Termux widget - Removes config file (`.subtitletrans.conf`) - Creates
backup of shell config - Bilingual-ready (English/Indonesian
originally) - Safe (does not delete the project folder or packages)

### Usage

``` bash
cd ~/zee-subtitle-translator
chmod +x uninstall.sh
./uninstall.sh
```

### What It Does

1.  Asks for confirmation before proceeding\
2.  Removes alias from shell config (and creates backup)\
3.  Removes Windows batch file (if exists)\
4.  Removes Termux widget (if exists)\
5.  Deletes config file\
6.  Provides instructions for:
    -   Manually deleting the project folder\
    -   Manually removing Python packages

### What It Does NOT Delete

-   Project folder (user decides)
-   Python packages (user decides)
-   Backup files (for safety)

------------------------------------------------------------------------

## Issue 2: Android "Permission Denied" Problem

### Problem

``` bash
~$ pwd
/data/data/com.termux/files/home

~$ cd ../..
data$ ls
Permission denied  ← WHY???
```

### Root Cause

**This is NOT a bug!** It is the Android security model.

**Explanation:**

    /data/data/com.termux/  ← Termux app sandbox (isolated)
             ↓ cd ..
    /data/data/            ← System area (still protected)
             ↓ cd ..
    /data/                 ← BLOCKED (requires root)

Every Android app has its own "jail" in `/data/data/`.\
An app cannot escape this jail without root access.

### Why This Matters

If you clone the project in Termux home (`~`): - Cannot be accessed from
phone file manager - Cannot be accessed by other apps - Deleted if
Termux is uninstalled - Difficult to back up or share

### Solution: Install in Shared Storage

**Android Storage Structure:**

    /data/data/com.termux/files/home/  ← Termux home (isolated)
    /storage/emulated/0/               ← Shared storage (accessible)

**Updated Setup Script (`setup_termux.sh`):** Now it:

1.  **Asks the user** where to install:

        1. Termux Home (~)
           ✓ Faster
           ✗ Not accessible from file manager
           ✗ Deleted when Termux is uninstalled

        2. Shared Storage (Recommended)
           ✓ Accessible from phone file manager
           ✓ Persists even if Termux is uninstalled
           ✓ Easy to back up / share

2.  **Installs to chosen location:**

    -   Option 1 →
        `/data/data/com.termux/files/home/zee-subtitle-translator/`
    -   Option 2 → `/storage/emulated/0/ZeeTranslator/` ← Recommended

3.  **Creates shortcuts:**

    ``` bash
    ~/downloads → /storage/emulated/0/Download
    ~/movies    → /storage/emulated/0/Movies
    ~/dcim      → /storage/emulated/0/DCIM
    ```

### User Experience

**Before (Bad):**

``` bash
pkg install git
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
# Installed in Termux home
# Not accessible from phone file manager
```

**After (Good):**

``` bash
./setup_termux.sh
# Script asks: "Choose location [1-2] (default 2): "
# User selects 2 (Shared Storage)
# Installed at /storage/emulated/0/ZeeTranslator/
# Now accessible from file manager
```

### Access via File Manager

After installing in Shared Storage: 1. Open **File Manager**\
2. Go to **Internal Storage**\
3. Locate **ZeeTranslator**\
4. Done --- view and edit files easily

Path:

    Internal Storage/ZeeTranslator/

### Migration Guide

If previously installed in Termux home:

``` bash
# Copy to shared storage
cp -r ~/zee-subtitle-translator /storage/emulated/0/ZeeTranslator

# Update alias
nano ~/.bashrc
# Update this:
alias zeetranslator='python /storage/emulated/0/ZeeTranslator/zee_translator.py'

# Reload
source ~/.bashrc

# Test
zeetranslator
```

------------------------------------------------------------------------

## Files Created / Updated

### New Files:

1.  `uninstall.sh` --- uninstaller script\
2.  `ANDROID_STORAGE_GUIDE.md` --- detailed Android storage info

### Updated Files:

1.  `setup_termux.sh` --- now asks for installation location\
2.  `README.md` --- added uninstall section + Android info

------------------------------------------------------------------------

## Comparison: Old vs New

### Old Android Setup

``` bash
cd ~
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
pip install -r requirements.txt
./zee_translator.py
```

**Issues:** - Installed inside Termux home (isolated) - Not visible from
phone file manager - Deleted on uninstall - No uninstall script

### New Android Setup

``` bash
./setup_termux.sh
# Choose location: 2 (Shared Storage)
zeetranslator
```

**Benefits:** - User chooses install location\
- File-manager friendly (Option 2)\
- Persists after Termux uninstall\
- Has uninstaller

------------------------------------------------------------------------

## Testing Checklist

### Uninstall Script

-   Removes alias\
-   Removes widget\
-   Backs up shell config\
-   Deletes config file\
-   Leaves project folder intact\
-   Works on Linux/macOS/Android

### Android Setup

-   Prompts for storage location\
-   Installs correctly to both targets\
-   Creates shortcuts\
-   Works with global command\
-   Accessible from file manager\
-   Persists on uninstall (Option 2)

------------------------------------------------------------------------

## Documentation

### For Users

**Quick Uninstall:**

``` bash
./uninstall.sh
```

**Android Storage Help:**\
Read `ANDROID_STORAGE_GUIDE.md`.

**Best Practices:** - On Android: Install in Shared Storage\
- Back up the project periodically\
- Use shortcuts like `~/downloads`

### For Developers

**Uninstall Logic:** - Confirm\
- Backup\
- Remove entries\
- Clean up\
- Notify user

**Android Storage Notes:** - Termux home =
`/data/data/com.termux/files/home/`\
- Shared storage = `/storage/emulated/0/`\
- Shared storage provides best user experience

------------------------------------------------------------------------

## Final Summary

**Uninstaller:**\
- Fully implemented\
- Safe + documented

**Android Fix:**\
- Clear explanation\
- Better installation flow\
- Improved UX

Everything is now polished and working correctly.
