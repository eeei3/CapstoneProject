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
import threading
import battle
import time


# Represents the graphical user interface of the game.
class GUI:
    def __init__(self):
        """
        Initialize the GUI object.
        """
        self.mainframe = None
        self.main = Tk()
        self.op = False
        self.game = False
        self.start = None
        self.process1 = None
        self.process2 = None
        self.process3 = None
        self.connect_process = None
        self.name = StringVar(self.main)
        self.name.set("Pick your username")

    def offgame(self):
        """
        Starts an offline game with a bot.
        """
        self.process2 = threading.Thread(target=self.offgame_wrapper())
        self.process2.start()

    def offgame_wrapper(self):
        """
        Wraps the function for starting an offline game with a bot.
        """
        self.main.withdraw()
        self.game = battle.LBattle(1)
        print("done")
        self.main.deiconify()

    def quit_game(self):
        """
        Quits the game and closes the GUI.
        """
        self.main.destroy()

    def checker(self):
        while True:
            while self.name.get() == "Pick your username" or self.name.get() == "":
                self.start.config(state="disabled")
            self.start.config(state="normal")
            time.sleep(1)


    def maingui(self):
        """
        Design the main title screen.
        """
        self.main.geometry("600x400")
        self.main.title("Pokémon Battle - Title Screen")
        maintitle = Label(self.main, text="Welcome to the Pokemon Battle!", font=("MS Comic Sans", "18"))
        maintitle.pack(ipadx=20, ipady=10, expand=True)
        choice3 = Label(self.main, text="Play a Trainer!", font=("MS Comic Sans", "14"))
        choice3.pack(ipadx=20, ipady=20, expand=True)
        username = Entry(self.main, textvariable=self.name)
        username.pack()
        self.start = Button(self.main, text="Play Bot!", command=self.offgame)
        self.start.pack()
        credit = Label(self.main, text="This program was made by Calvin, Ebaad and Josh", font=("MS Comic Sans", "10"))
        credit.pack(ipadx=20, ipady=20, expand=True)
        quit_button = Button(self.main, text="Quit", command=self.quit_game)
        quit_button.pack()
        self.main.mainloop()


if __name__ == "__main__":
    main = GUI()
    side = threading.Thread(target=main.checker)
    side.start()
    main.maingui()
