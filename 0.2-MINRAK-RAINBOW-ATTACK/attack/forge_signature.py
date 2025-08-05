# attack/forge_signature.py

import sys, os, pickle
from itertools import product
from sage.all import GF


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from attack.reconstructor import load_public_polys

F = GF(2)

def brute_forge(polys):
    """
    ─── ¡A IMPLEMENTAR! ────────────────────────────────────────────
    Dada la lista de polinomios públicos `polys`, busca un vector x en {0,1}^n
    tal que P_i(x) == 0 para cada i.

    - n = polys[0].parent().ngens()
    - Recorre todos los bits en itertools.product([0,1], repeat=n)
    - Convierte cada tupla `bits` a lista/tupla de enteros (0 o 1)
    - Evalúa todos los polinomios: if all(int(poly(*x_bits)) == 0)
      devuelve x_bits como tuple
    - Si al final no hay ninguno, devuelve None
    ────────────────────────────────────────────────────────────────
    """
    raise NotImplementedError("Implementa aquí tu función brute_forge")

if __name__ == "__main__":
    print("[*] Cargando polinomios centrales...")
    polys = load_public_polys()
    if not polys:
        sys.exit(1)

    print("[*] Buscando vector que anule todos los P_i(x)=0 …")
    x = brute_forge(polys)
    if x is None:
        print("[-] No se halló firma válida.")
        sys.exit(1)

    print(f"[✔] Firma falsificada encontrada: {x}")
    
    forged_dir = os.path.join(ROOT, "keys", "forged")
    os.makedirs(forged_dir, exist_ok=True)
    path = os.path.join(forged_dir, "forged_signature.pkl")
    with open(path, "wb") as f:
        pickle.dump(x, f)
    print(f"[✔] Firma guardada en {path}")
