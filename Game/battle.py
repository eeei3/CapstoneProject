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

# Disable certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


class LBattle:
    def __init__(self):
        self.lvl = 1
        """self.p1 = None
        self.p2 = enemies.Trainer(self.lvl)"""
        self.root = Toplevel()
        self.pokemon_data = self.load_pokemon_data()
        self.current_pokemon_index = 0
        self.lvl = 1
        self.p1 = player.Player("Larry")
        self.p2 = enemies.Trainer(self.lvl)
        self.t = None
        self.turn = 1
        self.pbuttons = []
        self.move_buttons = []

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

    def action(self):
        return

    def switch(self):
        return

    def start_battle(self):
        self.p2.start()
        self.t.insert('1.0', f"Start of match with Trainer {self.p2.name}")
        self.t.insert('1.0', f"Pick your Pokemon!")
        while(self.p1.played_pokemon == None):
            pass
        for pokemon in self.p1.pokemon:
            print(pokemon.name)
        choice4 = input("")
        self.p1.played_pokemon = self.p1.pokemon[int(choice4)]
        while True:
            self.t.insert('1.0', f"{self.p1.name}'s turn")
            self.turn = 1
            while self.turn == 1:
                pass
            self.invalidate_buttons(3)
            self.t.insert('1.0', f"{self.p2.name}'s turn")
            self.turn = 2
            while self.turn == 2:
                pass





            choice = input("")
            if choice == "attack":
                print("attacking")
                for attack in self.p1.played_pokemon.moves:
                    print(attack["Name"])
                choice2 = input("")
                self.p1.turn(self.p2.played_pokemon, choice2)
            elif choice == "switch":
                print("switching")
                choice1 = input("")
                self.p1.switch_pokemon(int(choice1))
            if self.p2.check() == 0:
                print("p2 pokemon dead")
            print("p2 turn")
            self.p2.turn(self.p1.played_pokemon)
            if self.p1.check() == 0:
                print("p1 pokemon dead")
                choice3 = input("")
                self.p1.switch_pokemon(int(choice3))

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

    def invalidate_buttons(self, num):
        if num == 1 or num == 3:
            for button in self.pbuttons:
                button["state"] = "disabled"
        elif num == 2 or num == 3:
            for button in self.move_buttons:
                button["state"] = "disabled"

    def validate_buttons(self):
        for button in self.pbuttons:
            button["stats"] = "enabled"

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
        button_state = []
        for i, name in enumerate(names):
            button_state.append([False, True, name])
        for i, name in enumerate(names):
            button = Button(self.root, text=name, command=lambda index=i: self.switch_pokemon(index))
            button.place(x=125 + i * 100, y=400)
            self.pbuttons.append(button)

        for i, button in enumerate(self.pbuttons):
            if not button_state[i][1]:
                button["state"] = "disabled"
            elif not button_state[i][0]:
                button["state"] = "disabled"


        # Create move buttons
        moves = self.pokemon_data[self.current_pokemon_index]["Moves"]
        for i, move in enumerate(moves):
            button = Button(self.root, text=move["Name"])
            button.place(x=150 + i * 150, y=350)
            self.move_buttons.append(button)

        v = Scrollbar(self.root, orient='vertical')
        v.place(x=500, y=100)

        self.t = Text(self.root, width=30, height=13, wrap=NONE, yscrollcommand=v.set)
        self.t.pack()

        self.t["state"] = "disabled"

        v.config(command=self.t.yview)

        self.root.mainloop()


class NBattle(LBattle):
    def __init__(self, stream):
        super().__init__()
        self.p1 = None
        self.p2 = None
        self.stream = stream
        return

"""
a = LBattle()
# if __name__ == '__main__':
    # a.root = Tk()
a.game_ui()"""
