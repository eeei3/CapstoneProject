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
    def main(self):
        self.mainframe = Frame()

        self.root.title("ebaad")
        self.root.maxsize(400, 700)
        self.root.minsize(400, 700)
        self.root.mainloop()

b = GUI()
b.main()