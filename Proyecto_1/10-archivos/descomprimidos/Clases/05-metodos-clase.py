class Perro:
    patas= 4
    def __init__(self, nombre, edad):
        self.nombre =nombre              #Esto se llama atributo
        self.edad = edad                 #Esto tambien es un atributo, porque son propiedades de una clase
    
    @classmethod    
    def habla(cls):    
        print("Guau!!!")

    @classmethod
    def factory(cls):
        return cls("Shaky",9)


mi_perro1 = Perro("Nessme",10)
mi_perro2 = Perro("Gordito",11)
Perro.habla()
mi_perro3 = Perro.factory()

print(mi_perro3.nombre, mi_perro3.edad)