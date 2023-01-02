from tkinter import *
from tkinter import messagebox as MessageBox


def test():


    resultado = MessageBox.askokcancel("Salir", "¿Sobreescribir fichero actual?")

    if resultado == True:
        root.destroy() # Hacer algo

root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()
