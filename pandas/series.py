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

print(espacio)
print(pd.Series(array))

print(espacio)
print(pd.Series(array, etiquetas))

diccionario = {'A': 25, 'B': 50, 'C': 75, 'D': 100}
print(espacio)
print(pd.Series(diccionario))

ingresos = pd.Series([100, 300, 200], index=['enero', 'febrero', 'marzo'])
print(espacio)
print(ingresos)

print(espacio)
print(ingresos[0])
print(espacio)
print(ingresos['enero'])

gastos = pd.Series([100, 150, 250], index=['enero', 'febrero', 'marzo'])
print(espacio)
print(gastos)

total = ingresos.subtract(gastos)
print(espacio)
print(total)

print(espacio)
print(ingresos - gastos)

print(espacio)
print(type(total))
print()
print()
print()
