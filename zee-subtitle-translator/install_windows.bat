@echo off
REM ================================================================
REM Zee Subtitle Translator - Bootstrap Installer for Windows
REM One-click auto-installer - No git required
REM Downloads directly from GitHub
REM ================================================================

setlocal enabledelayedexpansion
title Zee Subtitle Translator - Auto Installer
color 0B

REM Configuration
set "REPO_URL=https://github.com/zeewank/zee-subtitle-translator"
set "ZIP_URL=https://github.com/zeewank/zee-subtitle-translator/archive/refs/heads/main.zip"
set "INSTALL_DIR=%USERPROFILE%\zee-subtitle-translator"
set "TEMP_DIR=%TEMP%\zee-installer-%RANDOM%"

cls
echo.
echo ============================================================
echo   ZEE SUBTITLE TRANSLATOR - AUTO INSTALLER
echo            Download ^& Setup Automatically
echo ============================================================
echo.
echo [OK] Starting automatic installation...
echo.

REM Check PowerShell
powershell -Command "Write-Host 'PowerShell OK'" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] PowerShell not available!
    echo.
    echo This installer requires PowerShell 3.0 or higher.
    echo Please update Windows or install PowerShell.
    pause
    exit /b 1
)

echo [OK] PowerShell found
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo.
    echo This tool requires Python 3.7 or higher.
    echo.
    echo Downloading Python installer...
    echo Please wait...
    echo.
    
    set "PYTHON_URL=https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe"
    set "PYTHON_INSTALLER=%TEMP%\python-installer.exe"
    
    powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'}" 2>nul
    
    if not exist "%PYTHON_INSTALLER%" (
        echo [ERROR] Failed to download Python installer.
        echo.
        echo Please install Python manually from:
        echo https://www.python.org/downloads/
        echo.
        echo IMPORTANT: Check "Add Python to PATH" during installation!
        pause
        exit /b 1
    )
    
    echo [OK] Python installer downloaded
    echo.
    echo [INFO] Installing Python...
    echo Please wait 2-3 minutes...
    echo.
    
    "%PYTHON_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_pip=1
    timeout /t 5 /nobreak >nul
    
    REM Refresh PATH
    call :refresh_env
    
    python --version >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Python installation failed.
        echo.
        echo Please install Python manually and run this installer again.
        pause
        exit /b 1
    )
    
    del /f /q "%PYTHON_INSTALLER%" 2>nul
    echo [OK] Python installed successfully!
    echo.
)

for /f "tokens=2" %%v in ('python --version 2^>^&1') do set PYTHON_VER=%%v
echo [OK] Python !PYTHON_VER! found
echo.

REM Check if already installed
if exist "%INSTALL_DIR%" (
    echo.
    echo [WARNING] Zee Translator already installed at:
    echo %INSTALL_DIR%
    echo.
    set /p REINSTALL="Reinstall? (y/n): "
    if /i not "!REINSTALL!"=="y" (
        echo Installation cancelled.
        pause
        exit /b 0
    )
    echo.
    echo [INFO] Removing old installation...
    rmdir /s /q "%INSTALL_DIR%" 2>nul
)

REM Create temp directory
mkdir "%TEMP_DIR%" 2>nul

echo ============================================================
echo [1/5] Downloading project from GitHub...
echo URL: %ZIP_URL%
echo.
echo This may take 1-2 minutes depending on your connection...
echo ============================================================
echo.

REM Download using PowerShell
powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Write-Host 'Downloading...'; $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri '%ZIP_URL%' -OutFile '%TEMP_DIR%\zee-translator.zip'}"

if not exist "%TEMP_DIR%\zee-translator.zip" (
    echo [ERROR] Download failed!
    echo.
    echo Please check your internet connection and try again.
    rmdir /s /q "%TEMP_DIR%" 2>nul
    pause
    exit /b 1
)

echo.
echo [OK] Download complete!
echo.

echo ============================================================
echo [2/5] Extracting files...
echo ============================================================
echo.

REM Extract using PowerShell
powershell -Command "Expand-Archive -Path '%TEMP_DIR%\zee-translator.zip' -DestinationPath '%TEMP_DIR%' -Force"

if errorlevel 1 (
    echo [ERROR] Extraction failed!
    rmdir /s /q "%TEMP_DIR%" 2>nul
    pause
    exit /b 1
)

REM Find extracted directory
for /d %%i in ("%TEMP_DIR%\zee-subtitle-translator-*") do set "EXTRACTED_DIR=%%i"

if not defined EXTRACTED_DIR (
    echo [ERROR] Could not find extracted directory!
    rmdir /s /q "%TEMP_DIR%" 2>nul
    pause
    exit /b 1
)

REM Move to install directory
move "%EXTRACTED_DIR%" "%INSTALL_DIR%" >nul

echo [OK] Files extracted to: %INSTALL_DIR%
echo.

REM Clean up temp
rmdir /s /q "%TEMP_DIR%" 2>nul

REM Install dependencies
cd /d "%INSTALL_DIR%"

echo ============================================================
echo [3/5] Installing Python dependencies...
echo This may take 1-2 minutes...
echo ============================================================
echo.

python -m pip install --upgrade pip --quiet --disable-pip-version-check 2>nul

python -m pip install --quiet --disable-pip-version-check -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    echo.
    echo Please try manually:
    echo   cd %INSTALL_DIR%
    echo   pip install -r requirements.txt
    pause
    exit /b 1
)

echo [OK] Dependencies installed!
echo.

echo ============================================================
echo [4/5] Setting up global command...
echo ============================================================
echo.

REM Create batch file in WindowsApps
set "BATCH_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps"
set "BATCH_FILE=%BATCH_DIR%\zeetranslator.bat"

if not exist "%BATCH_DIR%" mkdir "%BATCH_DIR%"

echo @echo off > "%BATCH_FILE%"
echo python "%INSTALL_DIR%\zee_translator.py" %%* >> "%BATCH_FILE%"

echo [OK] Global command configured!
echo.

echo ============================================================
echo [5/5] Testing installation...
echo ============================================================
echo.

python -c "import srt, deep_translator, tqdm, chardet, pysubs2" 2>nul
if errorlevel 1 (
    echo [WARNING] Some dependencies may need attention
) else (
    echo [OK] All dependencies working!
)
echo.

REM Success message
echo.
echo ============================================================
echo   INSTALLATION COMPLETED SUCCESSFULLY!
echo ============================================================
echo.
echo Installation Details:
echo   Location: %INSTALL_DIR%
echo   Command:  zeetranslator
echo.
echo Quick Start:
echo.
echo   1. Close and reopen Command Prompt / PowerShell
echo.
echo   2. Then run:
echo      zeetranslator
echo.
echo Alternative (without global command):
echo   cd %INSTALL_DIR%
echo   python zee_translator.py
echo.
echo Documentation:
echo   README:      notepad %INSTALL_DIR%\README.md
echo   Quick Start: notepad %INSTALL_DIR%\QUICKSTART.md
echo   Full Guide:  notepad %INSTALL_DIR%\GUIDE.md
echo.
echo Uninstall:
echo   cd %INSTALL_DIR% ^&^& uninstall.sh
echo.
echo Happy translating! :)
echo.
pause
goto :eof

REM Function to refresh environment variables
:refresh_env
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "USER_PATH=%%b"
for /f "tokens=2*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH 2^>nul') do set "SYSTEM_PATH=%%b"
set "PATH=%SYSTEM_PATH%;%USER_PATH%"
goto :eof
