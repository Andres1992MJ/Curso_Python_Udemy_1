saludo = "Hola mundo global"

print(saludo)


def saludar():
    global saludo
    saludo = "Hola desde la funcion"


saludar()

print(saludo)


def saludar2():
    saludo = "Saludo desde la funcion 2"
    print(saludo)


saludar2()
