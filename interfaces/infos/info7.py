from tkinter import colorchooser as ColorChooser
from tkinter import *
from tkinter import messagebox as MessageBox


def test():

    color = ColorChooser.askcolor(title="Elige un color")
    print(color)


root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()
