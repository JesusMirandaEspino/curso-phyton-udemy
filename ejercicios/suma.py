def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print('Tipo de dato no es valido')
    else:
        return r


def resta(a, b):
    try:
        r = a - b
    except TypeError:
        print('Tipo de dato  invalido')
    else:
        return r


def producto(a, b):
    try:
        r = a * b
    except TypeError:
        print('Tipo de dato no valido')
    else:
        return r


def division(a, b):
    try:
        r = a / b
    except TypeError:
        print('Tipo de dato no valido')
    except ZeroDivisionError:
        print('No es posible dividir en cero')
    else:
        return r


