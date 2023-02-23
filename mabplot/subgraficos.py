import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

arr_pedro = np.random.randint(100, size=[6])
arr_marta = np.random.randint(100, size=[6])
arr_ana = np.random.randint(100, size=[6])

plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="2",
        marker="o", markersize="10", markeredgewidth="2", markerfacecolor="yellow", markeredgecolor="red")
plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="2",
        marker="*", markersize="15", markeredgewidth="2", markerfacecolor="cyan", markeredgecolor="#0000ff")
plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="2",
        marker="D", markersize="10", markeredgewidth="2", markerfacecolor="lime", markeredgecolor="green")
plt.xticks(mapeado, meses)
plt.legend()
plt.show()


# Tabla 1x3 y dibujaremos en la celda 1
plt.subplot(1, 3, 1)
plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="2",
         marker="o", markersize="10", markeredgewidth="2", markerfacecolor="yellow", markeredgecolor="red")
plt.xticks(mapeado, meses)
plt.legend()

# Tabla 1x3 y dibujaremos en la celda 2
plt.subplot(1, 3, 2)
plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="2",
        marker="*", markersize="15", markeredgewidth="2", markerfacecolor="cyan", markeredgecolor="#0000ff")
plt.xticks(mapeado, meses)
plt.legend()

# Tabla 1x3 y dibujaremos en la celda 3
plt.subplot(1, 3, 3)
plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="2",
        marker="D", markersize="10", markeredgewidth="2", markerfacecolor="lime", markeredgecolor="green")
plt.xticks(mapeado, meses)
plt.legend()

# Dibujamos el conjunto
plt.show()


plt.rcParams["figure.figsize"] = (15,5)  # pulgadas de ancho y alto


# Tabla 1x3 y dibujaremos en la celda 1
plt.subplot(1, 3, 1)
plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="2",
         marker="o", markersize="10", markeredgewidth="2", markerfacecolor="yellow", markeredgecolor="red")
plt.xticks(mapeado, meses)
plt.legend()

# Tabla 1x3 y dibujaremos en la celda 2
plt.subplot(1, 3, 2)
plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="2",
        marker="*", markersize="15", markeredgewidth="2", markerfacecolor="cyan", markeredgecolor="#0000ff")
plt.xticks(mapeado, meses)
plt.legend()

# Tabla 1x3 y dibujaremos en la celda 3
plt.subplot(1, 3, 3)
plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="2", marker="D",
        markersize="10", markeredgewidth="2", markerfacecolor="lime", markeredgecolor="green")
plt.xticks(mapeado, meses)
plt.legend()

# Dibujamos el conjunto
plt.show()


# Cambiamos el tamaño de los gráficos generados
plt.rcParams["figure.figsize"] = (9, 9)

# Dibujando 9 subgráficos
plt.suptitle('Subgráficos', size=15)
for i in range(9):
    plt.subplot(3, 3, i+1)  # Tabla 3x3
    plt.plot(np.random.randint(100, size=[6]))
    plt.plot(np.random.randint(100, size=[6]))
    plt.ylim(0, 100)
