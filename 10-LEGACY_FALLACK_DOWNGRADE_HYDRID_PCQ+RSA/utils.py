# utils.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

def derive_key(key: bytes) -> bytes:
    """Deriva 32B de clave a partir de key mediante SHA-256."""
    return hashlib.sha256(key).digest()

def aes_encrypt(key: bytes, plaintext: bytes):
    """
    Cifra EN AES-CBC with PKCS#7.
    Devuelve (ciphertext, iv).
    """
    iv = get_random_bytes(16)
    cipher = AES.new(derive_key(key), AES.MODE_CBC, iv)
    pad_len = 16 - (len(plaintext) % 16)
    padded = plaintext + bytes([pad_len]) * pad_len
    ct = cipher.encrypt(padded)
    return ct, iv

def aes_decrypt(key: bytes, ciphertext: bytes, iv: bytes) -> bytes:
    """
    Descifra AES-CBC y quita padding PKCS#7.
    """
    cipher = AES.new(derive_key(key), AES.MODE_CBC, iv)
    pt = cipher.decrypt(ciphertext)
    pad_len = pt[-1]
    return pt[:-pad_len]

