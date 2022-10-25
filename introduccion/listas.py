numeros = [1, 2, 3, 4]


datos = [4, "Una cadena", -15, 3.14, "Otra cadena"]

print(datos[0])
print(datos[-1])
print(datos[2:])


print(numeros + [5,6,7,8])


pares = [0, 2, 4, 5, 8, 10]
pares[3] = 6

pares.append(12)
pares.append(7*2)


print(pares)


letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3]
print(letras)

letras[:3] = ['A','B','C']

print(letras)


letras[:3] = []
print(letras)

letras = []
print(letras)

print(len(letras))
print(len(pares))


valor = input()
print(valor)


valor = input("Introduce un valor: ")  # Podemos mostrar un mensaje
print(valor)


valor = input("Introduce un número entero: ")
print(valor + 50)



valor = int(input("Introduce un número entero: "))
print(valor * 2)



valor = float(input("Introduce un número entero o flotante: "))
print(valor * 2)
