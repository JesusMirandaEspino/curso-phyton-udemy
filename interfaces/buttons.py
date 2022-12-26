from tkinter import *

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    borrar()

def producto():
    r.set( float(n1.get()) * float(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")


def hola():
    s.set("Hola mundo!")
    print("Hola mundo!")


# Configuración de la raíz
root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()
s = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="Saludo").pack()
Entry(root, justify="center", textvariable=s, state="disabled").pack()

Label(root, text="").pack()  # Separador

Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")


# Enlezamos la función a la acción del botón
Button(root, text="Clícame", command=hola).pack()


# Finalmente bucle de la aplicación
root.mainloop()
