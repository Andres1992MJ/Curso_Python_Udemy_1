import sqlite3

#Siempre hay que cerrar la conexion o nunc se podra volver a escribir en la base de datos
#Si el archivo no existe python lo crea:
con = sqlite3.connect("sqlite/app.db")   

con.close()