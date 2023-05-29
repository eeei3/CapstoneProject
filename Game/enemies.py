# ---------------------------------------------
# Title: enemies.py
# Class: CS 30
# Date: 15/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: enemies.py


"""
import random
from API import Poke_API_OOP
from Pokemon_Object import JSON_Poke
import csv

names = ["Ebaad", "Blue", "Red", "Trace", "Lance", "Leon", "Cynthia", "Alder", "Iris", "Elio", "Ash"]

with open("Data/types.csv", newline='') as c:
    EBAAD = []
    a = csv.reader(c, delimiter=' ', quotechar='|')
    for row in a:
        EBAAD.append(row)



class Trainer:
    def __init__(self, difficulty):
        self.api = Poke_API_OOP.PokemonAPI()
        self.name = names[random.randint(0, 10)]
        self.pokemon = self.pokeget()
        self.difficulty = difficulty
        self.played_pokemon = None

    def start(self):
        self.played_pokemon = self.pokemon[random.randint(0, 11)]
        print(f"Trainer has chosen {self.played_pokemon.name}")
        self.played_pokemon.onfield = True

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
            y = JSON_Poke.JSON_to_Obj(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon.append(poke)
        return pokemon

    def turn(self, epokemon):
        print("Trainer's turn!")
        trainer_choice = random.randint(0, 100)
        pokemon_choice = random.randint(0, len(self.pokemon) - 1)
        if self.played_pokemon.stats["hp"] <= 0:
            trainer_choice = 90
        if trainer_choice <= 80:
            # Attack
            if random.randint(0, 12) > self.difficulty:
                for attack in self.played_pokemon.moves:
                    if attack["Power"] == "N/A":
                        pass
                    else:
                        if epokemon.stats["hp"] < attack["Power"]:
                            print(f"Trainer has used {attack['Name']}")
                            self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 0, epokemon)
                        else:
                            for row in EBAAD:
                                for type in epokemon.types:
                                    if (type in row) and (type in attack["Type"]):
                                        print(f"Trainer has used {attack['Name']}")
                                        if 0.5 in row:
                                            self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 2, epokemon)
                                        else:
                                            self.played_pokemon.attack(
                                                random.randint(0, len(self.played_pokemon.moves)), 1, epokemon)

                self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 0, epokemon)
            else:
                self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 0, epokemon)
        else:
            # Switch Pokémon
            self.played_pokemon.onfield = False
            self.played_pokemon = self.pokemon[pokemon_choice]
            print(f"Trainer has chosen {self.played_pokemon.name}")
            self.played_pokemon.onfield = True
            return

    def check(self):
        if self.played_pokemon.stats["hp"] <= 0:
            self.played_pokemon.onfield = None
            return 0
        return 1
