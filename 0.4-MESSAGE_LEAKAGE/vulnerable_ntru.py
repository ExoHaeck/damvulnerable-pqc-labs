# vulnerable_ntru.py
import os

def fake_ntru_keypair():
    """
    Simula un par de claves pública/privada de NTRU
    """
    sk = os.urandom(32)  # clave privada
    pk = os.urandom(32)  # clave pública
    return pk, sk

def encrypt(pk: bytes, plaintext: bytes) -> bytes:
    """
    Cifrado vulnerable:
    - Simula el cifrado con XOR
    - Adjunta los primeros 8 bytes del mensaje en claro al final del ciphertext
    """
    keystream = os.urandom(len(plaintext))
    ciphertext = bytes([p ^ k for p, k in zip(plaintext, keystream)])
    return ciphertext + plaintext[:8]  # <-- VULNERABILIDAD: fuga directa

def decrypt(sk: bytes, ciphertext: bytes) -> bytes:
    """
    Descifra el mensaje (en este reto no se usará)
    """
    # Separamos el ciphertext real de la fuga
    ct, _ = ciphertext[:-8], ciphertext[-8:]
    keystream = os.urandom(len(ct))  # no se puede descifrar sin clave real
    return bytes([c ^ k for c, k in zip(ct, keystream)])
