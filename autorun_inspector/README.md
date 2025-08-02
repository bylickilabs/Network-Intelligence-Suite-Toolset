
# Service Tracker / Autorun Inspector

**Service Tracker / Autorun Inspector** is a forensic GUI-based tool for Windows that scans common autostart locations and displays registry entries, startup folders, and scheduled tasks.

---

## ✅ Features

- 🔍 Detect autorun entries from:
  - Windows Registry (HKLM / HKCU / WOW6432Node)
  - Shell Startup Folder
  - Windows Task Scheduler (via `schtasks`)
- 🧾 Visualize entries in a clean GUI (Tkinter)
- 🔐 Calculate SHA-256 hashes of executables
- 💾 Export results to CSV
- 🐞 Built-in debug/error output to console
- ⚠ Works locally – no external network access required

---

## 🧰 Requirements

- 🪟 **Windows OS only**
- Python 3.9+
- Admin rights recommended (for full registry/task access)

---

## 📦 File Structure

```
autorun_inspector_debug/
├── app.py              # GUI application with debug output
├── autoruns.py         # Registry, startup folder, scheduler collection
├── hashing.py          # SHA-256 hashing logic
├── README.md           # This documentation
```

---

## 🚀 How to Run

1. Extract the ZIP file  
2. Open PowerShell or CMD inside the folder  
3. Run:

```bash
python app.py
```

## Optional

If using IDLE:

- Right-click → Open with IDLE → Press F5

---

## 🧪 Sample Output

Each row in the GUI includes:
- Location (e.g. `HKCU\Run`)
- Type (Registry, Shell, Scheduler)
- Full command line
- SHA-256 hash (or error)

---

## 🧰 Debugging

Run in PowerShell or CMD to view logs:

```bash
python app.py
```

Errors during registry read, scheduler parsing, or file hashing will be printed.

---

## 🔐 License

MIT License © 2025 Thorsten Bylicki / BYLICKILABS
