import socket



URLS = {'/' : 'Hello index',
        '/blog': 'Hello blog'
        }


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>not found</p>'
    if code == 405:
        return "<h1>405</h1><p> method not allowed</p>"
    return '<h1>{}</h1>'.format(URLS[url]) 


def generate_headers(method, url):
    if not method == 'GET':
        return ('http/1.1 405 method not allowed\n\n', 405)
    if not url in URLS:
        return ('http/1.1 404 page not found\n\n', 400)
    return ('http/1.1 200 OK \n\n', 200)


def parsed_request(request):
    parsed = request.split(' ')
    method, url = parsed[0], parsed[1]
    return method, url             


def generate_response(request):
    method, url = parsed_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)

    return (headers + body).encode()


def run():
    #server part
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        #clien part
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(addr)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()



if __name__ == "__main__":
    run()