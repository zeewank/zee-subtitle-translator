@echo off
REM ================================================================
REM Zee Subtitle Translator - Windows Installer (FIXED)
REM Version 1.1 - Now with global command support!
REM ================================================================

title Zee Subtitle Translator - Installer
color 0B

echo.
echo ========================================================
echo     ZEE SUBTITLE TRANSLATOR INSTALLER
echo                Version 1.1
echo ========================================================
echo.

REM Check Python installation
echo [1/5] Checking Python installation...
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
echo [2/5] Checking pip installation...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [!] pip not found, installing...
    python -m ensurepip --upgrade
)
echo [OK] pip is ready
echo.

REM Upgrade pip
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [OK] pip upgraded
echo.

REM Install dependencies
echo [4/5] Installing required packages...
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

REM [5/5] Create global batch file
echo [5/5] Setting up global 'zeetranslator' command...

REM Get current directory
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_PATH=%SCRIPT_DIR%zee_translator.py"

REM Create batch file in Windows directory (requires admin)
REM Alternative: User's local bin directory
set "BATCH_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps"
set "BATCH_FILE=%BATCH_DIR%\zeetranslator.bat"

REM Check if directory exists
if not exist "%BATCH_DIR%" (
    mkdir "%BATCH_DIR%"
)

REM Create the batch file
echo @echo off > "%BATCH_FILE%"
echo python "%SCRIPT_PATH%" %%* >> "%BATCH_FILE%"

if exist "%BATCH_FILE%" (
    echo [OK] Global command 'zeetranslator' created successfully!
    echo.
    echo You can now type 'zeetranslator' from anywhere!
) else (
    echo [!] Could not create global command.
    echo You can still use: python "%SCRIPT_PATH%"
)
echo.

REM Create launcher script in current directory
echo @echo off > run_translator.bat
echo python zee_translator.py %%* >> run_translator.bat

echo ========================================================
echo     Installation completed successfully!
echo ========================================================
echo.
echo Quick Start:
echo   1. Type 'zeetranslator' from any directory
echo   2. Or double-click "run_translator.bat"
echo   3. Or run: python zee_translator.py
echo.
echo Usage Examples:
echo   zeetranslator                    - Interactive mode
echo   zeetranslator "C:\Videos\Subs"   - Translate folder
echo.
echo For detailed instructions, see README.md
echo ========================================================
echo.
pause
