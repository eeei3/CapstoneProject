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
# Important package imports
import random
import csv
import pokemon_api
import data_to_object
import os

# List of all enemy trainers
names = ["Ebaad", "Blue", "Red", "Trace", "Lance", "Leon", "Cynthia",
         "Alder", "Iris", "Elio", "Ash"]

# Opening and reading data from types.cvs
with open(os.path.join(os.getcwd(), "types.csv"), newline='') as c:
    type_list = []
    a = csv.reader(c, delimiter=' ', quotechar='|')
    for row in a:
        type_list.append(row)


# Trainer object used in game
class Trainer:
    def __init__(self, difficulty):
        """
        Initialize the Trainer object.
        """
        # Object for the API
        self.api = pokemon_api.PokemonAPI()
        # Picking trainer name
        self.name = names[random.randint(0, 10)]
        # Getting a list of Pokémon
        self.pokemon = self.get_return_pokemon()
        # Difficulty of trainer
        self.difficulty = difficulty
        # Pokémon that the trainer has played
        self.played_pokemon = self.pokemon[random.randint(0, 5)]

    def mark_field(self):
        """
        Marks the trainer's Pokémon as on the field.
        """
        self.played_pokemon.onfield = True

    def get_return_pokemon(self):
        """
        Retrieves a list of randomly generated Pokémon.
        """
        pokemon = []
        for i in range(6):
            pokemon_id = random.randint(1, 1010)
            self.api.call_api(pokemon_id)

        pokemon_raw = self.api.get_pokemon_data()

        pokemon_data = [pokemon_api.Pokemon(data).add_to_dict() for data in
                        pokemon_raw]
        index = 0
        for x in pokemon_data:
            y = data_to_object.data_to_obj(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon.append(poke)
            index += 1
        return pokemon

    def turn(self, epokemon):
        """
        Perform the trainer's turn.
        """
        trainer_choice = random.randint(0, 100)
        attlen = 0

        if self.played_pokemon.stats["hp"] <= 0:
            trainer_choice = 90

        if trainer_choice <= 80:
            # This is our logic for attacking as a trainer
            if random.randint(0, 12) > self.difficulty:
                for attack in self.played_pokemon.moves:
                    attlen += 1
                    if attack["Power"] == "N/A":
                        pass
                    else:
                        if epokemon.stats["hp"] < attack["Power"]:
                            att = self.played_pokemon.attack(
                                attack, 0, epokemon, self.difficulty)
                            if att == 0:
                                return [1, attack["Name"]]
                            else:
                                return [9, attack["Name"]]

                        else:
                            for row in type_list:
                                for atype in epokemon.types:
                                    if (atype.title() in row[0]) and (
                                            (atype.title() in
                                             attack["Type"].title()) or (
                                            attack["Type"].title()) in
                                            atype.title()):
                                        if 0.5 in row:
                                            att = self.played_pokemon.attack(
                                                attack, 2, epokemon,
                                                self.difficulty)
                                            if att == 0:
                                                return [5, attack["Name"]]
                                            else:
                                                return [9, attack["Name"]]
                                        else:
                                            att = self.played_pokemon.attack(
                                                attack, 1, epokemon,
                                                self.difficulty)
                                            if att == 0:
                                                return [6, attack["Name"]]
                                            else:
                                                return [9, attack["Name"]]

                        if len(self.played_pokemon.moves) == attlen:
                            maxim = len(self.played_pokemon.moves) - 1
                            attchoice = self.played_pokemon.moves[
                                random.randint(0, maxim)]
                            att = self.played_pokemon.attack(
                                attchoice, 0, epokemon, self.difficulty)
                            if att == 0:
                                return [1, attack["Name"]]
                            else:
                                return [9, attack["Name"]]
            else:
                length = len(self.played_pokemon.moves)
                attack = self.played_pokemon.moves[
                    random.randint(0, length - 1)]
                for row in type_list:
                    for atype in epokemon.types:
                        if (atype.title() in row[0]) and (
                                (atype.title() in attack["Type"].title()) or (
                                attack["Type"].title()) in atype.title()):
                            if 0.5 in row:
                                att = self.played_pokemon.attack(
                                    attack, 2, epokemon, self.difficulty)
                                if att == 0:
                                    return [5, attack["Name"]]
                                else:
                                    return [9, attack["Name"]]
                            else:
                                att = self.played_pokemon.attack(
                                    attack, 1, epokemon, self.difficulty)
                                if att == 0:
                                    return [6, attack["Name"]]
                                else:
                                    return [9, attack["Name"]]
                att = self.played_pokemon.attack(
                    attack, 0, epokemon, self.difficulty)
                if att == 0:
                    return [1, attack["Name"]]
                else:
                    return [9, attack["Name"]]
        else:
            if len(self.pokemon) == 0:
                return [8, None]
            # This is the logic for switching the trainers onfield Pokémon
            pokemon_choice = random.randint(0, len(self.pokemon) - 1)
            self.played_pokemon = self.pokemon[pokemon_choice]
            return [2, self.played_pokemon.name]

    def hp_check(self):
        """
        Check if the onfield Pokémon has fainted.
        """
        if self.played_pokemon.stats["hp"] <= 0:
            self.played_pokemon.onfield = None
            self.played_pokemon.remove()
            for i, pokemon in enumerate(self.pokemon):
                pokemon.index = i
            return 0
        else:
            return 1
