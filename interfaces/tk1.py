# Código final:
from tkinter import *


# Creamos la raíz
root = Tk()

# Comenzamos el bucle de aplicación, es como un while True
root.mainloop()

# Un par de opciones interesantes:
root.title("Hola mundo")     # Título de la ventana
root.iconbitmap('hola.ico')  # Icono de la ventana, en ico o xbm en Linux
root.resizable(0, 0)         # Desactivar redimensión de ventana
# Icono en GNU/Linux

# En la mayoría de distribuciones hay que usar un icono de tipo xbm con la siguiente lógica:
root.iconbitmap('@hola.xbm')
# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1, 1)
root.iconbitmap('hola.ico')

# Finalmente bucle de la aplicación
root.mainloop()
