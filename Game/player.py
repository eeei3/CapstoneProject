# ---------------------------------------------
# Title: player.py
# Class: CS 30
# Date: 23/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: player.py


"""
import random
from API import Poke_API_OOP
from Pokemon_Object import JSON_Poke
from tkinter import *
import csv

with open("Data/types.csv", newline='') as c:
    EBAAD = csv.reader(c, delimiter=' ', quotechar='|')


class Player:

    def __init__(self, name):
        self.api = Poke_API_OOP.PokemonAPI()
        self.name = name
        self.pokemon = self.pokeget()
        self.played_pokemon = None

    def pokeget(self):
        pokemon_list = []  # Empty list
        for i in range(12):
            pokemon_id = random.randint(1, 1010)  # random selection between ID 1 and ID 1010
            self.api.call_api(pokemon_id)  # call the pokemon based on the ID randomly selected

        pokemon_raw = self.api.get_pokemon_data()

        pokemon_data = [Poke_API_OOP.Pokemon(data).to_dict() for data in pokemon_raw]
        index = 0
        for x in pokemon_data:
            index += 1
            y = JSON_Poke.JSONtoPoke(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon_list.append(poke)
        return pokemon_list


    def UI(self, pokemon_list):
        root = Tk()
        root.geometry("500x400")
        root.title("Player Setup")

        # List of pokemon after pulling from API
        # pokemon_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        team = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

        # setup the pick variables
        pick = tkinter.StringVar(root)
        pick.set("Pick your first pokemon.")
        # Add dropdown menu to the GUI

        pokemon_dropdown = tkinter.OptionMenu(root, pick, *pokemon_list['Name'])
        pokemon_dropdown.pack()
        count = 0

        # this button will add the pokemon to the team
        def add_pokemon():
            global count
            dropdown = pick.get()
            index = pokemon_list['Name'].index(dropdown)
            pokemon_dropdown['menu'].delete(index)
            team[count] = pick
            count = 1 + count

        add = Button(root, text="Add Pokemon", command=add_pokemon)
        add.pack()

        # This will cause the program to run until we close it with the X\
        root.mainloop()"""

    def turn(self, epokemon):
        print("Trainer's turn!")
        trainer_choice = random.randint(0, 100)
        pokemon_choice = random.randint(0, len(self.pokemon) - 1)
        if trainer_choice <= 80:
            # Attack
            if random.randint(0, 12) > self.difficulty:
                for attack in self.played_pokemon.moves:
                    if attack["Power"] == "N/A":
                        pass
                    else:
                        if epokemon.stats["hp"] < attack["Power"]:
                            self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 0)
                        else:
                            for row in EBAAD:
                                for type in epokemon.types:
                                    if (type in row) and (type in attack["Type"]):
                                        self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 1)
                self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 0)
            else:
                self.played_pokemon.attack(random.randint(0, len(self.played_pokemon.moves)), 0)
        else:
            # Switch Pokémon
            self.played_pokemon.onfield = False
            self.played_pokemon = self.pokemon[pokemon_choice]
            print(f"Trainer has chosen {self.played_pokemon.name}")
            self.played_pokemon.onfield = True
            return

# when it starts, the player throws their first pokémon in the list
# print a list of options
# if the player chooses to attack, open a menu of different moves
# if the player chooses to switch, open a list of pokémon
# if the player chooses the bag, open a list of items the player can use
