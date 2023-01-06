import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

# Creamos un registro de prueba
cursor.execute("INSERT INTO usuarios VALUES "
               "(null, '55555555E', 'Fernando', 31, 'fernando@ejemplo.com')")

# Consultamos los usuarios
for usuario in cursor.execute("SELECT * FROM usuarios"):
    print(usuario)

# Ahora lo borramos
cursor.execute("DELETE FROM usuarios WHERE dni='55555555E'")

print()  # Espacio en blanco

# Consultamos de nuevo los usuarios
for usuario in cursor.execute("SELECT * FROM usuarios"):
    print(usuario)

conexion.commit()
conexion.close()
