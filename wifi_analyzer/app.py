import tkinter as tk
from tkinter import ttk, messagebox
import pywifi
import subprocess
from visualizer import plot_channel_usage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import logging
import traceback

logging.basicConfig(filename="error.log", level=logging.ERROR)

def get_connected_network_info():
    ssid = bssid = None
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True, encoding="utf-8", shell=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if line.strip().startswith("SSID") and "BSSID" not in line:
                ssid = line.split(":",1)[1].strip()
            if line.strip().startswith("BSSID"):
                bssid = line.split(":",1)[1].strip()
    except Exception:
        pass
    return ssid, bssid

def scan_wifi_networks():
    try:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        import time
        time.sleep(1.5)
        results = iface.scan_results()
        networks = []
        for net in results:
            info = {
                "SSID": net.ssid,
                "BSSID": net.bssid,
                "Signal": net.signal,
                "Frequency": net.freq,
                "Channel": "?",
            }
            # Channel from frequency
            try:
                if 2412 <= net.freq <= 2472:
                    info["Channel"] = (net.freq - 2412)//5 + 1
                elif 5180 <= net.freq <= 5825:
                    info["Channel"] = (net.freq - 5000)//5
                else:
                    info["Channel"] = net.freq
            except:
                pass
            networks.append(info)
        return networks
    except Exception as e:
        logging.error("pywifi scan failed", exc_info=True)
        raise RuntimeError("pywifi scan failed: " + str(e))

class WiFiAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WiFi Analyzer & Locator")
        self.geometry("1100x950")
        self.networks = []
        self.connected_info = {}
        self.create_widgets()
        self.refresh_data()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Button(frame, text="🔄 Refresh", command=self.refresh_data).pack(pady=5)

        # Connected network details panel
        self.conn_label = ttk.LabelFrame(frame, text="Currently Connected Network")
        self.conn_label.pack(fill=tk.X, padx=5, pady=8)
        self.conn_text = tk.Text(self.conn_label, height=6, font=("Courier", 10), wrap="none")
        self.conn_text.pack(fill=tk.X, expand=True)

        columns = ("SSID", "BSSID", "Signal (dBm)", "Channel", "Frequency (MHz)")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=210)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.figure = plt.Figure(figsize=(8, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(frame, height=6, font=("Courier", 8))
        self.log_text.pack(fill=tk.BOTH, expand=False, pady=5)
        self.log_text.insert(tk.END, "[App logs and errors will appear here]\n")

    def refresh_data(self):
        self.tree.delete(*self.tree.get_children())
        self.ax.clear()
        self.conn_text.delete(1.0, tk.END)
        try:
            self.networks = scan_wifi_networks()
            self.log_text.delete(1.0, tk.END)
            ssid_conn, bssid_conn = get_connected_network_info()
            conn = None
            for net in self.networks:
                if (ssid_conn and net.get("SSID") == ssid_conn) or (bssid_conn and net.get("BSSID") == bssid_conn):
                    conn = net
                self.tree.insert("", tk.END, values=(
                    net.get("SSID", "?"),
                    net.get("BSSID", "?"),
                    net.get("Signal", "?"),
                    net.get("Channel", "?"),
                    net.get("Frequency", "?")
                ))
            plot_channel_usage(self.ax, self.networks)
            self.canvas.draw()
            if conn:
                self.conn_text.insert(tk.END, "\n".join([f"{k}: {v}" for k,v in conn.items()]))
            else:
                self.conn_text.insert(tk.END, "No active connection detected (possibly due to Windows/driver limitations).")
            self.log_text.insert(tk.END, f"{len(self.networks)} networks found.\n")
        except Exception as e:
            logging.error("pywifi scan error", exc_info=True)
            self.log_text.insert(tk.END, "Scan error: " + str(e) + "\n")
            messagebox.showerror("Error", "An error occurred:\n" + str(e))

if __name__ == "__main__":
    try:
        app = WiFiAnalyzerApp()
        app.mainloop()
    except Exception as err:
        logging.error("Startup error", exc_info=True)
        print("Startup error:", err)
        traceback.print_exc()
