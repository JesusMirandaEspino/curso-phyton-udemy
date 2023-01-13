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


texto1 = "Hola mundo"
print(re.match('Hola', texto1))

texto2 = "Vamos a dividir esta cadena"
print(re.split(' ', texto2))

texto3 = "Hola amigo"
print(re.sub('amigo', 'amiga', texto3))

texto4 = "hola adios hola hola"
print(re.findall('hola', texto4))


print(len(re.findall('hola', texto4)))
