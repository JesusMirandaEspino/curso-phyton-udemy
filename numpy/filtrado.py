import numpy as np

# generamos un array con números aleatorios repetidos
arr = np.random.randint(0, 10, 40)

print(arr)
# aplicamos el filtro unique
print(np.unique(arr))
print(np.in1d([-1, 4, 8, 12], arr))


# generamos un array con números aleatorios
arr_1 = np.random.uniform(-5, 5, size=[3, 2])
print(arr_1)

# creamos un filtro que establece los negativos a 0
arr_2 = np.where(arr_1 < 0, 0, arr_1)
print(arr_2)

# añadimos otro filtro que establece los positivos a 1
arr_2 = np.where(arr_2 > 0, True, arr_2)
print(arr_2)


spaceIcons = '***********'
arr_bool=np.array([True, True, True, False])
print(spaceIcons)
print(arr_bool.all())
print(spaceIcons)
print(arr_bool.any())

# definimos un array de booleanos 2d
arr_bool_2d = np.array(
    [
        [False, True],
        [False, True],
        [False, True]
    ]
)

print(spaceIcons)
print(arr_bool_2d)
print(spaceIcons)
print(arr_bool_2d.all(0))
print(spaceIcons)
print(arr_bool_2d.any(1))

