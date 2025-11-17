#!/bin/bash
# ================================================================
# Zee Subtitle Translator - Bootstrap Installer
# One-line auto-installer for Linux/macOS
# No git required - downloads directly from GitHub
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

# Configuration
REPO_URL="https://github.com/zeewank/zee-subtitle-translator"
ZIP_URL="https://github.com/zeewank/zee-subtitle-translator/archive/refs/heads/main.zip"
INSTALL_DIR="$HOME/zee-subtitle-translator"
TEMP_DIR="/tmp/zee-installer-$$"

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════╗
║   ZEE SUBTITLE TRANSLATOR - INSTALLER     ║
║        Auto-Download & Setup              ║
╚═══════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${GREEN}✓ Starting automatic installation...${NC}"
echo ""

# Check for download tool
DOWNLOAD_CMD=""
if command -v curl &> /dev/null; then
    DOWNLOAD_CMD="curl -L -o"
    echo -e "${GREEN}✓ Using curl for download${NC}"
elif command -v wget &> /dev/null; then
    DOWNLOAD_CMD="wget -O"
    echo -e "${GREEN}✓ Using wget for download${NC}"
else
    echo -e "${RED}[ERROR] Neither curl nor wget found!${NC}"
    echo ""
    echo "Please install one of them:"
    echo "  Ubuntu/Debian: sudo apt install curl"
    echo "  macOS:         brew install curl"
    echo ""
    exit 1
fi

# Check for unzip
if ! command -v unzip &> /dev/null; then
    echo -e "${RED}[ERROR] unzip not found!${NC}"
    echo ""
    echo "Please install unzip:"
    echo "  Ubuntu/Debian: sudo apt install unzip"
    echo "  macOS:         brew install unzip"
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

# Check if already installed
if [ -d "$INSTALL_DIR" ]; then
    echo ""
    echo -e "${YELLOW}⚠ Zee Translator already installed at: $INSTALL_DIR${NC}"
    echo ""
    read -p "Reinstall? (y/n): " REINSTALL
    if [ "$REINSTALL" != "y" ] && [ "$REINSTALL" != "Y" ]; then
        echo -e "${YELLOW}Installation cancelled.${NC}"
        exit 0
    fi
    echo ""
    echo -e "${YELLOW}Removing old installation...${NC}"
    rm -rf "$INSTALL_DIR"
fi

# Create temp directory
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR"

# Download project
echo ""
echo -e "${CYAN}[1/5] Downloading project from GitHub...${NC}"
echo -e "${BLUE}URL: $ZIP_URL${NC}"
echo ""

if [ "$DOWNLOAD_CMD" = "curl -L -o" ]; then
    curl -L -o zee-translator.zip "$ZIP_URL" --progress-bar || {
        echo -e "${RED}[ERROR] Download failed!${NC}"
        echo "Please check your internet connection."
        rm -rf "$TEMP_DIR"
        exit 1
    }
else
    wget -O zee-translator.zip "$ZIP_URL" --show-progress || {
        echo -e "${RED}[ERROR] Download failed!${NC}"
        echo "Please check your internet connection."
        rm -rf "$TEMP_DIR"
        exit 1
    }
fi

echo ""
echo -e "${GREEN}✓ Download complete!${NC}"

# Extract
echo ""
echo -e "${CYAN}[2/5] Extracting files...${NC}"
unzip -q zee-translator.zip || {
    echo -e "${RED}[ERROR] Extraction failed!${NC}"
    rm -rf "$TEMP_DIR"
    exit 1
}

# Move to install directory
EXTRACTED_DIR=$(find . -maxdepth 1 -type d -name "zee-subtitle-translator-*" | head -n 1)
if [ -z "$EXTRACTED_DIR" ]; then
    echo -e "${RED}[ERROR] Could not find extracted directory!${NC}"
    rm -rf "$TEMP_DIR"
    exit 1
fi

mv "$EXTRACTED_DIR" "$INSTALL_DIR"
echo -e "${GREEN}✓ Files extracted to: $INSTALL_DIR${NC}"

# Clean up temp
rm -rf "$TEMP_DIR"

# Install dependencies
cd "$INSTALL_DIR"

echo ""
echo -e "${CYAN}[3/5] Installing Python dependencies...${NC}"
echo "This may take 1-2 minutes..."
echo ""

python3 -m pip install --upgrade pip --quiet --disable-pip-version-check 2>/dev/null || true

python3 -m pip install --quiet --disable-pip-version-check -r requirements.txt || {
    echo -e "${RED}[ERROR] Failed to install dependencies!${NC}"
    echo ""
    echo "Please try manually:"
    echo "  cd $INSTALL_DIR"
    echo "  pip install -r requirements.txt"
    exit 1
}

echo -e "${GREEN}✓ Dependencies installed!${NC}"

# Make scripts executable
chmod +x zee_translator.py 2>/dev/null || true
chmod +x installer.sh 2>/dev/null || true
chmod +x uninstall.sh 2>/dev/null || true

# Setup global command
echo ""
echo -e "${CYAN}[4/5] Setting up global command...${NC}"

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
alias zeetranslator='python3 $INSTALL_DIR/zee_translator.py'
EOL

echo -e "${GREEN}✓ Global command configured!${NC}"

# Test installation
echo ""
echo -e "${CYAN}[5/5] Testing installation...${NC}"

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
echo -e "  Location: ${YELLOW}$INSTALL_DIR${NC}"
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
echo -e "  ${YELLOW}cd $INSTALL_DIR${NC}"
echo -e "  ${YELLOW}./zee_translator.py${NC}"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo -e "  README:      ${YELLOW}cat $INSTALL_DIR/README.md${NC}"
echo -e "  Quick Start: ${YELLOW}cat $INSTALL_DIR/QUICKSTART.md${NC}"
echo -e "  Full Guide:  ${YELLOW}cat $INSTALL_DIR/GUIDE.md${NC}"
echo ""
echo -e "${MAGENTA}Uninstall:${NC}"
echo -e "  ${YELLOW}cd $INSTALL_DIR && ./uninstall.sh${NC}"
echo ""
echo -e "${GREEN}Happy translating! 🎬${NC}"
echo ""
