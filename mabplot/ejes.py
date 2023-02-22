import numpy as np
import matplotlib.pyplot as plt

# Generamos un array con ahorros de prueba
ahorros = np.random.randint(100, size=6)

# Gráficamos sin etiquetas
plt.plot(ahorros)


# Definimos una lista con los meses para el eje horizontal
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']

# Mapeamos un rango de índices para el eje horizontal
plt.plot(ahorros)
plt.xticks([0,1,2,3,4,5], meses)

plt.plot(ahorros)
plt.xticks(range(len(meses)), meses)
plt.show()

y = np.random.randint(20, size=[6])
plt.plot(y)
plt.show()


x = ["A", "B", "C", "D", "E", "F"]
plt.plot(x, y)
plt.show()


plt.plot(y, x)
plt.show()


x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()
