# generate_signature.py
from vulnerable_sphincs import fake_sphincs_keypair, sign

message = b"Operacion aprobada"
pk, sk = fake_sphincs_keypair()
signature = sign(message, sk)

print(f"Public key (hex): {pk.hex()}")
print(f"Signature (hex): {signature.hex()}")
print("Mensaje:", message.decode())
