import socket
from typing import Tuple


class Server:
    def __init__(self, port: int):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('', 8080))
        serversocket.listen(10)
        self.serversocket = serversocket

    def put_point(self, position: Tuple[float, float]):
        (x, y) = position
        self.serversocket.send()