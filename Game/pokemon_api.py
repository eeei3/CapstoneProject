# ---------------------------------------------
# Title: pokemon_api.py
# Class: CS 30
# Date: 13/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: pokemon_api.py

This file makes api calls to pokeapi.co.
It then stores the data received in a .json file for later use.
It also uses classes as per OOP formats.

DO NOT USE THIS FILE.
USE BATTLE.PY
"""
# Important package imports
import requests


class PokemonAPI:
    def __init__(self):
        """
        Initialize an empty list for collecting data
        """
        self.pokemon_data = []

    def call_api(self, pokemon_id):
        """
        Calling the API, storing response and printing any error status
        code
        """
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.pokemon_data.append(data)
        else:
            print(f"Error: {response.status_code}")

    def get_pokemon_data(self):
        """
        Returning the data collected after using the API
        """
        return self.pokemon_data


class Pokemon(PokemonAPI):
    def __init__(self, data):
        """
        Initializes certain values that API return.
        Only strips the information that we actually need to avoid
        garbage calls
        """
        super().__init__()
        self.name = data['name']
        self.id = data['id']
        self.stats = {stat_data['stat']['name']: stat_data['base_stat']
                      for stat_data in data['stats']}
        self.types = [types_data['type']['name']
                      for types_data in data['types']]
        self.sprites = data['sprites']['front_default']
        self.moves = []
        for move_data in data['moves'][:4]:
            move_name = move_data['move']['name']
            move_response = requests.get(move_data['move']['url']).\
                json()
            move_pp = move_response['pp']
            move_accuracy = move_response['accuracy'] or "N/A"
            move_power = move_response['power'] or "N/A"
            move_type = move_response['type']['name']
            self.moves.append({"Name": move_name, "PP": move_pp,
                               "Accuracy": move_accuracy, "Power":
                                   move_power,
                               "Type": move_type})

    def add_to_dict(self):
        """
        Returning the data that we have collected, striped and stored.
        """
        return {
            "ID": self.id,
            "Name": self.name,
            "Sprite": self.sprites,
            "Types": self.types,
            "Stats": self.stats,
            "Moves": self.moves
        }
