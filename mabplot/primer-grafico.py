import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ahorros = [52, 104, 32, 65, 15, 76]
plt.plot(ahorros)

ahorros = np.random.randint(100, size=[6])
plt.plot(ahorros)

df = pd.DataFrame(ahorros, index=['Enero','Febrero','Marzo','Abril','Mayo','Junio'])
plt.plot(df)

df.plot()
