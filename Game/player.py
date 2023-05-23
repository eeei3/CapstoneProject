import random
from API import Poke_API_OOP
from Pokemon_Object import JSON_Poke
import csv

class Player:

    def __init__(self, name):
        self.api = Poke_API_OOP.PokemonAPI()
        self.name = name
        self.pokemon = self.pokeget()
        self.played_pokemon = None

    def pokeget(self):
        pokemon = []
        for i in range(12):
            pokemon_id = random.randint(1, 1010)
            self.api.call_api(pokemon_id)

        pokemon_raw = self.api.get_pokemon_data()

        pokemon_data = [Poke_API_OOP.Pokemon(data).to_dict() for data in pokemon_raw]
        index = 0
        for x in pokemon_data:
            index += 1
            y = JSON_Poke.JSONtoPoke(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon.append(poke)
        return pokemon

    def turn(self, epokemon):
