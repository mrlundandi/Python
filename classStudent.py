class Student:
    def start(self,name,grades):
        self.name = name
        self.grades = grades

    def data(self):
            print("Name: ",self.name)
            print("Calification: ",self.grades)


    def results(self):
            if self.grades < 5:
                print("The student has failed")
            else:
                print("The student has passed")

# create object here:
student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()

# initialize data here:
student1.start("David", 2)
student2.start("Carla", 9)
student3.start("Anna", 4)
student4.start("Miguel", 6)

# results here:
student1.data()
student1.results()

student2.data()
student2.results()

student3.data()
student3.results()

student4.data()
student4.results()

'''En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada alumno
que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''