import numpy as np

arr = np.arange(0, 50, 5)

print('+++++++++++++++')
print(arr)
print(arr[0])
print(arr[4])
print(arr[-1])
arr[-1] = 99
print(arr)
print('+++++++++++++++')

arr2 = arr[:]
print(arr2)
print('+++++++++++++')


print(arr2)
print(arr[:3])
arr[1:-1] = 50
print(arr)
print('+++++++++++++++')

arr = np.arange(0, 30, 3)
print(arr)
print('----------------')

sub_arr = arr[0:4]
print(sub_arr)
print('----------------')

sub_arr[:] = 99
print(arr)
print('----------------')


arr = np.arange(0, 30, 3)
sub_arr = arr[0:4].copy()
sub_arr[:] = 99
print('-------------------')

print(sub_arr)
print(arr)
print('--------------------')
