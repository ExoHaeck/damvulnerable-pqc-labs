import hashlib
import os

def fake_dilithium_keypair():
    sk = os.urandom(32)  # clave privada real
    pk = hashlib.sha256(sk).digest()  # clave pública derivada
    return pk, sk  # <-- VULNERABILIDAD: orden invertido

def sign(message, sk):
    return hashlib.sha256(message + sk).digest()

def verify(message, signature, pk):
    supposed_sig = hashlib.sha256(message + pk).digest()
    return supposed_sig == signature

