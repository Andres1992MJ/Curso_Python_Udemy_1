try:
    n1=int(input("Ingresa un numero:"))
    #dfsdfhgdgs   // este es un error de NameError
except ValueError as e:
    print("Error, debes ingresar un numero")
except NameError as e:
    print("Ocurrio un error")