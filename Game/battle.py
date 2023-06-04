# ---------------------------------------------
# Title: battle.py
# Class: CS 30
# Date: 19/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: battle.py


"""
# Important package imports
import json
from tkinter import *
import io
from urllib import request
from PIL import Image, ImageTk
import ssl
import enemies
import player
import threading
import time

# Allows for connecting to outside domain
# Bypasses error on macOS
ssl._create_default_https_context = ssl._create_unverified_context


# Main class
class LBattle:
    # Initializing attributes
    def __init__(self):
        self.lvl = 1
        self.root = Toplevel()
        self.pokemon_data = self.load_pokemon_data()
        self.current_pokemon_index = 0
        self.lvl = 1
        self.turn = 1
        self.p1 = player.Player("Larry")
        self.p2 = enemies.Trainer(self.lvl, self.turn)
        self.t = None
        self.pbuttons = []
        self.pcmds = []
        self.move_buttons = []
        self.movecmds = []
        self.hp1 = StringVar()
        self.hp2 = StringVar()
        self.hp1.set(str(self.p1.played_pokemon.stats["hp"]))
        self.hp2.set(str(self.p2.played_pokemon.stats["hp"]))
        self.loading = False
        self.thread = threading.Thread(target=self.start_battle)
        self.thread.daemon = True
        self.thread.start()
        self.game_ui()

    # Loads the Pokémon data from the file
    # Returns the first 6 Pokémon and associated data
    def load_pokemon_data(self):
        with open('Data/data.json') as json_file:
            data = json.load(json_file)
            return data[6:]

    # This is where we request, download and return sprite data
    # The URL we access is given from the API itself, we simply download it
    def load_sprite(self, url):
        response = request.urlopen(url)
        image_data = response.read()
        image_stream = io.BytesIO(image_data)
        sprite = Image.open(image_stream)
        sprite = sprite.resize((150, 150), Image.LANCZOS)
        sprite = ImageTk.PhotoImage(sprite)
        return sprite

    def paction(self, move):
        self.p1.turn(self.p2.played_pokemon, move)
        self.turn = 2
        self.message(f"Player has used {move}\n")
        return

    def switch(self):
        self.turn = 2
        return

    def message(self, msg):
        self.t["state"] = "normal"
        self.t.insert(END, msg)
        self.t["state"] = "disabled"

    # This is the logic and code to starting the battle
    # Currently contains messages for debugging
    # Contains messages displaying changes in onfield Pokémon
    def start_battle(self):
        x = 0
        while x == 0:
            if self.loading == True:
                x = 1
            print(self.loading)
            time.sleep(1)
        print("Game has started properly")
        self.message(f"Start of match with Trainer {self.p2.name}\n")
        self.message(f"Trainer has chosen {self.p2.played_pokemon.name}\n")
        self.p2.start()
        print("More progress!")
        while True:
            print("Here")
            self.message(f"{self.p1.name}'s turn\n")
            self.turn = 1
            self.validate_buttons(3)
            while self.turn == 1:
                pass
            print("Player turn over")
            self.message(f"{self.p2.name}'s turn\n")
            self.invalidate_buttons(3)
            m = self.p2.turn(self.p1.played_pokemon)
            while self.turn == 2:
                pass
            if m[0] == 1:
                self.message(f"{self.p2.played_pokemon.name} has used {m[1]}\n")
            elif m[0] == 2:
                self.message(f"Trainer {self.p2.name} has switched to {self.p2.played_pokemon.name}")
            print(self.turn)

    # This is what we use to update the onfeild sprites if they are changed
    def update_sprite(self):
        sprite_url = self.p1.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.psprite_label.config(image=sprite)
        self.psprite_label.image = sprite
        sprite_url = self.p2.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.esprite_label.config(image=sprite)
        self.esprite_label.image = sprite

    # Gets the current Pokémon data and creates buttons that contains the move's name
    def update_moves(self):
        moves = self.pokemon_data[self.current_pokemon_index]["Moves"]
        for i, move in enumerate(moves):
            self.move_buttons[i].config(text=move["Name"])

    # If player switches, updates index, moves and sprites
    def switch_pokemon(self, index):
        self.current_pokemon_index = index
        self.update_sprite()
        self.update_moves()

    # Used to disable some buttons during the game
    def invalidate_buttons(self, num):
        if num == 1 or num == 3:
            for button in self.pbuttons:
                button["state"] = "disabled"
        elif num == 2 or num == 3:
            for button in self.move_buttons:
                button["state"] = "disabled"

    # Used to enable some buttons during the game
    def validate_buttons(self, num):
        if num == 1 or num == 3:
            for button in self.pbuttons:
                button["state"] = "normal"
        elif num == 2 or num == 3:
            for button in self.move_buttons:
                button["state"] = "normal"

    # Code that we use for our in-game UI
    def game_ui(self):
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")

        # Create sprite label from the downloaded image, and display it
        sprite_url = self.p1.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.psprite_label = Label(self.root, image=sprite)
        self.psprite_label.place(x=50, y=100)

        sprite_url = self.p2.played_pokemon.sprites
        esprite = self.load_sprite(sprite_url)
        self.esprite_label = Label(self.root, image=esprite)
        self.esprite_label.place(x=650, y=100)

        # Create a label that contains Pokémon current HP, and display it
        self.hitpointlabel1 = Label(self.root, textvariable=self.hp1)
        self.hitpointlabel1.place(x=50, y=250)

        self.hitpointlabel2 = Label(self.root, textvariable=self.hp2)
        self.hitpointlabel2.place(x=650, y=250)

        # Create a name button for each Pokémon the user has
        names = [pokemon.name for pokemon in self.p1.pokemon]
        button_state = []
        for i, name in enumerate(names):
            button_state.append([False, True, name])
        for i, name in enumerate(names):
            button = Button(self.root, text=name, command=lambda arg1=i: self.switch_pokemon(arg1))
            button["command"] = lambda arg1=i: self.switch_pokemon(arg1)
            button.place(x=125 + i * 100, y=400)
            self.pbuttons.append(button)

        for i, button in enumerate(self.pbuttons):
            if not button_state[i][1]:
                button["state"] = "disabled"
            elif not button_state[i][0]:
                button["state"] = "disabled"

        # Create move buttons using data from the Pokémon moveset, and display it
        moves = self.p1.played_pokemon.moves
        for i, move in enumerate(moves):
            button = Button(self.root, text=move["Name"])
            button["command"] = lambda arg1=button["text"]: self.paction(arg1)
            button.place(x=150 + i * 150, y=350)
            self.move_buttons.append(button)

        v = Scrollbar(self.root, orient='vertical')
        v.place(x=500, y=100)

        self.t = Text(self.root, width=30, height=13, wrap=NONE, yscrollcommand=v.set)
        self.t.pack()

        self.t["state"] = "disabled"

        v.config(command=self.t.yview)

        self.loading = True
        print(self.loading)
        self.root.mainloop()


class NBattle(LBattle):
    def __init__(self, stream):
        super().__init__()
        self.p1 = None
        self.p2 = None
        self.stream = stream
        return


a = LBattle()
