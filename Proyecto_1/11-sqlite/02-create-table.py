import sqlite3

con = sqlite3.connect("11-sqlite/app.db")
cursor = con.cursor() #se debe crear para poder realizar consultas
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuario 
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
con.commit()#Este ejecuta la consulta
con.close()