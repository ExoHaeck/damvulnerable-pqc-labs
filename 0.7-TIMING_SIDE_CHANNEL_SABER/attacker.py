# attacker.py
"""
Timing Side-Channel – Saber (CTF)

Objetivo:
Medir los tiempos de respuesta del servidor vulnerado por canal lateral de tiempo
y reconstruir la clave secreta de 8 bits.

Pistas:
- El servidor escucha en `127.0.0.1:5000` y devuelve, por cada ciphertext recibido,
  el tiempo que tardó en procesarlo.
- Los bits en 1 añaden un retardo de ~0.5 s cada uno.
- Mide un tiempo “base” con un ciphertext todo zeros, luego ataca bit a bit poniendo 0xFF
  en la posición correspondiente de un array de 8 bytes.
- Promedia varias mediciones para reducir ruido, luego compara contra el base time.

Entrega:
Imprime al final únicamente la cadena binaria de 8 bits reconstruida:
    01001011
"""

import socket
import binascii

HOST = "127.0.0.1"
PORT = 5000

KEY_LENGTH = 8
BIT_DELAY = 0.5  # debes usar el mismo valor que en vulnerable_saber.py

def handle_request(sock, hex_ct: str) -> float:
    """
    Envía un ciphertext (en hex) al servidor y devuelve el tiempo que tardó en procesarlo.
    """
    # TODO: implementar
    pass

def medir_promedio(sock, ciphertext: bytes, repeticiones=4) -> float:
    """
    Llama varias veces a handle_request() y devuelve el tiempo promedio.
    """
    # TODO: implementar
    pass

if __name__ == "__main__":
    # 1) Conectar al servidor
    # 2) Medir tiempo base con un ciphertext de KEY_LENGTH ceros
    # 3) Atacar bit a bit: para cada posición i, crear un ciphertext de KEY_LENGTH bytes,
    #    poner 0xFF en el byte i, medir y comparar con el tiempo base
    # 4) Reconstruir la lista recovered_bits de 0s y 1s
    # 5) Imprimir en pantalla: "[+] Clave recuperada: <bits>"
    
    # Ejemplo de impresión final:
    # [+] Clave recuperada: 01001011
    
    # TODO: completar el flujo descrito arriba
    pass














