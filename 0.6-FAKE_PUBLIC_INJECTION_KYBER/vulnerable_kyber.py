# vulnerable_kyber.py
import os
from utils import aes_encrypt

def fake_kyber_keypair():
    """
    Genera clave pública y privada simuladas para Kyber.
    """
    sk = os.urandom(32)
    pk = os.urandom(32)
    return pk, sk

def kem_encapsulate(pk: bytes) -> tuple:
    """
    Simula encapsulación de Kyber: genera shared_secret y ciphertext.
    VULNERABILIDAD: acepta cualquier pk sin validación.
    """
    shared_secret = os.urandom(32)
    ciphertext = b"CIPH" + pk[:8]
    return ciphertext, shared_secret

def server_encrypt_message(pk: bytes, plaintext: bytes) -> tuple:
    """
    Servidor: encapsula y cifra un mensaje con AES usando el shared_secret.
    """
    ciphertext_kem, shared_secret = kem_encapsulate(pk)
    ciphertext_aes, iv = aes_encrypt(shared_secret, plaintext)
    return ciphertext_kem, ciphertext_aes, iv

