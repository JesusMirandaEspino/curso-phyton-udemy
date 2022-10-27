print(1 + 1 == 3)
print(1 + 1 == 2)


print(3 == 2)
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 4)
print(3 <= 4)


a = 10
b = 5

print(a > b)
print(b != a)
print(a == b*2)
print("Hola" == "Hola")
print("Hola" != "Hola")

c = "Hola"
print(c[0] == "H")

c = "Hola"
print(c[-1] == "a")


l1 = [0, 1, 2]
l2 = [2, 3, 4]

print(l1 == l2)
print(len(l1) == len(l2))
print(l1[-1] == l2[0])
print(True == True)
print(False == True)
print(False != True)
print(True > False)
print(False > True)

print(True * 3)
print(False / 5)
print(True * False)


# Not(Negación lógica)
# Niega un valor o expresión lógica:
print(not True)
print(not False)
print(not True == False)

# And(Conjunción lógica)
# Devuelve verdadero sólo si se cumplen todas las condiciones:
print(True and True)
print(True and False)
print(False and True)
print(False and False)

Fa = 45
print(a > 10 and a < 20)

c = "Hola Mundo"
print(len(c) >= 20 and c[0] == "H")

# Or(Disyunción lógica)
# Devuelve verdadero si se cumple como mínimo una condición:
print(True or True)

print(True or False)

print(False or True)

print(False or False)

c = "OTRA COSA"
print(c == "EXIT" or c == "FIN" or c == "SALIR")

c = "Lector"
print(c[0] == "H" or c[0] == "h")


a = 10
b = 5

print(a * b - 2**b >= 20 and not (a % b) != 0)

# Suma en asignación
a = 5
a += 5
print(a)

# Resta en asignación
a = 5
a -= 10
print(a)

# Producto en asignación
a = 5
a *= 2
print(a)

# División en asignación
a = 5
a /= 2
print(a)

# Módulo en asignación
a = 5
a %= 2
print(a)

# Potencia en asignación
a = 5
a **= 3
print(a)

