@echo off
REM ================================================================
REM Zee Subtitle Translator - Windows Installer
REM Automatic setup for Windows users
REM ================================================================

title Zee Subtitle Translator - Installer
color 0B

echo.
echo ========================================================
echo     ZEE SUBTITLE TRANSLATOR INSTALLER
echo                Version 1
echo ========================================================
echo.

REM Check Python installation
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo [OK] Python detected
python --version
echo.

REM Check pip
echo [2/4] Checking pip installation...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [!] pip not found, installing...
    python -m ensurepip --upgrade
)
echo [OK] pip is ready
echo.

REM Upgrade pip
echo [3/4] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [OK] pip upgraded
echo.

REM Install dependencies
echo [4/4] Installing required packages...
echo This may take a few minutes...
echo.

python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [X] Failed to install some dependencies!
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo [OK] All dependencies installed successfully!
echo.

REM Create launcher script
echo @echo off > run_translator.bat
echo python zee_translator.py %%* >> run_translator.bat

echo ========================================================
echo     Installation completed successfully!
echo ========================================================
echo.
echo Quick Start:
echo   1. Double-click "run_translator.bat"
echo   2. Or run: python zee_translator.py
echo.
echo For detailed instructions, see README.md
echo ========================================================
echo.
pause
