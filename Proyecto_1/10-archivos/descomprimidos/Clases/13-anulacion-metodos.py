class Ave:          #Clase padre
    def vuela(self):
        print("Vuela ave")


class Pato(Ave):     #Subclase que hereda de la clase padre
    def vuela(self):
        print("Vuela Pato")

mi_pato_1 = Pato()

mi_pato_1.vuela()   #Aca reemplaza porque la clase pato reescribe el metodo de la clase padre


class Cuadrupedo:
    def __init__(self):
        self.corre = True

    def correr(self):
        print("Corre Cuadrupedo")

class Perro(Cuadrupedo):
    def __init__(self):
        super().__init__()
        self.trotar= True
       
    def correr(self):
        
        print("Corre Perro")
        super().correr()


mi_perro_1= Perro()

mi_perro_1.correr()

print(mi_perro_1.corre)