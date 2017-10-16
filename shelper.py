import socket
import select
import os

class SockServer:

    s = None
    timeout = 0.1

    def __init__(self, unix_socket):
        # Make sure the socket does not already exist

        try:
            os.unlink(unix_socket)
        except OSError:
            if os.path.exists(unix_socket):
                raise

        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.s.bind(unix_socket)

    def read_data(self):

        ready = select.select([self.s], [], [], self.timeout)
        if ready[0]:
            size = int(self.s.recv(6))
            buf = self.s.recv(size - 100000)
            return buf

    def close_socket(self):
        self.s.close()

class SockClient:
    s = None

    def __init__(self, unix_socket):
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.s.connect(unix_socket)

    def write_data(self, data):
        size = 100000 + len(data)
        self.s.send(str(size).encode('utf-8'))
        self.s.send(data.encode('utf-8'))

    def close_socket(self):
        self.s.close()
