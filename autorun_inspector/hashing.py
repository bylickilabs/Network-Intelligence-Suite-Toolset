
import hashlib
import os

def get_file_hash(path):
    if not os.path.exists(path):
        return "Not Found"
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        return f"Unreadable: {e}"
