from tkinter import *
root = Tk()
root.title("Mi editor")


def nuevo():
    mensaje.set('Nuevo fichero')


def abrir():
    mensaje.set('Nuevo fichero')


def guardar():
    mensaje.set('Guardar fichero')


def guardar_como():
    print("Guardar fichero como")

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

# Caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(padx=6, pady=4, bd=0, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar=mensaje, justify='right')
monitor.pack(side='left')

# Menu y bucle de la aplicación
root.config(menu=menubar)
root.mainloop()
