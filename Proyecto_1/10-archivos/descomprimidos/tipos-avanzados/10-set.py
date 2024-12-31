#Set significa grupo o conjunto

primer = {1,1,1,2,2,2,3,3}

print(primer)  #crea cnjuntos de los datos repetidos y solo muestra 1

primer.add(5)

primer.remove(1)

print(primer)

segundo=[3,3,4,5,5,6,4,7,8]

segundo= set(segundo)  #lo convierte en un set

print(segundo)

print(primer|segundo)  #une los dos sets

print(primer & segundo) #muestra solo los que se comparten en los sets

print(primer - segundo) #muestra solo los datos del primer set que no se repiten en el sewgundo

print(primer ^ segundo ) #muestra los elementos que no se repiten en ninguno de los dos sets


#no se pueden acceder por lo que para buscar algo se deberia buscar con un if

if 7 in segundo:
    print("si se encontro el 7")
else:
    print("no se encontro")

if 20 in segundo:
    print("si se encontro el 7")
else:
    print("no se encontro")