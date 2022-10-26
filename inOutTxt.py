file = open ("Text_file_example.txt", "w")
file.write ("Hi, i'm a Developer, Python is cool...\n")
file.close

file = open ("Text_file_example.txt", "r+")
file.readline()
file.write ("...But programming is hard sometimes.\n")

file.seek(0)
print(file.read())
file.close()

'''En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.'''