# Tutorial Instalasi Lengkap - Semua Platform

Panduan install Zee Subtitle Translator untuk pemula di Linux, Windows, dan Android.

## Fitur-Fitur

- Banyak pilihan mesin terjemah (Google Translate gratis atau DeepL API)
- Terjemahkan banyak file sekaligus
- Pilih file dengan mudah menggunakan browser interaktif
- Bersihin teks otomatis (hapus tag [MUSIC], (SOUND), dll)
- Kasih kredit nama Anda di subtitle hasil terjemahan
- Pantau progress dengan progress bar
- Support format SRT, VTT, dan ASS
- Deteksi encoding otomatis dan nama yang tidak perlu diterjemahkan
- Atur kecepatan: Aman (lambat), Standar, atau Agresif (cepat)
- Menu dalam bahasa Inggris atau Indonesia

---

## TUTORIAL LINUX (Ubuntu/Debian)

### Langkah 1: Update System

Buka Terminal (Ctrl + Alt + T) dan jalankan:

```bash
sudo apt update
sudo apt upgrade -y
```

Masukkan password jika diminta.

### Langkah 2: Install Python dan Git

```bash
sudo apt install -y python3 python3-pip git
```

Verifikasi instalasi:
```bash
python3 --version    # Harus Python 3.7 ke atas
pip3 --version
git --version
```

### Langkah 3: Download Project

```bash
# Pindah ke Home directory
cd ~

# Clone repository
git clone https://github.com/zeewank/zee-subtitle-translator.git

# Masuk ke folder
cd zee-subtitle-translator
```

### Langkah 4: Install Dependencies

```bash
# Jalankan installer
chmod +x installer.sh
./installer.sh
```

Pilih bahasa:
- Ketik `1` untuk English
- Ketik `2` untuk Bahasa Indonesia

Tunggu sampai selesai (2-5 menit).

### Langkah 5: Test Program

```bash
zeetranslator
```

Harus muncul menu utama dengan logo Zee Subtitle Translator.

**Instalasi Linux selesai.**

### Cara Menjalankan

```bash
# Dari mana saja (karena sudah global):
zeetranslator

# Atau cara tradisional:
cd ~/zee-subtitle-translator
./zee_translator.py

# Atau dengan Python:
python3 ~/zee-subtitle-translator/zee_translator.py

# Dengan path folder langsung:
zeetranslator ~/Videos/Subtitles
```

### Membuat Shortcut Desktop (Optional)

```bash
# Buat file .desktop
cat > ~/.local/share/applications/zeetranslator.desktop << 'EOF'
[Desktop Entry]
Name=Zee Translator
Comment=Subtitle Translator Tool
Exec=gnome-terminal -- zeetranslator
Icon=subtitle
Terminal=true
Type=Application
Categories=Utility;
EOF

# Update database
update-desktop-database ~/.local/share/applications/
```

Sekarang bisa dicari di Applications menu.

---

## TUTORIAL WINDOWS 10/11

### Langkah 1: Install Python

**Download Python:**
1. Buka browser, ke [python.org/downloads](https://www.python.org/downloads/)
2. Klik tombol hijau "Download Python 3.x.x"
3. File .exe akan terdownload

**Install Python:**
1. Double-click file installer
2. **PENTING:** Centang "Add Python to PATH" di bagian bawah
3. Klik "Install Now"
4. Tunggu sampai selesai
5. Klik "Close"

**Verifikasi:**
1. Tekan Win + R
2. Ketik `cmd` lalu Enter
3. Di Command Prompt, ketik:
   ```cmd
   python --version
   ```
4. Harus muncul: `Python 3.x.x`

### Langkah 2: Download Project

**Cara 1: Download ZIP (Paling Mudah)**

1. Buka browser ke [github.com/zeewank/zee-subtitle-translator](https://github.com/zeewank/zee-subtitle-translator)
2. Klik tombol hijau "Code"
3. Klik "Download ZIP"
4. Extract ZIP:
   - Klik kanan file ZIP
   - Pilih "Extract All..."
   - Pilih lokasi (contoh: `C:\ZeeTranslator\`)
   - Klik "Extract"

**Cara 2: Git Clone (Butuh Git)**

1. Install Git dari [git-scm.com/download/win](https://git-scm.com/download/win)
2. Buka Command Prompt
3. Ketik:
   ```cmd
   cd C:\
   git clone https://github.com/zeewank/zee-subtitle-translator.git
   cd zee-subtitle-translator
   ```

### Langkah 3: Install Dependencies

**Cara Otomatis (Recommended):**

1. Buka folder project di File Explorer
2. Double-click file `install_windows.bat`
3. Tunggu proses install (2-5 menit)
4. Akan muncul pesan sukses
5. Press any key untuk close

**Cara Manual (Jika otomatis gagal):**

1. Buka Command Prompt di folder project:
   - Buka File Explorer
   - Navigate ke folder `zee-subtitle-translator`
   - Klik address bar
   - Ketik `cmd` lalu Enter

2. Install dependencies:
   ```cmd
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

3. Tunggu sampai selesai

### Langkah 4: Test Program

**Cara 1: Command Prompt**
```cmd
zeetranslator
```

**Cara 2: Double-click**
- Double-click file `run_translator.bat`

Harus muncul menu utama.

**Instalasi Windows selesai.**

### Cara Menjalankan

**Termudah:**
```cmd
zeetranslator
```

**Dari Command Prompt:**
```cmd
cd C:\ZeeTranslator
python zee_translator.py
```

**Dengan path folder:**
```cmd
zeetranslator "C:\Users\NamaAnda\Videos\Subtitles"
```

### Membuat Desktop Shortcut

1. Klik kanan pada `run_translator.bat`
2. Pilih "Send to" → "Desktop (create shortcut)"
3. Rename shortcut jadi "Zee Translator"
4. Double-click untuk menjalankan

### Troubleshooting Windows

**Problem: "Python is not recognized"**

Solusi:
1. Uninstall Python
2. Install ulang
3. **PASTIKAN centang "Add Python to PATH"**

**Problem: "pip is not recognized"**

Solusi:
```cmd
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

**Problem: "Permission denied"**

Solusi:
- Klik kanan Command Prompt
- Pilih "Run as Administrator"
- Atau disable Antivirus sementara

---

## TUTORIAL ANDROID (Termux)

### Langkah 1: Install Termux

**PENTING: Jangan install dari Google Play Store!**

**Cara 1: F-Droid (Recommended)**

1. Download F-Droid:
   - Buka browser di HP
   - Ke [f-droid.org](https://f-droid.org)
   - Download F-Droid APK
   - Install (enable "Unknown sources" jika diminta)

2. Install Termux dari F-Droid:
   - Buka F-Droid app
   - Cari "Termux"
   - Install

**Cara 2: GitHub Direct**

1. Buka browser
2. Ke [github.com/termux/termux-app/releases](https://github.com/termux/termux-app/releases)
3. Download file `termux-app_vX.XX.apk` (yang terbaru)
4. Install APK (enable "Unknown sources")

### Langkah 2: Update Termux

Buka Termux, lalu jalankan:

```bash
# Update package list
pkg update -y

# Upgrade packages
pkg upgrade -y
```

Ketik `y` dan Enter jika ditanya.

### Langkah 3: Install Git

```bash
pkg install -y git
```

Tunggu 1-2 menit.

### Langkah 4: Download Project

```bash
# Clone repository
git clone https://github.com/zeewank/zee-subtitle-translator.git

# Masuk ke folder
cd zee-subtitle-translator
```

### Langkah 5: Install Dependencies

```bash
# Jalankan script setup
chmod +x setup_termux.sh
./setup_termux.sh
```

Pilih bahasa:
- Ketik `1` untuk English
- Ketik `2` untuk Bahasa Indonesia

Script ini akan otomatis:
- Install Python dan dependencies
- Setup storage access (klik "Allow" saat popup muncul)
- Buat shortcut ke Downloads, Movies, DCIM
- Setup global command
- Buat widget Termux

Tunggu 3-5 menit sampai selesai.

### Langkah 6: Test Program

```bash
zeetranslator
```

Harus muncul menu utama.

**Instalasi Android selesai.**

### Cara Menjalankan di Android

**Basic:**
```bash
zeetranslator
```

**Dengan folder tertentu:**
```bash
# Translate folder di Downloads
zeetranslator ~/downloads/Subtitles

# Translate folder di Movies
zeetranslator ~/movies/MyMovie/
```

**Cara tradisional:**
```bash
cd ~/zee-subtitle-translator
./zee_translator.py
```

### Setup Widget Termux

1. Long-press home screen
2. Tap "Widgets"
3. Cari "Termux:Widget"
4. Drag ke home screen
5. Pilih "ZeeTranslator"
6. Tap widget untuk langsung buka translator

### Tips Android

**Install Keyboard yang Bagus:**
- Install "Hacker's Keyboard" dari Play Store
- Lebih mudah untuk ketik command

**Keep Screen On:**
- Termux → Settings → Enable "Wake Lock"
- Screen tidak mati saat translate

**Prevent Kill:**
- Settings → Apps → Termux → Battery
- Disable "Battery optimization"
- Allow background activity

**Use Tmux (For Long Jobs):**
```bash
# Install tmux
pkg install tmux

# Start tmux session
tmux new -s translation

# Run translator
zeetranslator

# Detach: Ctrl+B lalu tekan D
# Screen bisa diminimize, proses tetap jalan

# Attach kembali nanti:
tmux attach -t translation
```

### Troubleshooting Android

**Problem: "Permission denied" saat ./zee_translator.py**

Solusi:
```bash
chmod +x zee_translator.py
# Atau:
python zee_translator.py
```

**Problem: "Cannot access /storage/emulated/0"**

Solusi:
```bash
termux-setup-storage
# Klik "Allow" di popup
```

**Problem: "Module not found"**

Solusi:
```bash
pip install --force-reinstall -r requirements.txt
```

**Problem: Termux crash saat translate**

Solusi:
- Enable Wake Lock di Settings
- Disable battery optimization
- Keep phone charging
- Gunakan Safe mode untuk stability

---

## Verification Checklist

Setelah install di platform apapun, cek:

- [ ] Program bisa dijalankan
- [ ] Menu utama muncul dengan baik
- [ ] Bisa browse folder
- [ ] Test translate 1-2 file kecil
- [ ] Output file terbuat dengan benar
- [ ] Colors tampil (optional, tergantung terminal)

---

## Quick Reference

### Linux
```bash
zeetranslator
# atau
cd ~/zee-subtitle-translator
./zee_translator.py
```

### Windows
```cmd
zeetranslator
# atau double-click: run_translator.bat
```

### Android
```bash
zeetranslator
# atau tap widget Termux
```

---

## Contoh Penggunaan

### Translate Satu Film

```bash
# Taruh file movie.srt di folder
cd ~/Movies/MyMovie
zeetranslator

# Pilih:
# - Current folder
# - All files
# - Same folder output
# - Standard speed
# - Language: id

# Hasil: movie.id.srt terbuat
```

### Translate TV Series (Satu Season)

```bash
# Navigate ke season folder
cd ~/Series/BreakingBad/Season1
zeetranslator

# Pilih:
# - Current folder
# - All files
# - New subfolder: "Indonesian"
# - Standard speed
# - Language: id

# Hasil: folder Indonesian/ dengan semua file .id.srt
```

### Translate Multiple Seasons

```bash
zeetranslator

# Pilih:
# - Multiple folders
# - Browse ke Season1 → ketik s (select)
# - Browse ke Season2 → ketik s (select)
# - Browse ke Season3 → ketik s (select)
# - Ketik 0 (finish)
# - Keep structure
# - Standard speed
# - Language: id

# Hasil: Setiap season dapat file terjemahan di folder aslinya
```

---

## Tips

**Yang Harus Dilakukan:**
- Mulai dengan Standard mode
- Test dengan 1-2 file dulu
- Backup file original
- Gunakan WiFi untuk batch besar
- Organisir file sebelum translate

**Yang Jangan Dilakukan:**
- Jangan pakai Aggressive mode di percobaan pertama
- Jangan translate 100+ file sekaligus
- Jangan hapus file original langsung
- Jangan close terminal saat processing
- Jangan pakai mobile data untuk batch besar

---

## Support Project

Jika tool ini bermanfaat:

**PayPal (International):**
```
https://paypal.me/zeewank
```

**Trakteer (Indonesia):**
```
https://trakteer.id/zeewank/tip
```

Setiap dukungan sangat membantu pengembangan project ini.

---

## Butuh Bantuan?

- Baca [README.md](README.md) untuk panduan umum
- Lihat [FAQ.md](FAQ.md) untuk masalah umum
- Lihat [GUIDE.md](GUIDE.md) untuk panduan detail
- Buka issue di [GitHub](https://github.com/zeewank/zee-subtitle-translator/issues)

---

**Selamat menggunakan Zee Subtitle Translator!**
