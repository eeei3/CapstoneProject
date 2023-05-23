import json


class Pokemon:
    def __init__(self, name, id, types, moves):
        self.name = name
        self.id = id
        self.types = types
        self.moves = moves


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