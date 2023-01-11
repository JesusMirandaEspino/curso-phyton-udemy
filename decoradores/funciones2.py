
def hola():
    def bienvenido():
        return "Hola!"
    return bienvenido

hola()
hola()()


bienvenido = hola()
bienvenido()


def hola1():
    return "Hola!"

def test(funcion):
    print(funcion())

test(hola1)
