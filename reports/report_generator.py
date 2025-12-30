import json
from jinja2 import Template

# Load data files
with open("../data/scored_iocs.json") as f:
    scored = json.load(f)

with open("../data/mitre_mapped_iocs.json") as f:
    mitre = json.load(f)

html_template = """
<html>
<head>
    <title>Cyber Threat Intelligence Report</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #b30000; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid black; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>

<h1>Cyber Threat Intelligence Report</h1>

<h2>Executive Summary</h2>
<p>This report analyzes malicious IPs collected from public threat feeds,
enriched using Kali Linux tools, scored for risk, and mapped to MITRE ATT&CK.</p>

<h2>Risk Scoring</h2>
<table>
<tr>
    <th>IP Address</th>
    <th>Risk Score</th>
    <th>Risk Level</th>
</tr>
{% for item in scored %}
<tr>
    <td>{{ item.ip }}</td>
    <td>{{ item.risk_score }}</td>
    <td>{{ item.risk_level }}</td>
</tr>
{% endfor %}
</table>

<h2>MITRE ATT&CK Mapping</h2>
{% for entry in mitre %}
<h3>{{ entry.ip }}</h3>
<ul>
{% for m in entry.mitre_mapping %}
<li>{{ m.tactic }} — {{ m.technique }}</li>
{% endfor %}
</ul>
{% endfor %}

<h2>Conclusion</h2>
<p>This automated CTI system demonstrates how threat data can be collected,
enriched, analyzed, and transformed into actionable intelligence.</p>

</body>
</html>
"""

template = Template(html_template)
output = template.render(scored=scored, mitre=mitre)

with open("CTI_Report.html", "w") as f:
    f.write(output)

print("[+] CTI_Report.html generated successfully")
