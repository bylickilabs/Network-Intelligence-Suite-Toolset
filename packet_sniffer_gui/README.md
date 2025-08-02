
# PacketSniffer GUI

**PacketSniffer GUI** is a lightweight packet capture tool built with Python and Tkinter, using the `scapy` library.

## ✅ Features

- Start/Stop live packet capture
- BPF filter support (e.g., `tcp`, `udp`, `port 80`)
- Live summary view of captured packets
- Export to `.pcap` file using `scapy`
- Built-in GUI (Tkinter)

## 🔍 Planned Features

- Hex view per packet
- Entropy analysis of payloads
- Protocol filtering & breakdown
- PyShark support for advanced inspection

## 💻 Requirements

- Python 3.9+
- `scapy`

Install with:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

```bash
python app.py
```

## 📁 Project Structure

```
packet_sniffer_gui/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
└── README.md           # English documentation
```

## ⚠️ Permissions

On Linux or macOS, run with sudo:

```bash
sudo python app.py
```

On Windows, run as Administrator.

## 🔐 License

MIT License © 2025 Thorsten Bylicki / BYLICKILABS
