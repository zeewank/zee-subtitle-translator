#!/data/data/com.termux/files/usr/bin/bash
# ================================================================
# Zee Subtitle Translator - Portable Launcher for Android/Termux
# Just run this file - no installation needed!
# ================================================================

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════╗
║      ZEE SUBTITLE TRANSLATOR v1.1         ║
║         Android Portable Launcher         ║
╚═══════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Check if we're in Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo -e "${RED}[ERROR] This script must be run in Termux!${NC}"
    echo ""
    echo "Please install Termux from F-Droid:"
    echo "  https://f-droid.org/packages/com.termux/"
    echo ""
    exit 1
fi

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo -e "${YELLOW}[SETUP] Python not found. Installing...${NC}"
    echo ""
    
    # Update packages
    pkg update -y -q
    
    # Install Python
    pkg install -y -q python || {
        echo -e "${RED}[ERROR] Failed to install Python${NC}"
        exit 1
    }
    
    echo -e "${GREEN}✓ Python installed${NC}"
fi

echo -e "${GREEN}✓ Python found${NC}"

# Check storage access
if [ ! -d "/storage/emulated/0" ]; then
    echo ""
    echo -e "${YELLOW}[SETUP] Setting up storage access...${NC}"
    echo -e "${CYAN}Please click 'Allow' on the popup!${NC}"
    echo ""
    termux-setup-storage
    sleep 2
fi

# Create storage shortcuts if they don't exist
if [ ! -L "$HOME/downloads" ]; then
    ln -sf /storage/emulated/0/Download "$HOME/downloads" 2>/dev/null
    ln -sf /storage/emulated/0/Movies "$HOME/movies" 2>/dev/null
    ln -sf /storage/emulated/0/DCIM "$HOME/dcim" 2>/dev/null
fi

# Check dependencies
echo "Checking dependencies..."

if ! python -c "import srt, deep_translator, tqdm, chardet, pysubs2" &> /dev/null; then
    echo ""
    echo -e "${CYAN}╔═══════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║  First-time setup - Installing packages  ║${NC}"
    echo -e "${CYAN}╚═══════════════════════════════════════════╝${NC}"
    echo ""
    echo "This will take 2-3 minutes..."
    echo ""
    
    # Ensure pip is available
    python -m ensurepip --upgrade 2>/dev/null || true
    
    # Install dependencies
    pip install --quiet --disable-pip-version-check \
        srt deep-translator tqdm chardet pysubs2 || {
        echo -e "${RED}[ERROR] Failed to install dependencies${NC}"
        echo "Please check your internet connection and try again."
        exit 1
    }
    
    echo ""
    echo -e "${GREEN}✓ Dependencies installed successfully!${NC}"
    echo ""
    
    # Show storage shortcuts info
    echo -e "${CYAN}Storage Shortcuts Created:${NC}"
    echo "  ~/downloads → /storage/emulated/0/Download"
    echo "  ~/movies    → /storage/emulated/0/Movies"
    echo "  ~/dcim      → /storage/emulated/0/DCIM"
    echo ""
    echo "You can now access your phone files easily!"
    echo ""
    sleep 2
fi

# Make main script executable
chmod +x zee_translator.py 2>/dev/null || true

# Run the program
clear
python zee_translator.py "$@"

# Capture exit code
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo -e "${RED}╔═══════════════════════════════════════════╗${NC}"
    echo -e "${RED}║      Program exited with an error         ║${NC}"
    echo -e "${RED}╚═══════════════════════════════════════════╝${NC}"
    echo ""
    echo "Check error_log.txt for details."
    echo ""
    read -p "Press Enter to exit..."
fi

exit $EXIT_CODE
