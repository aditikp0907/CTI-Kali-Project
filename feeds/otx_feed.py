import requests
import json

def fetch_threat_ips():
    print("[+] Fetching threat IPs from public AbuseIPDB feed...")

    url = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("[+] Threat feed downloaded successfully")
            return response.text
        else:
            print("[-] Failed to fetch threat feed")
            return None
    except Exception as e:
        print("[-] Error:", e)
        return None


def save_iocs(raw_data):
    print("[+] Saving IOCs to data/iocs.json")

    ips = []
    for line in raw_data.splitlines():
        if line and not line.startswith("#"):
            ips.append(line.split()[0])

    iocs = {
        "source": "Public AbuseIPDB Feed",
        "ioc_type": "malicious_ips",
        "count": len(ips),
        "ips": ips[:20]  # store only first 20 for demo
    }

    with open("../data/iocs.json", "w") as f:
        json.dump(iocs, f, indent=4)

    print("[+] IOCs saved successfully")


if __name__ == "__main__":
    data = fetch_threat_ips()
    if data:
        save_iocs(data)
