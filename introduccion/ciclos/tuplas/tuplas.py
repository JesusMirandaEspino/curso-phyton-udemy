# Tuplas
# Son unas colecciones muy parecidas a las listas con la peculiaridad de que son inmutables:
tupla = (100, "Hola", [1, 2, 3], -50)
print(tupla)


# Indexación y slicing
print(tupla)
print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])

# Inmutabilidad
tupla[0] = 50


# Función len()
# Igual que si fuera una lista podemos utilizarla para saber la longitud de una tupla:
print(len(tupla))
print(len(tupla[2]))


# Métodos integrados
# index()
# Sirve para buscar un elemento y saber su posición en la tupla:
tupla.index(100)
tupla.index('Hola')

# Da error si no se encuentra:
tupla.index('Otro')


# count()
# Sirve para contar cuantas veces aparece un elemento en una tupla:
tupla.count(100)
tupla.count('Algo')
tupla = (100, 100, 100, 50, 10)
tupla.count(100)

# append() ?
# Al ser inmutables, las tuplas no disponen de métodos para modificar su contenido:
tupla.append(10)

