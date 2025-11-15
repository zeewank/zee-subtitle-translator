#!/usr/bin/env python3
"""
Zee Subtitle Translator - Universal Launcher
Cross-platform portable launcher that auto-installs dependencies
"""

import sys
import subprocess
import os
from pathlib import Path

def print_header():
    """Print application header"""
    print("\n" + "=" * 60)
    print("    ZEE SUBTITLE TRANSLATOR v1.1")
    print("         Portable Launcher")
    print("=" * 60 + "\n")

def check_python_version():
    """Check if Python version is sufficient"""
    if sys.version_info < (3, 7):
        print("[ERROR] Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        print("\nPlease upgrade Python:")
        print("  - Download from: https://www.python.org/downloads/")
        input("\nPress Enter to exit...")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def check_dependencies():
    """Check and install required dependencies"""
    required_packages = {
        'srt': 'srt',
        'deep_translator': 'deep-translator',
        'tqdm': 'tqdm',
        'chardet': 'chardet',
        'pysubs2': 'pysubs2'
    }
    
    missing_packages = []
    
    print("Checking dependencies...")
    
    for module, package in required_packages.items():
        try:
            __import__(module)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n{'='*60}")
        print("  First-time setup - Installing dependencies")
        print('='*60 + "\n")
        print("Missing packages:", ', '.join(missing_packages))
        print("\nThis will take 1-2 minutes...")
        print("Installing...\n")
        
        try:
            # Upgrade pip first
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', 
                '--upgrade', 'pip', '--quiet', '--disable-pip-version-check'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Install missing packages
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install',
                *missing_packages,
                '--quiet', '--disable-pip-version-check'
            ])
            
            print("✓ Dependencies installed successfully!\n")
            
        except subprocess.CalledProcessError as e:
            print(f"\n[ERROR] Failed to install dependencies: {e}")
            print("\nPlease install manually:")
            print(f"  pip install {' '.join(missing_packages)}")
            input("\nPress Enter to exit...")
            sys.exit(1)
    else:
        print("✓ All dependencies are installed\n")

def run_main_program():
    """Run the main translator program"""
    script_dir = Path(__file__).parent
    main_script = script_dir / "zee_translator.py"
    
    if not main_script.exists():
        print(f"[ERROR] Main script not found: {main_script}")
        print("\nPlease ensure zee_translator.py is in the same directory.")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    print("Starting Zee Subtitle Translator...\n")
    print("=" * 60 + "\n")
    
    try:
        # Import and run the main module
        sys.path.insert(0, str(script_dir))
        import zee_translator
        
        # Run main function
        zee_translator.main()
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n[ERROR] Program crashed: {e}")
        print("\nCheck error_log.txt for details.")
        
        # Log error
        with open("error_log.txt", "a", encoding="utf-8") as f:
            import traceback
            f.write(f"\n[LAUNCHER ERROR] {traceback.format_exc()}\n")
        
        input("\nPress Enter to exit...")
        sys.exit(1)

def main():
    """Main launcher function"""
    print_header()
    
    # Check Python version
    check_python_version()
    
    # Check and install dependencies
    check_dependencies()
    
    # Run main program
    run_main_program()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)
