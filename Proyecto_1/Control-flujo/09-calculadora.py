
resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese el numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese la operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op == "suma":
        resultado += n2
    if op == "resta":
        resultado -= n2
    if op == "multi":
        resultado *= n2
    if op == "div":
        resultado /= n2
    print(f"""El resultado es: {resultado}""")
