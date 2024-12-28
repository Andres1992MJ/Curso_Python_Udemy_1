class Perro:
    patas= 4
    def __init__(self, nombre, edad):
        self.__nombre =nombre              #Esto se llama atributo
        self.__edad = edad                 #Esto tambien es un atributo, porque son propiedades de una clase
    
    
    def habla(self):    
        print(f"{self.__nombre}Dice Guau!!!")

    @classmethod
    def factory(cls):
        return cls("Shaky",9)
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre


mi_perro1 = Perro("Nessme",10)
mi_perro2 = Perro("Gordito",11)
mi_perro3 = Perro.factory()

mi_perro3.habla()
#print(mi_perro3.__nombre)   #Esto falla porque el nombre ahora es privado solo se puede acceder desde adentro
print(mi_perro3.get_nombre())
mi_perro3.set_nombre("Kaiser")
print(mi_perro3.get_nombre())

print(mi_perro2.__dict__)  #Se obtoiene la informacion de como acceder a los atributos privados
print(mi_perro2._Perro__nombre) #Trae el nombre
print(mi_perro2._Perro__edad)

mi_perro2._Perro__nombre = "Otra cosa" #HACK de los privados

print(mi_perro2.get_nombre())
