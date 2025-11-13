#!/data/data/com.termux/files/usr/bin/bash
# ================================================================
# Zee Subtitle Translator - Android/Termux Setup Script
# Quick setup for Android Termux users
# ================================================================

COLOR_RESET='\033[0m'
COLOR_GREEN='\033[92m'
COLOR_YELLOW='\033[93m'
COLOR_RED='\033[91m'
COLOR_CYAN='\033[96m'
COLOR_MAGENTA='\033[95m'

echo -e "${COLOR_CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════╗
║   ZEE SUBTITLE TRANSLATOR - TERMUX SETUP  ║
║              Version 1.0                  ║
╚═══════════════════════════════════════════╝
EOF
echo -e "${COLOR_RESET}"

echo -e "${COLOR_YELLOW}Pilih Bahasa / Select Language:${COLOR_RESET}"
echo "  1) English"
echo "  2) Bahasa Indonesia"
read -p "Choice / Pilihan [1-2]: " LANG_CHOICE

if [ "$LANG_CHOICE" = "2" ]; then
    LANG="ID"
else
    LANG="EN"
fi

# [1/6] Update packages
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[1/6] Memperbarui paket Termux...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[1/6] Updating Termux packages...${COLOR_RESET}"
fi

pkg update -y
pkg upgrade -y

# [2/6] Install Python and Git
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[2/6] Menginstal Python dan Git...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[2/6] Installing Python and Git...${COLOR_RESET}"
fi

pkg install -y python git

# [3/6] Setup storage
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[3/6] Mengatur akses storage...${COLOR_RESET}"
    echo -e "${COLOR_CYAN}Klik 'Allow' pada popup yang muncul!${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[3/6] Setting up storage access...${COLOR_RESET}"
    echo -e "${COLOR_CYAN}Click 'Allow' on the popup!${COLOR_RESET}"
fi

termux-setup-storage
sleep 2

# Create shortcuts to common folders
if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_CYAN}Membuat shortcut ke folder HP...${COLOR_RESET}"
else
    echo -e "${COLOR_CYAN}Creating shortcuts to phone folders...${COLOR_RESET}"
fi

ln -sf /storage/emulated/0/Download ~/downloads 2>/dev/null
ln -sf /storage/emulated/0/Movies ~/movies 2>/dev/null
ln -sf /storage/emulated/0/DCIM ~/dcim 2>/dev/null

# [4/6] Install dependencies
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[4/6] Menginstal dependensi Python...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[4/6] Installing Python dependencies...${COLOR_RESET}"
fi

pip install -r requirements.txt

# [5/6] Setup permissions
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[5/6] Mengatur izin...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[5/6] Setting up permissions...${COLOR_RESET}"
fi

chmod +x zee_translator.py

# [6/6] Create global command
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[6/6] Membuat command global 'zeetranslator'...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[6/6] Creating global 'zeetranslator' command...${COLOR_RESET}"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/zee_translator.py"

# Create alias in .bashrc
if ! grep -q "alias zeetranslator=" ~/.bashrc 2>/dev/null; then
    echo "" >> ~/.bashrc
    echo "# Zee Subtitle Translator" >> ~/.bashrc
    echo "alias zeetranslator='python $SCRIPT_PATH'" >> ~/.bashrc
    
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Command global berhasil dibuat!${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Global command created successfully!${COLOR_RESET}"
    fi
fi

# Create Termux widget shortcut
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}Membuat widget shortcut...${COLOR_RESET}"
else
    echo -e "\n${COLOR_CYAN}Creating widget shortcut...${COLOR_RESET}"
fi

mkdir -p ~/.shortcuts

cat > ~/.shortcuts/ZeeTranslator << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/zee-subtitle-translator
python zee_translator.py
EOF

chmod +x ~/.shortcuts/ZeeTranslator

# Reload bashrc
source ~/.bashrc 2>/dev/null || true

# Success message
echo ""
echo -e "${COLOR_GREEN}═══════════════════════════════════════════${COLOR_RESET}"
if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_GREEN}    Setup Termux Berhasil!${COLOR_RESET}"
else
    echo -e "${COLOR_GREEN}    Termux Setup Complete!${COLOR_RESET}"
fi
echo -e "${COLOR_GREEN}═══════════════════════════════════════════${COLOR_RESET}"

if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}Cara Menggunakan:${COLOR_RESET}"
    echo -e "  ${COLOR_GREEN}zeetranslator${COLOR_RESET}                # Dari mana saja!"
    echo "  ./zee_translator.py              # Cara alternatif"
    echo ""
    echo -e "${COLOR_CYAN}Shortcut Storage:${COLOR_RESET}"
    echo "  ~/downloads  →  /storage/emulated/0/Download"
    echo "  ~/movies     →  /storage/emulated/0/Movies"
    echo "  ~/dcim       →  /storage/emulated/0/DCIM"
    echo ""
    echo -e "${COLOR_CYAN}Contoh Penggunaan:${COLOR_RESET}"
    echo "  zeetranslator ~/downloads/Subtitles"
    echo ""
    echo -e "${COLOR_YELLOW}Tips:${COLOR_RESET}"
    echo "  - Install 'Hacker's Keyboard' untuk kemudahan mengetik"
    echo "  - Enable Wake Lock di Termux Settings"
    echo "  - Widget: Long-press home → Add Widget → Termux:Widget → ZeeTranslator"
else
    echo -e "\n${COLOR_CYAN}How to Use:${COLOR_RESET}"
    echo -e "  ${COLOR_GREEN}zeetranslator${COLOR_RESET}                # From anywhere!"
    echo "  ./zee_translator.py              # Alternative way"
    echo ""
    echo -e "${COLOR_CYAN}Storage Shortcuts:${COLOR_RESET}"
    echo "  ~/downloads  →  /storage/emulated/0/Download"
    echo "  ~/movies     →  /storage/emulated/0/Movies"
    echo "  ~/dcim       →  /storage/emulated/0/DCIM"
    echo ""
    echo -e "${COLOR_CYAN}Usage Examples:${COLOR_RESET}"
    echo "  zeetranslator ~/downloads/Subtitles"
    echo ""
    echo -e "${COLOR_YELLOW}Tips:${COLOR_RESET}"
    echo "  - Install 'Hacker's Keyboard' for easier typing"
    echo "  - Enable Wake Lock in Termux Settings"
    echo "  - Widget: Long-press home → Add Widget → Termux:Widget → ZeeTranslator"
fi

echo ""
echo -e "${COLOR_MAGENTA}═══════════════════════════════════════════${COLOR_RESET}"
echo -e "${COLOR_MAGENTA}          💖 Support This Project${COLOR_RESET}"
echo -e "${COLOR_MAGENTA}═══════════════════════════════════════════${COLOR_RESET}"
echo -e "${COLOR_CYAN}  🌍 PayPal: https://paypal.me/zeewank${COLOR_RESET}"
echo -e "${COLOR_CYAN}  🇮🇩 Trakteer: https://trakteer.id/zeewank/tip${COLOR_RESET}"
echo -e "${COLOR_MAGENTA}═══════════════════════════════════════════${COLOR_RESET}"
echo ""

if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_GREEN}✓ Siap digunakan! Ketik 'zeetranslator' untuk memulai${COLOR_RESET}\n"
else
    echo -e "${COLOR_GREEN}✓ Ready! Type 'zeetranslator' to start${COLOR_RESET}\n"
fi
