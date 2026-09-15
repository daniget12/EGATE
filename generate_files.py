import os
import zipfile
import base64

def generate():
    out_dir = os.path.join("app", "static", "challenges")
    os.makedirs(out_dir, exist_ok=True)

    # 1. flag.txt
    with open(os.path.join(out_dir, "flag.txt"), "w") as f:
        f.write("egate{s4n1ty_v3r1f13d}")

    # 2. ende.py and flag.txt.en
    with open(os.path.join(out_dir, "ende.py"), "w") as f:
        f.write('''import sys
import base64

def decode(encoded_flag, password):
    if password == "secr3t_k3y":
        return base64.b64decode(encoded_flag).decode('utf-8')
    return "Invalid password."

if len(sys.argv) < 3:
    print("Usage: python ende.py <file> <password>")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    data = f.read()

print(decode(data, sys.argv[2]))
''')
    
    with open(os.path.join(out_dir, "flag.txt.en"), "w") as f:
        f.write(base64.b64encode(b"egate{py7h0n_wran6l1ng_123}").decode('utf-8'))

    # 3. wave.py
    with open(os.path.join(out_dir, "wave.py"), "w") as f:
        f.write('''import sys
if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
    print("Oh, you need help? Here is a flag: egate{b1ns_4nd_fl4gs}")
else:
    print("Hello! I can do many things. Try asking for help.")
''')

    # 4. crackme.py
    with open(os.path.join(out_dir, "crackme.py"), "w") as f:
        f.write('''secret = "rpfgr{cl7u0a_e3i3ef1at_1f_sha}"
def decode():
    # ROT13 decode
    return "".join([chr((ord(c) - 97 + 13) % 26 + 97) if c.islower() else c for c in secret])
print("I have a secret, but I won't print it!")
''')

    # 5. chall.S
    with open(os.path.join(out_dir, "chall.S"), "w") as f:
        f.write('''main:
    mov r0, #4134207980
    mov r1, #950176538
    cmp r0, r1
    bgt print_r0
    print_r1:
        // prints r1 in hex
        bx lr
    print_r0:
        // prints r0 in hex
        bx lr
''')

    # 6. file.txt (First Grep)
    with open(os.path.join(out_dir, "file.txt"), "w") as f:
        lines = ["just random text here\n"] * 5000
        lines[3412] = "look here: egate{gr3p_1s_g00d_t0_f1nd_th1ngs}\n"
        f.writelines(lines)

    # 7. hidden.zip (MacroHard replacement)
    zip_path = os.path.join(out_dir, "hidden.zip")
    with zipfile.ZipFile(zip_path, 'w') as z:
        z.writestr("doc.xml", "<?xml version='1.0'?><data>Nothing here</data>")
        z.writestr("secret/flag.txt", "egate{z1p_f1l3s_4r3_34sy}")
        
    print("Files generated in", out_dir)

if __name__ == "__main__":
    generate()
