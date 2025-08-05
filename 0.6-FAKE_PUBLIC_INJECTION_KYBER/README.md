# Fake Public Key Injection – Kyber (CTF)

## Descripción
Este reto simula un fallo crítico en una implementación de Kyber KEM.
El servidor cifra mensajes usando la clave pública que recibe, sin validar si pertenece al dueño legítimo.
Esto permite a un atacante inyectar su propia clave pública, obtener el shared_secret y descifrar mensajes cifrados con AES.

## Objetivo
Inyectar tu propia clave pública y recuperar el mensaje secreto cifrado.

## Archivos
- vulnerable_kyber.py → Implementación vulnerable del KEM y cifrado AES.
- utils.py → Funciones auxiliares para cifrado/descifrado.
- generate_ciphertext.py → Genera datos cifrados usando la clave pública recibida.
- attacker.py → Script para realizar el ataque.

## Pasos
1. Ejecuta:
   ```bash
   python3 generate_ciphertext.py


