def leapYear():
  year: int = int(input("Enter a year and let's see if it's a leap year... "))

  if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
      print(f"The year {year} is leap!")
  else:
      print(f"Sorry... The year {year} isn't leap!")

print({leapYear()}) 

'''Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.'''