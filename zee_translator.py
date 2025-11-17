#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zee Subtitle Translator v1.1
A powerful batch subtitle translator with multi-format support
Now with ChatGPT API support!

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
import json
import requests
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
# CHATGPT API WRAPPER
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
        
        # Prepare prompt
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
                    print(c(f"\n⚠️ {_('Rate limit terlampaui, menunggu...', 'Rate limit exceeded, waiting...')}", Colors.YELLOW))
                    time.sleep(2 ** attempt)
                else:
                    print(c(f"\n⚠️ API Error: {response.status_code}", Colors.YELLOW))
                    last_exc = Exception(f"API returned {response.status_code}")
                    
            except requests.exceptions.Timeout:
                print(c(f"\n⚠️ {_('Timeout, mencoba lagi...', 'Timeout, retrying...')}", Colors.YELLOW))
                last_exc = Exception("Timeout")
            except Exception as e:
                last_exc = e
                if desc:
                    print(_(f"⚠️ Gagal '{desc[:30]}...', mencoba lagi ({attempt + 1})",
                           f"⚠️ Failed '{desc[:30]}...', retry ({attempt + 1})"))
                time.sleep(1)
        
        print(_(f"❌ Gagal permanen: {txt[:50]}", f"❌ Permanent fail: {txt[:50]}"))
        with open("error_log.txt", "a", encoding="utf-8") as ef:
            ef.write(f"[CHATGPT_FAIL] text={txt[:120]} err={repr(last_exc)}\n")
        return txt
    
    def translate_batch(self, texts: List[str]) -> List[str]:
        """Translate batch of texts"""
        if not texts:
            return []
        
        # ChatGPT works better with smaller batches
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
                
                # Clean translations
                translations = [t.strip() for t in translations]
                
                if len(translations) == len(texts):
                    return translations
                else:
                    print(c(f"\n⚠️ {_('Batch mismatch, fallback ke line-by-line', 'Batch mismatch, fallback to line-by-line')}", Colors.YELLOW))
                    return [self.translate(t) for t in texts]
            else:
                print(c(f"\n⚠️ API Error: {response.status_code}, fallback", Colors.YELLOW))
                return [self.translate(t) for t in texts]
                
        except Exception as e:
            print(c(f"\n⚠️ Batch failed: {e}, fallback", Colors.YELLOW))
            return [self.translate(t) for t in texts]


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
# FUNGSI PEMBERSIHAN TEKS
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

# 2. Wrapper "FAST" (Batch)
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

# NOTE: Fungsi-fungsi lainnya tetap sama seperti di zee_translator.py original
# Saya tidak copy semuanya di sini untuk menghemat space
# Termasuk: browse_folders_multiple, browse_item_interactive, select_files_interactive,
# process_srt_file_line, process_ass_vtt_file_line, process_srt_file_batch, 
# process_ass_vtt_file_batch, dll.

# ===============================================================
# MENU UTAMA YANG DIUPDATE
# ===============================================================

def process_translation_flow():
    print(_("\n🤖 Pilih mesin terjemah:", "\n🤖 Choose translation engine:"))
    print("  1. " + _("Google Translate (gratis, deteksi otomatis)", "Google Translate (free, auto-detect)"))
    print("  2. " + _("DeepL API (butuh API key)", "DeepL API (requires API key)"))
    print("  3. " + _("ChatGPT API (butuh API key)", "ChatGPT API (requires API key)"))
    engine_choice = input(_("Pilihan [1-3]: ", "Choice [1-3]: ")).strip() or "1"
    
    if engine_choice == "3":
        engine = "chatgpt"
        # Get API key
        api_key = os.getenv("OPENAI_API_KEY", "")
        if not api_key:
            print(_("\n🔑 API Key ChatGPT tidak ditemukan di environment variable.", 
                   "\n🔑 ChatGPT API Key not found in environment variable."))
            api_key = input(_("Masukkan OpenAI API Key: ", "Enter OpenAI API Key: ")).strip()
            if not api_key:
                print(_("❌ API Key diperlukan untuk ChatGPT!", "❌ API Key required for ChatGPT!"))
                return
        
        # Choose model
        print(_("\n📦 Pilih model ChatGPT:", "\n📦 Choose ChatGPT model:"))
        print("  1. gpt-3.5-turbo (lebih murah, cepat)")
        print("  2. gpt-4 (lebih akurat, lebih mahal)")
        print("  3. gpt-4-turbo (balance)")
        model_choice = input(_("Pilihan [1-3] (default 1): ", "Choice [1-3] (default 1): ")).strip() or "1"
        
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
    
    # Rest of the translation flow...
    # (Kode sisa nya sama seperti process_translation_flow original)
    
    print(_("\n📂 Pilih sumber subtitle:", "\n📂 Choose subtitle source:"))
    print("  1. " + _("Jelajahi folder / file .zip", "Browse folder / .zip file"))
    print("  2. " + _("Folder saat ini", "Current folder"))
    print("  3. " + _("Pilih multiple folder", "Select multiple folders"))
    folder_choice = input(_("Pilihan [1-3]: ", "Choice [1-3]: ")).strip() or "1"
    
    # ... (sisanya sama)
    
def main():
    try:
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
