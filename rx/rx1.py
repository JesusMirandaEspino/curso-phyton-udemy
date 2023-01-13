import re

texto = "En esta cadena se encuentra una palabra mágica"

print(re.search('mágica', texto))
print(re.search('hola', texto))

palabra = "mágica"

encontrado = re.search(palabra,  texto)
if encontrado:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra)

# Posición donde empieza la coincidencia
print( encontrado.start() ) 
# Posición donde termina la coincidencia
print( encontrado.end() )  
# Tupla con posiciones donde empieza y termina la coincidencia
print( encontrado.span() )   
# Cadena sobre la que se ha realizado la búsqueda
print( encontrado.string )   