import sqlite3
from tkinter import *

# Configuración de la raíz
root = Tk()
root.title('Bar Cheeto - Menu')
root.resizable(0,0)
root.config(bd=25,relief='sunken')

FONTTYPE = 'Times New Roman'
FONTSTYLE = 'bold italic'

Label(root, text='   Bar Cheeto   ', fg='darkgreen', font=(FONTTYPE, 28, FONTSTYLE)).pack()
Label(root, text='   Menu del dia   ', fg='green', font=(FONTTYPE, 24, FONTSTYLE)).pack()
Label(text='').pack()

conexion = sqlite3.connect('restaurante.db')
cursor = conexion.cursor()

categorias = cursor.execute("SELECT * FROM categoria").fetchall()

for categoria in categorias:
    Label(root, text=categoria[1], fg='darkgreen', font=( 'Times New Roman', 20, 'bold italic')).pack()
    platos = cursor.execute(
        "SELECT * FROM plato WHERE categoria_id = {} ".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg='gray', font=('Times New Roman', 16, 'bold italic')).pack()
    Label(text='').pack()

conexion.close()
root.mainloop()
