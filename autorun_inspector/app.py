
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import traceback

try:
    from autoruns import collect_autoruns
    from hashing import get_file_hash
except Exception as e:
    print("Import error:", e)
    traceback.print_exc()

class AutorunInspectorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Service Tracker / Autorun Inspector")
        self.geometry("1000x600")
        self.create_widgets()
        self.entries = []

    def create_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X)

        ttk.Button(btn_frame, text="Scan Autoruns", command=self.run_scan).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Export CSV", command=self.export_csv).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(frame, columns=("Location", "Type", "Command", "Hash"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=240)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

    def run_scan(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.entries = collect_autoruns()
            for entry in self.entries:
                file_hash = get_file_hash(entry["path"]) if entry["path"] else "N/A"
                self.tree.insert("", "end", values=(entry["location"], entry["type"], entry["command"], file_hash))
        except Exception as e:
            messagebox.showerror("Scan Error", f"Failed to scan autoruns:\n{e}")

    def export_csv(self):
        if not self.entries:
            messagebox.showerror("Error", "No data to export.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv")
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("Location,Type,Command,Hash\n")
                for entry in self.entries:
                    hashval = get_file_hash(entry["path"]) if entry["path"] else "N/A"
                    f.write(f'"{entry["location"]}","{entry["type"]}","{entry["command"]}","{hashval}"\n')
            messagebox.showinfo("Exported", f"Data saved to {path}")
        except Exception as e:
            messagebox.showerror("Export Error", str(e))

if __name__ == "__main__":
    try:
        app = AutorunInspectorApp()
        app.mainloop()
    except Exception as ex:
        print("Fatal GUI error:", ex)
        traceback.print_exc()
