# Métodos de las listas

# append()
# Añade un ítem al final de la lista:
lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)
# [1, 2, 3, 4, 5, 6]

# clear()
# Vacía todos los ítems de una lista:
lista.clear()
print(lista)
# []

# extend()
# Une una lista a otra:
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
# [1, 2, 3, 4, 5, 6]

# count()
# Cuenta el número de veces que aparece un ítem:
# ["Hola", "mundo", "mundo"].count("Hola")


# index()
# Devuelve el índice en el que aparece un ítem(error si no aparece):
# ["Hola", "mundo", "mundo"].index("mundo")


# insert()
# Agrega un ítem a la lista en un índice específico:

# Primera posición(0):
l = [1, 2, 3]
l.insert(0, 0)
print(l)
# [0, 1, 2, 3]

# Penúltima posición(-1):
l = [5, 10, 15, 25]
l.insert(-1, 20)
print(l)
# [5, 10, 15, 20, 25]

# Última posición en una lista con len():
l = [5, 10, 15, 25]
n = len(l)
l.insert(n, 30)
print(l)
# [5, 10, 15, 20, 25, 30]

# Una posición fuera de rango añade el elemento al final de la lista(999):
l.insert(999, 35)
print(l)
# [5, 10, 15, 20, 25, 30, 35]

# pop()
# Extrae un ítem de la lista y lo borra:
l = [10, 20, 30, 40, 50]
print(l.pop())
print(l)
# 50
# [10, 20, 30, 40]

# Podemos indicarle un índice con el elemento a sacar(0 es el primer ítem):
print(l.pop(0))
print(l)
# 10
# [20, 30, 40]

# remove()
# Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:
l = [20, 30, 30, 30, 40]
l.remove(30)
print(l)
# [20, 30, 30, 40]

# reverse()
# Le da la vuelta a la lista actual:
l.reverse()
print(l)
# [40, 30, 30, 20]
# Las cadenas no tienen el método .reverse() pero podemos simularlo haciendo unas conversiones:
lista = list("Hola mundo")
lista.reverse()
cadena = "".join(lista)
print(cadena)
# 'odnum aloH'

# sort()
# Ordena automáticamente los ítems de una lista por su valor de menor a mayor:
lista = [5, -10, 35, 0, -65, 100]
lista.sort()
print(lista)
# [-65, -10, 0, 5, 35, 100]

# Podemos utilizar el argumento reverse = True para indicar que la ordene del revés:
lista.sort(reverse=True)
print(lista)
# [100, 35, 5, 0, -10, -65]
