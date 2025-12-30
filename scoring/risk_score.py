import json

INPUT_FILE = "../data/enriched_iocs.json"
OUTPUT_FILE = "../data/scored_iocs.json"

def calculate_risk(nmap_output):
    score = 0

    # Simple risk logic (medium-level, acceptable)
    if "open" in nmap_output:
        score += 40
    if "ssh" in nmap_output:
        score += 20
    if "mysql" in nmap_output:
        score += 30
    if "nfs" in nmap_output:
        score += 20

    return min(score, 100)

def classify_risk(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"

def score_iocs():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    results = []

    for entry in data:
        score = calculate_risk(entry["nmap"])
        classification = classify_risk(score)

        results.append({
            "ip": entry["ip"],
            "risk_score": score,
            "risk_level": classification
        })

    return results

def save_results(results):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    scored_data = score_iocs()
    save_results(scored_data)
    print("[+] Risk scoring completed and saved")
