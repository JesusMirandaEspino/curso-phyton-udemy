from tkinter import *
# Widget Entry(Texto corto)
# Los campos de texto sirven generalmente para que el usuario escriba un valor. 
# Sería un puente que equivaldría a la función input() pero gráficamente. 
# Lo bueno es que integra muchos métodos que le permiten desde borrar el texto a desactivar el campo.


root = Tk()


frame1 = Frame(root)
frame1.pack()

entry = Entry(frame1)
entry.pack(side=RIGHT)

label = Label(frame1, text="Nombre")
label.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack()

entry2 = Entry(frame2)
entry2.pack(side=RIGHT)

label2 = Label(frame2, text="Apellidos")
label2.pack(side=LEFT)

root.mainloop()
