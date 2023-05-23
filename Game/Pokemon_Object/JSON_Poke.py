from Game.Pokemon_Object import Poke_Obj


class JSONtoPoke:
    def __init__(self, rawdata, index, caller):
        self.rawdata = rawdata
        self.name = None
        self.id = None
        self.types = None
        self.moves = None
        self.stats = None
        self.index = index
        self.caller = caller


    def get_moves(self):
        y = 0
        self.moves = []
        for x in self.rawdata["Moves"]:
            self.moves.append(x)
            self.moves[y]["DefaultPP"] = self.moves[0]["PP"]
            y += 1
        return self.moves

    def get_type(self):
        self.types = self.rawdata["Types"]
        return self.types

    def get_name(self):
        self.name = self.rawdata["Name"]
        return self.name

    def get_id(self):
        self.id = self.rawdata["ID"]
        return self.id

    def get_stats(self):
        self.stats = self.rawdata["Stats"]
        return self.stats

    def return_obj(self):
        self.name = self.get_name()
        self.id = self.get_id()
        self.types = self.get_type()
        self.moves = self.get_moves()
        self.stats = self.get_stats()
        pokemon = Poke_Obj.Pokemon(self.name, self.id, self.types, self.moves, self.stats, self.index, self.caller)
        return pokemon
