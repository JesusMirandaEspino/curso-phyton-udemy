import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

# Recuperamos un registro de la tabla de usuarios
cursor.execute("SELECT nombre, edad, email FROM usuarios WHERE dni='22222222B'")

usuario = cursor.fetchone()
print(usuario)

conexion.close()
