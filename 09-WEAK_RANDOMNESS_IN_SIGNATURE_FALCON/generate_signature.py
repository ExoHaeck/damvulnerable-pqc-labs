# generate_signature.py
from vulnerable_falcon import generate_keypair, sign
import binascii

# 1) Generar par de claves
pk, sk = generate_keypair()
## Activar el print para hacer debug y estar seguros que estamos devolviendo la SK valida.
# print(f"[DEBUG] Clave privada real (sk): {sk}") 

# 2) Firmar el mensaje (puedes cambiarlo)
message = b"Welcome to Falcon!"
signature = sign(message, sk)

# 3) Publicar parámetros del reto
print(f"Public key (hex):     {pk.hex()}")
print(f"Message:              {message.decode()}")
print(f"Signature (hex):      {signature.hex()}")
