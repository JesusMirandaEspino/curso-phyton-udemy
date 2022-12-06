from saludos import Saludo
from saludos import *
from saludos import saludar
import saludos


# Luego ya podremos utilizarlo desde otro script, por ejemplo script.py, en el mismo directorio haciendo un import y el nombre del módulo:
saludos.saludar()

# También podemos importar funciones directamente, de esta forma ahorraríamos memoria. Podemos hacerlo utilizando la sintaxis from import:

# Igual que antes, tendremos que llamar primero al módulo para referirnos a la clase:

s = saludos.Saludo()
# O cargar solo una clase con el from import:


s = Saludo()
# El problema ocurre cuando queremos utilizar nuestro módulo desde un directorio distinto por ejemplo test/script.py.
