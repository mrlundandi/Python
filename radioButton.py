from tkinter import *

def selection():
    monitor.config(text="{}".format(option.get()))
def reset():
    option.set(None)
    monitor.config(text="")

root = Tk()
option = StringVar()
option.set(None)

Radiobutton(root, text="KoRn", variable=option, 
            value='KoRn', command=selection).pack(anchor=W)
Radiobutton(root, text="Slipknot", variable=option, 
            value='Slipknot', command=selection).pack(anchor=W)
Radiobutton(root, text="Amon Amarth", variable=option,   
            value='Amon Amarth', command=selection).pack(anchor=W)
Radiobutton(root, text="Trivium", variable=option,   
            value='Trivium', command=selection).pack(anchor=W)
Radiobutton(root, text="In Flames", variable=option,   
            value='In Flames', command=selection).pack(anchor=W)
Radiobutton(root, text="Parkway Drive", variable=option,   
            value='Parkway Drive', command=selection).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reset", command=reset).pack()

root.mainloop()

'''Crea una lista de RadioButton que muestre la opción que se ha seleccionado
y que contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.'''