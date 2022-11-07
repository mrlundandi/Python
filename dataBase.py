import sqlite3

db_connection = sqlite3.connect('dataBase.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Students(Id INT, Name TEXT, Lastname TEXT)")

db_cursor.execute("INSERT INTO Students VALUES(1,'Julián', 'Palencia')")
db_cursor.execute("INSERT INTO Students VALUES(2,'Manuel', 'Huang')")
db_cursor.execute("INSERT INTO Students VALUES(3,'Lamine', 'Perez')")
db_cursor.execute("INSERT INTO Students VALUES(4,'Ana María', 'Santigosa')")
db_cursor.execute("INSERT INTO Students VALUES(5,'Lucía', 'Torres')")
db_cursor.execute("INSERT INTO Students VALUES(6,'Fátima', 'El Hammani')")
db_cursor.execute("INSERT INTO Students VALUES(7,'Tania', 'Gil')")
db_cursor.execute("INSERT INTO Students VALUES(8,'Rosa', 'Castillo')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Students WHERE Name = 'Lamine'")

lines = db_cursor.fetchall()

print(lines)

db_connection.close()

'''En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.'''