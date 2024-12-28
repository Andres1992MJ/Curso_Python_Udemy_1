class Perro():                     #Todos los metodos magicos empiezan con __ y terminan con __
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return f"Clase Perro, con el nombre: {self.nombre}"
    def __del__(self):
        print(f"Chao perrito {self.nombre}")
    def habla(self):    
        print(f"{self.nombre} dice: Guau!!!")
    


mi_perro_1=Perro("Gordo",12)

print(mi_perro_1)

texto= mi_perro_1

print(texto)

del mi_perro_1

print(mi_perro_1.nombre)


