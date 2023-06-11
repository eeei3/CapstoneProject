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
# Important package imports
from tkinter import *
import threading
import battle
import time
import gc


# Represents the graphical user interface of the game.
class GUI:
    def __init__(self):
        """
        Initialize the GUI object.
        """
        # Object for the main window
        self.main = Tk()
        # Object for the main game
        self.game = None
        # Object for the start game
        self.start = None
        # Object for additional thread
        self.process1 = None
        # Variable for player username
        self.name = StringVar(self.main)
        self.name.set("Pick your username")

    def begin_offline(self):
        """
        Starts an offline game with a bot.
        """
        self.process1 = threading.Thread(target=self.offline_wrapper())
        self.process1.start()

    def offline_wrapper(self):
        """
        Wraps the function for starting an offline game with a bot.
        """
        runtime = 0
        level = 1
        gamestatus = 3
        self.main.withdraw()
        self.game = battle.Battle(level, self.name.get(), runtime)
        while gamestatus != 2:
            gamestatus = self.game.begin_game()
            if gamestatus == 0:
                runtime += 1
                level += 1
                gc.collect()
                self.game = battle.Battle(level, self.name.get(),
                                          runtime)
            elif gamestatus == 1:
                runtime += 1
                level = 1
                gc.collect()
                # time.sleep(3)
                self.game = battle.Battle(level, self.name.get(),
                                          runtime)
            else:
                continue
        self.quit_game()
    def quit_game(self):
        """
        Quits the game and closes the GUI.
        """
        self.main.destroy()
        self.main.quit()
        quit()

    def name_checker(self):
        """
        Checking if the player's username is valid
        """
        while True:
            try:
                while self.name.get() == "Pick your username" \
                        or self.name.get() == "":
                    self.start.config(state="disabled")
                self.start.config(state="normal")
                time.sleep(1)
            except RuntimeError:
                pass

    def title_gui(self):
        """
        The main title screen.
        """
        self.main.geometry("600x400")
        self.main.title("Pokémon Battle - Title Screen")
        maintitle = Label(self.main, text="Welcome to the "
                                          "Pokemon Battle!",
                          font=("MS Comic Sans", "18"))
        maintitle.pack(ipadx=20, ipady=10, expand=True)
        choice3 = Label(self.main, text="Play a Trainer!",
                        font=("MS Comic Sans", "14"))
        choice3.pack(ipadx=20, ipady=20, expand=True)
        username = Entry(self.main, textvariable=self.name)
        username.pack()
        self.start = Button(self.main, text="Play Bot!", command=
        self.begin_offline)
        self.start.pack()
        credit = Label(self.main,
                       text="This program was made by Calvin, Ebaad "
                            "and Josh",
                       font=("MS Comic Sans", "10"))
        credit.pack(ipadx=20, ipady=20, expand=True)
        quit_button = Button(self.main, text="Quit", command=self.
                             quit_game)
        quit_button.pack()
        self.main.mainloop()


if __name__ == "__main__":
    main = GUI()
    side = threading.Thread(target=main.name_checker)
    side.start()
    main.title_gui()
