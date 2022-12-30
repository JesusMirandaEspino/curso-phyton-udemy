from tkinter import *
from tkinter import messagebox as MessageBox


def test():


    resultado = MessageBox.askquestion("Salir", "¿Está seguro que desea salir sin guardar?")

    if resultado == "yes":
        root.destroy()  # Destruir, alternativa a quit



root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()
