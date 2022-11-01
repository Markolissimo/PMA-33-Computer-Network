import socket
from views import *
# ip tcp

URLS={
    '/': index,
    '/home':home,

}

def parse_request(request):
    parsed=request.split(" ")
    print(request)
    print(parsed)
    method=parsed[0]
    url=parsed[1]
    return (method,url)

def generate_headers(method,url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n',405)
    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n',404)
    return ('HTTp/1.1 200 Ok\n\n',200)

def generate_content(code,url):
    if code==404:
        return '<h1>404</h1><p>Not found</p>'
    if code==405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return URLS[url]()

def generate_response(request):
    print(request)
    method,url=parse_request(request)
    headers,code=generate_headers(method,url)
    body=generate_content(code,url)

    return (headers+body).encode()

def run():

    #AF сімя адресів, INET протокол ip , 4 версія
    #tcp глобальна змінна SOCK_STREAM
    #server_socket субєкт з протоколамими які він використовує
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #bind приймає кортеж (перший аргумент адрес, другий число порт)
    server_socket.bind(("localhost",5000))
    #listen перевіряє чи є вхідні пакети
    server_socket.listen()

    while True:
        client_socket, addr=server_socket.accept()
        request=client_socket.recv(1024)
        print("---------------------")
        print(request)
        print()
        print(addr)

        response=generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()

if __name__ == '__main__':
    run()


