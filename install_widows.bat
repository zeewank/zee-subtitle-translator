@echo off
REM ================================================================
REM Zee Subtitle Translator - Traditional Installer for Windows
REM For users who already downloaded the ZIP file
REM Run this inside the project folder
REM ================================================================

setlocal enabledelayedexpansion
title Zee Subtitle Translator - Traditional Installer
color 0B

REM Get script directory
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

cls
echo.
echo ============================================================
echo   ZEE SUBTITLE TRANSLATOR - TRADITIONAL INSTALLER
echo            Setup from Local Folder
echo ============================================================
echo.
echo [OK] Installing from local directory...
echo Location: %SCRIPT_DIR%
echo.

REM Check if in correct directory
if not exist "zee_translator.py" (
    echo [ERROR] zee_translator.py not found!
    echo.
    echo Please run this script inside the project folder.
    echo Example:
    echo   cd zee-subtitle-translator
    echo   install_windows.bat
    echo.
    pause
    exit /b 1
)

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo.
    echo Please install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('python --version 2^>^&1') do set PYTHON_VER=%%v
echo [OK] Python !PYTHON_VER! found
echo.

REM Check requirements.txt
if not exist "requirements.txt" (
    echo [ERROR] requirements.txt not found!
    echo.
    echo Please make sure you're in the correct directory.
    pause
    exit /b 1
)

REM Install dependencies
echo ============================================================
echo [1/3] Installing Python dependencies...
echo This may take 1-2 minutes...
echo ============================================================
echo.

python -m pip install --upgrade pip --quiet --disable-pip-version-check 2>nul

python -m pip install --quiet --disable-pip-version-check -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    echo.
    echo Please try manually:
    echo   pip install -r requirements.txt
    pause
    exit /b 1
)

echo [OK] Dependencies installed!
echo.

REM Make script accessible
echo ============================================================
echo [2/3] Setting up global command...
echo ============================================================
echo.

REM Create batch file in WindowsApps
set "BATCH_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps"
set "BATCH_FILE=%BATCH_DIR%\zeetranslator.bat"

if not exist "%BATCH_DIR%" mkdir "%BATCH_DIR%"

echo @echo off > "%BATCH_FILE%"
echo python "%SCRIPT_DIR%zee_translator.py" %%* >> "%BATCH_FILE%"

echo [OK] Global command configured!
echo.

REM Test installation
echo ============================================================
echo [3/3] Testing installation...
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
echo   Location: %SCRIPT_DIR%
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
echo   cd %SCRIPT_DIR%
echo   python zee_translator.py
echo.
echo   Or double-click:
echo   zee_translator.py
echo.
echo Documentation:
echo   README:      notepad README.md
echo   Quick Start: notepad QUICKSTART.md
echo   Full Guide:  notepad GUIDE.md
echo.
echo Uninstall:
echo   uninstall.bat
echo.
echo Happy translating! :)
echo.
pause
