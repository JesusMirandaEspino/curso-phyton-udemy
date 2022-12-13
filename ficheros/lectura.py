# Lectura

from io import open

# Ruta donde leeremos el fichero, r indica lectura (por defecto ya es r)
fichero = open('fichero.txt', 'r')

# Lectura completa
texto = fichero.read()

# Cerramos el fichero
fichero.close()

print(texto)

# Una línea con texto
# Otra línea con texto
