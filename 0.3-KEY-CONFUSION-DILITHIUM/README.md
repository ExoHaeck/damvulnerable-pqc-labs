# Key Confusion - Dilithium (CTF)

## Descripción
Este reto simula un fallo de "Key Confusion" en Dilithium, donde la verificación usa la clave pública como si fuera privada.
Esto permite falsificar firmas para cualquier mensaje.

## Objetivo
Generar una firma válida para el mensaje:
"Transaccion fraudulenta"
usando únicamente la clave pública dada.

## Estructura
- vulnerable_dilithium.py → Código vulnerable
- generate_keypair.py → Genera claves y firma legítima
- attacker.py → Explota la vulnerabilidad

## Pasos
1. Ejecuta `python3 generate_keypair.py` para obtener la clave pública.
2. Usa `attacker.py` para generar la firma falsa.
3. Verifica que el sistema la acepte.

## Validación
La firma falsa debe ser aceptada por la función `verify` en `vulnerable_dilithium.py`.
