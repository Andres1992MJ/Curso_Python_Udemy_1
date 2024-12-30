from io import open
import csv
import os


#escribir // lo puede crear si no existe
with open("10-archivos/archivo_1.csv","w",newline="") as archivo:
    writer= csv.writer(archivo)
    writer.writerow(["twit_id","user_id","text"])
    writer.writerow(["1000","1","primera linea primer twit"])
    writer.writerow(["1001","2","segunda linea segundo twit"])

#leer
with open("10-archivos/archivo_1.csv") as archivo:
    reader= csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)



#modificar un archivo CSV

with open("10-archivos/archivo_3.csv") as r, open("10-archivos/archivo_3_temp.csv","w",newline="") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000,1,"Texto modificado segunda vez"])
        else:
            writer.writerow(linea)
os.remove("10-archivos/archivo_3.csv")
os.rename("10-archivos/archivo_3_temp.csv","10-archivos/archivo_3.csv")
    

