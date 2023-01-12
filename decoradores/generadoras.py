[numero for numero in [0,1,2,3,4,5,6,7,8,9,10] if numero % 2 == 0 ]

[numero for numero in range(0,11) if numero % 2 == 0 ]


def pares(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            yield numero
pares(10)

