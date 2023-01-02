from tkinter import *
from tkinter import messagebox as MessageBox


def test():
    MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")


root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()
