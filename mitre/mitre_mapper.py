import json

INPUT_FILE = "../data/enriched_iocs.json"
OUTPUT_FILE = "../data/mitre_mapped_iocs.json"

def map_to_mitre(nmap_output):
    techniques = []

    if "ssh" in nmap_output:
        techniques.append({
            "tactic": "Lateral Movement",
            "technique": "Remote Services (T1021)"
        })

    if "mysql" in nmap_output or "nfs" in nmap_output:
        techniques.append({
            "tactic": "Credential Access",
            "technique": "Unsecured Credentials (T1552)"
        })

    if "open" in nmap_output:
        techniques.append({
            "tactic": "Command and Control",
            "technique": "Application Layer Protocol (T1071)"
        })

    return techniques

def process_iocs():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    mapped = []

    for entry in data:
        mapped.append({
            "ip": entry["ip"],
            "mitre_mapping": map_to_mitre(entry["nmap"])
        })

    return mapped

def save_results(results):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    results = process_iocs()
    save_results(results)
    print("[+] MITRE ATT&CK mapping completed")
