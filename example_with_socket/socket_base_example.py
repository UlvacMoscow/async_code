import socket


def run():
    #server part
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsocopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        #clien part
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(addr)

        response = generate_response(request)

        client_socket.sendall('Hello world'.encode())
        client_socket.close()


def generate_response(response):
    pass



if __name__ == "__main__":
    run()