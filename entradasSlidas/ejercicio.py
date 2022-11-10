nombre = "Héctor"
cadena = "Hola {}".format(nombre)
print(cadena)

nombre = "Héctor"
cadena = f"Hola {nombre}"
print(cadena)

a, b = 10, 5

print(f"La suma de {a} y {b} es {a+b}")



def func():
    return "Pepe"


print(f"¡Hola {func()}!")

numero = {"uno": 1, "dos": 2, "tres": 3}

print(f"El número dos es {numero['dos']}")

print(f"{'Hola mundo':40}")  # a la izquierda 40 caracteres
texto = "Hola mundo"

print(f"{texto:40}")    # a la izquierda 40 caracteres
print(f"{texto:>40}")   # a la derecha 40 caracteres
print(f"{texto:^40}")   # al centro 40 caracteres

print(f"{texto:.4}")   # primeros 4 caracteres

limite = 4

print(f"{texto:.{limite}}")   # primeros 4 caracteres

print(f"{texto:>30.4}")
print(f"{texto:<30.4}")
print(f"{texto:^30.4}")

limite = 4
longitud = 30

print(f"{texto:>{longitud}.{limite}}")
print(f"{texto:<{longitud}.{limite}}")
print(f"{texto:^{longitud}.{limite}}")

print(f"{1:6d}")
print(f"{10:6d}")
print(f"{100:6d}")
print(f"{1000:6d}")
print(f"{10000:6d}")
print(f"{100000:6d}")

print(f"{1:06d}")
print(f"{10:06d}")
print(f"{100:06d}")
print(f"{1000:06d}")
print(f"{10000:06d}")
print(f"{100000:06d}")


# 4 dígitos: 3 enteros, 1 punto y 3 decimales

print(f"{3.1415926:7.3f}")   
print(f"{153.21:7.3f}")

# 9 dígitos: 4 enteros, 1 punto y 4 decimales

print(f"{3.1415926:09.4f}")   
print(f"{153.21:09.4f}")      

numero = 3.1415926
longitud = 21       # 1 para el decimal
decimales = 10

print(f"{numero:0{longitud}.{decimales}f}")