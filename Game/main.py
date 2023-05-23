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
        self.ip = None
        self.port = None
        self.fight = Button(self.root, text="fight")
        self.team = Button(self.root, text="team")
        self.bag = Button(self.root, text="bag")
        self.run = Button(self.root, text="run")
        self.root.withdraw()

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


    def temp_name(self):
        main = Tk()
        self.ip = StringVar(main)
        self.port = StringVar(main)
        self.ip.set("Enter IP Address Here")
        self.port.set("Enter Port Number Here")
        main.geometry("600x900")
        main.title("Pokémon Battle - Title Screen")
        maintitle = Label(main, text="Welcome to the Pokemon Battle!", font=("MS Comic Sans", "18"))
        maintitle.pack(ipadx=20,ipady=10,expand=True)
        choice1 = Label(main, text="Join a battle server", font=("MS Comic Sans", "14"))
        choice1.pack(ipadx=20,ipady=20,expand=True)
        ip1 = Entry(main, textvariable=self.ip)
        ip1.pack(ipadx=20)
        port1 = Entry(main, textvariable=self.port)
        port1.pack(ipadx=20)
        connect1 = Button(main, text="Connect!")
        connect1.pack()
        choice2 = Label(main, text="Create a battle server", font=("MS Comic Sans", "14"))
        choice2.pack(ipadx=20,ipady=20,expand=True)
        ip2 = Entry(main, textvariable=self.ip)
        ip2.pack(ipadx=20)
        port2 = Entry(main, textvariable=self.port)
        port2.pack(ipadx=20)
        create = Button(main, text="Create Server!")
        create.pack()
        credit = Label(main, text="This program was made by Calvin, Ebaad and Josh", font=("MS Comic Sans", "10"))
        credit.pack(ipadx=20,ipady=20,expand=True)
        main.mainloop()



    def main(self):
        self.root.deiconify()
        self.root.geometry("900x500")
        self.root.title("Pokémon Battle")
        self.fight.pack(side=RIGHT)
        self.team.pack(side=LEFT)
        self.bag.pack(side=BOTTOM)
        self.run.pack(side=BOTTOM)
        self.root.mainloop()


if __name__ == "__main__":
    b = GUI()
    # b.main()
    # Poke_API_OOP.PokemonAPI()
    b.temp_name()
