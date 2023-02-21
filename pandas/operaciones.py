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

# Contador de valores únicos de una columna
print(df['cadenas'].nunique())
print(divisor)


# Dataframe con los de valores únicos y su contador de una columna
print(df['cadenas'].value_counts())
print(divisor)

# Método interno de las Series columna
print(df['decimales'].sum())
print(divisor)

# Aplicar una función predefinida
print(df['cadenas'].apply(len))
print(divisor)

# Aplicar una función definida
def doblar(n):
    return n*2
print(df['enteros'].apply(doblar))
print(divisor)

# Aplicar una función anónima
print(df['enteros'].apply(lambda n: n/3))
print(divisor)

# Borrar permanentemente una columna
del df['decimales']
print(df)
print(divisor)

# Índices de las columnas
print(df.columns)
print(divisor)

# Índice de las filas
print(df.index)
print(divisor)

# Ordenar por columna (inplace=False por defecto)
print(df.sort_values(by='enteros'))
print(divisor)

# Ordenar por columna inversamente (inplace=False por defecto)
print(df.sort_values(by='enteros', ascending=False))
print(divisor)
