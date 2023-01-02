from tkinter import *
from tkinter import messagebox as MessageBox


def test():
    MessageBox.showwarning("Alerta","Sección sólo para administradores.")



root = Tk()

Button(root, text="Clícame", command=test).pack()

root.mainloop()
