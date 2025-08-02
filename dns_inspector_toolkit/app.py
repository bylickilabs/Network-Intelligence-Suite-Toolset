import tkinter as tk
from tkinter import ttk, messagebox
import traceback
from dns_utils import run_dns_checks
from whois_utils import get_whois_info

class DNSInspectorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DNS Inspector Toolkit")
        self.geometry("1000x700")
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        input_frame = ttk.Frame(frame)
        input_frame.pack(fill=tk.X, pady=5)

        ttk.Label(input_frame, text="Domain:").pack(side=tk.LEFT)
        self.domain_entry = ttk.Entry(input_frame, width=40)
        self.domain_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(input_frame, text="Inspect", command=self.inspect_domain).pack(side=tk.LEFT, padx=5)

        self.output = tk.Text(frame, wrap=tk.WORD, font=("Courier", 10))
        self.output.pack(fill=tk.BOTH, expand=True, pady=10)

    def inspect_domain(self):
        domain = self.domain_entry.get().strip()
        domain = domain.replace("https://", "").replace("http://", "").split("/")[0]

        if not domain:
            messagebox.showerror("Error", "Please enter a valid domain.")
            return

        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f"[i] Inspecting {domain}...\n\n")

        try:
            dns_result = run_dns_checks(domain)
            whois_result = get_whois_info(domain)
            self.output.insert(tk.END, dns_result)
            self.output.insert(tk.END, "\n\nWHOIS Info:\n")
            self.output.insert(tk.END, whois_result)
        except Exception as e:
            self.output.insert(tk.END, f"\n[ERROR] {e}\n")
            self.output.insert(tk.END, traceback.format_exc())

if __name__ == "__main__":
    try:
        app = DNSInspectorApp()
        app.mainloop()
    except Exception as e:
        print("Fatal Error:", e)
        traceback.print_exc()
