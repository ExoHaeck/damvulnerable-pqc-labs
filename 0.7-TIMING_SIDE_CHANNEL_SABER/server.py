# server.py
import socket, binascii, time
from vulnerable_saber import kem_decapsulate
from key_store import sk_server_bits

HOST = "127.0.0.1"
PORT = 5000

print(f"[*] Servidor iniciado en {HOST}:{PORT}")
print(f"[*] Clave secreta (bits): {''.join(map(str, sk_server_bits))}")

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"[*] Cliente conectado desde {addr}")
        with conn.makefile("rwb") as f:
            while True:
                line = f.readline()
                if not line:
                    print("[*] Cliente desconectado")
                    break

                hex_ct = line.strip().decode()
                try:
                    ct = binascii.unhexlify(hex_ct)
                except:
                    print("[!] Datos no hex, cerrando")
                    break

                start = time.perf_counter()
                kem_decapsulate(ct, sk_server_bits)
                elapsed = time.perf_counter() - start

                # Devolver el tiempo en segundos
                f.write(f"{elapsed:.6f}\n".encode())
                f.flush()
        # vuelve a esperar un nuevo cliente













