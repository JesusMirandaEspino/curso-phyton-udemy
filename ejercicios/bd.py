import sqlite3

def crear_db():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    try: 
        cursor.execute(
            ''' CREATE TABLE categoria( id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL ) ''')
    except sqlite3.OperationalError:
        print('la tabla categoria ya existe')
    else:
        print('La tabla categorias se ha creado correctamente')

    try:
        cursor.execute(
            ''' CREATE TABLE plato( id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL, FOREIGN KEY(categoria_id) REFERENCES categoria(id)) ''')
    except sqlite3.OperationalError:
        print('la tabla platos ya existe')
    else:
        print('La tabla platos se ha creado correctamente')


    conexion.close()


def agregar_categoria():
    categoria = input('Ingrese nombre de la Categoria: ')
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    try:
        cursor.execute(
            " INSERT INTO categoria VALUES (NULL, '{}') ".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya existe. ".format(categoria))
    else:
        print("La categoria '{}' ha sidp creada correctamente. ".format(categoria))

    conexion.commit()
    conexion.close()


def agregar_plato():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    categorias = cursor.execute( "SELECT * FROM categoria" ).fetchall()
    print("Selecciona un categoria ")

    for categoria in categorias:
        print("[{}] {} ".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("Seleccione"))

    plato = input("Ingrese el platillo")

    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    try:
        cursor.execute(" INSERT INTO plato VALUES (NULL, '{}', {}) ".format(plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe. ".format(plato))
    else:
        print("El plato '{}' ha sido creada correctamente. ".format(categoria))


crear_db()



while True:
    print('Bienvenido al gestor del restaurante')
    print('Elige una opcion')
    print('1.- Ingresar categoria ')
    print('2.- Ingresar platillo ')
    print('3.- Salir del programa ')
    option = input()

    if option == '1':
        agregar_categoria()
    elif option == '2':
        agregar_plato()
    elif option == '3':
        break
    else:
        print('Option incorrecta')