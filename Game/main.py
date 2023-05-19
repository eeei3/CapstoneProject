from tkinter import *
import json

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
        self.fight.pack(side=RIGHT)
        self.team.pack(side=LEFT)
        self.bag.pack(side=BOTTOM)
        self.run.pack(side=BOTTOM)
        self.root.mainloop()

b = GUI()
b.main()