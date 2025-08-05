# lab.py
import os, pickle, random
from itertools import product
from sage.all import GF, PolynomialRing, Matrix

# Parámetros Rainbow reducidos
F    = GF(2)
v1   = 3           # # variables vinegar (umbral MinRank)
o1   = 2           # # variables oil
n    = v1 + o1     # dimensión total
TARGET_RANK = v1   # buscamos rango ≤ v1

def gen_central_polys():
    """Genera o1 polinomios Oil-Vinegar en GF(2)[x0..x{n-1}]."""
    R    = PolynomialRing(F, n, "x")
    vars = R.gens()
    polys = []
    for _ in range(o1):
        p = R(0)
        # términos cuadráticos válidos
        for i in range(n):
            for j in range(i, n):
                if i < v1 or j < v1:
                    if random.getrandbits(1):
                        p += vars[i]*vars[j]
        # términos lineales
        for i in range(n):
            if random.getrandbits(1):
                p += vars[i]
        # constante
        if random.getrandbits(1):
            p += 1
        polys.append(p)
    return polys

def polynomials_to_matrices(polys):
    """Convierte cada polinomio a su matriz cuadrática en GF(2)."""
    def poly_to_matrix(poly):
        M = Matrix(F, n, n, 0)
        for exps, coeff in poly.dict().items():
            c = int(coeff)
            if c == 0:
                continue
            exps_list = list(exps)
            degree = sum(exps_list)
            if degree != 2:
                continue
            # caso x_i^2
            if 2 in exps_list:
                for idx, e in enumerate(exps_list):
                    if e == 2:
                        M[idx, idx] += 1
                        break
            else:
                i, j = [k for k,e in enumerate(exps_list) if e == 1]
                M[i, j] += 1
                M[j, i] += 1
        return M

    return [poly_to_matrix(p) for p in polys]

def minrank_attack(matrices):
    """
    ─── ¡A IMPLEMENTAR! ────────────────────────────────────────────
    Debe devolver (coeffs, combined_matrix) tales que
        rank(combined_matrix) ≤ TARGET_RANK

    - `matrices` es una lista [M1, M2, …, Mm]
    - `coeffs` debe ser una tupla de 0/1 de longitud m
    - `combined_matrix` = c1*M1 + … + cm*Mm

    Ejemplo de retorno válido:
       return (1,0,1),  M1 + M3

    ────────────────────────────────────────────────────────────────
    """
    raise NotImplementedError("Implementa aquí tu MinRank attack")

def main():
    os.makedirs("keys", exist_ok=True)
    
    polys = gen_central_polys()
    with open("keys/rainbow_public_key.pkl", "wb") as f:
        pickle.dump(polys, f)

    
    mats = polynomials_to_matrices(polys)
    coeffs, combined = minrank_attack(mats)

    
    os.makedirs("attack/output", exist_ok=True)
    with open("attack/output/minrank_solution.pkl", "wb") as f:
        pickle.dump({"coeffs": coeffs, "matrix": combined}, f)

    print(f" Instancia rota con coeficientes {coeffs} y rango {combined.rank()}")

if __name__ == "__main__":
    main()
