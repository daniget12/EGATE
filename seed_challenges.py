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
                "title": "Inspect the Login",
                "description": "The developer left something in the login page source. View the page source (Ctrl+U) to find the flag.",
                "category": "Web",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{h7ml_c0mm3n7s_r_fun}",
                "hint": "Right-click the page and choose 'View Page Source'. Look for HTML comments — they start with <!-- and end with -->."
            },
            {
                "title": "Robots taking over",
                "description": "Search engines respect a file that tells them where not to look. Check /robots.txt.",
                "category": "Web",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{r0b0ts_txt_1s_pUbl1c}",
                "hint": "Search engines check a specific file at the root of every website to know what not to crawl. Its name starts with 'robots'."
            },
            {
                "title": "Caesar's Secret",
                "description": "Julius Caesar used this cipher. The ciphertext is: hjhwh{fdhvdu_flskhu_lv_zhdn}. The shift is 3.",
                "category": "Crypto",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{caesar_cipher_is_weak}",
                "hint": "The shift is 3. Shift every letter back by 3 (A → X, B → Y, etc.). An online ROT decoder can help."
            },
            {
                "title": "Base64 Basic",
                "description": "Decode this string: ZWdhdGV7YmFzZTY0XzFzX2Vhc3l9",
                "category": "Crypto",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{base64_1s_easy}",
                "hint": "Base64 strings often end with '=' or '=='. Use an online Base64 decoder or Python's base64.b64decode()."
            },
            {
                "title": "ROT13 Riddle",
                "description": "Decode this ROT13 string: rtnGr{ebg13_vf_abg_pelcgb}",
                "category": "Crypto",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{rot13_is_not_crypto}",
                "hint": "ROT13 is a Caesar cipher with a shift of 13. It's its own inverse — apply it twice to get back to the original."
            },
            {
                "title": "Identify the File",
                "description": "A file starts with these hex bytes: 89 50 4E 47 0D 0A 1A 0A. What file format is this? Submit the flag as egate{png} (use the 3-letter extension in lowercase).",
                "category": "Forensics",
                "difficulty": "easy",
                "points": 75,
                "flag": "egate{png}",
                "hint": "The first few bytes of a file are called its 'magic bytes'. Search for 'PNG file signature' to identify this one."
            },
            {
                "title": "The Odd One Out",
                "description": "Find the flag among these strings: apple, banana, egate{n0t_4_fru1t}, orange, grape.",
                "category": "Misc",
                "difficulty": "easy",
                "points": 25,
                "flag": "egate{n0t_4_fru1t}",
                "hint": "One of these strings doesn't look like a normal word. Look for the one that starts with the same prefix as your platform flags."
            },
            {
                "title": "URL Decode",
                "description": "Decode this: %65%67%61%74%65%7B%75%72%6C%5F%65%6E%63%6F%64%31%6E%67%7D",
                "category": "Misc",
                "difficulty": "easy",
                "points": 50,
                "flag": "egate{url_encod1ng}",
                "hint": "Each %XX is a URL-encoded character. Paste the string into a URL decoder or use urllib.parse.unquote() in Python."
            },
            {
                "title": "Hash Cracking 101",
                "description": "Crack this MD5 hash to find the flag: 5d41402abc4b2a76b9719d911017c592",
                "category": "Crypto",
                "difficulty": "medium",
                "points": 100,
                "flag": "egate{hello}",
                "hint": "This is an MD5 hash. Try an online MD5 lookup or crackstation.net."
            }
        ]

        # Check if we already have challenges
        if Challenge.query.first():
            print("Challenges already seeded. Updating hints...")
            for c_data in challenges_data:
                existing = Challenge.query.filter_by(title=c_data["title"]).first()
                if existing:
                    existing.hint = c_data["hint"]
            db.session.commit()
            print("Hints updated.")
            return

        print("Seeding challenges...")

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
        print(f"Successfully seeded {count} challenges!")

if __name__ == "__main__":
    seed()
