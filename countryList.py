items = input("Write a list of countries (separated by commas):\n")

countries = [country for country in items.split(",")]

print(",".join(sorted(list(set(countries)))))

'''Crea un script que le pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.'''