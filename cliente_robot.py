import time
import socket
import random

# Set up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 2025))
endereco_servidor = ("127.0.0.1", 2024)

def mandarMensagem(acao, tempo=0.02):
    mensagem = f"controle;{acao}"                
    sent = sock.sendto(mensagem.encode(), endereco_servidor)
    time.sleep(tempo)      

# Send commands
try:
    while True:
        acao = input("Entre com o comando (up, down, left, right, pular, correr e esquivar) ou para sair (q): ").strip().lower()
        
        if acao == 'q':
            break
        
        if acao == 'correr':
            lado = input("Escolha o lado (left, right): ").strip().lower()
            velocidade = int(input("Escolha quantos passo por segundo: "))
            
            
            for i in range(20):
                mandarMensagem(lado, tempo=1 / velocidade * 10)
        
        if acao == 'esquivar':
            lado = ['left', 'right'] 
            es = random.randint(0, 1)
            
            for i in range(2):     
                for j in range(20): 
                    mandarMensagem(lado[(i - es) ** 2])
                   
        if acao == 'pular':
            lado = input("Escolha o lado (left, right): ")
            pulo = ['up', '', 'down']
            for i in range(3):      
                for j in range(10):
                    if i == 1 and j % 2 == 0:
                        continue
                    mandarMensagem(lado)
                    mandarMensagem(pulo[i])
                           
        mensagem = f"controle;{acao}"
        if mensagem:
            sent = sock.sendto(mensagem.encode(), endereco_servidor)
finally:
    print("Fechando socket")
    sock.close()
