import random
from API import Poke_API_OOP

names = ["Ebaad", "Blue", "red", "Trace", "Lance", "Leon", "Cynthia", "Alder", "Iris", "Elio", "Ash"]


class Trainer:
    def __init__(self):
        self.api = Poke_API_OOP.PokemonAPI()
        self.name = names[random.randint(0, 10)]
        self.pokemon = self.pokeget()
        # self.items
        print(self.pokemon)

        return

    def pokeget(self):
        for i in range(12):
            pokemon_id = random.randint(1, 1010)
            self.api.call_api(pokemon_id)

        pokemon_data = self.api.get_pokemon_data()

        pokemon = [Poke_API_OOP.Pokemon(data).to_dict() for data in pokemon_data]
        return pokemon


