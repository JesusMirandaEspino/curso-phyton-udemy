import numpy as np

# generamos un array de 2*3 con números aleatorios
arr = np.arange(1,7).reshape(2,3)
print(arr)

# sumatorio
print(arr.sum())

# media
print(arr.mean())

# desviación estándard
print(arr.std())

# varianza
print(arr.var())


# generamos un nuevo array aleatorio
arr = np.random.randint(-10, 10, [3, 3])
print(arr)

# Ordenar elementos horizontalmente
arr.sort()
print(arr)

# Ordenar elementos verticalmente
arr.sort(0)
print(arr)

