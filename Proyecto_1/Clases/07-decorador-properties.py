class Perro():
    def __init__(self,nombre):
        self.nombre=nombre

    @property                          #
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        return 

perro_1 = Perro("Nessme")

print(perro_1.nombre)