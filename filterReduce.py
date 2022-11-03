from functools import reduce

def app(listNum): 
    outcome = list(filter((lambda x: x % 2), listNum)) 
    print(outcome)
    outcome = reduce( (lambda x, y: x + y), outcome) 
    print(outcome)

listNum = list(range(100))

app(listNum)

'''Crea una aplicación que obtendrá los elementos impares de una lista pasada 
por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.'''