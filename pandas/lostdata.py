import pandas as pd
import numpy as np

espacio = '***********************'

df = pd.DataFrame({
    'A': [7, 8, -6, 8],
    'B': [12, np.nan, 1, np.nan],
    'C': [4, np.nan, np.nan, np.nan],
    'D': [4, np.nan, -2, -10]})

print(df)
print(espacio)

print(df.isnull())
print(espacio)

print(df.dropna())
print(espacio)

print(df.dropna(axis=1))
print(espacio)

print(df.dropna(thresh=2))
print(espacio)

print(df.dropna(thresh=3))
print(espacio)

print(df.fillna(value=0))
print(espacio)

print(df['B'].fillna(value=df['B'].min()))
print(espacio)
