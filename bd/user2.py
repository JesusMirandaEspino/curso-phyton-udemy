import sqlite3

conexion = sqlite3.connect('usuarios.db')

cursor = conexion.cursor()

# Añadimos un usuario con el mismo DNI
cursor.execute("INSERT INTO usuarios VALUES " \
    "('11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")

conexion.commit()
conexion.close()
