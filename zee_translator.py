#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zee Subtitle Translator v1.1
A powerful batch subtitle translator with multi-format support
Now with ChatGPT API support and Multiple Folder feature!

Author: Zee
License: MIT
Repository: https://github.com/zeewank/zee-subtitle-translator
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
import json
import requests
from datetime import timedelta, datetime
from pathlib import Path
from typing import List, Tuple, Optional, Union

# ===============================================================
# CONFIGURATION
# ===============================================================
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


# ===============================================================
# COLORS
# ===============================================================
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


# ===============================================================
# CHECK DEPENDENCIES
# ===============================================================
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
    pass  # Readline is optional


# ===============================================================
# PROCESS STATS
# ===============================================================
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
        print(c(f"🚀 {_('RINGKASAN PROSES', 'PROCESS SUMMARY')}", Colors.BOLD + Colors.CYAN))
        print(c(f"✅ {self.success_count} {_('file berhasil', 'files succeeded')}", Colors.GREEN))
        print(c(f"⚠️  {self.skipped_count} {_('dilewati', 'skipped')}", Colors.YELLOW))
        print(c(f"❌ {self.failed_count} {_('gagal', 'failed')}", Colors.RED))
        print(c(f"ℹ️  {_('Total durasi', 'Total duration')}: {duration_str}", Colors.CYAN))
        print("=" * 70)


# ===============================================================
# CHATGPT API TRANSLATOR
# ===============================================================
class ChatGPTTranslator:
    """ChatGPT API translator wrapper"""
    
    def __init__(self, api_key: str, target_lang: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.target_lang = target_lang
        self.model = model
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.max_retries = 3
        
        print(f"[Mode: ChatGPT API - {model}]")
    
    def translate(self, text: str, desc: str = "") -> str:
        """Translate text using ChatGPT API"""
        txt = (text or "").strip()
        if not txt:
            return txt
        
        prompt = f"Translate the following subtitle text to {self.target_lang}. Only return the translation, no explanations:\n\n{txt}"
        
        last_exc = None
        for attempt in range(self.max_retries):
            try:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                }
                
                data = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": f"You are a professional subtitle translator. Translate accurately to {self.target_lang}."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.3,
                    "max_tokens": 500
                }
                
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    json=data,
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    translated = result['choices'][0]['message']['content'].strip()
                    return translated
                elif response.status_code == 401:
                    print(c(f"\n❌ {_('API Key tidak valid!', 'Invalid API Key!')}", Colors.RED))
                    return txt
                elif response.status_code == 429:
                    print(c(f"\n⚠️  {_('Rate limit terlampaui, menunggu...', 'Rate limit exceeded, waiting...')}", Colors.YELLOW))
                    time.sleep(2 ** attempt)
                else:
                    print(c(f"\n⚠️  API Error: {response.status_code}", Colors.YELLOW))
                    last_exc = Exception(f"API returned {response.status_code}")
                    
            except requests.exceptions.Timeout:
                print(c(f"\n⚠️  {_('Timeout, mencoba lagi...', 'Timeout, retrying...')}", Colors.YELLOW))
                last_exc = Exception("Timeout")
            except Exception as e:
                last_exc = e
                time.sleep(1)
        
        print(_(f"❌ Gagal permanen: {txt[:50]}", f"❌ Permanent fail: {txt[:50]}"))
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[CHATGPT_FAIL] text={txt[:120]} err={repr(last_exc)}\n")
        return txt
    
    def translate_batch(self, texts: List[str]) -> List[str]:
        """Translate batch of texts"""
        if not texts:
            return []
        
        batch_text = "\n---SEPARATOR---\n".join(texts)
        prompt = f"Translate these subtitle lines to {self.target_lang}. Separate translations with ---SEPARATOR---. Only return translations:\n\n{batch_text}"
        
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": f"You are a professional subtitle translator. Translate accurately to {self.target_lang}."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3,
                "max_tokens": 2000
            }
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=data,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                translated = result['choices'][0]['message']['content'].strip()
                translations = translated.split("---SEPARATOR---")
                translations = [t.strip() for t in translations]
                
                if len(translations) == len(texts):
                    return translations
                else:
                    print(c(f"\n⚠️  {_('Batch mismatch, fallback ke line-by-line', 'Batch mismatch, fallback to line-by-line')}", Colors.YELLOW))
                    return [self.translate(t) for t in texts]
            else:
                print(c(f"\n⚠️  API Error: {response.status_code}, fallback", Colors.YELLOW))
                return [self.translate(t) for t in texts]
                
        except Exception as e:
            print(c(f"\n⚠️  Batch failed: {e}, fallback", Colors.YELLOW))
            return [self.translate(t) for t in texts]


# ===============================================================
# ENCODING DETECTION
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
# TEXT CLEANING
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
# CREDIT FUNCTIONS
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
# TRANSLATOR WRAPPERS
# ===============================================================
class LineTranslatorWrapper:
    """Line-by-line translator (Safe mode)"""
    
    def __init__(self, engine: str, target: str):
        self.engine = engine.lower()
        self.target = target
        self.max_retries = 3
        print(f"[Mode: {_('Aman (Baris per Baris)', 'Safe (Line-by-Line)')}]")
        
    def translate(self, text: str, desc: str = "") -> str:
        txt = (text or "").strip()
        if not txt:
            return txt
            
        last_exc = None
        for attempt in range(self.max_retries):
            try:
                if self.engine == "deepl":
                    key = os.getenv("DEEPL_API_KEY", "")
                    if not key:
                        raise RuntimeError("DEEPL_API_KEY not found.")
                    return DeeplTranslator(api_key=key, target=self.target, source="auto").translate(txt)
                else:
                    return GoogleTranslator(source="auto", target=self.target).translate(txt)
            except Exception as e:
                last_exc = e
                if desc:
                    print(_(f"⚠️  Gagal '{desc[:30]}...', mencoba lagi ({attempt + 1})",
                           f"⚠️  Fail '{desc[:30]}...', retry ({attempt + 1})"))
                time.sleep(1)
                
        print(_(f"❌ Gagal permanen: {txt[:50]}", f"❌ Permanent fail: {txt[:50]}"))
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[TRANSLATE_FAIL] engine={self.engine} text={txt[:120]} err={repr(last_exc)}\n")
        return txt


class BatchTranslatorWrapper:
    """Batch translator (Fast mode)"""
    
    def __init__(self, engine: str, target: str, sleep_time: float = 0.5):
        self.engine = engine.lower()
        self.target = target
        self.sleep_time = sleep_time
        self.max_retries = 3
        print(f"[Mode: {_('Cepat (Batch)', 'Fast (Batch)')}]")
        
        try:
            if self.engine == "deepl":
                key = os.getenv("DEEPL_API_KEY", "")
                if not key:
                    raise RuntimeError("DEEPL_API_KEY not found.")
                self.translator = DeeplTranslator(api_key=key, target=self.target, source="auto")
            else:
                self.translator = GoogleTranslator(source="auto", target=self.target)
        except Exception as e:
            print(_(f"❌ Gagal inisialisasi {engine} translator: {e}", 
                   f"❌ Failed to init {engine} translator: {e}"))
            sys.exit(1)

    def translate_batch(self, texts: List[str]) -> List[str]:
        if not texts:
            return []
            
        for attempt in range(self.max_retries):
            try:
                translated_texts = self.translator.translate_batch(texts)
                if translated_texts is None:
                    raise Exception("API returned None (likely rate-limit)")
                if len(translated_texts) != len(texts):
                    print(f"⚠️  {_('Peringatan: Jumlah batch tidak cocok!', 'Warning: Batch mismatch!')}")
                    return texts
                return translated_texts
            except Exception as e:
                print(_(f"\n⚠️  Gagal batch, mencoba lagi ({attempt+1})... Error: {e}",
                       f"\n⚠️  Batch failed, retrying ({attempt+1})... Error: {e}"))
                time.sleep(1 * (attempt + 1))
                
        print(_("❌ Gagal batch permanen. Menggunakan teks asli.", 
               "❌ Permanent batch fail. Using original text."))
        return texts


# ===============================================================
# FILE PROCESSING - SRT
# ===============================================================

def process_srt_file_line(file_path: Path, translator, output_path: Path, add_credit: bool):
    """Process SRT file line by line (Safe mode)"""
    try:
        content = read_file_with_detection(file_path)
        subs = list(srt.parse(content))

        for sub in tqdm(subs, desc=str(file_path.name)):
            original = sub.content
            cleaned = remove_bracketed(original)

            if cleaned:
                try:
                    translated = translator.translate(cleaned, desc=original[:30])
                except Exception as e:
                    # Defensive: fallback to original text
                    translated = cleaned
                sub.content = translated
            else:
                sub.content = ""

        subs = add_credit_to_srt(subs, add_credit)
        output_content = srt.compose(subs)
        output_path.write_text(output_content, encoding='utf-8')
        return ("success", "ask")
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[ERROR] file={file_path} error={str(e)}\n")
            ef.write(f"{traceback.format_exc()}\n")
        return ("failed", "ask")


def process_srt_file_batch(file_path: Path, translator, output_path: Path, batch_size: int, add_credit: bool):
    """Process SRT file in batches (Fast mode)"""
    try:
        content = read_file_with_detection(file_path)
        subs = list(srt.parse(content))

        texts_to_translate = []
        for sub in subs:
            cleaned = remove_bracketed(sub.content)
            texts_to_translate.append(cleaned)

        # Process in batches
        translated_all = []
        if not texts_to_translate:
            subs = add_credit_to_srt(subs, add_credit)
            output_path.write_text(srt.compose(subs), encoding='utf-8')
            return ("success", "ask")

        num_batches = (len(texts_to_translate) + batch_size - 1) // batch_size

        with tqdm(total=num_batches, desc=str(file_path.name)) as pbar:
            for i in range(0, len(texts_to_translate), batch_size):
                batch = texts_to_translate[i:i+batch_size]
                try:
                    translated_batch = translator.translate_batch(batch)
                except Exception as e:
                    translated_batch = None
                # Defensive: if API returned None or length mismatch, fallback to per-line
                if translated_batch is None or len(translated_batch) != len(batch):
                    fallback = []
                    for t in batch:
                        try:
                            fallback.append(translator.translate(t))
                        except Exception:
                            fallback.append(t)
                    translated_batch = fallback
                translated_all.extend(translated_batch)
                pbar.update(1)
                time.sleep(getattr(translator, 'sleep_time', 0.5))

        # Apply translations
        for sub, translated in zip(subs, translated_all):
            sub.content = translated if translated else ""

        subs = add_credit_to_srt(subs, add_credit)
        output_content = srt.compose(subs)
        output_path.write_text(output_content, encoding='utf-8')
        return ("success", "ask")
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[ERROR] file={file_path} error={str(e)}\n")
            ef.write(f"{traceback.format_exc()}\n")
        return ("failed", "ask")


def process_ass_vtt_file_line(file_path: Path, translator, output_path: Path, add_credit: bool):
    """Process ASS/VTT file line by line (Safe mode)"""
    try:
        subs = pysubs2.load(str(file_path))

        for event in tqdm(subs.events, desc=str(file_path.name)):
            original = event.text
            cleaned = remove_bracketed(original)

            if cleaned:
                try:
                    translated = translator.translate(cleaned, desc=original[:30])
                except Exception:
                    translated = cleaned
                event.text = translated
            else:
                event.text = ""

        subs = add_credit_to_ass_vtt(subs, add_credit)
        subs.save(str(output_path), encoding="utf-8")
        return ("success", "ask")
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[ERROR] file={file_path} error={str(e)}\n")
            ef.write(f"{traceback.format_exc()}\n")
        return ("failed", "ask")


def process_ass_vtt_file_batch(file_path: Path, translator, output_path: Path, batch_size: int, add_credit: bool):
    """Process ASS/VTT file in batches (Fast mode)"""
    try:
        subs = pysubs2.load(str(file_path))

        texts_to_translate = []
        for event in subs.events:
            cleaned = remove_bracketed(event.text)
            texts_to_translate.append(cleaned)

        # Process in batches
        translated_all = []
        if not texts_to_translate:
            subs = add_credit_to_ass_vtt(subs, add_credit)
            subs.save(str(output_path), encoding="utf-8")
            return ("success", "ask")

        num_batches = (len(texts_to_translate) + batch_size - 1) // batch_size

        with tqdm(total=num_batches, desc=str(file_path.name)) as pbar:
            for i in range(0, len(texts_to_translate), batch_size):
                batch = texts_to_translate[i:i+batch_size]
                try:
                    translated_batch = translator.translate_batch(batch)
                except Exception:
                    translated_batch = None
                if translated_batch is None or len(translated_batch) != len(batch):
                    fallback = []
                    for t in batch:
                        try:
                            fallback.append(translator.translate(t))
                        except Exception:
                            fallback.append(t)
                    translated_batch = fallback
                translated_all.extend(translated_batch)
                pbar.update(1)
                time.sleep(getattr(translator, 'sleep_time', 0.5))

        # Apply translations
        for event, translated in zip(subs.events, translated_all):
            event.text = translated if translated else ""

        subs = add_credit_to_ass_vtt(subs, add_credit)
        subs.save(str(output_path), encoding="utf-8")
        return ("success", "ask")
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[ERROR] file={file_path} error={str(e)}\n")
            ef.write(f"{traceback.format_exc()}\n")
        return ("failed", "ask")


# ===============================================================
# FILE BROWSER
# ===============================================================
def browse_item_interactive(start_path: Path = None) -> Optional[Path]:
    """Interactive file/folder browser"""
    if start_path is None:
        start_path = Path.cwd()
    
    current = start_path.resolve()
    
    while True:
        # Pre-fetch all text to avoid scope issues
        loc_text = _("Lokasi saat ini", "Current location")
        err_text = _("Tidak ada izin akses folder ini", "No permission to access this folder")
        empty_text = _("(Folder kosong)", "(Empty folder)")
        cmd_text = _("Perintah: angka=buka, Enter=pilih folder ini, q=keluar", 
                    "Commands: number=open, Enter=select this folder, q=exit")
        invalid_text = _("Pilihan tidak valid!", "Invalid choice!")
        input_text = _("Masukkan angka atau Enter!", "Enter a number or press Enter!")
        
        print(f"\n📂 {loc_text}: {current}")
        print("-" * 70)
        
        items = []
        try:
            if current.parent != current:
                items.append(("📁 ..", current.parent, True))
            
            for item in sorted(current.iterdir()):
                if item.is_dir():
                    items.append((f"📁 {item.name}/", item, True))
                elif item.suffix.lower() in ['.srt', '.vtt', '.ass', '.zip']:
                    items.append((f"📄 {item.name}", item, False))
        except PermissionError:
            print(c(f"❌ {err_text}", Colors.RED))
            current = current.parent
            continue
        
        if not items:
            print(empty_text)
        
        # FIXED: Don't use _ as throwaway variable!
        for idx, (display, item_path, item_is_dir) in enumerate(items, 1):
            print(f"  {idx}. {display}")
        
        print()
        print(cmd_text)
        
        choice = input("> ").strip()
        
        if not choice:
            return current
        if choice.lower() == 'q':
            return None
        
        try:
            idx = int(choice)
            if 1 <= idx <= len(items):
                display, path, is_dir = items[idx - 1]
                if is_dir:
                    current = path
                else:
                    return path
            else:
                print(c(invalid_text, Colors.RED))
        except ValueError:
            print(c(input_text, Colors.RED))


def select_files_interactive(files: List[Path]) -> List[Path]:
    """Interactive file selection"""
    if not files:
        return []
    
    found_text = _("Ditemukan", "Found")
    files_text = _("file", "files")
    print(f"\n📋 {found_text} {len(files)} {files_text}:")
    for idx, f in enumerate(files, 1):
        print(f"  {idx}. {f.name}")
    
    print()
    select_text = _("Pilih file:", "Select files:")
    all_text = _("  0. [PROSES SEMUA]", "  0. [PROCESS ALL]")
    example_text = _("  (contoh: 1, 3, 5) atau range (contoh: 1-10), atau tekan Enter untuk semua:", 
                    "  (e.g., 1, 3, 5) or range (e.g., 1-10), or press Enter for all:")
    exit_text = _("  q. Keluar/Batal", "  q. Exit/Cancel")
    
    print(select_text)
    print(all_text)
    print(example_text)
    print(exit_text)
    
    choice = input("> ").strip()
    
    if choice.lower() == 'q':
        return []
    
    # Handle empty input (Enter) or "0" - both select all files
    if choice == "0" or not choice:
        return files
    
    selected = []
    try:
        for part in choice.split(','):
            part = part.strip()
            if '-' in part:
                start, end = map(int, part.split('-'))
                selected.extend(range(start, end + 1))
            else:
                selected.append(int(part))
        
        return [files[i-1] for i in selected if 1 <= i <= len(files)]
    except:
        invalid_text = _("Format tidak valid!", "Invalid format!")
        print(c(invalid_text, Colors.RED))
        return []


# ===============================================================
# MULTIPLE FOLDER BROWSER
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


def detect_sub_files(folder: Path, recursive: bool = False) -> List[Path]:
    """Deteksi file subtitle dalam folder"""
    pattern = "**/*" if recursive else "*"
    extensions = [".srt", ".vtt", ".ass"]
    files = []
    for ext in extensions:
        files.extend(sorted(folder.glob(f"{pattern}{ext}")))
    return files


# ===============================================================
# MULTIPLE FOLDER PROCESSING
# ===============================================================
def process_multiple_folders_interactive(folders: List[Path], engine: str, stats: ProcessStats):
    """Process multiple folders dengan file subtitle"""
    print(c(_("\n📁 Folder yang akan diproses:", "\n📁 Folders to process:"), Colors.CYAN))
    for i, folder in enumerate(folders, 1):
        print(f"  {c(str(i), Colors.GREEN)}. {c(str(folder), Colors.YELLOW)}")
    
    recursive_choice = input(c(_("\n🔍 Cari di sub-folder juga? (y/n): ", "\n🔍 Search in sub-folders too? (y/n): "), Colors.CYAN)).strip().lower()
    recursive = recursive_choice in ('y', 'yes')
    
    # Kumpulkan semua file dari semua folder
    all_files = []
    for folder in folders:
        files = detect_sub_files(folder, recursive)
        all_files.extend(files)
    
    if not all_files:
        no_files_msg = _("❌ Tidak ada file subtitle ditemukan!", "❌ No subtitle files found!")
        print(c(no_files_msg, Colors.RED))
        return
    
    # Select files
    selected_files = select_files_interactive(all_files)
    if not selected_files:
        no_select_msg = _("❌ Tidak ada file dipilih", "❌ No files selected")
        print(c(no_select_msg, Colors.RED))
        return
    
    # Choose output location for multiple folders
    output_prompt = _("\n📂 Pilih lokasi output untuk MULTIPLE FOLDER:", "\n📂 Choose output location for MULTIPLE FOLDERS:")
    print(output_prompt)
    print("  1. " + _("Folder yang sama dengan file asli (setiap folder terpisah)", "Same folder as original files (each folder separate)"))
    print("  2. " + _("Satu folder output untuk semua file", "One output folder for all files"))
    print("  q. " + _("Keluar/Kembali", "Exit/Back"))
    output_choice = input(_("Pilihan [1-2/q] (default 1): ", "Choice [1-2/q] (default 1): ")).strip() or "1"
    
    if output_choice.lower() == 'q':
        return
    
    if output_choice == "2":
        # Mode: Satu output folder
        base_folder = folders[0].parent if len(folders) > 1 else folders[0]
        folder_name = input(_("Nama subfolder (default: translated): ", "Subfolder name (default: translated): ")).strip() or "translated"
        output_dir = base_folder / folder_name
        output_dir.mkdir(exist_ok=True)
        output_mode = "subfolder"
    else:
        # Mode: Output ke folder asli masing-masing
        output_dir = None
        output_mode = "same"
    
    # Choose speed mode
    speed_prompt = _("\n⚙️ Pilih 'Processing Engine' (Kecepatan):", "\n⚙️ Choose 'Processing Engine' (Speed):")
    print(speed_prompt)
    print("  1. " + _("Aman (Lambat)", "Safe (Slow)"))
    print("  2. " + _("Standard (Cepat / Direkomendasikan)", "Standard (Fast / Recommended)"))
    print("  3. " + _("Aggressive (Sangat Cepat)", "Aggressive (Very Fast)"))
    print("  q. " + _("Keluar/Kembali", "Exit/Back"))
    speed_choice = input(_("Pilihan [1-3/q] (default 2): ", "Choice [1-3/q] (default 2): ")).strip() or "2"
    
    if speed_choice.lower() == 'q':
        return
    
    batch_size = 1
    use_batch = False
    
    if speed_choice == "1":
        use_batch = False
    elif speed_choice == "3":
        use_batch = True
        batch_size = 100
    else:  # 2
        use_batch = True
        batch_size = 50
    
    # Choose target language
    lang_prompt = _("🎯 Bahasa target (default: id, atau q untuk keluar): ", "🎯 Target language (default: id, or q to exit): ")
    target_lang = input(lang_prompt).strip() or "id"
    
    if target_lang.lower() == 'q':
        return
    
    # Add credits?
    credit_prompt = _("🎬 Tambahkan kredit pembuat di awal? (y/n/q default y): ", 
                     "🎬 Add creator credit at the beginning? (y/n/q default y): ")
    add_credit_input = input(credit_prompt).strip().lower()
    
    if add_credit_input == 'q':
        return
    
    add_credit = add_credit_input != 'n'
    
    # Confirmation
    print("\n" + "✨" * 30)
    summary_text = _("        RINGKASAN KONFIRMASI", "        CONFIRMATION SUMMARY")
    print(c(summary_text, Colors.BOLD + Colors.CYAN))
    print("✨" * 30)
    
    source_label = _("Sumber", "Source")
    engine_label = _("Mesin", "Engine")
    speed_label = _("Kecepatan", "Speed")
    target_label = _("Target", "Target")
    files_label = _("File", "Files")
    output_label = _("Output", "Output")
    credit_label = _("Kredit", "Credit")
    
    speed_text = _('Aman' if not use_batch else ('Cepat' if batch_size == 50 else 'Aggressive'), 
                   'Safe' if not use_batch else ('Fast' if batch_size == 50 else 'Aggressive'))
    processing_text = _("Memproses", "Processing")
    same_folder_text = _("Folder asli masing-masing", "Original folders (each)")
    single_folder_text = _("Satu folder output", "Single output folder")
    yes_text = _("Ya", "Yes")
    no_text = _("Tidak", "No")
    
    print(f"  {source_label}      : {len(folders)} {_('folder', 'folders')}")
    print(f"  {engine_label}      : {engine}")
    print(f"  {speed_label}    : {speed_text}")
    print(f"  {target_label}      : {target_lang}")
    print(f"  {files_label}        : {processing_text} {len(selected_files)} {_('file', 'files')}")
    print(f"  {output_label}      : {same_folder_text if output_mode == 'same' else single_folder_text}")
    if output_mode == "subfolder":
        print(f"  {_('Folder Output', 'Output Folder')}  : {output_dir}")
    print(f"  {credit_label}      : {'✅ ' + yes_text if add_credit else '❌ ' + no_text}")
    print("=" * 70)
    
    confirm_prompt = _("\nMulai proses? (y/n/q): ", "\nStart processing? (y/n/q): ")
    confirm = input(confirm_prompt).strip().lower()
    if confirm != 'y':
        cancel_msg = _("❌ Dibatalkan", "❌ Cancelled")
        print(cancel_msg)
        return
    
    # Create translator
    if use_batch:
        translator = BatchTranslatorWrapper(engine, target_lang)
    else:
        translator = LineTranslatorWrapper(engine, target_lang)
    
    # Process files
    stats.start()
    
    print(f"\n🚀 {_('Memulai terjemahan...', 'Starting translation...')}")
    print("=" * 70)
    
    for idx, file_path in enumerate(selected_files, 1):
        print(f"\n📄 {_('Memproses file', 'Processing file')} {idx}/{len(selected_files)}: {file_path.name}")
        
        try:
            # Determine output path
            if output_mode == "subfolder":
                output_path = output_dir / f"{file_path.stem}.{target_lang}{file_path.suffix}"
            else:
                output_path = file_path.parent / f"{file_path.stem}.{target_lang}{file_path.suffix}"
            
            # Check if already exists
            if output_path.exists():
                overwrite = input(_(f"⚠️  File {output_path.name} sudah ada. Timpa? (y/n): ",
                                   f"⚠️  File {output_path.name} already exists. Overwrite? (y/n): ")).strip().lower()
                if overwrite != 'y':
                    print(_("⏭️  Dilewati", "⏭️  Skipped"))
                    stats.skipped_count += 1
                    continue
            
            # Process based on file type - PERBAIKAN: tidak unpack NoneType
            result_tuple = None
            if file_path.suffix.lower() == '.srt':
                if use_batch:
                    result_tuple = process_srt_file_batch(file_path, translator, output_path, batch_size, add_credit)
                else:
                    result_tuple = process_srt_file_line(file_path, translator, output_path, add_credit)
            else:  # .vtt or .ass
                if use_batch:
                    result_tuple = process_ass_vtt_file_batch(file_path, translator, output_path, batch_size, add_credit)
                else:
                    result_tuple = process_ass_vtt_file_line(file_path, translator, output_path, add_credit)
            
            # Handle return value - PERBAIKAN: fungsi sekarang return tuple (status, mode)
            if result_tuple and len(result_tuple) >= 1:
                status = result_tuple[0]
            else:
                status = "failed"
                
            if status == "success":
                print(c(f"✅ {_('Disimpan', 'Saved')}: {output_path.name}", Colors.GREEN))
                stats.success_count += 1
            else:
                stats.failed_count += 1
            
        except KeyboardInterrupt:
            print(_("\n\n❌ Dibatalkan oleh pengguna", "\n\n❌ Cancelled by user"))
            stats.stop()
            stats.print_summary()
            return
        except Exception as e:
            print(c(f"❌ {_('Gagal', 'Failed')}: {str(e)}", Colors.RED))
            stats.failed_count += 1
            with open("error_log.txt", "a", encoding="utf-8") as ef:
                ef.write(f"[ERROR] file={file_path} error={str(e)}\n")
                ef.write(f"{traceback.format_exc()}\n")
    
    stats.stop()


# ===============================================================
# ZIP FILE HANDLER
# ===============================================================
def process_zip_interactive(zip_path: Path, engine: str, stats: ProcessStats):
    """Process ZIP file containing subtitle files"""
    try:
        import zipfile
        import tempfile
        
        extract_msg = _("📦 Membuka file ZIP...", "📦 Opening ZIP file...")
        print(extract_msg)
        
        with zipfile.ZipFile(zip_path, 'r') as zf:
            all_files = zf.namelist()
            sub_files = sorted([f for f in all_files if f.lower().endswith(('.srt', '.vtt', '.ass')) and not f.startswith('__MACOSX/')])
            
            if not sub_files:
                no_files_msg = _("❌ Tidak ada file subtitle ditemukan di dalam .zip", "❌ No subtitle files found inside the .zip")
                print(c(no_files_msg, Colors.RED))
                return
            
            found_msg = _("Ditemukan", "Found")
            files_msg = _("file di", "files in")
            print(c(f"\n✅ {found_msg} {len(sub_files)} {files_msg} {zip_path.name}", Colors.GREEN))
            
            # Create fake Path objects for selection
            fake_paths = [Path(f) for f in sub_files]
            selected_fake_paths = select_files_interactive(fake_paths)
            
            if not selected_fake_paths:
                return
            
            selected_filenames = [str(p) for p in selected_fake_paths]
            
            # Get output location
            output_prompt = _("\n📂 Pilih lokasi output:", "\n📂 Choose output location:")
            print(output_prompt)
            print("  1. " + _("Buat subfolder baru", "Create a new subfolder"))
            print("  2. " + _("Folder yang sama dengan ZIP", "Same folder as ZIP"))
            print("  q. " + _("Keluar/Kembali", "Exit/Back"))
            output_choice = input(_("Pilihan [1-2/q] (default 1): ", "Choice [1-2/q] (default 1): ")).strip() or "1"
            
            if output_choice.lower() == 'q':
                return
            
            if output_choice == "2":
                output_dir = zip_path.parent
            else:
                folder_name = input(_("Nama subfolder (default: translated): ", "Subfolder name (default: translated): ")).strip() or "translated"
                output_dir = zip_path.parent / folder_name
            
            # Get speed mode
            speed_prompt = _("\n⚙️ Pilih 'Processing Engine' (Kecepatan):", "\n⚙️ Choose 'Processing Engine' (Speed):")
            print(speed_prompt)
            print("  1. " + _("Aman (Lambat)", "Safe (Slow)"))
            print("  2. " + _("Standard (Cepat / Direkomendasikan)", "Standard (Fast / Recommended)"))
            print("  3. " + _("Aggressive (Sangat Cepat)", "Aggressive (Very Fast)"))
            print("  q. " + _("Keluar/Kembali", "Exit/Back"))
            speed_choice = input(_("Pilihan [1-3/q] (default 2): ", "Choice [1-3/q] (default 2): ")).strip() or "2"
            
            if speed_choice.lower() == 'q':
                return
            
            batch_size = 1
            use_batch = False
            
            if speed_choice == "1":
                use_batch = False
            elif speed_choice == "3":
                use_batch = True
                batch_size = 100
            else:  # 2
                use_batch = True
                batch_size = 50
            
            # Get target language
            lang_prompt = _("🎯 Bahasa target (default: id, atau q untuk keluar): ", "🎯 Target language (default: id, or q to exit): ")
            target_lang = input(lang_prompt).strip() or "id"
            
            if target_lang.lower() == 'q':
                return
            
            # Add credits?
            credit_prompt = _("🎬 Tambahkan kredit pembuat di awal? (y/n/q default y): ", 
                             "🎬 Add creator credit at the beginning? (y/n/q default y): ")
            add_credit_input = input(credit_prompt).strip().lower()
            
            if add_credit_input == 'q':
                return
            
            add_credit = add_credit_input != 'n'
            
            # Confirmation
            print("\n" + "✨" * 30)
            summary_text = _("        RINGKASAN KONFIRMASI", "        CONFIRMATION SUMMARY")
            print(c(summary_text, Colors.BOLD + Colors.CYAN))
            print("✨" * 30)
            
            source_label = _("Sumber", "Source")
            engine_label = _("Mesin", "Engine")
            speed_label = _("Kecepatan", "Speed")
            target_label = _("Target", "Target")
            files_label = _("File", "Files")
            output_label = _("Output", "Output")
            credit_label = _("Kredit", "Credit")
            
            speed_text = _('Aman' if not use_batch else ('Cepat' if batch_size == 50 else 'Aggressive'), 
                           'Safe' if not use_batch else ('Fast' if batch_size == 50 else 'Aggressive'))
            processing_text = _("Memproses", "Processing")
            yes_text = _("Ya", "Yes")
            no_text = _("Tidak", "No")
            
            print(f"  {source_label}      : {zip_path.name}")
            print(f"  {engine_label}      : {engine}")
            print(f"  {speed_label}    : {speed_text}")
            print(f"  {target_label}      : {target_lang}")
            print(f"  {files_label}        : {processing_text} {len(selected_filenames)} {_('file', 'files')}")
            print(f"  {output_label}      : {output_dir}")
            print(f"  {credit_label}      : {'✅ ' + yes_text if add_credit else '❌ ' + no_text}")
            print("=" * 70)
            
            confirm_prompt = _("\nMulai proses? (y/n/q): ", "\nStart processing? (y/n/q): ")
            confirm = input(confirm_prompt).strip().lower()
            if confirm != 'y':
                cancel_msg = _("❌ Dibatalkan", "❌ Cancelled")
                print(cancel_msg)
                return
            
            # Extract and process
            with tempfile.TemporaryDirectory() as temp_dir:
                extract_msg = _(f"📦 Mengekstrak {len(selected_filenames)} file...", f"📦 Extracting {len(selected_filenames)} files...")
                print(f"\n{extract_msg}")
                
                extracted_paths = []
                for filename in selected_filenames:
                    zf.extract(filename, temp_dir)
                    extracted_paths.append(Path(temp_dir) / filename)
                
                # Create translator
                if use_batch:
                    translator = BatchTranslatorWrapper(engine, target_lang)
                else:
                    translator = LineTranslatorWrapper(engine, target_lang)
                
                # Process files
                output_dir.mkdir(parents=True, exist_ok=True)
                
                stats.start()
                
                print(f"\n🚀 {_('Memulai terjemahan...', 'Starting translation...')}")
                print("=" * 70)
                
                for idx, file_path in enumerate(extracted_paths, 1):
                    print(f"\n📄 {_('Memproses file', 'Processing file')} {idx}/{len(extracted_paths)}: {file_path.name}")
                    
                    try:
                        # Determine output path
                        output_path = output_dir / f"{file_path.stem}.{target_lang}{file_path.suffix}"
                        
                        # Check if already exists
                        if output_path.exists():
                            overwrite = input(_(f"⚠️  File {output_path.name} sudah ada. Timpa? (y/n): ",
                                               f"⚠️  File {output_path.name} already exists. Overwrite? (y/n): ")).strip().lower()
                            if overwrite != 'y':
                                print(_("⏭️  Dilewati", "⏭️  Skipped"))
                                stats.skipped_count += 1
                                continue
                        
                        # Process based on file type - PERBAIKAN: tidak unpack NoneType
                        result_tuple = None
                        if file_path.suffix.lower() == '.srt':
                            if use_batch:
                                result_tuple = process_srt_file_batch(file_path, translator, output_path, batch_size, add_credit)
                            else:
                                result_tuple = process_srt_file_line(file_path, translator, output_path, add_credit)
                        else:  # .vtt or .ass
                            if use_batch:
                                result_tuple = process_ass_vtt_file_batch(file_path, translator, output_path, batch_size, add_credit)
                            else:
                                result_tuple = process_ass_vtt_file_line(file_path, translator, output_path, add_credit)
                        
                        # Handle return value
                        if result_tuple and len(result_tuple) >= 1:
                            status = result_tuple[0]
                        else:
                            status = "failed"
                            
                        if status == "success":
                            stats.success_count += 1
                        else:
                            stats.failed_count += 1
                        
                    except KeyboardInterrupt:
                        print(_("\n\n❌ Dibatalkan oleh pengguna", "\n\n❌ Cancelled by user"))
                        stats.stop()
                        stats.print_summary()
                        return
                    except Exception as e:
                        print(c(f"❌ {_('Gagal', 'Failed')}: {str(e)}", Colors.RED))
                        stats.failed_count += 1
                        with open("error_log.txt", "a", encoding="utf-8") as ef:
                            ef.write(f"[ERROR] file={file_path} error={str(e)}\n")
                            ef.write(f"{traceback.format_exc()}\n")
                
                stats.stop()
        
    except zipfile.BadZipFile:
        bad_zip_msg = _("❌ File ZIP rusak atau tidak valid", "❌ Bad or invalid ZIP file")
        print(c(bad_zip_msg, Colors.RED))
    except Exception as e:
        error_msg = _(f"❌ Error memproses ZIP: {e}", f"❌ Error processing ZIP: {e}")
        print(c(error_msg, Colors.RED))
        traceback.print_exc()


# ===============================================================
# MAIN TRANSLATION FLOW
# ===============================================================
def process_translation_flow():
    """Main translation workflow"""
    
    # Choose engine
    engine_prompt = _("🤖 Pilih mesin terjemah:", "🤖 Choose translation engine:")
    print(f"\n{engine_prompt}")
    print("  1. " + _("Google Translate (gratis, deteksi otomatis)", "Google Translate (free, auto-detect)"))
    print("  2. " + _("DeepL API (butuh API key)", "DeepL API (requires API key)"))
    print("  3. " + _("ChatGPT API (butuh API key)", "ChatGPT API (requires API key)"))
    print("  q. " + _("Keluar/Kembali", "Exit/Back"))
    engine_choice = input(_("Pilihan [1-3/q]: ", "Choice [1-3/q]: ")).strip() or "1"
    
    if engine_choice.lower() == 'q':
        return
    
    translator = None
    engine = "google"
    
    if engine_choice == "3":
        engine = "chatgpt"
        api_key = os.getenv("OPENAI_API_KEY", "")
        if not api_key:
            api_prompt = _("\n🔑 API Key ChatGPT tidak ditemukan di environment variable.", 
                   "\n🔑 ChatGPT API Key not found in environment variable.")
            print(api_prompt)
            api_input = input(_("Masukkan OpenAI API Key (atau q untuk keluar): ", "Enter OpenAI API Key (or q to exit): ")).strip()
            if api_input.lower() == 'q':
                return
            api_key = api_input
            if not api_key:
                no_key_msg = _("❌ API Key diperlukan untuk ChatGPT!", "❌ API Key required for ChatGPT!")
                print(no_key_msg)
                return
        
        model_prompt = _("\n📦 Pilih model ChatGPT:", "\n📦 Choose ChatGPT model:")
        print(model_prompt)
        print("  1. gpt-3.5-turbo " + _("(lebih murah, cepat)", "(cheaper, faster)"))
        print("  2. gpt-4 " + _("(lebih akurat, lebih mahal)", "(more accurate, expensive)"))
        print("  3. gpt-4-turbo " + _("(balance)", "(balance)"))
        print("  q. " + _("Keluar/Kembali", "Exit/Back"))
        model_choice = input(_("Pilihan [1-3/q] (default 1): ", "Choice [1-3/q] (default 1): ")).strip() or "1"
        
        if model_choice.lower() == 'q':
            return
        
        model_map = {
            "1": "gpt-3.5-turbo",
            "2": "gpt-4",
            "3": "gpt-4-turbo-preview"
        }
        model = model_map.get(model_choice, "gpt-3.5-turbo")
        
    elif engine_choice == "2":
        engine = "deepl"
    else:
        engine = "google"
    
    # Choose source - TAMBAHKAN OPSI MULTIPLE FOLDER
    source_prompt = _("\n📂 Pilih sumber subtitle:", "\n📂 Choose subtitle source:")
    print(source_prompt)
    print("  1. " + _("Jelajahi folder", "Browse folder"))
    print("  2. " + _("Folder saat ini", "Current folder"))
    print("  3. " + _("Pilih multiple folder", "Select multiple folders"))  # OPSI BARU
    print("  q. " + _("Keluar/Kembali", "Exit/Back"))
    folder_choice = input(_("Pilihan [1-3/q]: ", "Choice [1-3/q]: ")).strip() or "1"
    
    if folder_choice.lower() == 'q':
        return
    
    # Initialize stats
    stats = ProcessStats()
    
    if folder_choice == "3":
        # OPSI MULTIPLE FOLDER BARU
        folders = browse_folders_multiple(Path.cwd())
        if folders:
            process_multiple_folders_interactive(folders, engine, stats)
            stats.print_summary()
        return
    elif folder_choice == "1":
        source_path = browse_item_interactive()
        if not source_path:
            cancel_msg = _("❌ Dibatalkan", "❌ Cancelled")
            print(cancel_msg)
            return
    else:
        source_path = Path.cwd()
    
    # Find files
    if source_path.is_file():
        if source_path.suffix.lower() == '.zip':
            # Handle ZIP file - stats passed as parameter
            process_zip_interactive(source_path, engine, stats)
            stats.print_summary()
            return
        files = [source_path]
    else:
        # Search for subtitle files
        patterns = ['*.srt', '*.vtt', '*.ass']
        files = []
        for pattern in patterns:
            files.extend(source_path.glob(pattern))
        
        if not files:
            no_files_msg = _("❌ Tidak ada file subtitle ditemukan!", "❌ No subtitle files found!")
            print(c(no_files_msg, Colors.RED))
            return
    
    # Select files
    selected_files = select_files_interactive(files)
    if not selected_files:
        no_select_msg = _("❌ Tidak ada file dipilih", "❌ No files selected")
        print(no_select_msg)
        return
    
    # Choose output location
    output_prompt = _("\n📂 Pilih lokasi output:", "\n📂 Choose output location:")
    print(output_prompt)
    print("  1. " + _("Buat subfolder baru (Anda bisa beri nama)", "Create a new subfolder (You can name it)"))
    print("  2. " + _("Folder yang sama dengan file asli", "Same folder as original files"))
    print("  q. " + _("Keluar/Kembali", "Exit/Back"))
    output_choice = input(_("Pilihan [1-2/q] (default 1): ", "Choice [1-2/q] (default 1): ")).strip() or "1"
    
    if output_choice.lower() == 'q':
        return
    
    if output_choice == "1":
        folder_name = input(_("Nama subfolder (default: translated): ", "Subfolder name (default: translated): ")).strip() or "translated"
        output_dir = source_path if source_path.is_dir() else source_path.parent
        output_dir = output_dir / folder_name
        output_dir.mkdir(exist_ok=True)
    else:
        output_dir = None
    
    # Choose speed mode
    speed_prompt = _("\n⚙️ Pilih 'Processing Engine' (Kecepatan):", "\n⚙️ Choose 'Processing Engine' (Speed):")
    print(speed_prompt)
    print("  1. " + _("Aman (Lambat)", "Safe (Slow)"))
    print("  2. " + _("Standard (Cepat / Direkomendasikan)", "Standard (Fast / Recommended)"))
    print("  3. " + _("Aggressive (Sangat Cepat)", "Aggressive (Very Fast)"))
    print("  q. " + _("Keluar/Kembali", "Exit/Back"))
    speed_choice = input(_("Pilihan [1-3/q] (default 2): ", "Choice [1-3/q] (default 2): ")).strip() or "2"
    
    if speed_choice.lower() == 'q':
        return
    
    batch_size = 1
    use_batch = False
    
    if speed_choice == "1":
        use_batch = False
    elif speed_choice == "3":
        use_batch = True
        batch_size = 100
    else:  # 2
        use_batch = True
        batch_size = 50
    
    # Choose target language
    lang_prompt = _("🎯 Bahasa target (default: id, atau q untuk keluar): ", "🎯 Target language (default: id, or q to exit): ")
    target_lang = input(lang_prompt).strip() or "id"
    
    if target_lang.lower() == 'q':
        return
    
    # Add credits?
    credit_prompt = _("🎬 Tambahkan kredit pembuat di awal? (y/n/q default y): ", 
                     "🎬 Add creator credit at the beginning? (y/n/q default y): ")
    add_credit_input = input(credit_prompt).strip().lower()
    
    if add_credit_input == 'q':
        return
    
    add_credit = add_credit_input != 'n'
    
    # Confirmation
    print("\n" + "✨" * 30)
    summary_text = _("        RINGKASAN KONFIRMASI", "        CONFIRMATION SUMMARY")
    print(c(summary_text, Colors.BOLD + Colors.CYAN))
    print("✨" * 30)
    
    source_label = _("Sumber", "Source")
    engine_label = _("Mesin", "Engine")
    speed_label = _("Kecepatan", "Speed")
    target_label = _("Target", "Target")
    files_label = _("File", "Files")
    output_label = _("Output", "Output")
    credit_label = _("Kredit", "Credit")
    
    speed_text = _('Aman' if not use_batch else ('Cepat' if batch_size == 50 else 'Aggressive'), 
                   'Safe' if not use_batch else ('Fast' if batch_size == 50 else 'Aggressive'))
    processing_text = _("Memproses", "Processing")
    same_folder_text = _("Folder yang sama", "Same folder")
    yes_text = _("Ya", "Yes")
    no_text = _("Tidak", "No")
    
    print(f"  {source_label}      : {source_path}")
    print(f"  {engine_label}      : {engine}")
    print(f"  {speed_label}    : {speed_text}")
    print(f"  {target_label}      : {target_lang}")
    print(f"  {files_label}        : {processing_text} {len(selected_files)} {_('file', 'files')}")
    print(f"  {output_label}      : {output_dir if output_dir else same_folder_text}")
    print(f"  {credit_label}      : {'✅ ' + yes_text if add_credit else '❌ ' + no_text}")
    print("=" * 70)
    
    confirm_prompt = _("\nMulai proses? (y/n/q): ", "\nStart processing? (y/n/q): ")
    confirm = input(confirm_prompt).strip().lower()
    if confirm != 'y':
        cancel_msg = _("❌ Dibatalkan", "❌ Cancelled")
        print(cancel_msg)
        return
    
    # Create translator
    if engine == "chatgpt":
        if use_batch:
            translator = ChatGPTTranslator(api_key, target_lang, model)
        else:
            translator = ChatGPTTranslator(api_key, target_lang, model)
    else:
        if use_batch:
            translator = BatchTranslatorWrapper(engine, target_lang)
        else:
            translator = LineTranslatorWrapper(engine, target_lang)
    
    # Process files
    stats = ProcessStats()
    stats.start()
    
    print(f"\n🚀 {_('Memulai terjemahan...', 'Starting translation...')}")
    print("=" * 70)
    
    for idx, file_path in enumerate(selected_files, 1):
        print(f"\n📄 {_('Memproses file', 'Processing file')} {idx}/{len(selected_files)}: {file_path.name}")
        
        try:
            # Determine output path
            if output_dir:
                output_path = output_dir / f"{file_path.stem}.{target_lang}{file_path.suffix}"
            else:
                output_path = file_path.parent / f"{file_path.stem}.{target_lang}{file_path.suffix}"
            
            # Check if already exists
            if output_path.exists():
                overwrite = input(_(f"⚠️  File {output_path.name} sudah ada. Timpa? (y/n): ",
                                   f"⚠️  File {output_path.name} already exists. Overwrite? (y/n): ")).strip().lower()
                if overwrite != 'y':
                    print(_("⏭️  Dilewati", "⏭️  Skipped"))
                    stats.skipped_count += 1
                    continue
            
            # Process based on file type - PERBAIKAN: tidak unpack NoneType
            result_tuple = None
            if file_path.suffix.lower() == '.srt':
                if use_batch:
                    result_tuple = process_srt_file_batch(file_path, translator, output_path, batch_size, add_credit)
                else:
                    result_tuple = process_srt_file_line(file_path, translator, output_path, add_credit)
            else:  # .vtt or .ass
                if use_batch:
                    result_tuple = process_ass_vtt_file_batch(file_path, translator, output_path, batch_size, add_credit)
                else:
                    result_tuple = process_ass_vtt_file_line(file_path, translator, output_path, add_credit)
            
            # Handle return value
            if result_tuple and len(result_tuple) >= 1:
                status = result_tuple[0]
            else:
                status = "failed"
                
            if status == "success":
                print(c(f"✅ {_('Disimpan', 'Saved')}: {output_path.name}", Colors.GREEN))
                stats.success_count += 1
            else:
                stats.failed_count += 1
            
        except KeyboardInterrupt:
            print(_("\n\n❌ Dibatalkan oleh pengguna", "\n\n❌ Cancelled by user"))
            stats.stop()
            stats.print_summary()
            return
        except Exception as e:
            print(c(f"❌ {_('Gagal', 'Failed')}: {str(e)}", Colors.RED))
            stats.failed_count += 1
            with open("error_log.txt", "a", encoding="utf-8") as ef:
                ef.write(f"[ERROR] file={file_path} error={str(e)}\n")
                ef.write(f"{traceback.format_exc()}\n")
    
    stats.stop()
    stats.print_summary()


# ===============================================================
# INTERACTIVE MENU
# ===============================================================
def interactive_menu():
    """Main interactive menu"""
    global LANG_UI
    
    while True:
        print("\n" + "=" * 70)
        print(c("╔═══════════════════════════════════════════╗", Colors.CYAN))
        print(c("║        ZEE SUBTITLE TRANSLATOR v1.1       ║", Colors.CYAN))
        print(c("╚═══════════════════════════════════════════╝", Colors.CYAN))
        print("\n" + _("Selamat datang!", "Welcome!"))
        print("-" * 70)
        print("1. " + _("Terjemahkan Subtitle", "Translate Subtitles"))
        print("2. " + _("Pengaturan Bahasa UI", "UI Language Settings"))
        print("3. " + _("Keluar", "Exit"))
        print("-" * 70)
        
        choice = input(_("Pilihan [1-3]: ", "Choice [1-3]: ")).strip()
        
        if choice == "1":
            try:
                process_translation_flow()
            except Exception as e:
                print(c(_("❌ Terjadi kesalahan:", "❌ An error occurred:"), Colors.RED))
                print(f"{type(e).__name__}: {str(e)}")
                print("\n" + c("Full traceback:", Colors.YELLOW))
                traceback.print_exc()
                with open("error_log.txt", "a", encoding="utf-8") as ef:
                    ef.write(f"[MENU_ERROR] {traceback.format_exc()}\n")
        elif choice == "2":
            change_ui_language()
        elif choice == "3":
            print(_("\n👋 Terima kasih telah menggunakan Zee Subtitle Translator!", 
                   "\n👋 Thank you for using Zee Subtitle Translator!"))
            sys.exit(0)
        else:
            print(c(_("❌ Pilihan tidak valid!", "❌ Invalid choice!"), Colors.RED))


def change_ui_language():
    """Change UI language"""
    global LANG_UI
    
    print("\n" + "-" * 70)
    print(_("🌐 Pilih bahasa UI:", "🌐 Choose UI language:"))
    print("  1. Bahasa Indonesia")
    print("  2. English")
    print("-" * 70)
    
    choice = input(_("Pilihan [1-2]: ", "Choice [1-2]: ")).strip()
    
    if choice == "1":
        LANG_UI = "ID"
        print(c("✅ Bahasa UI diubah ke: Bahasa Indonesia", Colors.GREEN))
    elif choice == "2":
        LANG_UI = "EN"
        print(c("✅ UI language changed to: English", Colors.GREEN))
    else:
        print(c(_("❌ Pilihan tidak valid!", "❌ Invalid choice!"), Colors.RED))
        return
    
    # Save to config
    try:
        CONFIG_FILE.write_text(f"LANG_UI={LANG_UI}\n", encoding="utf-8")
        print(c(_("💾 Pengaturan disimpan", "💾 Settings saved"), Colors.GREEN))
    except Exception as e:
        print(c(_(f"⚠️  Gagal menyimpan pengaturan: {e}", f"⚠️  Failed to save settings: {e}"), Colors.YELLOW))


# ===============================================================
# MAIN ENTRY POINT
# ===============================================================
def main():
    """Main entry point"""
    try:
        interactive_menu()
    except KeyboardInterrupt:
        print("\n" + _("👋 Dibatalkan oleh pengguna", "👋 Cancelled by user"))
        sys.exit(0)
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[FATAL] {traceback.format_exc()}\n")
        print(c(_("❌ Terjadi kesalahan tak terduga", "❌ Unexpected error occurred"), Colors.RED))
        print(str(e))
        print(_("\n💡 Error telah disimpan di error_log.txt", "\n💡 Error saved to error_log.txt"))
        sys.exit(1)


if __name__ == "__main__":
    main()