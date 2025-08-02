
# Secure File Transfer Assistant

A secure, end-to-end encrypted file transfer tool for local or peer-to-peer communication.

## ✅ Features

- AES-256 file encryption with custom or generated key
- Local receiver on port 8080 (writes to system temp folder)
- Decrypt received file using entered key
- QR code generation for localhost transfer link
- SHA-256 hash validation after encryption
- Simple Tkinter GUI

## 🧰 Requirements

- Python 3.9+
- `cryptography`
- `qrcode`

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run (Windows 11)

1. Right-click on `app.py`
2. Select **"Edit with IDLE"**
3. Make sure the correct installed Python version (e.g. 3.12) is used
4. Press **F5** or click **Run > Run Module** to start the app

## 🔁 Workflow

1. Select a file
2. Enter or generate a 32-character encryption key
3. Click **Encrypt & Send File** to send the `.enc` file
4. Start the receiver on target machine
5. Use **Decrypt Received File** to save a decrypted copy

## 📁 Structure

```
secure_transfer_assistant/
├── app.py              # Main GUI application
├── encryption.py       # AES logic & key generation
├── transfer.py         # File transfer functions
├── qr_util.py          # QR code generation
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## 🔐 Security Notes

- The key is not transmitted over the network – only the encrypted file is.
- Use secure channels (e.g. QR or offline transfer) to share the key.

## 📄 License

MIT License © 2025 Thorsten Bylicki / BYLICKILABS
