"""
Joshua
CS 30 Period 1
May 12, 2023
This is the module relating to connecting for pvp
"""
import socket


class GameConnection:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = (ip, port)

    def make_connection(self):
        try:
            self.socket.connect(self.connection)
        except Exception as e:
            print("Failed to connect to host")
            print(e)
        else:
            return

    def create_server(self):
        try:
            self.socket.bind(self.connection)
            self.socket.listen()
            conn, addr = self.socket.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
        except Exception as e:
            print("There has been a connection error!")
