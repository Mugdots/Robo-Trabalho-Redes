import socket


endereco_servidor = ("127.0.0.1", 2024)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(endereco_servidor)

while True:
    server_socket.listen(1)  

    # Aceita uma conexão do cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexão aceita de {client_address}")

    while True:
        data = client_socket.recv(2048) 
        if not data:
            print("Conexão fechada pelo cliente")
            break
        
        print(f": {data.decode('utf-8')}")
        response = "Mensagem recebida com sucesso!"
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()
server_socket.close()