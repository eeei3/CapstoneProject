# ---------------------------------------------
# Title: enemies.py
# Class: CS 30
# Date: 15/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: enemies.py

This file contains the Trainer class and related functions.
"""
import random
import csv
from API import Poke_API_OOP
from Pokemon_Object import JSON_Poke

# List of all enemy trainers
names = ["Ebaad", "Blue", "Red", "Trace", "Lance", "Leon", "Cynthia", "Alder", "Iris", "Elio", "Ash"]

# Opening and reading data from types.cvs
with open("Data/types.csv", newline='') as c:
    EBAAD = []
    a = csv.reader(c, delimiter=' ', quotechar='|')
    for row in a:
        EBAAD.append(row)


# Trainer object used in game
class Trainer:
    def __init__(self, difficulty, turn):
        """
        Initialize the Trainer object.
        """
        self.api = Poke_API_OOP.PokemonAPI()
        self.name = names[random.randint(0, 10)]
        self.pokemon = self.pokeget()
        self.difficulty = difficulty
        self.played_pokemon = self.pokemon[random.randint(0, 5)]
        self.gturn = turn

    def start(self):
        """
        Marks the trainer's Pokémon as on the field.
        """
        self.played_pokemon.onfield = True

    def pokeget(self):
        """
        Retrieves a list of randomly generated Pokémon.
        """
        pokemon = []
        for i in range(6):
            pokemon_id = random.randint(1, 1010)
            self.api.call_api(pokemon_id)

        pokemon_raw = self.api.get_pokemon_data()

        pokemon_data = [Poke_API_OOP.Pokemon(data).to_dict() for data in pokemon_raw]
        index = 0
        for x in pokemon_data:
            y = JSON_Poke.JSON_to_Obj(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon.append(poke)
            index += 1
        print(len(pokemon_data))
        print(len(pokemon))
        return pokemon

    def turn(self, epokemon):
        """
        Perform the trainer's turn.
        """
        print("Trainer's turn!")
        trainer_choice = random.randint(0, 100)
        attlen = 0

        if self.played_pokemon.stats["hp"] <= 0:
            trainer_choice = 90

        if trainer_choice <= 80:
            print("Trainer is going to attack")
            # This is our logic for attackiself.hp2.set(str(self.p2.played_pokemon.stats["hp"]))ng as a trainer
            if random.randint(0, 12) > self.difficulty:
                for attack in self.played_pokemon.moves:
                    attlen += 1
                    if attack["Power"] == "N/A":
                        pass
                    else:
                        if epokemon.stats["hp"] < attack["Power"]:
                            print(f"Trainer has used {attack['Name']}")
                            print(epokemon.name)
                            self.played_pokemon.attack(attack, 0, epokemon)
                            self.gturn = 1
                            print(self.played_pokemon.name)
                            print("F\n\n")
                            print(attack["Name"])
                            print("\n\nF")
                            return [1, attack["Name"]]

                        else:
                            for row in EBAAD:
                                for type in epokemon.types:
                                    if (type in row) and (type in attack["Type"]):
                                        print(f"Trainer has used {attack['Name']}")
                                        if 0.5 in row:
                                            print(epokemon.name)
                                            self.played_pokemon.attack(attack, 2, epokemon)
                                            # self.gturn = 1
                                            print(self.played_pokemon.name)
                                            print("T\n\n")
                                            print(attack["Name"])
                                            print("\n\nT")
                                            return [1, attack["Name"]]
                                        else:
                                            print(epokemon.name)
                                            self.played_pokemon.attack(attack, 1, epokemon)
                                            # self.gturn = 1
                                            print(self.played_pokemon.name)
                                            print("G\n\n")
                                            print(attack["Name"])
                                            print("\n\nG")
                                            return [1, attack["Name"]]

                        if len(self.played_pokemon.moves) == attlen:
                            print(epokemon.name)
                            self.played_pokemon.attack(attack, 0, epokemon)
                            # self.gturn = 1
                            print(self.played_pokemon.name)
                            print("Z\n\n")
                            print(attack["Name"])
                            print("\n\nZ")
                            return [1, attack["Name"]]
            else:
                length = len(self.played_pokemon.moves)
                choice = self.played_pokemon.moves[random.randint(0, length - 1)]
                self.played_pokemon.attack(choice, 0, epokemon)
                return [1, choice["Name"]]
        else:
            print("Trainer is gonna switch")
            # This is the logic for switching the trainers onfield Pokémon
            pokemon_choice = random.randint(0, len(self.pokemon) - 1)
            self.played_pokemon = self.pokemon[pokemon_choice]
            print(f"Trainer has chosen {self.played_pokemon.name}")
            print("H\n\n")
            print(self.played_pokemon)
            print("\n\nH")
            return [2, self.played_pokemon.name]

    def check(self):
        """
        Check if the onfield Pokémon has fainted.
        """
        if self.played_pokemon.stats["hp"] <= 0:
            self.played_pokemon.onfield = None
            self.played_pokemon.remove()
            for i, pokemon in enumerate(self.pokemon):
                print(f"cur_index {pokemon.index}")
                pokemon.index = i
                print(i)
            return 0
        else:
            return 1
