def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


l= largo("Hola a todos")

print(l)