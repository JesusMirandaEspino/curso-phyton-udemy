decimal = float( input("Introduce un número decimal con punto: ") )

valores = []

print("Introduce 3 valores")
for x in range(3):
    valores.append( input("Introduce un valor >") )


c = "{n} - {m} = {r}".format(m=2, r=3-2, n=3)

print(c)

c = "{:06d}".format(1234)

print(c)
