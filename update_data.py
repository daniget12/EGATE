import json
from app.courses.data import COURSES

def generate_content(slug, title):
    if slug == "intro-to-cybersecurity":
        return [
            {"type": "heading", "text": "What is Cybersecurity?"},
            {"type": "paragraph", "text": "Cybersecurity is the practice of protecting computer systems, networks, programs, and data from digital attacks, unauthorized access, and other vulnerabilities that can lead to compromise or loss."},
            {"type": "heading", "text": "The CIA Triad"},
            {"type": "paragraph", "text": "The CIA Triad is the foundational model for securing information systems. It represents three core principles:"},
            {"type": "table",
             "headers": ["Principle", "Description", "Example"],
             "rows": [
                ["Confidentiality", "Preventing unauthorized access to information", "Encryption, Access controls"],
                ["Integrity", "Assuring data is not altered or destroyed improperly", "Hashing, Digital signatures"],
                ["Availability", "Ensuring data and systems are accessible when needed", "Backups, DoS protection"]
             ]},
            {"type": "heading", "text": "The Threat Landscape"},
            {"type": "bullets", "items": [
                "Malware — viruses, worms, trojans",
                "Phishing — social engineering to steal credentials",
                "Ransomware — encrypts data and demands payment",
                "Social Engineering — exploiting human psychology"
             ]},
            {"type": "callout", "variant": "info", "text": "Every attack targets one or more pillars of the CIA Triad. Ask yourself: is the attacker trying to read data (Confidentiality), change data (Integrity), or block access (Availability)?"}
        ]
    elif slug == "networking-fundamentals":
        return [
            {"type": "heading", "text": "OSI vs TCP/IP Models"},
            {"type": "paragraph", "text": "Networking relies on structured models to ensure seamless communication across different hardware and software."},
            {"type": "table",
             "headers": ["OSI Layer", "TCP/IP Layer", "Function"],
             "rows": [
                ["7. Application", "Application", "End-user processes (HTTP, FTP)"],
                ["6. Presentation", "Application", "Data representation and encryption"],
                ["5. Session", "Application", "Interhost communication"],
                ["4. Transport", "Transport", "End-to-end connections (TCP, UDP)"],
                ["3. Network", "Internet", "Path determination and IP addressing"],
                ["2. Data Link", "Network Access", "MAC addressing and switching"],
                ["1. Physical", "Network Access", "Media, signal and binary transmission"]
             ]},
            {"type": "heading", "text": "IP Addressing"},
            {"type": "paragraph", "text": "IP addresses uniquely identify devices on a network. We primarily use IPv4 (32-bit) and IPv6 (128-bit)."},
            {"type": "bullets", "items": [
                "IPv4 Example: 192.168.1.1",
                "IPv6 Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "Subnetting divides a larger network into smaller, manageable sub-networks."
            ]},
            {"type": "callout", "variant": "warning", "text": "IPv4 addresses are exhausted! That's why NAT (Network Address Translation) and IPv6 were developed."}
        ]
    elif slug == "windows-defender-firewall":
        return [
            {"type": "heading", "text": "Windows Defender Overview"},
            {"type": "paragraph", "text": "Windows Defender is an integrated anti-malware component of Windows. It provides real-time protection against software threats like viruses, malware, and spyware across email, apps, the cloud, and the web."},
            {"type": "heading", "text": "Windows Firewall"},
            {"type": "paragraph", "text": "The Windows Firewall filters network data transmissions to and from your Windows system. It relies on a set of rules to determine what traffic is allowed."},
            {"type": "table",
             "headers": ["Rule Type", "Description", "Usage"],
             "rows": [
                 ["Inbound", "Controls traffic coming into the system.", "Block untrusted incoming connections (e.g., block external RDP)."],
                 ["Outbound", "Controls traffic originating from the system.", "Prevent malware from phoning home."],
                 ["Connection Security", "Secures traffic using IPsec.", "Encrypt data between two specific servers."]
             ]},
            {"type": "callout", "variant": "danger", "text": "Never disable the firewall completely! Instead, create specific exceptions for the services you need."}
        ]
    elif slug == "hashing-encryption":
        return [
            {"type": "heading", "text": "Hashing vs Encryption"},
            {"type": "paragraph", "text": "While both use cryptography to protect data, they serve different purposes. Encryption is a two-way function designed to hide data, while hashing is a one-way function meant to verify integrity."},
            {"type": "table",
             "headers": ["Feature", "Hashing", "Encryption"],
             "rows": [
                 ["Direction", "One-way (irreversible)", "Two-way (reversible)"],
                 ["Output", "Fixed length (e.g., 256 bits)", "Variable length (depends on input)"],
                 ["Primary Goal", "Data Integrity", "Data Confidentiality"],
                 ["Examples", "MD5, SHA-1, SHA-256", "AES, RSA, DES"]
             ]},
            {"type": "heading", "text": "Symmetric vs Asymmetric Encryption"},
            {"type": "bullets", "items": [
                "Symmetric Encryption: Uses a single shared key for both encryption and decryption (e.g., AES). It's fast but requires secure key exchange.",
                "Asymmetric Encryption: Uses a key pair (public key to encrypt, private key to decrypt) (e.g., RSA). It's slower but solves the key exchange problem."
            ]},
            {"type": "callout", "variant": "info", "text": "MD5 and SHA-1 are considered cryptographically broken. Always use SHA-256 or better for secure hashing."}
        ]
    else:
        return [
            {"type": "heading", "text": title + " Concepts"},
            {"type": "paragraph", "text": "This module covers the essential principles, tools, and methodologies required to master " + title.lower() + ". Understanding these concepts is critical for modern cybersecurity operations."},
            {"type": "heading", "text": "Core Principles"},
            {"type": "bullets", "items": [
                "Identify vulnerabilities and misconfigurations.",
                "Apply best practices for secure deployment.",
                "Utilize industry-standard tools effectively."
            ]},
            {"type": "table",
             "headers": ["Concept", "Application", "Relevance"],
             "rows": [
                 ["Analysis", "Reviewing system states and logs", "High"],
                 ["Implementation", "Applying secure configurations", "Critical"],
                 ["Validation", "Testing applied controls", "Medium"]
             ]},
            {"type": "callout", "variant": "info", "text": "Remember to review the external practice links to gain hands-on experience with these concepts."}
        ]

for course in COURSES:
    for module in course["modules"]:
        module["content"] = generate_content(module["slug"], module["title"])

with open('app/courses/data.py', 'w', encoding='utf-8') as f:
    f.write("COURSES = ")
    f.write(json.dumps(COURSES, indent=4))
    f.write("\n")
