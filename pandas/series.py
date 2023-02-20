import numpy as np
import pandas as pd

etiquetas = ['A', 'B', 'C', 'D']
lista = [25, 50, 75, 100]
espacio = '***********************'

print(lista)
print(pd.Series(data=lista))
print(espacio)

print(pd.Series(data=lista, index=etiquetas))
print(espacio)

print(pd.Series(lista, etiquetas))
print(espacio)

array = np.random.randint(50, size=4)
print(array)


print()
print()
print()
print()
print()
