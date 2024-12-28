class Mi_Error(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo):
        self.mensaje =mensaje
        self.codigo =codigo
    
    def __str__(self):
        return f"{self.mensaje} -- codigo: {self.codigo}"


def dividir(n=0):
    if n == 0:
        raise Mi_Error("No se puede dividir por 0", 808)
    return 5/n

try:
    dividir()
except Mi_Error as e:
    print(e)