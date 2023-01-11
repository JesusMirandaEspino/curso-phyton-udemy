# Funciones decoradoras

def hola():
    def bienvenido():
        return "Hola!"
    print(locals())  # Mostramos el ámbito local
hola()


lista = [1, 2, 3]
def hola1():
    numero = 50
    def bienvenido1():
        return "Hola!"
    print(locals())  # Mostramos el ámbito local
hola1()


# Antes de ejecutar el bloque reinicia el Notebook para vaciar la memoria
lista2 = [1, 2, 3]
def hola2():
    numero = 50
    def bienvenido2():
        return "Hola!"
    print(globals())  # Mostramos el ámbito global
hola2()


globals().keys()


globals()['lista']

