import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print('--------------------')
print(arr.T)
print('--------------------')
print(arr.T.T)
print('++++++++++++++++++++')

arr.swapaxes(0,1)
print(arr)
print('++++++++++++++++++++')

arr_3d = np.arange(8).reshape(2,2,2)
print(arr_3d)
print('*+++++++++++++++++++')
print(arr_3d.T)
print('*+++++++++++++++++++')


arr_3d.swapaxes(0, 2)
print(arr_3d)
print('********************')

arr_3d.swapaxes(0,1)
print(arr_3d)
