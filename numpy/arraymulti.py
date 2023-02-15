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
print(arr_2d)
print(arr_2d)

