# generate_ciphertext.py
from vulnerable_kem import keypair, encapsulate
from utils import aes_encrypt

# 1) Genera par de claves
pk, sk = keypair()

# 2) Encapsula: obtenemos KEM‐ciphertext y shared_secret “real”
ct_kem, ss_real = encapsulate(pk)

# 3) ¡Aquí está el truco! 👉 Usa ct_kem (no ss_real) como clave para AES
ct_aes, iv = aes_encrypt(ct_kem, b"FLAG{broken_kem_interface_pwned}")

# 4) Publica sólo pk, ct_kem, ct_aes, iv
print(f"Public key (hex):       {pk.hex()}")
print(f"Ciphertext KEM (hex):   {ct_kem.hex()}")
print(f"Ciphertext AES (hex):   {ct_aes.hex()}")
print(f"IV (hex):               {iv.hex()}")
