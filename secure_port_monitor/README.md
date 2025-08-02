
# Secure Port Monitor

**Secure Port Monitor** is a real-time port monitoring tool for local systems, written in Python using Tkinter and `psutil`. It detects and logs changes to open listening ports (e.g., when a new service starts or stops) and displays this information in a clear GUI.

## ✅ Features

- Monitors open listening ports in real time
- Logs added or removed ports with timestamp
- Lightweight GUI using Tkinter
- Automatically updates every 5 seconds
- Status bar shows the last change detected

## 🛠️ Planned Extensions

- Tray icon with background monitoring
- Email or Syslog notifications for critical ports
- GeoIP detection for remote foreign IPs (future TCP mode)
- Export history to CSV or JSON
- Rule-based alerting

## 📦 Requirements

- Python 3.9+
- [psutil](https://pypi.org/project/psutil/)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

```bash
python app.py
```

## 📁 File Structure

```
secure_port_monitor/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

## 🔐 License

MIT License © 2025 Thorsten Bylicki / BYLICKILABS
