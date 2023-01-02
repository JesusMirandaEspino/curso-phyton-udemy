from tkinter import *


def selec():
    monitor.config(text="Opción {}".format(opcion.get()))


root = Tk()
root.config(bd=15)

opcion = IntVar()  # Como StrinVar pero en entero

Radiobutton(root, text="Opción 1", variable=opcion,
            value=1, command=selec).pack()
Radiobutton(root, text="Opción 2", variable=opcion,
            value=2, command=selec).pack()
Radiobutton(root, text="Opción 3", variable=opcion,
            value=3, command=selec).pack()

monitor = Label(root)
monitor.pack()

root.mainloop()
