# Automated Cyber Threat Intelligence Platform (Kali Linux)

## 📌 Project Overview
This project implements an **Automated Cyber Threat Intelligence (CTI) Platform**
using **Kali Linux**.  
It demonstrates the **complete CTI lifecycle** — from threat data collection
to enrichment, analysis, MITRE ATT&CK mapping, and report generation.

The goal is to convert **raw threat data** into **actionable intelligence**
using automation and industry‑standard frameworks.

---

## 🎯 Objectives
- Collect threat indicators (IOCs) from public threat feeds
- Enrich IOCs using Kali Linux tools
- Analyze and assign risk scores
- Map attacker behavior to the **MITRE ATT&CK framework**
- Generate a professional, shareable CTI report

---

## 🛠️ Technology Stack
- **Operating System:** Kali Linux
- **Programming Language:** Python
- **Threat Intelligence:** Public AbuseIPDB feed
- **Security Tools:** Nmap, Whois
- **Framework:** MITRE ATT&CK
- **Reporting:** HTML (GitHub Pages)

---

## 🔄 Workflow (How the Project Works)

### Step 1: Threat Data Collection
- Malicious IPs are collected from a public threat feed
- Data is stored in `iocs.json`

### Step 2: IOC Enrichment
- Each IP is scanned using **Nmap**
- Ownership and abuse details are gathered using **Whois**
- Output stored in `enriched_iocs.json`

### Step 3: Risk Scoring
- Risk is calculated based on open services and exposure
- IPs are classified as **Low / Medium / High**
- Output stored in `scored_iocs.json`

### Step 4: MITRE ATT&CK Mapping
- Observed behaviors are mapped to MITRE ATT&CK tactics
- Output stored in `mitre_mapped_iocs.json`

### Step 5: Report Generation
- All results are compiled into a **static HTML report**
- The report is accessible on any system using a browser

---

## 🌍 Public Report Access
The final Cyber Threat Intelligence report is publicly available at:

👉 **https://aditikp0907.github.io/CTI-Kali-Project/CTI_Report.html**

No Kali Linux or Python installation is required to view the report.

---

## 🔐 Ethical Considerations
- Only **publicly available threat data** is used
- No exploitation or active attacks are performed
- Project is intended strictly for **educational and research purposes**

---

## 📌 Conclusion
This project demonstrates how raw cyber threat data can be transformed
into meaningful intelligence using automation, Kali Linux tools, and
industry frameworks like MITRE ATT&CK.

It reflects real‑world **SOC and Threat Intelligence workflows**.

---

## 👤 Author
**Aditi Patil**  
Cyber Security Student  
GitHub: https://github.com/aditikp0907

