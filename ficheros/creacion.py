# Ficheros de texto
# Hay varias formas de abrir un fichero, la más común es utilizando la función open del módulo io.

# Creación y escritura
from io import open

texto = "Una línea con texto\nOtra línea con texto"

# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('fichero.txt','w')

# Escribimos el texto
fichero.write(texto)

# Cerramos el fichero
fichero.close()



