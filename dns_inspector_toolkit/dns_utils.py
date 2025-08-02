
import dns.resolver
import dns.flags
import dns.query
import dns.message

def run_dns_checks(domain):
    output = []
    record_types = ['A', 'AAAA', 'NS', 'MX', 'CNAME', 'TXT', 'SOA']

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            for rdata in answers:
                output.append(f"{rtype:<6}: {rdata}")
        except:
            output.append(f"{rtype:<6}: (not found)")

    # TXT records for root
    spf_found = False
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        for txt in txt_records:
            txt_val = str(txt).strip('"')
            if 'v=spf1' in txt_val:
                output.append(f"SPF   : {txt_val}")
                spf_found = True
    except:
        pass

    # Check _dmarc.domain
    try:
        dmarc_txt = dns.resolver.resolve(f"_dmarc.{domain}", "TXT")
        for r in dmarc_txt:
            output.append(f"DMARC : {str(r).strip('"')}")
    except:
        output.append("DMARC : (not found)")

    # Check DKIM
    try:
        dkim_txt = dns.resolver.resolve(f"default._domainkey.{domain}", "TXT")
        for r in dkim_txt:
            output.append(f"DKIM  : {str(r).strip('"')}")
    except:
        output.append("DKIM  : (not found)")

    if not spf_found:
        output.append("SPF   : (not found)")

    # DNSSEC AD-flag check
    try:
        query = dns.message.make_query(domain, dns.rdatatype.A)
        query.flags |= dns.flags.AD
        response = dns.query.udp(query, '8.8.8.8', timeout=2)
        if response.flags & dns.flags.AD:
            output.append("DNSSEC: validated ✅ (AD flag set)")
        else:
            output.append("DNSSEC: not validated ❌")
    except Exception as e:
        output.append(f"DNSSEC: (error) {e}")

    return "\n".join(output)
