# attack_lwe_ctf.py
# Desafío CTF: Recuperación de clave en Kyber con parámetros rotos
# Debes completar las funciones marcadas como TODO para que el script recupere la clave
# en dos escenarios:
#  - ETA1 = 0  → recuperación completa trivial
#  - ETA1 = 1  → recuperación parcial inicial, pero debes aplicar filtrado estadístico
#                para mejorar y lograr el 100% o acercarte lo máximo posible.

import numpy as np
from fpylll import IntegerMatrix, LLL, BKZ
from utils import load_json

# =========================
# Funciones a completar
# =========================

def reduce_mod_q(vec, q):
    """
    Reduce los valores de un vector módulo q y normaliza a [-1, 0, 1]
    TODO: Implementar la lógica de reducción y normalización
    """
    pass  # TODO

def score_candidate(A, b, q, s_candidate):
    """
    Calcula un puntaje para un candidato de clave s:
    norma de (A*s - b) mod q, usando distancia mínima módulo q.
    TODO: Implementar cálculo de norma
    """
    pass  # TODO

# =========================
# Código principal
# =========================

# Cargar instancia vulnerable
data = load_json("data/instance.json")
A = np.array(data["A"])
b = np.array(data["b"])
Q = data["q"]
N = A.shape[0]
s_original = data["secret_s"]

# Construcción del retículo
reps = 6
rows = reps * N + 1
cols = N + 1
M = IntegerMatrix(rows, cols)

for r in range(reps):
    for i in range(N):
        for j in range(N):
            M[r * N + i, j] = int(A[i, j])
        M[r * N + i, N] = int(b[i])
M[rows - 1, cols - 1] = Q

# Reducción
print("[*] Ejecutando LLL inicial...")
LLL.reduction(M)

bkz_params = BKZ.Param(block_size=40)

print("[*] Ejecutando BKZ (pasada 1)...")
BKZ.reduction(M, bkz_params)

print("[*] Ejecutando LLL intermedio...")
LLL.reduction(M)

print("[*] Ejecutando BKZ (pasada 2)...")
BKZ.reduction(M, bkz_params)

print("[*] Ejecutando LLL final...")
LLL.reduction(M)

# Evaluar candidatos
candidates = []
for row in M:
    row_list = list(map(int, list(row)[:N]))
    candidate = reduce_mod_q(row_list, Q)  # <-- Debe funcionar
    match_score = sum(1 for a, b_ in zip(candidate, s_original) if a == b_)
    candidates.append((candidate, match_score))

# Ordenar por coincidencia
candidates.sort(key=lambda x: x[1], reverse=True)

print("\n[+] Clave original:   ", s_original)
print("\n[+] Top 5 por coincidencia:")
for idx, (cand, score) in enumerate(candidates[:5], start=1):
    print(f"   #{idx} -> {cand} ({score}/{N} = {score/N*100:.2f}%)")

# Post-procesado estadístico
# TODO: Elegir el mejor candidato basado en score_candidate()
best_stat_candidate = None  # TODO: seleccionar usando min() y score_candidate
best_stat_score = 0  # TODO: calcular coincidencia con clave original

print("\n[+] Mejor candidato estadístico:")
print(f"    {best_stat_candidate} ({best_stat_score}/{N} = {best_stat_score/N*100:.2f}%)")

# Resultado final
if best_stat_score == N:
    print("\n[✔] Ataque exitoso – clave recuperada por completo")
elif best_stat_score > candidates[0][1]:
    print("\n[✔] Mejora gracias al filtrado estadístico")
else:
    print("\n[!] No se logró mejorar el mejor candidato inicial")








