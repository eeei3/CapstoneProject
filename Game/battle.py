# ---------------------------------------------
# Title: battle.py
# Class: CS 30
# Date: 19/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: battle.py


"""
# Important package imports
import enemies
from tkinter import *


class LBattle:
    def __init__(self):
        self.lvl = 1
        """self.p1 = None
        self.p2 = enemies.Trainer(self.lvl)"""
        self.root = Tk()

    """def start_battle(self):
        self.p1.turn(self.p2.played_pokemon)
        self.p2.turn(self.p1.played_pokemon)"""

    def gamewin(self):
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")
        fight = Button(self.root, text="fight")
        team = Button(self.root, text="team")
        bag = Button(self.root, text="bag")
        run = Button(self.root, text="run")
        fight.pack(side=RIGHT)
        team.pack(side=LEFT)
        bag.pack(side=BOTTOM)
        run.pack(side=BOTTOM)
        self.root.mainloop()


class NBattle(LBattle):
    def __init__(self, stream):
        super().__init__()
        self.p1 = None
        self.p2 = None
        self.stream = stream
        return

a = LBattle()
a.gamewin()