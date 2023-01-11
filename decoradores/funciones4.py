def monitorizar_args(funcion):

    def decorar(*args, **kwargs):
        print("\t* Se está apunto de ejecutar la función:", funcion.__name__)
        funcion(*args, **kwargs)
        print("\t* Se ha finalizado de ejecutar la función:", funcion.__name__)

    return decorar


@monitorizar_args
def hola(nombre):
    print("Hola {}!".format(nombre))


@monitorizar_args
def adios(nombre):
    print("Adiós {}!".format(nombre))


hola("Héctor")
print()
adios("Héctor")
