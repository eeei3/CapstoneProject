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
        # self.game.game_ui()

    def quit_game(self):
        """
        Quits the game and closes the GUI.
        """
        self.main.destroy()

    def temp_name(self):
        """
        Design the main title screen.
        """
        self.main.geometry("600x400")
        self.main.title("Pokémon Battle - Title Screen")
        maintitle = Label(self.main, text="Welcome to the Pokemon Battle!", font=("MS Comic Sans", "18"))
        maintitle.pack(ipadx=20, ipady=10, expand=True)
        choice3 = Label(self.main, text="Play a Trainer!", font=("MS Comic Sans", "14"))
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
