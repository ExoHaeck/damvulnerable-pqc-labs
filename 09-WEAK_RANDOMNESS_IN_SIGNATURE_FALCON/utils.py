# utils.py
import math

Q = 2**16

def egcd(a: int, b: int):
    if b == 0:
        return (1, 0, a)
    x, y, g = egcd(b, a % b)
    return (y, x - (a // b) * y, g)

def inv_mod(a: int, q: int) -> int:
    """
    Inverso modular de a mod q, asumiendo gcd(a,q)=1.
    """
    x, y, g = egcd(a, q)
    if g != 1:
        raise ValueError("No existe inverso")
    return x % q
