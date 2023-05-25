# ---------------------------------------------
# Title: connection.py
# Class: CS 30
# Date: 11/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: connection.py


"""
import socket
import time
from multiprocessing import Process


"""
HOW THIS FILE WORKS:
FOR THE SERVER:
The server opens up a port on it's IP Address
The server waits for a connection
If the connection sends the word "Accept" 
the server responds with the word "Connect"
Once this exchange has compeleted, the server
will send it's data and read the received data from
the client every second
"""


class GameConnection:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = (ip, port)
        self.sdata = None
        self.rdata = None
        self.accept_connection = False
        self.connec = False
        self.process1 = Process(target=self.mail)
        self.process2 = Process(target=self.listen)

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
            self.connec = True
            self.process2.start()
            self.process1.start()

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

    def listen(self):
        while self.connec:
            self.rdata = self.socket.recv(5024)

    def mail(self):
        while self.connec:
            self.socket.sendall(self.sdata)
            self.sdata = None
