# 📚 Tutorial Instalasi Lengkap - Semua Platform

Panduan install Zee Subtitle Translator untuk pemula di Linux, Windows, dan Android.

✨ Fitur-Fitur

- 🚀 Banyak Pilihan Mesin Terjemah: Bisa pakai Google Translate (gratis) atau DeepL API
- 📁 Terjemahkan Banyak File Sekaligus: Gak perlu satu-satu, bisa langsung banyak file dan folder
- 🎯 Pilih File dengan Mudah: Ada browser file interaktif yang gampang dipake, bisa pilih dari beberapa folder sekaligus
- 🧹 Bersihin Teks Otomatis: Hapus sendiri tag-tag kayak [MUSIC], (SOUND), dan yang sejenis
- 🎬 Kasih Nama Anda: Tambahin kredit atau nama Anda di subtitle hasil terjemahan
- 📊 Pantau Progress: Ada progress bar yang jalan dan laporan lengkap setelah selesai
- 🔤 Support Banyak Format: SRT, VTT, sama ASS semua bisa
- 🧠 Deteksi Pintar: Otomatis deteksi encoding file dan nama-nama yang gak perlu diterjemahkan
- ⚡ Atur Kecepatan: Pilih mode Aman (lambat tapi aman), Standar, atau Agresif (cepat tapi berisiko)
- 🌍 Dua Bahasa: Menu bisa dalam bahasa Inggris atau Indonesia, terserah Anda

---

## 🐧 TUTORIAL LINUX (Ubuntu/Debian)

### Langkah 1: Update System

Buka **Terminal** (Ctrl + Alt + T) dan jalankan:

```bash
sudo apt update
sudo apt upgrade -y
```

Masukkan password Anda jika diminta.

### Langkah 2: Install Python & Git

```bash
sudo apt install -y python3 python3-pip git
```

Verifikasi install:
```bash
python3 --version    # Harus Python 3.7+
pip3 --version       # Harus ada
git --version        # Harus ada
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

**Pilih bahasa:**
- Ketik `1` untuk English
- Ketik `2` untuk Bahasa Indonesia

Tunggu sampai selesai (2-5 menit).

### Langkah 5: Test Program

```bash
./zee_translator.py
```

**Harus muncul:**
```
╔═══════════════════════════════════════════╗
║                                           ║
║        ZEE SUBTITLE TRANSLATOR v1.0       ║
║                                           ║
╚═══════════════════════════════════════════╝
Selamat datang!
```

✅ **Instalasi Linux Berhasil!**

### Cara Menjalankan:

```bash
# Method 1: Direct
cd ~/zee-subtitle-translator
./zee_translator.py

# Method 2: With Python
python3 ~/zee-subtitle-translator/zee_translator.py

# Method 3: Dengan path folder
./zee_translator.py ~/Videos/Subtitles
```

### Membuat Shortcut (Optional):

```bash
# Buat alias di ~/.bashrc
echo 'alias ztrans="python3 ~/zee-subtitle-translator/zee_translator.py"' >> ~/.bashrc
source ~/.bashrc

# Sekarang bisa pakai:
ztrans
```

---

## 🪟 TUTORIAL WINDOWS 10/11

### Langkah 1: Install Python

1. **Download Python:**
   - Buka [python.org/downloads](https://www.python.org/downloads/)
   - Klik "Download Python 3.x.x" (versi terbaru)
   - File `.exe` akan terdownload

2. **Install Python:**
   - **Double-click** file yang didownload
   - ⚠️ **PENTING:** **Centang** ✅ **"Add Python to PATH"** di bagian bawah
   - Klik **"Install Now"**
   - Tunggu sampai selesai
   - Klik **"Close"**

3. **Verifikasi Install:**
   - Tekan **Win + R**
   - Ketik `cmd` lalu Enter
   - Di Command Prompt, ketik:
     ```cmd
     python --version
     ```
   - Harus muncul: `Python 3.x.x`

### Langkah 2: Download Project

**Method 1: Download ZIP (Paling Mudah)**

1. **Buka browser** ke:
   ```
   https://github.com/zeewank/zee-subtitle-translator
   ```

2. **Klik tombol hijau "Code"**

3. **Klik "Download ZIP"**

4. **Extract ZIP:**
   - Klik kanan file ZIP
   - Pilih "Extract All..."
   - Pilih lokasi (misalnya `C:\ZeeTranslator\`)
   - Klik "Extract"

**Method 2: Git Clone (Butuh Git)**

1. **Install Git:**
   - Download dari [git-scm.com/download/win](https://git-scm.com/download/win)
   - Install dengan setting default

2. **Clone repository:**
   ```cmd
   cd C:\
   git clone https://github.com/zeewank/zee-subtitle-translator.git
   cd zee-subtitle-translator
   ```

### Langkah 3: Install Dependencies

**Method 1: Auto Installer (Recommended)**

1. **Buka folder project** di File Explorer
2. **Double-click** file `install_windows.bat`
3. Tunggu proses install (2-5 menit)
4. Akan muncul pesan sukses
5. Press any key untuk close

**Method 2: Manual (Jika auto gagal)**

1. **Buka Command Prompt di folder project:**
   - Buka File Explorer
   - Navigate ke folder `zee-subtitle-translator`
   - Klik di address bar (path folder di atas)
   - Ketik `cmd` lalu Enter

2. **Install dependencies:**
   ```cmd
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

3. Tunggu sampai selesai

### Langkah 4: Test Program

**Method 1: Double-click**
- Double-click file `run_translator.bat`

**Method 2: Command Prompt**
```cmd
python zee_translator.py
```

**Harus muncul menu utama!**

✅ **Instalasi Windows Berhasil!**

### Cara Menjalankan:

**Termudah:**
- Double-click `run_translator.bat`

**Dari Command Prompt:**
```cmd
cd C:\ZeeTranslator
python zee_translator.py
```

**Dengan path folder:**
```cmd
python zee_translator.py "C:\Users\YourName\Videos\Subtitles"
```

### Membuat Desktop Shortcut:

1. **Klik kanan** pada `run_translator.bat`
2. Pilih **"Send to"** → **"Desktop (create shortcut)"**
3. Rename shortcut jadi "Zee Translator"
4. Double-click untuk run!

### Troubleshooting Windows:

**Problem: "Python is not recognized"**

Solution:
1. Uninstall Python
2. Install ulang
3. ✅ **CENTANG "Add Python to PATH"**

**Problem: "pip is not recognized"**

Solution:
```cmd
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

**Problem: "Permission denied"**

Solution:
- Run Command Prompt as Administrator
- Atau disable Antivirus sementara

---

## 📱 TUTORIAL ANDROID (Termux)

### Langkah 1: Install Termux

⚠️ **PENTING: Jangan install dari Google Play Store!**

**Method 1: F-Droid (Recommended)**

1. **Download F-Droid:**
   - Buka browser di HP
   - Ke [f-droid.org](https://f-droid.org)
   - Download F-Droid APK
   - Install F-Droid (enable "Unknown sources" jika diminta)

2. **Install Termux dari F-Droid:**
   - Buka F-Droid app
   - Search "Termux"
   - Install

**Method 2: GitHub Direct**

1. **Download Termux APK:**
   - Buka browser
   - Ke [github.com/termux/termux-app/releases](https://github.com/termux/termux-app/releases)
   - Download file `termux-app_vX.XX.apk` (yang terbaru)
   - Install APK (enable "Unknown sources")

### Langkah 2: Setup Termux

**Buka Termux**, lalu jalankan command ini **SATU PER SATU**:

```bash
# Update package list
pkg update -y

# Upgrade packages
pkg upgrade -y
```

*Ketik `y` dan Enter jika ditanya.*

```bash
# Install Python dan Git
pkg install -y python git
```

*Tunggu 2-5 menit.*

```bash
# Verifikasi install
python --version
git --version
```

Harus muncul versi Python dan Git.

### Langkah 3: Setup Storage Access

**Agar bisa akses file HP:**

```bash
termux-setup-storage
```

**Popup muncul** → **"Allow"**

**Buat shortcut ke folder HP:**

```bash
# Shortcut ke Downloads
ln -s /storage/emulated/0/Download ~/downloads

# Shortcut ke Movies
ln -s /storage/emulated/0/Movies ~/movies

# Shortcut ke DCIM
ln -s /storage/emulated/0/DCIM ~/dcim
```

Test:
```bash
ls ~/downloads    # Harus tampil isi Downloads
ls ~/movies       # Harus tampil isi Movies
```

### Langkah 4: Download Project

```bash
# Pindah ke home
cd ~

# Clone repository
git clone https://github.com/zeewank/zee-subtitle-translator.git

# Masuk ke folder
cd zee-subtitle-translator
```

### Langkah 5: Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt
```

*Tunggu 3-5 menit.*

```bash
# Make executable
chmod +x zee_translator.py
```

### Langkah 6: Test Program

```bash
./zee_translator.py
```

**Harus muncul menu!**

✅ **Instalasi Android Berhasil!**

### Cara Menjalankan di Android:

**Basic:**
```bash
cd ~/zee-subtitle-translator
./zee_translator.py
```

**Dengan folder:**
```bash
./zee_translator.py ~/downloads/Subtitles
```

**Translate file di Movies:**
```bash
./zee_translator.py ~/movies/MyMovie/
```

### Membuat Shortcut di Termux:

**Method 1: Alias**

```bash
# Edit .bashrc
nano ~/.bashrc

# Tambahkan di akhir file:
alias ztrans='python ~/zee-subtitle-translator/zee_translator.py'

# Save: Ctrl+X, Y, Enter

# Reload bashrc
source ~/.bashrc

# Sekarang bisa pakai:
ztrans
```

**Method 2: Script**

```bash
# Buat script
cat > ~/ztrans.sh << 'EOF'
#!/bin/bash
cd ~/zee-subtitle-translator
python zee_translator.py "$@"
EOF

# Make executable
chmod +x ~/ztrans.sh

# Run dengan:
~/ztrans.sh
```

**Method 3: Widget (Advanced)**

```bash
# Buat folder widget
mkdir -p ~/.shortcuts

# Buat script widget
cat > ~/.shortcuts/ZeeTranslator << 'EOF'
#!/bin/bash
cd ~/zee-subtitle-translator
./zee_translator.py
EOF

chmod +x ~/.shortcuts/ZeeTranslator
```

**Cara pakai Widget:**
1. Long-press home screen
2. Add Widget
3. Pilih "Termux:Widget"
4. Select "ZeeTranslator"
5. Tap widget untuk run!

### Tips Android:

**1. Install Keyboard yang Bagus:**
- Install "Hacker's Keyboard" dari Play Store
- Lebih mudah ketik command

**2. Keep Screen On:**
- Termux → Settings → Enable "Wake Lock"
- Screen tidak mati saat translate

**3. Prevent Kill:**
- Settings → Apps → Termux → Battery
- Disable "Battery optimization"
- Allow background activity

**4. Use Tmux (For Long Jobs):**
```bash
# Install tmux
pkg install tmux

# Start tmux session
tmux new -s translation

# Run translator
./zee_translator.py

# Detach: Ctrl+B then D
# Screen bisa di-minimize, proses tetap jalan

# Reattach nanti:
tmux attach -t translation
```

### Troubleshooting Android:

**Problem: "Permission denied" saat ./zee_translator.py**

Solution:
```bash
chmod +x zee_translator.py
# Atau:
python zee_translator.py
```

**Problem: "Cannot access /storage/emulated/0"**

Solution:
```bash
termux-setup-storage
# Klik "Allow" di popup
```

**Problem: "Module not found"**

Solution:
```bash
pip install --force-reinstall -r requirements.txt
```

**Problem: Termux crash saat translate**

Solution:
- Enable Wake Lock
- Disable battery optimization
- Keep phone charging
- Use Safe mode (option 1) untuk stability

---

## ✅ Verification Checklist

Setelah install di platform apapun, cek:

- [ ] Program bisa dijalankan
- [ ] Menu utama muncul dengan baik
- [ ] Bisa browse folder
- [ ] Test translate 1-2 file
- [ ] Output file terbuat dengan benar
- [ ] Colors tampil (optional)

---

## 🎯 Quick Reference

### Linux:
```bash
cd ~/zee-subtitle-translator
./zee_translator.py
```

### Windows:
```cmd
Double-click: run_translator.bat
# Atau:
cd C:\ZeeTranslator
python zee_translator.py
```

### Android:
```bash
cd ~/zee-subtitle-translator
./zee_translator.py
```

---

## 💖 Support Project

Jika tool ini bermanfaat:

**🌍 PayPal (International):**
```
https://paypal.me/zeewank
```

**🇮🇩 Trakteer (Indonesia):**
```
https://trakteer.id/zeewank/tip
```

Every support helps keep this project free! 🙏

---

## 📞 Butuh Bantuan?

- 📖 Baca [README.md](README.md)
- 📚 Lihat [FAQ.md](FAQ.md)

---

**Selamat menggunakan Zee Subtitle Translator! 🎉**
