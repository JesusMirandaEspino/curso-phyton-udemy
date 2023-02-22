import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(ahorros)
#plt.show()

plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(1, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
#plt.show()                                # Finalmente lo mostramos

plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(1, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend(loc=4)                         # Mostramos la leyenda
#plt.show()                                # Finalmente lo mostramos

plt.plot(ahorros, label="Evolución")      # Añadimos el gráfico con una label
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(1, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend(["Evolución"], loc=0)          # Mostramos la leyenda
#plt.show()                                # Finalmente lo mostramos

plt.plot(np.random.randint(100, size=[6]))
plt.plot(np.random.randint(100, size=[6]))
plt.plot(np.random.randint(100, size=[6]))
plt.xticks(mapeado, meses)
plt.xlim(1, 4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en €")
plt.legend(["Pedro", "Marta", "Ana"])
#plt.show()


df = pd.DataFrame(
    data=[
        np.random.randint(100, size=[6]),
        np.random.randint(100, size=[6]),
        np.random.randint(100, size=[6])],
    index=['Pedro', 'Marta', 'Ana'],
    columns=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'])

print(df)

# Veamos como queda...
#plt.plot(df)
#plt.show()

# Intercambiamos los ejes con el dataframe transpuesto
#plt.plot(df.T)
#plt.show()

# Resultado final utilizando un DataFrame
plt.plot(df.T)
plt.xlim(1, 4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en €")
plt.legend(['Pedro', 'Marta', 'Ana'])
#plt.show()

# Tablas de multiplicar del 1 al 10
for t in range(1, 11):
    plt.plot(
        range(1, 11),                   # Eje X
        [t * n for n in range(1, 11)],  # Eje Y
        label=f"Tabla del {t}")         # Leyenda para cada serie

plt.title('Tablas')
plt.xlabel('Número')
plt.ylabel('Resultado')
plt.legend()
plt.show()
