import os, json
from vulnerable_saber import fake_saber_keypair

KEY_FILE = os.path.join(os.path.dirname(__file__), "shared_key.json")

if os.path.exists(KEY_FILE):
    with open(KEY_FILE,"r") as f:
        data = json.load(f)
        pk_server = bytes.fromhex(data["pk_server"])
        sk_server_bits = data["sk_server_bits"]
else:
    pk_server, sk_server_bits = fake_saber_keypair()
    with open(KEY_FILE,"w") as f:
        json.dump({
            "pk_server": pk_server.hex(),
            "sk_server_bits": sk_server_bits
        }, f)









