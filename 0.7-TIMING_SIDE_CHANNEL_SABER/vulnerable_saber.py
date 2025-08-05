import os
import time

KEY_LENGTH = 8  # clave cortísima

def fake_saber_keypair():
    sk_bits = [os.urandom(1)[0] % 2 for _ in range(KEY_LENGTH)]
    pk = os.urandom(2)
    return pk, sk_bits

def kem_decapsulate(ciphertext: bytes, sk_bits: list[int]):
    """
    Time side-channel simulated: cada bit=1 provoca 0.5s extra de sleep.
    """
    delay = 0.0
    for i, bit in enumerate(sk_bits):
        if bit == 1 and ciphertext[i % len(ciphertext)] == 0xFF:
            delay += 0.5
    time.sleep(delay)
    return os.urandom(2), delay









