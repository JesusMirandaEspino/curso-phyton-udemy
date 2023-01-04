# Importamos el módulo
import sqlite3

# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios con nombres, edades y emails
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Guardamos los cambios haciendo un commit
conexion.commit()

# Cerramos la conexión, si no la cerramos quedará abierta
# y no podremos gestionar el fichero
conexion.close()
