numeros=(1,2,3) + (4,5,6)

print(numeros)

punto=tuple([1,2])

print(punto)

menosNumeros=numeros[:2]

print(menosNumeros)

primero, segundo, tercero, *otros =numeros

print(tercero)
print(primero, segundo, tercero, otros)

for n in numeros:
    print(n)

listaNumeros= list(numeros)

listaNumeros[2] = "Hola amor"

print(listaNumeros)



