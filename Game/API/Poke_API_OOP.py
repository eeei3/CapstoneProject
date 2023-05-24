# Important package imports
import json
import requests
import random


# This is the Pokémon API class, which handles calls and returns from the API
class PokemonAPI:
    # Initializing an array so that it can take data when needed.
    def __init__(self):
        self.pokemon_data = []

    # Calling on the PokeAPI and returning data and any error codes
    def call_api(self, pokemon_id):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.pokemon_data.append(data)
        else:
            print(f"Error: {response.status_code}")

    # Returns whatever data pokemon_data has so that it can be used later
    def get_pokemon_data(self):
        return self.pokemon_data


# This class deals with creating new objects with data retrieved from the API
class Pokemon:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.stats = {stat_data['stat']['name']: stat_data['base_stat'] for stat_data in data['stats']}
        self.types = [types_data['type']['name'] for types_data in data['types']]
        self.sprites = data['sprites']['front_default']
        self.moves = []
        for move_data in data['moves'][:4]:
            move_name = move_data['move']['name']
            move_response = requests.get(move_data['move']['url']).json()
            move_pp = move_response['pp']
            move_accuracy = move_response['accuracy'] or "N/A"
            move_power = move_response['power'] or "N/A"
            move_type = move_response['type']['name']
            self.moves.append({"Name": move_name, "PP": move_pp, "Accuracy": move_accuracy,
                               "Power": move_power, "Type": move_type})

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Sprite: {self.sprites}")
        print("Stats:")
        for stat_name, stat_value in self.stats.items():
            print(f" - {stat_name}: {stat_value}")
        print("Types:")
        for type_name in self.types:
            print(f" - {type_name}")
        print("Moves:")
        for move in self.moves:
            print(f" - {move['Name']} (PP: {move['PP']}, Accuracy: {move['Accuracy']},"
                  f" Power: {move['Power']}, Type: {move['Type']})")

    # We use this to return some data in certain forms, used when printing to file
    def to_dict(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Sprite": self.sprites,
            "Types": self.types,
            "Stats": self.stats,
            "Moves": self.moves
        }


# Main file loop (for testing)
"""class Main:
    api = PokemonAPI()

    # Makes 12 API calls with a random number from 1 to 1010
    for i in range(12):
        pokemon_id = random.randint(1, 1010)
        api.call_api(pokemon_id)

    pokemon_data = api.get_pokemon_data()

    for data in pokemon_data:
        pokemon = Pokemon(data)
        pokemon.print_info()

    # This part is what we use to print the data to our file.
    # We use json.dump so that our file would print into a dictionary
    with open("./Data/data.json", "w+") as f:
        pokemon_list = [Pokemon(data).to_dict() for data in pokemon_data]
        json.dump(pokemon_list, f, indent=4)"""


# main()
