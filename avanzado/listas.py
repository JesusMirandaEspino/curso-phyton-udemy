
lista1 = []
for letra in 'casa':
    lista1.append(letra)
print(lista1)


# Con comprensión de listas
lista = [letra for letra in 'casa']
print(lista)


# Método tradicional
lista2 = []
for numero in range(0, 11):
    lista2.append(numero**2)
print(lista2)

# Con comprensión de listas
lista3 = [numero**2 for numero in range(0, 11)]
print(lista3)


# Método tradicional
lista4 = []
for numero in range(0, 11):
    lista4.append(numero**2)
print(lista4)


# Método tradicional
lista5 = []
for numero in range(0, 11):
    if numero % 2 == 0:
        lista5.append(numero)
print(lista5)

# Añadir los números del 0 al 10 cuando su módulo de 2 sea 0
lista6 =  [numero for numero in range(0, 11) if numero % 2 == 0]
print(lista6)


# Método tradicional
lista7 = []
for numero in range(0, 11):
    lista7.append(numero**2)

pares = []
for numero in lista7:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)


# Con comprensión de listas
lista8 = [numero for numero in [numero**2 for numero in range(0, 11)] if numero % 2 == 0]
print(lista8)
