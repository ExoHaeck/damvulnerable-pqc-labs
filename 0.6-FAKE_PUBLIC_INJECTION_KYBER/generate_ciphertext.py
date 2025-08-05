# generate_ciphertext.py
from vulnerable_kyber import fake_kyber_keypair, server_encrypt_message

# Servidor genera par legítimo
pk_legit, sk_legit = fake_kyber_keypair()

# Mensaje secreto / FLAG (NO se imprime en modo CTF)
secret_message = b"FLAG{kyber_fake_pk_injection_success}"

# Servidor cifra usando clave pública recibida (legítima en este caso)
ciphertext_kem, ciphertext_aes, iv = server_encrypt_message(pk_legit, secret_message)

# Salida para el jugador
print("[SERVIDOR] Datos cifrados:")
print(f"Ciphertext KEM (hex): {ciphertext_kem.hex()}")
print(f"Ciphertext AES (hex): {ciphertext_aes.hex()}")
print(f"IV (hex): {iv.hex()}")


