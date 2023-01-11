

def monitorizar(funcion):
    def decorar():
        print("\t* Se está apunto de ejecutar la función:", funcion.__name__)
        funcion()
        print("\t* Se ha finalizado de ejecutar la función:", funcion.__name__)
    return decorar


@monitorizar
def hola():
    print("Hola!")


@monitorizar
def adios():
    print("Adiós!")
