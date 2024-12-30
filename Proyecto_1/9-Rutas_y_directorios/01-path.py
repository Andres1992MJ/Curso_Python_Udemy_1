from pathlib import Path

                #Esto son solo referencias, no necesariamente la ruta debe existir:
# Path(r"C:\Users\Andres Medina\Desktop\UDEMY\Curso_Python") <---- esta es la forma para windows
# Path()
# Path.home()   <---- esta es la carpeta de inicio del usuario

path= Path(r"hola-mundo\mi-archivo.py")


print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.absolute())
