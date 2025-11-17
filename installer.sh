#!/bin/bash
# ================================================================
# Zee Subtitle Translator - Traditional Installer
# For users who already downloaded the ZIP file
# Run this inside the project folder
# ================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════╗
║   ZEE SUBTITLE TRANSLATOR - INSTALLER     ║
║        Traditional Setup (Local)          ║
╚═══════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${GREEN}✓ Installing from local directory...${NC}"
echo -e "${BLUE}Location: $SCRIPT_DIR${NC}"
echo ""

# Check if in correct directory
if [ ! -f "zee_translator.py" ]; then
    echo -e "${RED}[ERROR] zee_translator.py not found!${NC}"
    echo ""
    echo "Please run this script inside the project folder:"
    echo "  cd zee-subtitle-translator"
    echo "  ./installer.sh"
    echo ""
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python 3 not found!${NC}"
    echo ""
    echo "Please install Python 3.7+:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  macOS:         brew install python3"
    echo ""
    exit 1
fi

echo -e "${GREEN}✓ Python 3 found${NC}"

# Check requirements.txt
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}[ERROR] requirements.txt not found!${NC}"
    echo ""
    echo "Please make sure you're in the correct directory."
    exit 1
fi

# Install dependencies
echo ""
echo -e "${CYAN}[1/3] Installing Python dependencies...${NC}"
echo "This may take 1-2 minutes..."
echo ""

python3 -m pip install --upgrade pip --quiet --disable-pip-version-check 2>/dev/null || true

python3 -m pip install --quiet --disable-pip-version-check -r requirements.txt || {
    echo -e "${RED}[ERROR] Failed to install dependencies!${NC}"
    echo ""
    echo "Please try manually:"
    echo "  pip install -r requirements.txt"
    exit 1
}

echo -e "${GREEN}✓ Dependencies installed!${NC}"

# Make scripts executable
echo ""
echo -e "${CYAN}[2/3] Making scripts executable...${NC}"

chmod +x zee_translator.py 2>/dev/null || true
chmod +x installer.sh 2>/dev/null || true
chmod +x uninstall.sh 2>/dev/null || true
chmod +x bootstrap_installer.sh 2>/dev/null || true

echo -e "${GREEN}✓ Scripts are now executable!${NC}"

# Setup global command
echo ""
echo -e "${CYAN}[3/3] Setting up global command...${NC}"

# Detect shell
if [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
else
    SHELL_CONFIG="$HOME/.profile"
fi

# Remove old alias if exists
sed -i.bak '/# Zee Subtitle Translator/,/alias zeetranslator=/d' "$SHELL_CONFIG" 2>/dev/null || \
sed -i '' '/# Zee Subtitle Translator/,/alias zeetranslator=/d' "$SHELL_CONFIG" 2>/dev/null || true

# Add new alias
cat >> "$SHELL_CONFIG" << EOL

# Zee Subtitle Translator
alias zeetranslator='python3 $SCRIPT_DIR/zee_translator.py'
EOL

echo -e "${GREEN}✓ Global command configured!${NC}"

# Test installation
if python3 -c "import srt, deep_translator, tqdm, chardet, pysubs2" 2>/dev/null; then
    echo -e "${GREEN}✓ All dependencies working!${NC}"
else
    echo -e "${YELLOW}⚠ Some dependencies may need attention${NC}"
fi

# Reload shell config
if [ -n "$BASH_VERSION" ]; then
    source "$SHELL_CONFIG" 2>/dev/null || true
elif [ -n "$ZSH_VERSION" ]; then
    source "$SHELL_CONFIG" 2>/dev/null || true
fi

# Success message
echo ""
echo -e "${GREEN}╔═══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   INSTALLATION COMPLETED SUCCESSFULLY!    ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Installation Details:${NC}"
echo -e "  Location: ${YELLOW}$SCRIPT_DIR${NC}"
echo -e "  Command:  ${GREEN}zeetranslator${NC}"
echo ""
echo -e "${CYAN}Quick Start:${NC}"
echo ""
echo -e "  ${GREEN}# Activate command (one time only):${NC}"
echo -e "  ${YELLOW}source $SHELL_CONFIG${NC}"
echo ""
echo -e "  ${GREEN}# Or open a new terminal window${NC}"
echo ""
echo -e "  ${GREEN}# Then run:${NC}"
echo -e "  ${YELLOW}zeetranslator${NC}"
echo ""
echo -e "${CYAN}Alternative (without global command):${NC}"
echo -e "  ${YELLOW}cd $SCRIPT_DIR${NC}"
echo -e "  ${YELLOW}./zee_translator.py${NC}"
echo ""
echo -e "  ${GREEN}# Or use Python directly:${NC}"
echo -e "  ${YELLOW}python3 $SCRIPT_DIR/zee_translator.py${NC}"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo -e "  README:      ${YELLOW}cat README.md${NC}"
echo -e "  Quick Start: ${YELLOW}cat QUICKSTART.md${NC}"
echo -e "  Full Guide:  ${YELLOW}cat GUIDE.md${NC}"
echo ""
echo -e "${MAGENTA}Uninstall:${NC}"
echo -e "  ${YELLOW}./uninstall.sh${NC}"
echo ""
echo -e "${GREEN}Happy translating! 🎬${NC}"
echo ""
