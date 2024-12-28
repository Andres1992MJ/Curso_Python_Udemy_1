from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")

class Usuario(Model):
    def guardar(self):
        print("Guardadndo en BBDD")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario_1= Usuario()

sesion_1 = Sesion()


guardar([usuario_1, sesion_1])

