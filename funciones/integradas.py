# Funciones integradas
# La librería estándar de Python incluye muchas funciones. Las hay para hacer conversiones entre tipos, matemáticas, utilidades...

# Aquí un resumen de las más utilizadas incluyendo algunas que ya conocemos:
# int()
# Transforma una cadena a un entero(si no es posible da error):
n = int("10")
print(n)

# float()
# Transforma una cadena a un flotante(si no es posible da error):
f = float("10.5")
print(f)

# str()
# Transforma cualquier valor a una cadena:
c = "Un texto y dos números " + str(10) + " y " + str(3.14)
print(c)

# Un texto y dos números 10 y 3.14
# bin()
# Conversión de entero a binario:
bin(10)
# '0b1010'

# hex()
# Conversión de entero a hexadecimal:
hex(10)
# '0xa'

# int(numero, base)
# Reconversión a entero(base 10):
print(int('0b1010', 2))
print(int('0xa', 16))

# abs()
# Valor absoluto de un número(distancia):
abs(-10)

# round()
# Redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza:
print(round(5.5))
print(round(5.4))

# eval()
# Evalúa una cadena como una expresión, acepta variables si se han definido anteriormente:
eval('2 + 5')
n = 10
eval('n * 10 - 5')

# len()
# Longitud de una colección o cadena:
print(len("Una cadena"))
print(len([]))

# help()
# Invoca el menú de ayuda del intérprete de Python:
help()
