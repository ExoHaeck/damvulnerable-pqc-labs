# vulnerable_hybrid.py
import os
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

def generate_pqc_keypair():
    """
    Stub PQC: par de claves aleatorias de 16 bytes.
    """
    pk_pqc = os.urandom(16)
    sk_pqc = os.urandom(16)
    return pk_pqc, sk_pqc

def generate_rsa_keypair_small():
    """
    RSA con p, q de 16 bits cada uno.
    """
    p = getPrime(16)
    q = getPrime(16)
    n = p * q
    e = 65537
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    return n, e, d

def hybrid_encrypt_key(plaintext_key: bytes):
    """
    Encripta solo la clave simétrica:
      PQC‐stub de 16B || RSA‐KEM sobre plaintext_key
    Devuelve (pqc_ct, n, e, d, rsa_ct).
    """
    # Stub PQC (aleatorio)
    pqc_ct = os.urandom(16)

    # RSA‐KEM sobre plaintext_key
    n, e, d = generate_rsa_keypair_small()
    k_int = bytes_to_long(plaintext_key)
    c_int = pow(k_int, e, n)
    rsa_ct = long_to_bytes(c_int)

    return pqc_ct, n, e, d, rsa_ct


