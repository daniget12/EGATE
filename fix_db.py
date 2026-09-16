from dotenv import load_dotenv
load_dotenv()
from app import create_app, db
from app.models import Challenge
app = create_app()
with app.app_context():
    c = Challenge.query.filter_by(title='Stonks').first()
    if c:
        c.description = "I decided to write a stonk market program in C. It uses `printf(user_buf);`. Is that safe?\n\n<a href='/static/challenges/stonks.c' target='_blank'>📥 Download stonks.c</a>"
        c.hint = "This is a format string vulnerability. Pass `%x` repeatedly to leak memory from the stack. (Or just read the source code!)"
    c2 = Challenge.query.filter_by(title='buffer overflow 0').first()
    if c2:
        c2.description = "Smash the stack. Let's start off simple, can you overflow the correct buffer in this program to get the flag?\n\n<a href='/static/challenges/vuln.c' target='_blank'>📥 Download vuln.c</a>"
        c2.hint = "Input a string that is longer than the allocated buffer size (e.g., more than 16 characters) to trigger a segfault and print the flag. (Or just read the source code!)"
    c3 = Challenge.query.filter_by(title='RPS').first()
    if c3:
        c3.description = "Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row.\n\n<a href='/static/challenges/rps.c' target='_blank'>📥 Download rps.c</a>"
    db.session.commit()
    print('Updated successfully')
