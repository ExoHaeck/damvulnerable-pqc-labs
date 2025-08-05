import hashlib

def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()
