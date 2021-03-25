import socket

BUFF = 2048
ENCODDING = 'utf-8'

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect(('localhost', 1111))  # установка связи с сервером


def listen_server():
    while True:
        data = client_sock.recv(BUFF)
        print(data.decode(ENCODDING))


def send_to_server():
    while True:
        client_sock.send(input(':::').encode(ENCODDING))


if __name__ == '__main__':
    send_to_server()