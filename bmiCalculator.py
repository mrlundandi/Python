weigth = input("What's your weight in kg? ")
height = input("What's your height in meters? ")
bmi = round(float(weigth)/float(height)**2, 2)
print("Your body mass index (BMI) is " + str(bmi))

'''Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
"Tu índice de masa corporal es ", donde es el índice de masa corporal calculado redondeado con dos decimales.'''