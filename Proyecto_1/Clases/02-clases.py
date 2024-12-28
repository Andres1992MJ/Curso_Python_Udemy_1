class Perro:    #PascalCase // Upper Camel Case
    def habla(self):    #Esto ya no es una funcion, se llama metodo siempre tendra self
        print("Guau!!!")

mi_perro= Perro()

print(type(mi_perro))

mi_perro.habla()

print(isinstance(mi_perro,Perro))  #Dice si es una instancia de la clase en el sugundo parametro