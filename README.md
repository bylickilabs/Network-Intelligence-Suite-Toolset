
# 🧠 BYLICKILABS Network Intelligence Suite – GUI Powered

A powerful collection of graphical tools for real-time network monitoring, diagnostics, and security analysis – developed by me, released for you.

---

## 📦 What is this?

**BYLICKILABS Network Intelligence Suite** is a modernized set of **10 advanced network utilities**, transformed from traditional CLI tools into a fully interactive **GUI-based security environment**.

Each tool in this suite has been carefully redesigned, extended, and refined to meet the demands of modern IT infrastructures – now available as open-source software under my MIT license.

Whether you're a sysadmin, a network analyst, or a cybersecurity engineer, this toolkit is designed to help you **observe**, **inspect**, **validate**, and **harden** your environment.

---

## 🔧 What's Inside?

Here’s what you get – all tools run locally, require no external dashboards, and are built entirely in Python:

### 1. ⚙️ Autorun Inspector  
Visualize, filter and analyze auto-start entries, services, registry hooks, and scheduled tasks – identify stealthy background activity in real time.

### 2. 🌐 DNS Inspector  
Query and validate DNS records (A, MX, TXT), verify SPF/DKIM/DMARC, check DNSSEC, and detect anomalies with passive DNS and WHOIS integrations.

### 3. 🔥 Firewall Rule Analyzer  
Import and simulate local or external firewall rules (UFW, iptables, Windows), detect misconfigurations, and test rule logic visually.

### 4. 🛠️ MAC Address Lookup (API)  
Identify unknown devices on your network using vendor resolution via MAC address and a secured lookup API. Works online with fallback caching.

### 5. 📡 Network Toolkit  
Run subnet scans, traceroutes, ping sweeps, and detailed TCP port inspections – all from a modular interface with live response visualization.

### 6. 🔎 Packet Sniffer  
Capture live packets with protocol filtering, entropy analysis, and raw view export (.pcap, hex). Includes traffic shaping insights and session parsing.

### 7. 🔒 Secure Port Monitor  
Continuously track open ports and services (inbound/outbound). Receive warnings on changes, remote connections, and unauthorized listeners.

### 8. 📁 Secure Transfer Assistant  
Send files securely with built-in AES or GPG encryption, including checksum validation, QR-based pairing, and optional WebRTC fallback.

### 9. 🚀 Speed Test Utility  
Benchmark your bandwidth with precision using the official speedtest.net API – shows latency, jitter, packet loss, ISP info, and logs for reporting.

### 10. 📶 WiFi Analyzer  
Scan and map nearby wireless networks, visualize signal strength over time, analyze channel congestion, and log SSID changes in your vicinity.

---

## 🔓 Why Open Source?

Because transparency matters.

> All tools in this suite are released as free and open source under the MIT license – so you can audit, customize, and extend them as needed.

Security software must be trustworthy. Closed black boxes are no longer acceptable in modern infosec operations. This project reflects the belief that **functionality, control, and visibility belong in the hands of users**.

---

## 🖥️ System Requirements

- Python 3.10+  
- OS: Windows 10/11 recommended (partial support for Linux)  
- GUI Framework: Tkinter (included in standard Python)  
- Required packages listed in `requirements.txt`

---

## 📚 Documentation

Each tool in this suite is bundled with its own detailed documentation, including:

- ✅ Feature overview  
- 🖼️ GUI walkthrough  
- ⚙️ Configuration/setup instructions  
- 🧪 Known limitations  
- 🔧 Troubleshooting tips

> You’ll find each tool’s documentation in its respective subfolder.

---

## 🚀 Getting Started

Clone the repository and launch the GUI:

```bash
git clone https://github.com/bylickilabs/network-intelligence-suite.git
cd network-intelligence-suite
(folder) python app.py
```

No installer required. All tools are embedded in a centralized launcher.

---

## 🔍 Design Philosophy

- 🧠 **Clarity over clutter** – every element in the interface has a purpose  
- 🔐 **Security by design** – no hardcoded keys, no telemetry, no backdoors  
- 🛠️ **Built to last** – no placeholders, no simulations, no “coming soon” banners  
- 📄 **Documentation is part of the product** – not an afterthought  
- 🧩 **Extensible architecture** – each module can be extended or isolated as a standalone tool

---

## 🧑‍💻 Author & Maintainer

**Thorsten Bylicki**  
Founder, BYLICKILABS  
GitHub: [BYLICKILABS](https://github.com/bylickilabs)

---

## ✅ License

This project is licensed under the **MIT License**.  
Use it freely, fork it, enhance it — just don’t forget to give credit.
[LICENSE](LICENSE)

---

## 💡 Final Words

This suite is more than just a repackaging of old CLI tools — it’s a professional-grade GUI toolkit for serious network and security work.

Use it to:

- Investigate anomalies  
- Benchmark your infrastructure  
- Analyze risk  
- Maintain visibility

And most importantly: **stay in control** of your network.

---

> **🛡️ BYLICKILABS – Code. Secure. Repeat.**
