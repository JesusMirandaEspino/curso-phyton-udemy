# Sentencia for (para)
# for con listas
# Para ilustrar la utilidad de esta sentencia vamos a empezar mostrando como recorrer los elementos de una lista utilizando While:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice += 1

# Lo mismo utilizando el For:


for numero in numeros:  # Para [variable] en [lista]
    print(numero)

# ¿Mucho más fácil no?
# Para asignar un nuevo valor a los elementos de una lista mientras la recorremos, podríamos intentar asignar al número el nuevo valor:


for numero in numeros:
    numero *= 10


# Sin embargo, esto no funciona. La forma correcta de hacerlo es haciendo referencia al índice de la lista en lugar de la variable:


indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[indice] *= 10
    indice += 1


# Podemos utilizar la función enumerate() para conseguir el índice y el valor en cada iteración fácilmente:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 10


# for con cadenas
# Funciona exactamente igual que con las listas, pero con caracteres en lugar de elementos:


cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)

# Pero debemos recordar que las cadenas son inmutables:


for i, c in enumerate(cadena):
    cadena[i] = "*"

cadena = "Hola amigos"
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2


# La función range()
# Sirve para generar una lista de números que podemos recorrer fácilmente, pero no ocupa memoria porque se interpreta sobre la marcha:


for i in range(10):
    print(i)

# Esta función devuelve un generador, una estructura manejada en tiempo de ejecución:


range(10)

range(0, 10)
# Si queremos conseguir la lista literal podemos transformar el range a una lista:


list(range(10))

