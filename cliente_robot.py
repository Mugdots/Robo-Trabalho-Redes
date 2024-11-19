import time
import socket

# Set up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 2025))
endereco_servidor = ("127.0.0.1", 2024)

# Send commands
try:
    while True:
        acao = input("Entre com o comando (up, down, left, right) ou para sair (q): ").strip().lower()
        if acao == 'q':
            break
        if acao == 'correr':
            lado = input("Escolha o lado (left, right): ")
            velocidade = int(input("Escolha quantos passo por segundo: "))
            
            for i in range(20):
                
                mensagem = f"controle;{lado}"
                
                sent = sock.sendto(mensagem.encode(), endereco_servidor)            
                time.sleep(1 / velocidade * 10)
        if acao == 'esquivar':
            
            lado = ['left', 'right'] 
            for i in range(20):
                
                mensagem = f"controle;{lado[0]}"
                
                sent = sock.sendto(mensagem.encode(), endereco_servidor)            
                time.sleep(0.01)
            
            for i in range(20):
                
                mensagem = f"controle;{lado[1]}"
                
                sent = sock.sendto(mensagem.encode(), endereco_servidor)            
                time.sleep(0.01)
            
            
        
        mensagem = f"controle;{acao}"
        if mensagem:
            sent = sock.sendto(mensagem.encode(), endereco_servidor)
finally:
    print("Fechando socket")
    sock.close()
