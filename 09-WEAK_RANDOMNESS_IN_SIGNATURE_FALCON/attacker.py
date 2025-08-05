#!/usr/bin/env python3
# attacker.py

"""
Weak Randomness in Signature – Falcon (CTF)

Objetivo:
  Recuperar la clave privada `sk` explotando la predictibilidad
  del nonce `k` generado con random.seed(ts) en la firma vulnerable.

Cómo usar:
  1. Ejecuta `python3 generate_signature.py` y anota:
       - Public key (hex)
       - Message
       - Signature (hex)
  2. Ejecuta este script:
       python3 attacker.py
  3. Rellena los valores cuando te los pida.
  4. Completa las secciones marcadas con `# TODO`.
"""

import sys
import hashlib
import random
import binascii

from utils import inv_mod, Q           # Q = 2**16
from vulnerable_falcon import generate_keypair, sign  # sólo referencia

def main():
    # 1) Leer parámetros del reto
    pk_hex   = input("Public key (hex):    ").strip()
    message  = input("Message:             ").encode()
    sig_hex  = input("Signature (hex):     ").strip()

    # 2) Convertir la firma de hex a bytes
    try:
        signature = bytes.fromhex(sig_hex)
    except ValueError:
        print("Error: signature hex inválido", file=sys.stderr)
        sys.exit(1)

    if len(signature) != 6:
        print("Error: la firma debe tener 6 bytes (4 ts + 2 sig)", file=sys.stderr)
        sys.exit(1)

    # 3) Extraer timestamp y parte de la firma
    # ts      = <primeros 4 bytes de signature, big-endian>
    # sig_int = <bytes 4 y 5 de signature, big-endian>
    # TODO: escribe aquí la extracción de ts y sig_int

    # 4) Regenerar el nonce k
    # random.seed(ts)
    # k = random.getrandbits(16)
    # TODO: siembra y genera k de 16 bits

    # 5) Calcular h = SHA256(message) mod Q
    # digest = hashlib.sha256(message).digest()
    # h = <reduce digest a entero mod Q>
    # TODO: calcula h

    # 6) Recuperar sk:
    #      sk = (sig_int - h) * inv_mod(k, Q) mod Q
    # TODO: aplica la fórmula usando inv_mod

    # 7) Mostrar el resultado
    print(f"[+] Clave privada recuperada (sk): {sk}")

if __name__ == "__main__":
    main()

