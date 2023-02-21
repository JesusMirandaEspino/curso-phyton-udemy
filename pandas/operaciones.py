import pandas as pd
import numpy as np

divisor = '-----------------'
# Rango de fechas para usar de índice en un dataframe
index = pd.date_range("7/15/2022", periods=20)

print(index)
print(divisor)

# Lo utilizamos para rellenar un df con valores aleatorios
df = pd.DataFrame(np.random.randn(20, 4), index=index, columns=["A", "B", "C", "D"])
print(df)
print(divisor)

# Primeras filas (cabeza)
print(df.head())
print(divisor)

# Primeras tres filas
print(df.head(3))
print(divisor)

# Últimas filas (cola)
print(df.tail())
print(divisor)

# Últimas tres filas
print(df.tail(3))
print(divisor)

# Definimos un DataFrame con información de diferentes tipos
df = pd.DataFrame({
    'enteros': [100, 200, 300, 400],
    'decimales': [3.14, 2.72, 1.618, 3.14],
    'cadenas': ['hola', 'adiós', 'hola', 'adiós']})
print(df)
print(divisor)

# Array de valores únicos de una columna
print(df['cadenas'].unique())
print(divisor)


print(df)
print(divisor)
