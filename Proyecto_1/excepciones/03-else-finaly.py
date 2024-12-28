try:
    n1=int(input("Ingresa un numero:"))
    #dfsdfhgdgs   // este es un error de NameError
except ValueError as e:
    print("Error, debes ingresar un numero")
else:
    print("No ocurrio un error")
finally:
    print("Se ejecuta siempre")