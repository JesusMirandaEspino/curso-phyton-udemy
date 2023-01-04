import sqlite3

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()

# Insertamos un registro en la tabla de usuarios
cursor.execute("INSERT INTO usuarios VALUES " \
    "('Hector', 27, 'hector@ejemplo.com')")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()