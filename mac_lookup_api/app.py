import tkinter as tk
from tkinter import ttk, messagebox
import requests
import subprocess
import platform
import re

# ✅ Correct: Only the key is stored here
API_KEY = "ONLY_YOUR_API_KEY_HERE"

def lookup_mac_vendor(mac, output_format="json"):
    # DON'T TOUCH THIS URL LINE
    url = "https://api.macaddress.io/v1"
    params = {
        "apiKey": API_KEY,
        "output": output_format,
        "search": mac
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        elif response.status_code == 429:
            return "Too many requests – rate limit exceeded (HTTP 429)."
        else:
            return f"API error: HTTP {response.status_code}"
    except Exception as e:
        return f"API lookup failed: {e}"

def resolve_ip_from_mac(mac):
    try:
        norm_mac = mac.lower().replace("-", ":")
        if platform.system().lower() == "windows":
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True, shell=True)
            for line in result.stdout.splitlines():
                if norm_mac[-5:] in line.lower() or norm_mac in line.lower():
                    parts = line.split()
                    if len(parts) >= 2:
                        return parts[0]
        else:
            result = subprocess.run(["arp", "-n"], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if norm_mac in line.lower():
                    return line.split()[0]
        return "Not found"
    except Exception as e:
        return f"Lookup error: {e}"

class MacLookupApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MAC Address Lookup + Local IP Resolver")
        self.geometry("700x500")
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(self, padding=20)
        frm.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frm, text="Enter MAC Address:").pack(anchor="w")
        self.mac_entry = ttk.Entry(frm, font=("Courier", 12), width=30)
        self.mac_entry.pack(fill=tk.X, pady=4)

        ttk.Label(frm, text="Select Output Format:").pack(anchor="w", pady=(10, 0))
        self.format_var = tk.StringVar(value="json")
        formats = [("JSON", "json"), ("XML", "xml"), ("CSV", "csv")]
        for label, value in formats:
            ttk.Radiobutton(frm, text=label, variable=self.format_var, value=value).pack(anchor="w")

        ttk.Button(frm, text="🔍 Lookup", command=self.lookup).pack(pady=10)

        ttk.Label(frm, text="Vendor Information:").pack(anchor="w")
        self.vendor_text = tk.Text(frm, height=10, font=("Courier", 10), wrap="none")
        self.vendor_text.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frm, text="Local IP (if known):").pack(anchor="w", pady=(10, 0))
        self.ip_label = ttk.Label(frm, text="(Will appear here)", font=("Courier", 10))
        self.ip_label.pack(anchor="w")

    def lookup(self):
        mac = self.mac_entry.get().strip()
        output_format = self.format_var.get()
        if not mac:
            messagebox.showerror("Input Error", "Please enter a MAC address.")
            return

        self.vendor_text.delete(1.0, tk.END)
        self.vendor_text.insert(tk.END, "Looking up vendor...\n")
        vendor = lookup_mac_vendor(mac, output_format)
        self.vendor_text.delete(1.0, tk.END)
        self.vendor_text.insert(tk.END, vendor)

        self.ip_label.config(text="Resolving local IP...")
        ip = resolve_ip_from_mac(mac)
        self.ip_label.config(text=f"Local IP (if found): {ip}")

if __name__ == "__main__":
    app = MacLookupApp()
    app.mainloop()
