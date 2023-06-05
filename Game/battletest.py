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
import enemies
import player


class LBattle:
    def __init__(self):
        self.lvl = 1
        self.p1 = player.Player("Larry")
        self.p2 = enemies.Trainer(self.lvl)

    def start_battle(self):
        self.p2.start()
        print("start")
        for index, pokemon in enumerate(self.p1.pokemon):
            print(f"{index}. {pokemon.name}")

        while True:
            print("p1 turn")
            choice = input("Enter your choice: ")
            if choice == "attack":
                print("attacking")
                for index, attack in enumerate(self.p1.played_pokemon.moves):
                    print(f"{index}. {attack['Name']}")
                choice2 = input("Enter the attack number: ")
                self.p1.turn(self.p2.played_pokemon, int(choice2))
            elif choice == "switch":
                print("switching")
                choice1 = input("Enter the Pokemon number to switch: ")
                self.p1.switch_pokemon(int(choice1))

            if self.p2.check() == 0:
                print("p2 pokemon dead")

            print("p2 turn")
            self.p2.turn(self.p1.played_pokemon)

            if self.p1.check() == 0:
                print("p1 pokemon dead")
                choice3 = input("Enter the Pokemon number to switch: ")
                self.p1.switch_pokemon(int(choice3))


a = LBattle()
a.start_battle()
