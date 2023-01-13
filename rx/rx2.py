import re

def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )


texto = "hala hela hila hola hula"
patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
buscar(patrones, texto)

texto1 = "haala heeela hiiiila hoooooola"
patrones1 = ['h[ae]la', 'h[ae]*la', 'h[io]{3,9}la']
buscar(patrones1, texto1)

texto3 = "hola h0la Hola mola m0la M0la"
patrones3 = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}']
buscar(patrones3, texto3)

texto4 = "Este curso de Python se publicó en el año 2016"
patrones4 = [r'\d+', r'\D+', r'\s', r'\S+', r'\w+', r'\W+']
buscar(patrones4, texto4)
