def hola(arg):
    """Este es el docstring de la función"""
    print("Hola", arg, "!")

hola("Héctor")
help(hola)


class Clase:
    """ Este es el docstring de la clase"""
    def __init__(self):
        """Este es el docstring del inicializador de clase"""
    def metodo(self):
        """Este es el docstring del metodo de clase"""

o = Clase()
help(o)