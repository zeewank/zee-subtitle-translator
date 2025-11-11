# 📖 Detailed Usage Guide

This guide covers all features and usage scenarios for Zee Subtitle Translator.

## Table of Contents
- [Basic Workflow](#basic-workflow)
- [Translation Modes](#translation-modes)
- [Multiple Folder Selection](#multiple-folder-selection)
- [Output Options](#output-options)
- [Advanced Features](#advanced-features)
- [Tips & Tricks](#tips--tricks)
- [Troubleshooting](#troubleshooting)

## Basic Workflow

### Simple Translation

```bash
# Start the program
./zee_translator.py

# Follow the prompts:
# 1. Choose translation engine (Google/DeepL)
# 2. Select subtitle source
# 3. Choose files to translate
# 4. Select output location
# 5. Choose translation speed
# 6. Set target language
# 7. Enable/disable credits
# 8. Confirm and start
```

### Direct Path Input

```bash
# Translate specific folder
./zee_translator.py /path/to/subtitles/

# Translate ZIP file
./zee_translator.py /path/to/subtitles.zip
```

## Translation Modes

### 1. Safe Mode (Line-by-Line)

**When to use:**
- First-time translation of important files
- Files with complex formatting
- When stability is priority over speed
- Troubleshooting translation issues

**Characteristics:**
- Translates one line at a time
- Slowest but most reliable
- Best error recovery
- ~2-3 minutes per file

**Example:**
```
Speed Choice: 1

Processing: movie.srt
Progress: |████████████████████| 450/450 lines
✅ Saved: movie.id.srt
```

### 2. Standard Mode (Recommended)

**When to use:**
- Regular translation tasks
- Balanced speed and reliability
- Most file types and sizes
- Default choice for most users

**Characteristics:**
- Translates 50 lines per batch
- Good speed/stability balance
- Handles most edge cases
- ~1-2 minutes per file

**Example:**
```
Speed Choice: 2

Processing: episode01.srt
Progress: |████████████████████| 9/9 batches
✅ Saved: episode01.id.srt
```

### 3. Aggressive Mode

**When to use:**
- Large batch jobs (>20 files)
- Stable network connection
- Less critical content
- When speed is priority

**Characteristics:**
- Translates 100 lines per batch
- Fastest mode
- May trigger rate limits
- ~30-45 seconds per file

**Warning:** May get blocked if overused.

## Multiple Folder Selection

### Navigation Commands

| Command | Action | Example |
|---------|--------|---------|
| `14` | Open/browse folder 14 | Opens Downloads folder |
| `s14` | Select folder 14 without opening | Adds folder to selection |
| `u1` | Remove folder 1 from selection | Removes from list |
| `.` | Select current folder | Adds pwd to selection |
| `0` | Finish and proceed | Starts processing |
| `q` | Cancel selection | Returns to menu |

### Workflow Example

**Scenario:** Translate Season 1 and Season 2 from different locations

```bash
# Start program
./zee_translator.py

# Choose: 3. Select multiple folders

# Navigate to Season 1
Current: /home/user
> 14           # Open Downloads
> s5           # Select "TV Show S01" folder
✅ Added: TV Show S01

# Navigate to Season 2
> 24           # Go to parent
> 13           # Open Documents
> s8           # Select "TV Show S02" folder
✅ Added: TV Show S02

# Finish
> 0            # Start processing

📁 Selected folders:
  [1] /home/user/Downloads/TV Show S01
  [2] /home/user/Documents/TV Show S02
```

### Visual Indicators

```
📂 Folder list:
  1) Archive/
  2) Movies/
  3) TV Shows/ ✓    ← Already selected
  4) Downloads/
```

## Output Options

### Single Folder Mode

**Option 1: New Subfolder**
```
Input:  /media/movies/subtitles/
Output: /media/movies/subtitles/translated/
```

**Option 2: Same Folder**
```
Input:  /media/movies/subtitles/movie.srt
Output: /media/movies/subtitles/movie.id.srt
```

### Multiple Folder Mode

**Option 1: Keep Structure (Recommended)**
```
Input:  /downloads/season1/ep01.srt
        /downloads/season2/ep01.srt
Output: /downloads/season1/ep01.id.srt
        /downloads/season2/ep01.id.srt
```

**Option 2: Merge to One Folder**
```
Input:  /downloads/season1/ep01.srt
        /downloads/season2/ep01.srt
Output: /downloads/translated/ep01.id.srt
        /downloads/translated/ep01.id.srt
```

⚠️ **Warning:** Option 2 may overwrite files with same names!

## Advanced Features

### Custom Credits

Add your signature to translated subtitles:

```
🎬 Add creator credit? (y/n): y

Result:
1
00:00:02,000 --> 00:00:07,000
Subtitle by Z33

2
00:00:10,000 --> 00:00:12,000
[Original subtitle text]
```

### Automatic Text Cleaning

Removes common noise automatically:

**Input:**
```
[MUSIC PLAYING]
(DOOR CREAKS)
<i>Internal thoughts</i>
{Translator note: Context}
```

**Output:**
```
[Empty - removed]
[Empty - removed]
Internal thoughts
Context
```

**Cleaned tags:**
- `[...]` - Sound effects
- `(...)` - Sound descriptions
- `<...>` - Formatting tags
- `{...}` - Notes

### Smart Name Detection

Proper names are NOT translated:

**Input:**
```
Hello, my name is McDonald.
Visit New York City.
Call 911!
```

**Output (to Indonesian):**
```
Halo, nama saya McDonald.
Kunjungi New York City.
Hubungi 911!
```

Names detected: `McDonald`, `New York City` (kept as-is)

### File Selection Patterns

**Select all:**
```
> 0
```

**Select specific:**
```
> 1, 5, 8, 12
```

**Select range:**
```
> 1-10
```

**Combined:**
```
> 1-5, 8, 12-15
```

## Tips & Tricks

### Faster Translation

1. **Use Standard mode** - Good balance
2. **Select fewer files** - Process in batches
3. **Stable connection** - Wired > WiFi
4. **Avoid peak hours** - Less API congestion

### Better Quality

1. **Use Safe mode** - More accurate
2. **Check sample first** - Test 1-2 files
3. **Review output** - Spot-check results
4. **Use DeepL** - Better quality (paid)

### Large Batches

1. **Split by folder** - Organize before translate
2. **Use Aggressive mode** - If you accept risks
3. **Process overnight** - For 100+ files
4. **Resume capability** - Skip existing `.id.srt`

### Organizing Output

**Before translation:**
```
/subtitles/
  ├── Season 1/
  ├── Season 2/
  └── Season 3/
```

**After translation (keep structure):**
```
/subtitles/
  ├── Season 1/
  │   ├── ep01.srt
  │   └── ep01.id.srt
  ├── Season 2/
  │   ├── ep01.srt
  │   └── ep01.id.srt
  └── Season 3/
      ├── ep01.srt
      └── ep01.id.srt
```

## Troubleshooting

### Slow Translation

**Problem:** Taking much longer than expected

**Solutions:**
1. Check internet speed
2. Switch to Safe mode
3. Reduce batch size
4. Try different time of day
5. Use VPN if region-blocked

### Garbled Output

**Problem:** Strange characters in translated files

**Solutions:**
1. Check input encoding (should auto-detect)
2. Convert source to UTF-8 first
3. Try Safe mode
4. Report as bug if persistent

### API Rate Limits

**Problem:** "Rate limit exceeded" or similar errors

**Solutions:**
1. Wait 1-2 hours
2. Switch to Safe mode (slower = less likely to hit limits)
3. Process smaller batches
4. Use DeepL API (paid, higher limits)
5. Use VPN to different region

### Files Not Found

**Problem:** "No subtitle files found"

**Solutions:**
1. Check file extensions (.srt, .vtt, .ass)
2. Enable recursive search
3. Check file permissions
4. Ensure files aren't hidden

### Translation Errors

**Problem:** Some lines failed to translate

**Solutions:**
1. Check `error_log.txt` for details
2. Retry failed files in Safe mode
3. Split very long lines manually
4. Report persistent errors

### Memory Issues

**Problem:** Program crashes on large files

**Solutions:**
1. Process files individually
2. Close other programs
3. Use Aggressive mode (less memory)
4. Split large files (<5000 lines each)

## Command Reference

### Main Menu
- `1` - Translate Subtitles
- `2` - UI Language Settings
- `3` - Exit

### Source Selection
- `1` - Browse folders/ZIP
- `2` - Current folder
- `3` - Multiple folders

### Output Selection
- `1` - New subfolder (custom name)
- `2` - Same as originals

### Speed Selection
- `1` - Safe (line-by-line)
- `2` - Standard (50/batch) ✅ Recommended
- `3` - Aggressive (100/batch)

---

**Need more help?** Open an issue on GitHub!
