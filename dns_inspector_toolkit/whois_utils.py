
import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        result = []
        for k, v in w.items():
            result.append(f"{k}: {v}")
        return "\n".join(result)
    except Exception as e:
        return f"[WHOIS Error] {e}"
