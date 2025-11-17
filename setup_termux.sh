#!/data/data/com.termux/files/usr/bin/bash
# ================================================================
# Zee Subtitle Translator - Traditional Installer for Android/Termux
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
║     Android Traditional Setup (Local)     ║
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

echo -e "${GREEN}✓ Installing from local directory...${NC}"
echo -e "${BLUE}Location: $SCRIPT_DIR${NC}"
echo ""

# Check if in correct directory
if [ ! -f "zee_translator.py" ]; then
    echo -e "${RED}[ERROR] zee_translator.py not found!${NC}"
    echo ""
    echo "Please run this script inside the project folder:"
    echo "  cd zee-subtitle-translator"
    echo "  ./setup_termux.sh"
    echo ""
    exit 1
fi

# Update packages
echo -e "${CYAN}Updating Termux packages...${NC}"
pkg update -y -q 2>/dev/null || pkg update -y

# Install required packages
echo ""
echo -e "${CYAN}Installing required packages...${NC}"
pkg install -y -q python 2>/dev/null || pkg install -y python

echo -e "${GREEN}✓ Required packages installed${NC}"

# Setup storage access if needed
if [ ! -d "/storage/emulated/0" ]; then
    echo ""
    echo -e "${YELLOW}Setting up storage access...${NC}"
    echo -e "${CYAN}Please click 'Allow' on the popup!${NC}"
    echo ""
    termux-setup-storage
    sleep 2
fi

# Check requirements.txt
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}[ERROR] requirements.txt not found!${NC}"
    echo ""
    echo "Please make sure you're in the correct directory."
    exit 1
fi

# Install dependencies
echo ""
echo -e "${CYAN}[1/4] Installing Python dependencies...${NC}"
echo "This may take 2-3 minutes..."
echo ""

python -m pip install --upgrade pip --quiet --disable-pip-version-check 2>/dev/null || true

python -m pip install --quiet --disable-pip-version-check -r requirements.txt || {
    echo -e "${RED}[ERROR] Failed to install dependencies!${NC}"
    echo ""
    echo "Please try manually:"
    echo "  pip install -r requirements.txt"
    exit 1
}

echo -e "${GREEN}✓ Dependencies installed!${NC}"

# Make scripts executable
echo ""
echo -e "${CYAN}[2/4] Making scripts executable...${NC}"

chmod +x zee_translator.py 2>/dev/null || true
chmod +x setup_termux.sh 2>/dev/null || true
chmod +x uninstall.sh 2>/dev/null || true
chmod +x bootstrap_termux.sh 2>/dev/null || true

echo -e "${GREEN}✓ Scripts are now executable!${NC}"

# Setup storage shortcuts
echo ""
echo -e "${CYAN}[3/4] Creating storage shortcuts...${NC}"

ln -sf /storage/emulated/0/Download "$HOME/downloads" 2>/dev/null || true
ln -sf /storage/emulated/0/Movies "$HOME/movies" 2>/dev/null || true
ln -sf /storage/emulated/0/DCIM "$HOME/dcim" 2>/dev/null || true

echo -e "${GREEN}✓ Storage shortcuts created!${NC}"
echo "  ~/downloads → /storage/emulated/0/Download"
echo "  ~/movies    → /storage/emulated/0/Movies"
echo "  ~/dcim      → /storage/emulated/0/DCIM"

# Setup global command
echo ""
echo -e "${CYAN}[4/4] Setting up global command...${NC}"

SHELL_CONFIG="$HOME/.bashrc"

# Remove old alias if exists
sed -i.bak '/# Zee Subtitle Translator/,/alias zeetranslator=/d' "$SHELL_CONFIG" 2>/dev/null || true

# Add new alias
cat >> "$SHELL_CONFIG" << EOL

# Zee Subtitle Translator
alias zeetranslator='python $SCRIPT_DIR/zee_translator.py'
EOL

echo -e "${GREEN}✓ Global command configured!${NC}"

# Setup Termux widget
WIDGET_DIR="$HOME/.shortcuts"
mkdir -p "$WIDGET_DIR"

cat > "$WIDGET_DIR/ZeeTranslator" << EOL
#!/data/data/com.termux/files/usr/bin/bash
cd "$SCRIPT_DIR"
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
echo -e "  Location: ${YELLOW}$SCRIPT_DIR${NC}"
echo -e "  Command:  ${GREEN}zeetranslator${NC}"
echo ""
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
echo -e "  ${YELLOW}cd $SCRIPT_DIR${NC}"
echo -e "  ${YELLOW}./zee_translator.py${NC}"
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
