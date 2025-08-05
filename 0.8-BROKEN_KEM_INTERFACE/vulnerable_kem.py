# vulnerable_kem.py
import os
import hashlib

def keypair():
    """
    KEM genérico:
      sk = seed aleatoria
      pk = H(sk)
    """
    sk = os.urandom(32)
    pk = hashlib.sha256(sk).digest()
    return pk, sk

def encapsulate(pk: bytes):
    """
    Genera shared_secret y ciphertext:
      ss := aleatorio
      ct := H(ss || pk)
    """
    ss = os.urandom(32)
    ct = hashlib.sha256(ss + pk).digest()
    return ct, ss

def decapsulate(ct: bytes, sk: bytes):
    """
    BUG CRÍTICO: en vez de derivar ss usando sk y ct, 
    devuelve el ct tal cual—¡el secreto queda expuesto!
    """
    return ct
