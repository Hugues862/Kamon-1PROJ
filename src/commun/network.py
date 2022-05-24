import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        self.bytes = 2048
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(self.bytes).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(self.bytes).decode()
        except socket.error as e:
            print(e)