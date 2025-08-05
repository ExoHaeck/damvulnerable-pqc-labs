"""
Fake Public Key Injection – Kyber (CTF)

Objetivo:
Inyectar tu propia clave pública maliciosa en el sistema vulnerable para que el servidor
genere un shared_secret que tú puedas conocer, y usarlo para descifrar el mensaje secreto
cifrado con AES.

Pistas:
- Observa que el servidor usa la clave pública recibida sin validarla.
- Si logras que el servidor cifre con tu clave pública, podrás derivar la misma clave AES.
- La FLAG está cifrada con AES-CBC usando el shared_secret.

Entrega:
- Clave pública maliciosa en hex.
- Mensaje descifrado en texto plano.
"""

# TODO:
# 1. Recibir desde input el Ciphertext AES y el IV (ambos en hex) entregados por el servidor.
# 2. Generar un par de claves malicioso (pk, sk) usando fake_kyber_keypair().
# 3. Usar kem_encapsulate(pk) para obtener el shared_secret asociado a tu clave pública.
# 4. Usar aes_decrypt(shared_secret, ciphertext_aes, iv) para descifrar el mensaje.
# 5. Imprimir:
#    - Clave pública maliciosa (hex)
#    - Mensaje descifrado (texto plano)

# from vulnerable_kyber import ...
# from utils import ...

# cipher_aes_hex = input("Ciphertext AES (hex): ").strip()
# iv_hex = input("IV (hex): ").strip()

# TODO: implementar lógica del ataque aquí.

