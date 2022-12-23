from tkinter import *
# Widget Entry(Texto corto)
# Los campos de texto sirven generalmente para que el usuario escriba un valor.
# Sería un puente que equivaldría a la función input() pero gráficamente.
# Lo bueno es que integra muchos métodos que le permiten desde borrar el texto a desactivar el campo.


root = Tk()


label = Label(root, text="Nombre")
label.grid(row=0, column=0, sticky=W)

entry = Entry(root)
entry.grid(row=0, column=1)

label2 = Label(root, text="Apellidos")
label2.grid(row=1, column=0, sticky=W)

entry2 = Entry(root)
entry2.grid(row=1, column=1)


root.mainloop()
