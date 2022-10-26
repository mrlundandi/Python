from pickle import *

class Vehicle:
    def __init__(self,brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        
    def __str__(self):
        return "The car is a {} {}, the color is {}".format( self.brand, self.model, self.color )

car = Vehicle("Mazda", "RX7", "red")
print(car)

file = open ("File_Vehicle_Example", "wb")
dump(car, file)

file.seek(0)
new_car = load(file)

print(new_car)
file.close()

'''En este ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.'''