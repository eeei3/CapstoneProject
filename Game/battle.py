"""
Joshua
CS 30 Period 1
May 12, 2023
This is the battling mechanic of the Pokémon game
"""

class LBattle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        return

    def start_battle(self):
        self.p1.turn()
        self.p2.turn()



class NBattle(LBattle):
    def __init__(self, p1, p2, stream):
        super().__init__(p1, p2)
        return