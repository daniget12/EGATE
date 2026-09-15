import sys
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
