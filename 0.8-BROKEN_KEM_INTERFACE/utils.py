# utils.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

def derive_key(ss: bytes) -> bytes:
    return hashlib.sha256(ss).digest()

def aes_encrypt(ss: bytes, pt: bytes):
    key = derive_key(ss)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pad = 16 - len(pt)%16
    pt += bytes([pad])*pad
    return cipher.encrypt(pt), iv

def aes_decrypt(ss: bytes, ct: bytes, iv: bytes):
    key = derive_key(ss)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ct)
    pad = pt[-1]
    return pt[:-pad]
