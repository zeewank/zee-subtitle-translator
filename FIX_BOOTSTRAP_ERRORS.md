# 🔧 Fix Bootstrap Installation Errors 

## 🔴 Problem 1: Windows PowerShell Error

### Error Shown:

    PS C:\Users\user> powershell
    Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat"
    ...
    Oops, something went wrong.
    System.IO.IOException: The handle is invalid.

### Cause:

1.  **Incorrect URL** -- The file on GitHub is named
    `bootstrap_installer.bat`, not `install_windows.bat`.
2.  **Nested PowerShell** -- User executed `powershell` inside
    PowerShell.
3.  **PSReadLine console issue** -- Console handle problem.

### ✅ SOLUTION:

#### Solution 1: Use the Correct URL

**Open PowerShell (not inside PowerShell), then paste:**

``` powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

**IMPORTANT:** The file on GitHub is `bootstrap_installer.bat`, **NOT**
`install_windows.bat`.

#### Solution 2: Use Command Prompt

``` cmd
curl -o "%TEMP%\zee-install.bat" https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat && "%TEMP%\zee-install.bat"
```

#### Solution 3: Manual Download

1.  Download:
    https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat\
2.  Save as `bootstrap_installer.bat`\
3.  Double‑click to run

------------------------------------------------------------------------

## 🔴 Problem 2: Android/Termux 404 Error

### Error Shown:

``` bash
$ curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
bash: line 1: 404: command not found
```

### Cause:

**Incorrect URL** -- File is named `bootstrap_termux.sh`, not
`setup_termux.sh`.

### ✅ SOLUTION:

Use the correct URL:

``` bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_termux.sh | bash
```

**IMPORTANT:** File is `bootstrap_termux.sh`, **NOT** `setup_termux.sh`.

------------------------------------------------------------------------

## 📝 Summary: Correct File Names

### ❌ WRONG (Old Names)

  Platform   Wrong Name
  ---------- -----------------------
  Windows    `install_windows.bat`
  Android    `setup_termux.sh`

### ✅ CORRECT (Current Names)

  -----------------------------------------------------------------------------------------------------------------------------------------------------------
  Platform                    File Name                      URL
  --------------------------- ------------------------------ ------------------------------------------------------------------------------------------------
  **Linux/macOS**             `bootstrap_installer.sh`       https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.sh

  **Windows**                 `bootstrap_installer.bat`      https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat

  **Android**                 `bootstrap_termux.sh`          https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_termux.sh
  -----------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🎯 Correct Installation Commands

### Linux / macOS

``` bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.sh | bash
```

### Windows (PowerShell)

``` powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

### Windows (Command Prompt)

``` cmd
curl -o "%TEMP%\zee-install.bat" https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat && "%TEMP%\zee-install.bat"
```

### Android (Termux)

``` bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_termux.sh | bash
```

------------------------------------------------------------------------

## 🔄 Difference: Bootstrap vs Traditional Installer

There are **two types of installers** in this project:

### 1. **Bootstrap Installer** (Auto-download)

**For:** Users who **have NOT downloaded** the project.

  Platform      File
  ------------- ---------------------------
  Linux/macOS   `bootstrap_installer.sh`
  Windows       `bootstrap_installer.bat`
  Android       `bootstrap_termux.sh`

**Usage:** Copy-paste one-liner command.

Process:\
1. Downloads the project\
2. Extracts ZIP\
3. Installs dependencies\
4. Sets up command

------------------------------------------------------------------------

### 2. **Traditional Installer** (Local installation)

**For:** Users who **already downloaded ZIP**.

  Platform      File
  ------------- -----------------------
  Linux/macOS   `installer.sh`
  Windows       `install_windows.bat`
  Android       `setup_termux.sh`

**Usage:** Run inside the project folder.

------------------------------------------------------------------------

## 🛠️ Additional Troubleshooting

### Windows: "Invoke-WebRequest is not recognized"

Use CMD:

``` cmd
curl -o "%TEMP%\zee-install.bat" https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/bootstrap_installer.bat && "%TEMP%\zee-install.bat"
```

------------------------------------------------------------------------

### Termux: "curl: command not found"

``` bash
pkg install curl
```

------------------------------------------------------------------------

### All Platforms: "404 Not Found"

Causes: - Wrong URL - File not uploaded to GitHub yet

Solutions: 1. Check GitHub repository\
2. If file doesn't exist, use **Traditional Installer**

------------------------------------------------------------------------

## ✅ Verification

``` bash
zeetranslator
```

The program menu should appear.

------------------------------------------------------------------------

## 📧 Need Help?

Submit issue:\
https://github.com/zeewank/zee-subtitle-translator/issues

Include: Platform + Error + Installation method.

------------------------------------------------------------------------

**Good luck! 🚀**
