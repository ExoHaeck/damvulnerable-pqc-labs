# attacker.py
"""
Broken KEM Interface – CTF

Objetivo:
  Descubrir la FLAG cifrada con AES-CBC explotando
  el bug en decapsulate(ct, sk) que devuelve el ciphertext
  en lugar del shared_secret.

Cómo usar:
  1. Ejecuta previamente `python3 server.py` para que genere
     y exponga:
       - Public key (hex)
       - Ciphertext KEM (hex)
       - Ciphertext AES  (hex)
       - IV (hex)
  2. Rellena los valores solicitados a continuación.
  3. Completa este script donde veas `# TODO` para recuperar
     y descifrar la FLAG.
"""

import sys
from vulnerable_kem import decapsulate
from utils import aes_decrypt

def main():
    # 1) Leer inputs del reto
    pk_hex      = input("Public key (hex): ").strip()
    ct_kem_hex  = input("Ciphertext KEM (hex): ").strip()
    ct_aes_hex  = input("Ciphertext AES (hex): ").strip()
    iv_hex      = input("IV (hex): ").strip()

    # 2) Convertir de hex a bytes
    try:
        ct_kem = bytes.fromhex(ct_kem_hex)
        ct_aes = bytes.fromhex(ct_aes_hex)
        iv     = bytes.fromhex(iv_hex)
    except ValueError:
        print("Error: entrada hex no válida.", file=sys.stderr)
        sys.exit(1)

    # 3) Exploit: decapsulate debería devolver el shared_secret
    #    pero debido al bug devuelve ct_kem directamente.
    # TODO: ¿qué valor debes pasar como sk?
    fake_sk = b""  # <--- Rellena esto

    # TODO: llama a decapsulate para obtener ss
    ss = decapsulate(ct_kem, fake_sk)

    # 4) Usar `ss` para descifrar el mensaje AES-CBC
    # TODO: llama a aes_decrypt
    try:
        plaintext = aes_decrypt(  # <--- Rellena argumentos
            ss,
            ct_aes,
            iv
        )
    except Exception as e:
        print(f"Error al descifrar AES: {e}", file=sys.stderr)
        sys.exit(1)

    # 5) Imprimir la FLAG
    print(f"[+] FLAG descubierta: {plaintext.decode()}")

if __name__ == "__main__":
    main()

