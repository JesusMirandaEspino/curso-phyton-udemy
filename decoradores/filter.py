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


def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]
print(list(map(doblar, numeros)))
print(list( map(lambda x: x*2, numeros) ))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
otra_lista = list( map(lambda x,y : x*y, a,b) )
print(otra_lista)

c = [11, 12, 13, 14, 15]
print(list( map(lambda x,y,z : x*y*z, a,b,c) ))

def incrementar(p):
    p.edad += 1
    return p

personas = map(incrementar, personas)

for persona in personas:
    print(persona)


personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]

personas = map(lambda p: Persona(p.nombre, p.edad+1), personas)

for persona in personas:
    print(persona)
