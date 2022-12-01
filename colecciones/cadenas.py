# Métodos de las cadenas
# upper()
# Devuelve la cadena con todos sus caracteres a mayúscula:
"Hola Mundo".upper()
# 'HOLA MUNDO'

# lower()
# Devuelve la cadena con todos sus caracteres a minúscula:
"Hola Mundo".lower()
'hola mundo'

# capitalize()
# Devuelve la cadena con su primer carácter en mayúscula:
"hola mundo".capitalize()
'Hola mundo'

# title()
# Devuelve la cadena con el primer carácter de cada palabra en mayúscula:
"hola mundo".title()
'Hola Mundo'

# count()
# Devuelve una cuenta de las veces que aparece una subcadena en la cadena:
"Hola mundo".count('mundo')
# 1

# find()
# Devuelve el índice en el que aparece la subcadena(-1 si no aparece):
"Hola mundo".find('mundo')
# 5

"Hola mundo".find('mundoz')
# -1

# rfind()
# Devuelve el índice en el que aparece la subcadena, empezando por el final:
"Hola mundo mundo mundo".rfind('mundo')
# 17

# isdigit()
# Devuelve True si la cadena es todo números(False en caso contrario):
c = "100"
c.isdigit()
# True

# isalnum()
# Devuelve True si la cadena es todo números o carácteres alfabéticos:
c = "ABC10034po"
c.isalnum()
# True

# isalpha()
# Devuelve True si la cadena es todo carácteres alfabéticos:
c = "ABC10034po"
c.isalpha()
# False
"Holamundo".isalpha()
True

# islower()
# Devuelve True si la cadena es todo minúsculas:
"Hola mundo".islower()
# False

# isupper()
# Devuelve True si la cadena es todo mayúsculas:
"Hola mundo".isupper()
# False

# istitle()
# Devuelve True si la primera letra de cada palabra es mayúscula:
"Hola Mundo".istitle()
# True

# isspace()
# Devuelve True si la cadena es todo espacios:
"  -  ".isspace()
# False

# startswith()
# Devuelve True si la cadena empieza con una subcadena:
"Hola mundo".startswith("Mola")
False

# endswith()
# Devuelve True si la cadena acaba con una subcadena:
"Hola mundo".endswith('mundo')
# True

# split()
# Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista:
"Hola mundo mundo".split()[0]
#'Hola'
# Podemos indicar el carácter a partir del que se separa:
"Hola,mundo,mundo,otra,palabra".split(',')
# ['Hola', 'mundo', 'mundo', 'otra', 'palabra']

# join()
# Une todos los caracteres de una cadena utilizando un caracter de unión:
",".join("Hola mundo")
# 'H,o,l,a, ,m,u,n,d,o'
# " ".join("Hola")
# 'H o l a'

# strip()
# Borra todos los espacios por delante y detrás de una cadena y la devuelve:
"   Hola mundo     ".strip()
# 'Hola mundo'
# Podemos indicar el carácter a borrar:
"-----Hola mundo---".strip('-')
# 'Hola mundo'

# replace()
# Reemplaza una subcadena de una cadena por otra y la devuelve:
"Hola mundo".replace('o', '0')
# 'H0la mund0'
# Podemos indicar un límite de veces a reemplazar:
"Hola mundo mundo mundo mundo mundo".replace(' mundo', '', 4)
# 'Hola mundo'
