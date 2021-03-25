from socket import *
import json
import time
import re
from threading import Thread

# запросы клиента:
quit = {
    'action': 'quit'
}
AUTH_CLIENT = {
    'action': 'authenticate',
    # 'action': 'dfgdfg',
    'time': time.ctime(),
    'user': {
        'account_name': 'C0deMaver1ck',
        'password': 'CorrectHorseBatterStaple'
    }
}
PRESENTS_MSG = {  # сообщение о присутствии — presence
    'action': 'presence',
    'time': time.ctime(),
    'type': 'status',
    'user': {
        'account_name': 'C0deMaver1ck',
        'status': 'Yep, I am here!'
    }
}

# ========================client===================================================
BUFSIZ = 640
ENCODE = 'utf-8'
HOST = "localhost"
PORT = 1111


def py_dumps_str_foo(param_user):
    return json.dumps(param_user)


client_sock = socket(AF_INET, SOCK_STREAM)

client_sock.connect((HOST, PORT))  # установка связи с серверо


def listen_server():
    while True:
        data = client_sock.recv(BUFSIZ)
        print(data.decode(ENCODE))


def send_server():
    while True:
        client_sock.send(input(':::::').encode())


# def current_start_client(HOST, port):
#     auth_from_client_json = py_dumps_str_foo(AUTH_CLIENT)
#     msg_presence_json = py_dumps_str_foo(PRESENTS_MSG)
#     quit_json = py_dumps_str_foo(quit)
#
#     client_sock.connect((HOST, int(port)))  # установка связи с сервером
#     time.sleep(3)
#     client_sock.send(auth_from_client_json.encode(ENCODE))
#     data = client_sock.recv(BUFSIZ)  # ожидание (получение) ответа
#
#     if data.decode(ENCODE) == 'An optional message/notification - Ok!':
#         client_sock.send(msg_presence_json.encode(ENCODE))
#         print(data.decode(ENCODE))
#
#     if data.decode(ENCODE) != 'spam':
#         egg = data.decode(ENCODE)
#         match = re.findall(r'wrong', egg)
#         if match:
#             print('authentication denied\n')
#             time.sleep(4)
#             print(data.decode(ENCODE))
#             # break
#
#     if data.decode(ENCODE) != 'spam':
#         egg = data.decode(ENCODE)
#         match = re.findall(r'probe!!!', egg)
#         if match:
#             print('probe!!!')
#             client_sock.send(quit_json.encode(ENCODE))
#             time.sleep(3)
#             # break


if __name__ == '__main__':
    send_server()
    # current_start_client(HOST, PORT)
