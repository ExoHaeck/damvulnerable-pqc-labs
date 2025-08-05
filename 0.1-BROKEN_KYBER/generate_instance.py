# generate_instance.py
import numpy as np
from utils import gen_noise, gen_matrix, save_json
from kyber_params import N, Q, ETA1

# Generar instancia vulnerable
A = gen_matrix()
s = gen_noise(N, ETA1)
e = gen_noise(N, ETA1)
b = (A @ s + e) % Q

# Guardar en data/instance.json
save_json("data/instance.json", {
    "A": A.tolist(),
    "b": b.tolist(),
    "q": Q,
    "secret_s": s.tolist()  # Solo para verificar en el laboratorio
})

print("[+] Instancia vulnerable generada en data/instance.json")
