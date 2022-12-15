# Manejando el puntero
# Es posible posicioar el puntero en el fichero manualmente usando el método seek e indicando un número de caracteres para luego leer una cantidad de caracteres con el método read:

from io import open

fichero = open('fichero.txt','r')
fichero.seek(0)   # Puntero al principio
fichero.read(10)  # Leemos 10 carácteres

# 'Una línea '
# Para posicionar el puntero justo al inicio de la segunda línea, podríamos ponerlo justo en la longitud de la primera:

fichero = open('fichero.txt','r')
fichero.seek(0)

# Leemos la primera línea y situamos el puntero al principio de la segunda
fichero.seek( len(fichero.readline()) )

# Leemos todo lo que queda del puntero hasta el final
fichero.read()

# '\nOtra línea con texto\nOtra línea más abajo del todo'
# Lectura con escritura
# Se puede abrir un fichero en modo lectura con escritura, pero éste debe existir préviamente. Además por defecto el puntero estará al principio y si escribimos algo sobreescribiremos el contenido actual, así que prestad atención a los saltos de línea y caracteres especiales:


# Creamos un fichero de prueba con 4 líneas
fichero = open('fichero2.txt','w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()

# Lo abrimos en lectura con escritura y escribimos algo
fichero = open('fichero2.txt','r+')
fichero.write("0123456")

# Volvemos a ponter el puntero al inicio y leemos hasta el final
fichero.seek(0)
fichero.read()
fichero.close()

# '0123456\nLínea 2\nLínea 3\nLínea 4'
# Modificar una línea
# Para lograr este fin lo mejor es leer todas las líneas en una lista, modificar la línea en la lista, posicionar el puntero al principio y reescribir de nuevo todas las líneas:


fichero = open('fichero2.txt','r+')
texto = fichero.readlines()

# Modificamos la línea que queramos a partir del índice
texto[2] = "Esta es la línea 3 modificada\n"

# Volvemos a ponter el puntero al inicio y reescribimos
fichero.seek(0)
fichero.writelines(texto)
fichero.close()

# Leemos el fichero de nuevo
with open("fichero2.txt", "r") as fichero:
    print(fichero.read())

# 0123456
# Línea 2
# Esta es la línea 3 modificada
# Línea 4
