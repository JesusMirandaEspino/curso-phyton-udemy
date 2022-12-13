from io import open
# Extensión
# Este modo nos permite añadir datos al final de un fichero:

    # Ruta donde leeremos el fichero, a indica extensión (puntero al final)
fichero = open('fichero.txt', 'a')

fichero.write('\nOtra línea más abajo del todo')

fichero.close()
# La variante 'a+' permite crear el fichero si no existe:


fichero = open('fichero_inventado.txt', 'a+')
# Manejando el puntero
# Es posible posicioar el puntero en el fichero manualmente usando el método seek e indicando un número de caracteres para luego leer una cantidad de caracteres con el método read:


fichero = open('fichero.txt', 'r')
fichero.seek(0)   # Puntero al principio
fichero.read(10)  # Leemos 10 carácteres

# 'Una línea '
fichero.close()
