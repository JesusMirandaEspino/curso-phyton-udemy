import pandas as pd

divi = '+++++++++++++++++'

df1 = pd.DataFrame({'A': ['1A', '2A'], 'B': ['1B', '2B'], 'C': ['1C', '2C']}, index=[1, 2])
print(df1)
print(divi)

df2 = pd.DataFrame({'A':['3A','4A','5A'], 'B':['3B','4B','5B'], 'C':['3C','4C','5C']}, index=[3, 4, 5]) 
print(df2)
print(divi)

df3 = pd.DataFrame({'A': ['6A', '7A'], 'B': ['6B', '7B'], 'C': ['6C', '7C']}, index=[6, 7])
print(df3)
print(divi)

# Concatenar filas
print(pd.concat([df1, df2, df3]))
print(divi)

df1 = pd.DataFrame({'clave': ['K1', 'K2', 'K3'], 'A': ['1A', '2A', '3A'], 'B': ['1B', '2B', '3B']})
print(df1)
print(divi)

df2 = pd.DataFrame({'clave': ['K1', 'K2', 'K3'], 'C': ['1C', '2C', '3C'], 'D': ['1D', '2D', '3D']})
print(df2)
print(divi)

# Fusionar columnas a partir de una columna común
print(pd.merge(df1, df2, on='clave'))
print(divi)

df1 = pd.DataFrame({'A': ['1A', '2A', '3A'], 'B': ['1B', '2B', '3B']}, index=['K1', 'K2', 'K3'])
print(df1)
print(divi)

df2 = pd.DataFrame({'C': ['1C', '2C', '3C'], 'D': ['1D', '2D', '3D']}, index=['K1', 'K2', 'K3'])
print(df2)
print(divi)

# Unir columnas mediante los índices
print(df1.join(df2))
print(divi)
