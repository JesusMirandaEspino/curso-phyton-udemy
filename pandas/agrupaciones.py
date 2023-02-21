import pandas as pd
div = '*****************'

# Creamos un diccionario con mucha información
ventas = {
    'Comercial': ['Juan', 'María', 'Manuel', 'Vanesa', 'Ana', 'Marcos'],
    'Empresa': ['Movistar', 'Jazztel', 'Movistar', 'Jazztel', 'Vodafone', 'Vodafone'],
    'Primas': [300, 220, 140, 70, 400, 175]
}


df = pd.DataFrame(ventas)
print(df)
print(div)

df.groupby('Empresa')
print(df)
print(div)

por_empresa = df.groupby("Empresa")
# Prima media por empresa
print(por_empresa.mean())
print(div)

# Lo mismo sin guardar el objeto en una variable
df.groupby('Empresa').mean()
print(df)
print(div)

# Desviación estándar (dispersion del conjunto)
print(por_empresa.std())
print(div)

# Primas mínimas (error)
print(por_empresa.min())
print(div)

# ID de las primas mínimas
print(por_empresa['Primas'].idxmin())
print(div)

# Usamos las ID de las primas máximas como fuente del df
print(df.loc[por_empresa['Primas'].idxmin()])
print(div)

# Primas mínimas
print(df.loc[por_empresa['Primas'].idxmax()])
print(div)

# Contador de primas por empresa
print(por_empresa.count())
print(div)

# Reporte de analíticas descriptivas por empresa
print(por_empresa.describe())
print(div)

# Reporte transpuesto (filas por columnas)
print(por_empresa.describe().transpose())
print(div)

# Reporte transpuesto de una sola empresa
print(por_empresa.describe().transpose()['Movistar'])
print(div)
