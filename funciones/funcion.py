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
