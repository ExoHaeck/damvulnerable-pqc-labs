# Legacy-Fallback Downgrade – Hybrid (CTF)

## Descripción
Implementamos un esquema híbrido PQC+RSA donde, si la parte PQC falla,
el sistema “cae” a RSA. El atacante puede forzar dicho fallback manipulando
el prefijo del ciphertext, luego factorizar el módulo pequeño y recuperar
el mensaje secreto (la FLAG).

## Archivos
- `vulnerable_hybrid.py`    → Genera el ciphertext híbrido.  
- `generate_ciphertext.py`   → Script para generar el reto (produce pk_pqc, n, e, hybrid_ct).  
- `attacker.py`             → Tu script: debes completarlo para recuperar la FLAG.  

## Uso

1. Genera el reto:
   ```bash
   python3 generate_ciphertext.py
