buscar = 15

for numero in range(10):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontre el numero buscado")


texto = "Ultimate Python"

for char in texto:
    print(char)
