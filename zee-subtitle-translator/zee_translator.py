#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zee Subtitle Translator v1
A powerful batch subtitle translator with multi-format support

Author: Zee
License: MIT
Repository: https://github.com/yourusername/zee-subtitle-translator
"""

import os
import re
import sys
import time
import glob
import argparse
import traceback
import zipfile
import tempfile
from datetime import timedelta, datetime
from pathlib import Path
from typing import List, Tuple, Optional, Union

CONFIG_FILE = Path.home() / ".subtitletrans.conf"
LANG_UI = "EN"

if CONFIG_FILE.exists():
    try:
        content = CONFIG_FILE.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("LANG_UI="):
                LANG_UI = line.strip().split("=", 1)[1].upper()
                break
    except Exception:
        pass

# Helper for bilingual text
def _(id_text: str, en_text: str) -> str:
    """Return text based on selected UI language"""
    global LANG_UI
    return en_text if LANG_UI == "EN" else id_text


# ANSI color codes for terminal output
class Colors:
    """Terminal color codes"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_GREEN = '\033[102m\033[30m'
    BG_YELLOW = '\033[103m\033[30m'
    BG_BLUE = '\033[104m\033[97m'
    BG_MAGENTA = '\033[105m\033[97m'


def c(text: str, color: str) -> str:
    """Apply color to text"""
    return f"{color}{text}{Colors.RESET}"

# Check required dependencies
try:
    import srt
    from deep_translator import GoogleTranslator, DeeplTranslator
    from tqdm import tqdm
    import chardet
    import pysubs2
except ImportError as e:
    print(_("Beberapa dependensi Python belum terpasang!",
            "Some Python dependencies are missing!"))
    print("Run: pip install srt deep-translator tqdm chardet pysubs2")
    print(f"Error: {e}")
    sys.exit(1)

try:
    import readline
except ImportError:
    pass  # Readline is optional, only for better input UX


class ProcessStats:
    """Track translation statistics"""
    
    def __init__(self):
        self.success_count = 0
        self.skipped_count = 0
        self.failed_count = 0
        self.start_time = None
        self.end_time = None
    
    def start(self):
        """Mark start time"""
        self.start_time = datetime.now()
    
    def stop(self):
        """Mark end time"""
        self.end_time = datetime.now()
    
    def get_duration(self) -> str:
        """Calculate and format duration"""
        if not self.start_time or not self.end_time:
            return "0 " + _('detik', 'seconds')
        
        delta = self.end_time - self.start_time
        total_seconds = int(delta.total_seconds())
        
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        parts = []
        if hours > 0:
            parts.append(f"{hours} {_('jam', 'hours')}")
        if minutes > 0:
            parts.append(f"{minutes} {_('menit', 'minutes')}")
        if seconds > 0 or not parts:
            parts.append(f"{seconds} {_('detik', 'seconds')}")
        
        return " ".join(parts)
    
    def print_summary(self):
        duration_str = self.get_duration()
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        print("\n" + "=" * 70)
        print(c(f"{timestamp} [🚀] --- {_('RINGKASAN PROSES', 'PROCESS SUMMARY')} ---", Colors.BOLD + Colors.CYAN))
        print(c(f"✅ {self.success_count} {_('file berhasil', 'files succeeded')}", Colors.GREEN))
        print(c(f"⚠️ {self.skipped_count} {_('dilewati', 'skipped')}", Colors.YELLOW))
        print(c(f"❌ {self.failed_count} {_('gagal', 'failed')}", Colors.RED))
        print(c(f"ℹ️ Total durasi: {duration_str}", Colors.CYAN))
        print(c(f"{timestamp} [ℹ️] {_('Ringkasan', 'Summary')}: {self.success_count} {_('Sukses', 'Success')}, {self.skipped_count} {_('Lewati', 'Skip')}, {self.failed_count} {_('Gagal', 'Fail')}. {_('Durasi', 'Duration')}: {duration_str}", Colors.BOLD + Colors.MAGENTA))
        print("=" * 70)

# ===============================================================
# DETEKSI ENCODING CERDAS
# ===============================================================
def detect_encoding(file_path: Path) -> str:
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read(5000)
            result = chardet.detect(raw_data)
            encoding = result.get('encoding', 'utf-8')
            if result.get('confidence', 0) < 0.7:
                return 'utf-8'
            return encoding if encoding else 'utf-8'
    except Exception:
        return 'utf-8'

def read_file_with_detection(file_path: Path) -> str:
    encoding = detect_encoding(file_path)
    try:
        return file_path.read_text(encoding=encoding, errors='ignore')
    except Exception:
        return file_path.read_text(encoding='latin-1', errors='ignore')

# ===============================================================
# FUNGSI PEMBERSIHAN TEKS (FIXED - More Aggressive)
# ===============================================================
def remove_bracketed(text: str) -> str:
    if not text:
        return text
    s = text
    pattern = r'[\(\[\{<][^\)\]\}>]*[\)\]\}>]'
    while re.search(pattern, s):
        s = re.sub(pattern, ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def looks_like_name(s: str) -> bool:
    if not s or ' ' in s:
        return False
    if re.search(r'[\d]', s):
        return False
    if re.match(r"^[A-Z][a-z]+(?:[-'][A-Za-z]+)?$", s):
        return True
    if re.match(r"^[A-Z]{2,}$", s):
        return True
    return False

# ===============================================================
# FUNGSI TAMBAHAN UNTUK KREDIT
# ===============================================================
def add_credit_to_srt(subs: list, add_credit: bool) -> list:
    if not add_credit:
        return subs
    
    credit_cue = srt.Subtitle(
        index=1,
        start=timedelta(seconds=2),
        end=timedelta(seconds=7),
        content="Subtitle by Z33"
    )
    
    for sub in subs:
        sub.index += 1
    
    return [credit_cue] + subs

def add_credit_to_ass_vtt(subs, add_credit: bool):
    if not add_credit:
        return subs
    
    credit_event = pysubs2.SSAEvent()
    credit_event.start = pysubs2.make_time(s=2)
    credit_event.end = pysubs2.make_time(s=7)
    credit_event.text = "Subtitle by Z33"
    
    subs.events.insert(0, credit_event)
    
    return subs

# ===============================================================
# TRANSLATOR WRAPPERS (SLOW & FAST)
# ===============================================================

# 1. Wrapper "SLOW" (Line-by-Line)
class LineTranslatorWrapper:
    def __init__(self, engine: str, target: str):
        self.engine = engine.lower()
        self.target = target
        self.max_retries = 3
        print(f"[Mode: {_('Aman (Baris per Baris)', 'Safe (Line-by-Line)')}]")
        
    def translate(self, text: str, desc: str = "") -> str:
        txt = (text or "").strip()
        if not txt: return txt
        last_exc = None
        for attempt in range(self.max_retries):
            try:
                if self.engine == "deepl":
                    key = os.getenv("DEEPL_API_KEY", "")
                    if not key: raise RuntimeError("DEEPL_API_KEY not found.")
                    return DeeplTranslator(api_key=key, target=self.target, source="auto").translate(txt)
                else:
                    return GoogleTranslator(source="auto", target=self.target).translate(txt)
            except Exception as e:
                last_exc = e
                if desc:
                    print(_(f"⚠️ Gagal '{desc[:30]}...', mencoba lagi ({attempt + 1})",
                           f"⚠️ Fail '{desc[:30]}...', retry ({attempt + 1})"))
                time.sleep(1)
        print(_(f"❌ Gagal permanen: {txt[:50]}", f"❌ Permanent fail: {txt[:50]}"))
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[TRANSLATE_FAIL] engine={self.engine} text={txt[:120]} err={repr(last_exc)}\n")
        return txt

# 2. Wrapper "FAST" (Batch) - ANTI-STUCK VERSION
class BatchTranslatorWrapper:
    def __init__(self, engine: str, target: str, sleep_time: float = 0.5):
        self.engine = engine.lower()
        self.target = target
        self.sleep_time = sleep_time
        self.max_retries = 3
        print(f"[Mode: {_('Cepat (Batch)', 'Fast (Batch)')}]")
        try:
            if self.engine == "deepl":
                key = os.getenv("DEEPL_API_KEY", "")
                if not key: raise RuntimeError("DEEPL_API_KEY not found.")
                self.translator = DeeplTranslator(api_key=key, target=self.target, source="auto")
            else:
                self.translator = GoogleTranslator(source="auto", target=self.target)
        except Exception as e:
            print(_(f"❌ Gagal inisialisasi {engine} translator: {e}", f"❌ Failed to init {engine} translator: {e}"))
            sys.exit(1)

    def translate_batch(self, texts: List[str]) -> List[str]:
        if not texts: return []
        for attempt in range(self.max_retries):
            try:
                translated_texts = self.translator.translate_batch(texts)
                if translated_texts is None:
                    raise Exception("API returned None (likely rate-limit)")
                if len(translated_texts) != len(texts):
                    print(f"⚠️ {_('Peringatan: Jumlah batch tidak cocok!', 'Warning: Batch mismatch!')}")
                    return texts
                return translated_texts
            except Exception as e:
                print(_(f"\n⚠️ Gagal batch, mencoba lagi ({attempt+1})... Error: {e}",
                       f"\n⚠️ Batch failed, retrying ({attempt+1})... Error: {e}"))
                time.sleep(1 * (attempt + 1))
        print(_("❌ Gagal batch permanen. Menggunakan teks asli.", 
               "❌ Permanent batch fail. Using original text."))
        return texts

# ===============================================================
# BROWSER & PEMILIHAN FOLDER MULTIPLE
# ===============================================================
def browse_folders_multiple(start: Path) -> List[Path]:
    """Memilih multiple folder dengan opsi Buka/Pilih"""
    selected_folders = []
    cur = start
    
    while True:
        print(f"\n{c(_('Lokasi saat ini:', 'Current folder:'), Colors.CYAN)} {c(str(cur), Colors.YELLOW)}")
        print(f"{c(_('Folder terpilih:', 'Selected folders:'), Colors.CYAN)} {c(str(len(selected_folders)), Colors.GREEN)}")
        
        if selected_folders:
            print(c(_("\n📌 Folder yang sudah dipilih:", "\n📌 Selected folders:"), Colors.MAGENTA))
            for i, folder in enumerate(selected_folders, 1):
                print(f"  {c(f'[{i}]', Colors.GREEN)} {c(str(folder), Colors.YELLOW)}")
        
        items = []
        try:
            dirs = sorted([p for p in cur.iterdir() if p.is_dir()], key=lambda p: p.name.lower())
            items = dirs
        except PermissionError:
            print(c(_("Izin ditolak.", "Permission denied."), Colors.RED))
            cur = cur.parent
            continue
        
        print(c(_("\n📂 Daftar folder:", "\n📂 Folder list:"), Colors.BLUE))
        for i, p in enumerate(items, 1):
            marker = c(" ✓", Colors.GREEN) if p in selected_folders else ""
            print(f"  {i}) {p.name}/{marker}")
        print(f"  {len(items)+1}) .. {_('(naik ke folder parent)', '(go to parent folder)')}")
        
        print(c(_("\n⚙️ Perintah:", "\n⚙️ Commands:"), Colors.CYAN))
        print(_("  • Ketik nomor lalu tekan ENTER untuk BUKA folder", 
               "  • Type number then ENTER to OPEN folder"))
        print(c(_("  • Ketik 's' + nomor (misal: s14) untuk PILIH folder tanpa membuka",
               "  • Type 's' + number (e.g., s14) to SELECT folder without opening"), Colors.GREEN))
        print(c(_("  • Ketik 'u' + nomor (misal: u1) untuk HAPUS folder dari pilihan",
               "  • Type 'u' + number (e.g., u1) to UNSELECT folder from selection"), Colors.RED))
        print(c(_("  • Ketik '.' (titik) untuk PILIH folder saat ini",
               "  • Type '.' (dot) to SELECT current folder"), Colors.YELLOW))
        print(c(_("  • Ketik '0' untuk SELESAI dan lanjut proses",
               "  • Type '0' to FINISH and continue"), Colors.MAGENTA))
        print(c(_("  • Ketik 'q' atau 'x' untuk BATAL dan kembali ke menu",
               "  • Type 'q' or 'x' to CANCEL and return to menu"), Colors.RED))
        
        prompt = c(_("\nPilihan Anda: ", "\nYour choice: "), Colors.CYAN)
        choice = input(prompt).strip().lower()
        
        if choice == "0":
            if selected_folders:
                return selected_folders
            else:
                print(c(_("⚠️ Belum ada folder dipilih!", "⚠️ No folders selected!"), Colors.YELLOW))
                continue
        
        if choice in ('q', 'x', 'exit', 'quit', 'back'): 
            print(c(_("↩️ Kembali ke menu utama...", "↩️ Returning to main menu..."), Colors.YELLOW))
            return []
        
        if choice == ".":
            if cur in selected_folders:
                selected_folders.remove(cur)
                print(c(f"➖ {_('Dihapus dari pilihan:', 'Removed from selection:')} {cur.name}", Colors.RED))
            else:
                selected_folders.append(cur)
                print(c(f"➕ {_('Ditambahkan ke pilihan:', 'Added to selection:')} {cur.name}", Colors.GREEN))
            continue
        
        if choice.startswith("s") and choice[1:].isdigit():
            idx = int(choice[1:])
            if 1 <= idx <= len(items):
                selected_path = items[idx - 1]
                if selected_path in selected_folders:
                    selected_folders.remove(selected_path)
                    print(c(f"➖ {_('Dihapus dari pilihan:', 'Removed from selection:')} {selected_path.name}", Colors.RED))
                else:
                    selected_folders.append(selected_path)
                    print(c(f"➕ {_('Ditambahkan ke pilihan:', 'Added to selection:')} {selected_path.name}", Colors.GREEN))
            else:
                print(c(_("❌ Nomor tidak valid!", "❌ Invalid number!"), Colors.RED))
            continue
        
        if choice.startswith("u") and choice[1:].isdigit():
            idx = int(choice[1:])
            if 1 <= idx <= len(selected_folders):
                removed = selected_folders.pop(idx - 1)
                print(c(f"➖ {_('Dihapus dari pilihan:', 'Removed from selection:')} {removed.name}", Colors.RED))
            else:
                print(c(_("❌ Nomor tidak valid!", "❌ Invalid number!"), Colors.RED))
            continue
        
        if choice.isdigit():
            idx = int(choice)
            if idx == len(items) + 1:
                cur = cur.parent
            elif 1 <= idx <= len(items):
                cur = items[idx - 1]
            else:
                print(c(_("❌ Nomor tidak valid!", "❌ Invalid number!"), Colors.RED))
            continue
        
        print(c(_("❌ Perintah tidak dikenali!", "❌ Unrecognized command!"), Colors.RED))

def browse_item_interactive(start: Path) -> Path:
    cur = start
    while True:
        print(f"\n{_('Lokasi saat ini:', 'Current folder:')} {cur}")
        items = []
        try:
            dirs = sorted([p for p in cur.iterdir() if p.is_dir()], key=lambda p: p.name.lower())
            files = sorted([p for p in cur.iterdir() if p.is_file() and p.suffix.lower() == '.zip'], key=lambda p: p.name.lower())
            items = dirs + files
        except PermissionError:
            print(_("Izin ditolak.", "Permission denied."))
            cur = cur.parent
            continue
        
        for i, p in enumerate(items, 1):
            print(f"  {i}) {p.name}{'/' if p.is_dir() else ''}")
        print(f"  {len(items)+1}) .. (parent folder)")
        
        prompt = _("Ketik nomor (folder/zip) atau Enter untuk pilih folder ini: ",
                   "Type number (folder/zip) or Enter to choose this folder: ")
        choice = input(prompt).strip()
        
        if choice == "": return cur
        if choice.lower() == "q": return start
        if not choice.isdigit(): continue
            
        idx = int(choice)
        if idx == len(items) + 1:
            cur = cur.parent
        elif 1 <= idx <= len(items):
            selected_path = items[idx - 1]
            if selected_path.is_dir(): cur = selected_path
            else: return selected_path

def check_overwrite(file_path: Path, overwrite_mode: str) -> Tuple[bool, str]:
    if overwrite_mode == 'always':
        return True, 'always'
    if not file_path.exists():
        return True, overwrite_mode
    if overwrite_mode == 'ask':
        response = input(_(f"File {file_path.name} sudah ada. Timpa? (y/n/a=timpa semua): ",
                         f"File {file_path.name} already exists. Overwrite? (y/n/a=overwrite all): ")).strip().lower()
        if response == 'a': return True, 'always'
        if response in ('y', 'yes'): return True, 'ask'
    return False, 'skip'

def select_files_interactive(files: List[Path], title: str) -> List[Path]:
    print(f"\n📋 {title}:")
    for i, file_path in enumerate(files, 1):
        print(f"  {i}. {file_path.name}")
    print("\n" + _("Pilih file:", "Select files:"))
    print("  0. " + _("[PROSES SEMUA]", "[PROCESS ALL]"))
    print(_("  (misal: 1, 3, 5) atau rentang (misal: 1-10):", " (e.g., 1, 3, 5) or range (e.g., 1-10):"))
    choice = input("> ").strip()
    if choice == "0" or not choice: return files
    
    selected_files = []
    try:
        parts = choice.split(',')
        for part in parts:
            part = part.strip()
            if '-' in part:
                start, end = map(int, part.split('-'))
                for i in range(start, end + 1):
                    if 1 <= i <= len(files): selected_files.append(files[i-1])
            else:
                idx = int(part)
                if 1 <= idx <= len(files): selected_files.append(files[idx-1])
    except ValueError:
        return files
    return sorted(list(set(selected_files)), key=files.index)

# ===============================================================
# FUNGSI FILE
# ===============================================================
def safe_makedir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def detect_sub_files(folder: Path, recursive: bool = False) -> List[Path]:
    pattern = "**/*" if recursive else "*"
    extensions = [".srt", ".vtt", ".ass"]
    files = []
    for ext in extensions:
        files.extend(sorted(folder.glob(f"{pattern}{ext}")))
    return files

# ===============================================================
# ESTIMASI WAKTU & MENU
# ===============================================================

def estimate_processing_time(file_count: int, processing_mode: str, batch_size: int) -> str:
    """Memberikan estimasi waktu pengerjaan yang sangat kasar."""
    seconds_per_file = 0
    if processing_mode == "line_by_line":
        seconds_per_file = 150 # ~2-3 menit per file
    else: # mode batch
        if batch_size == 100: # Agresif
            seconds_per_file = 30 # ~30 detik/file
        else: # Standar (50)
            seconds_per_file = 45 # ~45 detik/file
    
    total_seconds = seconds_per_file * file_count
    
    if total_seconds < 60:
        return f"~{total_seconds} {_('detik', 'seconds')}"
    if total_seconds < 120:
        return _("~1-2 menit", "~1-2 minutes")
    
    minutes = (total_seconds // 60)
    if minutes < 60:
        return f"~{minutes} {_('menit', 'minutes')}"
    else:
        hours = total_seconds / 3600
        return f"~{hours:.1f} {_('jam', 'hours')}"

def get_processing_speed() -> Tuple[str, int, float]:
    """Minta pengguna memilih kecepatan proses."""
    print(_("\n⚙️ Pilih 'Mesin Proses' (Kecepatan):", "\n⚙️ Choose 'Processing Engine' (Speed):"))
    print("  1. " + _("Aman (Lambat)", "Safe (Slow)"))
    print("     " + _("↳ Menerjemahkan baris per baris. Paling stabil.", 
                    "↳ Translates line-by-line. Most stable."))
    print("  2. " + _("Standar (Cepat / Direkomendasikan)", "Standard (Fast / Recommended)"))
    print("     " + _("↳ Menerjemahkan per 50 baris (Batch). Keseimbangan terbaik.", 
                    "↳ Translates 50 lines at a time (Batch). Best balance."))
    print("  3. " + _("Agresif (Sangat Cepat)", "Aggressive (Very Fast)"))
    print("     " + _("↳ Menerjemahkan per 100 baris (Batch). Mungkin diblokir API.", 
                    "↳ Translates 100 lines at a time (Batch). May get API blocked."))
    
    choice = input(_("Pilihan [1-3] (default 2): ", "Choice [1-3] (default 2): ")).strip() or "2"
    
    if choice == "1":
        return "line_by_line", 1, 0.1
    elif choice == "3":
        return "batch", 100, 0.5
    else:
        return "batch", 50, 0.5

def get_output_location(default_folder: Path) -> Tuple[Path, str]:
    """Dapatkan lokasi output dengan nama kustom."""
    print(_("\n📁 Pilih lokasi output:", "\n📁 Choose output location:"))
    print("  1. " + _("Buat sub-folder baru (Anda bisa menamainya)", "Create a new sub-folder (You can name it)"))
    print("  2. " + _("Folder yang sama dengan file asli", "Same folder as original files"))
    
    choice = input(_("Pilihan [1-2] (default 1): ", "Choice [1-2] (default 1): ")).strip() or "1"
    
    if choice == "2":
        return default_folder, "same"
    else:
        default_name = _("hasil_terjemahan", "translated_output")
        folder_name = input(_(f"\nMasukkan nama folder output (default: {default_name}): ", 
                            f"\nEnter output folder name (default: {default_name}): ")).strip()
        if not folder_name:
            folder_name = default_name
        
        return default_folder / folder_name, "subfolder"

def get_credit_option() -> bool:
    """Minta pengguna memilih apakah ingin menambahkan kredit."""
    choice = input(_("\n🎬 Tambahkan kredit pembuat di awal subtitle? (y/n default y): ",
                     "\n🎬 Add creator credit at the beginning? (y/n default y): ")).strip().lower() or "y"
    return choice == "y"

# ===============================================================
# PROSESOR FILE (Pembersihan Otomatis - FIXED)
# ===============================================================

# --- FUNGSI MODE 'LINE_BY_LINE' (SLOW) ---
def process_srt_file_line(path: Path, translator: LineTranslatorWrapper, 
                    outdir: Path, overwrite_mode: str, add_credit: bool) -> Tuple[str, str]:
    try:
        content = read_file_with_detection(path)
        subs = list(srt.parse(content))
    except Exception as e:
        print(_(f"[ERROR] Gagal membaca {path.name}: {e}", f"[ERROR] Failed to read {path.name}: {e}"))
        return "failed", overwrite_mode
    out_name = f"{path.stem}.{translator.target}.srt"
    out_path = outdir / out_name
    can_write, overwrite_mode = check_overwrite(out_path, overwrite_mode)
    if not can_write:
        print(_(f"⏭️  Lewati {out_path.name}", f"⏭️  Skipped {out_path.name}"))
        return "skipped", 'skip'
    out_subs = []
    iterator = tqdm(subs, desc=path.name, unit="l", bar_format='{l_bar}{bar:30}{r_bar}')
    for cue in iterator:
        text_strip = (cue.content or "").strip()
        text_strip = remove_bracketed(text_strip)
        if not text_strip: continue
        if looks_like_name(text_strip):
            translated = text_strip
        else:
            short_text = text_strip[:30].replace("\n", " ")
            iterator.set_postfix_str(f"\"{short_text}...\"")
            translated = translator.translate(text_strip, desc=short_text)
        cue.content = translated or text_strip
        out_subs.append(cue)
    
    if add_credit:
        out_subs = add_credit_to_srt(out_subs, add_credit)
    
    if out_subs:
        try:
            safe_makedir(outdir)
            out_path.write_text(srt.compose(out_subs), encoding="utf-8")
            print(c(f"✅ {_('Disimpan:', 'Saved:')} {out_path.name}", Colors.GREEN))
            return "success", overwrite_mode
        except Exception as e:
            print(_(f"[ERROR] Gagal menulis {out_path.name}: {e}", f"[ERROR] Failed to write {out_path.name}: {e}"))
    return "failed", overwrite_mode

def process_ass_vtt_file_line(path: Path, translator: LineTranslatorWrapper, 
                        outdir: Path, overwrite_mode: str, add_credit: bool) -> Tuple[str, str]:
    """Fungsi gabungan untuk .ASS dan .VTT (keduanya pakai pysubs2)"""
    try:
        encoding = detect_encoding(path)
        subs = pysubs2.load(str(path), encoding=encoding)
    except Exception as e:
        print(_(f"[ERROR] Gagal membaca {path.name}: {e}", f"[ERROR] Failed to read {path.name}: {e}"))
        return "failed", overwrite_mode
    out_name = f"{path.stem}.{translator.target}{path.suffix}"
    out_path = outdir / out_name
    can_write, overwrite_mode = check_overwrite(out_path, overwrite_mode)
    if not can_write:
        print(_(f"⏭️  Lewati {out_path.name}", f"⏭️  Skipped {out_path.name}"))
        return "skipped", 'skip'

    iterator = tqdm(subs.events, desc=path.name, unit="l", bar_format='{l_bar}{bar:30}{r_bar}')
    for event in iterator:
        text_strip = (event.plaintext or "").strip()
        text_strip = remove_bracketed(text_strip)
        if not text_strip:
            event.text = ""
            continue
        if looks_like_name(text_strip):
            translated = text_strip
        else:
            short_text = text_strip[:30].replace("\n", " ")
            iterator.set_postfix_str(f"\"{short_text}...\"")
            translated = translator.translate(text_strip, desc=short_text)
        event.text = translated or text_strip
    subs.events = [ev for ev in subs.events if ev.text.strip()]
    
    if add_credit:
        subs = add_credit_to_ass_vtt(subs, add_credit)
    
    if subs.events:
        try:
            safe_makedir(outdir)
            subs.save(str(out_path), encoding="utf-8")
            print(c(f"✅ {_('Disimpan:', 'Saved:')} {out_path.name}", Colors.GREEN))
            return "success", overwrite_mode
        except Exception as e:
            print(_(f"[ERROR] Gagal menulis {out_path.name}: {e}", f"[ERROR] Failed to write {out_path.name}: {e}"))
    return "failed", overwrite_mode

# --- FUNGSI MODE 'BATCH' (FAST) ---
def process_srt_file_batch(path: Path, translator: BatchTranslatorWrapper, 
                    outdir: Path, overwrite_mode: str, batch_size: int, add_credit: bool) -> Tuple[str, str]:
    try:
        content = read_file_with_detection(path)
        subs = list(srt.parse(content))
    except Exception as e:
        print(_(f"[ERROR] Gagal membaca {path.name}: {e}", f"[ERROR] Failed to read {path.name}: {e}"))
        return "failed", overwrite_mode
    out_name = f"{path.stem}.{translator.target}.srt"
    out_path = outdir / out_name
    can_write, overwrite_mode = check_overwrite(out_path, overwrite_mode)
    if not can_write:
        print(_(f"⏭️  Lewati {out_path.name}", f"⏭️  Skipped {out_path.name}"))
        return "skipped", 'skip'
    original_texts = []
    indices_to_translate = []
    for i, cue in enumerate(subs):
        text_strip = (cue.content or "").strip()
        text_strip = remove_bracketed(text_strip)
        if text_strip and not looks_like_name(text_strip):
            original_texts.append(text_strip)
            indices_to_translate.append(i)
        else:
            cue.content = text_strip
    translated_texts = []
    iterator = tqdm(range(0, len(original_texts), batch_size), desc=path.name, unit="b", bar_format='{l_bar}{bar:30}{r_bar}')
    for i in iterator:
        batch = original_texts[i:i + batch_size]
        iterator.set_postfix_str(f"{_('menerjemahkan', 'translating')} {len(batch)} {_('baris', 'lines')}")
        translated_batch = translator.translate_batch(batch)
        translated_texts.extend(translated_batch)
        time.sleep(translator.sleep_time)
    for i, translated in zip(indices_to_translate, translated_texts):
        subs[i].content = translated or subs[i].content
    subs = [s for s in subs if s.content.strip()]
    
    if add_credit:
        subs = add_credit_to_srt(subs, add_credit)
    
    if subs:
        try:
            safe_makedir(outdir)
            out_path.write_text(srt.compose(subs), encoding="utf-8")
            print(c(f"✅ {_('Disimpan:', 'Saved:')} {out_path.name}", Colors.GREEN))
            return "success", overwrite_mode
        except Exception as e:
            print(_(f"[ERROR] Gagal menulis {out_path.name}: {e}", f"[ERROR] Failed to write {out_path.name}: {e}"))
    return "failed", overwrite_mode

def process_ass_vtt_file_batch(path: Path, translator: BatchTranslatorWrapper, 
                        outdir: Path, overwrite_mode: str, batch_size: int, add_credit: bool) -> Tuple[str, str]:
    try:
        encoding = detect_encoding(path)
        subs = pysubs2.load(str(path), encoding=encoding)
    except Exception as e:
        print(_(f"[ERROR] Gagal membaca {path.name}: {e}", f"[ERROR] Failed to read {path.name}: {e}"))
        return "failed", overwrite_mode
    out_name = f"{path.stem}.{translator.target}{path.suffix}"
    out_path = outdir / out_name
    can_write, overwrite_mode = check_overwrite(out_path, overwrite_mode)
    if not can_write:
        print(_(f"⏭️  Lewati {out_path.name}", f"⏭️  Skipped {out_path.name}"))
        return "skipped", 'skip'
    original_texts = {}
    lines_to_translate = []
    for event in subs.events:
        text_strip = (event.plaintext or "").strip()
        text_strip = remove_bracketed(text_strip)
        event.text = text_strip
        if text_strip and not looks_like_name(text_strip) and text_strip not in original_texts:
            original_texts[text_strip] = ""
            lines_to_translate.append(text_strip)
    translated_texts = []
    iterator = tqdm(range(0, len(lines_to_translate), batch_size), desc=path.name, unit="b", bar_format='{l_bar}{bar:30}{r_bar}')
    for i in iterator:
        batch = lines_to_translate[i:i + batch_size]
        iterator.set_postfix_str(f"{_('menerjemahkan', 'translating')} {len(batch)} {_('baris', 'lines')}")
        translated_batch = translator.translate_batch(batch)
        translated_texts.extend(translated_batch)
        time.sleep(translator.sleep_time)
    for original, translated in zip(lines_to_translate, translated_texts):
        original_texts[original] = translated or original
    for event in subs.events:
        if event.text in original_texts:
            event.text = original_texts[event.text]
    subs.events = [ev for ev in subs.events if ev.text.strip()]
    
    if add_credit:
        subs = add_credit_to_ass_vtt(subs, add_credit)
    
    if subs.events:
        try:
            safe_makedir(outdir)
            subs.save(str(out_path), encoding="utf-8")
            print(c(f"✅ {_('Disimpan:', 'Saved:')} {out_path.name}", Colors.GREEN))
            return "success", overwrite_mode
        except Exception as e:
            print(_(f"[ERROR] Gagal menulis {out_path.name}: {e}", f"[ERROR] Failed to write {out_path.name}: {e}"))
    return "failed", overwrite_mode

# ===============================================================
# ALUR UTAMA
# ===============================================================
def show_confirmation_summary(
    source: Union[Path, str],
    engine: str,
    target_lang: str,
    processing_mode: str,
    batch_size: int,
    files_to_process: List[Union[Path, str]],
    outdir: Path,
    add_credit: bool
) -> bool:
    """Display confirmation summary before processing"""
    speed_map = {
        "line_by_line": _("Aman (Lambat)", "Safe (Slow)"),
        "batch": _("Cepat (Batch)", "Fast (Batch)")
    }
    
    file_count = len(files_to_process)

    print("\n" + c("✨" * 30, Colors.MAGENTA))
    print(c(_("    RINGKASAN KONFIRMASI", "    CONFIRMATION SUMMARY"), Colors.BOLD + Colors.CYAN))
    print(c("✨" * 30, Colors.MAGENTA))
    print(f"  {c(_('Sumber', 'Source'), Colors.YELLOW)}      : {source}")
    print(f"  {c(_('Engine', 'Engine'), Colors.YELLOW)}      : {engine}")
    print(f"  {c(_('Kecepatan', 'Speed'), Colors.YELLOW)}   : {speed_map.get(processing_mode, 'N/A')}")
    print(f"  {c(_('Target', 'Target'), Colors.YELLOW)}      : {target_lang}")
    print(f"  {c(_('File', 'Files'), Colors.YELLOW)}       : {c(_('Memproses', 'Processing'), Colors.GREEN)} {c(str(file_count), Colors.GREEN)} file")
    print(f"  {c(_('Output', 'Output'), Colors.YELLOW)}      : {c(str(outdir.absolute()), Colors.CYAN)}")
    print(f"  {c(_('Pembersihan', 'Cleaning'), Colors.YELLOW)} : {c(_('Selalu Aktif', 'Always On'), Colors.GREEN)} (e.g., [MUSIC], (SOUND))")
    print(f"  {c(_('Kredit', 'Credit'), Colors.YELLOW)}      : {c('✅ ' + _('Ya', 'Yes'), Colors.GREEN) if add_credit else c('❌ ' + _('Tidak', 'No'), Colors.RED)}")
    print("=" * 60)
    
    choice = input(c(_("Mulai proses? (y/n): ", "Start processing? (y/n): "), Colors.CYAN)).strip().lower()
    return choice in ('y', 'yes', '')

def run_translation_loop(
    engine: str,
    target_lang: str,
    processing_mode: str,
    batch_size: int,
    sleep_time: float,
    files_to_process: List[Path],
    outdir_base: Path,
    output_mode: str,
    add_credit: bool,
    stats: ProcessStats
):
    print(_("\n🚀 Memulai terjemahan...", "\n🚀 Starting translation..."))
    print("=" * 60)
    
    if processing_mode == "batch":
        translator = BatchTranslatorWrapper(engine, target_lang, sleep_time)
    else:
        translator = LineTranslatorWrapper(engine, target_lang)

    overwrite_mode = 'ask'

    for i, file_path in enumerate(files_to_process, 1):
        print(_(f"\n📄 Memproses file {i}/{len(files_to_process)}: {file_path.name}", 
               f"\n📄 Processing file {i}/{len(files_to_process)}: {file_path.name}"))
        
        outdir = file_path.parent if output_mode == 'same' else outdir_base
        
        try:
            result = "failed"
            suffix = file_path.suffix.lower()
            
            if processing_mode == "batch":
                if suffix == '.srt':
                    result, overwrite_mode = process_srt_file_batch(file_path, translator, outdir, overwrite_mode, batch_size, add_credit)
                elif suffix in ('.vtt', '.ass'):
                    result, overwrite_mode = process_ass_vtt_file_batch(file_path, translator, outdir, overwrite_mode, batch_size, add_credit)
            else:
                if suffix == '.srt':
                    result, overwrite_mode = process_srt_file_line(file_path, translator, outdir, overwrite_mode, add_credit)
                elif suffix in ('.vtt', '.ass'):
                    result, overwrite_mode = process_ass_vtt_file_line(file_path, translator, outdir, overwrite_mode, add_credit)

            if result == "success":
                stats.success_count += 1
            elif result == "skipped":
                stats.skipped_count += 1
            else:
                stats.failed_count += 1
                
            if overwrite_mode == 'skip': 
                overwrite_mode = 'ask'
                
        except Exception as e:
            stats.failed_count += 1
            with open("error_log.txt", "a", encoding="utf-8") as ef:
                ef.write(f"[ERROR] processing {file_path}: {traceback.format_exc()}\n")
            print(_("❌ Proses file gagal. Lihat error_log.txt.", "❌ Processing file failed. See error_log.txt."))

    print("=" * 60)
    
    if output_mode == 'subfolder':
        print(_(f"\n📂 File hasil terjemahan disimpan di: {outdir_base.absolute()}",
               f"\n📂 Translated files saved in: {outdir_base.absolute()}"))
    else:
        print(_(f"\n📂 File hasil terjemahan disimpan di folder yang sama dengan aslinya.",
               f"\n📂 Translated files saved in the same folders as originals."))

def process_folder_interactive(folder: Path, engine: str, stats: ProcessStats):
    recursive_choice = input(_("\n🔍 Cari di sub-folder juga? (y/n): ", "\n🔍 Search in sub-folders too? (y/n): ")).strip().lower()
    recursive = recursive_choice in ('y', 'yes')
    
    files = detect_sub_files(folder, recursive)
    if not files:
        print(_("❌ Tidak ada file subtitle (.srt, .vtt, .ass) ditemukan", "❌ No subtitle files (.srt, .vtt, .ass) found"))
        return
    
    files_to_process = select_files_interactive(files, _(f"Ditemukan {len(files)} file", f"Found {len(files)} files"))
    if not files_to_process: return

    outdir, output_mode = get_output_location(folder)
    processing_mode, batch_size, sleep_time = get_processing_speed()
    target_lang = input(_("\n🎯 Bahasa target (default: id): ", "\n🎯 Target language (default: id): ")).strip() or "id"
    add_credit = get_credit_option()
    
    if not show_confirmation_summary(
        source=folder.name, engine=engine, target_lang=target_lang,
        processing_mode=processing_mode, batch_size=batch_size,
        files_to_process=files_to_process,
        outdir=outdir if output_mode == 'subfolder' else Path(_("Folder Asli", "Original Folders")),
        add_credit=add_credit
    ):
        print(_("Dibatalkan.", "Aborted."))
        return

    stats.start()
    run_translation_loop(
        engine, target_lang, processing_mode, batch_size, sleep_time,
        files_to_process, outdir, output_mode, add_credit, stats
    )
    stats.stop()

def process_multiple_folders_interactive(folders: List[Path], engine: str):
    print(c(_("\n📁 Folder yang akan diproses:", "\n📁 Folders to process:"), Colors.CYAN))
    for i, folder in enumerate(folders, 1):
        print(f"  {c(str(i), Colors.GREEN)}. {c(str(folder), Colors.YELLOW)}")
    
    recursive_choice = input(c(_("\n🔍 Cari di sub-folder juga? (y/n): ", "\n🔍 Search in sub-folders too? (y/n): "), Colors.CYAN)).strip().lower()
    recursive = recursive_choice in ('y', 'yes')
    
    # Kumpulkan semua file dari semua folder dengan tracking asal folder
    all_files_with_source = []  # List of tuples: (file_path, source_folder)
    for folder in folders:
        files = detect_sub_files(folder, recursive)
        for f in files:
            all_files_with_source.append((f, folder))
    
    if not all_files_with_source:
        print(c(_("❌ Tidak ada file subtitle (.srt, .vtt, .ass) ditemukan", "❌ No subtitle files (.srt, .vtt, .ass) found"), Colors.RED))
        return
    
    all_files = [f for f, _ in all_files_with_source]
    files_to_process = select_files_interactive(all_files, _(f"Ditemukan {len(all_files)} file dari {len(folders)} folder", f"Found {len(all_files)} files from {len(folders)} folders"))
    if not files_to_process: return

    # Tanya opsi output untuk multiple folder
    print(c(_("\n📁 Pilih lokasi output untuk MULTIPLE FOLDER:", "\n📁 Choose output location for MULTIPLE FOLDERS:"), Colors.CYAN))
    print("  1. " + _("Folder yang sama dengan file asli (setiap folder terpisah)", "Same folder as originals (each folder separate)"))
    print("  2. " + _("Satu folder output untuk semua file", "One output folder for all files"))
    
    output_choice = input(_("Pilihan [1-2] (default 1): ", "Choice [1-2] (default 1): ")).strip() or "1"
    
    if output_choice == "2":
        # Mode: Satu output folder
        base_folder = folders[0].parent if len(folders) > 1 else folders[0]
        outdir, output_mode = get_output_location(base_folder)
        output_mode = "subfolder"  # Force subfolder mode
    else:
        # Mode: Output ke folder asli masing-masing
        outdir = None
        output_mode = "same"
    
    processing_mode, batch_size, sleep_time = get_processing_speed()
    target_lang = input(c(_("\n🎯 Bahasa target (default: id): ", "\n🎯 Target language (default: id): "), Colors.CYAN)).strip() or "id"
    add_credit = get_credit_option()
    
    source_desc = _(f"{len(folders)} folder", f"{len(folders)} folders")
    
    if not show_confirmation_summary(
        source=source_desc, engine=engine, target_lang=target_lang,
        processing_mode=processing_mode, batch_size=batch_size,
        files_to_process=files_to_process,
        outdir=outdir if output_mode == 'subfolder' else Path(_("Folder Asli Masing-Masing", "Original Folders (Each)")),
        add_credit=add_credit
    ):
        print(c(_("Dibatalkan.", "Aborted."), Colors.YELLOW))
        return

    stats = ProcessStats()
    stats.start()
    
    # Proses dengan logic yang benar untuk multiple folder
    if output_mode == "same":
        # Output ke folder asli masing-masing
        run_translation_loop(
            engine, target_lang, processing_mode, batch_size, sleep_time,
            files_to_process, None, output_mode, add_credit, stats
        )
    else:
        # Output ke satu folder
        run_translation_loop(
            engine, target_lang, processing_mode, batch_size, sleep_time,
            files_to_process, outdir, output_mode, add_credit, stats
        )
    
    stats.stop()
    stats.print_summary()

def process_zip_interactive(zip_path: Path, engine: str, stats: ProcessStats):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            all_files = zf.namelist()
            sub_files = sorted([f for f in all_files if f.lower().endswith(('.srt', '.vtt', '.ass')) and not f.startswith('__MACOSX/')])
            if not sub_files:
                print(_("❌ Tidak ada file subtitle ditemukan di dalam .zip", "❌ No subtitle files found inside the .zip"))
                return
            
            fake_paths = [Path(f) for f in sub_files]
            selected_fake_paths = select_files_interactive(fake_paths, _(f"Ditemukan {len(sub_files)} file di {zip_path.name}", f"Found {len(sub_files)} files in {zip_path.name}"))
            if not selected_fake_paths: return

            selected_filenames = [str(p) for p in selected_fake_paths]
            
            outdir, output_mode = get_output_location(zip_path.parent)
            processing_mode, batch_size, sleep_time = get_processing_speed()
            target_lang = input(_("\n🎯 Bahasa target (default: id): ", "\n🎯 Target language (default: id): ")).strip() or "id"
            add_credit = get_credit_option()

            if not show_confirmation_summary(
                source=zip_path.name, engine=engine, target_lang=target_lang,
                processing_mode=processing_mode, batch_size=batch_size,
                files_to_process=selected_filenames,
                outdir=outdir,
                add_credit=add_credit
            ):
                print(_("Dibatalkan.", "Aborted."))
                return
            
            with tempfile.TemporaryDirectory() as temp_dir:
                print(_(f"Ekstrak {len(selected_filenames)} file...", f"Extracting {len(selected_filenames)} files..."))
                extracted_paths = []
                for filename in selected_filenames:
                    zf.extract(filename, temp_dir)
                    extracted_paths.append(Path(temp_dir) / filename)
                
                stats.start()
                run_translation_loop(
                    engine, target_lang, processing_mode, batch_size, sleep_time,
                    extracted_paths, outdir, output_mode, add_credit, stats
                )
                stats.stop()
    except zipfile.BadZipFile:
        print(_("❌ File zip rusak.", "❌ Bad zip file."))
    except Exception as e:
        print(_(f"❌ Error pemrosesan zip: {e}", f"❌ Error processing zip: {e}"))
        traceback.print_exc()

def process_translation_flow():
    print(_("\n🤖 Pilih mesin terjemah:", "\n🤖 Choose translation engine:"))
    print("  1. " + _("Google Translate (gratis, deteksi otomatis)", "Google Translate (free, auto-detect)"))
    print("  2. " + _("DeepL API (butuh API key)", "DeepL API (requires API key)"))
    engine_choice = input(_("Pilihan [1-2]: ", "Choice [1-2]: ")).strip() or "1"
    engine = "google" if engine_choice == "1" else "deepl"
    
    print(_("\n📁 Pilih sumber subtitle:", "\n📁 Choose subtitle source:"))
    print("  1. " + _("Jelajahi folder / file .zip", "Browse folder / .zip file"))
    print("  2. " + _("Folder saat ini", "Current folder"))
    print("  3. " + _("Pilih multiple folder", "Select multiple folders"))
    folder_choice = input(_("Pilihan [1-3]: ", "Choice [1-3]: ")).strip() or "1"
    
    stats = ProcessStats()
    
    if folder_choice == "3":
        # Mode multiple folder
        folders = browse_folders_multiple(Path.home())
        if folders:
            process_multiple_folders_interactive(folders, engine)
    elif folder_choice == "1":
        selected_path = browse_item_interactive(Path.home())
        if not selected_path: return
        
        if selected_path.is_file() and selected_path.suffix.lower() == '.zip':
            process_zip_interactive(selected_path, engine, stats)
            stats.print_summary()
        elif selected_path.is_dir():
            process_folder_interactive(selected_path, engine, stats)
            stats.print_summary()
        else:
            print(_("❌ Pilihan tidak valid (harus folder atau file .zip).", "❌ Invalid selection (must be a folder or .zip file)."))
    else:
        selected_path = Path(".").resolve()
        process_folder_interactive(selected_path, engine, stats)
        stats.print_summary()

# ===============================================================
# MENU UTAMA & LAIN-LAIN
# ===============================================================

def language_settings_menu():
    global LANG_UI
    print("\n" + "="*50)
    print(_("🌐 PENGATURAN BAHASA UI", "🌐 UI LANGUAGE SETTINGS"))
    print("="*50)
    print("1. " + _("Bahasa Indonesia", "Indonesian"))
    print("2. " + _("English", "English"))
    print("3. " + _("Kembali", "Back"))
    choice = input(_("\nPilihan [1-3]: ", "\nChoice [1-3]: ")).strip()
    if choice == "1":
        LANG_UI = "ID"
        CONFIG_FILE.write_text("LANG_UI=ID\n", encoding="utf-8")
        print("✅ " + _("Bahasa diatur ke Indonesia", "Language set to Indonesian"))
    elif choice == "2":
        LANG_UI = "EN"
        CONFIG_FILE.write_text("LANG_UI=EN\n", encoding="utf-8")
        print("✅ " + _("Language set to English", "Language set to English"))
    time.sleep(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Zee Subtitle Translator v1')
    parser.add_argument('input_path', nargs='?', help=_('Path ke folder atau file .zip (opsional)', 'Path to folder or .zip file (optional)'))
    return parser.parse_args()

def interactive_menu():
    while True:
        banner = (
            "╔═══════════════════════════════════════════╗\n"
            "║                                           ║\n"
            "║        ZEE SUBTITLE TRANSLATOR v1         ║\n"
            "║                                           ║\n"
            "╚═══════════════════════════════════════════╝"
        )
        print(banner)
        print(_("Selamat datang!", "Welcome!"))
        print("-" * 60)
        print("1. " + _("Terjemahkan Subtitle", "Translate Subtitles"))
        print("2. " + _("Pengaturan Bahasa UI", "UI Language Settings"))
        print("3. " + _("Keluar", "Exit"))
        print("-" * 60)
        choice = input(_("Pilihan [1-3]: ", "Choice [1-3]: ")).strip()
        if choice == "1": process_translation_flow()
        elif choice == "2": language_settings_menu()
        elif choice == "3": farewell()
        else: print(_("❌ Pilihan tidak valid", "❌ Invalid choice"))

def farewell():
    if LANG_UI == "EN":
        print("\n✨ Thank you for using Zee Subtitle Translator v1!\n")
    else:
        print("\n✨ Terima kasih telah menggunakan Zee Subtitle Translator v1!\n")
    sys.exit(0)

def main():
    try:
        args = parse_arguments()
        if args.input_path:
            path = Path(args.input_path)
            if not path.exists():
                print(_(f"❌ Path tidak ditemukan: {path}", f"❌ Path not found: {path}"))
                sys.exit(1)
            print(_(f"📂 Path terdeteksi: {path}", f"📂 Path detected: {path}"))
            use_path = input(_("Gunakan path ini? (y/n): ", "Use this path? (y/n): ")).strip().lower()
            if use_path in ('y', 'yes', ''):
                print(_("\n🤖 Pilih mesin terjemah:", "\n🤖 Choose translation engine:"))
                print("  1. Google (default)")
                print("  2. DeepL")
                engine_choice = input("> ").strip() or "1"
                engine = "google" if engine_choice == "1" else "deepl"
                
                stats = ProcessStats()
                
                if path.is_file() and path.suffix.lower() == '.zip':
                    process_zip_interactive(path, engine, stats)
                    stats.print_summary()
                elif path.is_dir():
                    process_folder_interactive(path, engine, stats)
                    stats.print_summary()
                else:
                    print(_("❌ Path harus berupa folder atau file .zip.", "❌ Path must be a folder or a .zip file."))
            else:
                interactive_menu()
        else:
            interactive_menu()
    except KeyboardInterrupt:
        print("\n" + _("❌ Dibatalkan oleh pengguna", "❌ Cancelled by user"))
        sys.exit(1)
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[FATAL] {traceback.format_exc()}\n")
        print(_("❌ Terjadi kesalahan tak terduga", "❌ Unexpected error occurred"))
        print(str(e))

if __name__ == "__main__":
    main()
