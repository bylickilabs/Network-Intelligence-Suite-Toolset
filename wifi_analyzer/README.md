
# WiFi Analyzer & Locator – Final Clean Version

A stable, fully tested WiFi analysis tool for Windows.

## ✅ Features

- Scans using `netsh wlan show networks mode=bssid`
- Supports localized output (detects both "Channel" and "Kanal")
- Displays SSID, BSSID, Signal (dBm), and Channel
- Channel usage visualization using matplotlib
- Error-free – no unterminated f-string issues
- Logs errors to `error.log`

## 🛠 Requirements

- Windows with an active WiFi adapter
- Python 3.9 or higher
- `matplotlib` package installed

## ▶️ How to Start

```bash
pip install -r requirements.txt
python app.py
```

## 🔐 License

MIT License © 2025 Thorsten Bylicki / BYLICKILABS
