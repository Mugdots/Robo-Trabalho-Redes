import time
import socket
import random

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
            es = random.randint(0, 1)
            
            for i in range(2):     
                for j in range(20):
                    mensagem = f"controle;{lado[(i - es) ** 2]}"
                    
                    sent = sock.sendto(mensagem.encode(), endereco_servidor)            
                    time.sleep(0.01)
        
        if acao == 'pular':
            lado = input("Escolha o lado (left, right): ")
            ladoA = [lado, 'up']
            ladoE = [lado, 'down']
            for i in range(20):        
                mensagem = f"controle;{ladoA[i % 2]}"
                
                sent = sock.sendto(mensagem.encode(), endereco_servidor)            
                time.sleep(0.02)
            
            for i in range(5):        
                mensagem = f"controle;{lado}"
                
                sent = sock.sendto(mensagem.encode(), endereco_servidor)            
                time.sleep(0.02)
            
            for i in range(20):        
                mensagem = f"controle;{ladoE[i % 2]}"
                
                sent = sock.sendto(mensagem.encode(), endereco_servidor)            
                time.sleep(0.02)
        
        mensagem = f"controle;{acao}"
        if mensagem:
            sent = sock.sendto(mensagem.encode(), endereco_servidor)
finally:
    print("Fechando socket")
    sock.close()
