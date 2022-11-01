elementos = ["Hola", 4, "Adiós", [1, 2, 3]]

for e in elementos:
    print(e)


for i, e in enumerate(elementos):
    print(i, e)


a, b, c = 10, 50, 100
print(a,b,c)

a, b, c = [10, 50, 100]
print(a,b,c)

a, b, c = (10, 50, 100)
print(a,b,c)


elementos = ["Hola", 4, "Adiós", [1, 2, 3]]

list(enumerate(elementos))


for tupla in enumerate(elementos):
    print(tupla)


for indice, valor in enumerate(elementos):
    print(indice, valor)
