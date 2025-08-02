
import qrcode
import os
import tempfile
import webbrowser

def generate_qr(data):
    img = qrcode.make(data)
    temp_path = os.path.join(tempfile.gettempdir(), "qr_link.png")
    img.save(temp_path)
    print(f"[✓] QR code saved to: {temp_path}")
    webbrowser.open(temp_path)
