# utils.py
import numpy as np
import json
from secrets import randbelow
from kyber_params import N, Q

def gen_noise(size, eta):
    """
    Genera vector de ruido en [-eta, eta] y aplica factor de escala.
    ETA debe ser entero en kyber_params.py, y aquí ajustas el factor para simular menos ruido.
    """
    scale_factor = 1  # Cambia este valor para simular ruido menor (0.5 = mitad del ruido)
    max_val = int(2 * eta + 1)  # asegurar entero para randbelow

    return np.array([
        int((randbelow(max_val) - eta) * scale_factor)
        for _ in range(size)
    ])

def gen_matrix():
    """Genera matriz aleatoria NxN módulo Q"""
    return np.random.randint(0, Q, size=(N, N))

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f)

def load_json(path):
    with open(path) as f:
        return json.load(f)

