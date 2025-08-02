
import psutil
import socket
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class PortMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Port Monitor")
        self.geometry("700x500")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.active_ports = set()
        self.running = True
        self.create_widgets()
        self.monitor_thread = threading.Thread(target=self.monitor_ports, daemon=True)
        self.monitor_thread.start()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame, columns=("Port", "Status", "Timestamp"), show="headings")
        self.tree.heading("Port", text="Port")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.status_label = ttk.Label(frame, text="Monitoring open ports...", anchor="w")
        self.status_label.pack(fill=tk.X, pady=5)

    def monitor_ports(self):
        while self.running:
            try:
                current_ports = self.get_open_ports()
                added_ports = current_ports - self.active_ports
                removed_ports = self.active_ports - current_ports

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                for port in added_ports:
                    self.log_change(port, "Opened", timestamp)

                for port in removed_ports:
                    self.log_change(port, "Closed", timestamp)

                self.active_ports = current_ports
                time.sleep(5)
            except Exception as e:
                print(f"[Error] Monitoring failed: {e}")

    def get_open_ports(self):
        ports = set()
        for conn in psutil.net_connections(kind="inet"):
            if conn.status == psutil.CONN_LISTEN and conn.laddr:
                ports.add(conn.laddr.port)
        return ports

    def log_change(self, port, status, timestamp):
        self.tree.insert("", tk.END, values=(port, status, timestamp))
        self.status_label.config(text=f"Port {port} {status.lower()} at {timestamp}")

    def on_close(self):
        self.running = False
        self.destroy()

if __name__ == "__main__":
    app = PortMonitorApp()
    app.mainloop()
