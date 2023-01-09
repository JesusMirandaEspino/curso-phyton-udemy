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
    categoria = input('Ingrese nombre de la Categoria')
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    cursor.execute(" INSERT INTO categoria VALUES (NULL, '{}') ".format(categoria))

    conexion.commit()
    conexion.close()


crear_db()
agregar_categoria()