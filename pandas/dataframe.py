import pandas as pd
import numpy as np

array = np.random.uniform(-10, 10, size=[4,4])
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])
espacio = '***********************'

print(df)
print(type(df))
print(espacio)

print(df['X'])
print(espacio)

print(type(df['X']))
print(espacio)

print(df[['Y', 'Z']])
print(espacio)

df['TOTAL'] = df['W'] + df['X'] + df['Y'] + df['Z']
print(df)
print(espacio)

df.drop('TOTAL', axis=1)
print(df)
print(espacio)

df.drop('TOTAL', axis=1, inplace=True)
print(df)
print(espacio)

df.drop('D', axis=0)

print(df.loc['C'])
print(espacio)

print(df.iloc[2])
print(espacio)

print()
print(espacio)

print(df.loc['C','Z'])
print(espacio)

print(df.loc[['A', 'B'], ['W', 'Y']])
print(espacio)

print(df > 0)
print(espacio)

print(df[df['X'] > 0])
print(espacio)

print(df[df['X'] > 0][['Y', 'Z']])
print(espacio)

print(df[(df['X'] > 0) | (df['Z'] < 0)])
print(espacio)

print(df[(df['X']>0) | (df['Z'] < 0)][['W','Y']])
print(espacio)

array = np.random.uniform(-10, 10, size=[4, 4])
df = pd.DataFrame(array, index=['A', 'B', 'C', 'D'], columns=['W', 'X', 'Y', 'Z'])
df['Códigos'] = ['AA', 'BB', 'CC', 'DD']

print(espacio)
print(df)

df.set_index('Códigos')
print(df)
print(espacio)

df.set_index('Códigos', inplace=True)
print(df)
print(espacio)


