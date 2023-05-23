from tkinter import *
import json
import connection
import battle
from API import Poke_API_OOP

with open('Data/data.json', 'r') as file:
    data = file.read()

parsed_json = json.loads(data)

for i in parsed_json:
    print(i['Sprite'])


class GUI:
    def __init__(self):
        self.mainframe = None
        self.root = Tk()
        self.pipe = None
        self.online = False
        self.op = False
        self.game = False
        self.fight = Button(self.root, text="fight")
        self.team = Button(self.root, text="team")
        self.bag = Button(self.root, text="bag")
        self.run = Button(self.root, text="run")

    def connec(self, ip, port):
        self.pipe = connection.GameConnection(ip, port)
        self.pipe.make_connection()

    def makeserver(self, ip, port):
        self.pipe = connection.GameConnection(ip, port)
        self.pipe.create_server()

    def start(self, ip=None, port=None):
        if self.online:
            if self.op:
                self.pipe.makeserver(ip, port)
                self.game = battle.NBattle(self.pipe)
                self.game.start_battle()
            else:
                self.pipe.connec(ip, port)
                self.game = battle.NBattle(self.pipe)
        else:
            self.game = battle.LBattle()
            self.game.start_battle()



    def main(self):
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")
        self.fight.pack(side=RIGHT)
        self.team.pack(side=LEFT)
        self.bag.pack(side=BOTTOM)
        self.run.pack(side=BOTTOM)
        self.root.mainloop()


if __name__ == "__main__":
    b = GUI()
    b.main()
    Poke_API_OOP.PokemonAPI()
