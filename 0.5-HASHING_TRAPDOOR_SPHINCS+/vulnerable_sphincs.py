# vulnerable_sphincs.py
import os

def fake_sphincs_keypair():
    """
    Genera par de claves simplificado tipo SPHINCS+ (simulado)
    """
    sk = os.urandom(32)  # clave privada
    pk = os.urandom(32)  # clave pública
    return pk, sk

def trapdoor_hash(data: bytes) -> bytes:
    """
    Función hash débil con trapdoor:
    - Solo devuelve los primeros 3 bytes del XOR de todos los bloques.
    - Facilita encontrar colisiones.
    """
    xor_val = [0, 0, 0]
    for i, b in enumerate(data):
        xor_val[i % 3] ^= b
    return bytes(xor_val)  # salida muy pequeña → colisiones fáciles

def sign(message: bytes, sk: bytes) -> bytes:
    """
    Firma = hash_trapdoor(mensaje || sk)
    """
    return trapdoor_hash(message + sk)

def verify(message: bytes, signature: bytes, pk: bytes) -> bool:
    """
    Verificación vulnerable:
    No valida adecuadamente la relación sk ↔ pk, confía solo en hash pequeño.
    """
    expected_sig = trapdoor_hash(message + pk)  # Error: usa pk en vez de sk real
    return expected_sig == signature
