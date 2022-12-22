from tkinter import *
# Widget Frame(Marco)
# Los Frames son marcos contenedores de otros widgets. Pueden tener tamaño propio y 
# posicionarse en distintos lugares de otro contenedor(ya sea la raíz u otro marco):
root = Tk()

# Hijo de root, no ocurre nada
frame = Frame(root)

# Empaqueta el frame en la raíz
frame.pack()

# Como no tenemos ningún elemento dentro del frame,
# no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

# Color de fondo, background
frame.config(bg="lightblue")

# Podemos establecer un tamaño,
# la raíz se adapta al frame que contiene
frame.config(width=480, height=320)

# También podemos añadir la configuración al crear el frame:


Frame(root, width=480, height=320)
# Algo interesante de los frames es que permiten parámetros visuales utilizando atributos estándar:


frame.config(cursor="")         # Tipo de cursor
frame.config(relief="sunken")   # relieve del frame hundido
frame.config(bd=25)             # tamaño del borde en píxeles
# Pero esto no es algo único de los Frames, todos los widgets aceptan estos parámetros visuales, 
# incluso la raíz:

root.config(bg="blue")          # color de fondo, background
root.config(cursor="pirate")    # tipo de cursor (arrow defecto)
root.config(relief="sunken")    # relieve del root
root.config(bd=25)              # tamaño del borde en píxeles
# De esta forma podéis apreciar como se diferencia claramente el espacio de la raíz y el frame.


# Sin embargo, fijaros que curiosamente si hacemos la ventana grande, 
# el frame se encuentra centrado arriba al medio, eso es porque el método pack alinea el widget arriba al medio.Esta posición se conoce como la distribución del Widget y podemos cambiarla de dos formas posibles justo al empacar el frame. Con alineación[arriba, abajo, izquierda, derecha] o con anclaje[N, S, E, W, NE…]:


frame.pack(side=RIGHT)   # a la derecha al medio
frame.pack(anchor=SE)    # sudeste, abajo a la derecha

# Y no sólo eso, también podemos redimensionar un widget:


frame.pack(fill="x")                # ancho como el padre
frame.pack(fill="y")                # alto como el padre
frame.pack(fill="both")             # ambas opciones
frame.pack(fill="both", expand=1)   # expandirse para ocupar el espacio

root.mainloop()
