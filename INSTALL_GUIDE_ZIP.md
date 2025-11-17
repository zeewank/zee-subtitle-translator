# 📦 Installation Guide - For Users Who Downloaded ZIP

Panduan ini untuk Anda yang **download project sebagai ZIP file** dari GitHub, bukan pakai one-liner command.

---

## 🎯 Cara Install Setelah Download ZIP

### 🐧 Linux / macOS

#### 1. Extract ZIP file

```bash
# Kalau download di ~/Downloads/
cd ~/Downloads/
unzip zee-subtitle-translator-main.zip
cd zee-subtitle-translator-main/
```

#### 2. Jalankan installer

```bash
chmod +x installer.sh
./installer.sh
```

#### 3. Aktifkan command

```bash
source ~/.bashrc  # atau source ~/.zshrc untuk macOS
```

#### 4. Jalankan program

```bash
zeetranslator
```

---

### 🪟 Windows

#### 1. Extract ZIP file

- Klik kanan file ZIP
- Pilih **"Extract All..."**
- Pilih lokasi (contoh: `C:\Users\YourName\`)
- Klik **Extract**

#### 2. Buka folder hasil extract

```
C:\Users\YourName\zee-subtitle-translator-main\
```

#### 3. Jalankan installer

**Double-click file:**
```
install_windows.bat
```

**Atau lewat Command Prompt:**
```cmd
cd C:\Users\YourName\zee-subtitle-translator-main
install_windows.bat
```

#### 4. Restart Command Prompt

Tutup dan buka ulang Command Prompt / PowerShell

#### 5. Jalankan program

```cmd
zeetranslator
```

---

### 📱 Android (Termux)

#### 1. Extract ZIP file

Gunakan aplikasi **File Manager** atau **ZArchiver** untuk extract ZIP.

Contoh lokasi extract:
```
/storage/emulated/0/Download/zee-subtitle-translator-main/
```

#### 2. Buka Termux

#### 3. Masuk ke folder project

```bash
cd /storage/emulated/0/Download/zee-subtitle-translator-main/
```

**Atau** kalau ada di Internal Storage:
```bash
cd ~/storage/downloads/zee-subtitle-translator-main/
```

#### 4. Jalankan installer

```bash
chmod +x setup_termux.sh
./setup_termux.sh
```

#### 5. Aktifkan command

```bash
source ~/.bashrc
```

**Atau restart Termux**

#### 6. Jalankan program

```bash
zeetranslator
```

---

## 🔧 Troubleshooting

### Error: "installer.sh not found"

**Penyebab:** Anda belum masuk ke folder project

**Solusi:**
```bash
cd zee-subtitle-translator-main/
ls  # Harus melihat file installer.sh
./installer.sh
```

---

### Error: "Permission denied"

**Penyebab:** File tidak executable

**Solusi Linux/macOS/Android:**
```bash
chmod +x installer.sh
./installer.sh
```

---

### Error: "Python not found"

**Penyebab:** Python belum terinstall

**Solusi:**

**Linux:**
```bash
sudo apt install python3 python3-pip
```

**macOS:**
```bash
brew install python3
```

**Windows:**
Download dari https://www.python.org/downloads/  
**PENTING:** Centang "Add Python to PATH"

**Android:**
```bash
pkg install python
```

---

### Error: "requirements.txt not found"

**Penyebab:** Anda tidak berada di folder yang benar

**Solusi:**
```bash
# Pastikan Anda di folder project
ls
# Harus melihat file-file ini:
# - zee_translator.py
# - requirements.txt
# - installer.sh (Linux/macOS)
# - install_windows.bat (Windows)
# - setup_termux.sh (Android)
```

---

### Windows: Error saat jalankan install_windows.bat

**Penyebab:** Antivirus block atau permission

**Solusi:**
1. Klik kanan `install_windows.bat`
2. Pilih **"Run as Administrator"**
3. Atau disable Antivirus sementara

---

### Android: "Cannot access storage"

**Penyebab:** Termux belum punya izin storage

**Solusi:**
```bash
termux-setup-storage
# Klik "Allow" di popup
```

---

## 📂 Struktur File Setelah Extract

```
zee-subtitle-translator-main/
├── zee_translator.py           ← Main program
├── requirements.txt            ← Python dependencies
├── installer.sh                ← Linux/macOS installer
├── install_windows.bat         ← Windows installer
├── setup_termux.sh             ← Android installer
├── bootstrap_installer.sh      ← Bootstrap (optional)
├── bootstrap_installer.bat     ← Bootstrap (optional)
├── bootstrap_termux.sh         ← Bootstrap (optional)
├── uninstall.sh                ← Uninstaller
├── README.md                   ← Documentation
├── QUICKSTART.md               ← Quick guide
├── GUIDE.md                    ← Detailed guide
└── ...
```

---

## 🎯 File Installer yang Harus Dipakai

| Platform | File Installer |
|----------|----------------|
| **Linux** | `installer.sh` |
| **macOS** | `installer.sh` |
| **Windows** | `install_windows.bat` |
| **Android (Termux)** | `setup_termux.sh` |

---

## 🆚 Perbedaan: Installer vs Bootstrap

| | Traditional Installer | Bootstrap Installer |
|---|---|---|
| **Untuk siapa** | User yang sudah download ZIP | User yang belum download |
| **Cara pakai** | Jalankan di folder project | Copy-paste one-liner |
| **Download project** | Tidak (sudah ada) | Ya (otomatis) |
| **File** | `installer.sh`, `install_windows.bat`, `setup_termux.sh` | `bootstrap_installer.sh`, `bootstrap_installer.bat`, `bootstrap_termux.sh` |

**Kesimpulan:** Kalau sudah download ZIP, pakai **Traditional Installer**!

---

## ✅ Verification - Memastikan Instalasi Berhasil

Setelah install, coba jalankan:

```bash
zeetranslator
```

**Harus muncul:**
```
╔═══════════════════════════════════════════╗
║        ZEE SUBTITLE TRANSLATOR v1         ║
╚═══════════════════════════════════════════╝

Welcome!
------------------------------------------------------------
1. Translate Subtitles
2. UI Language Settings
3. Exit
------------------------------------------------------------
Choice [1-3]:
```

**Kalau muncul = SUCCESS!** ✅

---

## 🔗 Link Penting

- **GitHub Repository:** https://github.com/zeewank/zee-subtitle-translator
- **Report Issue:** https://github.com/zeewank/zee-subtitle-translator/issues
- **Documentation:** README.md, QUICKSTART.md, GUIDE.md

---

## 💡 Tips

1. **Simpan folder project** - Jangan hapus setelah install
2. **Bookmark lokasi folder** - Untuk update nanti
3. **Baca README.md** - Ada info lengkap tentang fitur
4. **Test dengan 1-2 file** - Sebelum translate banyak file

---

**Selamat menggunakan Zee Subtitle Translator! 🎬**
