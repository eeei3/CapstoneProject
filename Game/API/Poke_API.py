import requests
import random

# Initialize an empty list to store the data
pokemon_data = []

# Repeat the API call 12 times
for i in range(12):
    # Generate a random Pokémon number
    pokemon = random.randint(1, 1010)

    # Construct the URL for the PokeAPI request
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'

    # Send a GET request to the PokeAPI URL
    response = requests.get(url)

    if response.status_code == 200:
        # the request was successful
        data = response.json()
        # Append the data to the list
        pokemon_data.append(data)
    else:
        # handle the error
        print(f"Error: {response.status_code}")

# Print the data for all 12 Pokémon
for data in pokemon_data:
    print(f"Name: {data['name']}")
    print(f"ID: {data['id']}")
    print(f"Types:")
    for types in data['types']:
        print(f" - {types['type']['name']}")
    print("Moves:")
    for move_data in data['moves'][:4]:
        move_name = move_data['move']['name']
        print(f" - {move_name}")

file = open("../Data/data.json", "w")

for data in pokemon_data:
    # Write the ID and name to the file
    file.write(f"\042ID\042: {data['id']}\n")
    file.write(f"\042Name\042: {data['name']}\n")
    file.write("\042Types\042:\n")
    for type_data in data['types']:
        type_name = type_data['type']['name']
        file.write(f" - {type_name}\n")
    file.write("\042Moves\042:\n")
    for move_data in data['moves'][:4]:
        move_name = move_data['move']['name']
        file.write(f" - {move_name}\n")

file.close()
