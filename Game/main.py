"""

"""

from tkinter import *
from Pokemon_Object import Poke_Obj


class GUI:
    def __init__(self):
        self.root = Tk()
    def main(self):
        self.mainframe = Frame()

        self.root.title("ebaad")
        self.root.maxsize(400, 700)
        self.root.minsize(400, 700)
        self.root.mainloop()

b = GUI()
b.main()