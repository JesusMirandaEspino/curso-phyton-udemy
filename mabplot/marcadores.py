import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

arr_pedro = np.random.randint(100, size=[6])
arr_marta = np.random.randint(100, size=[6])
arr_ana = np.random.randint(100, size=[6])

# Configuración de las líneas
plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="5")
plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="4")
plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="3")
plt.xticks(mapeado, meses)
plt.legend()
plt.show()


# Configuración de los marcadores
plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="2",
        marker="o", markersize="10", markeredgewidth="2", markerfacecolor="yellow", markeredgecolor="red")

plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="2",
        marker="*", markersize="15", markeredgewidth="2", markerfacecolor="cyan", markeredgecolor="#0000ff")

plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="2",
        marker="D", markersize="10", markeredgewidth="2", markerfacecolor="lime", markeredgecolor="green")

plt.xticks(mapeado, meses)
plt.legend()
plt.show()
