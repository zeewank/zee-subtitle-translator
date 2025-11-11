#!/bin/bash
# ================================================================
# Zee Subtitle Translator - Automatic Installer
# Version 1.0 - Language Selection: EN/ID
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
        echo "[1/4] Memeriksa instalasi Python..."
    else
        echo "[1/4] Checking Python installation..."
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
        echo -e "\n${COLOR_YELLOW}[2/4] Memeriksa instalasi pip...${COLOR_RESET}"
    else
        echo -e "\n${COLOR_YELLOW}[2/4] Checking pip installation...${COLOR_RESET}"
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
        echo -e "\n${COLOR_YELLOW}[3/4] Menginstal paket yang diperlukan...${COLOR_RESET}"
        echo "Ini mungkin memakan waktu beberapa menit..."
    else
        echo -e "\n${COLOR_YELLOW}[3/4] Installing required packages...${COLOR_RESET}"
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
        echo -e "\n${COLOR_YELLOW}[4/4] Mengatur izin executable...${COLOR_RESET}"
    else
        echo -e "\n${COLOR_YELLOW}[4/4] Setting up executable permissions...${COLOR_RESET}"
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
        echo "  ./zee_translator.py              # Jalankan program"
        echo "  python3 zee_translator.py        # Cara alternatif"
        echo ""
        echo -e "${COLOR_CYAN}Untuk informasi lebih lanjut:${COLOR_RESET}"
        echo "  Lihat README.md untuk panduan lengkap"
    else
        echo -e "\n${COLOR_CYAN}Quick Start:${COLOR_RESET}"
        echo "  ./zee_translator.py              # Run the program"
        echo "  python3 zee_translator.py        # Alternative way"
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

# Start installation
msg_checking_python
if ! command -v python3 &> /dev/null; then
    msg_python_not_found
    exit 1
fi

msg_python_detected
python3 --version
echo

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
echo

if [ "$LANG" = "ID" ]; then
    echo "Memperbarui pip..."
else
    echo "Upgrading pip..."
fi
python3 -m pip install --upgrade pip --quiet
msg_installing
echo


if [ $? -eq 0 ]; then
    echo
    msg_success
else
    echo
    msg_failed
    exit 1
fi

msg_setup_permissions
chmod +x zee_translator.py
msg_setup_complete

msg_installation_complete
msg_quick_start
msg_support
echo
