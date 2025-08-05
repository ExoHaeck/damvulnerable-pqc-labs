# attacker.py
"""
Objetivo:
Encontrar un mensaje diferente que produzca el mismo hash que el mensaje original
firmado, usando únicamente la clave pública y la firma legítima.

Pistas:
- El hash usado es extremadamente pequeño.
- Una búsqueda por fuerza bruta puede ser suficiente.
- No necesitas conocer la clave privada real.
"""

# TODO:
# 1. Recibir clave pública y firma legítima.
# 2. Implementar lógica para encontrar colisión en trapdoor_hash().
# 3. Mostrar el mensaje malicioso y su hash.

