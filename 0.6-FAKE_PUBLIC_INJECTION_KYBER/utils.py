# utils.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

def derive_aes_key(shared_secret: bytes) -> bytes:
    """
    Deriva clave AES-256 a partir del shared_secret usando SHA-256.
    """
    return hashlib.sha256(shared_secret).digest()

def aes_encrypt(shared_secret: bytes, plaintext: bytes):
    """
    Cifra un mensaje con AES-CBC.
    """
    key = derive_aes_key(shared_secret)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    pad_len = 16 - (len(plaintext) % 16)
    padded_plaintext = plaintext + bytes([pad_len]) * pad_len

    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext, iv

def aes_decrypt(shared_secret: bytes, ciphertext: bytes, iv: bytes) -> bytes:
    """
    Descifra un mensaje con AES-CBC.
    """
    key = derive_aes_key(shared_secret)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    pad_len = padded_plaintext[-1]
    return padded_plaintext[:-pad_len]

