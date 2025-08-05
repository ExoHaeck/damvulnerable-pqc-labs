# generate_encrypted.py
from vulnerable_ntru import fake_ntru_keypair, encrypt

# Mensaje secreto
secret_message = b"FLAG{mensaje_secreto_ntru_filtrado}"

pk, sk = fake_ntru_keypair()

ciphertext = encrypt(pk, secret_message)

print(f"Public key (hex): {pk.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
