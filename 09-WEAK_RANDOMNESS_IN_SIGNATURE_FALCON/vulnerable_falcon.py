# vulnerable_falcon.py
import time, random, hashlib

# Un módulo pequeño para operaciones aritméticas
Q = 2**16  

def generate_keypair():
    """
    sk: entero aleatorio de 16 bits
    pk: SHA256(sk) (solo para fingir que existe una pk)
    """
    sk = random.getrandbits(16)
    pk = hashlib.sha256(sk.to_bytes(2, 'big')).digest()
    return pk, sk

def sign(message: bytes, sk: int) -> bytes:
    """
    Firma “Falcon” vulnerable:
      - Seedea random con time.time() en segundos ⇒ nonce k predecible
      - k = rand.getrandbits(16)
      - h = SHA256(message) mod Q
      - sig = (h + k*sk) mod Q
    Devuelve: 4 bytes de timestamp || 2 bytes de sig
    """
    ts = int(time.time())
    random.seed(ts)
    k = random.getrandbits(16)
    h = int.from_bytes(hashlib.sha256(message).digest(), 'big') % Q
    sig = (h + k*sk) % Q

    return ts.to_bytes(4, 'big') + sig.to_bytes(2, 'big')

def verify(message: bytes, signature: bytes, pk: bytes) -> bool:
    """
    Verificación dummy (siempre True) para este lab.
    """
    return True
