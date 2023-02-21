import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

divi = '+++++++++++++++++'

# Definimos un dataframe con datos de ejemplos
df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])
print(df)
print(divi)

df.to_csv('datos.csv', index=False)
# Borramos el df de la memoria
del(df)
df = pd.read_csv('datos.csv')
print(df)
print(divi)

df.to_json('datos.json')
# Borramos el df de la memoria
del(df)
df = pd.read_json('datos.json')
print(df)
print(divi)

df.to_excel('datos.xlsx', sheet_name='Sheet1', index=False)
# Borramos el df de la memoria
del(df)
df = pd.read_excel('datos.xlsx', sheet_name='Sheet1')
print(df)
print(divi)


# Realizamos un scrapping de una tabla de la wikipedia
df = pd.read_html('https://web.archive.org/web/20220717170349/https://en.wikipedia.org/wiki/List_of_countries_by_past_fertility_rate')
print(df[2])
print(divi)

# Guardamos el dataframe
fertility_rate = df[2]
fertility_rate.head()
# Renombramos la primera columna para que sea más fácil consultarla
fertility_rate.rename(columns={'Country/dependent territory': 'Country'}, inplace=True)
print(fertility_rate)
print(divi)

# Índice de natalidad por país entre los años 2010-2015
print(fertility_rate[["Country", "2010–2015"]])
print(divi)

# Misma consulta aplicando el styler para esconder la primera columna
print(fertility_rate[["Country", "2010–2015"]].head().style.hide(axis=0))
print(divi)

# Índice de natalidad por país entre los años 1985–1990 ordenado de más a menos (primeros resultados)
print(fertility_rate[["Country", "1985–1990"]].sort_values(by="1985–1990", ascending=False).head().style.hide(axis=0))
print(divi)

# Índice de natalidad por país entre los años 1985–1990 ordenado de más o menos (últimos resultados)
print(fertility_rate[["Country", "1985–1990"]].sort_values(by="1985–1990", ascending=False).tail().style.hide(axis=0))
print(divi)

# Vamos a transformar todas las columnas desde la segunda hasta la última a valores númericos
print(fertility_rate[["Country", "1985–1990"]].sort_values(by="1985–1990", ascending=False).tail().style.hide(axis=0))
print(divi)

# Ahora podemos consultar la media del índice de natalidad para cada año
print(fertility_rate.mean()[1:])
print(divi)

plt.rcParams["figure.figsize"] = 10, 5
print(fertility_rate.mean()[1:].plot(kind='line', xlabel="Períodos", ylabel="Media de natalidad mundial"))
print(divi)
