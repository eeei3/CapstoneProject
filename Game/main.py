# ---------------------------------------------
# Title: main.py
# Class: CS 30
# Date: 15/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: main.py

This file contains important GUI code.
Always run the game from this file.
"""
from tkinter import *
from multiprocessing import Process
import connection
import battle


# Represents the graphical user interface of the game.
class GUI:
    def __init__(self):
        """
        Initialize the GUI object.
        """
        self.mainframe = None
        self.main = Tk()
        self.pipe = None
        self.online = False
        self.op = False
        self.game = False
        self.ip = None
        self.port = None
        self.process1 = None
        self.process2 = None
        self.process3 = None
        self.connect_process = None

    def connec(self, ip, port):
        """
        Connects to another player's game.
        """
        ip = self.ip.get()
        port = self.port.get()
        self.pipe = connection.GameConnection(ip, port)
        self.pipe.make_connection()

    def makeserver(self, ip, port):
        """
        Creates a game server.
        """
        self.pipe = connection.GameConnection(ip, port)
        self.pipe.create_server()

    def offgame(self):
        """
        Starts an offline game with a bot.
        """
        self.process2 = Process(target=self.offgame_wrapper())
        self.process2.start()

    def offgame_wrapper(self):
        """
        Wraps the function for starting an offline game with a bot.
        """
        self.game = battle.LBattle()
        self.game.game_ui()

    def joingame(self):
        """
        Joins a hosted game on a server.
        """
        ip = self.ip.get()
        port = self.port.get()
        self.pipe = connection.GameConnection(ip, port)
        try:
            self.pipe.connec(ip, port)
        except Exception as e:
            print("Could not connect!")
        self.process1.start()

    def ongame(self):
        """
        Starts a new server for hosting a game.
        """
        ip = self.ip.get()
        port = self.port.get()
        try:
            self.process3 = Process(target=self.pipe.makeserver, args=(ip, port,))
            self.process3.start()
        except Exception as e:
            self.process3.join()
            print("Could not create a new server!")
        self.process3.join()

        def quit_game(self):
            """
            Quits the game and closes the GUI.
            """
            self.main.destroy()

    def temp_name(self):
        """
        Design the main title screen.
        """
        self.ip = StringVar(self.main)
        self.port = StringVar(self.main)
        self.ip.set("Enter IP Address Here")
        self.port.set("Enter Port Number Here")
        self.main.geometry("600x900")
        self.main.title("Pokémon Battle - Title Screen")
        maintitle = Label(self.main, text="Welcome to the Pokemon Battle!", font=("MS Comic Sans", "18"))
        maintitle.pack(ipadx=20, ipady=10, expand=True)
        choice1 = Label(self.main, text="Join a battle server", font=("MS Comic Sans", "14"))
        choice1.pack(ipadx=20, ipady=20, expand=True)
        ip1 = Entry(self.main, textvariable=self.ip)
        ip1.pack(ipadx=20)
        port1 = Entry(self.main, textvariable=self.port)
        port1.pack(ipadx=20)
        connect1 = Button(self.main, text="Connect!", command=self.joingame)
        connect1.pack()
        choice2 = Label(self.main, text="Create a battle server", font=("MS Comic Sans", "14"))
        choice2.pack(ipadx=20, ipady=20, expand=True)
        ip2 = Entry(self.main, textvariable=self.ip)
        ip2.pack(ipadx=20)
        port2 = Entry(self.main, textvariable=self.port)
        port2.pack(ipadx=20)
        create = Button(self.main, text="Create Server!", command=self.ongame)
        create.pack()
        choice3 = Label(self.main, text="Play an offline bot!", font=("MS Comic Sans", "14"))
        choice3.pack(ipadx=20, ipady=20, expand=True)
        start = Button(self.main, text="Play Bot!", command=self.offgame)
        start.pack()
        credit = Label(self.main, text="This program was made by Calvin, Ebaad and Josh", font=("MS Comic Sans", "10"))
        credit.pack(ipadx=20, ipady=20, expand=True)
        quit_button = Button(self.main, text="Quit", command=self.quit_game)
        quit_button.pack()
        self.main.mainloop()


if __name__ == "__main__":
    b = GUI()
    b.temp_name()
