from vulnerable_dilithium import fake_dilithium_keypair, sign

message = b"Transaccion autorizada"
pk, sk = fake_dilithium_keypair()

# Firma legítima
signature = sign(message, sk)

print(f"Public key (hex): {pk.hex()}")
print(f"Signature (hex): {signature.hex()}")
print("Mensaje:", message.decode())

