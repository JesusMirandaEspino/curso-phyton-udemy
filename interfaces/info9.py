from tkinter import filedialog as FileDialog
from tkinter import *
from tkinter import messagebox as MessageBox


def test():
    fichero = FileDialog.asksaveasfile(
        title="Guardar un fichero", mode='w', defaultextension=".txt")

    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()


root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()
