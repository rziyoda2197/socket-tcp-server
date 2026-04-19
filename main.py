import socket

def echo_server():
    # Server porti
    port = 12345

    # Server socket yaratish
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server portiga qo'shish
    server_socket.bind(('localhost', port))

    # Server porti ochish
    server_socket.listen(1)

    print(f"Server ishlayapti. Port: {port}")

    while True:
        # Klientga qo'shish
        client_socket, client_address = server_socket.accept()

        # Klientdan xabar qabul qilish
        data = client_socket.recv(1024)

        # Xabar qaytarish
        client_socket.sendall(data)

        # Klientni yopish
        client_socket.close()

echo_server()
