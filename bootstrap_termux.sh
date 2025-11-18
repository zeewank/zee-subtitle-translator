#!/data/data/com.termux/files/usr/bin/bash
# ================================================================
# Zee Subtitle Translator - Bootstrap Installer for Android/Termux
# One-line auto-installer - No git required
# Downloads directly from GitHub
# FIXED: Better permission handling and error checking
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
    echo "⚠️  DO NOT use Google Play Store version (it's broken)!"
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
echo "     ✓ No permission needed"
echo "     ✗ Not accessible from phone file manager"
echo "     ✗ Deleted if Termux uninstalled"
echo ""
echo "  2. Shared Storage (/storage/emulated/0/ZeeTranslator)"
echo "     ✓ Accessible from phone file manager"
echo "     ✓ Persists after Termux uninstall"
echo "     ✓ Easy to backup/share"
echo "     ✗ Requires storage permission"
echo "     ✗ Slightly slower"
echo ""
read -p "Choice [1-2] (default 2): " LOCATION_CHOICE
LOCATION_CHOICE=${LOCATION_CHOICE:-2}

if [ "$LOCATION_CHOICE" = "1" ]; then
    INSTALL_DIR="$HOME/zee-subtitle-translator"
    echo -e "${YELLOW}Installing to Termux Home...${NC}"
else
    # Setup storage access if needed
    if [ ! -d "/storage/emulated/0" ] || [ ! -d "$HOME/storage/shared" ]; then
        echo ""
        echo -e "${YELLOW}═══════════════════════════════════════════${NC}"
        echo -e "${YELLOW}   STORAGE PERMISSION REQUIRED${NC}"
        echo -e "${YELLOW}═══════════════════════════════════════════${NC}"
        echo ""
        echo -e "${CYAN}Termux needs permission to access Android storage.${NC}"
        echo ""
        echo "What will happen:"
        echo "  1. A popup will appear asking for permission"
        echo "  2. Please click 'Allow' or 'Izinkan'"
        echo "  3. Installation will continue automatically"
        echo ""
        read -p "Press ENTER to continue..." 
        echo ""
        echo -e "${YELLOW}Setting up storage access...${NC}"
        echo -e "${CYAN}👉 Please click 'Allow' on the popup!${NC}"
        echo ""
        termux-setup-storage
        sleep 3
    fi
    
    # Verify storage access is granted
    echo -e "${CYAN}Verifying storage permission...${NC}"
    
    if [ ! -d "$HOME/storage/shared" ]; then
        echo ""
        echo -e "${RED}╔═══════════════════════════════════════════╗${NC}"
        echo -e "${RED}║   ERROR: STORAGE PERMISSION NOT GRANTED  ║${NC}"
        echo -e "${RED}╚═══════════════════════════════════════════╝${NC}"
        echo ""
        echo "Termux needs storage access to install in Shared Storage."
        echo ""
        echo -e "${YELLOW}Please follow these steps:${NC}"
        echo "  1. Run: ${GREEN}termux-setup-storage${NC}"
        echo "  2. Click '${GREEN}Allow${NC}' when popup appears"
        echo "  3. Run this installer again"
        echo ""
        echo -e "${CYAN}Or choose Option 1 (Termux Home) for installation without storage permission.${NC}"
        echo ""
        exit 1
    fi
    
    echo -e "${GREEN}✓ Storage permission granted${NC}"
    
    # Test write permission to shared storage
    echo -e "${CYAN}Testing storage write permission...${NC}"
    
    TEST_FILE="/storage/emulated/0/.test_write_$$"
    if ! touch "$TEST_FILE" 2>/dev/null; then
        echo ""
        echo -e "${RED}╔═══════════════════════════════════════════╗${NC}"
        echo -e "${RED}║   ERROR: CANNOT WRITE TO SHARED STORAGE  ║${NC}"
        echo -e "${RED}╚═══════════════════════════════════════════╝${NC}"
        echo ""
        echo "Storage permission may not be granted properly."
        echo ""
        echo -e "${YELLOW}Solutions:${NC}"
        echo ""
        echo "  ${CYAN}Method 1: Grant permission via Settings${NC}"
        echo "    1. Open Android Settings"
        echo "    2. Go to Apps → Termux → Permissions"
        echo "    3. Enable 'Storage' or 'Files and media' permission"
        echo "    4. Run this installer again"
        echo ""
        echo "  ${CYAN}Method 2: Use termux-setup-storage${NC}"
        echo "    1. Run: ${GREEN}termux-setup-storage${NC}"
        echo "    2. Click '${GREEN}Allow${NC}' when popup appears"
        echo "    3. Run this installer again"
        echo ""
        echo "  ${CYAN}Method 3: Install to Termux Home instead${NC}"
        echo "    1. Run this installer again"
        echo "    2. Choose Option 1 (Termux Home)"
        echo ""
        exit 1
    fi
    
    rm -f "$TEST_FILE" 2>/dev/null
    echo -e "${GREEN}✓ Storage write permission OK${NC}"
    
    INSTALL_DIR="/storage/emulated/0/ZeeTranslator"
    echo -e "${GREEN}Installing to Shared Storage...${NC}"
fi

# Check if already installed
if [ -d "$INSTALL_DIR" ]; then
    echo ""
    echo -e "${YELLOW}⚠️  Zee Translator already installed at: $INSTALL_DIR${NC}"
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
    echo ""
    echo "Please check your internet connection."
    echo ""
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

# Create parent directory if needed (with proper error handling)
PARENT_DIR="$(dirname "$INSTALL_DIR")"
if [ ! -d "$PARENT_DIR" ]; then
    if ! mkdir -p "$PARENT_DIR" 2>/dev/null; then
        echo -e "${RED}[ERROR] Cannot create directory: $PARENT_DIR${NC}"
        echo ""
        echo "This usually means storage permission issue."
        echo "Please try:"
        echo "  1. Run: termux-setup-storage"
        echo "  2. Or choose Option 1 (Termux Home)"
        echo ""
        rm -rf "$TEMP_DIR"
        exit 1
    fi
fi

# Move extracted directory to install location
if ! mv "$EXTRACTED_DIR" "$INSTALL_DIR" 2>/dev/null; then
    echo -e "${RED}[ERROR] Cannot move files to: $INSTALL_DIR${NC}"
    echo ""
    echo "This usually means storage permission issue."
    echo "Please try:"
    echo "  1. Run: termux-setup-storage"
    echo "  2. Or choose Option 1 (Termux Home)"
    echo ""
    rm -rf "$TEMP_DIR"
    exit 1
fi

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
    echo -e "${YELLOW}⚠️  Some dependencies may need attention${NC}"
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
    echo -e "${CYAN}📱 Access from Phone File Manager:${NC}"
    echo -e "  1. Open ${YELLOW}File Manager${NC} app"
    echo -e "  2. Go to ${YELLOW}Internal Storage${NC}"
    echo -e "  3. Open ${YELLOW}ZeeTranslator${NC} folder"
    echo ""
fi

echo -e "${CYAN}🚀 Quick Start:${NC}"
echo ""
echo -e "  ${GREEN}# Activate command (one time only):${NC}"
echo -e "  ${YELLOW}source ~/.bashrc${NC}"
echo ""
echo -e "  ${GREEN}# Or simply restart Termux${NC}"
echo ""
echo -e "  ${GREEN}# Then run:${NC}"
echo -e "  ${YELLOW}zeetranslator${NC}"
echo ""
echo -e "  ${GREEN}# Or tap the Termux widget on home screen${NC}"
echo ""
echo -e "${CYAN}📂 Storage Shortcuts:${NC}"
echo -e "  ${YELLOW}cd ~/downloads${NC}  # Your Downloads folder"
echo -e "  ${YELLOW}cd ~/movies${NC}     # Your Movies folder"
echo -e "  ${YELLOW}cd ~/dcim${NC}       # Your Camera folder"
echo ""
echo -e "${CYAN}Alternative (without global command):${NC}"
echo -e "  ${YELLOW}cd $INSTALL_DIR${NC}"
echo -e "  ${YELLOW}./zee_translator.py${NC}"
echo ""
echo -e "${BLUE}📖 Documentation:${NC}"
echo -e "  README:      ${YELLOW}cat $INSTALL_DIR/README.md${NC}"
echo -e "  Quick Start: ${YELLOW}cat $INSTALL_DIR/QUICKSTART.md${NC}"
echo -e "  Full Guide:  ${YELLOW}cat $INSTALL_DIR/GUIDE.md${NC}"
echo -e "  Android FAQ: ${YELLOW}cat $INSTALL_DIR/ANDROID_STORAGE_GUIDE.md${NC}"
echo ""
echo -e "${MAGENTA}🗑️  Uninstall:${NC}"
echo -e "  ${YELLOW}cd $INSTALL_DIR && ./uninstall.sh${NC}"
echo ""
echo -e "${GREEN}Happy translating! 🎬${NC}"
echo ""
