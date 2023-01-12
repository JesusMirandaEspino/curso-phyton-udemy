[numero for numero in [0,1,2,3,4,5,6,7,8,9,10] if numero % 2 == 0 ]

[numero for numero in range(0,11) if numero % 2 == 0 ]


def pares(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            print(numero)
            yield numero
pares(10)

for numero in pares(10):
    print(numero)

[numero for numero in pares(10)]


pares = pares(3)


print(next(pares))
print(next(pares))

lista = [1, 2, 3, 4, 5]
lista_iterable = iter(lista)
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))


cadena = "Hola"
cadena_iterable = iter(cadena)
print( next(cadena_iterable) )
print( next(cadena_iterable) )
print( next(cadena_iterable) )
print( next(cadena_iterable) )