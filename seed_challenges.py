from dotenv import load_dotenv
load_dotenv()

import os
from sqlalchemy import inspect, text
from app import create_app, db
from app.models import Challenge

def seed():
    app = create_app()
    with app.app_context():
        inspector = inspect(db.engine)
        challenge_columns = {col["name"] for col in inspector.get_columns("challenges")}
        if "hint" not in challenge_columns:
            db.session.execute(text("ALTER TABLE challenges ADD COLUMN hint TEXT"))
            db.session.commit()
            print("Added hint column to challenges table.")

        challenges_data = [
            # GENERAL SKILLS
            {
                "title": "Obedient Cat",
                "description": "This file has a flag in plain sight (aka \"in-the-clear\"). `cat flag.txt`\nOutput: `egate{s4n1ty_v3r1f13d}`",
                "category": "General Skills",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{s4n1ty_v3r1f13d}",
                "hint": "Any text editor can read a plain text file, or just look at the description."
            },
            {
                "title": "Python Wrangling",
                "description": "Python scripts are invoked kind of like programs in the Terminal... Can you run this python script using this password to get the flag? \n`python ende.py -d flag.txt.en`",
                "category": "General Skills",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{py7h0n_wran6l1ng_123}",
                "hint": "You'll need to use the command line and python to decrypt."
            },
            {
                "title": "Wave a flag",
                "description": "Can you invoke help flags for a tool or binary? This program just prints out a flag if you pass it the `-h` or `--help` argument.",
                "category": "General Skills",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{b1ns_4nd_fl4gs}",
                "hint": "Run the binary with the -h flag in a terminal."
            },
            {
                "title": "Nice netcat...",
                "description": "There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 12222`, but it doesn't speak English...",
                "category": "General Skills",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{n3tc4t_1s_sw33t}",
                "hint": "You can practice using netcat. The output might be ASCII numbers you need to convert to characters."
            },

            # WEB EXPLOITATION
            {
                "title": "GET aHEAD",
                "description": "Find the flag being held on this server to get ahead of the competition. Check the headers of the request.",
                "category": "Web Exploitation",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{r3j3ct_g3t_us3_h34d}",
                "hint": "Maybe you have more than 2 choices (GET, POST). Check out other HTTP methods like HEAD."
            },
            {
                "title": "Cookies",
                "description": "Who doesn't love cookies? I heard the admin likes chocolate chip... check your browser's dev tools.",
                "category": "Web Exploitation",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{c00ki3s_4r3_d3l1c10us}",
                "hint": "Check your browser's Application or Storage tab and try modifying the cookie value."
            },
            {
                "title": "SQL Direct",
                "description": "Connect to this PostgreSQL server and find the flag! \n`psql -h sql.server -U postgres -d public`",
                "category": "Web Exploitation",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{p5ql_1s_p0w3rful}",
                "hint": "Use standard SQL queries like SELECT * FROM table_name to find the hidden data."
            },
            {
                "title": "Local Authority",
                "description": "Can you get the flag? Go to this website and see what you can discover. Look closely at the source code of the login page.",
                "category": "Web Exploitation",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{1nspeC7_3l3ment_1s_k3y}",
                "hint": "Sometimes developers leave comments or javascript files containing passwords."
            },

            # CRYPTOGRAPHY
            {
                "title": "Mod 26",
                "description": "Cryptography can be easy, do you know what ROT13 is? \n`rtngr{arkg_gvzr_V_yy_gel_2_ebhaqf_bs_ebg13_MAQOIAXX}`",
                "category": "Cryptography",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{next_time_I_ll_try_2_rounds_of_rot13_ZNDBVNKK}",
                "hint": "ROT13 is a Caesar cipher with a shift of 13. An online ROT decoder can help."
            },
            {
                "title": "Mind your Ps and Qs",
                "description": "In RSA, small e and n can be factored. \n`c: 2012...`\n`n: 2056...`\n`e: 65537`\nDecrypt this to get the flag.",
                "category": "Cryptography",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{sm4ll_N_n0_g00d}",
                "hint": "Use a tool like FactorDB to find the prime factors of N (p and q)."
            },
            {
                "title": "Bases",
                "description": "What does this `ZWdhdGV7dGgzczNfYjRzM3NfYXIzX3VzM2Z1bH0=` mean? I think it has something to do with bases.",
                "category": "Cryptography",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{th3s3_b4s3s_ar3_us3ful}",
                "hint": "Base64 strings often end with '=' or '=='. Use an online Base64 decoder."
            },
            {
                "title": "Vigenere",
                "description": "Can you decrypt this message? \n`rgpkh{q41i3_c1p43r_i0q3p}`\nKey: `CYLAB`",
                "category": "Cryptography",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{v1g3_c1p43r_w0rks}",
                "hint": "The Vigenère cipher uses a keyword to shift letters differently based on their position."
            },

            # REVERSE ENGINEERING
            {
                "title": "Transformation",
                "description": "I wonder what this really is...\n```python\n''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])\n```\nOutput: `敧慴敻ㄶ形楴獟ㅮ獴㌴摟て弸ⅽ`",
                "category": "Reverse Engineering",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{16_bits_1nst34d_0f_8!}",
                "hint": "Each output character is made by shifting one character by 8 bits and adding the next. Write a script to reverse this."
            },
            {
                "title": "crackme-py",
                "description": "We found this Python script `crackme.py` but it's obfuscated. Can you find the secret string?",
                "category": "Reverse Engineering",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{py7h0n_r3v3rs1ng_1s_fun}",
                "hint": "Look for a variable that contains a strange string and try to print it out after decoding."
            },
            {
                "title": "ARMssembly 0",
                "description": "What integer does this program print with arguments 4134207980 and 950176538? File: `chall.S`",
                "category": "Reverse Engineering",
                "difficulty": "hard",
                "points": 200,
                "flag": "egate{E5A91D0C}",
                "hint": "You don't need to execute it, just read the assembly. It looks like it's just comparing two numbers and printing the larger one in hex."
            },

            # FORENSICS
            {
                "title": "Information",
                "description": "Files can always be changed in a secret way. Can you find the flag hidden inside this image's metadata?",
                "category": "Forensics",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{m3t4d4t4_1s_h1dd3n}",
                "hint": "Look at the details of the image using a tool like exiftool."
            },
            {
                "title": "Glory of the Garden",
                "description": "This garden contains more than it seems. Look deeply into the hex data of the image.",
                "category": "Forensics",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{m0r3_th4n_m33ts_th3_3y3}",
                "hint": "A hex editor or the `strings` command can find text hidden inside non-text files."
            },
            {
                "title": "Wireshark doo dooo do doo",
                "description": "Can you find the flag? We captured some network traffic in a PCAP file.",
                "category": "Forensics",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{w1r3sh4rk_p4ck3ts_sn1ff3d}",
                "hint": "Follow the TCP streams in Wireshark. The flag might be sent in plain text."
            },
            {
                "title": "MacroHard StrongEdge",
                "description": "I've hidden a flag in this document. Can you find it? It's a `.pptm` file.",
                "category": "Forensics",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{m4cr0s_4r3_v3ry_d4ng3r0us}",
                "hint": "Office documents are just ZIP files. Unzip it and look for a hidden text file or macro."
            },

            # BINARY EXPLOITATION
            {
                "title": "Stonks",
                "description": "I decided to write a stonk market program in C. It uses `printf(user_buf);`. Is that safe?",
                "category": "Binary Exploitation",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{f0rm4t_str1ng_vuln3r4b1l1ty}",
                "hint": "This is a format string vulnerability. Pass `%x` repeatedly to leak memory from the stack."
            },
            {
                "title": "buffer overflow 0",
                "description": "Smash the stack. Let's start off simple, can you overflow the correct buffer in this program to get the flag?",
                "category": "Binary Exploitation",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{st4ck_sm4sh1ng_d3t3ct3d}",
                "hint": "Input a string that is longer than the allocated buffer size (e.g., more than 16 characters) to trigger a segfault and print the flag."
            },
            {
                "title": "RPS",
                "description": "Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row.",
                "category": "Binary Exploitation",
                "difficulty": "hard",
                "points": 200,
                "flag": "egate{strstr_1s_n0t_3qu4ls}",
                "hint": "Check the source code carefully. Does it use `strstr` to check your input? What if your input contains all three choices?"
            }
        ]

        # First we must delete UserChallenge references
        from app.models import UserChallenge
        db.session.query(UserChallenge).delete()
        db.session.commit()
        print("Cleared user progress.")

        # Clear existing ones to cleanly replace them.
        db.session.query(Challenge).delete()
        db.session.commit()
        print("Cleared old challenges.")

        print("Seeding new picoCTF style challenges...")

        count = 0
        for c_data in challenges_data:
            challenge = Challenge(
                title=c_data["title"],
                description=c_data["description"],
                category=c_data["category"],
                difficulty=c_data["difficulty"],
                points=c_data["points"],
                hint=c_data["hint"]
            )
            # set_flag handles the werkzeug.security.generate_password_hash part
            challenge.set_flag(c_data["flag"])
            db.session.add(challenge)
            count += 1
            
        db.session.commit()
        print(f"Successfully seeded {count} picoCTF style challenges!")

if __name__ == "__main__":
    seed()
