import numpy as np
import matplotlib.pyplot as plt


ahorros = np.random.randint(50, 100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.show()                  # Finalmente lo mostramos

# Límites verticales
plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.ylim(0, 100)            # Configuramos el límite vertical
plt.show()                  # Finalmente lo mostramos

# Límites horizontales
plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.xlim(1, 4)              # Configuramos el límite horizontal
plt.ylim(0, 100)            # Configuramos el límite vertical
plt.show()                  # Finalmente lo mostramos
