import numpy as np
import matplotlib.pyplot as plt

# Gráfico lineal

x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.plot(x, y)
plt.show()


# Gráfico de líneas verticales
plt.stem(x, y)
plt.show()


# Gráfico de series comparadas
for t in range(1, 11)[::-1]:
    plt.fill_between(
        range(1, 11),
        [t * n for n in range(1, 11)],
        label=f"Tabla del {t}"
    )

plt.title("Tablas de multiplicar")
plt.legend(loc='upper left')
plt.show()


# Gráfico circular o de pastel
# https://es.wikipedia.org/wiki/Anexo:Destinos_tur%C3%ADsticos_mundiales

turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
paises = ['Francia', 'España', 'EEUU', 'China', 'Italia',
        'México', 'Reino Unido', 'Turquía', 'Alemania', 'Tailandia']

explode = [0, 0.2, 0, 0, 0, 0.5, 0, 0, 0, 0]  # Destacar algunos

plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2017')
plt.pie(turistas, labels=paises, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()


# Gráfico de cajas y bigotes
# https://es.wikipedia.org/wiki/Estatura

jap = np.random.uniform(160, 170, 100)
hol = np.random.uniform(171, 180, 100)
ale = np.random.uniform(168, 176, 100)

# Cambio los colores para que se vea bien en VSC con tema oscura
plt.boxplot([jap, hol, ale], notch=True, patch_artist=True)
plt.xticks([1, 2, 3], ['Japón', 'Países Bajos', 'Alemania'])
plt.ylabel('Estatura media (cm)')
plt.show()


# Gráfico histograma
alturas = np.random.uniform(170, 180, 1000)

# El rango se define con bins, debe ser menor que el número de muestras
plt.hist(alturas, bins=10, edgecolor='black')

plt.title("Distribución de 1000 alturas")
plt.xlabel("Altura media (cm)")
plt.ylabel("Muestras")
plt.show()


# Gráfico histograma gaussiano
numeros = np.random.normal(size=1000)

plt.hist(numeros, bins=10, edgecolor='black')

plt.title("Histograma Gaussiano")
plt.show()


# Gráfico de barras
# http://www.datosmacro.com/prima-riesgo/espana

fechas = ['25/06/2022', '27/06/2022', '28/06/2022', '29/06/2022', '30/06/2022']
primas = [111, 111, 109, 107, 108]

plt.bar(range(5), primas, edgecolor='black')

plt.xticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.ylim(min(primas)-1, max(primas)+1)
plt.show()


# Gráfico de barras horizontales
# http://www.datosmacro.com/prima-riesgo/espana

fechas = ['25/06/2022', '27/06/2022', '28/06/2022', '29/06/2022', '30/06/2022']
primas = [111, 111, 109, 107, 108]

plt.barh(range(5), primas, edgecolor='black')

plt.yticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.xlim(min(primas)-1, max(primas)+1)
plt.show()


# Gráfico de escaleras
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.step(x, y)
plt.show()
