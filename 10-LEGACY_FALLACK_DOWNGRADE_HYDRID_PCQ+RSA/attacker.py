#!/usr/bin/env python3
# attacker.py

"""
Legacy-Fallback Downgrade – Hybrid (CTF)

Objetivo:
  1) Forzar el downgrade a RSA.
  2) Extraer el bloque RSA-KEM del ciphertext híbrido.
  3) Factorizar n para recuperar (p, q) y calcular d.
  4) RSA-decrypt para obtener la clave AES (3 bytes).
  5) AES-CBC decrypt para revelar la FLAG.
"""

import sys
import math
from Crypto.Util.number import long_to_bytes
from utils import aes_decrypt

def main():
    # 1) Leer parámetros
    n_str     = input("RSA modulus n (int):     ").strip()
    e_str     = input("RSA exponent e (int):    ").strip()
    kem_hex   = input("Hybrid-KEM ciphertext (hex): ").strip()
    ct_hex    = input("AES-CBC ciphertext (hex):    ").strip()
    iv_hex    = input("IV (hex):                   ").strip()

    # 2) Parsear entradas
    try:
        n       = int(n_str)
        e       = int(e_str)
        hybrid  = bytes.fromhex(kem_hex)
        ct_aes  = bytes.fromhex(ct_hex)
        iv      = bytes.fromhex(iv_hex)
    except:
        print("Error: formato inválido.", file=sys.stderr)
        sys.exit(1)

    # 3) Forzar fallback a RSA
    # TODO: si hybrid empieza por b"PQC", reemplaza ese prefijo por b"RSA"
    # hybrid = ...

    # 4) Extraer solo la parte RSA-KEM (descartar los primeros 22 bytes)
    #    (3B "RSA" + 16B stub PQC + 3B "RSA")
    # rsa_ct = ...

    # 5) Factorizar n para hallar p, q
    # TODO: busca un divisor i de n en 2…sqrt(n)
    # p = q = None
    # for i in range(...):
    #     if n % i == 0:
    #         p, q = i, n//i
    #         break

    # 6) Calcular d = e⁻¹ mod φ(n)
    # TODO: phi = (p-1)*(q-1); d = pow(e, -1, phi)
    # d = ...

    # 7) RSA-decrypt para recuperar sym_key de 3 bytes
    # TODO:
    # c_int    = int.from_bytes(rsa_ct, 'big')
    # k_int    = pow(c_int, d, n)
    # sym_key  = long_to_bytes(k_int, 3)

    # 8) AES-CBC decrypt de la FLAG
    # TODO: flag = aes_decrypt(sym_key, ct_aes, iv)

    # 9) Mostrar resultado
    print(f"[+] FLAG descubierta: {flag.decode()}")

if __name__ == "__main__":
    main()







