from dotenv import load_dotenv
load_dotenv()

import os
from app import create_app, db
from app.models import Challenge

def seed():
    app = create_app()
    with app.app_context():
        # Check if we already have challenges
        if Challenge.query.first():
            print("Challenges already seeded.")
            return

        print("Seeding challenges...")

        challenges_data = [
            {
                "title": "Inspect the Login",
                "description": "The developer left something in the login page source. View the page source (Ctrl+U) to find the flag.",
                "category": "Web",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{h7ml_c0mm3n7s_r_fun}"
            },
            {
                "title": "Robots taking over",
                "description": "Search engines respect a file that tells them where not to look. Check /robots.txt.",
                "category": "Web",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{r0b0ts_txt_1s_pUbl1c}"
            },
            {
                "title": "Caesar's Secret",
                "description": "Julius Caesar used this cipher. The ciphertext is: hjhwh{fdhvdu_flskhu_lv_zhdn}. The shift is 3.",
                "category": "Crypto",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{caesar_cipher_is_weak}"
            },
            {
                "title": "Base64 Basic",
                "description": "Decode this string: ZWdhdGV7YmFzZTY0XzFzX2Vhc3l9",
                "category": "Crypto",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{base64_1s_easy}"
            },
            {
                "title": "ROT13 Riddle",
                "description": "Decode this ROT13 string: rtnGr{ebg13_vf_abg_pelcgb}",
                "category": "Crypto",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{rot13_is_not_crypto}"
            },
            {
                "title": "Identify the File",
                "description": "A file starts with these hex bytes: 89 50 4E 47 0D 0A 1A 0A. What file format is this? Submit the flag as egate{png} (use the 3-letter extension in lowercase).",
                "category": "Forensics",
                "difficulty": "easy",
                "points": 75,
                "flag": "egate{png}"
            },
            {
                "title": "The Odd One Out",
                "description": "Find the flag among these strings: apple, banana, egate{n0t_4_fru1t}, orange, grape.",
                "category": "Misc",
                "difficulty": "easy",
                "points": 25,
                "flag": "egate{n0t_4_fru1t}"
            },
            {
                "title": "URL Decode",
                "description": "Decode this: %65%67%61%74%65%7B%75%72%6C%5F%65%6E%63%6F%64%31%6E%67%7D",
                "category": "Misc",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{url_encod1ng}"
            },
            {
                "title": "Hash Cracking 101",
                "description": "Crack this MD5 hash to find the flag: 5d41402abc4b2a76b9719d911017c592",
                "category": "Crypto",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{hello}"
            }
        ]

        count = 0
        for c_data in challenges_data:
            challenge = Challenge(
                title=c_data["title"],
                description=c_data["description"],
                category=c_data["category"],
                difficulty=c_data["difficulty"],
                points=c_data["points"]
            )
            # set_flag handles the werkzeug.security.generate_password_hash part
            challenge.set_flag(c_data["flag"])
            db.session.add(challenge)
            count += 1
            
        db.session.commit()
        print(f"Successfully seeded {count} challenges!")

if __name__ == "__main__":
    seed()
