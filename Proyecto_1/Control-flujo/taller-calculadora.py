operacion = ""
numero1= ""
numero2= ""
acumulado= 0


print("""Bienvenidos a la calculadora
Para salir escribe Salir
Las operaciones son suma, resta, multi, div""")

while True:
    if numero1 == "":
        numero1 = int(input("Ingrese el pirmer numero: "))
        operacion = input("Ingrese la operacion: ").lower()
        if operacion == "salir":
            break
        numero2 = int(input("Ingrese el segundo numero: "))
        if operacion == "suma":
            acumulado = numero1 + numero2 
        if operacion == "resta":
            acumulado = numero1 - numero2 
        if operacion == "multi":
            acumulado = numero1 * numero2 
        if operacion == "div":
            acumulado = numero1 / numero2 
        print(f"""El resultado es: {acumulado}""")
    else:
        operacion = input("Ingrese la operacion: ").lower()
        if operacion == "salir":
            break
        numero2 = int(input("Ingrese el segundo numero: "))
        if operacion == "suma":
            acumulado = acumulado + numero2 
        if operacion == "resta":
            acumulado = acumulado - numero2 
        if operacion == "multi":
            acumulado = acumulado * numero2 
        if operacion == "div":
            acumulado = acumulado / numero2
        print(f"""El resultado es: {acumulado}""") 

    
     

