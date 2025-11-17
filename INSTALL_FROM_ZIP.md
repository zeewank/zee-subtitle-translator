# 📦 Installation Guide - For Users Who Downloaded ZIP (English Version)

This guide is for users who **downloaded the project as a ZIP file**
from GitHub instead of using the one-liner command.

------------------------------------------------------------------------

## 🎯 How to Install After Downloading ZIP

### 🐧 Linux / macOS

#### 1. Extract the ZIP file

``` bash
cd ~/Downloads/
unzip zee-subtitle-translator-main.zip
cd zee-subtitle-translator-main/
```

#### 2. Run the installer

``` bash
chmod +x installer.sh
./installer.sh
```

#### 3. Activate the command

``` bash
source ~/.bashrc   # or source ~/.zshrc for macOS
```

#### 4. Run the program

``` bash
zeetranslator
```

------------------------------------------------------------------------

### 🪟 Windows

#### 1. Extract the ZIP file

-   Right-click ZIP file\
-   Choose **"Extract All..."**\
-   Select location\
-   Click **Extract**

#### 2. Open the extracted folder

    C:\Users\YourName\zee-subtitle-translator-main\

#### 3. Run the installer

Double-click:

    install_windows.bat

Or Command Prompt:

``` cmd
cd C:\Users\YourName\zee-subtitle-translator-main
install_windows.bat
```

#### 4. Restart Command Prompt

#### 5. Run the program

``` cmd
zeetranslator
```

------------------------------------------------------------------------

### 📱 Android (Termux)

#### 1. Extract ZIP using File Manager or ZArchiver

Example path:

    /storage/emulated/0/Download/zee-subtitle-translator-main/

#### 2. Open Termux

#### 3. Go to the project folder

``` bash
cd /storage/emulated/0/Download/zee-subtitle-translator-main/
```

Or:

``` bash
cd ~/storage/downloads/zee-subtitle-translator-main/
```

#### 4. Run the installer

``` bash
chmod +x setup_termux.sh
./setup_termux.sh
```

#### 5. Activate the command

``` bash
source ~/.bashrc
```

Or restart Termux.

#### 6. Run the program

``` bash
zeetranslator
```

------------------------------------------------------------------------

## 🔧 Troubleshooting

### Error: "installer.sh not found"

Cause: Not inside project folder.

Solution:

``` bash
cd zee-subtitle-translator-main/
ls
./installer.sh
```

------------------------------------------------------------------------

### Error: "Permission denied"

Cause: File not executable.

Solution:

``` bash
chmod +x installer.sh
./installer.sh
```

------------------------------------------------------------------------

### Error: "Python not found"

Cause: Python is missing.

Linux:

``` bash
sudo apt install python3 python3-pip
```

macOS:

``` bash
brew install python3
```

Windows: Download from python.org (check **Add to PATH**)\
Android:

``` bash
pkg install python
```

------------------------------------------------------------------------

### Error: "requirements.txt not found"

Cause: Wrong folder.

Solution:

``` bash
ls   # confirm files exist
```

------------------------------------------------------------------------

### Windows installer error

Run as Administrator or disable antivirus.

------------------------------------------------------------------------

### Android storage error

``` bash
termux-setup-storage
```

------------------------------------------------------------------------

## 📂 Extracted File Structure

    zee-subtitle-translator-main/
    ├── zee_translator.py
    ├── requirements.txt
    ├── installer.sh
    ├── install_windows.bat
    ├── setup_termux.sh
    ├── bootstrap_installer.sh
    ├── bootstrap_installer.bat
    ├── bootstrap_termux.sh
    ├── uninstall.sh
    ├── README.md
    ├── QUICKSTART.md
    ├── GUIDE.md
    └── ...

------------------------------------------------------------------------

## 🎯 Installer Files to Use

  Platform   File
  ---------- -----------------------
  Linux      `installer.sh`
  macOS      `installer.sh`
  Windows    `install_windows.bat`
  Android    `setup_termux.sh`

------------------------------------------------------------------------

## 🆚 Installer vs Bootstrap

  -----------------------------------------------------------------------
                          Installer               Bootstrap
  ----------------------- ----------------------- -----------------------
  For                     ZIP users               Non-ZIP users

  How                     Run inside folder       Copy-paste command

  Downloads project       No                      Yes

  Files                   installer.sh,           bootstrap installers
                          install_windows.bat,    
                          setup_termux.sh         
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## ✅ Verify Installation

``` bash
zeetranslator
```

Expected output:

    ZEE SUBTITLE TRANSLATOR v1

    1. Translate Subtitles
    2. UI Language Settings
    3. Exit

------------------------------------------------------------------------

## 🔗 Useful Links

GitHub, Issues, Documentation.

------------------------------------------------------------------------

## 💡 Tips

-   Keep project folder\
-   Read documentation\
-   Test with small files

------------------------------------------------------------------------

Enjoy using Zee Subtitle Translator! 🎬
