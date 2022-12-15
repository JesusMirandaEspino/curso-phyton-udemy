from io import open
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


# Ejemplo catálogo de películas
# A continuación os dejo un ejemplo para que veáis como adaptar un catálogo de películas para usar persistencia utilizando pickle:


class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self, p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} películas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()


# El uso de las clases no tendría mucha complicación:

    # Creamos un catálogo
c = Catalogo()

# Mostramos el contenido
c.mostrar()

# Agregamos unas películas
c.agregar(Pelicula("El Padrino", 175, 1972))
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))

# Mostramos el catálogo de nuevo
c.mostrar()

# Borramos el catálogo de la memoria ram (persistirá el fichero)
del(c)

# El fichero está vacío
# Se han cargado 0 películas

# El catálogo está vacío

# Se ha creado la película: El Padrino
# Se ha creado la película: El Padrino: Parte 2

# El Padrino(1972)
# El Padrino: Parte 2 (1974)
# Ahora al crear de nuevo un catálogo se recuperarán los datos del fichero y 
# podríamos seguir trabajando con él:

    # Creamos un catálogo
c = Catalogo()

# Mostramos el contenido
c.mostrar()

# Agregamos una película
c.agregar(Pelicula("Prueba", 100, 2005))

# Mostramos el catálogo de nuevo
c.mostrar()

# Se han cargado 2 películas

# El Padrino(1972)
# El Padrino: Parte 2 (1974)

# Se ha creado la película: Prueba

# El Padrino(1972)
# El Padrino: Parte 2 (1974)
# Prueba(2005)
