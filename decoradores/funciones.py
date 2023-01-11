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
