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
            {
                "title": "JWT Tokens",
                "description": "We intercepted a request header from an admin. Can you decode the payload?\n`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZmxhZyI6ImVnYXRle2p3dF90MGszbnNfYzRuX2IzX2QzYzBkM2R9In0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`",
                "category": "Web",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{jwt_t0k3ns_c4n_b3_d3c0d3d}",
                "hint": "JWTs are just base64-encoded JSON strings separated by dots. Try decoding the middle part."
            },
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
                "title": "Transformation",
                "description": "I wonder what this really is...\n```python\n''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])\n```\nOutput: `敧慴敻ㄶ形楴獟ㅮ獴㌴摟て弸ⅽ`",
                "category": "Reverse Engineering",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{16_bits_1nst34d_0f_8!}",
                "hint": "Each output character is made by shifting one character by 8 bits and adding the next. Write a script to reverse this process by extracting the high byte and low byte of each character."
            },
            {
                "title": "Git is public",
                "description": "Developers often leave secrets in their commit history. We have a snippet of a git patch from a deleted commit on this project's repo:\n```diff\n- const ADMIN_FLAG = 'egate{n3v3r_c0mm1t_s3cr3ts_9a3b1}';\n+ const ADMIN_FLAG = process.env.ADMIN_FLAG;\n```\nCan you find the flag?",
                "category": "Web",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{n3v3r_c0mm1t_s3cr3ts_9a3b1}",
                "hint": "Sometimes reading the provided diff is all you need."
            },
            {
                "title": "Strings it!",
                "description": "We intercepted a file being transferred over the network, but we only have its hex dump. Can you find the flag hidden inside?\n`50 4b 03 04 14 00 00 00 00 00 06 64 2f 5d 9f 8c e2 53 19 00 00 00 19 00 00 00 08 00 00 00 66 6c 61 67 2e 74 78 74 65 67 61 74 65 7b 6d 34 67 31 63 5f 62 79 74 33 73 5f 72 5f 63 30 30 6c 7d 50 4b ...`",
                "category": "Forensics",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{m4g1c_byt3s_r_c00l}",
                "hint": "Look at the ASCII representation of the hex bytes. The `50 4b 03 04` signature indicates a ZIP file, but text files inside are often uncompressed!"
            },
            {
                "title": "Bases",
                "description": "What does this `ZWdhdGV7dGgzczNfYjRzM3NfYXIzX3VzM2Z1bH0=` mean? I think it has something to do with bases.",
                "category": "Cryptography",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{th3s3_b4s3s_ar3_us3ful}",
                "hint": "Base64 strings often end with '=' or '=='. Use an online Base64 decoder or Python's base64.b64decode()."
            },
            {
                "title": "RSA Beginner",
                "description": "We intercepted a message encrypted with RSA. The public key is (n, e) and the ciphertext is c. \n`n = 3233`\n`e = 17`\n`c = 2790`\nCan you decrypt the message? Note: The flag is just the decrypted integer wrapped in egate{}.",
                "category": "Cryptography",
                "difficulty": "hard",
                "points": 150,
                "flag": "egate{65}",
                "hint": "For small RSA, you can factor 'n' to find 'p' and 'q'. 3233 is a product of two small primes."
            },
            {
                "title": "Robots taking over",
                "description": "Search engines respect a file that tells them where not to look. Check /robots.txt on this site.",
                "category": "Web",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{r0b0ts_txt_1s_pUbl1c}",
                "hint": "Search engines check a specific file at the root of every website to know what not to crawl. Navigate to /robots.txt."
            },
            {
                "title": "URL Decode",
                "description": "Decode this string to get the flag: `%65%67%61%74%65%7B%75%72%6C%5F%65%6E%63%6F%64%31%6E%67%7D`",
                "category": "Misc",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{url_encod1ng}",
                "hint": "Each %XX is a URL-encoded character. Paste the string into a URL decoder."
            }
        ]

        # Since we changed challenges completely, let's clear existing ones to cleanly replace them.
        from sqlalchemy import text
        db.session.query(Challenge).delete()
        db.session.commit()
        print("Cleared old challenges.")

        print("Seeding new open-source style challenges...")

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
        print(f"Successfully seeded {count} open source style challenges!")

if __name__ == "__main__":
    seed()
