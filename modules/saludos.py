
# Módulos
# Crear un módulo en Python es tan sencillo como crear un script, sólo tenemos que añadir alguna función a un fichero con la extensión .py, por ejemplo saludos.py:


def saludar():
    print("Hola, te estoy saludando desde la función saludar() "
        "del módulo saludos")

saludar()
# Para importar todas las funciones con la sintaxis from import debemos poner un asterisco:


saludar()
# Dicho esto, a parte de funciones también podemos reutilizar clases:


class Saludo():
    def __init__(self):
        print("Hola, te estoy saludando desde el __init__ "
            "de la clase Saludo")


