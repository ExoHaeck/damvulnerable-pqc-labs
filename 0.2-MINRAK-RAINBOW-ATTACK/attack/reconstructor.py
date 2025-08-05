# attack/reconstructor.py

import os
import pickle
from sage.all import *

def load_public_polys(path="keys/rainbow_public_key.pkl"):
    print("[*] Cargando polinomios centrales...")
    if not os.path.exists(path):
        print(f"[-] Archivo no encontrado: {path}")
        return []
    with open(path, "rb") as f:
        polys = pickle.load(f)
    print(f"[✓] {len(polys)} polinomios cargados.")
    return polys

def poly_to_matrix(poly, num_vars):
    """
    Convierte un polinomio cuadrático en su matriz simétrica en GF(2).
    Solo considera monomios de grado EXACTO 2.
    """
    mat = Matrix(GF(2), num_vars, num_vars, 0)

    for exp_tuple, coeff in poly.dict().items():
        c = int(coeff)
        if c == 0:
            continue

        # exp_tuple
        exps = list(exp_tuple)
        degree = sum(exps)
        if degree != 2:
            continue

        # Caso x_i^2 
        if 2 in exps:
            for idx, e in enumerate(exps):
                if e == 2:
                    mat[idx, idx] += 1
                    break
        else:
            
            idxs = [i for i, e in enumerate(exps) if e == 1]
            i, j = idxs
            mat[i, j] += 1
            mat[j, i] += 1

    return mat

def extract_all_matrices(polys):
    if not polys:
        return []
    num_vars = polys[0].parent().ngens()
    return [poly_to_matrix(p, num_vars) for p in polys]

if __name__ == "__main__":
    polys = load_public_polys()
    if not polys:
        exit(1)

    matrices = extract_all_matrices(polys)
    for i, mat in enumerate(matrices, start=1):
        print(f"\nMatriz {i}:")
        print(mat.str())
