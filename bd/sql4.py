import sqlite3

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()

# Creamos una lista con varios usuarios
usuarios = [('Mario', 51, 'mario@ejemplo.com'),
            ('Mercedes', 38, 'mercedes@ejemplo.com'),
            ('Juan', 19, 'juan@ejemplo.com')]

# Ahora utilizamos el método executemany() para insertar varios
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()