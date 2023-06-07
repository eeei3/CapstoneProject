# ---------------------------------------------
# Title: Poke_Obj.py
# Class: CS 30
# Date: 13/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: Poke_Obj.py

This file is used to make objects from our stored data in our .json file.
It opens the .json file in read mode, creates a list of objects from the data.
It prints some data that can be used to verify if the file is working as intended
"""
# Import package imports
import random


# Class that is being used to make objects from the data
class Pokemon:
    def __init__(self, name, id, types, moves, stats, index, caller, sprites):
        self.name = name
        self.id = id
        self.types = types
        self.moves = moves
        self.stats = stats
        self.index = index
        self.caller = caller
        self.sprites = sprites

    def remove(self):
        self.caller.pokemon.pop(self.index)

    def attack(self, att, crit, target):
        if (random.randint(0, 100) < att["Accuracy"]) and (att["Accuracy"] != 100):
            return
        else:
            if crit == 1:
                dmg = att["Power"] * 2
            elif crit == 2:
                dmg = att["Power"] * 0.5
            else:
                dmg = att["Power"]
            target.take_dmg(dmg)
        return

    def take_dmg(self, amount):
        try:
            self.stats["hp"] -= amount
        except:
            pass
        return
