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
# Important import statements
import random
from API import Poke_API_OOP
from Pokemon_Object import JSON_Poke
import csv

# Here we open and read the types.csv file which we use for in-game mechanics
with open("Data/types.csv", newline='') as c:
    EBAAD = []
    a = csv.reader(c, delimiter=' ', quotechar='|')
    for row in a:
        EBAAD.append(row)


# Our main Player class is declared here
class Player:

    # Initializing attributes
    def __init__(self, name):
        self.api = Poke_API_OOP.PokemonAPI()
        self.name = name
        self.pokemon = self.pokeget()
        self.played_pokemon = self.pokemon[random.randint(0, 5)]

    # Here we have an empty list that we populate with data from the PokeAPI
    def pokeget(self):
        pokemon_list = []  # Empty list
        for i in range(6):
            pokemon_id = random.randint(1, 1010)  # random selection between ID 1 and ID 1010
            self.api.call_api(pokemon_id)  # call the pokemon based on the ID randomly selected

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

    # Checks to see if Pokémon is currently on the field or not
    def switch_pokemon(self, index):
        self.played_pokemon.onfield = False
        self.played_pokemon = self.pokemon[index]
        self.played_pokemon.onfield = True

    def turn(self, epokemon, attack):
        attchoice = None
        for att in self.played_pokemon.moves:
            if att["Name"] == attack:
                attchoice = att
                break
        if attchoice == None:
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

    # Checks HP of Pokémon on the field to see if fainted or not
    def check(self):
        if self.played_pokemon.stats["hp"] <= 0:
            self.played_pokemon.onfield = None
            return 0
        return 1
# when it starts, the player throws their first pokémon in the list
# print a list of options
# if the player chooses to attack, open a menu of different moves
# if the player chooses to switch, open a list of pokémon
# if the player chooses the bag, open a list of items the player can use
