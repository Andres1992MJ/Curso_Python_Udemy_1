from pathlib import Path

#Importante, aca me tuve que salir en la terminal con CD hasta 
# PS C:\Users\Andres Medina\Desktop\UDEMY\Curso_Python\Proyecto_1
#porque no servia en el directorio en el que estaba, CUIDADO !!!!

path= Path("9-Rutas_y_directorios")

#path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("Gordito-feliz")

# print(path.exists())
# print(Path.cwd())

print(path.iterdir())

for p in path.iterdir():
    print(p)                  #<---- 


print("-----------------------")

archivos = [p for p in path.iterdir() if not p.is_dir()] #<--- Esto imprime todos los archivos en el directorio que no sean un directorio "carpeta"
archivos2 = [p for p in path.glob("*.py")]  #Imprime solo los que tengan la extencion en el directorio
archivos3 = [p for p in path.glob("01-*.py")] #Imprime solo los archivos que tengan 01 al inicio, claramente esto puede ser cualquier cosa
archivos4 = [p for p in path.glob("**/*.py")] #imprime todos los archivos que se encuentren en el directorio principal y subcarpetas
archivos5 = [p for p in path.rglob("*.py")] #Lo mismo que el anterior pero con otra sintaxis
print("1-----------------------")
print(archivos)
print("2-----------------------")
print(archivos2)
print("3-----------------------")
print(archivos3)
print("4-----------------------")
print(archivos4)
print("5-----------------------")
print(archivos5)