# attack/verify_signature.py

import sys, os, pickle
from sage.all import GF

# ──────────────────────────────────────────────────────────────────────────────
# 1) Aseguramos importar desde la raíz del proyecto
# ──────────────────────────────────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# ──────────────────────────────────────────────────────────────────────────────
# 2) Cargamos el loader de polinomios
# ──────────────────────────────────────────────────────────────────────────────
from attack.reconstructor import load_public_polys

# ──────────────────────────────────────────────────────────────────────────────
# 3) Ruta de la firma falsificada
# ──────────────────────────────────────────────────────────────────────────────
SIG_PATH = os.path.join(ROOT, "keys", "forged", "forged_signature.pkl")

def load_forged_signature(path=SIG_PATH):
    if not os.path.exists(path):
        print(f"[-] No se encontró la firma falsificada en: {path}")
        sys.exit(1)
    with open(path, "rb") as f:
        sig = pickle.load(f)
    print(f"[✓] Firma cargada (raw): {sig} (type={type(sig)})")
    return sig

def signature_to_list(x):
    """
    Convierte x (tupla, lista o Sage vector) en lista de ints de Python.
    """
    # Si ya es tuple/list
    if isinstance(x, (tuple, list)):
        return [int(v) for v in x]
    # Si tiene método .list()
    if hasattr(x, "list"):
        try:
            return [int(v) for v in x.list()]
        except Exception:
            pass
    # Intentamos iterar
    try:
        return [int(v) for v in x]
    except Exception as e:
        raise ValueError(f"No pude convertir la firma a lista de enteros: {e}")

def verify_signature(polys, x):
    try:
        x_list = signature_to_list(x)
    except ValueError as e:
        print(f"[!] {e}")
        return False

    print(f"[✓] Firma como lista de ints: {x_list}")

    valid = True
    for idx, poly in enumerate(polys, start=1):
        if poly is None:
            print(f"[!] Polinomio P{idx} es None, lo salto.")
            valid = False
            continue
        try:
            res = poly(*x_list)
            r = int(res)
        except Exception as e:
            print(f"[!] Error al evaluar P{idx}(x): {e}")
            valid = False
            continue

        print(f"P{idx}(x) = {r}")
        if r != 0:
            valid = False

    return valid

if __name__ == "__main__":
    print("[*] Cargando polinomios centrales...")
    polys = load_public_polys()
    if not polys:
        sys.exit("[-] No hay polinomios para verificar.")

    print("[*] Cargando firma falsificada...")
    x = load_forged_signature()

    print("[*] Verificando firma contra los polinomios...")
    if verify_signature(polys, x):
        print("\n ¡Firma VÁLIDA! Has roto el esquema.")
    else:
        print("\n Firma NO válida.")
