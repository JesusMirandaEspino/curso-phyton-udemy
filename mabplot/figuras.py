# Gráficos usando figuras
import numpy as np
import matplotlib.pyplot as plt

# La figura crea un espacio donde dibujar el gráfico
fig = plt.figure()

# Añadimos los límites para crear un objeto de ejes donde dibujar
rect = (0, 0, 1, 1)
axes = fig.add_axes(rect)

# En los ejes podemos crear el gráfico mediante plt
axes.plot(np.random.randint(100,size=[6]), label="Pedro")
axes.plot(np.random.randint(100,size=[6]), label="Marta")
axes.plot(np.random.randint(100,size=[6]), label="Ana")

# La mayor diferencia es a la hora de personalizar el gráfico,
# refieriéndonos a los métodos con la palabra set antes del nombre
axes.set_ylim(0, 100)
axes.set_xlabel("Meses")
axes.set_ylabel("Cantidad en €")
axes.set_title("Ahorros del primer semestre")


# El mapeado de nombres ahora requiere usar dos métodos diferentes
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))
axes.set_xticks(mapeado)
axes.set_xticklabels(meses)


# Finalmente mostramos la figura resultante
print(fig)


fig.set_size_inches(2, 2)
fig.set_dpi(100)
print(fig)


# Probamos con un tamaño mayor
fig.set_size_inches(4, 3)
fig.set_dpi(100)
print(fig)


fig.savefig('grafico.png', bbox_inches='tight', dpi=100)


# Creamos una figura para almacenar varios subgráficos
fig, axes = plt.subplots(3, 3)
fig.suptitle('Subgráficos en figuras', size=15)

# Dibujando 3x3=9 subgráficos
for i in range(3):
    for j in range(3):
        axes[i, j].plot(np.random.randint(100, size=6))
        axes[i, j].plot(np.random.randint(100, size=6))
        axes[i, j].plot(np.random.randint(100, size=6))
        axes[i, j].set_ylim(0, 100)
        axes[i, j].set_title(f'Ejes [{i}, {j}]')


fig.set_size_inches(12, 12)
print(fig)


fig.savefig('subgraficos.png', bbox_inches='tight', dpi=100)
