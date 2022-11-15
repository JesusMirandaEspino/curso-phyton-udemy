# Definición y llamada
# Se definen con la palabra reservada def, el nombre de la función y unos paréntesis, que también se utilizan para hacer la llamada:
def saludar():
    print("Hola! Este print se llama desde la función saludar()")
saludar()

# Hola! Este print se llama desde la función saludar()
# Dentro de una función podemos utilizar variables y sentencias de control:
def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i, i*5))
dibujar_tabla_del_5()

# Ámbito de las variables
# Una variable declarada en una función no existe en la función principal:
def test():
    n = 10
test()

m = 10
def test():
    print(m)
test()

# Siempre que declaremos la variable antes de la ejecución, podemos acceder a ella desde dentro:
def test():
    print(l)
l = 10
test()


# En el caso que declaremos de nuevo una variable en la función, se creará un copia de la misma que sólo funcionará dentro de la función.
# Por tanto no podemos modificar una variable externa dentro de una función:
def test():
    o = 5  # variable que sólo existe dentro de la función
    print(o)

o = 10  # variable externa, no modificable
test()
print(o)

# La instrucción global
# Para poder modificar una variable externa en la función, debemos indicar que es global de la siguiente forma:
def test():
    global o  # variable que hace referencia a la o externa
    o = 5
    print(o)
o = 10
test()
print(o)

# Paso por valor y referencia
# Dependiendo del tipo de dato que enviemos a la función, podemos diferenciar dos comportamientos:

# Paso por valor: Se crea una copia local de la variable dentro de la función.
# Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro de la función le afectarán también fuera.
# Tradicionalmente:
# Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
# Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...
# Ejemplo de paso por valor
# Como ya sabemos los números se pasan por valor y crean una copia dentro de la función, por eso no les afecta externamente lo que hagamos con ellos:
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)

# Ejemplo de paso por referencia
# Sin embargo las listas u otras colecciones, al ser tipos compuestos se pasan por referencia, y si las modificamos dentro de la función estaremos modificándolas también fuera:

def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

ns = [10, 50, 100]
doblar_valores(ns)
print(ns)

# Para modificar los tipos simples podemos devolverlos modificados y reasignarlos:
def doblar_valor(numero):
    return numero * 2

n = 10
n = doblar_valor(n)
print(n)

# Y en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia:
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
ns = [10, 50, 100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print(ns)
