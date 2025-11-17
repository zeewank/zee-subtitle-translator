#!/data/data/com.termux/files/usr/bin/bash
# ================================================================
# Zee Subtitle Translator - Bootstrap Installer for Android/Termux
# One-line auto-installer - No git required
# Downloads directly from GitHub
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
TEMP_DIR="$HOME/.zee-installer-$$"

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════╗
║   ZEE SUBTITLE TRANSLATOR - INSTALLER     ║
║     Android Auto-Download & Setup         ║
╚═══════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Check if in Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo -e "${RED}[ERROR] This script must be run in Termux!${NC}"
    echo ""
    echo "Please install Termux from F-Droid:"
    echo "  https://f-droid.org/packages/com.termux/"
    echo ""
    exit 1
fi

echo -e "${GREEN}✓ Starting automatic installation...${NC}"
echo ""

# Update packages
echo -e "${CYAN}Updating Termux packages...${NC}"
pkg update -y -q 2>/dev/null || pkg update -y

# Install required packages
echo ""
echo -e "${CYAN}Installing required packages...${NC}"
pkg install -y -q python curl unzip 2>/dev/null || pkg install -y python curl unzip

echo -e "${GREEN}✓ Required packages installed${NC}"

# Ask for installation location
echo ""
echo -e "${YELLOW}╔═══════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║   WHERE TO INSTALL?                       ║${NC}"
echo -e "${YELLOW}╚═══════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Choose installation location:${NC}"
echo ""
echo "  1. Termux Home (~/zee-subtitle-translator)"
echo "     ✓ Faster"
echo "     ✗ Not accessible from phone file manager"
echo "     ✗ Deleted if Termux uninstalled"
echo ""
echo "  2. Shared Storage (/storage/emulated/0/ZeeTranslator)"
echo "     ✓ Accessible from phone file manager"
echo "     ✓ Persists after Termux uninstall"
echo "     ✓ Easy to backup/share"
echo "     ✗ Slightly slower"
echo ""
read -p "Choice [1-2] (default 2): " LOCATION_CHOICE
LOCATION_CHOICE=${LOCATION_CHOICE:-2}

if [ "$LOCATION_CHOICE" = "1" ]; then
    INSTALL_DIR="$HOME/zee-subtitle-translator"
    echo -e "${YELLOW}Installing to Termux Home...${NC}"
else
    # Setup storage access if needed
    if [ ! -d "/storage/emulated/0" ]; then
        echo ""
        echo -e "${YELLOW}Setting up storage access...${NC}"
        echo -e "${CYAN}Please click 'Allow' on the popup!${NC}"
        echo ""
        termux-setup-storage
        sleep 2
    fi
    
    INSTALL_DIR="/storage/emulated/0/ZeeTranslator"
    echo -e "${GREEN}Installing to Shared Storage...${NC}"
fi

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
echo -e "${CYAN}[1/6] Downloading project from GitHub...${NC}"
echo -e "${BLUE}URL: $ZIP_URL${NC}"
echo ""

curl -L -o zee-translator.zip "$ZIP_URL" --progress-bar || {
    echo -e "${RED}[ERROR] Download failed!${NC}"
    echo "Please check your internet connection."
    rm -rf "$TEMP_DIR"
    exit 1
}

echo ""
echo -e "${GREEN}✓ Download complete!${NC}"

# Extract
echo ""
echo -e "${CYAN}[2/6] Extracting files...${NC}"
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

mkdir -p "$(dirname "$INSTALL_DIR")"
mv "$EXTRACTED_DIR" "$INSTALL_DIR"
echo -e "${GREEN}✓ Files extracted to: $INSTALL_DIR${NC}"

# Clean up temp
rm -rf "$TEMP_DIR"

# Install dependencies
cd "$INSTALL_DIR"

echo ""
echo -e "${CYAN}[3/6] Installing Python dependencies...${NC}"
echo "This may take 2-3 minutes..."
echo ""

python -m pip install --upgrade pip --quiet --disable-pip-version-check 2>/dev/null || true

python -m pip install --quiet --disable-pip-version-check -r requirements.txt || {
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
chmod +x setup_termux.sh 2>/dev/null || true
chmod +x uninstall.sh 2>/dev/null || true

# Setup storage shortcuts
echo ""
echo -e "${CYAN}[4/6] Creating storage shortcuts...${NC}"

ln -sf /storage/emulated/0/Download "$HOME/downloads" 2>/dev/null || true
ln -sf /storage/emulated/0/Movies "$HOME/movies" 2>/dev/null || true
ln -sf /storage/emulated/0/DCIM "$HOME/dcim" 2>/dev/null || true

echo -e "${GREEN}✓ Storage shortcuts created!${NC}"
echo "  ~/downloads → /storage/emulated/0/Download"
echo "  ~/movies    → /storage/emulated/0/Movies"
echo "  ~/dcim      → /storage/emulated/0/DCIM"

# Setup global command
echo ""
echo -e "${CYAN}[5/6] Setting up global command...${NC}"

SHELL_CONFIG="$HOME/.bashrc"

# Remove old alias if exists
sed -i.bak '/# Zee Subtitle Translator/,/alias zeetranslator=/d' "$SHELL_CONFIG" 2>/dev/null || true

# Add new alias
cat >> "$SHELL_CONFIG" << EOL

# Zee Subtitle Translator
alias zeetranslator='python $INSTALL_DIR/zee_translator.py'
EOL

echo -e "${GREEN}✓ Global command configured!${NC}"

# Setup Termux widget
echo ""
echo -e "${CYAN}[6/6] Setting up Termux widget...${NC}"

WIDGET_DIR="$HOME/.shortcuts"
mkdir -p "$WIDGET_DIR"

cat > "$WIDGET_DIR/ZeeTranslator" << EOL
#!/data/data/com.termux/files/usr/bin/bash
cd "$INSTALL_DIR"
python zee_translator.py
EOL

chmod +x "$WIDGET_DIR/ZeeTranslator"

echo -e "${GREEN}✓ Termux widget created!${NC}"

# Test installation
if python -c "import srt, deep_translator, tqdm, chardet, pysubs2" 2>/dev/null; then
    echo -e "${GREEN}✓ All dependencies working!${NC}"
else
    echo -e "${YELLOW}⚠ Some dependencies may need attention${NC}"
fi

# Reload shell config
source "$SHELL_CONFIG" 2>/dev/null || true

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

if [ "$LOCATION_CHOICE" = "2" ]; then
    echo -e "${CYAN}Access from Phone File Manager:${NC}"
    echo -e "  Open ${YELLOW}File Manager${NC}"
    echo -e "  Go to ${YELLOW}Internal Storage${NC}"
    echo -e "  Open ${YELLOW}ZeeTranslator${NC} folder"
    echo ""
fi

echo -e "${CYAN}Quick Start:${NC}"
echo ""
echo -e "  ${GREEN}# Activate command (one time only):${NC}"
echo -e "  ${YELLOW}source ~/.bashrc${NC}"
echo ""
echo -e "  ${GREEN}# Or restart Termux${NC}"
echo ""
echo -e "  ${GREEN}# Then run:${NC}"
echo -e "  ${YELLOW}zeetranslator${NC}"
echo ""
echo -e "  ${GREEN}# Or tap the Termux widget on home screen${NC}"
echo ""
echo -e "${CYAN}Storage Shortcuts:${NC}"
echo -e "  ${YELLOW}cd ~/downloads${NC}  # Your Downloads folder"
echo -e "  ${YELLOW}cd ~/movies${NC}     # Your Movies folder"
echo -e "  ${YELLOW}cd ~/dcim${NC}       # Your Camera folder"
echo ""
echo -e "${CYAN}Alternative (without global command):${NC}"
echo -e "  ${YELLOW}cd $INSTALL_DIR${NC}"
echo -e "  ${YELLOW}./zee_translator.py${NC}"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo -e "  README:      ${YELLOW}cat $INSTALL_DIR/README.md${NC}"
echo -e "  Quick Start: ${YELLOW}cat $INSTALL_DIR/QUICKSTART.md${NC}"
echo -e "  Full Guide:  ${YELLOW}cat $INSTALL_DIR/GUIDE.md${NC}"
echo -e "  Android FAQ: ${YELLOW}cat $INSTALL_DIR/ANDROID_STORAGE_GUIDE.md${NC}"
echo ""
echo -e "${MAGENTA}Uninstall:${NC}"
echo -e "  ${YELLOW}cd $INSTALL_DIR && ./uninstall.sh${NC}"
echo ""
echo -e "${GREEN}Happy translating! 🎬${NC}"
echo ""
