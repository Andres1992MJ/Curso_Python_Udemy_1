class Perro:
    patas= 4
    def __init__(self, nombre_P, edad_P):   #Parametros
        self.nombre_A =nombre_P              #Esto se llama atributo
        self.edad_A = edad_P                 #Esto tambien es un atributo, porque son propiedades de una clase
        
    def habla(self):    
        print(f"{self.nombre_A} dice: Guau!!!")


mi_perro1 = Perro("Nessme",10)
mi_perro2 = Perro("Gordito",11)

print(mi_perro1.nombre_A)
print(mi_perro2.nombre_A)

mi_perro1.habla()
print(Perro.patas)

print(mi_perro1.patas)

Perro.patas= 3 #Modifica el valor Global de las patas de la clase perro
mi_perro2.patas=5 #Modifica la propiedad patas solo en el objeto donde lo estoy asignando

print(mi_perro1.patas)
print(mi_perro2.patas)




#Perro.habla()