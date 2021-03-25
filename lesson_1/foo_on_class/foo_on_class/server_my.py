from contextlib import closing
from socket import *
import json
import time

# Ответы сервераa
LIST_AUTH = [
    {
        "response": 200,
        "alert": "An optional message/notification - Ok!"
    },
    {
        "response": 402,
        "error": "This could be 'wrong password' or 'no account with that name'"
    },
]
PROBE = {
    "action": "probe!!!",
    "time": time.time(),
}

# =====================server=======================================
# =====================server=======================================
HOST = ""
PORT = 1111
BUFSIZ = 2048
ENCODE = 'utf-8'

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(5)

def bind_create_from_user(s_tsp, addr, port):
    return s_tsp.bind((addr, int(port)))


def server_listen_ready(s_tsp):
    return s_tsp.listen(5)


def recved_data(user_socket):
    return user_socket.recv(BUFSIZ)


def b_decode_str_foo(b_data_recvd):  # from b'' (json) to str
    return b_data_recvd.decode(ENCODE)


def str_loads_dict_foo(data_str):  # from str to  dict
    return json.loads(data_str)


def py_dumps_str_foo(param_server):  # from py (dict) to str
    return json.dumps(param_server)




users_sockets = []


def send_all(data):
    for user_socket in users_sockets:
        user_socket.send(data)


def listen_user(user_sock):
    print('listening user')
    while True:
        data = user_sock.recv(BUFSIZ)
        print(f'user send {data.decode(ENCODE)}')

        send_all(data)


def start_server():
    print('server is listening....')
    while True:
        client_socket, addr = server_socket.accept()
        print(f'User <{addr[0]}> подключился только что... ')
        users_sockets.append(client_socket)


def current_start_server(addr, port):
    lst_answers_after_auth_json = py_dumps_str_foo(LIST_AUTH)
    PROBE_json = py_dumps_str_foo(PROBE)
    with tcp_sock_create() as s_tsp:  # создаем сокет сервера
        bind_create_from_user(s_tsp, addr, port)  # связываем сокет с адресом И ПОРТОМ
        print(f'======================')
        server_listen_ready(s_tsp)
        print('Server in listening..........')

        while True:  # бесконечный цикл сервера
            print('Waiting for client...')
            client_socket, addr = s_tsp.accept()  # ждем клиента, при соединении .accept()
            with closing(client_socket):
                print(f'Connected from: {addr[0]}')
                while True:  # цикл связи
                    data = recved_data(client_socket)
                    data_str = b_decode_str_foo(data)
                    data_dict = str_loads_dict_foo(data_str)
                    auth_response_server_list = json.loads(lst_answers_after_auth_json)

                    if not data:
                        break  # разрываем связь если данных нет
                    if 'action' in data_dict and data_dict['action'] == 'authenticate':
                        for var_response in auth_response_server_list:
                            if 'response' in var_response and var_response['response'] == 200:
                                msg = var_response['alert']
                                client_socket.send(bytes(msg, ENCODE))

                    elif 'action' in data_dict and data_dict['action'] == 'presence':
                        msg = PROBE_json.encode(ENCODE)
                        client_socket.send(msg)
                        print('прилетел presence')
                    elif 'action' in data_dict and data_dict['action'] == 'quit':
                        client_socket.send('finish'.encode(ENCODE))
                        print(f'прилетел quit {time.ctime()}')
                    elif 'action' in data_dict and data_dict['action'] != 'authenticate':
                        for var_response in auth_response_server_list:
                            if 'response' in var_response and var_response['response'] == 402:
                                msg = var_response['error']
                                client_socket.send(bytes(msg, ENCODE))
                        print('ошибка auth')


if __name__ == '__main__':
    # current_start_server(HOST, PORT)
    start_server()
