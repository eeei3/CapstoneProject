"""
Joshua
CS 30 Period 1
May 12, 2023
This is the module relating to connecting for pvp
"""
import socket
import time


class GameConnection:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = (ip, port)
        self.sdata = None
        self.rdata = None
        self.accept_connection = False

    def make_connection(self):
        try:
            ip = self.get_local_ip()
            message = "User " + ip + "wishes to connect to your machine"
            self.socket.connect(self.connection)
            self.socket.sendall(message)
            data = self.socket.recv(5024)
            if data == "Accept":
                print("Server has accepted your connection! Prepare for battle.")
                self.socket.sendall(b"Connect")
            else:
                print("Server has refused your connection!")
                return 1

        except Exception as e:
            print("Failed to connect to host")
            print(e)
        else:
            self.connect()


    def create_server(self):
        try:
            await_connect = True
            self.socket.bind(self.connection)
            self.socket.listen()
            conn, addr = self.socket.accept()
            with conn:
                while await_connect:
                    data = conn.recv(5024)
                    if data == "Connect":
                        await_connect = False
                    else:
                        pass
                self.connect()

        except Exception as e:
            print("There has been a connection error!")
            print(e)

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def connect(self):
        connec = True
        while connec:
            self.socket.sendall(self.sdata)
            self.rdata = self.socket.recv(5024)
            self.sdata = None
            time.sleep(1)
