import random


class Pokemon:
    def __init__(self, name, id, types, moves, stats, index, owner):
        self.name = name
        self.id = id
        self.types = types
        self.moves = moves
        self.stats = stats
        self.onfield = False
        self.index = index
        self.owner = owner

    def attack(self, attack, condition, opp):
        print(
            f" {self.owner} has used {self.name}'s {self.moves[attack]['Name']}")
        self.moves[attack]["PP"] -= 1
        if random.randint(0, 100) < self.moves[attack]["Acuracy"]:
            print("Attack successful!")
        else:
            print("Missed!")

        return

    def take_damage(self, dmg):
        self.stats["HP"] -= dmg
        return

    def faint(self):
        return

"""
# Read the data from the JSON file
with open("../Data/data.json", "r") as f:
    data = json.load(f)

# Create a list of Pokémon objects from the data
pokemon_list = []

for pokemon_data in data:
    name = pokemon_data['Name']
    id = pokemon_data['ID']
    types = pokemon_data['Types']
    moves = pokemon_data['Moves']
    pokemon = Pokemon(name, id, types, moves)
    pokemon_list.append(pokemon)

# Example usage:
for pokemon in pokemon_list:
    print(pokemon.name, pokemon.id, pokemon.types)"""
