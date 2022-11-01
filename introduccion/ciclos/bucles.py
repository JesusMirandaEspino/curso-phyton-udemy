lista = ["Hola", 10, "Adiós", [50, 100, 150]]

lista[-1]

lista[-1][0]

lista[-1][-1]


for numero in lista[-1]:
    print(numero)


lista = [
    "Esto es un texto",             # cadena
    (1, 5, 10, 15, 20, 25),         # tupla
    ["Azul", "Verde", "Amarillo"]   # lista
]

for coleccion in lista:
    for subelemento in coleccion:
        print(coleccion, '->', subelemento)


lista = [
    "Esto es un texto",             # cadena
    (1, 5, 10, 15, 20, 25),         # tupla
    ["Azul", "Verde", "Amarillo"]   # lista
]

for indice_coleccion, coleccion in enumerate(lista):
    for indice_subelemento, subelemento in enumerate(coleccion):
        print(lista[indice_coleccion], '->', lista[indice_coleccion]
              [indice_subelemento])  # Acceso por indice


# For de la primera dimensión
for i, coleccion in enumerate(lista):
    # For de la segunda dimensión
    for j, subelemento in enumerate(coleccion):
        print(lista[i], '->', lista[i][j])


tabla = [
    [0, 0, 0],  # primera fila
    [1, 1, 1],  # segunda fila
    [2, 2, 2]   # tercera fila
]

for i, fila in enumerate(tabla):
    for j, columna in enumerate(fila):
        print(tabla[i][j], end=" ")
    print()


tabla = [
    [0, 0, 0],  # primera fila
    [1, 1, 1],  # segunda fila
    [2, 2, 2]   # tercera fila
]

cubo = [tabla, tabla, tabla]

print(cubo[0][0][0])
print(cubo[1][1][1])
print(cubo[2][2][2])


for k, tabla in enumerate(cubo):
    for i, fila in enumerate(tabla):
        for j, columna in enumerate(fila):
            print(cubo[k][i][j], end=" ")
        print()
    print()
