import numpy as np

# arrays de prueba
arr_1 = np.arange(1,6)
arr_2 = np.array([-3,7,3,13,0])

print(np.add(arr_1, arr_2))
print('------------')
print(np.subtract(arr_2, arr_1))
print('------------')
print(np.sqrt(arr_1))
print('************')
print(np.power(arr_1, 2))
print('************')
print(np.sign(arr_1))
print('++++++++++++')


print(np.sin(arr_1))
print('++++++++++++')
print(np.cos(arr_1))
print('____________')
print(np.tan(arr_1))
print('____________')
print(np.tan(arr_1))
print('............')
print(np.deg2rad(arr_1))
print('............')
print(np.rad2deg(arr_1))

print('#############')
print(np.maximum(arr_1, arr_2))
print('#############')
print(np.minimum(arr_1, arr_2))
print('#------------#')
print(np.equal(arr_1, arr_2))
print('#------------#')
print(np.greater(arr_1, arr_2))

# tercer array de prueba
arr_3 = np.array([3.14, 2.57, -6.4, 0.47, 5.5])

print('#++++++++++++#')
print(np.fabs(arr_3))
print('#+++++++++++++#')
print(np.ceil(arr_3))
print('#.............#')
print(np.floor(arr_3))
