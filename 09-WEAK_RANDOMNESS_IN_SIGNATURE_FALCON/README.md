# Weak Randomness in Signature – Falcon

## Descripción
En este reto tienes un esquema de firma tipo Falcon simplificado donde el nonce **k** se genera con `random.seed(ts)` usando únicamente la marca de tiempo en segundos.  
Por tanto, **k es completamente predecible** y permite recuperar la clave privada **sk**.

## Objetivo
Completar `attacker.py` para:
1. Leer `Public key`, `Message` y `Signature` (hex).  
2. Extraer `ts` (los primeros 4 bytes de la firma) y `sig_int`.  
3. Regenerar `k = random.getrandbits(16)` con `random.seed(ts)`.  
4. Calcular `h = SHA256(message) mod Q`.  
5. Recuperar `sk = (sig_int - h) * inv_mod(k, Q) mod Q`.  
6. Imprimir `[+] Clave privada recuperada (sk): <valor>`.

## Archivos
- `vulnerable_falcon.py`     → Firma vulnerable.  
- `utils.py`                 → Inverso modular y constantes.  
- `generate_signature.py`    → Genera el reto.  
- `attacker.py`              → Esqueleto que debes completar.

## Uso

1. Genera el reto:
   ```bash
   python3 generate_signature.py
