from tkinter import *



def hola():
    print("Hola mundo!")


# Configuración de la raíz
root = Tk()
root.config(bd=15)


s = StringVar()



Label(root, text="").pack()  # Separador



# Enlezamos la función a la acción del botón
Button(root, text="Clícame", command=hola).pack()


# Finalmente bucle de la aplicación
root.mainloop()
