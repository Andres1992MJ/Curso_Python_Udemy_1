class Produccto:
    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"Producto: {self.nombre}, precio: {self.precio}"
    
class Categoria:
    productos=[]
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)
    
kayak = Produccto("Kayak",1000)
bicicleta = Produccto("bicicleta",2500)
surfboard = Produccto("Surfboard", 600)

deportes = Categoria("Deportes", [kayak,bicicleta])

deportes.imprimir()

deportes.agregar(surfboard)

deportes.imprimir()