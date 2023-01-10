import sqlite3
from tkinter import *

# Configuración de la raíz
root = Tk()
root.title('Bar Cheeto - Menu')
root.resizable(0,0)
root.config(bd=25,relief='sunken')

Label(root, text='   Bar Cheeto   ', fg='darkgreen', font=( 'Times New Roman', 28, 'bold italic' ) ).pack()

root.mainloop()