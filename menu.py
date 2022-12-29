from tkinter import *

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)  # Lo asignamos a la base

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)


menubar.add_cascade(label="Archivo", menu=filemenu)


root.mainloop()
