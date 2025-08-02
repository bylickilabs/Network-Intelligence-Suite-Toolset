
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import platform
import subprocess
import os

class FirewallRuleAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Firewall Rule Analyzer")
        self.geometry("900x600")
        self.configure_gui()

    def configure_gui(self):
        frm = ttk.Frame(self, padding=10)
        frm.pack(fill=tk.BOTH, expand=True)

        button_frame = ttk.Frame(frm)
        button_frame.pack(fill=tk.X, pady=5)

        ttk.Button(button_frame, text="Import Rules (Text File)", command=self.import_rules).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Load System Rules", command=self.load_system_rules).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Simulate Conflict Check", command=self.simulate_conflicts).pack(side=tk.LEFT, padx=5)

        self.rule_display = tk.Text(frm, wrap=tk.WORD, font=("Courier", 10))
        self.rule_display.pack(fill=tk.BOTH, expand=True, pady=10)

    def import_rules(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = f.read()
                    self.rule_display.delete(1.0, tk.END)
                    self.rule_display.insert(tk.END, data)
                    self.status_message(f"Loaded rules from {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")

    def load_system_rules(self):
        try:
            rules = ""
            if platform.system() == "Linux":
                rules = subprocess.check_output(["sudo", "iptables", "-L"], encoding="utf-8", errors="ignore")
            elif platform.system() == "Windows":
                rules = subprocess.check_output(["powershell", "-Command", "Get-NetFirewallRule | Format-Table -AutoSize"], encoding="utf-8", errors="ignore")
            else:
                rules = "[Error] Unsupported system for live rule retrieval."
            self.rule_display.delete(1.0, tk.END)
            self.rule_display.insert(tk.END, rules)
            self.status_message("Loaded system firewall rules")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load system rules: {e}")

    def simulate_conflicts(self):
        content = self.rule_display.get(1.0, tk.END).splitlines()
        blocked_ports = set()
        conflicts = []

        for line in content:
            if "block" in line.lower() or "deny" in line.lower():
                for word in line.split():
                    if word.isdigit():
                        blocked_ports.add(word)

        for line in content:
            if "allow" in line.lower() or "accept" in line.lower():
                for word in line.split():
                    if word in blocked_ports:
                        conflicts.append(f"Conflict detected: Port {word} is both blocked and allowed")

        if conflicts:
            self.rule_display.insert(tk.END, "\n\n=== CONFLICTS DETECTED ===\n")
            for conflict in conflicts:
                self.rule_display.insert(tk.END, conflict + "\n")
            self.status_message("Conflicts found in rule set.")
        else:
            self.rule_display.insert(tk.END, "\n\nNo conflicts found. Rule set is consistent.\n")
            self.status_message("No conflicts found.")

    def status_message(self, msg):
        self.title(f"Firewall Rule Analyzer – {msg}")

if __name__ == "__main__":
    app = FirewallRuleAnalyzerApp()
    app.mainloop()
