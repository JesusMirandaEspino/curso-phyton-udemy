def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es


numeros = [2, 5, 10, 23, 50, 33]

print(filter(multiple, numeros))

print(list(filter(multiple, numeros)))

nueva_lista = list(filter(lambda numero: numero % 5 == 0, numeros))

print(nueva_lista)


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)


personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]


menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)
