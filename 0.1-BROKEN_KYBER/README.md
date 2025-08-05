# Broken Parameter Selection – Kyber (Laboratorio)

Este laboratorio simula una vulnerabilidad en Kyber causada por **selección incorrecta de parámetros** (`ETA1` y `ETA2` demasiado bajos), lo que reduce la dureza del problema LWE.

## Estructura
- `kyber_params.py` → Parámetros inseguros (modificables)
- `utils.py` → Funciones auxiliares
- `generate_instance.py` → Genera `A`, `b`, `s` vulnerables
- `attack_lwe.py` → Aplica LLL para intentar recuperar `s`
- `data/` → Guarda instancias y resultados

## Uso
1. Instalar dependencias:
```bash
pip install numpy fpylll
