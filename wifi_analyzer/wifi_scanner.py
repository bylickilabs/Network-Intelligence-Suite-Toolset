import subprocess

_last_output = []

def get_raw_output():
    """Return the last raw netsh output as a list of lines."""
    return _last_output

def scan_wifi_networks():
    """
    Scan for WiFi networks using netsh and return a list of networks
    with SSID, BSSID, Signal (dBm), and Channel information.
    Supports both English ('Channel') and German ('Kanal') Windows.
    """
    try:
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'networks', 'mode=bssid'],
            capture_output=True, text=True, encoding="utf-8", shell=True
        )
        output = result.stdout.splitlines()
        global _last_output
        _last_output = output
    except Exception as e:
        raise RuntimeError("netsh command failed: " + str(e))

    networks = []
    current = {}

    for line in output:
        line = line.strip()
        if line.startswith("SSID ") and "BSSID" not in line:
            if current:
                networks.append(current)
                current = {}
            current["SSID"] = line.split(":", 1)[1].strip()
        elif "BSSID" in line:
            current["BSSID"] = line.split(":", 1)[1].strip()
        elif "Signal" in line:
            try:
                percent = int(line.split(":", 1)[1].replace("%", "").strip())
                current["Signal"] = percent_to_dbm(percent)
            except:
                current["Signal"] = "?"
        elif "Channel" in line or "Kanal" in line:
            try:
                val = line.split(":", 1)[1].strip()
                current["Channel"] = int(val)
            except:
                current["Channel"] = "?"

    if current:
        networks.append(current)
    return networks

def percent_to_dbm(quality):
    """Convert WiFi signal quality percentage to approximate dBm."""
    return round((quality / 2) - 100)
