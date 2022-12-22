from tkinter import *

root = Tk()
root.title("Hola mundo")
root.resizable(0, 0)

frame = Frame(root, width=480, height=320)
frame.pack()

frame.config(bg="blue")
frame.config(width=480, height=320)

frame.config(cursor="arrow")         
frame.config(relief="sunken")   
frame.config(bd=25)             

root.config(bg="blue")          
root.config(cursor="arrow")    
root.config(relief="sunken")    
root.config(bd=25)              

frame.pack(side='bottom', anchor='w')   
frame.pack(anchor=SE)    

frame.pack(fill="x")                
frame.pack(fill="y")                
frame.pack(fill="both")             
frame.pack(fill="both", expand=1)   

root.mainloop()
