
import winreg
import subprocess
import os

def collect_registry_run_keys():
    keys = [
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run", "HKLM\Run"),
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", "HKCU\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run", "HKLM\WOW6432\Run")
    ]
    entries = []
    for hive, path, label in keys:
        try:
            with winreg.OpenKey(hive, path) as key:
                for i in range(0, winreg.QueryInfoKey(key)[1]):
                    name, cmd, _ = winreg.EnumValue(key, i)
                    entries.append({
                        "location": label,
                        "type": "Registry",
                        "command": cmd,
                        "path": extract_exe_path(cmd)
                    })
        except Exception as e:
            print(f"[Registry] Failed to read {label}: {e}")
    return entries

def collect_startup_folder():
    folder = os.path.join(os.environ.get("APPDATA", ""), r"Microsoft\Windows\Start Menu\Programs\Startup")
    entries = []
    if os.path.exists(folder):
        for file in os.listdir(folder):
            full = os.path.join(folder, file)
            if os.path.isfile(full):
                entries.append({
                    "location": "Startup Folder",
                    "type": "Shell",
                    "command": full,
                    "path": full
                })
    return entries

def collect_scheduled_tasks():
    entries = []
    try:
        result = subprocess.check_output("schtasks /query /fo LIST /v", shell=True, encoding="utf-8", errors="ignore")
        tasks = result.split("\n\n")
        for block in tasks:
            lines = block.splitlines()
            for line in lines:
                if line.startswith("Task To Run:"):
                    cmd = line.split(":", 1)[-1].strip()
                    entries.append({
                        "location": "Task Scheduler",
                        "type": "Scheduler",
                        "command": cmd,
                        "path": extract_exe_path(cmd)
                    })
    except Exception as e:
        print(f"[Scheduler] schtasks failed: {e}")
    return entries

def extract_exe_path(cmd):
    if not cmd:
        return None
    cmd = cmd.strip().strip('"')
    if ".exe" in cmd.lower():
        idx = cmd.lower().find(".exe") + 4
        return cmd[:idx].strip('"')
    return None

def collect_autoruns():
    data = []
    data.extend(collect_registry_run_keys())
    data.extend(collect_startup_folder())
    data.extend(collect_scheduled_tasks())
    return data
