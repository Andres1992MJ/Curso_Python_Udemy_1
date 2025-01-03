import sqlite3

#aca no necesitamos cerrar la conexion ni commit ya que with se encarga de eso.
with sqlite3.connect("11-sqlite/app2.db") as con:
    cursor = con.cursor() #se debe crear para poder realizar consultas
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuario2 
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
