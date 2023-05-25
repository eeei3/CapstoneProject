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
# Import module Poke_Obj, which is used later on
from Game.Pokemon_Object import Poke_Obj


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

    # Class reads the moves PP value and returns the value.
    def get_moves(self):
        y = 0
        self.moves = []
        for x in self.rawdata["Moves"]:
            self.moves.append(x)
            self.moves[y]["DefaultPP"] = self.moves[0]["PP"]
            y += 1
        return self.moves

    # Class reads the Pokémons type and returns the value.
    def get_type(self):
        self.types = self.rawdata["Types"]
        return self.types

    # Class reads the Pokémons name and returns the value.
    def get_name(self):
        self.name = self.rawdata["Name"]
        return self.name

    # Class reads the Pokémons' ID and returns the value.
    def get_id(self):
        self.id = self.rawdata["ID"]
        return self.id

    # Class reads the Pokémons stats and returns the value.
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
        pokemon = Poke_Obj.Pokemon(self.name, self.id, self.types, self.moves, self.stats, self.index, self.caller)
        return pokemon
