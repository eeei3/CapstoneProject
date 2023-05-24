import random
from API import Poke_API_OOP
from Pokemon_Object import JSON_Poke
import csv

names = ["Ebaad", "Blue", "Red", "Trace", "Lance", "Leon", "Cynthia", "Alder", "Iris", "Elio", "Ash"]

with open("Data/types.csv", newline='') as c:
    EBAAD = csv.reader(c, delimiter=' ', quotechar='|')


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
            y = JSON_Poke.JSONtoPoke(x, index, self)
            poke = y.return_obj()
            poke.index = index
            pokemon.append(poke)
        return pokemon

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
