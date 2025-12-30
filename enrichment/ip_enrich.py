import json
import subprocess

IOC_FILE = "../data/iocs.json"
OUTPUT_FILE = "../data/enriched_iocs.json"

def load_iocs():
    with open(IOC_FILE, "r") as f:
        return json.load(f)["ips"]

def nmap_scan(ip):
    try:
        result = subprocess.check_output(
            ["nmap", "-Pn", "-F", ip],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result
    except Exception:
        return "Nmap scan failed"

def whois_lookup(ip):
    try:
        result = subprocess.check_output(
            ["whois", ip],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result[:500]  # limit output
    except Exception:
        return "Whois lookup failed"

def enrich_ips(ips):
    enriched = []

    for ip in ips[:5]:  # only first 5 to stay safe
        print(f"[+] Enriching {ip}")
        enriched.append({
            "ip": ip,
            "nmap": nmap_scan(ip),
            "whois": whois_lookup(ip)
        })

    return enriched

def save_results(data):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    ips = load_iocs()
    enriched_data = enrich_ips(ips)
    save_results(enriched_data)
    print("[+] Enriched IOC data saved")
