import sqlite3

#aca no necesitamos cerrar la conexion ni commit ya que with se encarga de eso.
with sqlite3.connect("11-sqlite/app2.db") as con:
    cursor = con.cursor() #se debe crear para poder realizar consultas
    cursor.execute(
        "insert into usuario2 values(?,?)", (1, "Andres Medina")    
    )
