#!/data/data/com.termux/files/usr/bin/bash
# ================================================================
# Zee Subtitle Translator - Android/Termux Setup Script
# Fixed version: Installs to accessible storage location
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

# [1/7] Update packages
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[1/7] Memperbarui paket Termux...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[1/7] Updating Termux packages...${COLOR_RESET}"
fi

pkg update -y
pkg upgrade -y

# [2/7] Install Python and Git
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[2/7] Menginstal Python dan Git...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[2/7] Installing Python and Git...${COLOR_RESET}"
fi

pkg install -y python git

# [3/7] Setup storage
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[3/7] Mengatur akses storage...${COLOR_RESET}"
    echo -e "${COLOR_CYAN}PENTING: Klik 'Allow' pada popup yang muncul!${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[3/7] Setting up storage access...${COLOR_RESET}"
    echo -e "${COLOR_CYAN}IMPORTANT: Click 'Allow' on the popup!${COLOR_RESET}"
fi

termux-setup-storage
sleep 3

# Verify storage access
if [ ! -d "/storage/emulated/0" ]; then
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_RED}✗ Akses storage gagal! Jalankan ulang script ini.${COLOR_RESET}"
    else
        echo -e "${COLOR_RED}✗ Storage access failed! Re-run this script.${COLOR_RESET}"
    fi
    exit 1
fi

# Create shortcuts to common folders
if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_CYAN}Membuat shortcut ke folder HP...${COLOR_RESET}"
else
    echo -e "${COLOR_CYAN}Creating shortcuts to phone folders...${COLOR_RESET}"
fi

ln -sf /storage/emulated/0/Download ~/downloads 2>/dev/null
ln -sf /storage/emulated/0/Movies ~/movies 2>/dev/null
ln -sf /storage/emulated/0/DCIM ~/dcim 2>/dev/null

# [4/7] Clone to accessible storage
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[4/7] Menentukan lokasi instalasi...${COLOR_RESET}"
    echo ""
    echo -e "${COLOR_CYAN}PENTING: Pilih lokasi instalasi${COLOR_RESET}"
    echo ""
    echo "Termux punya 2 area storage:"
    echo ""
    echo "1. TERMUX HOME (~)"
    echo "   Lokasi: /data/data/com.termux/files/home/"
    echo "   ✓ Cepat diakses dari Termux"
    echo "   ✗ Tidak bisa diakses dari file manager HP"
    echo "   ✗ Hilang jika uninstall Termux"
    echo ""
    echo "2. SHARED STORAGE (Recommended)"
    echo "   Lokasi: /storage/emulated/0/ (Internal Storage HP)"
    echo "   ✓ Bisa diakses dari file manager HP"
    echo "   ✓ Tetap ada walaupun uninstall Termux"
    echo "   ✓ Bisa backup/share lebih mudah"
    echo ""
    read -p "Pilih lokasi [1-2] (default 2): " STORAGE_CHOICE
else
    echo -e "\n${COLOR_YELLOW}[4/7] Choosing installation location...${COLOR_RESET}"
    echo ""
    echo -e "${COLOR_CYAN}IMPORTANT: Choose installation location${COLOR_RESET}"
    echo ""
    echo "Termux has 2 storage areas:"
    echo ""
    echo "1. TERMUX HOME (~)"
    echo "   Location: /data/data/com.termux/files/home/"
    echo "   ✓ Fast access from Termux"
    echo "   ✗ Can't access from phone file manager"
    echo "   ✗ Lost if uninstall Termux"
    echo ""
    echo "2. SHARED STORAGE (Recommended)"
    echo "   Location: /storage/emulated/0/ (Phone Internal Storage)"
    echo "   ✓ Accessible from phone file manager"
    echo "   ✓ Persists after uninstalling Termux"
    echo "   ✓ Easier to backup/share"
    echo ""
    read -p "Choose location [1-2] (default 2): " STORAGE_CHOICE
fi

STORAGE_CHOICE=${STORAGE_CHOICE:-2}

if [ "$STORAGE_CHOICE" = "1" ]; then
    INSTALL_DIR="$HOME/zee-subtitle-translator"
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}Instalasi ke Termux Home${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}Installing to Termux Home${COLOR_RESET}"
    fi
else
    INSTALL_DIR="/storage/emulated/0/ZeeTranslator"
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}Instalasi ke Shared Storage (Recommended)${COLOR_RESET}"
        echo -e "${COLOR_CYAN}Folder: Internal Storage/ZeeTranslator/${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}Installing to Shared Storage (Recommended)${COLOR_RESET}"
        echo -e "${COLOR_CYAN}Folder: Internal Storage/ZeeTranslator/${COLOR_RESET}"
    fi
fi

# Check if already exists
if [ -d "$INSTALL_DIR" ]; then
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}Folder sudah ada. Menggunakan folder existing.${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}Folder exists. Using existing folder.${COLOR_RESET}"
    fi
    cd "$INSTALL_DIR"
else
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_CYAN}Mendownload project...${COLOR_RESET}"
    else
        echo -e "${COLOR_CYAN}Downloading project...${COLOR_RESET}"
    fi
    
    cd "$(dirname "$INSTALL_DIR")"
    git clone https://github.com/zeewank/zee-subtitle-translator.git "$(basename "$INSTALL_DIR")"
    cd "$INSTALL_DIR"
fi

SCRIPT_PATH="$INSTALL_DIR/zee_translator.py"

# [5/7] Install dependencies
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[5/7] Menginstal dependensi Python...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[5/7] Installing Python dependencies...${COLOR_RESET}"
fi

pip install -r requirements.txt

# [6/7] Setup permissions
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[6/7] Mengatur izin...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[6/7] Setting up permissions...${COLOR_RESET}"
fi

chmod +x zee_translator.py

# [7/7] Create global command
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}[7/7] Membuat command global 'zeetranslator'...${COLOR_RESET}"
else
    echo -e "\n${COLOR_YELLOW}[7/7] Creating global 'zeetranslator' command...${COLOR_RESET}"
fi

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

cat > ~/.shortcuts/ZeeTranslator << EOF
#!/data/data/com.termux/files/usr/bin/bash
cd "$INSTALL_DIR"
python zee_translator.py
EOF

chmod +x ~/.shortcuts/ZeeTranslator

# Activate in current session
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}Mengaktifkan command di session ini...${COLOR_RESET}"
else
    echo -e "\n${COLOR_CYAN}Activating command in current session...${COLOR_RESET}"
fi

# Create alias in current shell immediately
alias zeetranslator="python $SCRIPT_PATH" 2>/dev/null || true

# Reload bashrc
source ~/.bashrc 2>/dev/null || true

# Test if command works
if command -v zeetranslator &> /dev/null || alias zeetranslator &> /dev/null; then
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Command 'zeetranslator' siap digunakan!${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Command 'zeetranslator' is ready!${COLOR_RESET}"
    fi
else
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}⚠ Command belum aktif. Jalankan: source ~/.bashrc${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}⚠ Command not active. Run: source ~/.bashrc${COLOR_RESET}"
    fi
fi

# Success message
echo ""
echo -e "${COLOR_GREEN}╔═══════════════════════════════════════════╗${COLOR_RESET}"
if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_GREEN}║         Setup Termux Berhasil!            ║${COLOR_RESET}"
else
    echo -e "${COLOR_GREEN}║         Termux Setup Complete!            ║${COLOR_RESET}"
fi
echo -e "${COLOR_GREEN}╚═══════════════════════════════════════════╝${COLOR_RESET}"

if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}Lokasi Instalasi:${COLOR_RESET}"
    echo "  $INSTALL_DIR"
    echo ""
    echo -e "${COLOR_CYAN}Cara Menggunakan:${COLOR_RESET}"
    echo -e "  ${COLOR_GREEN}zeetranslator${COLOR_RESET}                # Dari mana saja"
    echo "  cd $INSTALL_DIR"
    echo "  ./zee_translator.py              # Cara alternatif"
    echo ""
    echo -e "${COLOR_CYAN}Shortcut Storage:${COLOR_RESET}"
    echo "  ~/downloads  →  /storage/emulated/0/Download"
    echo "  ~/movies     →  /storage/emulated/0/Movies"
    echo "  ~/dcim       →  /storage/emulated/0/DCIM"
    echo ""
    echo -e "${COLOR_CYAN}Contoh Penggunaan:${COLOR_RESET}"
    echo "  zeetranslator ~/downloads/Subtitles"
    echo "  zeetranslator ~/movies/MyMovie/"
    echo ""
    echo -e "${COLOR_YELLOW}Tips:${COLOR_RESET}"
    echo "  - Install 'Hacker's Keyboard' untuk kemudahan mengetik"
    echo "  - Enable Wake Lock di Termux Settings"
    echo "  - Widget: Long-press home → Widgets → Termux:Widget → ZeeTranslator"
    echo ""
    if [ "$STORAGE_CHOICE" = "2" ]; then
        echo -e "${COLOR_CYAN}Akses dari File Manager:${COLOR_RESET}"
        echo "  Buka file manager HP → Internal Storage → ZeeTranslator"
    fi
else
    echo -e "\n${COLOR_CYAN}Installation Location:${COLOR_RESET}"
    echo "  $INSTALL_DIR"
    echo ""
    echo -e "${COLOR_CYAN}How to Use:${COLOR_RESET}"
    echo -e "  ${COLOR_GREEN}zeetranslator${COLOR_RESET}                # From anywhere"
    echo "  cd $INSTALL_DIR"
    echo "  ./zee_translator.py              # Alternative way"
    echo ""
    echo -e "${COLOR_CYAN}Storage Shortcuts:${COLOR_RESET}"
    echo "  ~/downloads  →  /storage/emulated/0/Download"
    echo "  ~/movies     →  /storage/emulated/0/Movies"
    echo "  ~/dcim       →  /storage/emulated/0/DCIM"
    echo ""
    echo -e "${COLOR_CYAN}Usage Examples:${COLOR_RESET}"
    echo "  zeetranslator ~/downloads/Subtitles"
    echo "  zeetranslator ~/movies/MyMovie/"
    echo ""
    echo -e "${COLOR_YELLOW}Tips:${COLOR_RESET}"
    echo "  - Install 'Hacker's Keyboard' for easier typing"
    echo "  - Enable Wake Lock in Termux Settings"
    echo "  - Widget: Long-press home → Widgets → Termux:Widget → ZeeTranslator"
    echo ""
    if [ "$STORAGE_CHOICE" = "2" ]; then
        echo -e "${COLOR_CYAN}Access from File Manager:${COLOR_RESET}"
        echo "  Open phone file manager → Internal Storage → ZeeTranslator"
    fi
fi

echo ""
echo -e "${COLOR_MAGENTA}Support This Project${COLOR_RESET}"
echo -e "${COLOR_CYAN}  PayPal: https://paypal.me/zeewank${COLOR_RESET}"
echo -e "${COLOR_CYAN}  Trakteer: https://trakteer.id/zeewank/tip${COLOR_RESET}"
echo ""

if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_GREEN}Siap digunakan! Ketik 'zeetranslator' untuk memulai${COLOR_RESET}"
    echo -e "${COLOR_CYAN}Atau restart Termux jika command belum aktif${COLOR_RESET}\n"
else
    echo -e "${COLOR_GREEN}Ready! Type 'zeetranslator' to start${COLOR_RESET}"
    echo -e "${COLOR_CYAN}Or restart Termux if command is not active yet${COLOR_RESET}\n"
fi
