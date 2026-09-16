from app import create_app, db
from app.models import Challenge
app = create_app()
with app.app_context():
    c_rsa = Challenge.query.filter_by(title='Mind your Ps and Qs').first()
    if c_rsa:
        c_rsa.description = "In RSA, small e and n can be factored. \n`c: 33111275379347282813756567856162044514238180266169705281784`\n`n: 848703330753199591841216813413842474259116682085832930700873`\n`e: 65537`\nDecrypt this to get the flag."
    
    c_vig = Challenge.query.filter_by(title='Vigenere').first()
    if c_vig:
        c_vig.description = "Can you decrypt this message? \n`geltf{x1e3_n1p43s_y0pvs}`\nKey: `CYLAB`"
    
    db.session.commit()
    print('Updated successfully')
