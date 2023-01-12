def doblar(num): return num*2
print(doblar(2))

doblar2 = lambda num: num*2
print(doblar2(2))


impar = lambda num: num%2 != 0
print(impar(5))


revertir = lambda cadena: cadena[::-1]
print(revertir("Hola"))


sumar = lambda x,y: x+y
print(sumar(5, 2))
