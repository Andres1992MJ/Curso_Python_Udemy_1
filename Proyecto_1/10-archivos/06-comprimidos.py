from pathlib import Path
from zipfile import ZipFile

#Crear un zipfile
with ZipFile("10-archivos/comprimidos.zip","w") as zip:
    for path in Path().rglob("*.*"):
        #print(path)
        if str(path) != "10-archivos/comprimidos.zip":
            zip.write(path)

print("------------------LECTURA-------------------")
#leer un zipfile

with ZipFile("10-archivos/comprimidos.zip","r") as zip:
    print(zip.namelist())   #muestra todos los archivos que se encuentran en el comprimido
    info= zip.getinfo("10-archivos/comprimidos.zip") #Muestra la informacion del archivo
    print(info.file_size,
        info.compress_size,
        info.compress_level
    )

#Extraer archivos de un zip:
with ZipFile("10-archivos/comprimidos.zip") as zip:
    zip.extractall("10-archivos/descomprimidos")