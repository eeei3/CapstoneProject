from tkinter import *
import json
import connection
import battle
from multiprocessing import Process
# from API import Poke_API_OOP

"""with open('Data/data.json', 'r') as file:
    data = file.read()

parsed_json = json.loads(data)

for i in parsed_json:
    print(i['Sprite'])"""


class GUI:
    def __init__(self):
        self.mainframe = None
        self.root = Tk()
        self.main = Tk()
        self.pipe = None
        self.online = False
        self.op = False
        self.game = False
        self.ip = None
        self.port = None
        self.process1 = Process(target=self.gamewin)
        self.process2 = None
        self.process3 = None
        self.connect_process = connection.GameConnection()
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

    def offgame(self):
        #self.game = battle.LBattle()
        self.process1.start()
        #self.process2 = Process(target=self.game.start_battle)
        #self.process2.start()
       # self.process2.join()
        self.process1.join()

    def joingame(self):
        ip = self.ip.get()
        port = self.port.get()
        try:
            self.pipe.connec(ip, port)
        except Exception as e:
            print("Could not connect!")
        self.process1.start()
        #self.game = battle.NBattle(self.pipe)

    def ongame(self):
        ip = self.ip.get()
        port = self.port.get()
        try:
            self.process3 = Process(target=self.pipe.makeserver, args=(ip, port,))
            self.process3.start()
        except Exception as e:
            self.process3.join()
            print("Could not create a new server!")
        """self.game = battle.NBattle(self.pipe)
        self.process2 = Process(target=self.game.start_battle)
        self.process1.start()
        self.process2.start()
        self.process1.join()
        self.process2.join()"""

    def temp_name(self):
        self.ip = StringVar(self.main)
        self.port = StringVar(self.main)
        self.ip.set("Enter IP Address Here")
        self.port.set("Enter Port Number Here")
        self.main.geometry("600x900")
        self.main.title("Pokémon Battle - Title Screen")
        maintitle = Label(self.main, text="Welcome to the Pokemon Battle!", font=("MS Comic Sans", "18"))
        maintitle.pack(ipadx=20,ipady=10,expand=True)
        choice1 = Label(self.main, text="Join a battle server", font=("MS Comic Sans", "14"))
        choice1.pack(ipadx=20,ipady=20,expand=True)
        ip1 = Entry(self.main, textvariable=self.ip)
        ip1.pack(ipadx=20)
        port1 = Entry(self.main, textvariable=self.port)
        port1.pack(ipadx=20)
        connect1 = Button(self.main, text="Connect!", command=self.joingame)
        connect1.pack()
        choice2 = Label(self.main, text="Create a battle server", font=("MS Comic Sans", "14"))
        choice2.pack(ipadx=20,ipady=20,expand=True)
        ip2 = Entry(self.main, textvariable=self.ip)
        ip2.pack(ipadx=20)
        port2 = Entry(self.main, textvariable=self.port)
        port2.pack(ipadx=20)
        create = Button(self.main, text="Create Server!", command=self.ongame)
        create.pack()
        choice3 = Label(self.main, text="Play an offline bot!", font=("MS Comic Sans", "14"))
        choice3.pack(ipadx=20, ipady=20, expand=True)
        start = Button(self.main, text="Play Bot!", command=self.offgame)
        start.pack()
        credit = Label(self.main, text="This program was made by Calvin, Ebaad and Josh", font=("MS Comic Sans", "10"))
        credit.pack(ipadx=20,ipady=20,expand=True)
        self.main.mainloop()

    def gamewin(self):
        self.root.deiconify()
        self.main.withdraw()
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
