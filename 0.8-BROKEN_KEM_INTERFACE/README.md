# Broken KEM Interface – CTF

## Descripción
Este reto muestra un fallo en la interfaz de un KEM genérico:
la función `decapsulate(ct, sk)` **no utiliza** la clave privada `sk` para recuperar
el `shared_secret`, sino que devuelve directamente el `ciphertext` generado en `encapsulate`.
Esto expone el secreto y permite descifrar cualquier mensaje cifrado con él.

## Objetivo
Escribir un script (`attacker.py`) que, dado:
- **Public key**  
- **Ciphertext KEM**  
- **Ciphertext AES**  
- **IV**  

recupere la `shared_secret` incorrecto (igual al `ciphertext KEM`) y descifre la FLAG.

## Archivos
- `vulnerable_kem.py`      → Implementación KEM con bug en `decapsulate()`.  
- `utils.py`              → Funciones para AES-CBC.  
- `generate_ciphertext.py`→ Genera datos de reto (no revela sk ni ss_real).  
- `attacker.py`           → Esqueleto que debes completar.  

## Uso

1. Genera el reto:
   ```bash
   python3 generate_ciphertext.py
