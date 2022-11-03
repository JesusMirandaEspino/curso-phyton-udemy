# Pilas
# Son colecciones de elementos ordenados que únicamente permiten dos acciones:

# Añadir un elemento a la pila.
# Sacar un elemento de la pila.
# La peculiaridad es que el último elemento en entrar es el primero en salir. En inglés se conocen como estructuras LIFO(Last In First Out).

# Las podemos crear como listas normales y añadir elementos al final con el append():
pila = [3, 4, 5]
pila.append(6)
pila.append(7)
print(pila)


# Para sacar los elementos utilizaremos el método pop(). Al utilizareste método devolveremos el último elemento, pero también lo borraremos:
print(pila.pop())
print(pila)


# Si queremos trabajar con él deberíamos asignarlo a una variable:
numero = pila.pop()
print(numero)


# Si vamos sacando elementos llegará un momento en que la pila estará vacía y dará error porque no podrá sacar nada más:
pila.pop()
pila.pop()
pila.pop()
pila.pop()
