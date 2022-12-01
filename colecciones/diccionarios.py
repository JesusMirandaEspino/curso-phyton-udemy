# Métodos de los diccionarios

colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}

# get()
# Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto:
print(colores.get('negro', 'no se encuentra'))
# 'no se encuentra'

# keys()
# Genera una lista en clave de los registros del diccionario:
print(colores.keys())
# dict_keys(['amarillo', 'azul', 'verde'])

# values()
# Genera una lista en valor de los registros del diccionario:
print(colores.values())
# dict_values(['yellow', 'blue', 'green'])

# items()
# Genera una lista en clave-valor de los registros del diccionario:
print(colores.items())
# dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])

for clave, valor in colores.items():
    print(clave, valor)
# amarillo yellow
# azul blue
# verde green

# pop()
# Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto:
print(colores.pop("amarillo", "no se ha encontrado"))
#'yellow'

print(colores.pop("negro", "no se ha encontrado"))
# 'no se ha encontrado'

# clear()
# Borra todos los registros de un diccionario:
colores.clear()
print(colores)
# {}
