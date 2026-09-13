import json

COURSES = [
    {
        "code": "DAET-FOE-CYT101",
        "title": "Cybersecurity Essentials",
        "description": "Core concepts, networking, packet analysis, and defense mechanisms.",
        "modules": [
            {
                "slug": "intro-to-cybersecurity",
                "title": "Introduction to Cybersecurity",
                "summary": "Define cybersecurity, understand the CIA Triad, and identify today's threat landscape.",
                "objectives": [
                    "Define cybersecurity and its significance",
                    "Explain the CIA Triad and apply it to security decisions",
                    "Identify major cybersecurity domains",
                    "Classify threat actors and their motivations"
                ],
                "topics": [
                    "CIA Triad (Confidentiality, Integrity, Availability)",
                    "Cybersecurity Domains",
                    "Common Threats",
                    "Vulnerabilities vs. Exploits",
                    "Threat Actors and Motivations"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Pre Security Path", "url": "https://tryhackme.com/path/outline/presecurity", "description": "Free guided path covering the fundamentals."},
                    {"name": "Cisco Networking Academy \u2014 Intro to Cybersecurity", "url": "https://www.netacad.com/courses/cybersecurity", "description": "Free course from Cisco on cybersecurity basics."}
                ],
                "content": [
                    {"type": "heading", "text": "Defining Cybersecurity"},
                    {"type": "paragraph", "text": "Cybersecurity is the practice of protecting computer systems, networks, programs, and data from digital attacks, unauthorized access, and other vulnerabilities that can lead to compromise or loss. The primary objectives include ensuring the confidentiality, integrity, and availability of information."},
                    {"type": "heading", "text": "The CIA Triad"},
                    {"type": "paragraph", "text": "The CIA Triad is a foundational model in cybersecurity that represents the three core principles for securing information systems: Confidentiality, Integrity, and Availability."},
                    {"type": "table", "headers": ["Principle", "Description", "Example"], "rows": [
                        ["Confidentiality", "Preventing unauthorized access to information", "Encryption, Access controls"],
                        ["Integrity", "Assuring data is not altered or destroyed improperly", "Hashing, Digital signatures"],
                        ["Availability", "Ensuring data and systems are accessible when needed", "Backups, DoS protection"]
                    ]},
                    {"type": "heading", "text": "Threat Actors"},
                    {"type": "table", "headers": ["Threat Actor Type", "Description", "Example"], "rows": [
                        ["Script Kiddies", "Novice hackers using existing tools", "Defacement attacks"],
                        ["Insiders", "Individuals with legitimate access abusing it", "Data theft by employees"],
                        ["Organized Crime", "Groups acting for financial gain", "Banking malware rings"],
                        ["APTs", "Sophisticated, well-funded, often state-sponsored", "Stuxnet, SolarWinds"]
                    ]},
                    {"type": "heading", "text": "Risk Calculation"},
                    {"type": "callout", "variant": "warning", "text": "Risk is often quantified using the formula: Risk = Threat \u00d7 Vulnerability \u00d7 Impact. By assessing each factor, organizations can calculate a risk score to prioritize security efforts."}
                ]
            },
            {
                "slug": "networking-fundamentals",
                "title": "Networking Fundamentals",
                "summary": "Understand OSI, TCP/IP, IP addressing, and subnetting.",
                "objectives": [
                    "Understand the purpose and structure of the OSI and TCP/IP models.",
                    "Identify the functions of each layer in both models.",
                    "Define and calculate IP addressing and subnetting; distinguish between private and public IPs."
                ],
                "topics": [
                    "OSI and TCP/IP models",
                    "Layered Communication and Encapsulation",
                    "IP addressing and subnetting",
                    "Ping and Traceroute"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Network Fundamentals", "url": "https://tryhackme.com/module/network-fundamentals", "description": "Learn how networks work and the concepts behind them."},
                    {"name": "Professor Messer \u2014 Network+", "url": "https://www.professormesser.com/network-plus/n10-009/n10-009-training-course/", "description": "Comprehensive CompTIA Network+ training."}
                ],
                "content": [
                    {"type": "heading", "text": "OSI Model (7 Layers)"},
                    {"type": "paragraph", "text": "The Open Systems Interconnection (OSI) Model is a conceptual framework used to understand and standardize how different networking protocols interact across seven distinct layers."},
                    {"type": "table", "headers": ["Layer", "Function", "Example Protocols"], "rows": [
                        ["Application", "User-facing network services", "HTTP, FTP, SMTP"],
                        ["Presentation", "Data formatting, encryption, compression", "SSL, JPEG"],
                        ["Session", "Establishes, manages & terminates sessions", "NetBIOS, RPC"],
                        ["Transport", "Reliable data transfer, segmentation, error check", "TCP, UDP"],
                        ["Network", "Logical addressing & routing", "IP, ICMP"],
                        ["Data Link", "Node-to-node data transfer, MAC addressing", "Ethernet, PPP"],
                        ["Physical", "Transmission of raw bits over medium", "Ethernet cables"]
                    ]},
                    {"type": "heading", "text": "TCP/IP Model"},
                    {"type": "paragraph", "text": "The TCP/IP model condenses networking functions into four layers (Application, Transport, Internet, Network Access) that reflect how data flows across the Internet and other networks."},
                    {"type": "heading", "text": "IP Addressing Basics"},
                    {"type": "table", "headers": ["Feature", "IPv4", "IPv6"], "rows": [
                        ["Length", "32 bits (e.g., 192.168.1.1)", "128 bits (e.g., 2001:0db8:85a3::8a2e:370:7334)"],
                        ["Address Pool", "~4.3 billion unique addresses", "340 undecillion addresses"],
                        ["Security", "Optional IPsec", "Mandatory IPsec"]
                    ]},
                    {"type": "callout", "variant": "info", "text": "Subnetting is the process of dividing a large network into smaller, more manageable segments. It enhances network performance and increases security by isolating groups of devices."}
                ]
            },
            {
                "slug": "packet-analysis",
                "title": "Packet Analysis",
                "summary": "Learn about HTTP, HTTPS, DNS, ARP, and packet inspection using Wireshark.",
                "objectives": [
                    "Understand the role of network protocols in digital communication.",
                    "Identify and describe common protocols including HTTP, HTTPS, DNS, and ARP.",
                    "Use Wireshark to capture, inspect, and analyze network packets."
                ],
                "topics": [
                    "Protocols (HTTP, HTTPS, DNS, ARP)",
                    "Packet sniffing and inspection with Wireshark",
                    "Capture and analyze real-time traffic"
                ],
                "external_links": [
                    {"name": "Wireshark Sample Captures", "url": "https://wiki.wireshark.org/SampleCaptures", "description": "Sample packet captures for practice."},
                    {"name": "TryHackMe \u2014 Wireshark 101", "url": "https://tryhackme.com/room/wireshark", "description": "Learn the basics of Wireshark."}
                ],
                "content": [
                    {"type": "heading", "text": "HTTP vs. HTTPS"},
                    {"type": "table", "headers": ["Feature", "HTTP", "HTTPS"], "rows": [
                        ["Port", "80", "443"],
                        ["Encryption", "None", "SSL/TLS"],
                        ["Security", "Unencrypted", "Encrypted and authenticated"],
                        ["Use Case", "Public content", "Sensitive transactions, login"]
                    ]},
                    {"type": "heading", "text": "DNS (Domain Name System)"},
                    {"type": "paragraph", "text": "The function of DNS is to translate human-readable domain names into machine-readable IP addresses to enable network communication."},
                    {"type": "table", "headers": ["Record Type", "Purpose"], "rows": [
                        ["A", "Maps a domain to an IPv4 address"],
                        ["AAAA", "Maps a domain to an IPv6 address"],
                        ["CNAME", "Alias for another domain (canonical name)"],
                        ["MX", "Identifies the mail exchange server for email delivery"]
                    ]},
                    {"type": "heading", "text": "ARP (Address Resolution Protocol)"},
                    {"type": "bullets", "items": [
                        "ARP maps an IP address (Layer 3) to a MAC address (Layer 2) on a LAN.",
                        "It is used in Ethernet and Wi-Fi networks.",
                        "It is required for any communication within a local subnet."
                    ]},
                    {"type": "callout", "variant": "danger", "text": "Security Risk: Malicious devices can send fake ARP replies to associate their MAC with another device's IP (man-in-the-middle attack)."}
                ]
            },
            {
                "slug": "common-attack-techniques",
                "title": "Common Attack Techniques",
                "summary": "Explore reconnaissance methods and Man-in-the-Middle (MITM) attacks.",
                "objectives": [
                    "Identify tools used for scanning, spoofing, and sniffing.",
                    "Explain concepts of MITM and ARP spoofing.",
                    "Differentiate TCP SYN scan and UDP scan."
                ],
                "topics": [
                    "MITM Attacks (ARP Spoofing)",
                    "Reconnaissance and Scanning with Nmap",
                    "OS Fingerprinting"
                ],
                "external_links": [
                    {"name": "HackTheBox", "url": "https://www.hackthebox.com/", "description": "A massive hacking playground and cybersecurity community."},
                    {"name": "TryHackMe \u2014 Jr Penetration Tester", "url": "https://tryhackme.com/path/outline/jrpenetrationtester", "description": "Learn the core methodologies and tools of a penetration tester."}
                ],
                "content": [
                    {"type": "heading", "text": "Attack Techniques Overview"},
                    {"type": "paragraph", "text": "Understanding how attackers map networks and intercept communications is vital. This module covers reconnaissance methods and Man-in-the-Middle (MITM) attacks."},
                    {"type": "heading", "text": "MITM and ARP Spoofing"},
                    {"type": "bullets", "items": [
                        "Use tools like arpspoof or ettercap to perform ARP poisoning.",
                        "Intercept unencrypted HTTP traffic flowing through the network.",
                        "Capture credentials and session cookies with Wireshark."
                    ]},
                    {"type": "heading", "text": "Scanning and Enumeration"},
                    {"type": "paragraph", "text": "Nmap is the premier tool for network discovery and security auditing."},
                    {"type": "table", "headers": ["Scan Type", "Description", "Example Command"], "rows": [
                        ["TCP SYN Scan", "Sends SYN packets to ports, waits for SYN-ACK", "nmap -sS 192.168.1.0/24"],
                        ["OS Fingerprinting", "Attempts to identify OS and version", "nmap -O target_ip"],
                        ["Service Detection", "Identifies software and versions running on ports", "nmap -sV target_ip"],
                        ["Aggressive Scan", "Combines OS detection, version detection, and scripts", "nmap -A target_ip"]
                    ]},
                    {"type": "callout", "variant": "info", "text": "Always ensure you have explicit written authorization before conducting scanning or spoofing activities against any network."}
                ]
            },
            {
                "slug": "network-defense-and-security",
                "title": "Network Defense and Security Measures",
                "summary": "Understand firewalls, IDS/IPS, and network segmentation.",
                "objectives": [
                    "Apply defensive measures to secure networks and systems.",
                    "Understand how to segment a network effectively.",
                    "Identify the roles of firewalls and IDS/IPS."
                ],
                "topics": [
                    "Firewalls",
                    "IDS/IPS",
                    "Network Segmentation",
                    "Best practices for securing a network"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Network Fundamentals", "url": "https://tryhackme.com/module/network-fundamentals", "description": "Learn how networks work and the concepts behind them."}
                ],
                "content": [
                    {"type": "heading", "text": "Defensive Measures"},
                    {"type": "paragraph", "text": "Organizations implement defensive measures to secure networks and systems against intrusions. These defenses operate at various layers of the network stack to detect, prevent, and respond to threats."},
                    {"type": "heading", "text": "Key Defensive Strategies"},
                    {"type": "bullets", "items": [
                        "Firewalls: Filter traffic based on predefined rules (IPs, ports, protocols).",
                        "Intrusion Detection Systems (IDS): Monitor network traffic for suspicious activity and alert administrators.",
                        "Intrusion Prevention Systems (IPS): Actively block or prevent detected intrusions.",
                        "Network Segmentation: Dividing a network into smaller, isolated subnets to limit exposure."
                    ]},
                    {"type": "callout", "variant": "info", "text": "Good network segmentation limits lateral movement. A flat network topology is highly vulnerable during an attack because a compromise of one device provides access to all others."}
                ]
            },
            {
                "slug": "virtual-lab-setup",
                "title": "Virtual Lab Setup and Simulation",
                "summary": "Configure Kali Linux and simulate secured and unsecured network environments.",
                "objectives": [
                    "Demonstrate a secure lab setup.",
                    "Configure secure systems in virtual lab environments.",
                    "Simulate secured and unsecured network environments."
                ],
                "topics": [
                    "Configuring Kali Linux",
                    "VirtualBox and GNS3",
                    "Simulating network environments"
                ],
                "external_links": [
                    {"name": "OverTheWire \u2014 Bandit", "url": "https://overthewire.org/wargames/bandit/", "description": "Wargame aimed at beginners for learning Linux."}
                ],
                "content": [
                    {"type": "heading", "text": "Lab Environment Setup"},
                    {"type": "paragraph", "text": "A secure, isolated lab environment is essential for analyzing network traffic and safely practicing cyber-attacks and defenses without risking production systems."},
                    {"type": "heading", "text": "Setup Requirements"},
                    {"type": "bullets", "items": [
                        "Install and configure Kali Linux as the attacker machine.",
                        "Use virtualization platforms like VirtualBox or VMware.",
                        "Build and configure network topologies using tools like GNS3 or packet tracer."
                    ]},
                    {"type": "callout", "variant": "info", "text": "Simulating secured and unsecured network environments side-by-side allows learners to compare traffic (e.g., HTTP vs HTTPS) and understand the practical value of encryption and secure protocols."}
                ]
            }
        ]
    },
    {
        "code": "DAET-FOE-CYT102",
        "title": "Windows Security Essentials",
        "description": "Understand Windows security mechanisms, group policies, and active directory.",
        "modules": [
            {
                "slug": "user-group-policies",
                "title": "User & Group Policies",
                "summary": "Configure local security policy, NTFS and share permissions.",
                "objectives": [
                    "Configure local security policies",
                    "Manage NTFS & share permissions",
                    "Enforce password policies"
                ],
                "topics": [
                    "gpedit.msc",
                    "Local Security Policy",
                    "NTFS Permissions"
                ],
                "external_links": [
                    {"name": "Microsoft Learn \u2014 Windows Security", "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security", "description": "Official Microsoft training for Windows security."},
                    {"name": "TryHackMe \u2014 Windows Fundamentals", "url": "https://tryhackme.com/module/windows-fundamentals", "description": "Learn the core basics of Windows operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "User & Group Policies"},
                    {"type": "paragraph", "text": "Windows provides powerful tools for configuring user rights, account policies, and file access. Understanding and configuring user and group policies is foundational to securing a Windows system."},
                    {"type": "heading", "text": "Key Tools and Concepts"},
                    {"type": "bullets", "items": [
                        "Configuring Local Security Policy (secpol.msc)",
                        "Managing NTFS (New Technology File System) & Share Permissions",
                        "Enforcing password length, complexity, and expiration policies via gpedit.msc"
                    ]},
                    {"type": "callout", "variant": "info", "text": "Proper access control using Group Policy and NTFS permissions is critical for protecting sensitive data from unauthorized local or network access."}
                ]
            },
            {
                "slug": "windows-defender-firewall",
                "title": "Windows Defender & Firewall",
                "summary": "Implement and configure real-time protection and custom firewall rules.",
                "objectives": [
                    "Enable real-time protection",
                    "Configure custom firewall rules",
                    "Block inbound RDP/ICMP traffic"
                ],
                "topics": [
                    "Microsoft Defender",
                    "Windows Firewall",
                    "Custom firewall rules"
                ],
                "external_links": [
                    {"name": "Microsoft Learn \u2014 Windows Security", "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security", "description": "Official Microsoft training for Windows security."},
                    {"name": "TryHackMe \u2014 Windows Fundamentals", "url": "https://tryhackme.com/module/windows-fundamentals", "description": "Learn the core basics of Windows operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "Windows Defender & Firewall"},
                    {"type": "paragraph", "text": "Windows Defender is an integrated anti-malware component that provides real-time protection. The Windows Firewall filters network data transmissions to and from your Windows system using a set of rules."},
                    {"type": "heading", "text": "Firewall Configuration"},
                    {"type": "bullets", "items": [
                        "Enabling real-time protection against spyware and malware.",
                        "Creating custom inbound and outbound firewall rules.",
                        "Blocking unnecessary inbound traffic, such as RDP (Remote Desktop Protocol) or ICMP (Ping)."
                    ]},
                    {"type": "callout", "variant": "danger", "text": "Never disable the firewall completely! Instead, create specific exceptions for the legitimate services your system needs to run."}
                ]
            },
            {
                "slug": "patch-management",
                "title": "Patch Management",
                "summary": "Apply service packs, hotfixes, and manage patches using Windows Update and WSUS.",
                "objectives": [
                    "Apply service packs and hotfixes",
                    "Use Windows Update and WSUS",
                    "Run MBSA scans to identify missing patches"
                ],
                "topics": [
                    "Windows Update",
                    "WSUS",
                    "MBSA Scan"
                ],
                "external_links": [
                    {"name": "Microsoft Learn \u2014 Windows Security", "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security", "description": "Official Microsoft training for Windows security."}
                ],
                "content": [
                    {"type": "heading", "text": "Patch Management"},
                    {"type": "paragraph", "text": "Patch management is the process of distributing and applying updates to software. Keeping systems secure by regularly applying updates is one of the most effective defenses against known vulnerabilities."},
                    {"type": "heading", "text": "Tools and Practices"},
                    {"type": "bullets", "items": [
                        "Applying service packs, security rollups, and hotfixes.",
                        "Using Windows Update for individual machines and WSUS (Windows Server Update Services) for enterprise management.",
                        "Running Microsoft Baseline Security Analyzer (MBSA) or similar modern scanning tools to identify missing patches."
                    ]}
                ]
            },
            {
                "slug": "active-directory-security",
                "title": "Active Directory Security",
                "summary": "Enforce policies using Group Policy Objects (GPOs).",
                "objectives": [
                    "Understand Active Directory basics",
                    "Create and manage Group Policy Objects",
                    "Enforce security configurations centrally"
                ],
                "topics": [
                    "Active Directory",
                    "Group Policy Objects (GPOs)",
                    "Security enforcement"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Windows Fundamentals", "url": "https://tryhackme.com/module/windows-fundamentals", "description": "Learn the core basics of Windows operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "Active Directory Security"},
                    {"type": "paragraph", "text": "Active Directory (AD) is a directory service developed by Microsoft for Windows domain networks. It manages computers and other devices on a network and enforces security policies centrally."},
                    {"type": "heading", "text": "Key Components"},
                    {"type": "bullets", "items": [
                        "Group Policy Objects (GPOs) for enterprise-wide enforcement of registry settings, security options, and software installation.",
                        "Securing AD infrastructure by limiting Domain Admin access.",
                        "Auditing AD changes to detect privilege escalation."
                    ]}
                ]
            },
            {
                "slug": "powershell-security",
                "title": "PowerShell for Security Automation",
                "summary": "Script user audits and log analysis with PowerShell.",
                "objectives": [
                    "Automate user privilege audits",
                    "Perform log analysis",
                    "Write basic PowerShell security scripts"
                ],
                "topics": [
                    "PowerShell Security Scripting",
                    "User audits automation",
                    "Log analysis"
                ],
                "external_links": [
                    {"name": "Microsoft Learn \u2014 Windows Security", "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security", "description": "Official Microsoft training for Windows security."}
                ],
                "content": [
                    {"type": "heading", "text": "PowerShell Security Automation"},
                    {"type": "paragraph", "text": "PowerShell is a task automation and configuration management framework. It provides full access to COM and WMI, enabling administrators to execute complex security audits and tasks automatically."},
                    {"type": "heading", "text": "Capabilities"},
                    {"type": "bullets", "items": [
                        "Scripting automated user and group privilege audits.",
                        "Parsing and analyzing Event Viewer logs at scale.",
                        "Enforcing security baselines across multiple servers rapidly."
                    ]}
                ]
            },
            {
                "slug": "backup-recovery",
                "title": "Backup & Recovery",
                "summary": "Configure Windows Backup and System Restore.",
                "objectives": [
                    "Configure Windows Backup",
                    "Set up System Restore",
                    "Perform data recovery"
                ],
                "topics": [
                    "Windows Backup",
                    "System Restore",
                    "Disaster recovery planning"
                ],
                "external_links": [
                    {"name": "Microsoft Learn \u2014 Windows Security", "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security", "description": "Official Microsoft training for Windows security."}
                ],
                "content": [
                    {"type": "heading", "text": "Backup & Recovery"},
                    {"type": "paragraph", "text": "A robust backup strategy ensures data availability and business continuity in the event of hardware failures, accidental deletion, or destructive attacks like ransomware."},
                    {"type": "heading", "text": "Disaster Recovery Tools"},
                    {"type": "bullets", "items": [
                        "Windows Backup for creating image-based or file-level backups of critical systems.",
                        "System Restore for rolling back the operating system state, registries, and drivers to a known-good point.",
                        "Testing backups regularly to ensure data can actually be recovered when needed."
                    ]}
                ]
            }
        ]
    },
    {
        "code": "DAET-FOE-CYT103",
        "title": "Linux Security Essentials",
        "description": "Learn Linux security essentials including permissions, MAC, and network security.",
        "modules": [
            {
                "slug": "permissions-user-management",
                "title": "Permissions & User Management",
                "summary": "Manage /etc/passwd, /etc/shadow, groups, and password policies.",
                "objectives": [
                    "Manage Linux user accounts",
                    "Configure secure password policies",
                    "Understand file ownership and sticky bits"
                ],
                "topics": [
                    "File ownership, rwxr permissions, sticky bits",
                    "sudo configuration & least privilege",
                    "/etc/passwd and /etc/shadow"
                ],
                "external_links": [
                    {"name": "OverTheWire \u2014 Bandit", "url": "https://overthewire.org/wargames/bandit/", "description": "Wargame aimed at absolute beginners for learning Linux commands."},
                    {"name": "TryHackMe \u2014 Linux Fundamentals", "url": "https://tryhackme.com/module/linux-fundamentals", "description": "Learn how to use Linux operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "User and Group Accounts"},
                    {"type": "paragraph", "text": "User accounts are essential components of Linux operating systems, providing the foundation for user access, security, and system management. Each login session is tied to a specific user identity, enabling the OS to enforce user-specific policies."},
                    {"type": "heading", "text": "Account Information Files"},
                    {"type": "table", "headers": ["File", "Description"], "rows": [
                        ["/etc/passwd", "Primary file storing basic user account details (UID, GID, home directory)."],
                        ["/etc/shadow", "Holds hashed user passwords and password-related metadata. Readable only by root."],
                        ["/etc/group", "Contains group account data specifying which users belong to which groups."],
                        ["/etc/gshadow", "Stores secure group password data and administrative permissions."]
                    ]},
                    {"type": "heading", "text": "User Private Groups (UPGs)"},
                    {"type": "bullets", "items": [
                        "A new group is automatically created for each user when the user account is created.",
                        "Each user's files are owned by a private group, isolating access.",
                        "Ensures better default file security compared to traditional shared groups."
                    ]},
                    {"type": "callout", "variant": "warning", "text": "The root user has UID 0 and holds superuser privileges. Audit all users with UID 0 to detect potential unauthorized access."}
                ]
            },
            {
                "slug": "service-hardening",
                "title": "Service Hardening",
                "summary": "Disable unnecessary services and secure SSH.",
                "objectives": [
                    "Disable unnecessary services",
                    "Secure SSH (key-based auth, disable root login)",
                    "Configure PAM"
                ],
                "topics": [
                    "systemctl disable",
                    "Securing SSH",
                    "Pluggable Authentication Modules (PAM)"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Linux Fundamentals", "url": "https://tryhackme.com/module/linux-fundamentals", "description": "Learn how to use Linux operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "Disabling Services and Securing Access"},
                    {"type": "paragraph", "text": "Service hardening involves minimizing the attack surface by disabling unnecessary services (using systemctl disable) and securing essential ones like SSH. Best practices for SSH include using key-based authentication and disabling root login."},
                    {"type": "heading", "text": "PAM (Pluggable Authentication Modules)"},
                    {"type": "paragraph", "text": "PAM is a powerful tool that allows an administrator to provide restrictions to user accounts, such as limiting access by time or resource utilization. It is called by authentication-based software like local login and SSH."},
                    {"type": "table", "headers": ["PAM Category", "Description"], "rows": [
                        ["account", "Verifies if a user account has the rights to use a service."],
                        ["auth", "Authenticates that the user is who they claim to be."],
                        ["password", "Updates authentication methods like providing a new password."],
                        ["session", "Performs actions prior to and after a service has been provided."]
                    ]},
                    {"type": "callout", "variant": "danger", "text": "Be very careful when changing PAM configuration files. Misconfigurations can easily lock the root account out of the system!"}
                ]
            },
            {
                "slug": "mac-policies",
                "title": "Mandatory Access Control (MAC)",
                "summary": "Configure SELinux and AppArmor policies.",
                "objectives": [
                    "Understand Mandatory Access Control",
                    "Configure SELinux policies",
                    "Implement AppArmor profiles"
                ],
                "topics": [
                    "SELinux",
                    "AppArmor policies",
                    "Security Contexts"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Linux Fundamentals", "url": "https://tryhackme.com/module/linux-fundamentals", "description": "Learn how to use Linux operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "Mandatory Access Control"},
                    {"type": "paragraph", "text": "Mandatory Access Control (MAC) systems, such as SELinux and AppArmor, enforce security policies that confine user programs and system services to the minimum amount of privilege they require to function."},
                    {"type": "heading", "text": "Implementation Details"},
                    {"type": "bullets", "items": [
                        "SELinux assigns security contexts to files and processes, ensuring that a compromised service cannot access unauthorized files.",
                        "AppArmor uses file paths to restrict programs' capabilities.",
                        "You can configure SELinux policies to restrict web servers like Apache or Nginx strictly to their document roots."
                    ]}
                ]
            },
            {
                "slug": "network-security",
                "title": "Network Security",
                "summary": "Configure iptables and UFW for traffic filtering.",
                "objectives": [
                    "Configure iptables",
                    "Configure UFW (Uncomplicated Firewall)",
                    "Filter network traffic"
                ],
                "topics": [
                    "iptables",
                    "nftables",
                    "UFW"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Linux Fundamentals", "url": "https://tryhackme.com/module/linux-fundamentals", "description": "Learn how to use Linux operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "Firewalls and Traffic Filtering"},
                    {"type": "paragraph", "text": "Network security on Linux involves configuring robust firewalls to block unauthorized access while allowing legitimate traffic."},
                    {"type": "heading", "text": "Tools"},
                    {"type": "bullets", "items": [
                        "iptables and nftables: Powerful command-line tools for packet filtering and NAT.",
                        "UFW (Uncomplicated Firewall): A user-friendly frontend for managing iptables rules.",
                        "Common configurations include allowing SSH (port 22) and Web traffic (ports 80/443) while dropping all other incoming connections."
                    ]}
                ]
            },
            {
                "slug": "file-integrity",
                "title": "File Integrity & Monitoring",
                "summary": "Set up AIDE or Tripwire for intrusion detection.",
                "objectives": [
                    "Set up AIDE/Tripwire",
                    "Detect unauthorized changes in /etc",
                    "Verify file hashes using md5sum"
                ],
                "topics": [
                    "AIDE",
                    "Tripwire",
                    "md5sum"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Linux Fundamentals", "url": "https://tryhackme.com/module/linux-fundamentals", "description": "Learn how to use Linux operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "File Integrity Monitoring"},
                    {"type": "paragraph", "text": "File Integrity Monitoring (FIM) tools are used to detect unauthorized changes to critical system files, which could indicate a compromise or malware installation."},
                    {"type": "heading", "text": "Common Tools"},
                    {"type": "bullets", "items": [
                        "AIDE (Advanced Intrusion Detection Environment) takes a snapshot of file hashes and permissions, then regularly checks the live system against this baseline.",
                        "Tripwire operates similarly, alerting administrators to unexpected modifications in directories like /etc and /bin.",
                        "md5sum or sha256sum can be used manually to verify the integrity of individual files."
                    ]}
                ]
            },
            {
                "slug": "container-security",
                "title": "Container Security",
                "summary": "Harden Docker and run read-only containers.",
                "objectives": [
                    "Harden Docker containers",
                    "Drop capabilities (--cap-drop)",
                    "Run read-only containers"
                ],
                "topics": [
                    "Docker hardening",
                    "Capabilities",
                    "Read-only containers"
                ],
                "external_links": [
                    {"name": "TryHackMe \u2014 Linux Fundamentals", "url": "https://tryhackme.com/module/linux-fundamentals", "description": "Learn how to use Linux operating systems."}
                ],
                "content": [
                    {"type": "heading", "text": "Container Security"},
                    {"type": "paragraph", "text": "Securing containerized environments involves running containers with the least required privileges to prevent container breakouts."},
                    {"type": "heading", "text": "Hardening Techniques"},
                    {"type": "bullets", "items": [
                        "Dropping Linux capabilities using '--cap-drop' to remove unnecessary privileges from the container root user.",
                        "Running containers with a read-only filesystem to prevent attackers from writing malicious payloads.",
                        "Ensuring Docker daemon is properly secured and not exposed without authentication."
                    ]},
                    {"type": "callout", "variant": "info", "text": "Always run a container with minimal privileges to reduce the impact of a potential compromise."}
                ]
            }
        ]
    },
    {
        "code": "DAET-AKS-CYT201",
        "title": "Cryptography",
        "description": "Understand encryption, hashing, and secure communication protocols.",
        "modules": [
            {
                "slug": "hashing-encryption",
                "title": "Hashing and Encryption",
                "summary": "Compare MD5, SHA, RSA, and AES functions.",
                "objectives": [
                    "Compare MD5, SHA-1, and SHA-256",
                    "Understand RSA and AES encryption",
                    "Encrypt and decrypt files"
                ],
                "topics": [
                    "MD5, SHA",
                    "RSA, AES",
                    "Symmetric vs Asymmetric Encryption",
                    "GPG and OpenSSL"
                ],
                "external_links": [
                    {"name": "CryptoHack", "url": "https://cryptohack.org/", "description": "A fun, free platform for learning cryptography."},
                    {"name": "CyberChef", "url": "https://gchq.github.io/CyberChef/", "description": "The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis."}
                ],
                "content": [
                    {"type": "heading", "text": "Hashing vs Encryption"},
                    {"type": "paragraph", "text": "Understand the differences between hashing and encryption, and the common algorithms used for each. Encryption is a two-way process for confidentiality, while hashing is a one-way process for data integrity."},
                    {"type": "heading", "text": "Core Concepts"},
                    {"type": "bullets", "items": [
                        "Compare MD5, SHA-1, and SHA-256 hashing functions. Note that MD5 is considered cryptographically broken.",
                        "Symmetric vs Asymmetric Encryption: Symmetric uses one key (AES), while asymmetric uses a public/private key pair (RSA).",
                        "Encrypt and decrypt files using GPG and OpenSSL."
                    ]},
                    {"type": "callout", "variant": "warning", "text": "Never use MD5 or SHA-1 for securing new data. Always opt for modern standards like SHA-256 or SHA-3."}
                ]
            },
            {
                "slug": "tls-protocol",
                "title": "TLS Protocol and Encrypted Communication",
                "summary": "Analyze TLS handshakes and secure email communication.",
                "objectives": [
                    "Analyze TLS handshake in Wireshark",
                    "Exchange encrypted and signed emails",
                    "Understand PKI basics"
                ],
                "topics": [
                    "TLS Protocol",
                    "Encrypted email communication",
                    "Wireshark TLS analysis"
                ],
                "external_links": [
                    {"name": "CryptoHack", "url": "https://cryptohack.org/", "description": "A fun, free platform for learning cryptography."},
                    {"name": "CyberChef", "url": "https://gchq.github.io/CyberChef/", "description": "The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis."}
                ],
                "content": [
                    {"type": "heading", "text": "TLS Protocol"},
                    {"type": "paragraph", "text": "Transport Layer Security (TLS) ensures encrypted communication over a network, providing confidentiality, data integrity, and authentication."},
                    {"type": "heading", "text": "Implementation and Analysis"},
                    {"type": "bullets", "items": [
                        "Analyze the TLS handshake process using Wireshark to understand how keys are exchanged securely.",
                        "Exchange encrypted and signed emails using GPG to learn how PGP web of trust works.",
                        "Understand Public Key Infrastructure (PKI) basics, including Certificate Authorities (CAs)."
                    ]}
                ]
            },
            {
                "slug": "secure-passwords",
                "title": "Secure Password Creation and Password Cracking",
                "summary": "Create secure passwords and use tools like John the Ripper.",
                "objectives": [
                    "Create strong, secure passwords",
                    "Perform password cracking exercises",
                    "Understand credential storage"
                ],
                "topics": [
                    "Secure password creation",
                    "Password cracking",
                    "John the Ripper"
                ],
                "external_links": [
                    {"name": "CryptoHack", "url": "https://cryptohack.org/", "description": "A fun, free platform for learning cryptography."},
                    {"name": "CyberChef", "url": "https://gchq.github.io/CyberChef/", "description": "The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis."}
                ],
                "content": [
                    {"type": "heading", "text": "Password Security"},
                    {"type": "paragraph", "text": "Creating secure passwords and testing their strength against cracking tools is essential for credential security and policy enforcement."},
                    {"type": "heading", "text": "Tools and Methods"},
                    {"type": "bullets", "items": [
                        "Offline password cracking using tools like John the Ripper or Hashcat.",
                        "Understanding different password hashing formats (e.g., bcrypt, SHA-512 crypt) and the role of salts.",
                        "Developing password policies that resist dictionary and brute-force attacks."
                    ]},
                    {"type": "callout", "variant": "info", "text": "Always use strong, complex passwords combined with Multi-Factor Authentication (MFA) to fully protect critical accounts."}
                ]
            }
        ]
    },
    {
        "code": "DAET-AKS-CYT202",
        "title": "Web Security",
        "description": "Learn to identify and mitigate common web vulnerabilities.",
        "modules": [
            {
                "slug": "owasp-top-10",
                "title": "OWASP Top 10",
                "summary": "Understand SQL Injection, XSS, and other top vulnerabilities.",
                "objectives": [
                    "Understand the OWASP Top 10",
                    "Exploit vulnerable web apps with SQL injection",
                    "Execute XSS attacks and demonstrate mitigation"
                ],
                "topics": [
                    "OWASP Top 10",
                    "SQL Injection (SQLi)",
                    "Cross-Site Scripting (XSS)",
                    "Firewalls"
                ],
                "external_links": [
                    {"name": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security", "description": "Free, interactive web security training."},
                    {"name": "OWASP Juice Shop", "url": "https://owasp.org/www-project-juice-shop/", "description": "Probably the most modern and sophisticated insecure web application."},
                    {"name": "TryHackMe \u2014 OWASP Top 10", "url": "https://tryhackme.com/room/owasptop10", "description": "Learn about and exploit each of the OWASP Top 10 vulnerabilities."}
                ],
                "content": [
                    {"type": "heading", "text": "OWASP Top 10"},
                    {"type": "paragraph", "text": "The OWASP Top 10 is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications."},
                    {"type": "heading", "text": "Primary Vulnerabilities"},
                    {"type": "bullets", "items": [
                        "SQL Injection (SQLi): Occurs when untrusted data is sent to an interpreter as part of a command or query.",
                        "Cross-Site Scripting (XSS): Occurs when an application includes untrusted data in a web page without proper validation or escaping.",
                        "Exploiting vulnerable web apps (e.g., DVWA) in a safe lab environment to understand attacker methodology."
                    ]}
                ]
            },
            {
                "slug": "session-hijacking",
                "title": "Session Hijacking and Cookie Manipulation",
                "summary": "Learn how attackers manipulate sessions and cookies using proxies.",
                "objectives": [
                    "Understand session management vulnerabilities",
                    "Use ZAP Proxy to hijack sessions",
                    "Manipulate cookies"
                ],
                "topics": [
                    "Session Hijacking",
                    "Cookie Manipulation",
                    "ZAP Proxy / Burp Suite"
                ],
                "external_links": [
                    {"name": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security", "description": "Free, interactive web security training."},
                    {"name": "OWASP Juice Shop", "url": "https://owasp.org/www-project-juice-shop/", "description": "Probably the most modern and sophisticated insecure web application."},
                    {"name": "TryHackMe \u2014 OWASP Top 10", "url": "https://tryhackme.com/room/owasptop10", "description": "Learn about and exploit each of the OWASP Top 10 vulnerabilities."}
                ],
                "content": [
                    {"type": "heading", "text": "Session Hijacking"},
                    {"type": "paragraph", "text": "Session hijacking involves exploiting a valid computer session to gain unauthorized access to information or services in a computer system."},
                    {"type": "heading", "text": "Attack Techniques"},
                    {"type": "bullets", "items": [
                        "Using interception proxies like OWASP ZAP or Burp Suite to capture and inspect HTTP requests.",
                        "Manipulating session cookies to bypass authentication controls.",
                        "Understanding mitigation strategies like Secure and HttpOnly cookie flags."
                    ]}
                ]
            },
            {
                "slug": "secure-login-systems",
                "title": "Secure Login Systems",
                "summary": "Write a secure login system using HTTPS and hashed passwords.",
                "objectives": [
                    "Implement HTTPS",
                    "Securely hash and salt passwords",
                    "Build a secure login workflow"
                ],
                "topics": [
                    "HTTPS",
                    "Password hashing (bcrypt/Argon2)",
                    "Secure Login Systems"
                ],
                "external_links": [
                    {"name": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security", "description": "Free, interactive web security training."},
                    {"name": "OWASP Juice Shop", "url": "https://owasp.org/www-project-juice-shop/", "description": "Probably the most modern and sophisticated insecure web application."},
                    {"name": "TryHackMe \u2014 OWASP Top 10", "url": "https://tryhackme.com/room/owasptop10", "description": "Learn about and exploit each of the OWASP Top 10 vulnerabilities."}
                ],
                "content": [
                    {"type": "heading", "text": "Secure Login Systems"},
                    {"type": "paragraph", "text": "Building secure authentication mechanisms requires proper implementation of transport layer encryption and secure storage of user credentials."},
                    {"type": "heading", "text": "Best Practices"},
                    {"type": "bullets", "items": [
                        "Enforce HTTPS across all authentication endpoints to prevent credential sniffing.",
                        "Hash passwords securely using modern algorithms like bcrypt or Argon2, incorporating unique salts for every user.",
                        "Implement account lockout mechanisms to prevent brute-force attacks."
                    ]}
                ]
            }
        ]
    },
    {
        "code": "DAET-AKS-CYT203",
        "title": "Ethical Hacking and Penetration Testing",
        "description": "Perform reconnaissance, scanning, and system exploitation.",
        "modules": [
            {
                "slug": "reconnaissance",
                "title": "Passive and Active Reconnaissance",
                "summary": "Footprinting, banner grabbing, and gathering information on targets.",
                "objectives": [
                    "Conduct passive information gathering",
                    "Use WHOIS, DNS, and Google dorking",
                    "Perform banner grabbing"
                ],
                "topics": [
                    "Passive and Active Reconnaissance",
                    "Footprinting",
                    "Banner grabbing",
                    "WHOIS, DNS, Google dorking"
                ],
                "external_links": [
                    {"name": "HackTheBox", "url": "https://www.hackthebox.com/", "description": "A massive hacking playground and cybersecurity community."},
                    {"name": "TryHackMe \u2014 Jr Penetration Tester", "url": "https://tryhackme.com/path/outline/jrpenetrationtester", "description": "Learn the core methodologies and tools of a penetration tester."},
                    {"name": "picoCTF", "url": "https://picoctf.org/", "description": "A free computer security education program."}
                ],
                "content": [
                    {"type": "heading", "text": "Reconnaissance"},
                    {"type": "paragraph", "text": "Reconnaissance is the first phase of ethical hacking, involving gathering information about a target before launching an attack. This data informs the strategy for the rest of the penetration test."},
                    {"type": "heading", "text": "Information Gathering"},
                    {"type": "bullets", "items": [
                        "Conduct passive information gathering using public records (WHOIS, DNS records) to map the target's external footprint.",
                        "Utilize advanced search engine operators (Google Dorking) to find exposed files and sensitive information.",
                        "Perform active footprinting and banner grabbing to identify service versions running on open ports."
                    ]}
                ]
            },
            {
                "slug": "scanning-enumeration",
                "title": "Scanning and Enumeration",
                "summary": "Discover network services using Nmap and Netcat.",
                "objectives": [
                    "Perform network scanning",
                    "Enumerate services using Nmap and Netcat",
                    "Analyze and document service enumeration results"
                ],
                "topics": [
                    "Scanning and Enumeration",
                    "Nmap",
                    "Netcat"
                ],
                "external_links": [
                    {"name": "HackTheBox", "url": "https://www.hackthebox.com/", "description": "A massive hacking playground and cybersecurity community."},
                    {"name": "TryHackMe \u2014 Jr Penetration Tester", "url": "https://tryhackme.com/path/outline/jrpenetrationtester", "description": "Learn the core methodologies and tools of a penetration tester."},
                    {"name": "picoCTF", "url": "https://picoctf.org/", "description": "A free computer security education program."}
                ],
                "content": [
                    {"type": "heading", "text": "Scanning and Enumeration"},
                    {"type": "paragraph", "text": "After reconnaissance, attackers scan the network to discover live hosts, open ports, and running services. Enumeration extracts detailed information such as user names, machine names, and network resources."},
                    {"type": "heading", "text": "Techniques and Tools"},
                    {"type": "bullets", "items": [
                        "Perform scanning and service enumeration using tools like Nmap and Netcat.",
                        "Extract SMB shares, SNMP data, and user lists from target machines.",
                        "Analyze and document service enumeration results to identify potential exploitation vectors."
                    ]}
                ]
            },
            {
                "slug": "system-exploitation",
                "title": "Brute Force Attacks and System Exploitation",
                "summary": "Run brute force attacks with Hydra and exploit systems using Metasploit.",
                "objectives": [
                    "Run brute force login attacks using Hydra",
                    "Work with the Metasploit Framework",
                    "Exploit system vulnerabilities"
                ],
                "topics": [
                    "Brute force attacks",
                    "System exploitation",
                    "Hydra",
                    "Metasploit"
                ],
                "external_links": [
                    {"name": "HackTheBox", "url": "https://www.hackthebox.com/", "description": "A massive hacking playground and cybersecurity community."},
                    {"name": "TryHackMe \u2014 Jr Penetration Tester", "url": "https://tryhackme.com/path/outline/jrpenetrationtester", "description": "Learn the core methodologies and tools of a penetration tester."},
                    {"name": "picoCTF", "url": "https://picoctf.org/", "description": "A free computer security education program."}
                ],
                "content": [
                    {"type": "heading", "text": "System Exploitation"},
                    {"type": "paragraph", "text": "Exploitation involves taking advantage of discovered vulnerabilities to gain unauthorized access to a system or application."},
                    {"type": "heading", "text": "Exploitation Methods"},
                    {"type": "bullets", "items": [
                        "Run online brute force login attacks against services (e.g., SSH, FTP) using THC Hydra.",
                        "Work with the Metasploit Framework to select and deploy pre-packaged exploits against vulnerable targets.",
                        "Understand payload generation, reverse shells, and post-exploitation basics."
                    ]}
                ]
            },
            {
                "slug": "ctf-practice",
                "title": "CTF Practice Challenge",
                "summary": "Complete mini CTFs to practice and apply learned exploitation methods.",
                "objectives": [
                    "Complete mini CTF challenges",
                    "Report all flags and exploit methods",
                    "Identify vulnerabilities and recover evidence"
                ],
                "topics": [
                    "CTF practice",
                    "Flag reporting",
                    "Vulnerability identification"
                ],
                "external_links": [
                    {"name": "HackTheBox", "url": "https://www.hackthebox.com/", "description": "A massive hacking playground and cybersecurity community."},
                    {"name": "TryHackMe \u2014 Jr Penetration Tester", "url": "https://tryhackme.com/path/outline/jrpenetrationtester", "description": "Learn the core methodologies and tools of a penetration tester."},
                    {"name": "picoCTF", "url": "https://picoctf.org/", "description": "A free computer security education program."}
                ],
                "content": [
                    {"type": "heading", "text": "CTF Practice"},
                    {"type": "paragraph", "text": "Capture The Flag (CTF) challenges simulate real-world scenarios to practice and refine ethical hacking skills in a legal, safe environment."},
                    {"type": "heading", "text": "Challenge Objectives"},
                    {"type": "bullets", "items": [
                        "Complete mini CTFs covering web exploitation, cryptography, reverse engineering, and forensics.",
                        "Document and report all captured flags alongside the specific exploit methods used.",
                        "Identify vulnerabilities and recover forensic evidence."
                    ]}
                ]
            }
        ]
    },
    {
        "code": "DAET-CYT-GLI-401",
        "title": "Advanced Topics in CyberTech and Projects",
        "description": "Apply all acquired cybersecurity knowledge in a final Red vs Blue scenario.",
        "modules": [
            {
                "slug": "capstone-ctf",
                "title": "Capstone: Final Team-Based CTF Challenge",
                "summary": "Apply acquired knowledge and tools to complete a structured Red vs Blue CTF.",
                "objectives": [
                    "Apply cybersecurity knowledge in a real-world scenario",
                    "Participate in a multi-stage CTF with working tools and exploits",
                    "Document flags, methodologies, and lessons learned"
                ],
                "topics": [
                    "Red vs Blue CTF",
                    "Secure login systems / Vulnerable apps",
                    "Malware analysis / Wireless pentesting",
                    "Phishing awareness"
                ],
                "external_links": [
                    {"name": "picoCTF", "url": "https://picoctf.org/", "description": "A free computer security education program."},
                    {"name": "CTFtime", "url": "https://ctftime.org/", "description": "The most comprehensive CTF tracking platform."},
                    {"name": "Internal Challenges", "url": "/challenges", "description": "EGATE's own challenge platform for hands-on practice."}
                ],
                "content": [
                    {"type": "heading", "text": "Capstone Project"},
                    {"type": "paragraph", "text": "Apply all acquired cybersecurity knowledge and tools to complete a structured Red vs Blue CTF scenario in teams. This capstone serves as a showcase project for academic advancement or internships."},
                    {"type": "heading", "text": "Example Capstone Topics"},
                    {"type": "bullets", "items": [
                        "Build a secure login system with multi-factor authentication.",
                        "Create a vulnerable app for ethical hacking and patch tracking.",
                        "Perform malware analysis and generate detection rules.",
                        "Simulate and document a wireless penetration test.",
                        "Develop and test a phishing awareness toolkit."
                    ]},
                    {"type": "callout", "variant": "info", "text": "Learners will demonstrate practical mastery of cybersecurity concepts, tools, and teamwork in a simulated real-world challenge. Full documentation of flags and methodologies is required."}
                ]
            }
        ]
    }
]

with open('app/courses/data.py', 'w', encoding='utf-8') as f:
    f.write("COURSES = ")
    f.write(json.dumps(COURSES, indent=4))
    f.write("\n")
