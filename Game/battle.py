"""
Joshua
CS 30 Period 1
May 12, 2023,
This is the battling mechanic of the Pokémon game
"""
import enemies


class LBattle:
    def __init__(self):
        self.lvl = 1
        self.p1 = None
        self.p2 = enemies.Trainer(self.lvl)
        return

    def start_battle(self):
        self.p1.turn(self.p2.played_pokemon)
        self.p2.turn(self.p1.played_pokemon)

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


class NBattle(LBattle):
    def __init__(self, stream):
        super().__init__()
        self.p1 = None
        self.p2 = None
        self.stream = stream
        return