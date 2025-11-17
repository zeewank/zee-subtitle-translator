# Tutorial Instalasi Lengkap - Semua Platform

Panduan install Zee Subtitle Translator untuk pemula di Linux, Windows, dan Android.

## 📋 Daftar Isi

- [Fitur-Fitur](#fitur-fitur)
- [Instalasi Super Cepat (Satu Baris)](#instalasi-super-cepat-satu-baris)
- [Cara Menggunakan](#cara-menggunakan)
- [Tutorial Lengkap Step by Step](#tutorial-lengkap---step-by-step)
- [Cara Cepat Pakai](#cara-cepat-pakai)
- [Tips Penting](#tips-penting)
- [Troubleshooting](#troubleshooting)
- [Instalasi Manual](#instalasi-manual-alternatif)
- [Uninstall](#uninstall)

---

## Fitur-Fitur

✅ **Banyak pilihan mesin terjemah** - Google Translate gratis atau DeepL API  
✅ **Terjemahkan banyak file sekaligus** - Batch processing untuk efisiensi  
✅ **Browser interaktif** - Pilih file dengan mudah  
✅ **Pembersihan teks otomatis** - Hapus tag [MUSIC], (SOUND), dll  
✅ **Tambah kredit nama Anda** - Di awal subtitle hasil terjemahan  
✅ **Progress bar** - Pantau proses terjemahan secara real-time  
✅ **Support banyak format** - SRT, VTT, dan ASS  
✅ **Deteksi encoding otomatis** - Tidak perlu repot setting manual  
✅ **Deteksi nama** - Nama orang tidak diterjemahkan  
✅ **3 mode kecepatan** - Aman, Standar, atau Agresif  
✅ **Bilingual UI** - Menu dalam bahasa Inggris atau Indonesia  

---

## ⚡ INSTALASI SUPER CEPAT (SATU BARIS)

**Tidak perlu download manual! Tidak perlu install git!**  
Cukup copy-paste satu baris perintah, selesai!

### 🐧 LINUX (Ubuntu/Debian/Arch/Fedora)

Buka Terminal (tekan `Ctrl + Alt + T`) lalu paste perintah ini:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

**Atau** kalau pakai `wget`:

```bash
wget -qO- https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash
```

**Itu saja!** Tunggu 2-5 menit sampai selesai.

---

### 🪟 WINDOWS 10/11

**Cara 1: Pakai PowerShell (Recommended)**

1. Klik kanan tombol **Start**
2. Pilih **Windows PowerShell**
3. Paste perintah ini:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat" -OutFile "$env:TEMP\zee-install.bat"; & "$env:TEMP\zee-install.bat"
```

**Cara 2: Pakai Command Prompt**

1. Tekan `Win + R`
2. Ketik `cmd` lalu Enter
3. Paste perintah ini:

```cmd
curl -o "%TEMP%\zee-install.bat" https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat && "%TEMP%\zee-install.bat"
```

**Itu saja!** Tunggu 2-5 menit sampai selesai.

---

### 📱 ANDROID (Termux)

**⚠️ PENTING:** Install Termux dari **F-Droid** atau **GitHub**, **BUKAN** dari Google Play Store!

**Download Termux:**
- **F-Droid:** https://f-droid.org/packages/com.termux/
atau
- **GitHub:** https://github.com/termux/termux-app/releases

**Setelah install Termux:**

1. Buka aplikasi **Termux**
2. Paste perintah ini:

```bash
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

3. Kalau muncul popup **"Allow Termux to access storage"**, klik **Allow**

**Itu saja!** Tunggu 3-5 menit sampai selesai.

---

## 🎉 Apa Yang Terjadi Saat Instalasi?

Installer otomatis akan melakukan:

1. ✅ **Cek Python** - Install kalau belum ada (Windows otomatis)
2. ✅ **Download project** - Langsung dari GitHub (tidak perlu git!)
3. ✅ **Extract semua file** - Otomatis unzip
4. ✅ **Install dependencies** - Semua library Python
5. ✅ **Setup command global** - Bisa jalankan dari mana saja dengan `zeetranslator`
6. ✅ **Buat shortcut** - (Khusus Android: downloads, movies, dcim)
7. ✅ **Buat widget Termux** - (Khusus Android)

**Total waktu:** 2-5 menit tergantung kecepatan internet Anda.

**Tidak butuh git!** Semua serba otomatis.

---

## 🚀 Cara Menggunakan

Setelah instalasi selesai:

### Langkah 1: Aktifkan Command

**Linux / Android:**
```bash
source ~/.bashrc
```

**macOS:**
```bash
source ~/.zshrc
```

**Windows:**
- Tutup PowerShell/Command Prompt
- Buka lagi baru

**Atau lebih mudah:** Buka terminal/command prompt **baru**.

---

### Langkah 2: Jalankan Program

Ketik perintah ini:

```bash
zeetranslator
```

Tekan **Enter**.

**Harus muncul menu seperti ini:**

```
╔═══════════════════════════════════════════╗
║        ZEE SUBTITLE TRANSLATOR v1         ║
╚═══════════════════════════════════════════╝

Selamat datang!
------------------------------------------------------------
1. Terjemahkan Subtitle
2. Pengaturan Bahasa UI
3. Keluar
------------------------------------------------------------
Pilihan [1-3]:
```

**✅ Selesai! Sudah bisa dipakai!**

---

## 📖 Tutorial Lengkap - Step by Step

### Contoh Kasus: Menerjemahkan Subtitle Film

Mari kita terjemahkan subtitle film dari bahasa Inggris ke Indonesia.

#### **Langkah 1: Jalankan Program**

```bash
zeetranslator
```

---

#### **Langkah 2: Pilih Menu Terjemahkan**

```
Pilihan [1-3]: 1
```

Ketik **1** lalu tekan **Enter**.

---

#### **Langkah 3: Pilih Mesin Terjemah**

```
🤖 Pilih mesin terjemah:
  1. Google Translate (gratis, deteksi otomatis)
  2. DeepL API (butuh API key)
Pilihan [1-2]: 1
```

Ketik **1** (Google Translate - gratis) lalu **Enter**.

---

#### **Langkah 4: Pilih Sumber Subtitle**

```
📂 Pilih sumber subtitle:
  1. Jelajahi folder / file .zip
  2. Folder saat ini
  3. Pilih multiple folder
Pilihan [1-3]: 1
```

Ketik **1** lalu **Enter**.

---

#### **Langkah 5: Cari Folder Subtitle Anda**

Program akan menampilkan daftar folder:

```
Lokasi saat ini: /home/user

📂 Daftar folder:
  1) Documents/
  2) Downloads/
  3) Movies/
  4) Videos/
  5) .. (naik ke folder parent)
```

- Ketik **nomor folder** untuk masuk ke folder tersebut
- Tekan **Enter** kalau sudah ketemu file subtitle

**Contoh:** Ketik `3` untuk masuk ke folder Movies.

---

#### **Langkah 6: Cari di Sub-folder?**

```
🔍 Cari di sub-folder juga? (y/n): n
```

- Ketik **n** kalau subtitle ada di folder itu saja
- Ketik **y** kalau subtitle ada di sub-folder

---

#### **Langkah 7: Pilih File yang Mau Diterjemahkan**

```
📋 Ditemukan 5 file:
  1. episode01.srt
  2. episode02.srt
  3. episode03.srt
  4. episode04.srt
  5. episode05.srt

Pilih file:
  0. [PROSES SEMUA]
  (misal: 1, 3, 5) atau rentang (misal: 1-10):
>
```

**Pilihan:**
- Ketik **0** → Proses semua file
- Ketik **1,3,5** → Proses file nomor 1, 3, dan 5
- Ketik **1-10** → Proses file 1 sampai 10

---

#### **Langkah 8: Pilih Lokasi Output**

```
📂 Pilih lokasi output:
  1. Buat sub-folder baru (Anda bisa menamainya)
  2. Folder yang sama dengan file asli
Pilihan [1-2] (default 1):
```

**Ketik 1** lalu beri nama folder:

```
Masukkan nama folder output (default: hasil_terjemahan): Terjemahan
```

Ketik **Terjemahan** (atau nama lain yang Anda mau).

---

#### **Langkah 9: Pilih Kecepatan Proses**

```
⚙️ Pilih 'Mesin Proses' (Kecepatan):
  1. Aman (Lambat)
     ↳ Menerjemahkan baris per baris. Paling stabil.
  2. Standar (Cepat / Direkomendasikan)
     ↳ Menerjemahkan per 50 baris (Batch). Keseimbangan terbaik.
  3. Agresif (Sangat Cepat)
     ↳ Menerjemahkan per 100 baris (Batch). Mungkin diblokir API.
Pilihan [1-3] (default 2): 2
```

**Ketik 2** (Standar - Recommended) lalu **Enter**.

---

#### **Langkah 10: Pilih Bahasa Target**

```
🎯 Bahasa target (default: id): id
```

- Tekan **Enter** untuk bahasa Indonesia (`id`)
- Atau ketik kode bahasa lain (misal: `es` untuk Spanyol)

---

#### **Langkah 11: Tambah Kredit atau Tidak**

```
🎬 Tambahkan kredit pembuat di awal subtitle? (y/n default y): y
```

- Ketik **y** untuk menambahkan nama Anda di awal subtitle
- Ketik **n** untuk tidak menambahkan

---

#### **Langkah 12: Konfirmasi dan Mulai**

Program akan menampilkan ringkasan:

```
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
    RINGKASAN KONFIRMASI
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
  Sumber      : Movies
  Engine      : google
  Kecepatan   : Cepat (Batch)
  Target      : id
  File        : Memproses 5 file
  Output      : /home/user/Movies/Terjemahan
  Pembersihan : Selalu Aktif
  Kredit      : ✅ Ya
============================================================

Mulai proses? (y/n): y
```

**Ketik y** lalu **Enter** untuk mulai!

---

#### **Langkah 13: Lihat Progress**

Program akan menampilkan progress real-time:

```
🚀 Memulai terjemahan...
============================================================

📄 Memproses file 1/5: episode01.srt
episode01.srt: |████████████████████| 9/9 batches
✅ Disimpan: episode01.id.srt

📄 Memproses file 2/5: episode02.srt
episode02.srt: |████████████████████| 9/9 batches
✅ Disimpan: episode02.id.srt

...
```

---

#### **Langkah 14: Selesai!**

Setelah semua file selesai:

```
============================================================
    RINGKASAN PROSES
============================================================
✅ 5 file berhasil
⚠️ 0 dilewati
❌ 0 gagal
ℹ️ Total durasi: 3 menit 24 detik
============================================================
```

**File hasil terjemahan ada di:** `/home/user/Movies/Terjemahan/`

---

## 🎯 Cara Cepat Pakai

### Terjemahkan Satu Film

```bash
cd ~/Videos/MyMovie
zeetranslator
```

Pilih folder saat ini → Pilih semua file → Terjemahkan → Selesai!

---

### Terjemahkan Serial TV (Satu Season)

```bash
zeetranslator ~/Series/BreakingBad/Season1/
```

Semua episode langsung diterjemahkan sekaligus dalam satu proses.

---

### Terjemahkan Beberapa Season Sekaligus

```bash
zeetranslator
```

1. Pilih: **Multiple folders** (menu 3)
2. Browse ke **Season 1**, ketik `s1` (select)
3. Browse ke **Season 2**, ketik `s2` (select)
4. Browse ke **Season 3**, ketik `s3` (select)
5. Ketik `0` (selesai pilih)
6. Pilih **"Keep structure"**
7. Mulai!

Setiap season dapat hasil terjemahan di folder masing-masing.

---

### Terjemahkan File ZIP

```bash
zeetranslator ~/Downloads/subtitles.zip
```

Program otomatis extract ZIP dan terjemahkan semua subtitle di dalamnya.

---

## 💡 Tips Penting

### Mode Kecepatan

| Mode | Kecepatan | Waktu per File | Kapan Pakai |
|------|-----------|----------------|-------------|
| **Aman** | Lambat | ~2-3 menit | File penting, format kompleks |
| **Standar** ⭐ | Cepat | ~1-2 menit | **Direkomendasikan untuk semua** |
| **Agresif** | Sangat Cepat | ~30-45 detik | Batch besar, koneksi stabil |

**Rekomendasi:** Mulai dengan **Standar**. Kalau gagal, pakai **Aman**.

---

### Kode Bahasa Target

Bahasa yang sering dipakai:

| Kode | Bahasa |
|------|--------|
| `id` | Indonesia |
| `en` | Inggris |
| `es` | Spanyol |
| `fr` | Perancis |
| `de` | Jerman |
| `it` | Italia |
| `pt` | Portugis |
| `ru` | Rusia |
| `ja` | Jepang |
| `ko` | Korea |
| `zh-CN` | Mandarin (Simplified) |
| `ar` | Arab |
| `th` | Thailand |
| `vi` | Vietnam |

---

### Cara Pilih File

- **0** → Proses semua file
- **1,3,5** → Proses file nomor 1, 3, dan 5
- **1-10** → Proses file 1 sampai 10
- **1-5,8,12-15** → Kombinasi (file 1-5, 8, dan 12-15)

---

### Navigasi Folder (Multiple Folder Selection)

| Perintah | Fungsi |
|----------|--------|
| `14` | Buka folder nomor 14 |
| `s14` | Pilih folder 14 tanpa membuka |
| `u1` | Hapus folder 1 dari pilihan |
| `.` | Pilih folder saat ini |
| `0` | Selesai pilih, mulai proses |
| `q` | Batal dan kembali ke menu |

---

## 🔧 Troubleshooting

### Command Not Found

**Problem:** Ketik `zeetranslator` tapi muncul error "command not found"

**Solusi:**

**Linux / Android:**
```bash
source ~/.bashrc
```

**macOS:**
```bash
source ~/.zshrc
```

**Windows:**
Tutup dan buka ulang Command Prompt / PowerShell.

**Atau pakai cara tradisional:**
```bash
cd ~/zee-subtitle-translator
python zee_translator.py
```

---

### Instalasi Gagal

**Problem:** Installer error atau stuck

**Solusi:**

**Linux:**
```bash
# Coba pakai wget:
wget -qO- https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh | bash

# Atau download manual:
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh
chmod +x installer.sh
./installer.sh
```

**Windows:**
1. Download [install_windows.bat](https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat)
2. Klik kanan → **Run as Administrator**

**Android:**
```bash
# Update Termux dulu:
pkg update -y && pkg upgrade -y

# Install dependencies:
pkg install -y python curl unzip

# Coba lagi:
curl -sSL https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh | bash
```

---

### Terjemahan Lambat

**Problem:** Proses terjemahan sangat lama

**Solusi:**
- ✅ Pakai **WiFi**, bukan data seluler
- ✅ Coba mode **Aman** (lebih stabil)
- ✅ Terjemahkan pas **jam sepi** (malam hari)
- ✅ Cek **kecepatan internet**
- ✅ Proses file lebih **sedikit** per batch

---

### Permission Denied

**Problem:** Error "Permission denied"

**Solusi:**

**Linux / Android:**
```bash
chmod +x zee_translator.py
```

**Windows:**
Jalankan Command Prompt sebagai **Administrator** (klik kanan → Run as Administrator).

---

### Dependencies Hilang

**Problem:** Error "Module not found"

**Solusi:**
```bash
cd ~/zee-subtitle-translator
pip install --force-reinstall -r requirements.txt
```

---

## 📦 Instalasi Manual (Alternatif)

Kalau instalasi one-liner tidak jalan, bisa pakai cara manual:

### Linux

```bash
# 1. Download bootstrap script
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/installer.sh

# 2. Beri izin eksekusi
chmod +x installer.sh

# 3. Jalankan
./installer.sh
```

### Windows

```cmd
REM 1. Download bootstrap script
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/install_windows.bat

REM 2. Jalankan (double-click atau ketik)
install_windows.bat
```

### Android

```bash
# 1. Download bootstrap script
curl -O https://raw.githubusercontent.com/zeewank/zee-subtitle-translator/main/setup_termux.sh

# 2. Beri izin eksekusi
chmod +x setup_termux.sh

# 3. Jalankan
./setup_termux.sh
```

---

## 🗑️ Uninstall

Untuk menghapus Zee Subtitle Translator:

### Linux / Android

```bash
cd ~/zee-subtitle-translator
./uninstall.sh
```

### Windows

```cmd
cd %USERPROFILE%\zee-subtitle-translator
uninstall.bat
```

**Uninstaller akan:**
- ✅ Hapus command global `zeetranslator`
- ✅ Hapus alias dari shell config
- ✅ Hapus widget Termux (kalau ada)
- ✅ Hapus file konfigurasi
- ✅ Buat backup shell config

**Note:** Untuk juga hapus folder project:

```bash
# Linux / Android
rm -rf ~/zee-subtitle-translator

# Windows
rmdir /s "%USERPROFILE%\zee-subtitle-translator"
```

---

## 📚 Dokumentasi Lainnya

- [README.md](README.md) - Panduan umum (Bahasa Inggris)
- [QUICKSTART.md](QUICKSTART.md) - Quick start 5 menit (Bahasa Inggris)
- [GUIDE.md](GUIDE.md) - Panduan lengkap fitur (Bahasa Inggris)
- [FAQ.md](FAQ.md) - Pertanyaan umum (Bahasa Inggris)
- [ANDROID_STORAGE_GUIDE.md](ANDROID_STORAGE_GUIDE.md) - Penjelasan storage Android

---

## 💻 Catatan Platform

### Linux
- ✅ Tested di Ubuntu, Debian, Arch, Fedora
- ✅ Butuh `curl` atau `wget` dan `unzip`
- ✅ Command global jalan di bash dan zsh

### Windows
- ✅ Windows 10/11 recommended
- ✅ PowerShell lebih bagus dari Command Prompt
- ✅ Python otomatis install kalau belum ada

### Android (Termux)
- ⚠️ **Harus pakai F-Droid atau GitHub version**
- ❌ **Jangan pakai Google Play Store** (broken)
- ✅ Install ke Shared Storage biar bisa diakses file manager
- ✅ Widget support untuk quick launch
- ✅ Storage shortcuts otomatis dibuat

---

## 💖 Support Project

Kalau tool ini bermanfaat untuk Anda:

**PayPal (International):**
```
https://paypal.me/zeewank
```

**Trakteer (Indonesia):**
```
https://trakteer.id/zeewank/tip
```

Setiap dukungan sangat membantu pengembangan project ini. Terima kasih! 🙏

---

## 🆘 Butuh Bantuan?

- [GitHub Issues](https://github.com/zeewank/zee-subtitle-translator/issues) - Report bug
- [GitHub Discussions](https://github.com/zeewank/zee-subtitle-translator/discussions) - Tanya jawab
- [FAQ.md](FAQ.md) - Pertanyaan umum

---

**Selamat menggunakan Zee Subtitle Translator! 🎬**

**Dibuat oleh Zee dengan ❤️**
