# Keylogger — Windows Keystroke Capture & Exfiltration Demo

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A Python-based keylogger built to demonstrate how keystroke capture and data exfiltration work at a technical level. Written for malware research, security awareness training, and understanding attacker techniques in controlled lab environments.

> ⚠️ **Authorized use only.** Running this on any system without explicit written consent is illegal. This is a research and education tool — treat it accordingly.

---

## What It Does

- Captures all keystrokes using `pynput`
- Stores logs in an obfuscated temp file with a randomized filename
- Encodes logs in base64 and exfiltrates via Gmail SMTP on a randomized timer (200–450s)
- Displays a decoy image on launch while running silently in the background
- Can be compiled to a standalone `.exe` with PyInstaller for lab deployment testing

---

## Technical Overview

| Component | Implementation |
|---|---|
| Keystroke capture | `pynput.keyboard.Listener` |
| Log storage | Randomized `.dat` file in `%TEMP%` |
| Encoding | Base64 via `base64` module |
| Exfiltration | SMTP over Gmail with App Password auth |
| Persistence trigger | Background thread, timer-based flush |
| Decoy | `PIL.Image` display on launch |

---

## Setup

```bash
git clone https://github.com/Dawn-Fighter/Keylogger.git
cd Keylogger
pip install pynput pillow
```

### Configure Email Exfiltration

Open `keylogger.py` and set your credentials in the `tx()` function:

```python
s  = "sender@gmail.com"         # sending address
r  = "receiver@gmail.com"       # receiving address
pw = "xxxx xxxx xxxx xxxx"      # Gmail App Password (not your main password)
```

To get a Gmail App Password: Google Account → Security → 2-Step Verification → App Passwords.

### Add Decoy Image

Place any image as `walpaper.jpg` in the same directory as `main.py`, or update the filename in the script.

---

## Usage

```bash
# Run directly
python main.py
```

Decoy image flashes briefly, then the logger runs silently. Logs are flushed and emailed every 200–450 seconds. Kill via Task Manager or `Ctrl+C`.

### Build as Executable (Lab Testing)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "walpaper.jpg;." keylogger.py
```

Output lands in `dist/`. Add `--icon=youricon.ico` to set a custom icon for social engineering simulations.

---

## Decoding Captured Logs

Exfiltrated `.dat` attachments are base64-encoded. Decode with:

```bash
# Windows
certutil -decode yourfile.dat output.txt

# Linux / macOS
base64 -d yourfile.dat > output.txt
```

---

## Detection

Modern AV and EDR solutions will flag this. Tested detections include:

- Windows Defender — flags on `pynput` listener pattern
- Process behavior monitoring — catches SMTP calls from non-browser processes
- Network-level — SMTP traffic from endpoints without mail clients

This is intentional — part of the educational value is understanding *why* and *how* it gets caught.

---

## Disclaimer

Built for malware analysis, blue team training, and understanding offensive techniques. Only deploy in isolated lab environments on systems you own or have written authorization to test. The author assumes no responsibility for misuse.

---

## Author

**Chethas Dileep** — Penetration Tester & Security Developer

[![GitHub](https://img.shields.io/badge/GitHub-Dawn--Fighter-181717?style=flat-square&logo=github)](https://github.com/Dawn-Fighter)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-chethas--dileep-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/chethas-dileep-530722211)
[![Portfolio](https://img.shields.io/badge/Portfolio-edneam.site-FF4500?style=flat-square&logo=firefox)](http://www.edneam.site)
