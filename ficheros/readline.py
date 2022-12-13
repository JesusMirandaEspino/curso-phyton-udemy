from io import open
# Podemos usar el método readlines() del fichero para generar una lista con las líneas:


fichero = open('fichero.txt', 'r')

# Leempos creando una lista de líneas
texto = fichero.readlines()

fichero.close()
print(texto)

# ['Una línea con texto\n', 'Otra línea con texto\n']


# También se puede leer un fichero utilizando la instrucción estándar with de la siguiente forma:


with open("fichero.txt", "r") as fichero:
    for linea in fichero:
        print(linea)

# Una línea con texto

# Otra línea con texto

fichero.close()
