# ---------------------------------------------
# Title: player.py
# Class: CS 30
# Date: 23/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: player.py

This file is used to create a Player object using data from the API.
We also use this file for some of our game logic
"""
# Important package imports
import csv
import os
import random
import data_to_object
import pokemon_api

# Read types.csv file for in-game mechanics
with open(os.path.join(os.getcwd(), "types.csv"), newline='') as \
        csv_file:
    type_list = []
    csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in csv_reader:
        type_list.append(row)


# Represents a Player object in the game.
class Player:
    def __init__(self, name):
        """
        Initialize the Player object.
        """
        # Object for the API
        self.api = pokemon_api.PokemonAPI()
        # Player name
        self.name = name
        # List of player's Pokémon
        self.pokemon = self.get_return_pokemon()
        # The Pokémon that the player has on the field
        self.played_pokemon = self.pokemon[random.randint(0, 5)]

    def get_return_pokemon(self):
        """
        Fetches Pokémon data from the PokeAPI and returns a list of
        Pokémon objects.
        """
        pokemon_list = []
        for _ in range(6):
            pokemon_id = random.randint(1, 1010)
            self.api.call_api(pokemon_id)

        pokemon_raw = self.api.get_pokemon_data()
        pokemon_data = [pokemon_api.Pokemon(data).add_to_dict() for data
                        in pokemon_raw]
        index = 0
        for x in pokemon_data:
            y = data_to_object.DataToObj(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon_list.append(poke)
            index += 1
        return pokemon_list

    def switch_pokemon(self, index):
        """
        Switches the currently played Pokémon.
        """
        self.played_pokemon.onfield = False
        self.played_pokemon = self.pokemon[index]
        self.played_pokemon.onfield = True

    def turn(self, epokemon, attack):
        """
        Player is performing their move
        """
        attchoice = None
        for att in self.played_pokemon.moves:
            if att["Name"] == attack:
                attchoice = att
                break
        if attchoice is None:
            return 9
        for row in type_list:
            for atype in epokemon.types:
                if (atype.title() in row[0]) and (
                        (atype.title() in attchoice["Type"].title()) or
                        (attchoice["Type"].title()) in atype.title()):
                    if 0.5 in row:
                        att = self.played_pokemon(attchoice, 2,
                                                  epokemon)
                        if att == 0:
                            return 5
                        else:
                            return 9
                    else:
                        att = self.played_pokemon.attack(attchoice, 1,
                                                         epokemon)
                        if att == 0:
                            return 6
                        else:
                            return 9
        att = self.played_pokemon.attack(attchoice, 0, epokemon)
        if att == 0:
            return
        else:
            return 9

    def hp_check(self):
        """
        Checks the HP of the currently played Pokémon.
        """
        if self.played_pokemon.stats["hp"] <= 0:
            self.played_pokemon.onfield = None
            self.played_pokemon.remove()
            for i, pokemon in enumerate(self.pokemon):
                pokemon.index = i
            return 0
        return 1
