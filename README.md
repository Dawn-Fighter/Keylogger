# Keylogger
This repository contains a simple Python-based keylogger for Windows. It captures keystrokes, logs them to a hidden temporary file, and periodically emails the log using a Gmail account and app password.

# Python Keylogger for Windows (Educational Purposes Only)

> **Warning**:  
> This project is for **EDUCATIONAL USE ONLY** and must **never be used without the explicit, informed consent of all users of the target machine**. Unauthorized use of keyloggers is illegal in most jurisdictions and can lead to criminal prosecution. Always use responsibly and ethically.

---

## Overview

This repository contains a simple Python-based keylogger for Windows. It captures keystrokes, logs them to a hidden temporary file, and periodically emails the log using a Gmail account and app password.

This tool demonstrates concepts like keyboard event listening, file handling, and secure email transmission in Python.

---

## Features

- Logs all keystrokes made on the system.
- Stores key logs in a hidden file in a random temp directory.
- Periodically emails logs to a specified address via Gmail’s SMTP server.
- Script obfuscation via base64 strings.
- Runs silently (without visible console window).

---

## Setup Instructions

### Prerequisites

- **Python 3.x** installed on your Windows machine.
- **pip** to install Python packages.

### Required Python Libraries

pip install pynput

### 2. (Optional) If converting to .exe, install PyInstaller


---

## Gmail App Password Setup

*Due to Google security features, you must use a Gmail app password (not your main password).*

1. Go to your [Google Account Security page](https://myaccount.google.com/security).
2. Enable **2-Step Verification** if not already turned on.
3. Go to the **App passwords** section.
4. Choose **Mail** as the app, and **Windows Computer** for the device.
5. Generate and copy the 16-character password.
6. You will use this password in the script.

*Never share or publish your app password!*

---

## Configuration

Edit the following values in `keylogger.py`:


**Change:**  
- `sender` to your Gmail address  
- `receiver` to the address that should receive logs  
- `auth` to your Gmail app password

---

## Usage

### Run the script


- The script captures keystrokes in the background and sends them at set intervals (default: ~8 minutes).
- By default, the window is hidden (no visible console).
- To stop: open Task Manager and terminate the Python process.

---

### Build a Windows Executable (.exe)

You can run without needing Python installed on target machines.

1. In your project folder, run:
pyinstaller --onefile --windowed keylogger.py


2. The resulting `.exe` will appear in the `dist` subfolder.
3. Double-click the `.exe` to run it (it runs silently).
4. **Note:** Most antivirus software will flag and potentially block/delete keylogger executables for security reasons.

---

## Customization

- **Change log email interval:**  
  Edit the second argument in the `time.sleep()` call in the script.  
  E.g., `time.sleep(300)` for 5 minutes.

- **Change log file location/obfuscation:**  
  Adjust file path/code if more advanced stealth is needed (for learning purposes only).

---

## Legal and Ethical Notice

**DO NOT** use this software for any real-world or unauthorized surveillance.  
Keyloggers are considered malicious in most contexts and their use is covered by computer misuse and privacy laws.  
Use only on computers you own or with clear, explicit, informed permission from all users.

Violators may be subject to administrative, civil, and/or criminal penalties.

---


---

## Disclaimer

**This repository is strictly for educational, ethical, and research purposes only. The author accepts no responsibility for any damage or legal consequences resulting from the misuse of this software.**  
**By using or modifying this project, you accept full responsibility for compliance with all applicable laws and regulations.**








