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
It prints some data that can be used to verify if the file is working as
intended
"""
# Import package imports
import random


# Class that is being used to make objects from the data
class Pokemon:
    def __init__(self, name, id, types, moves, stats, index, caller, sprites):
        """
        Initialize various values that we need later
        """
        # Pokemon name
        self.name = name
        # Pokemon ID
        self.id = id
        # Pokemon types
        self.types = types
        # Pokemon moves
        self.moves = moves
        # Pokemon stats such as HP
        self.stats = stats
        # Pokemon owner
        self.index = index
        # Pokemon's index in the owners pokemon list
        self.caller = caller
        # Pokemon's sprite
        self.sprites = sprites

    def remove(self):
        """
        Remove the Pokémon from the caller's list
        """
        self.caller.pokemon.pop(self.index)

    def attack(self, att, crit, target, *diff):
        """
        Pokémon attack logic
        """
        # Adjusting hit chance for enemy difficulty
        if len(diff) < 0:
            attack_chance = random.randint(0, 100) * \
                            (int(diff[0] ** 0.8) << 2) / 10
        else:
            attack_chance = random.randint(0, 100)
        # Checking if attack is hit or miss
        if (attack_chance < att["Accuracy"]) and (att["Accuracy"] != 100):
            return 1
        else:
            # Is type effectiveness being used?
            if crit == 1:
                # Effective
                dmg = att["Power"] * 2
            elif crit == 2:
                # Not effective
                dmg = att["Power"] * 0.5
            else:
                # If attack is a critical hit
                if random.randint(0, 2) == random.randint(0, 2):
                    dmg = att["Power"] * 1.5
                else:
                    # Normal attack
                    dmg = att["Power"]
            # Actually inflicting damage
            target.take_dmg(dmg)
            return 0

    def take_dmg(self, amount):
        """
        Reduce the Pokemon's HP by the given amount
        """
        try:
            self.stats["hp"] -= amount
        except:
            pass
        return
