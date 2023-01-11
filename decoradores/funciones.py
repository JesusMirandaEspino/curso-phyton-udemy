# Funciones decoradoras

def hola():

    def bienvenido():
        return "Hola!"

    print(locals())  # Mostramos el ámbito local


hola()
