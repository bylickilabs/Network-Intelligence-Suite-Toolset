
# Firewall Rule Analyzer

**Firewall Rule Analyzer** is a GUI-based desktop tool for analyzing, importing, simulating, and visualizing firewall rule sets.  
Designed for administrators, DevSecOps engineers, and security analysts.

## ✅ Features

- Import firewall rules from a text file
- Load active system rules (supports Windows Defender Firewall and iptables)
- Simulate conflict detection (e.g., blocked & allowed same port)
- Display rules and detection results in a readable GUI

## 🧠 Target Audience

- System Administrators
- DevSecOps Engineers
- Security Auditors
- Network Engineers

## 🖥️ GUI

- Built with `tkinter`
- Responsive layout
- Displays raw rules and analysis output

## 🔧 Requirements

- Python 3.9+
- `tkinter` (built-in)
- Administrative rights may be needed to load system rules

## 💻 How to Run

```bash
python app.py
```

## 📁 File Structure

```
firewall_rule_analyzer/
├── app.py              # Main application
├── requirements.txt    # Dependencies (none currently required)
└── README.md           # English documentation
```

## 🔐 License

MIT License © 2025 Thorsten Bylicki / BYLICKILABS
