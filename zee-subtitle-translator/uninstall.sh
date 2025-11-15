#!/bin/bash
# ================================================================
# Zee Subtitle Translator - Uninstaller
# Removes global command and cleans up configuration
# ================================================================

set -e

COLOR_RESET='\033[0m'
COLOR_GREEN='\033[92m'
COLOR_YELLOW='\033[93m'
COLOR_RED='\033[91m'
COLOR_CYAN='\033[96m'

echo -e "${COLOR_CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════╗
║   ZEE SUBTITLE TRANSLATOR - UNINSTALLER   ║
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

# Confirm uninstall
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_YELLOW}Anda yakin ingin uninstall Zee Subtitle Translator?${COLOR_RESET}"
    echo "Ini akan:"
    echo "  - Hapus global command 'zeetranslator'"
    echo "  - Hapus alias dari shell config"
    echo "  - Hapus Termux widget (jika ada)"
    echo "  - TIDAK menghapus folder project dan Python packages"
    echo ""
    read -p "Lanjutkan? (y/n): " CONFIRM
else
    echo -e "\n${COLOR_YELLOW}Are you sure you want to uninstall Zee Subtitle Translator?${COLOR_RESET}"
    echo "This will:"
    echo "  - Remove global 'zeetranslator' command"
    echo "  - Remove alias from shell config"
    echo "  - Remove Termux widget (if exists)"
    echo "  - NOT delete project folder and Python packages"
    echo ""
    read -p "Continue? (y/n): " CONFIRM
fi

if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}Uninstall dibatalkan.${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}Uninstall cancelled.${COLOR_RESET}"
    fi
    exit 0
fi

# Detect shell config
if [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
else
    SHELL_CONFIG="$HOME/.profile"
fi

if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}[1/4] Menghapus alias dari $SHELL_CONFIG...${COLOR_RESET}"
else
    echo -e "\n${COLOR_CYAN}[1/4] Removing alias from $SHELL_CONFIG...${COLOR_RESET}"
fi

# Remove alias from shell config
if [ -f "$SHELL_CONFIG" ]; then
    # Create backup
    cp "$SHELL_CONFIG" "$SHELL_CONFIG.backup_$(date +%Y%m%d_%H%M%S)"
    
    # Remove Zee Subtitle Translator section
    sed -i.tmp '/# Zee Subtitle Translator/,/alias zeetranslator=/d' "$SHELL_CONFIG" 2>/dev/null || \
    sed -i '' '/# Zee Subtitle Translator/,/alias zeetranslator=/d' "$SHELL_CONFIG" 2>/dev/null || true
    
    # Clean up empty lines
    sed -i.tmp '/^$/N;/^\n$/d' "$SHELL_CONFIG" 2>/dev/null || \
    sed -i '' '/^$/N;/^\n$/d' "$SHELL_CONFIG" 2>/dev/null || true
    
    # Remove temp files
    rm -f "$SHELL_CONFIG.tmp" 2>/dev/null
    
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Alias dihapus dari $SHELL_CONFIG${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Alias removed from $SHELL_CONFIG${COLOR_RESET}"
    fi
else
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}⚠ File $SHELL_CONFIG tidak ditemukan${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}⚠ File $SHELL_CONFIG not found${COLOR_RESET}"
    fi
fi

# Remove Windows batch file (if exists)
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}[2/4] Memeriksa file Windows...${COLOR_RESET}"
else
    echo -e "\n${COLOR_CYAN}[2/4] Checking Windows files...${COLOR_RESET}"
fi

WIN_BATCH="$HOME/AppData/Local/Microsoft/WindowsApps/zeetranslator.bat"
if [ -f "$WIN_BATCH" ]; then
    rm -f "$WIN_BATCH"
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ File Windows batch dihapus${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Windows batch file removed${COLOR_RESET}"
    fi
else
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}⚠ Tidak ada file Windows batch${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}⚠ No Windows batch file${COLOR_RESET}"
    fi
fi

# Remove Termux widget (if exists)
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}[3/4] Memeriksa Termux widget...${COLOR_RESET}"
else
    echo -e "\n${COLOR_CYAN}[3/4] Checking Termux widget...${COLOR_RESET}"
fi

WIDGET_FILE="$HOME/.shortcuts/ZeeTranslator"
if [ -f "$WIDGET_FILE" ]; then
    rm -f "$WIDGET_FILE"
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ Termux widget dihapus${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Termux widget removed${COLOR_RESET}"
    fi
else
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}⚠ Tidak ada Termux widget${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}⚠ No Termux widget${COLOR_RESET}"
    fi
fi

# Remove config file
if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}[4/4] Menghapus file konfigurasi...${COLOR_RESET}"
else
    echo -e "\n${COLOR_CYAN}[4/4] Removing configuration file...${COLOR_RESET}"
fi

CONFIG_FILE="$HOME/.subtitletrans.conf"
if [ -f "$CONFIG_FILE" ]; then
    rm -f "$CONFIG_FILE"
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_GREEN}✓ File konfigurasi dihapus${COLOR_RESET}"
    else
        echo -e "${COLOR_GREEN}✓ Configuration file removed${COLOR_RESET}"
    fi
else
    if [ "$LANG" = "ID" ]; then
        echo -e "${COLOR_YELLOW}⚠ Tidak ada file konfigurasi${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}⚠ No configuration file${COLOR_RESET}"
    fi
fi

# Remove alias from current session
unalias zeetranslator 2>/dev/null || true

echo ""
echo -e "${COLOR_GREEN}╔═══════════════════════════════════════════╗${COLOR_RESET}"
if [ "$LANG" = "ID" ]; then
    echo -e "${COLOR_GREEN}║     Uninstall Berhasil Diselesaikan!     ║${COLOR_RESET}"
else
    echo -e "${COLOR_GREEN}║     Uninstall Completed Successfully!    ║${COLOR_RESET}"
fi
echo -e "${COLOR_GREEN}╚═══════════════════════════════════════════╝${COLOR_RESET}"

if [ "$LANG" = "ID" ]; then
    echo -e "\n${COLOR_CYAN}Yang dihapus:${COLOR_RESET}"
    echo "  ✓ Global command 'zeetranslator'"
    echo "  ✓ Alias dari shell config"
    echo "  ✓ Termux widget (jika ada)"
    echo "  ✓ File konfigurasi"
    echo ""
    echo -e "${COLOR_YELLOW}Yang TIDAK dihapus:${COLOR_RESET}"
    echo "  • Folder project: $(pwd)"
    echo "  • Python packages: srt, deep-translator, dll"
    echo "  • File backup: $SHELL_CONFIG.backup_*"
    echo ""
    echo -e "${COLOR_CYAN}Untuk menghapus folder project:${COLOR_RESET}"
    echo "  cd .."
    echo "  rm -rf zee-subtitle-translator"
    echo ""
    echo -e "${COLOR_CYAN}Untuk menghapus Python packages:${COLOR_RESET}"
    echo "  pip uninstall srt deep-translator tqdm chardet pysubs2"
    echo ""
    echo -e "${COLOR_CYAN}Untuk mengaktifkan perubahan di session ini:${COLOR_RESET}"
    echo "  source $SHELL_CONFIG"
    echo "  Atau buka terminal baru"
else
    echo -e "\n${COLOR_CYAN}What was removed:${COLOR_RESET}"
    echo "  ✓ Global command 'zeetranslator'"
    echo "  ✓ Alias from shell config"
    echo "  ✓ Termux widget (if exists)"
    echo "  ✓ Configuration file"
    echo ""
    echo -e "${COLOR_YELLOW}What was NOT removed:${COLOR_RESET}"
    echo "  • Project folder: $(pwd)"
    echo "  • Python packages: srt, deep-translator, etc"
    echo "  • Backup files: $SHELL_CONFIG.backup_*"
    echo ""
    echo -e "${COLOR_CYAN}To remove project folder:${COLOR_RESET}"
    echo "  cd .."
    echo "  rm -rf zee-subtitle-translator"
    echo ""
    echo -e "${COLOR_CYAN}To remove Python packages:${COLOR_RESET}"
    echo "  pip uninstall srt deep-translator tqdm chardet pysubs2"
    echo ""
    echo -e "${COLOR_CYAN}To apply changes in current session:${COLOR_RESET}"
    echo "  source $SHELL_CONFIG"
    echo "  Or open a new terminal"
fi

echo ""
