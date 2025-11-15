# Android Storage Guide for Termux

## Problem: "Permission Denied" Outside Termux Home

### Situation

``` bash
~$ pwd
/data/data/com.termux/files/home

~$ cd ..
files$ cd ..
com.termux$ cd ..
data$ ls
ls: cannot open directory '.': Permission denied  ← ERROR!
```

### Why Does This Happen?

**This is NOT a bug --- it's Android's design!**

## Android Storage Structure

    Android Storage Structure:
    ├── /data/                          ← System area (protected)
    │   └── data/
    │       └── com.termux/             ← Termux app private area
    │           └── files/
    │               └── home/           ← Termux ~ (ISOLATED)
    │                   └── your-files
    │
    └── /storage/
        └── emulated/
            └── 0/                      ← Shared storage (accessible)
                ├── Download/
                ├── Movies/
                ├── DCIM/
                └── ...

### Explanation

**1. Termux Home in `/data/data/`** - Location:
`/data/data/com.termux/files/home/` - This is the Termux "jail" (app
sandbox) - Only Termux can access it - Protected by Android's security
model

**2. Shared Storage in `/storage/emulated/0/`** - Location: your phone's
internal storage - Accessible by all apps (with permission) - Visible to
your file manager - This is what you usually see as "Internal Storage"

### Why Permission Denied?

``` bash
/data/data/com.termux/  ← You are here (in Termux jail)
         ↓
       cd ..
         ↓
/data/data/             ← Still inside system area
         ↓
       cd ..
         ↓
/data/                  ← BLOCKED! Need root access
```

**Android Rules:** - Every app has a private folder in `/data/data/` -
App A cannot access App B's folder - Root access is required to leave
the sandbox - This is Android protection, not a Termux bug

## Solution: Clone in Accessible Storage

### ❌ WRONG: Clone in Termux Home

``` bash
cd ~
git clone https://github.com/zeewank/zee-subtitle-translator.git
cd zee-subtitle-translator
```

**Problems:** - Folder lives in `/data/data/com.termux/files/home/` -
Cannot be accessed by phone file manager - Cannot be accessed by other
apps - Deleted if you uninstall Termux

### ✅ CORRECT: Clone in Shared Storage

``` bash
cd /storage/emulated/0/
git clone https://github.com/zeewank/zee-subtitle-translator.git ZeeTranslator
cd ZeeTranslator
```

**Benefits:** - Folder located at `Internal Storage/ZeeTranslator/` -
Fully accessible by file manager - Usable by other apps (with
permission) - Persists even if Termux is uninstalled - Easy to back up
or share

## Updated Setup Script

The new `setup_termux.sh` script is fixed and improved.

**Features:** 1. Asks user where to install: - Option 1: Termux Home
(fast but isolated) - Option 2: Shared Storage (recommended, accessible)

2.  Auto-configuration based on chosen location\
3.  Provides pros/cons for each option

## Manual Method: Move Project to Shared Storage

If you already cloned inside Termux home:

``` bash
# 1. Move to shared storage
cd /storage/emulated/0/

# 2. Copy project
cp -r ~/zee-subtitle-translator ./ZeeTranslator

# 3. Update alias
nano ~/.bashrc

# 4. Change path from:
alias zeetranslator='python ~/zee-subtitle-translator/zee_translator.py'

# To:
alias zeetranslator='python /storage/emulated/0/ZeeTranslator/zee_translator.py'

# 5. Save & reload
source ~/.bashrc

# 6. Test
zeetranslator
```

## Access Project from Phone File Manager

After installing in Shared Storage:

1.  Open **File Manager**
2.  Go to **Internal Storage**
3.  Open **ZeeTranslator** folder
4.  Done!

**Full Path:**

    Internal Storage/ZeeTranslator/
    ├── zee_translator.py
    ├── installer.sh
    ├── setup_termux.sh
    ├── requirements.txt
    └── ...

## Storage Shortcuts in Termux

Setup script automatically creates shortcuts:

``` bash
~/downloads → /storage/emulated/0/Download
~/movies    → /storage/emulated/0/Movies
~/dcim      → /storage/emulated/0/DCIM
```

**Usage:**

``` bash
ls ~/downloads
zeetranslator ~/movies/MyMovie/
cd ~/dcim
```

## Comparison: Termux Home vs Shared Storage

  ----------------------------------------------------------------------------------------
  Aspect              Termux Home                           Shared Storage
  ------------------- ------------------------------------- ------------------------------
  **Path**            `~/`                                  `/storage/emulated/0/`

  **Real Path**       `/data/data/com.termux/files/home/`   `/storage/emulated/0/`

  **Speed**           Faster                                Slightly slower

  **Accessibility**   Termux only                           All apps + file manager

  **Persistence**     Lost on uninstall                     Persists

  **Backup**          Difficult                             Easy

  **Share Files**     Difficult                             Easy

  **Permission**      No permission needed                  Requires storage permission
  ----------------------------------------------------------------------------------------

## FAQ

**Q: Why doesn't Termux install in a normal folder like other apps?**\
A: All Android apps are the same---each has a private folder under
`/data/data/`.

**Q: Can I root my phone to access `/data/data/`?**\
A: Yes, but not recommended due to security risks. Better to use Shared
Storage.

**Q: Will my project be deleted if I uninstall Termux?**\
A:\
- If inside Termux Home: **Yes, deleted**\
- If inside Shared Storage: **No, remains**

**Q: What's the best installation location?**\
A: **Shared Storage** (Option 2) for better accessibility & safety.

**Q: Is Shared Storage slower?**\
A: Slightly, but not noticeable in typical use.

**Q: Can I move the project after installing?**\
A: Yes---copy folder and update alias.

**Q: What is the `~/downloads` shortcut?**\
A: A symbolic link to `/storage/emulated/0/Download`.

## Troubleshooting

**Problem: "Permission denied" accessing `/storage/emulated/0/`**

Solution:

``` bash
termux-setup-storage
# Tap "Allow" on the permission popup
```

**Problem: `ZeeTranslator` not visible in file manager**

Solution:

``` bash
ls /storage/emulated/0/ZeeTranslator
```

**Problem: "No such file or directory" when using `cd ~/downloads`**

Solution:

``` bash
ln -sf /storage/emulated/0/Download ~/downloads
```

------------------------------------------------------------------------

**Bottom Line:**\
Android isolates apps for security. Termux lives in `/data/data/`, while
your phone storage is `/storage/emulated/0/`.\
Clone your project in Shared Storage for easy access.

**Recommended:** Use the updated `setup_termux.sh` and choose Option 2
(Shared Storage).
