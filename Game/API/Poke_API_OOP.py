import requests
import random


class PokemonAPI:
    def __init__(self):
        self.pokemon_data = []

    def call_api(self, pokemon_id):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.pokemon_data.append(data)
        else:
            print(f"Error: {response.status_code}")

    def get_pokemon_data(self):
        return self.pokemon_data


class Pokemon:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.types = [types_data['type']['name'] for types_data in data['types']]
        self.moves = [move_data['move']['name'] for move_data in data['moves'][:4]]

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print("Types:")
        for type_name in self.types:
            print(f" - {type_name}")
        print("Moves:")
        for move_name in self.moves:
            print(f" - {move_name}")

    def to_dict(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Types": self.types,
            "Moves": self.moves
        }


if __name__ == '__main__':
    api = PokemonAPI()

    for i in range(12):
        pokemon_id = random.randint(1, 1010)
        api.call_api(pokemon_id)

    pokemon_data = api.get_pokemon_data()

    for data in pokemon_data:
        pokemon = Pokemon(data)
        pokemon.print_info()

    with open("../Data/data.json", "w") as f:
        for data in pokemon_data:
            pokemon = Pokemon(data)
            pokemon_dict = pokemon.to_dict()

            for key, value in pokemon_dict.items():
                f.write(f'"{key}": {value}\n')
