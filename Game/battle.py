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

# Disable certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


class LBattle:
    def __init__(self):
        self.lvl = 1
        """self.p1 = None
        self.p2 = enemies.Trainer(self.lvl)"""
        self.root = Tk()
        self.pokemon_data = self.load_pokemon_data()
        self.current_pokemon_index = 0

    def load_pokemon_data(self):
        with open('./Data/player.json') as json_file:
            data = json.load(json_file)
            return data

    def load_sprite(self, url):
        response = request.urlopen(url)
        image_data = response.read()
        image_stream = io.BytesIO(image_data)
        sprite = Image.open(image_stream)
        sprite = sprite.resize((150, 150), Image.LANCZOS)
        sprite = ImageTk.PhotoImage(sprite)
        return sprite

    def update_sprite(self):
        sprite_url = self.pokemon_data[self.current_pokemon_index]["Sprite"]
        sprite = self.load_sprite(sprite_url)
        self.sprite_label.config(image=sprite)
        self.sprite_label.image = sprite  # Keep a reference to avoid garbage collection

    def update_moves(self):
        moves = self.pokemon_data[self.current_pokemon_index]["Moves"]
        for i, move in enumerate(moves):
            self.move_buttons[i].config(text=move["Name"])

    def switch_pokemon(self, index):
        self.current_pokemon_index = index
        self.update_sprite()
        self.update_moves()

    def game_ui(self):
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")

        # Create sprite label
        sprite_url = self.pokemon_data[self.current_pokemon_index]["Sprite"]
        sprite = self.load_sprite(sprite_url)
        self.sprite_label = Label(self.root, image=sprite)
        self.sprite_label.place(x=50, y=100)

        # Create name buttons for each Pokémon
        names = [pokemon["Name"] for pokemon in self.pokemon_data]
        name_buttons = []
        for i, name in enumerate(names):
            button = Button(self.root, text=name, command=lambda index=i: self.switch_pokemon(index))
            button.place(x=125 + i * 100, y=400)
            name_buttons.append(button)

        # Create move buttons
        moves = self.pokemon_data[self.current_pokemon_index]["Moves"]
        self.move_buttons = []
        for i, move in enumerate(moves):
            button = Button(self.root, text=move["Name"])
            button.place(x=150 + i * 150, y=350)
            self.move_buttons.append(button)

        self.root.mainloop()


class NBattle(LBattle):
    def __init__(self, stream):
        super().__init__()
        self.p1 = None
        self.p2 = None
        self.stream = stream
        return


a = LBattle()
a.game_ui()
