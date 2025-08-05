# attacker.py
"""
Objetivo del reto:
Generar una firma válida para el mensaje:
"Transaccion fraudulenta"
usando ÚNICAMENTE la clave pública entregada por generate_keypair.py

Pistas:
- El esquema de verificación de firmas es vulnerable a 'Key Confusion'.
- Observa cómo se construye la verificación en vulnerable_dilithium.py.
- Recuerda que hashlib.sha256() se puede usar para simular la función de firma.

Entrega:
- Imprimir en pantalla la firma falsa en hexadecimal.
- Imprimir el mensaje falso.

No modifiques vulnerable_dilithium.py ni generate_keypair.py.
"""

# TODO: Implementar lógica para:
# 1. Pedir al usuario la clave pública en hex.
# 2. Convertirla a bytes.
# 3. Generar una firma falsa para "Transaccion fraudulenta".
# 4. Mostrar la firma falsa y el mensaje.


