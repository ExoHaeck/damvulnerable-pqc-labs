# generate_ciphertext.py
from vulnerable_hybrid import hybrid_encrypt_key
from utils import aes_encrypt
import os

# 1) FLAG completa
FLAG = b"FLAG{legacy_fallback_pwned}"

# 2) Generar clave simétrica de 3 bytes (24 bits < n)
SYM_KEY_LEN = 3
sym_key = os.urandom(SYM_KEY_LEN)

# 3) Cifrar la FLAG con AES-CBC
ct_aes, iv = aes_encrypt(sym_key, FLAG)

# 4) Encriptar sólo la clave simétrica con Hybrid‐RSA
pqc_ct, n, e, d, rsa_ct = hybrid_encrypt_key(sym_key)

# 5) Construir ciphertext híbrido: "PQC"||stub16||"RSA"||rsa_ct
hybrid_kem_ct = b"PQC" + pqc_ct + b"RSA" + rsa_ct

# 6) Publicar los parámetros del reto
print(f"RSA modulus n (int):               {n}")
print(f"RSA exponent e (int):              {e}")
print(f"Hybrid-KEM ciphertext (hex):       {hybrid_kem_ct.hex()}")
print(f"AES-CBC ciphertext (hex):          {ct_aes.hex()}")
print(f"IV (hex):                          {iv.hex()}")


