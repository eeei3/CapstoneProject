# ---------------------------------------------
# Title: JSON_Poke.py
# Class: CS 30
# Date: 17/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: JSON_Poke.py

This file is what we use to make objects from
"""
# Import module Poke_Obj, which is used later on,
# DO NOT DELETE - Comment out if this breaks your code
from CapstoneProject.Game.Pokemon_Object import Poke_Obj
# from Game.Pokemon_Object import Poke_Obj
# from Pokemon_Object import Poke_Obj


# This class turns the data given from the .json into objects for later usage
class JSON_to_Obj:
    # Initializes default values.
    # Some values assume None, until given data later.
    def __init__(self, rawdata, index, caller):
        self.rawdata = rawdata
        self.name = None
        self.id = None
        self.types = None
        self.moves = None
        self.stats = None
        self.index = index
        self.caller = caller
        self.sprites = None

    # Class reads the moves PP value and returns the value.
    def get_moves(self):
        y = 0
        self.moves = []
        for x in self.rawdata["Moves"]:
            if "N/A" == x["Power"]:
                x["Power"] = 10
            if "N/A" == x["Accuracy"]:
                x["Accuracy"] = 50
            self.moves.append(x)
            self.moves[y]["DefaultPP"] = self.moves[0]["PP"]
            y += 1
        return self.moves

    # Class reads the Pokémon type and returns the value.
    def get_type(self):
        self.types = self.rawdata["Types"]
        return self.types

    def get_sprite(self):
        self.sprites = self.rawdata["Sprite"]
        return self.sprites

    # Class reads the Pokémon name and returns the value.
    def get_name(self):
        self.name = self.rawdata["Name"]
        return self.name

    # Class reads the Pokémon's ID and returns the value.
    def get_id(self):
        self.id = self.rawdata["ID"]
        return self.id

    # Class reads the Pokémon stats and returns the value.
    def get_stats(self):
        self.stats = self.rawdata["Stats"]
        return self.stats

    # Class returns the values that it has received and updates the object.
    def return_obj(self):
        self.name = self.get_name()
        self.id = self.get_id()
        self.types = self.get_type()
        self.moves = self.get_moves()
        self.stats = self.get_stats()
        self.sprites = self.get_sprite()
        pokemon = Poke_Obj.Pokemon(self.name, self.id, self.types, self.moves,
                                   self.stats, self.index, self.caller, self.sprites)
        return pokemon
