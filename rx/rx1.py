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


texto5 = "hola adios hello bye"
print(re.findall('hola|hello', texto5))

texto6 = "hla hola hoola hooola hooooola"

def buscar(patrones, texto6):
    for patron in patrones:
        print(re.findall(patron, texto6))


patrones = ['hla', 'hola', 'hoola']
buscar(patrones, texto6)

patrones1 = ['ho', 'ho*', 'ho*la', 'hu*la']
buscar(patrones1, texto6)

patrones2 = ['ho*', 'ho+']
buscar(patrones2, texto6)

patrones3 = ['ho*', 'ho+', 'ho?', 'ho?la']
buscar(patrones3, texto6)

patrones4 = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,9}la']
buscar(patrones4, texto6)
