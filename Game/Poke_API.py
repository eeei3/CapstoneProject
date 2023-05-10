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
    # print(f"Height: {data['height']}")
    # print(f"Weight: {data['weight']}")
    # print("Abilities:")
    # for ability in data['abilities']:
    # print(f" - {ability['ability']['name']}")
