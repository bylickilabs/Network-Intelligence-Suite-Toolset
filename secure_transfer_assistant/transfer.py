
import socket
import threading
import os
import tempfile

def start_receiver():
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
        print(f"[✓] File received and saved to: {output_path}")
    threading.Thread(target=handle, daemon=True).start()

def send_file(path, ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, 8080))
        with open(path, "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                s.sendall(data)
