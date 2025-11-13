#!/bin/bash
# ================================================================
# Zee Subtitle Translator - Automatic Installer (FIXED)
# Version 1.0 - Now with proper dependency installation!
# ================================================================

set -e

COLOR_RESET='\033[0m'
COLOR_GREEN='\033[92m'
COLOR_YELLOW='\033[93m'
COLOR_RED='\033[91m'
COLOR_CYAN='\033[96m'
COLOR_MAGENTA='\033[95m'

# Language Selection
echo -e "${COLOR_CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════╗
║    ZEE SUBTITLE TRANSLATOR INSTALLER      ║
║              Version 1.0                  ║
╚═══════════════════════════════════════════╝
EOF
echo -e "${COLOR_RESET}"

echo -e "${COLOR_YELLOW}Select Language / Pilih Bahasa:${COLOR_RESET}"
echo "  1) English"
echo "  2) Bahasa Indonesia"
read -p "Choice / Pilihan [1-2]: " LANG_CHOICE

if [ "$LANG_CHOICE" = "2" ]; then
    LANG="ID"
else
    LANG="EN"
fi

# Language functions
msg_checking_python() {
    if [ "$LANG" = "ID" ]; then
        echo "[1/5] Memeriksa instalasi Python..."
    else
        echo "[1/5] Checking Python installation..."
    fi
}

msg_python_not_found() {
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_RED}✗ Python 3 tidak terinstal!${COLOR_RESET}"
        echo "Silakan instal Python 3.7 atau lebih tinggi dari https://python.org"
    else
        echo -e "${COLOR_RED}✗ Python 3 is not installed!${COLOR_RESET}"
        echo "Please install Python 3.7 or higher from https://python.org"
    fi
}

msg_python_detected() {
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Python terdeteksi${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Python detected${COLOR_RESET}"
    fi
}

msg_checking_pip() {
    if [ "$LANG" = "ID" ]; then
        echo -e "\n${COLOR_YELLOW}[2/5] Memeriksa instalasi pip...${COLOR_RESET}"
    else
        echo -e "\n${COLOR_YELLOW}[2/5] Checking pip installation...${COLOR_RESET}"
    fi
}

msg_pip_ready() {
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ pip siap digunakan${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ pip is ready${COLOR_RESET}"
    fi
}

msg_installing() {
    if [ "$LANG" = "ID" ]; then
        echo -e "\n${COLOR_YELLOW}[3/5] Menginstal paket yang diperlukan...${COLOR_RESET}"
        echo "Ini mungkin memakan waktu beberapa menit..."
    else
        echo -e "\n${COLOR_YELLOW}[3/5] Installing required packages...${COLOR_RESET}"
        echo "This may take a few minutes..."
    fi
}

msg_success() {
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Semua dependensi berhasil diinstal${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ All dependencies installed successfully${COLOR_RESET}"
    fi
}

msg_failed() {
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_RED}✗ Gagal menginstal beberapa dependensi${COLOR_RESET}"
    else
        echo -e "${COLOR_RED}✗ Failed to install some dependencies${COLOR_RESET}"
    fi
}

msg_setup_permissions() {
    if [ "$LANG" = "ID" ]; then
        echo -e "\n${COLOR_YELLOW}[4/5] Mengatur izin executable...${COLOR_RESET}"
    else
        echo -e "\n${COLOR_YELLOW}[4/5] Setting up executable permissions...${COLOR_RESET}"
    fi
}

msg_setup_global() {
    if [ "$LANG" = "ID" ]; then
        echo -e "\n${COLOR_YELLOW}[5/5] Mengatur command global 'zeetranslator'...${COLOR_RESET}"
    else
        echo -e "\n${COLOR_YELLOW}[5/5] Setting up global 'zeetranslator' command...${COLOR_RESET}"
    fi
}

msg_setup_complete() {
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Pengaturan selesai${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Setup complete${COLOR_RESET}"
    fi
}

msg_installation_complete() {
    if [ "$LANG" = "ID" ]; then
        echo -e "\n${COLOR_GREEN}═══════════════════════════════════════════${COLOR_RESET}"
        echo -e "${COLOR_GREEN}    Instalasi berhasil diselesaikan!${COLOR_RESET}"
        echo -e "${COLOR_GREEN}═══════════════════════════════════════════${COLOR_RESET}"
    else
        echo -e "\n${COLOR_GREEN}═══════════════════════════════════════════${COLOR_RESET}"
        echo -e "${COLOR_GREEN}    Installation completed successfully!${COLOR_RESET}"
        echo -e "${COLOR_GREEN}═══════════════════════════════════════════${COLOR_RESET}"
    fi
}

msg_quick_start() {
    if [ "$LANG" = "ID" ]; then
        echo -e "\n${COLOR_CYAN}Mulai Cepat:${COLOR_RESET}"
        echo -e "  ${COLOR_GREEN}zeetranslator${COLOR_RESET}                # Jalankan dari mana saja!"
        echo "  ./zee_translator.py              # Cara alternatif"
        echo "  python3 zee_translator.py        # Cara manual"
        echo ""
        echo -e "${COLOR_CYAN}Contoh Penggunaan:${COLOR_RESET}"
        echo "  zeetranslator ~/Videos/Subtitles # Translate folder tertentu"
        echo ""
        echo -e "${COLOR_CYAN}Untuk informasi lebih lanjut:${COLOR_RESET}"
        echo "  Lihat README.md untuk panduan lengkap"
    else
        echo -e "\n${COLOR_CYAN}Quick Start:${COLOR_RESET}"
        echo -e "  ${COLOR_GREEN}zeetranslator${COLOR_RESET}                # Run from anywhere!"
        echo "  ./zee_translator.py              # Alternative way"
        echo "  python3 zee_translator.py        # Manual way"
        echo ""
        echo -e "${COLOR_CYAN}Usage Examples:${COLOR_RESET}"
        echo "  zeetranslator ~/Videos/Subtitles # Translate specific folder"
        echo ""
        echo -e "${COLOR_CYAN}For more information:${COLOR_RESET}"
        echo "  See README.md for detailed usage"
    fi
    echo "  Visit: https://github.com/zeewank/zee-subtitle-translator"
}

msg_support() {
    echo ""
    echo -e "${COLOR_MAGENTA}═══════════════════════════════════════════${COLOR_RESET}"
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_MAGENTA}   💖 Dukung Proyek Ini / Support This Project${COLOR_RESET}"
    else
        echo -e "${COLOR_MAGENTA}          💖 Support This Project${COLOR_RESET}"
    fi
    echo -e "${COLOR_MAGENTA}═══════════════════════════════════════════${COLOR_RESET}"
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}Jika tool ini bermanfaat, pertimbangkan untuk berdonasi:${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}If this tool is helpful, consider donating:${COLOR_RESET}"
    fi
    echo ""
    echo -e "${COLOR_CYAN}  🌍 PayPal: https://paypal.me/zeewank${COLOR_RESET}"
    echo -e "${COLOR_CYAN}  🇮🇩 Trakteer: https://trakteer.id/zeewank/tip${COLOR_RESET}"
    echo ""
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}Setiap dukungan sangat berarti untuk pengembangan! 🙏${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}Every support means a lot for development! 🙏${COLOR_RESET}"
    fi
    echo -e "${COLOR_MAGENTA}═══════════════════════════════════════════${COLOR_RESET}"
}

# ============================================================
# START INSTALLATION
# ============================================================

# [1/5] Check Python
msg_checking_python
if ! command -v python3 &> /dev/null; then
    msg_python_not_found
    exit 1
fi

msg_python_detected
python3 --version
echo

# [2/5] Check pip
msg_checking_pip
python3 -m pip --version &> /dev/null
if [ $? -ne 0 ]; then
    if [ "$LANG" = "ID" ]; then
        echo "[!] pip tidak ditemukan, menginstal..."
    else
        echo "[!] pip not found, installing..."
    fi
    python3 -m ensurepip --upgrade
fi
msg_pip_ready

# Upgrade pip
if [ "$LANG" = "ID" ]; then
    echo "Memperbarui pip..."
else
    echo "Upgrading pip..."
fi
python3 -m pip install --upgrade pip --quiet
echo

# [3/5] Install dependencies - THIS WAS MISSING!
msg_installing
python3 -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo
    msg_success
else
    echo
    msg_failed
    exit 1
fi

# [4/5] Setup permissions
msg_setup_permissions
chmod +x zee_translator.py
msg_setup_complete

# [5/5] Setup global command
msg_setup_global

# Get absolute path to script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/zee_translator.py"

# Detect shell and config file
if [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
else
    SHELL_CONFIG="$HOME/.profile"
fi

# Check if alias already exists
if grep -q "alias zeetranslator=" "$SHELL_CONFIG" 2>/dev/null; then
    if [ "$LANG" = "ID" ]; then
        echo "[!] Alias 'zeetranslator' sudah ada, melewati..."
    else
        echo "[!] Alias 'zeetranslator' already exists, skipping..."
    fi
else
    # Add alias to shell config
    echo "" >> "$SHELL_CONFIG"
    echo "# Zee Subtitle Translator" >> "$SHELL_CONFIG"
    echo "alias zeetranslator='python3 $SCRIPT_PATH'" >> "$SHELL_CONFIG"
    
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Command global 'zeetranslator' berhasil ditambahkan!${COLOR_RESET}"
        echo -e "${COLOR_YELLOW}⚠️  Jalankan: source $SHELL_CONFIG${COLOR_RESET}"
        echo -e "${COLOR_YELLOW}   Atau buka terminal baru untuk mengaktifkan command${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Global 'zeetranslator' command added successfully!${COLOR_RESET}"
        echo -e "${COLOR_YELLOW}⚠️  Run: source $SHELL_CONFIG${COLOR_RESET}"
        echo -e "${COLOR_YELLOW}   Or open a new terminal to activate the command${COLOR_RESET}"
    fi
fi

msg_installation_complete
msg_quick_start
msg_support

# Auto-reload shell config
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}Mengaktifkan command global...${COLOR_RESET}"
else
    echo -e "\n${COLOR_CYAN}Activating global command...${COLOR_RESET}"
fi

source "$SHELL_CONFIG" 2>/dev/null || true

if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_GREEN}✓ Siap digunakan! Ketik 'zeetranslator' untuk memulai${COLOR_RESET}\n"
else
    echo -e "${COLOR_GREEN}✓ Ready to use! Type 'zeetranslator' to start${COLOR_RESET}\n"
fi
