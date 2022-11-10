import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0:
        print("Error - Número es incorrecto")
        print("Ejemplo: descomposicion.py [0-999999999999999999999999]")
    else:
        # Aqui va la lógica
        cadena = str(numero)
        longitud = len(cadena)
        for i in range(longitud):
            # Utilizamos identificadores para la cadena y la longitud 
            print( "{cadena:0{longitud}d}".format(
                cadena=int(cadena[longitud-1-i]) * 10 ** i, 
                longitud=longitud))
else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: descomposicion.py [0-999999999999999999999999]")