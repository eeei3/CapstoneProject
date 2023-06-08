# ---------------------------------------------
# Title: Poke_API_OOP.py
# Class: CS 30
# Date: 13/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: Poke_API_OOP.py

This file makes api calls to pokeapi.co.
It then stores the data received in a .json file for later use.
It also uses classes as per OOP formats.

DO NOT USE THIS FILE.
USE BATTLE.PY
"""
# Important package imports
import json
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

    def to_dict(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Sprite": self.sprites,
            "Types": self.types,
            "Stats": self.stats,
            "Moves": self.moves
        }


class Main(PokemonAPI):
    def __init__(self):
        super().__init__()
        for i in range(12):
            pokemon_id = random.randint(1, 1010)
            self.call_api(pokemon_id)

        pokemon_data = self.get_pokemon_data()

        for data in pokemon_data:
            pokemon = Pokemon(data)

        with open("Data/data.json", "w+") as f:
            pokemon_list = [Pokemon(data).to_dict() for data in pokemon_data]
            json.dump(pokemon_list, f, indent=4)

Main()
