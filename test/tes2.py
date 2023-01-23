import doctest

def doblar(lista):
    """Dobla el valor de los elementos de una lista
    >>> l = [1, 2, 3, 4, 5] 
    >>> doblar(l)
    [2, 4, 6, 8, 10]

    >>> l = [] 
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [n*2 for n in lista]


def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    Pueden ser números:

    >>> suma(5,10)
    15

    >>> suma(-5,7)
    2

    Cadenas de texto:

    >>> suma('aa','bb')
    'aabb'

    O listas:

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    Sin embargo no podemos sumar elementos de tipos diferentes:

    >>> suma(10,"hola")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a+b
