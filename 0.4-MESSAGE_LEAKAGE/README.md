# Message Leakage – NTRU (CTF)

## Descripción
Este reto simula una implementación vulnerable de cifrado basada en NTRU.  
Por un error en la función de cifrado, parte del mensaje original en texto plano se incluye directamente dentro del ciphertext.  

Esto provoca una fuga directa de información, rompiendo la confidencialidad del mensaje y permitiendo a un atacante reconstruirlo parcial o totalmente.

---

## Objetivo
Analizar el ciphertext entregado y **extraer la parte del mensaje original que ha sido filtrada**.  
No es necesario descifrar todo el mensaje, solo identificar la fuga y mostrar el fragmento en claro.

---

## Archivos
- `vulnerable_ntru.py` → Simulación del cifrado vulnerable.
- `generate_encrypted.py` → Genera la clave pública y el ciphertext con fuga.
- `attacker.py` → Script que el participante debe completar para encontrar la fuga.

---

## Pasos para el reto
1. Ejecuta:
   ```bash
   python3 generate_encrypted.py

