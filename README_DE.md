
# 🧠 BYLICKILABS Netzwerk-Intelligence Suite – GUI Edition

Eine leistungsstarke Sammlung grafischer Tools für Echtzeit-Netzwerküberwachung, Diagnose und Sicherheitsanalyse – entwickelt von mir, veröffentlicht für euch.

---

## 📦 Was ist das?

Die **BYLICKILABS Netzwerk-Intelligence Suite** ist eine modernisierte Sammlung von **10 fortgeschrittenen Netzwerk-Werkzeugen**, die vollständig von der Kommandozeile in eine interaktive, benutzerfreundliche **GUI-basierte Sicherheitsumgebung** überführt wurden.

Jedes Tool dieser Suite wurde sorgfältig überarbeitet, erweitert und verfeinert, um modernen Anforderungen in IT-Infrastrukturen gerecht zu werden – jetzt als **Open-Source-Software** unter meiner MIT-Lizenz verfügbar.

Ob Systemadministrator, Netzwerkanalyst oder Cybersecurity-Experte – dieses Toolkit hilft dir, deine Umgebung zu **analysieren**, **überwachen**, **überprüfen** und **absichern**.

---

## 🔧 Enthaltene Tools

Alle Tools laufen lokal, benötigen keine externen Dashboards und sind vollständig in Python geschrieben:

### 1. ⚙️ Autorun Inspector  
Visualisiere und analysiere Autostart-Einträge, geplante Tasks, Dienste und Registry-Hooks – erkenne versteckte Prozesse im Systemstart.

### 2. 🌐 DNS Inspector  
Prüfe DNS-Einträge (A, MX, TXT), validiere SPF/DKIM/DMARC, prüfe DNSSEC und erkenne Anomalien mit passivem DNS und WHOIS-Abfragen.

### 3. 🔥 Firewall Rule Analyzer  
Importiere und simuliere Firewall-Regeln (UFW, iptables, Windows), erkenne Konflikte, doppelte Einträge und logische Fehler in Regelsets.

### 4. 🛠️ MAC Address Lookup (API)  
Identifiziere unbekannte Geräte im Netzwerk durch Herstellerauflösung via MAC-Adresse – mit Online-API und Caching.

### 5. 📡 Network Toolkit  
Führe Subnetz-Scans, Traceroutes, Ping-Sweeps und Portanalysen durch – alles modular und grafisch visualisiert.

### 6. 🔎 Packet Sniffer  
Erfasse Live-Traffic mit Protokollfiltern, Entropieanalyse, Export als .pcap und HEX-Viewer – inklusive Session-Parsing.

### 7. 🔒 Secure Port Monitor  
Überwache offene Ports (lokal/remote), erkenne neue Verbindungen, ungewöhnliche Dienste und führe GeoIP-Zuordnungen durch.

### 8. 📁 Secure Transfer Assistant  
Übertrage Dateien sicher mit AES- oder GPG-Verschlüsselung, inklusive Hashprüfung, QR-Kopplung und optionalem WebRTC-Fallback.

### 9. 🚀 Speed Test Utility  
Messe deine Bandbreite via speedtest.net API – inklusive Latenz, Jitter, Paketverlust, Providerinformationen und Protokollierung.

### 10. 📶 WiFi Analyzer  
Scanne WLAN-Netze in deiner Umgebung, visualisiere Signalstärke, analysiere Kanalnutzung und erfasse SSID-Veränderungen.

---

## 🔓 Warum Open Source?

Weil Transparenz zählt.

> Alle Tools dieser Suite sind **frei und quelloffen** unter der MIT-Lizenz veröffentlicht – prüfe sie, erweitere sie, passe sie an.

Sicherheitssoftware muss vertrauenswürdig sein. Geschlossene Systeme sind nicht mehr zeitgemäß. Diese Veröffentlichung steht für die Überzeugung, dass **Sichtbarkeit, Kontrolle und Eigenverantwortung beim Nutzer liegen**.

---

## 🖥️ Systemvoraussetzungen

- Python 3.10+  
- Betriebssystem: Windows 10/11 empfohlen (Linux teilweise unterstützt)  
- GUI: Tkinter (in Python enthalten)  
- Abhängigkeiten in `requirements.txt`

---

## 📚 Dokumentation

Jedes Tool enthält eigene, ausführliche Dokumentation:

- ✅ Funktionsübersicht  
- 🖼️ GUI-Anleitung  
- ⚙️ Setup- und API-Hinweise  
- 🧪 Bekannte Einschränkungen  
- 🔧 Tipps zur Fehlerbehebung

> Die Dokumentation befindet sich im jeweiligen Unterordner des Tools.

---

## 🚀 Schnellstart

Klonen und starten:

```bash
git clone https://github.com/bylickilabs/Network-Intelligence-Suite-Toolset.git
cd Network-Intelligence-Suite-Toolset
(verzeichnis) python app.py
```

Kein Installer notwendig. Zentrale GUI mit Zugriff auf alle Tools.

---

## 🔍 Philosophie

- 🧠 **Klarheit statt Komplexität** – jede UI-Komponente hat ihren Zweck  
- 🔐 **Sicherheit von Anfang an** – keine Backdoors, kein Tracking  
- 🛠️ **Produktionsreif** – keine Platzhalter, keine Simulationen  
- 📄 **Dokumentation ist Teil des Produkts** – nicht optional  
- 🧩 **Modular und erweiterbar** – jedes Tool auch einzeln lauffähig

---

## 👨‍💻 Autor & Maintainer

**Thorsten Bylicki**  
Gründer, BYLICKILABS  
GitHub: [BYLICKILABS](https://github.com/bylickilabs)

---

## ✅ Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.  
Du kannst es frei nutzen, ändern, weitergeben – mit entsprechendem Hinweis auf den Autor.
[LICENSE](LICENSE)

---

## 💬 Abschließende Worte

Diese Suite ist keine GUI-Spielerei – sie ist ein **Werkzeugkasten für Profis**.  
Nutze sie, um:

- Auffälligkeiten zu untersuchen  
- Netzwerkinfrastruktur zu prüfen  
- Sicherheitslücken zu erkennen  
- Stabilität und Transparenz zu gewinnen

Bleib informiert. Bleib sicher. **Bleib im Kontrollbereich deines Netzwerks.**

---

> **🛡️ BYLICKILABS – Code. Sicher. Wiederholen.**
