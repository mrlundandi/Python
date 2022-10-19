class Vehicle :
    
    def __init__(self, color, wheels, doors):
        self.color = color
        self.wheels = wheels
        self.doors = doors
        
    def __str__(self):
        return "Color {}, {} wheels, {} doors".format( self.color, self.wheels, self.doors )
        
class Car(Vehicle):
    def __init__(self, color, wheels, doors, speed, engineCapacity):
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.speed = speed
        self.engineCapacity = engineCapacity
        
    def __str__(self):
        return "Color {}, {} wheels, {} doors, max. speed {} kph, {} cc".format( self.color, self.wheels, self.doors, self.speed, self.engineCapacity )
    
    '''Create class Car object here:'''

car = Car("Black", 4, 5 ,210, 2140)
print(car)


'''En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
Color
Ruedas
Puertas
Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
Velocidad
Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.'''