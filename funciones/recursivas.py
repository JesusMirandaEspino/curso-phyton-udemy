# Funciones recursivas
# Se trata de funciones que se llaman a sí mismas durante su propia ejecución. Funcionan de forma similar a las iteraciones, pero debemos encargarnos de planificar el momento en que dejan de llamarse a sí mismas o tendremos una función rescursiva infinita.

# Suele utilizarse para dividir una tarea en subtareas más simples de forma que sea más fácil abordar el problema y solucionarlo.

# Ejemplo sin retorno
# Cuenta regresiva hasta cero a partir de un número:
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)


cuenta_atras(5)

# Ejemplo con retorno
# El factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número. Es el ejemplo con retorno más utilizado para mostrar la utilidad de este tipo de funciones:

def factorial(num):
    print("Valor inicial ->", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("valor final ->", num)
    return num

print(factorial(5))


def doblar():
    global num
    num *= 2


num = 5
doblar()
print(num)


def test(num):
   return num, num*2, num*4


test(5)
