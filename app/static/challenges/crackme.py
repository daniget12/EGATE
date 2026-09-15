secret = "rpfgr{cl7u0a_e3i3ef1at_1f_sha}"
def decode():
    # ROT13 decode
    return "".join([chr((ord(c) - 97 + 13) % 26 + 97) if c.islower() else c for c in secret])
print("I have a secret, but I won't print it!")
