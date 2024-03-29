# Normalmente se suele importar numpy como np
import numpy as np

# Podemos crear un arreglo a partir de
array = np.array([1, 2, 3, 4, 5])

print(array)
type(array)


print(array.ndim)
print(array.shape)


array2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])


print(array2)
print(array2.ndim)
print(array2.shape)


array3 = np.array([1, 2, 3, 4, 5])
array4 = np.array([1, 2, 3, 4, 5, 6.1234])
array5 = np.array(["Hola", "que", "tal"])
array6 = np.array(["Hola", 1234, 3.1415])
print(array3.dtype)
print(array4.dtype)
print(array5.dtype)
print(array6.dtype)
