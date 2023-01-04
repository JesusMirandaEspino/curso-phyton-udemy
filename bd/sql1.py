# Importamos el módulo
import sqlite3

# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('ejemplo.db')

# Cerramos la conexión, si no la cerramos quedará abierta
# y no podremos gestionar el fichero
conexion.close()
