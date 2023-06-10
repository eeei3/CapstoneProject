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
# Important package imports
import Poke_Obj


# This class turns the data given from the .json into objects for later usage
class JSON_to_Obj:
    def __init__(self, rawdata, index, caller):
        """
        Initializes default values.
        Some values assume None, until given data later.
        """
        self.rawdata = rawdata
        # Pokemon name
        self.name = None
        # Pokemon ID
        self.id = None
        # Pokemon types
        self.types = None
        # Pokemon moves
        self.moves = None
        # Pokemon stats such as HP
        self.stats = None
        # Pokemon's place in the owner's list
        self.index = index
        # The pokemon's owner
        self.caller = caller
        # The pokemon's sprite
        self.sprites = None

    def get_moves(self):
        """
        Reads the moves PP value and returns the value.
        """
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

    def get_type(self):
        """
        Reads the Pokémon type and returns the value.
        """
        self.types = self.rawdata["Types"]
        return self.types

    def get_sprite(self):
        """
        Reads the Pokémon sprite and returns the value.
        """
        self.sprites = self.rawdata["Sprite"]
        return self.sprites

    def get_name(self):
        """
        Reads the Pokémon name and returns the value.
        """
        self.name = self.rawdata["Name"]
        return self.name

    def get_id(self):
        """
        Reads the Pokémon ID and returns the value.
        """
        self.id = self.rawdata["ID"]
        return self.id

    def get_stats(self):
        """
        Reads the Pokémon stats and returns the value.
        """
        self.stats = self.rawdata["Stats"]
        return self.stats

    def return_obj(self):
        """
        Returns the values that it has received and updates the object.
        """
        self.name = self.get_name()
        self.id = self.get_id()
        self.types = self.get_type()
        self.moves = self.get_moves()
        self.stats = self.get_stats()
        self.sprites = self.get_sprite()
        pokemon = Poke_Obj.Pokemon(self.name, self.id, self.types, self.moves,
                                   self.stats, self.index, self.caller,
                                   self.sprites)
        return pokemon
