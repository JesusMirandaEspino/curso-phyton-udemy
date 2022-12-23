from tkinter import *
root = Tk()


frame = Frame(root, width=480, height=320)
frame.pack()
label = Label(frame,text="¡Hola Mundo!")


label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor=CENTER)
label.config(fg="blue", bg="green", font=("Verdana", 24))
texto = StringVar()
texto.set("Un nuevo texto")
label.config(textvariable=texto)  # añadimos una variable de texto
Label(root, text="¡Hola Mundo!").pack()
Label(root, text="¡Otra etiqueta!").pack()
Label(root, text="¡Última etiqueta!").pack()
Label(root, text="¡Hola Mundo!").pack(anchor=NW)
Label(root, text="¡Otra etiqueta!").pack(anchor=CENTER)
Label(root, text="¡Última etiqueta!").pack(anchor=SE)


label.pack()

root.mainloop() 

