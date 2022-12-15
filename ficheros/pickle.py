import pickle
# Módulo pickle
# Este módulo nos permite almacenar fácilmente colecciones y 
# objetos en ficheros binarios abstrayendo todo la parte de escritura y lectura binaria.
# Escritura de colecciones
# Podemos guardar lo que queramos, listas, diccionarios, tuplas...
lista = [1, 2, 3, 4, 5]

# Escritura en modo binario, vacía el fichero si existe
fichero = open('lista.pckl', 'wb')

# Escribe la colección en el fichero
pickle.dump(lista, fichero)

fichero.close()



# Lectura de colecciones

# Lectura en modo binario
fichero = open('lista.pckl', 'rb')

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
print(lista_fichero)

fichero.close()

# [1, 2, 3, 4, 5]
# Persistencia de objetos
# Para guardar objetos lo haremos dentro de una colección. La lógica sería la siguiente:

# Crear una colección.
# Introducir los objetos en la colección.
# Guardar la colección haciendo un dump.
# Recuperar la colección haciendo un load.
# Seguir trabajando con nuestros objetos.

# Creamos una clase de prueba


class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


# Creamos la lista con los objetos
nombres = ["Héctor", "Mario", "Marta"]
personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)

# Escribimos la lista en el fichero con pickle
f = open('personas.pckl', 'wb')
pickle.dump(personas, f)
f.close()

# Leemos la lista del fichero con pickle
f = open('personas.pckl', 'rb')
personas = pickle.load(f)
f.close()

for p in personas:
    print(p)

# Héctor
# Mario
# Marta
