
# MAC Address Vendor Lookup (macaddress.io API)

This GUI tool resolves MAC addresses to full vendor details using the [LINK](https://macaddress.io) API.

## ✅ Features

- Enter any MAC address
- Select output format: JSON, XML, or CSV
- Displays full vendor information
- Uses the official `https://api.macaddress.io/v1` endpoint
- Error handling for rate limits and connection issues

## 🔐 API Access Required

To use this application, you **must register for a free API key** at [LINK](https://macaddress.io).

The free plan allows:
- **100 requests/month**
- Access to JSON, XML, and CSV formats

After registration:
1. Copy your API key
2. Open `app.py`
3. Replace this line:

```python
API_KEY = "ONLY_YOUR_API_KEY_HERE"
```

with:

```python
API_KEY = "your_actual_api_key"
```

Then save and run the application.

## 🛠 Requirements

- Python 3.9+
- requests

Install with:

```bash
pip install -r requirements.txt
```

## ▶ Run

```bash
python app.py
```

## 🔐 License

MIT License © 2025 Thorsten Bylicki / BYLICKILABS
