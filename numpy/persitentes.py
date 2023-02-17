import numpy as np

# creamos un array aleatorio
arr_1 = np.random.randint(0, 4, [3, 3])
print(arr_1)

# lo guardarmos en un binario con extensión .npy
np.save('arr_1.npy', arr_1)

# borramos el array de la memoria para asegurarnos de que ya no existe
del(arr_1)
# print(arr_1)

# lo cargamos desde el fichero binario
arr_1 = np.load('arr_1.npy')
print(arr_1)

# creamos otro array aleatorio
arr_2 = np.random.randint(-4, 0, [3, 3])
print(arr_2)

# utilizaremos savez para guardar de forma comprimida con la extensión .npz
# debemos especificar una clave para cada array que queramos guardar
np.savez('arrays.npz', arr_1=arr_1, arr_2=arr_2)
