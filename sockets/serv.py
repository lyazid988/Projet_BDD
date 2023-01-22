import socket

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Received: {request.decode()}")
    client_socket.send(b"hello")
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen(5)
    print("Server is listening on 127.0.0.1:8000...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_client(client_socket)

run_server()