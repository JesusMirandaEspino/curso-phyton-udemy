from tkinter import *
from tkinter import messagebox as MessageBox


def test():


    resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")

    if resultado == True:
        # Hacer algo
        root.destroy()  # Hacer algo


root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()
