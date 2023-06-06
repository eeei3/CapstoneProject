# ---------------------------------------------
# Title: battle.py
# Class: CS 30
# Date: 19/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: battle.py


"""
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

# Allows for connecting to an outside domain
# Bypasses error on macOS
ssl._create_default_https_context = ssl._create_unverified_context


class LBattle:
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

    def load_pokemon_data(self):
        with open('Data/data.json') as json_file:
            data = json.load(json_file)
            return data[6:]

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
        self.message(f"Player has used {move}\n")
        self.turn = 2

    def message(self, msg):
        self.t.config(state="normal")
        self.t.insert(END, msg)
        self.t.config(state="disabled")

    def start_battle(self):
        while not self.loading:
            time.sleep(1)

        self.message(f"Start of match with Trainer {self.p2.name}\n")
        self.message(f"Trainer has chosen {self.p2.played_pokemon.name}\n")
        self.p2.start()

        while True:
            self.message(f"{self.p1.name}'s turn\n")
            self.turn = 1
            self.validate_buttons(3)
            while self.turn == 1:
                pass
            self.message(f"{self.p2.name}'s turn\n")
            self.p2.check()
            self.hp2.set(str(self.p2.played_pokemon.stats["hp"]))
            self.hp1.set(str(self.p1.played_pokemon.stats["hp"]))
            self.invalidate_buttons(3)
            time.sleep(3)
            m = self.p2.turn(self.p1.played_pokemon)
            time.sleep(3)
            while m is None:
                pass
            if m[0] == 1:
                self.message(f"{self.p2.played_pokemon.name} has used {m[1]}\n")
            elif m[0] == 2:
                self.message(f"Trainer {self.p2.name} has switched to {self.p2.played_pokemon.name}\n")
                self.update_sprite()
            elif m[0] == 5:
                self.message(f"{self.p2.played_pokemon.name} has used {m[1]}, its not very effective\n")
            elif m[0] == 6:
                self.message(f"{self.p2.played_pokemon.name} has used {m[1]}, its very effective!\n")
            name = self.p1.played_pokemon.name
            if self.p1.check() == 0:
                i = 0
                for button in self.pbuttons:
                    if button[2] == name:
                        button[1] = 1
                    elif button[1] == 0:
                        button[0]["command"] = lambda arg1=i: self.switch_pokemon(arg1)
                        i += 1
                for button in self.move_buttons:
                    button[1] = 1
            else:
                for button in self.move_buttons:
                    button[1] = 0
            self.hp1.set(str(self.p1.played_pokemon.stats["hp"]))
            self.hp2.set(str(self.p2.played_pokemon.stats["hp"]))
            self.update_sprite()

    def update_sprite(self):
        sprite_url = self.p1.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.psprite_label.config(image=sprite)
        self.psprite_label.image = sprite
        sprite_url = self.p2.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.esprite_label.config(image=sprite)
        self.esprite_label.image = sprite

    def update_moves(self):
        moves = self.p1.played_pokemon.moves
        for i, move in enumerate(moves):
            self.move_buttons[i][0].config(text=move["Name"])
            self.move_buttons[i][0]["command"] = lambda arg1=self.move_buttons[i][0]["text"]: self.paction(arg1)

    def switch_pokemon(self, index):
        self.message(f"{self.p1.name} has switched to {self.p1.played_pokemon.name}\n")
        self.current_pokemon_index = index
        self.p1.switch_pokemon(index)
        self.update_sprite()
        self.update_moves()
        self.turn = 2

    def invalidate_buttons(self, num):
        if num == 1 or num == 3:
            for button in self.pbuttons:
                button[0].config(state="disabled")
        if num == 2 or num == 3:
            for button in self.move_buttons:
                button[0].config(state="disabled")

    def validate_buttons(self, num):
        if num == 1 or num == 3:
            for i, button in enumerate(self.pbuttons):
                if button[1] == 0:
                    button[0].config(state="normal")
        if num == 2 or num == 3:
            for i, button in enumerate(self.move_buttons):
                if button[1] == 0:
                    button[0].config(state="normal")

    def quit_game(self):
        self.root.destroy()

    def game_ui(self):
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")

        quit_button = Button(self.root, text="Quit", command=self.quit_game)
        quit_button.place(x=450, y=450)

        sprite_url = self.p1.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.psprite_label = Label(self.root, image=sprite)
        self.psprite_label.place(x=50, y=100)

        sprite_url = self.p2.played_pokemon.sprites
        esprite = self.load_sprite(sprite_url)
        self.esprite_label = Label(self.root, image=esprite)
        self.esprite_label.place(x=650, y=100)

        self.hitpointlabel1 = Label(self.root, textvariable=self.hp1)
        self.hitpointlabel1.place(x=50, y=250)

        self.hitpointlabel2 = Label(self.root, textvariable=self.hp2)
        self.hitpointlabel2.place(x=650, y=250)

        names = [pokemon.name for pokemon in self.p1.pokemon]
        """button_state = [[False, True, name] for name in names]"""
        for i, name in enumerate(names):
            button = Button(self.root, text=name, command=lambda arg1=i: self.switch_pokemon(arg1))
            button["command"] = lambda arg1=i: self.switch_pokemon(arg1)
            button.place(x=125 + i * 100, y=400)
            self.pbuttons.append([button, 0, name])

        moves = self.p1.played_pokemon.moves
        for i, move in enumerate(moves):
            button = Button(self.root, text=move["Name"])
            button["command"] = lambda arg1=button["text"]: self.paction(arg1)
            button.place(x=150 + i * 150, y=350)
            self.move_buttons.append([button, 0])

        v = Scrollbar(self.root, orient='vertical')
        v.place(x=500, y=100)

        self.t = Text(self.root, width=30, height=13, wrap=NONE, yscrollcommand=v.set)
        self.t.pack()

        self.t.config(state="disabled")

        v.config(command=self.t.yview)

        self.loading = True
        self.root.mainloop()

