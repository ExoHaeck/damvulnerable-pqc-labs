# Timing Side-Channel – Saber (CTF)

## Descripción  
En este reto simulamos un ataque por canal lateral de tiempo contra una implementación vulnerable de Saber KEM.  
La función de decapsulación introduce un retraso **proporcional** a cada bit `1` de la clave secreta, y midiendo ese tiempo podrás reconstruir la clave completa de 8 bits.

## Objetivo  
Implementar un cliente (`attacker.py`) que:
1. Se conecte al servidor vulnerable (`127.0.0.1:5000`).  
2. Mida un **tiempo base** con un ciphertext de ceros.  
3. Envíe 8 ciphertexts distintos (activando un solo bit a la vez) y mida el tiempo para cada uno.  
4. Compare contra el tiempo base y determine si cada bit es `0` o `1`.  
5. Imprima en pantalla la cadena binaria de 8 bits recuperada.

## Archivos  
- **`vulnerable_saber.py`** → Simula la generación de clave y la decapsulación vulnerable.  
- **`key_store.py`**       → Guarda/recarga la misma clave secreta en `shared_key.json`.  
- **`server.py`**          → Espera conexiones TCP, recibe ciphertexts y devuelve tiempos.  
- **`attacker.py`**        → Esqueleto para que implementes el ataque (debes completarlo).  
- **`shared_key.json`**    → Se crea automáticamente la primera vez al levantar el server.

## Preparación  
1. Clona/descarga este directorio y muévete a él.  
2. Asegúrate de tener instalado Python 3 y la librería estándar.  
3. Si existe `shared_key.json` de pruebas anteriores, bórralo:
   ```bash
   rm shared_key.json

