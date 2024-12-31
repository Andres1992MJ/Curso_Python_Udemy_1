class Perro:
    def __init__(self, nombre, edad):  #---> lo que pasamos aca son parametros
        self.nombre =nombre            #A efectos prácticos los atributos no son muy distintos de las 
        self.edad = edad               #variables, la diferencia fundamental es que sólo existen dentro del objeto.
        
    def habla(self):    
        print(f"{self.nombre} dice: Guau!!!")

mi_perro1 = Perro("Nessme",10)
mi_perro2 = Perro("Gordito",11)

print(mi_perro1.nombre)
print(mi_perro2.edad)

mi_perro1.habla()