# ---------------------------------------------
# Title: battle.py
# Class: CS 30
# Date: 19/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: battle.py

This file is our main battling file.
It handles our battle logic, move and spite presentations
It contains the Battle UI, quit buttons and updating moves and
sprites when changing
"""
# Important package imports
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


# The Main battle class contains codes for various battling obejcts
class LBattle:
    def __init__(self, lvl, username):
        """
        Initializing the battle class
        """
        # Enemy difficulty
        self.lvl = lvl
        # Tkinter window
        self.root = Toplevel()
        # self.current_pokemon_index = 0
        # Keeping track of turn
        self.turn = 1
        # Player object
        self.p1 = player.Player(username)
        # Enemy object
        self.p2 = enemies.Trainer(self.lvl)
        # Object for textbox
        self.t = None
        # List of pokemon buttons
        self.pbuttons = []
        # self.pcmds = []
        # List of moves buttons
        self.move_buttons = []
        # self.movecmds = []
        # Variable for storing player pokemon health
        self.hp1 = StringVar()
        # Variable for storing enemy pokemon health
        self.hp2 = StringVar()
        self.hp1.set(str(self.p1.played_pokemon.stats["hp"]))
        self.hp2.set(str(self.p2.played_pokemon.stats["hp"]))
        # Number of enemy pokemon
        self.enemypokemon = IntVar()
        self.enemypokemon.set(len(self.p2.pokemon))
        # Checking if the game is finished loading
        self.loading = False
        # Object for thread
        self.thread = threading.Thread(target=self.start_battle)
        self.thread.daemon = False
        # Return code
        self.code = 1

    def start(self):
        """
        Starting the battle thread and the game UI
        """
        self.thread.start()
        self.game_ui()
        return self.code

    def load_sprite(self, url):
        """
        Loading and resizing the sprite image from a URL
        """
        response = request.urlopen(url)
        image_data = response.read()
        image_stream = io.BytesIO(image_data)
        sprite = Image.open(image_stream)
        sprite = sprite.resize((150, 150), Image.LANCZOS)
        sprite = ImageTk.PhotoImage(sprite)
        return sprite

    def paction(self, move):
        """
        Wrapper function for player action
        """
        m = self.p1.turn(self.p2.played_pokemon, move)
        if m == 5:
            self.message(f"{self.p1.played_pokemon.name} has "
                         f"used {move}, its not very effective\n")
        elif m == 6:
            self.message(f"{self.p1.played_pokemon.name} has "
                         f"used {move}, its very effective!\n")
        elif m == 9:
            self.message(f"{self.p1.played_pokemon.name} missed!\n")
        else:
            self.message(f"{self.p1.played_pokemon.name} has "
                         f"used {move}\n")
        self.turn = 2

    def message(self, msg):
        """
        Method for piping data to the text box
        """
        self.t.config(state="normal")
        self.t.insert(END, msg)
        self.t.config(state="disabled")

    def start_battle(self):
        """
        Main battle loop and logic
        """
        while not self.loading:
            time.sleep(1)
        self.message(f"Start of match with Trainer {self.p2.name}\n")
        self.message(f"Trainer has chosen {self.p2.played_pokemon.name}"
                     f"\n")
        self.p2.start()
        b = bool(self.t.winfo_ismapped())
        while b is True:
            try:
                b = bool(self.t.winfo_ismapped())
            except:
                b = False
            while (len(self.p2.pokemon) != 0) and (b is True):
                b = bool(self.t.winfo_ismapped())
                self.message(f"{self.p1.name}'s turn\n")
                self.turn = 1
                self.validate_buttons(3)
                while self.turn == 1:
                    pass
                self.message(f"{self.p2.name}'s turn\n")
                if self.p2.check() == 0:
                    self.message(f"{self.p2.name}'s pokemon has fainted"
                                 f"!\n")
                self.enemypokemon.set(len(self.p2.pokemon))
                self.hp2.set(str(self.p2.played_pokemon.stats["hp"]))
                self.hp1.set(str(self.p1.played_pokemon.stats["hp"]))
                if len(self.p2.pokemon) == 0:
                    self.code = 0
                    self.message("You won congrats! You will move onto "
                                 "a harder trainer in\n")
                    self.message("5\n")
                    time.sleep(1)
                    self.message("4\n")
                    time.sleep(1)
                    self.message("3\n")
                    time.sleep(1)
                    self.message("2\n")
                    time.sleep(1)
                    self.message("1\n")
                    time.sleep(1)
                    self.quit_window()
                    continue
                self.invalidate_buttons(3)
                time.sleep(1)
                m = self.p2.turn(self.p1.played_pokemon)
                time.sleep(1)
                self.hp1.set(str(self.p1.played_pokemon.stats["hp"]))
                self.hp2.set(str(self.p2.played_pokemon.stats["hp"]))
                while m is None:
                    pass
                if m[0] == 1:
                    self.message(f"{self.p2.played_pokemon.name} has "
                                 f"used {m[1]}\n")
                elif m[0] == 2:
                    self.message(f"Trainer {self.p2.name} has switched "
                                 f"to {self.p2.played_pokemon.name}\n")
                    self.update_sprite()
                elif m[0] == 5:
                    self.message(f"{self.p2.played_pokemon.name} has "
                                 f"used {m[1]}, its not very effective"
                                 f"\n")
                elif m[0] == 6:
                    self.message(f"{self.p2.played_pokemon.name} "
                                 f"has used {m[1]}, its very effective!"
                                 f"\n")
                elif m[0] == 9:
                    self.message(f"{self.p2.played_pokemon.name} "
                                 f"missed their attack!\n")
                name = self.p1.played_pokemon.name
                if self.p1.check() == 0:
                    i = 0
                    self.message(f"{self.p1.name}'s pokemon has fainted"
                                 f"!\n")
                    for button in self.pbuttons:
                        if button[2] == name:
                            button[1] = 1
                        elif button[1] == 0:
                            button[0]["command"] = lambda arg1=i: \
                                self.switch_pokemon(arg1)
                            i += 1
                    for button in self.move_buttons:
                        button[1] = 1
                    if len(self.p1.pokemon) == 0:
                        self.message("You lost!\n")
                        self.message("Press the quit button to return "
                                     "to main menu and restart\n")
                        while True:
                            pass

                else:
                    for button in self.move_buttons:
                        button[1] = 0
                self.update_sprite()
        return 0

    def update_sprite(self):
        """
        Updating and handling player and trainers sprites
        """
        sprite_url = self.p1.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.psprite_label.config(image=sprite)
        self.psprite_label.image = sprite
        sprite_url = self.p2.played_pokemon.sprites
        sprite = self.load_sprite(sprite_url)
        self.esprite_label.config(image=sprite)
        self.esprite_label.image = sprite

    def update_moves(self):
        """
        Updating the players move options, whenever they switch
        """
        moves = self.p1.played_pokemon.moves
        if len(self.move_buttons) < len(moves):
            self.move_buttons = []
            for i, move in enumerate(moves):
                button = Button(self.root, text=move["Name"])
                button["command"] = lambda arg1=button["text"]: \
                    self.paction(arg1)
                button.place(x=150 + i * 150, y=350)
                self.move_buttons.append([button, 0])
        elif len(self.move_buttons) > len(moves):
            self.move_buttons = []
            for i, move in enumerate(moves):
                button = Button(self.root, text=move["Name"])
                button["command"] = lambda arg1=button["text"]: \
                    self.paction(arg1)
                button.place(x=150 + i * 150, y=350)
                self.move_buttons.append([button, 0])
        else:
            for i, move in enumerate(moves):
                self.move_buttons[i][0].config(text=move["Name"])
                self.move_buttons[i][0]["command"] = lambda \
                        arg1=self.move_buttons[i][0]["text"]: \
                    self.paction(arg1)

    def switch_pokemon(self, index):
        """
        Handling the switching of a Pokémon
        """
        self.current_pokemon_index = index
        self.p1.switch_pokemon(index)
        self.update_sprite()
        self.update_moves()
        self.message(f"{self.p1.name} has switched to "
                     f"{self.p1.played_pokemon.name}\n")
        self.turn = 2

    def invalidate_buttons(self, num):
        """
        Handles disabling buttons for various reasons.
        """
        if num == 1 or num == 3:
            for button in self.pbuttons:
                button[0].config(state="disabled")
        if num == 2 or num == 3:
            for button in self.move_buttons:
                button[0].config(state="disabled")

    def validate_buttons(self, num):
        """
        Handles enabling buttons for various reasons
        """
        if num == 1 or num == 3:
            for i, button in enumerate(self.pbuttons):
                if button[1] == 0:
                    button[0].config(state="normal")
        if num == 2 or num == 3:
            for i, button in enumerate(self.move_buttons):
                if button[1] == 0:
                    button[0].config(state="normal")

    def quit_window(self, *code):
        """
        Used to allow player to quit the game in the Game UI
        """
        if len(code) > 0:
            self.code = 1
        self.root.destroy()
        self.root.quit()

    def game_ui(self):
        """
        Sets up the game UI window
        """
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")

        quit_button = Button(
            self.root, text="Quit", command=lambda arg1=1:
            self.quit_window(arg1))
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

        enemypokemonlabel = Label(
            self.root, text="Enemy's remaining pokemon:")
        enemypokemonlabel.place(x=650, y=300)

        enemypokemonnum = Label(self.root, textvariable=
        self.enemypokemon)
        enemypokemonnum.place(x=820, y=300)

        names = [pokemon.name for pokemon in self.p1.pokemon]

        for i, name in enumerate(names):
            button = Button(self.root, text=name, command=lambda
                arg1=i: self.switch_pokemon(arg1))
            button["command"] = lambda arg1=i: self.switch_pokemon(arg1)
            button.place(x=125 + i * 100, y=400)
            self.pbuttons.append([button, 0, name])

        moves = self.p1.played_pokemon.moves

        for i, move in enumerate(moves):
            button = Button(self.root, text=move["Name"])
            button["command"] = lambda arg1=button["text"]: \
                self.paction(arg1)
            button.place(x=150 + i * 150, y=350)
            self.move_buttons.append([button, 0])

        v = Scrollbar(self.root, orient='vertical')
        v.place(x=500, y=100)

        self.t = Text(self.root, width=50, height=13, wrap=NONE,
                      yscrollcommand=v.set)
        self.t.pack()

        self.t.config(state="disabled")

        v.config(command=self.t.yview)

        self.loading = True
        self.root.mainloop()
        return 0
