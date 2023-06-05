# ---------------------------------------------
# Title: player.py
# Class: CS 30
# Date: 23/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: player.py

This file is used to create a Player object using data from the API
We also use this file for some of our game logic
"""
import random
import csv
from API import Poke_API_OOP
from Pokemon_Object import JSON_Poke

# Read types.csv file for in-game mechanics
with open("Data/types.csv", newline='') as csv_file:
    EBAAD = []
    csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in csv_reader:
        EBAAD.append(row)


# Represents a Player object in the game.
class Player:
    def __init__(self, name):
        """
        Initialize the Player object.
        """
        self.api = Poke_API_OOP.PokemonAPI()
        self.name = name
        self.pokemon = self.pokeget()
        self.played_pokemon = self.pokemon[random.randint(0, 5)]

    def pokeget(self):
        """
        Fetches Pokémon data from the PokeAPI and returns a list of Pokémon objects.
        """
        pokemon_list = []
        for _ in range(6):
            pokemon_id = random.randint(1, 1010)
            self.api.call_api(pokemon_id)

        pokemon_raw = self.api.get_pokemon_data()
        pokemon_data = [Poke_API_OOP.Pokemon(data).to_dict() for data in pokemon_raw]
        index = 0
        for x in pokemon_data:
            index += 1
            y = JSON_Poke.JSON_to_Obj(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon_list.append(poke)
        return pokemon_list

    def switch_pokemon(self, index):
        """
        Switches the currently played Pokémon.
        """
        self.played_pokemon.onfield = False
        self.played_pokemon = self.pokemon[index - 1]
        self.played_pokemon.onfield = True

    def turn(self, epokemon, attack):
        """
        Performs a turn in the game.
        """
        attchoice = None
        for att in self.played_pokemon.moves:
            if att["Name"] == attack:
                attchoice = att
                break
        if attchoice is None:
            print("You messed up")
            return 9
        for row in EBAAD:
            for type in epokemon.types:
                if (type in row) and (type in attchoice["Type"]):
                    print(attchoice)
                    if 0.5 in row:
                        self.played_pokemon(attchoice, 2, epokemon)
                    else:
                        self.played_pokemon.attack(attchoice, 1, epokemon)
                    return
        print(attchoice)
        self.played_pokemon.attack(attchoice, 0, epokemon)

    def check(self):
        """
        Checks the HP of the currently played Pokémon.
        """
        if self.played_pokemon.stats["hp"] <= 0:
            self.played_pokemon.onfield = False
            self.played_pokemon.remove()
            return 0
        return 1
