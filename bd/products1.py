import sqlite3

conexion = sqlite3.connect('productos.db')

cursor = conexion.cursor()

# Las cláusulas not null indican que no puede ser campos vacíos
cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(100) NOT NULL, 
                    marca VARCHAR(50) NOT NULL, 
                    precio FLOAT NOT NULL)''')

conexion.close()
