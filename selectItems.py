from tkinter import *
items = Tk()
element = StringVar()
listbox = Listbox(items)
for item in ["Hero", "Bandit", "Astrologer", "Warrior", "Prisoner", "Confessor", "Wretch", "Vagabond", "Prophet", "Samurai"]:
    listbox.insert(END, item)
listbox.pack()
label = Label(text="Elden Ring Classes")
label.pack()
items.mainloop()

'''Crea una interfaz sencilla la cual debe de contener una lista de elementos
seleccionables, también debe de tener un label con un texto cualquiera.'''