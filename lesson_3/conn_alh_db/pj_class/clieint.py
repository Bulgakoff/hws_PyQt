import json
from sockett import SocketClass
# from pj_class.sockett import SocketClass
import time
from threading import Thread

from DataCl import AnwQuit, Authenticate, Presence, \
    Responce, ResponceError, Probe

#
# BUFF = 2048
# ENCODDING = 'utf-8'
# HOST = "localhost"
# PORT = 1111
# запросы клиента:
quit = {
    'action': 'quit'
}
AUTH_CLIENT = {
    'action': 'authenticate',
    'time': 'qwe',
    'user': {
        'account_name': 'Alex',
        'password': 'parol'
    }
}
PRESENTS_MSG = {
    'action': 'presence',
    'time': 'qwe',
    'type': 'status',
    'user': {
        'account_name': 'Alex',
        'status': 'Yep, I am here!'
    }
}


class ClientSock(SocketClass):
    def __init__(self):
        super(ClientSock, self).__init__()

        self._get_time_foo = time.ctime

    def py_dumps_str_foo(self, param_user):
        return json.dumps(param_user)

    def b_decode_str_foo(self, b_request_recvd):  # from b'' (json) to str
        return b_request_recvd.decode(self.ENCODDING)

    def str_loads_dict_foo(self, request_str):  # from str to  dict
        return json.loads(request_str)

    # def to_do_deserialize(self, msg_bytes):
    #     msg_bytes_str = msg_bytes.decode(self.ENCODDING)
    #     exit_msg_py = json.loads(msg_bytes_str)
    #     return exit_msg_py

    def parse(self, parser_data_py):
        if "action" in parser_data_py:
            action = parser_data_py["action"]
            if action == "quit":
                return AnwQuit(action=parser_data_py['action'])

            elif action == "authenticate":
                return Authenticate(account_name=parser_data_py["user"]["account_name"],
                                    password=parser_data_py["user"]["password"])
            elif action == "presence":
                return Presence(account_name=parser_data_py["user"]["account_name"],
                                status=parser_data_py["user"]["status"])
            elif action == "probe!!!":
                return Probe(action=parser_data_py['action'])

        elif "response" in parser_data_py:
            response = parser_data_py["response"]
            if response == "200":
                return Responce(response=parser_data_py['response'],
                                alert=parser_data_py['alert'])
            elif response == "402":
                return ResponceError(response=parser_data_py['response'],
                                     error=parser_data_py['error'])

    def on_msg(self, msg):
        if isinstance(msg, Probe):
            self.on_probe(msg)

    def on_probe(self, msg_data_class):
        # добавляем в список клиентов ?????
        if msg_data_class.action == "probe!!!":
            response_err = AnwQuit('quit')
            data = self.serialize(response_err)
            time.sleep(10)
            self.send(data)
        else:
            pass

    def serialize(self, obj_A_msg):
        if isinstance(obj_A_msg, Authenticate):
            result_py = {
                'action': 'authenticate',
                # 'action': 'dfgdfg',
                'time': self._get_time_foo(),
                'user': {
                    'account_name': obj_A_msg.account_name,
                    'password': obj_A_msg.password
                }
            }
            result_str = json.dumps(result_py)
            result_byte = result_str.encode(self.ENCODDING)
            return result_byte
        elif isinstance(obj_A_msg, Responce):
            result_py = {
                "response": obj_A_msg.response,
                "alert": obj_A_msg.alert
            }
            result_str = json.dumps(result_py)
            result_byte = result_str.encode(self.ENCODDING)
            return result_byte
        elif isinstance(obj_A_msg, ResponceError):
            result_py = {
                "response": obj_A_msg.response,
                "error": obj_A_msg.error
            }
            result_str = json.dumps(result_py)
            result_byte = result_str.encode(self.ENCODDING)
            return result_byte
        elif isinstance(obj_A_msg, AnwQuit):
            result_py = {
                'action': 'quit',
            }
            result_str = json.dumps(result_py)
            result_byte = result_str.encode(self.ENCODDING)
            return result_byte

    def set_up(self):
        self.connect((self.HOST, self.PORT))  # установка связи с сервером

        # self.send_data(AUTH_CLIENT)
        listen_thread = Thread(target=self.listen_socket)
        listen_thread.start()

        send_data_thread = Thread(target=self.send_data, args=(AUTH_CLIENT,))
        send_data_thread.start()



    def listen_socket(self, listened_sock=None):
        while True:
            data = self.recv(self.BUFF)
            if not data:
                break
            # data = data.decode(self.ENCODDING)
            elif data.decode(self.ENCODDING) == 'OK!':
                self.send_data(PRESENTS_MSG)
            # elif data.decode(self.ENCODDING) == '{"action": "probe!!!",}':
            elif data.decode(self.ENCODDING) == 'finished!!!':
                print(f'server  send ========> FINISH')
                time.sleep(6)
                break
            else:
                parser_data_str = self.b_decode_str_foo(data)  # decode=> str
                parser_data_py = self.str_loads_dict_foo(parser_data_str)  # loads =>  dict
                msg_data_class = self.parse(parser_data_py)  # => dataclass
                self.on_msg(msg_data_class)

                # listened_sock.send(self.py_dumps_str_foo(PRESENTS_MSG).encode(self.ENCODDING))
                # print(data.decode(self.ENCODDING))

            print(f'==========>{data.decode(self.ENCODDING)}')

    def send_data(self, data):
        # while True:
        time.sleep(2)
        self.send(self.py_dumps_str_foo(data).encode(self.ENCODDING))
        # break

    # listen_server()


if __name__ == '__main__':
    client = ClientSock()
    client.set_up()
