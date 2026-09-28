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
                    {
                        "name": "TryHackMe \u2014 Pre Security Path",
                        "url": "https://tryhackme.com/path/outline/presecurity",
                        "description": "Free guided path covering the fundamentals."
                    },
                    {
                        "name": "Cisco Networking Academy \u2014 Intro to Cybersecurity",
                        "url": "https://www.netacad.com/courses/cybersecurity",
                        "description": "Free course from Cisco on cybersecurity basics."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "What is Cybersecurity?"
                    },
                    {
                        "type": "paragraph",
                        "text": "Cybersecurity is the practice of protecting computer systems, networks, programs, and data from digital attacks, unauthorized access, and other vulnerabilities that can lead to compromise or loss."
                    },
                    {
                        "type": "heading",
                        "text": "The CIA Triad"
                    },
                    {
                        "type": "paragraph",
                        "text": "The CIA Triad is the foundational model for securing information systems. It represents three core principles:"
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Principle",
                            "Description",
                            "Example"
                        ],
                        "rows": [
                            [
                                "Confidentiality",
                                "Preventing unauthorized access to information",
                                "Encryption, Access controls"
                            ],
                            [
                                "Integrity",
                                "Assuring data is not altered or destroyed improperly",
                                "Hashing, Digital signatures"
                            ],
                            [
                                "Availability",
                                "Ensuring data and systems are accessible when needed",
                                "Backups, DoS protection"
                            ]
                        ]
                    },
                    {
                        "type": "heading",
                        "text": "The Threat Landscape"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Malware \u2014 viruses, worms, trojans",
                            "Phishing \u2014 social engineering to steal credentials",
                            "Ransomware \u2014 encrypts data and demands payment",
                            "Social Engineering \u2014 exploiting human psychology"
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Every attack targets one or more pillars of the CIA Triad. Ask yourself: is the attacker trying to read data (Confidentiality), change data (Integrity), or block access (Availability)?"
                    }
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
                    {
                        "name": "TryHackMe \u2014 Network Fundamentals",
                        "url": "https://tryhackme.com/module/network-fundamentals",
                        "description": "Learn how networks work and the concepts behind them."
                    },
                    {
                        "name": "Professor Messer \u2014 Network+",
                        "url": "https://www.professormesser.com/network-plus/n10-009/n10-009-training-course/",
                        "description": "Comprehensive CompTIA Network+ training."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "OSI vs TCP/IP Models"
                    },
                    {
                        "type": "paragraph",
                        "text": "Networking relies on structured models to ensure seamless communication across different hardware and software."
                    },
                    {
                        "type": "table",
                        "headers": [
                            "OSI Layer",
                            "TCP/IP Layer",
                            "Function"
                        ],
                        "rows": [
                            [
                                "7. Application",
                                "Application",
                                "End-user processes (HTTP, FTP)"
                            ],
                            [
                                "6. Presentation",
                                "Application",
                                "Data representation and encryption"
                            ],
                            [
                                "5. Session",
                                "Application",
                                "Interhost communication"
                            ],
                            [
                                "4. Transport",
                                "Transport",
                                "End-to-end connections (TCP, UDP)"
                            ],
                            [
                                "3. Network",
                                "Internet",
                                "Path determination and IP addressing"
                            ],
                            [
                                "2. Data Link",
                                "Network Access",
                                "MAC addressing and switching"
                            ],
                            [
                                "1. Physical",
                                "Network Access",
                                "Media, signal and binary transmission"
                            ]
                        ]
                    },
                    {
                        "type": "heading",
                        "text": "IP Addressing"
                    },
                    {
                        "type": "paragraph",
                        "text": "IP addresses uniquely identify devices on a network. We primarily use IPv4 (32-bit) and IPv6 (128-bit)."
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "IPv4 Example: 192.168.1.1",
                            "IPv6 Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                            "Subnetting divides a larger network into smaller, manageable sub-networks."
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "warning",
                        "text": "IPv4 addresses are exhausted! That's why NAT (Network Address Translation) and IPv6 were developed."
                    }
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
                    {
                        "name": "Wireshark Sample Captures",
                        "url": "https://wiki.wireshark.org/SampleCaptures",
                        "description": "Sample packet captures for practice."
                    },
                    {
                        "name": "TryHackMe \u2014 Wireshark 101",
                        "url": "https://tryhackme.com/room/wireshark",
                        "description": "Learn the basics of Wireshark."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Packet Analysis Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master packet analysis. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "HackTheBox",
                        "url": "https://www.hackthebox.com/",
                        "description": "A massive hacking playground and cybersecurity community."
                    },
                    {
                        "name": "TryHackMe \u2014 Jr Penetration Tester",
                        "url": "https://tryhackme.com/path/outline/jrpenetrationtester",
                        "description": "Learn the core methodologies and tools of a penetration tester."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Common Attack Techniques Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master common attack techniques. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "TryHackMe \u2014 Network Fundamentals",
                        "url": "https://tryhackme.com/module/network-fundamentals",
                        "description": "Learn how networks work and the concepts behind them."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Network Defense and Security Measures Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master network defense and security measures. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "OverTheWire \u2014 Bandit",
                        "url": "https://overthewire.org/wargames/bandit/",
                        "description": "Wargame aimed at beginners for learning Linux."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Virtual Lab Setup and Simulation Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master virtual lab setup and simulation. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "Microsoft Learn \u2014 Windows Security",
                        "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security",
                        "description": "Official Microsoft training for Windows security."
                    },
                    {
                        "name": "TryHackMe \u2014 Windows Fundamentals",
                        "url": "https://tryhackme.com/module/windows-fundamentals",
                        "description": "Learn the core basics of Windows operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "User & Group Policies Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master user & group policies. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "Microsoft Learn \u2014 Windows Security",
                        "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security",
                        "description": "Official Microsoft training for Windows security."
                    },
                    {
                        "name": "TryHackMe \u2014 Windows Fundamentals",
                        "url": "https://tryhackme.com/module/windows-fundamentals",
                        "description": "Learn the core basics of Windows operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Windows Defender Overview"
                    },
                    {
                        "type": "paragraph",
                        "text": "Windows Defender is an integrated anti-malware component of Windows. It provides real-time protection against software threats like viruses, malware, and spyware across email, apps, the cloud, and the web."
                    },
                    {
                        "type": "heading",
                        "text": "Windows Firewall"
                    },
                    {
                        "type": "paragraph",
                        "text": "The Windows Firewall filters network data transmissions to and from your Windows system. It relies on a set of rules to determine what traffic is allowed."
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Rule Type",
                            "Description",
                            "Usage"
                        ],
                        "rows": [
                            [
                                "Inbound",
                                "Controls traffic coming into the system.",
                                "Block untrusted incoming connections (e.g., block external RDP)."
                            ],
                            [
                                "Outbound",
                                "Controls traffic originating from the system.",
                                "Prevent malware from phoning home."
                            ],
                            [
                                "Connection Security",
                                "Secures traffic using IPsec.",
                                "Encrypt data between two specific servers."
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "danger",
                        "text": "Never disable the firewall completely! Instead, create specific exceptions for the services you need."
                    }
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
                    {
                        "name": "Microsoft Learn \u2014 Windows Security",
                        "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security",
                        "description": "Official Microsoft training for Windows security."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Patch Management Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master patch management. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "TryHackMe \u2014 Windows Fundamentals",
                        "url": "https://tryhackme.com/module/windows-fundamentals",
                        "description": "Learn the core basics of Windows operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Active Directory Security Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master active directory security. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "Microsoft Learn \u2014 Windows Security",
                        "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security",
                        "description": "Official Microsoft training for Windows security."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "PowerShell for Security Automation Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master powershell for security automation. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "Microsoft Learn \u2014 Windows Security",
                        "url": "https://learn.microsoft.com/en-us/training/browse/?terms=windows%20security",
                        "description": "Official Microsoft training for Windows security."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Backup & Recovery Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master backup & recovery. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "OverTheWire \u2014 Bandit",
                        "url": "https://overthewire.org/wargames/bandit/",
                        "description": "Wargame aimed at absolute beginners for learning Linux commands."
                    },
                    {
                        "name": "TryHackMe \u2014 Linux Fundamentals",
                        "url": "https://tryhackme.com/module/linux-fundamentals",
                        "description": "Learn how to use Linux operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Permissions & User Management Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master permissions & user management. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "TryHackMe \u2014 Linux Fundamentals",
                        "url": "https://tryhackme.com/module/linux-fundamentals",
                        "description": "Learn how to use Linux operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Service Hardening Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master service hardening. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "TryHackMe \u2014 Linux Fundamentals",
                        "url": "https://tryhackme.com/module/linux-fundamentals",
                        "description": "Learn how to use Linux operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Mandatory Access Control (MAC) Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master mandatory access control (mac). Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "TryHackMe \u2014 Linux Fundamentals",
                        "url": "https://tryhackme.com/module/linux-fundamentals",
                        "description": "Learn how to use Linux operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Network Security Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master network security. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "TryHackMe \u2014 Linux Fundamentals",
                        "url": "https://tryhackme.com/module/linux-fundamentals",
                        "description": "Learn how to use Linux operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "File Integrity & Monitoring Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master file integrity & monitoring. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "TryHackMe \u2014 Linux Fundamentals",
                        "url": "https://tryhackme.com/module/linux-fundamentals",
                        "description": "Learn how to use Linux operating systems."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Container Security Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master container security. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "CryptoHack",
                        "url": "https://cryptohack.org/",
                        "description": "A fun, free platform for learning cryptography."
                    },
                    {
                        "name": "CyberChef",
                        "url": "https://gchq.github.io/CyberChef/",
                        "description": "The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Hashing vs Encryption"
                    },
                    {
                        "type": "paragraph",
                        "text": "While both use cryptography to protect data, they serve different purposes. Encryption is a two-way function designed to hide data, while hashing is a one-way function meant to verify integrity."
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Feature",
                            "Hashing",
                            "Encryption"
                        ],
                        "rows": [
                            [
                                "Direction",
                                "One-way (irreversible)",
                                "Two-way (reversible)"
                            ],
                            [
                                "Output",
                                "Fixed length (e.g., 256 bits)",
                                "Variable length (depends on input)"
                            ],
                            [
                                "Primary Goal",
                                "Data Integrity",
                                "Data Confidentiality"
                            ],
                            [
                                "Examples",
                                "MD5, SHA-1, SHA-256",
                                "AES, RSA, DES"
                            ]
                        ]
                    },
                    {
                        "type": "heading",
                        "text": "Symmetric vs Asymmetric Encryption"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Symmetric Encryption: Uses a single shared key for both encryption and decryption (e.g., AES). It's fast but requires secure key exchange.",
                            "Asymmetric Encryption: Uses a key pair (public key to encrypt, private key to decrypt) (e.g., RSA). It's slower but solves the key exchange problem."
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "MD5 and SHA-1 are considered cryptographically broken. Always use SHA-256 or better for secure hashing."
                    }
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
                    {
                        "name": "CryptoHack",
                        "url": "https://cryptohack.org/",
                        "description": "A fun, free platform for learning cryptography."
                    },
                    {
                        "name": "CyberChef",
                        "url": "https://gchq.github.io/CyberChef/",
                        "description": "The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "TLS Protocol and Encrypted Communication Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master tls protocol and encrypted communication. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "CryptoHack",
                        "url": "https://cryptohack.org/",
                        "description": "A fun, free platform for learning cryptography."
                    },
                    {
                        "name": "CyberChef",
                        "url": "https://gchq.github.io/CyberChef/",
                        "description": "The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Secure Password Creation and Password Cracking Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master secure password creation and password cracking. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "PortSwigger Web Security Academy",
                        "url": "https://portswigger.net/web-security",
                        "description": "Free, interactive web security training."
                    },
                    {
                        "name": "OWASP Juice Shop",
                        "url": "https://owasp.org/www-project-juice-shop/",
                        "description": "Probably the most modern and sophisticated insecure web application."
                    },
                    {
                        "name": "TryHackMe \u2014 OWASP Top 10",
                        "url": "https://tryhackme.com/room/owasptop10",
                        "description": "Learn about and exploit each of the OWASP Top 10 vulnerabilities."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "OWASP Top 10 Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master owasp top 10. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "PortSwigger Web Security Academy",
                        "url": "https://portswigger.net/web-security",
                        "description": "Free, interactive web security training."
                    },
                    {
                        "name": "OWASP Juice Shop",
                        "url": "https://owasp.org/www-project-juice-shop/",
                        "description": "Probably the most modern and sophisticated insecure web application."
                    },
                    {
                        "name": "TryHackMe \u2014 OWASP Top 10",
                        "url": "https://tryhackme.com/room/owasptop10",
                        "description": "Learn about and exploit each of the OWASP Top 10 vulnerabilities."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Session Hijacking and Cookie Manipulation Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master session hijacking and cookie manipulation. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "PortSwigger Web Security Academy",
                        "url": "https://portswigger.net/web-security",
                        "description": "Free, interactive web security training."
                    },
                    {
                        "name": "OWASP Juice Shop",
                        "url": "https://owasp.org/www-project-juice-shop/",
                        "description": "Probably the most modern and sophisticated insecure web application."
                    },
                    {
                        "name": "TryHackMe \u2014 OWASP Top 10",
                        "url": "https://tryhackme.com/room/owasptop10",
                        "description": "Learn about and exploit each of the OWASP Top 10 vulnerabilities."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Secure Login Systems Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master secure login systems. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "HackTheBox",
                        "url": "https://www.hackthebox.com/",
                        "description": "A massive hacking playground and cybersecurity community."
                    },
                    {
                        "name": "TryHackMe \u2014 Jr Penetration Tester",
                        "url": "https://tryhackme.com/path/outline/jrpenetrationtester",
                        "description": "Learn the core methodologies and tools of a penetration tester."
                    },
                    {
                        "name": "picoCTF",
                        "url": "https://picoctf.org/",
                        "description": "A free computer security education program."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Passive and Active Reconnaissance Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master passive and active reconnaissance. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "HackTheBox",
                        "url": "https://www.hackthebox.com/",
                        "description": "A massive hacking playground and cybersecurity community."
                    },
                    {
                        "name": "TryHackMe \u2014 Jr Penetration Tester",
                        "url": "https://tryhackme.com/path/outline/jrpenetrationtester",
                        "description": "Learn the core methodologies and tools of a penetration tester."
                    },
                    {
                        "name": "picoCTF",
                        "url": "https://picoctf.org/",
                        "description": "A free computer security education program."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Scanning and Enumeration Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master scanning and enumeration. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "HackTheBox",
                        "url": "https://www.hackthebox.com/",
                        "description": "A massive hacking playground and cybersecurity community."
                    },
                    {
                        "name": "TryHackMe \u2014 Jr Penetration Tester",
                        "url": "https://tryhackme.com/path/outline/jrpenetrationtester",
                        "description": "Learn the core methodologies and tools of a penetration tester."
                    },
                    {
                        "name": "picoCTF",
                        "url": "https://picoctf.org/",
                        "description": "A free computer security education program."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Brute Force Attacks and System Exploitation Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master brute force attacks and system exploitation. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "HackTheBox",
                        "url": "https://www.hackthebox.com/",
                        "description": "A massive hacking playground and cybersecurity community."
                    },
                    {
                        "name": "TryHackMe \u2014 Jr Penetration Tester",
                        "url": "https://tryhackme.com/path/outline/jrpenetrationtester",
                        "description": "Learn the core methodologies and tools of a penetration tester."
                    },
                    {
                        "name": "picoCTF",
                        "url": "https://picoctf.org/",
                        "description": "A free computer security education program."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "CTF Practice Challenge Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master ctf practice challenge. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
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
                    {
                        "name": "picoCTF",
                        "url": "https://picoctf.org/",
                        "description": "A free computer security education program."
                    },
                    {
                        "name": "CTFtime",
                        "url": "https://ctftime.org/",
                        "description": "The most comprehensive CTF tracking platform."
                    },
                    {
                        "name": "Internal Challenges",
                        "url": "/challenges",
                        "description": "EGATE's own challenge platform for hands-on practice."
                    }
                ],
                "content": [
                    {
                        "type": "heading",
                        "text": "Capstone: Final Team-Based CTF Challenge Concepts"
                    },
                    {
                        "type": "paragraph",
                        "text": "This module covers the essential principles, tools, and methodologies required to master capstone: final team-based ctf challenge. Understanding these concepts is critical for modern cybersecurity operations."
                    },
                    {
                        "type": "heading",
                        "text": "Core Principles"
                    },
                    {
                        "type": "bullets",
                        "items": [
                            "Identify vulnerabilities and misconfigurations.",
                            "Apply best practices for secure deployment.",
                            "Utilize industry-standard tools effectively."
                        ]
                    },
                    {
                        "type": "table",
                        "headers": [
                            "Concept",
                            "Application",
                            "Relevance"
                        ],
                        "rows": [
                            [
                                "Analysis",
                                "Reviewing system states and logs",
                                "High"
                            ],
                            [
                                "Implementation",
                                "Applying secure configurations",
                                "Critical"
                            ],
                            [
                                "Validation",
                                "Testing applied controls",
                                "Medium"
                            ]
                        ]
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "text": "Remember to review the external practice links to gain hands-on experience with these concepts."
                    }
                ]
            }
        ]
    }
]
