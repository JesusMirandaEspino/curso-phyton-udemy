# Argumentos por posición
# Cuando enviamos argumentos a una función, estos se reciben por orden en los parámetros definidos. Se dice por tanto que son argumentos por posición:
def resta(a, b):
    return a - b

resta(30, 10)  # argumento 30 => posición 0 => parámetro a
# argumento 10 => posición 1 => parámetro b
# Argumentos por nombre
# Sin embargo es posible evadir el orden de los parámetros si indicamos durante la llamada que valor tiene cada parámetro a partir de su nombre:
resta(b=30, a=10)

# Llamada sin argumentos
# Al llamar una función que tiene definidos unos parámetros, si no pasamos los argumentos correctamente provocará un error:
# resta()

# Parámetros por defecto
# Para solucionarlo podemos asignar unos valores por defecto nulos a los parámetros, de esa forma podríamos hacer una comprobación antes de ejecutar el código de la función:

def resta(a=None, b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return   # indicamos el final de la función aunque no devuelva nada
    return a-b
resta()

# Argumentos indeterminados
# Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar a una función. En estos casos podemos utilizar los parámetros indeterminados por posición y por nombre.
# Por posición
# Para recibir un número indeterminado de parámetros por posición, debemos crear una lista dinámica de argumentos(una tupla en realidad) definiendo el parámetro con un asterisco:

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(5, "Hola", [1, 2, 3, 4, 5])

# Por nombre
# Para recibir un número indeterminado de parámetros por nombre(clave-valor o en inglés keyword args), debemos crear un diccionario dinámico de argumentos definiendo el parámetro con dos asteriscos:
def indeterminados_nombre(**kwargs):
    print(kwargs)

# indeterminados_nombre(n=5, c="Hola", l=[1, 2, 3, 4, 5])
# Al recibirse como un diccionario, podemos iterarlo y mostrar la clave y valor de cada argumento:
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(n=5, c="Hola", l=[1, 2, 3, 4, 5])

# Por posición y nombre
# Si queremos aceptar ambos tipos de parámetros simultáneamente, entonces debemos crear ambas colecciones dinámicas. Primero los argumentos indeterminados por valor y luego los que son por clave y valor:
def super_funcion(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    print("sumatorio => ", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])


super_funcion(10, 50, -1, 1.56, 10, 20, 300, nombre="Hector", edad=27)

# Los nombres args y kwargs no son obligatorios, pero se suelen utilizar por convención.
# Muchos frameworks y librerías los utilizan por lo que es una buena practica llamarlos así.
