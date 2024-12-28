numeros = [2,4,76,8,9,2,11,73,5,34]

numeros.sort()

print(numeros, "SORT_Ordena en orden ascendente")

numeros.sort(reverse=True)

print(numeros, "SORT_REVERSE_TRUE_Ordena en orden descendente")

numeros2 = sorted(numeros)

print(numeros2, "SORTED_Entrega una nueva lista, lo que permite modificar sin afectar la primera")

numeros2 = sorted(numeros, reverse=True)

print(numeros2,"Sorted_REVERSE_tambien se puede ornear la nueva lista en orden descendente")

usuarios =[
    [2,"Andres"],
    [1,"Carolina"],
    [4,"Luz"],
    [3,"Dani"]
]
usuarios.sort()
print(usuarios, "SORT_puede ornenar listas cuando el parentesis esta vacio el id debe estar adelante")

usuarios2 =[
    ["Andres",1],
    ["Carolina", 3],
    ["Luz", 4],
    ["Dani", 2]
]
def ordenar(elemento):
    return elemento[1]

usuarios2.sort(key= ordenar)

print(usuarios2)


usuarios3 =[
    ["Andres",1],
    ["Carolina", 3],
    ["Luz", 4],
    ["Dani", 2]
]

usuarios3.sort(key =lambda el: el[1])

print(usuarios3)

usuarios3.sort(key =lambda el: el[1], reverse=True)

print(usuarios3)