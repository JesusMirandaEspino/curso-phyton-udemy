import math
# Módulo math
# Este módulo contiene un buen puñado de funciones para manejar números, 
# hacer redondeos, sumatorios precisos, truncamientos... además de constantes.

# Redondeos
print(math.floor(3.99))  # Redondeo a la baja (suelo)
print(math.ceil(3.01))   # Redondeo al alta (techo)

# 3
# 4

# Sumatorio mejorado
numeros = [0.9999999, 1, 2, 3]
print(math.fsum(numeros))
# 6.9999999

# Trucamiento
print(math.trunc(123.45))
# 123

# Potencias y raices
math.pow(2, 3)  # Potencia con flotante
math.sqrt(9)    # Raíz cuadrada (square root)

# TODO 8.0
# TODO 3.0
# Constantes

print(math.pi)  # Constante pi
print(math.e)   # Constante e

# TODO 3.141592653589793
# TODO 2.718281828459045
