# Argumentos por posición
# Cuando enviamos argumentos a una función, estos se reciben por orden en los parámetros definidos. Se dice por tanto que son argumentos por posición:
def resta(a, b):
    return a - b

resta(30, 10)  # argumento 30 => posición 0 => parámetro a
# argumento 10 => posición 1 => parámetro b
# Argumentos por nombre
# Sin embargo es posible evadir el orden de los parámetros si indicamos durante la llamada que valor tiene cada parámetro a partir de su nombre:
resta(b=30, a=10)

# Llamada sin argumentos
# Al llamar una función que tiene definidos unos parámetros, si no pasamos los argumentos correctamente provocará un error:
# resta()

# Parámetros por defecto
# Para solucionarlo podemos asignar unos valores por defecto nulos a los parámetros, de esa forma podríamos hacer una comprobación antes de ejecutar el código de la función:

def resta(a=None, b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return   # indicamos el final de la función aunque no devuelva nada
    return a-b
resta()
