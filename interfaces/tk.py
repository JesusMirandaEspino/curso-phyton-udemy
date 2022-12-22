# Widget Tk (Raíz)
# Muy bien, pues vamos a comenzar por lo más esencial, la raíz o base de la interfaz gráfica.
# Recordad que la raíz es el contenedor base de todos los widgets que forman la interfaz, 
# no tiene tamaño propio sino que se adapta a los widgets que contiene:

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

# Tip Windows: Abrir los scripts gráficos con doble clic

# Si cambiamos la extensión de nuestros scripts gráficos a .pyw y asignamos el ejecutable pythonw.exe como aplicación por defecto para abrirlos podremos ejecutarlos haciendo doble clic. Podéis encontrar el ejeuctable en la carpeta de Anaconda. Por cierto, la 'w' significa 'windowed' (modo ventana) y esconde la terminal de fondo.

