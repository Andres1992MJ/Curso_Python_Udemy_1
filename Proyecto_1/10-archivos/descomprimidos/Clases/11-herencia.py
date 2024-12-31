class Animal:
    def comer(self):
        print("Comiendo")

class Perro(Animal):
    def pasear(self):
        print("Paseando")


class Gato(Animal):
    pass
mi_perro = Perro()

mi_perro.comer()
mi_perro.pasear()

mi_gato = Gato()

mi_gato.comer()