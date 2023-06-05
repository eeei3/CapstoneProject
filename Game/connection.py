# ---------------------------------------------
# Title: connection.py
# Class: CS 30
# Date: 11/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: connection.py

This file contains the GameConnection class that handles the network connection for the game.
"""

import socket
from multiprocessing import Process


# Game Connection object, used for network connection ingame
class GameConnection:
    def __init__(self, ip, port):
        """
        Initialize the GameConnection object.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = (ip, port)
        self.sdata = None
        self.rdata = None
        self.accept_connection = False
        self.connec = False
        self.process1 = Process(target=self.mail)
        self.process2 = Process(target=self.listen)

    def make_connection(self):
        """
        Make a connection to the server.
        """
        try:
            ip = self.get_local_ip()
            message = "User " + ip + "wishes to connect to your machine"
            self.socket.connect(self.connection)
            self.socket.sendall(message.encode())
            data = self.socket.recv(5024)
            if data == b"Accept":
                print("Server has accepted your connection! Prepare for battle.")
                self.socket.sendall(b"Connect")
            else:
                print("Server has refused your connection!")
                return 1

        except Exception as e:
            print("Failed to connect to host")
            print(e)
            return 1
        else:
            self.connec = True
            self.process2.start()
            self.process1.start()

    def create_server(self):
        """
        Create a server and wait for a connection.
        """
        try:
            await_connect = True
            self.socket.bind(self.connection)
            self.socket.listen()
            conn, addr = self.socket.accept()
            with conn:
                while await_connect:
                    data = conn.recv(5024)
                    if data == b"Connect":
                        await_connect = False
                    else:
                        pass
                self.connect()

        except Exception as e:
            print("There has been a connection error!")
            print(e)
            return 1

    def get_local_ip(self):
        """
        Get the local IP address.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def listen(self):
        """
        Listen for incoming data from the server.
        """
        while self.connec:
            self.rdata = self.socket.recv(5024)

    def mail(self):
        """
        Send data to the server.
        """
        while self.connec:
            if self.sdata:
                self.socket.sendall(self.sdata)
                self.sdata = None
