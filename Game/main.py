from tkinter import *
import json
from API import Poke_API_OOP

with open('Data/data.json', 'r') as file:
    data = file.read()

parsed_json = json.loads(data)

for i in parsed_json:
    print(i['Sprite'])


class GUI:
    def __init__(self):
        self.root = Tk()
        self.fight = Button(self.root, text="fight")
        self.team = Button(self.root, text="team")
        self.bag = Button(self.root, text="bag")
        self.run = Button(self.root, text="run")

    def main(self):
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")
        self.fight.place(x=750, y=400)
        self.team.place(x=650, y=400)
        self.bag.place(x=750, y=450)
        self.run.place(x=650, y=450)
        self.root.mainloop()


if __name__ == "__main__":
    b = GUI()
    b.main()
    Poke_API_OOP.PokemonAPI()
