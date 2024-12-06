import time
import socket
import random

# Set up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endereco_servidor = ("127.0.0.1", 2024)
sock.connect(endereco_servidor)


# Send commands
try:
    while True:
        acao = input()
        mensagem = f"controle;{acao}"
        if mensagem:
            sent = sock.sendall(mensagem.encode())
        while True:
            mensagemRecebida = sock.recv(1024).decode('utf-8')
            if mensagemRecebida:
                print(mensagemRecebida)
                break
            
        
finally:
    print("Fechando socket")
    sock.close()
