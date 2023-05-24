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
import json


# Class that is being used to make objects from the data
class Pokemon:
    def __init__(self, name, id, types, moves, stats, index, caller):
        self.name = name
        self.id = id
        self.types = types
        self.moves = moves
        self.stats = stats
        self.index = index
        self.caller = caller


"""
# Read the data from the JSON file
with open("../Data/data.json", "r") as f:
    data = json.load(f)

# Create a list of Pokémon objects from the data
pokemon_list = []

for pokemon_data in data:
    name = pokemon_data['Name']
    id = pokemon_data['ID']
    types = pokemon_data['Types']
    moves = pokemon_data['Moves']
    pokemon = Pokemon(name, id, types, moves)
    pokemon_list.append(pokemon)

# Example usage:
for pokemon in pokemon_list:
    print(pokemon.name, pokemon.id, pokemon.types, pokemon.moves)
"""
