import socket

class SocketClass(socket.socket):
    def __init__(self):
        super(SocketClass,self).__init__(
             socket.AF_INET,
            socket.SOCK_STREAM,
        )
    def send_data(self):
        raise NotImplementedError()
