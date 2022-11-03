from collections import deque
# Colas
# Son colecciones de elementos ordenados que únicamente permiten dos acciones:

# Añadir un elemento a la cola.
# Sacar un elemento de la cola.
# La peculiaridad es que el primer elemento en entrar es el primero en salir. En inglés se conocen como estructuras FIFO(First In First Out).
# Debemos importar la colección deque manualmente para crear una cola:
cola = deque()
print(cola)
deque([])

# Podemos añadir elementos al crear la cola pasándolos en una lista:
cola = deque(['Hector', 'Juan', 'Miguel'])
print(cola)
deque(['Hector', 'Juan', 'Miguel'])

# Luego podemos seguir añadiéndolos utilizando el método append():
cola.append('Maria')
cola.append('Arnaldo')
print(cola)
deque(['Hector', 'Juan', 'Miguel', 'Maria', 'Arnaldo'])

# La parte interesante es a la hora de sacar los elementos, pues en esta ocasión utilizaremos el método popleft(). Hace lo mismo que pop() pero los extrae por la parte izquierda, que sería el principio de la cola:
print(cola.popleft())
print(cola)
deque(['Juan', 'Miguel', 'Maria', 'Arnaldo'])

# Además al igual que antes debemos asegurarnos de almacenar los elementos al sacarlos o los perderemos:
persona = cola.popleft()
print(persona)
print(cola)
