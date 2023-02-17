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

# los borramos de la memoria
del(arr_1)
del(arr_2)

# los cargamos desde el fichero binario
arrays = np.load('arrays.npz')
print(arrays)

print(arrays['arr_1'])
print(arrays['arr_2'])

# creamos un array de prueba
arr_3 = np.random.randint(-10, 10, [3, 3])
print(arr_3)

# lo guardamos en un fichero de texto
np.savetxt('arr_3.txt', arr_3)

# lo borramos de la memoria
del(arr_3)

# lo cargamos indicando el separador (si lo hemos cambiado)
arr_3 = np.loadtxt('arr_3.txt', delimiter=',')

print(arr_3)
