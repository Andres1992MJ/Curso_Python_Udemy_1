class Animal:
    def comer(self):
        print("Comiendo")

class Perro():
    def pasear(self):
        print("Paseando")

class Gato(Animal, Perro):   #La herencia se mantiende de izquierda a derecha es decir la masd fuerte es la izquierda
    def dormir(self):
        print("Durmiendo")

mi_perro = Perro()

#mi_perro.comer()
mi_perro.pasear()

mi_gato = Gato()

mi_gato.comer()
mi_gato.pasear()