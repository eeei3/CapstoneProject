# ---------------------------------------------
# Title: battletest.py
# Class: CS 30
# Date: 27/05/23
# Version: 1.0
# ---------------------------------------------
"""
Current Assignment: battletest.py

This file is what we use for testing our various battle mechanics.
Do not run this file, run MAIN.PY
"""
# Important import statements
import enemies
import player


# Battle Class
class LBattle:

    # Initializing attributes
    def __init__(self):
        self.lvl = 1
        self.p1 = player.Player("Larry")
        self.p2 = enemies.Trainer(self.lvl)

    # Battle testing code
    def start_battle(self):
        self.p2.start()
        print("start")
        for pokemon in self.p1.pokemon:
            print(pokemon.name)
        choice4 = input("")
        self.p1.played_pokemon = self.p1.pokemon[int(choice4)]
        while True:
            print("p1 turn")
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


a = LBattle()
a.start_battle()
