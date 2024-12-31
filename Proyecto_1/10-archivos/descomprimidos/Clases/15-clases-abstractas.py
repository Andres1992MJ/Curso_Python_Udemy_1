from abc import ABC, abstractmethod

class Model(ABC):
    

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")
    @property
    @abstractmethod    
    def tabla(self):
        pass
    
    def guardar(self):
        print(f"Guardando {self.tabla} en BDD")
    @classmethod
    def buscar_por_id(self, _id):
        print(f" Buscando usuario por con ID {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

mi_usuario_1= Usuario()

mi_usuario_1.guardar()
Usuario.buscar_por_id(34)