
import os
import socket
import threading
import tempfile
import hashlib
import secrets
import string
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import qrcode
import webbrowser

class SecureTransferApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure File Transfer Assistant")
        self.geometry("750x520")
        self.selected_file = None
        self.key = tk.StringVar()
        self.ip_address = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(self, padding=10)
        frm.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frm, text="Encryption Key (32 characters):").pack(anchor="w")
        ttk.Entry(frm, textvariable=self.key, width=64).pack(fill=tk.X, pady=5)

        ttk.Button(frm, text="Generate Random Key", command=self.generate_key).pack(fill=tk.X, pady=5)
        ttk.Button(frm, text="Select File to Send", command=self.select_file).pack(fill=tk.X, pady=5)
        ttk.Button(frm, text="Encrypt & Send File", command=self.encrypt_and_send).pack(fill=tk.X, pady=5)

        ttk.Label(frm, text="Send to IP:").pack(anchor="w", pady=(10, 0))
        ttk.Entry(frm, textvariable=self.ip_address).pack(fill=tk.X, pady=5)

        ttk.Button(frm, text="Start Receiver", command=self.start_receiver_gui).pack(fill=tk.X, pady=5)
        ttk.Button(frm, text="Generate QR Code (Localhost)", command=self.generate_qr_link).pack(fill=tk.X, pady=5)

        ttk.Separator(frm).pack(fill=tk.X, pady=10)

        ttk.Button(frm, text="Decrypt Received File", command=self.decrypt_received).pack(fill=tk.X, pady=5)

        self.status = ttk.Label(frm, text="Status: Ready")
        self.status.pack(anchor="w", pady=(10, 0))

    def generate_key(self):
        chars = string.ascii_letters + string.digits
        self.key.set(''.join(secrets.choice(chars) for _ in range(32)))
        self.status.config(text="Generated random encryption key.")

    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.selected_file = path
            self.status.config(text=f"Selected: {os.path.basename(path)}")

    def encrypt_and_send(self):
        key = self.key.get().strip()
        ip = self.ip_address.get().strip()
        if not self.selected_file or not key or len(key) != 32 or not ip:
            messagebox.showerror("Error", "Check file, key (32 chars), and IP address.")
            return
        try:
            output = self.selected_file + ".enc"
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            with open(self.selected_file, "rb") as f_in, open(output, "wb") as f_out:
                f_out.write(iv)
                f_out.write(encryptor.update(f_in.read()) + encryptor.finalize())
            sha256 = hashlib.sha256(open(output, "rb").read()).hexdigest()
            self.send_file(output, ip)
            self.status.config(text=f"File sent. SHA256: {sha256}")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption/Transfer failed: {e}")

    def send_file(self, path, ip):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, 8080))
            with open(path, "rb") as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    s.sendall(data)

    def start_receiver_gui(self):
        self.status.config(text="Receiver started on port 8080")
        def handle():
            output_path = os.path.join(tempfile.gettempdir(), "received_file.enc")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("0.0.0.0", 8080))
                s.listen(1)
                conn, addr = s.accept()
                with conn, open(output_path, "wb") as f:
                    while True:
                        data = conn.recv(4096)
                        if not data:
                            break
                        f.write(data)
            print(f"[✓] Received file saved to: {output_path}")
            self.status.config(text="File received. Ready to decrypt.")
        threading.Thread(target=handle, daemon=True).start()

    def generate_qr_link(self):
        qr_img = qrcode.make("http://127.0.0.1:8080")
        qr_path = os.path.join(tempfile.gettempdir(), "qr_link.png")
        qr_img.save(qr_path)
        webbrowser.open(qr_path)
        self.status.config(text=f"QR Code saved: {qr_path}")

    def decrypt_received(self):
        key = self.key.get().strip()
        input_path = os.path.join(tempfile.gettempdir(), "received_file.enc")
        if not key or len(key) != 32:
            messagebox.showerror("Error", "Enter a valid 32-character key.")
            return
        if not os.path.exists(input_path):
            messagebox.showerror("Error", "No received file found in temp directory.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".dec", filetypes=[("Decrypted Files", "*.dec")])
        if not output_path:
            return
        try:
            with open(input_path, "rb") as f_in:
                iv = f_in.read(16)
                cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=default_backend())
                decryptor = cipher.decryptor()
                data = decryptor.update(f_in.read()) + decryptor.finalize()
                with open(output_path, "wb") as f_out:
                    f_out.write(data)
            self.status.config(text=f"Decrypted and saved to: {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")

if __name__ == "__main__":
    app = SecureTransferApp()
    app.mainloop()
