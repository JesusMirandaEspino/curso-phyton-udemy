from tkinter import *

# Funciones backend


def borrar():
    n1.set('')
    n2.set('')


def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()


# Estructura del formulario
root = Tk()
root.config(bd=15)  # borde exterior de 15 píxeles, queda mejor

# Tres StringVar para manejar los números y el resultado
n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Numero 1").pack()
Entry(root, justify=CENTER, textvariable=n1).pack()

Label(root, text="\nNumero 2").pack()
Entry(root, justify=CENTER, textvariable=n2).pack()

Label(root, text="\nResultado").pack()
Entry(root, justify=CENTER, state=DISABLED, textvariable=r).pack()

Label(root).pack()  # Separador

Button(root, text="Sumar", command=sumar).pack()

root.mainloop()
