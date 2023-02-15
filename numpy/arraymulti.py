import numpy as np

arr_2d = np.array(([0,5,10], [15,20,25], [30,35,40]))

print(arr_2d)
print(arr_2d[0])
print(arr_2d[0][0])
print(arr_2d[-1][-1])

arr_2d[-1][0] = 99
print(arr_2d)


print(arr_2d[:,:])
print(arr_2d[:2, :])
print(arr_2d[:, :1])

arr_2d[:, 1:2] = 99
print(arr_2d)

arr_2d[-1, :] = 88
print(arr_2d)

arr_2d = np.zeros((5, 10))
print(arr_2d)

arr_2d[[0, 2, -1]] = 5
print(arr_2d)

arr_2d = np.array(([0, 5, 10], [15, 20, 25], [30, 35, 40]))
for fila in arr_2d:
    print(fila)


for i, fila in enumerate(arr_2d):
    for j, columna in enumerate(fila):
        arr_2d[i][j] = len(fila) * i + j

print(arr_2d)

arr_1d = np.array([1, 2])
print(arr_1d)

arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)


arr_4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(arr_4d)

arr_3d = np.zeros([2, 2, 2])
print(arr_3d)

arr_4d = np.ones([2, 2, 2, 2])
print(arr_4d)

arr_2d = np.arange(9).reshape(3,3)
print(arr_2d)

arr_3d = np.arange(27).reshape(3,3,3)
print(arr_3d)
