import numpy as np

print(np.zeros(3))
print('-----------')
print(np.zeros([3,3]))
print('-----------')
print(np.ones([3,3]))
print('--------------')
print(np.eye(3))
print('--------------')

print(np.arange(4))
print('----------------')
print(np.arange(4.))
print('--------------')
print(np.arange(-3, 3))
print('-----------------')
print(np.arange(0, 20, 5))


# Dos arrays
arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([5, 6, 7, 8])

# Los sumamos
print(arr_1 + arr_2)
print(arr_1 - arr_2)
print(arr_1 * arr_2)
print(arr_1 * 10)
print(arr_1 * np.array(10))
print(arr_1 / arr_2)
print(arr_1 / 2)
print(1 / arr_1)
print(arr_1 ** arr_2)


arr_5 = np.array([[1, 2], [3, 4]])
arr_6 = np.array([[5, 6], [7, 8]])

print(arr_5 + arr_6)
print(arr_5 * np.array([5, 10]))



